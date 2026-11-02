---
type: architecture
status: ACTIVE
tags: [architecture, security, testing]
aliases: [Attack campaign, Stress testing]
---

# Attack and stress campaign

The protocol was attacked the way an outsider would attack a public fabric: with no knowledge of the secret, with valid but narrow tokens, with malformed and oversized input, and with sheer volume. Every attack that matters now runs on every change, in two places. [[test/Security/AttackTest]] drives the real router in process with each `pudu test`, and [[tools/Siege]] presses a live server over the network.

```bash
pudu test test
pudu run tools/Siege.pudu --fabric http://127.0.0.1:7420 --token "$(pudu run src/Main.pudu token --scope siege --id root)"
```

## What held from the start

Forging a token failed in every form tried: claims rewritten under another token's signature, a missing signature, an extra segment, a token sixty thousand characters long, and a delegated token whose abilities were widened after signing. A token from one scope was refused in another with exactly the same answer whether the target existed or not, and the local time to answer differed by less than a millisecond. Equal responses prevent status-based enumeration; these timing samples alone do not establish the absence of a timing side channel. A subagent could not delegate, widen a delegation, move it to another graph, outlive its parent, send as another participant, read another inbox, change the graph, erase, or revoke a token it did not issue. Identifiers carrying path traversal, spaces, header injection, or non-ASCII letters were refused before they reached anything that could misuse them. A body nested twenty thousand levels deep was refused without harming the server, and an oversized payload was answered `grail.too-large`. Cross-origin reads were never granted to an unlisted origin. A stranger could neither answer nor cancel a task, an unsolicited JSON-RPC response was refused rather than attached to something, and batched JSON-RPC was refused.

## What broke, and how it was fixed

**Ledger poisoning through reserved ids.** The fabric records each graph change in the ledger under an id of the form `mutation:<graph>@<revision>`. A sender could submit an envelope with the next such id before the change happened, and the fabric would later overwrite that record, corrupting the ledger's sequence. Ids beginning with `mutation:` are now reserved for the fabric and refused from senders ([[protocol/07-Security#7.7 Resource bounds]]).

**Quadratic cycle detection.** Creating the largest legal graph took 22 seconds, and the store's lock was held the whole time, so one request could freeze every scope on the fabric. Cycle detection computed reachability from every node. It now orders the graph topologically in linear time and, only when that fails, walks predecessors among the leftover nodes to name one cycle ([[src/Engine/Topology]]). The same graph is created in 0.7 seconds and a cycle through all 1024 participants is found in 0.07 seconds.

**Rate limiting that never limited.** A flood of 800 requests in under a second was answered in full. The standard guard keyed each window by the peer's address and port, and every new connection has a new port, so every connection started a fresh window. Peers are now named by host before the limiter sees them ([[src/Web/Peers]]); the same flood is now cut at the window's limit. The defect belongs to the standard library and is recorded on [[grammar/pudu#Known compiler issues]] for upstream.

**Workers exhausted by waiting pulls.** Long pulls let a participant anywhere receive work without the fabric ever calling it, but forty waiting pulls held every worker and a discovery request took fifteen seconds. Waiting pulls may now hold at most half the workers; beyond that a pull answers immediately and the client simply pulls again, and the default worker count rose to 64 ([[src/Services/Runtime]]). With 48 pulls held open, discovery answers in 7 milliseconds.

**Unbounded growth.** Delivery keys were never forgotten and a scope's ledger could grow without limit in memory. Keys older than the deduplication window are now dropped as each envelope is committed, live keys and ledger entries per scope are bounded by the contract, and the walk of ancestry that gates a task is bounded too, failing closed so that a dependency hidden beyond the bound is treated as unmet ([[src/Engine/Admission]], [[src/Engine/Causality]]).

**Responses that did not match the specification.** An oversized payload was answered `grail.invalid` instead of `grail.too-large`, and revocation and erasure were specified but could not be invoked. Both operations now exist in the contract ([[protocol/08-Bindings#8.1 Operations]]), and payload size is checked before shape.

## Mutation testing as an attack on the tests

The suites themselves were attacked with [[tools/Mutate]], which changes one operator at a time in the engines and requires some test to fail. Surviving mutants pointed at untested boundaries (a deadline equal to now, a clock exactly at the skew bound, a delegation chain exactly at its depth limit, containment exactly at its depth limit) and at dead code, which was removed rather than tested. [[src/Engine/Authority]] kills every mutant.

### Engine sweep on 2026-11-02

The five unfinished engine sweeps attempted 64 mutants against the full suite in an isolated copy. Initial results were:

| Engine | Mutants | Killed initially | Survived initially |
| --- | --- | --- | --- |
| Mutations | 18 | 17 | 1 |
| Delivery | 30 | 29 | 1 |
| Kinds | 3 | 3 | 0 |
| Topology | 12 | 9 | 3 |
| Erasure | 1 | 1 | 0 |

All five survivors were missing-test cases. The mutation bound lacked an assertion accepting exactly the maximum edge count. Delivery traces lacked assertions distinguishing visible and hidden ancestors. Cycle witnesses lacked a graph with an acyclic path feeding into a cycle, which exposed incorrect incoming counts, incorrect count decrements, and an invalid ready-queue index.

The added regressions pass on the original engines, and targeted reruns kill each of the five surviving source changes. Production engines were unchanged. These targeted reruns supplement the initial sweeps; a second complete sweep was not run. Nonterminating mutants are counted as killed when the harness timeout expires. With the proxy regressions included, the final suite holds 200 assertions; the layer gate still reports 84 modules, 392 internal edges, no refused imports, and no cycles.

## Tunnel validation on 2026-11-02

A temporary Cloudflare Tunnel targeted a fresh fabric bound to `127.0.0.1`, with `GRAIL_CLIENT_IP_HEADER=CF-Connecting-IP`, 64 workers, and a new random secret. The edge response carried `cf-ray`. Both the tunnel and the fabric were stopped after the campaign. The header setting defaults to empty; when enabled, the trusted proxy must overwrite it and provide the fabric's sole ingress. Missing or blank header values fall back to the connection host ([[src/Web/Peers]]).

The earlier run passed 43 of 45 checks. Two delegation checks had expired after only one second and reached validity-window validation before the intended authority check. Giving those requests two minutes of remaining validity produced the expected `grail.forbidden` responses for both ability widening and graph changes.

The repeat passed 44 of 45 checks. All non-timing checks passed; the remaining timing threshold is discussed below.

| Measurement | Repeat result |
| --- | --- |
| Largest legal graph, 1024 participants | created in 7.09 s |
| Cycle through 1024 participants | refused in 0.45 s |
| Discovery while 40 pulls wait | answered in 0.73 s |
| Flood, 1200 requests in 30.3 s | 600 answered, 600 rate limited, no transport failures |
| Flood latency | median 0.412 s, 95th percentile 0.870 s |
| Scope-refusal timing medians | existing 341.2 ms, missing 309.1 ms |

The timing probe collected the two groups sequentially and applied a fixed 20 ms threshold. It failed on the repeat but passed on an earlier run with medians of 247.8 ms and 241.5 ms. These uncontrolled internet measurements neither demonstrate a timing leak nor establish its absence. A controlled, interleaved experiment remains necessary before making a timing-isolation claim. The repeat also required resolving the temporary hostname through `1.1.1.1` after local resolution failed; TLS hostname verification remained enabled.

An independent local HTTP check exercised the rate-limit boundary without internet timing: the first 600 requests succeeded and the next returned 429. With forwarding disabled, changing the supplied header still returned 429. With the trusted header configured, another address had a separate window and received 200. In-process regressions cover disabled forwarding, case-insensitive lookup, IPv6, whitespace trimming, and missing or blank header fallback.

## Nested composition regressions

The composition audit reproduced an entry dependency bypass through a graph participant and a valid inner result that could not satisfy the enclosing team's dependency. Both are fixed by retained admission-time paths and graph-qualified producers ([[decisions/ADR-0008-composable-causal-gates]]). The 18-case composition suite passes. Five selected source mutations are killed: checking only outer gates, dropping enclosing producer credit, crediting the wrong recipient path, rejecting the exact path limit, and accepting a partial expansion with an empty branch. These selected mutations cover the changed contracts; they are not a full new engine sweep.

## Limits of this campaign

The siege runs from one host, so it measures per-host limiting and worker exhaustion, not a distributed flood; a fabric facing the open internet still belongs behind a network-level shield. The store is in memory, so durability under crash is out of scope until [[seams/ScopeStore]] gains a durable adapter.

## Referenced by

[[architecture/_MOC]] · [[architecture/SECURITY]] · [[test/Security/AttackTest]] · [[tools/Siege]]
