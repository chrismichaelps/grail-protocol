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

Forging a token failed in every form tried: claims rewritten under another token's signature, a missing signature, an extra segment, a token sixty thousand characters long, and a delegated token whose abilities were widened after signing. A token from one scope was refused in another with exactly the same answer whether the target existed or not, and the time to answer differed by less than a millisecond, so scopes cannot be enumerated by status or by timing. A subagent could not delegate, widen a delegation, move it to another graph, outlive its parent, send as another participant, read another inbox, change the graph, erase, or revoke a token it did not issue. Identifiers carrying path traversal, spaces, header injection, or non-ASCII letters were refused before they reached anything that could misuse them. A body nested twenty thousand levels deep was refused without harming the server, and an oversized payload was answered `grail.too-large`. Cross-origin reads were never granted to an unlisted origin. A stranger could neither answer nor cancel a task, an unsolicited JSON-RPC response was refused rather than attached to something, and batched JSON-RPC was refused.

## What broke, and how it was fixed

**Ledger poisoning through reserved ids.** The fabric records each graph change in the ledger under an id of the form `mutation:<graph>@<revision>`. A sender could submit an envelope with the next such id before the change happened, and the fabric would later overwrite that record, corrupting the ledger's sequence. Ids beginning with `mutation:` are now reserved for the fabric and refused from senders ([[protocol/07-Security#7.7 Resource bounds]]).

**Quadratic cycle detection.** Creating the largest legal graph took 22 seconds, and the store's lock was held the whole time, so one request could freeze every scope on the fabric. Cycle detection computed reachability from every node. It now orders the graph topologically in linear time and, only when that fails, walks predecessors among the leftover nodes to name one cycle ([[src/Engine/Topology]]). The same graph is created in 0.7 seconds and a cycle through all 1024 participants is found in 0.07 seconds.

**Rate limiting that never limited.** A flood of 800 requests in under a second was answered in full. The standard guard keyed each window by the peer's address and port, and every new connection has a new port, so every connection started a fresh window. Peers are now named by host before the limiter sees them ([[src/Web/Peers]]); the same flood is now cut at the window's limit. The defect belongs to the standard library and is recorded on [[grammar/pudu#Known compiler issues]] for upstream.

**Workers exhausted by waiting pulls.** Long pulls let a participant anywhere receive work without the fabric ever calling it, but forty waiting pulls held every worker and a discovery request took fifteen seconds. Waiting pulls may now hold at most half the workers; beyond that a pull answers immediately and the client simply pulls again, and the default worker count rose to 64 ([[src/Services/Runtime]]). With 48 pulls held open, discovery answers in 7 milliseconds.

**Unbounded growth.** Delivery keys were never forgotten and a scope's ledger could grow without limit in memory. Keys older than the deduplication window are now dropped as each envelope is committed, live keys and ledger entries per scope are bounded by the contract, and the walk of ancestry that gates a task is bounded too, failing closed so that a dependency hidden beyond the bound is treated as unmet ([[src/Engine/Admission]], [[src/Engine/Causality]]).

**Responses that did not match the specification.** An oversized payload was answered `grail.invalid` instead of `grail.too-large`, and revocation and erasure were specified but could not be invoked. Both operations now exist in the contract ([[protocol/08-Bindings#8.1 Operations]]), and payload size is checked before shape.

## Mutation testing as an attack on the tests

The suites themselves were attacked with [[tools/Mutate]], which changes one operator at a time in the engines and requires some test to fail. Surviving mutants pointed at untested boundaries (a deadline equal to now, a clock exactly at the skew bound, a delegation chain exactly at its depth limit, containment exactly at its depth limit) and at dead code, which was removed rather than tested. [[src/Engine/Authority]] kills every mutant.

## Limits of this campaign

The siege runs from one host, so it measures per-host limiting and worker exhaustion, not a distributed flood; a fabric facing the open internet still belongs behind a network-level shield. The store is in memory, so durability under crash is out of scope until [[seams/ScopeStore]] gains a durable adapter.

## Referenced by

[[architecture/_MOC]] · [[architecture/SECURITY]] · [[test/Security/AttackTest]] · [[tools/Siege]]
