---
type: adr
status: ACCEPTED
date: 2026-11-02
decision_risk: HIGH
tags: [adr, protocol]
---

# ADR-0001 — Turning the draft into a specification

## Context

The first draft of Grail described the right idea: one envelope, one mechanism, graphs of equal participants, causality and provenance in the substrate, and isolation per user. It was written as a manifesto. It had no wire format, no state machines, no error model, no versioning rule, and several promises that cannot be implemented as written. A protocol that others are meant to implement needs every one of those.

The review compared the draft with the published specifications of agent and tool protocols (task lifecycles, discovery documents, stateless HTTP transports, routing headers), with capability-token designs that support attenuated delegation, with RFC 9457 problem documents, with hybrid logical clocks, and with canonical JSON hashing.

## Decision

Keep the draft's model unchanged and specify it. The changes, each with its reason:

| # | Draft | Specification | Why |
| --- | --- | --- | --- |
| 1 | Prose description of envelope contents. | Exact members, types, limits, and an `x-` rule for unknown members ([[protocol/03-Envelope]]). | Two implementations cannot interoperate on prose. |
| 2 | "Kinds are open." | A registry of reserved kinds with the fabric behavior each triggers; everything else is opaque or `x-`. | An open set with no reserved meaning gives the fabric nothing to enforce. |
| 3 | "Exactly-once" delivery. | `effectively-once`: deduplication by key and digest for at least 24 hours ([[protocol/04-Transfer#4.3 Delivery guarantees]]). | Exactly-once delivery is impossible over a lossy network; the honest contract is one ledger entry per key. |
| 4 | No lifecycle. | A task lifecycle with seven states and an explicit transition table. | "Wait on a causal reply" needs a state to wait on, and illegal transitions need a refusal. |
| 5 | Edges express "permission, ordering, causality". | Two relations: `flow` authorizes, `dependency` orders. Causality lives in `parents`. | One edge type doing three jobs made every rule ambiguous. |
| 6 | "B may only run after A has produced valid output." | Dependency gating: a task is accepted only if a result from each dependency is among its causal ancestors ([[protocol/05-Causality#5.3 Dependency gating]]). | Gives the sentence a checkable meaning without a central scheduler. |
| 7 | Nothing about cycles. | Dependency edges and graph containment must be acyclic; mutations that would close a cycle are refused ([[protocol/06-Graphs#6.3 The acyclicity rule]]). | A cycle of dependencies can never run. Refusing at mutation time is cheap; discovering it at run time is a deadlock. |
| 8 | Graphs are "living". | Revisions, optimistic concurrency, atomic multi-operation mutations, and a ledger entry per mutation. | Concurrent editors of one graph need a conflict rule, and graph history is provenance too. |
| 9 | "Verifiable, append-only provenance." | A hash-linked ledger per scope with canonical digests anyone can recompute ([[protocol/05-Causality#5.4 The ledger]]). | "Verifiable" needs an algorithm. |
| 10 | "Nothing is lost. Information is immortal." | Payload erasure with tombstones that keep digests and links ([[protocol/05-Causality#5.6 Erasure]]). | Keeping personal data forever conflicts with data-protection law. The chain stays verifiable without the content. |
| 11 | "Mathematically enforced isolation." | Per-scope signing keys, verified against the scope a request names, so any cross-scope request is refused before a lookup with the same answer whether its target exists or not ([[protocol/07-Security#7.2 Scope isolation]]). | Isolation must also hide existence, or a probe can enumerate other users. |
| 12 | "Graph-scoped capability tokens." | Tokens with abilities, audience, windows, and attenuated delegation chains with six checks and a depth limit ([[protocol/07-Security#7.5 Delegation]]). | Agents hand work to sub-agents; authority must narrow at every hop, never widen. |
| 13 | Clocks implied. | Hybrid logical clocks with a skew bound, used for ordering in traces but never for causality. | Wall clocks lie; parents do not. |
| 14 | No transport. | Operations with stable identifiers, an HTTP binding, a line binding, and discovery, all read from one contract file ([[protocol/08-Bindings]]). | A protocol without a binding cannot be implemented. Generating both bindings from one file keeps them identical. |
| 15 | No error model. | RFC 9457 problems with an append-only code registry ([[protocol/09-Errors]]). | Clients need stable codes to branch on. |
| 16 | "Zero loss of functionality" for legacy tool messages. | A bridge with an exact mapping and a list of what it does not do ([[protocol/10-Bridge]]). | The claim could not be tested; the mapping can. |
| 17 | Conformance as one sentence. | Profiles, ten required checks, and test vectors ([[protocol/11-Conformance]]). | Conformance must be decidable. |
| 18 | No versioning. | `major.minor` with additive minors and an `x-` extension namespace ([[protocol/12-Evolution]]). | The protocol will change; the rules for change must exist before the first change. |
| 19 | Payload size, counts, depths unbounded. | Limits for every collection, advertised in discovery. | Unbounded inputs are denial of service. |
| 20 | Pull or push unspecified. | Cursor-based pulls with limits; the cursor is the acknowledgement. | Flow control falls out of pulling: a recipient never receives more than it asked for. |

## Rationale

Every change either gives a sentence of the draft a testable meaning or removes a promise no implementation could keep. None removes a concept.

## Consequences

- The reference implementation can be judged against the ten checks of [[protocol/11-Conformance#11.2 Required checks]].
- Push delivery (callbacks, sockets) is left for a minor version; pulls cover every guarantee in 1.0.
- Asymmetric token signatures are an extension in 1.0; scope-key HMAC is the baseline every fabric shares.

## Alternatives

- **Adopt an existing agent protocol's task model wholesale.** Rejected: those models are request-centred between two agents and have no graph, no dependency gating, and no scope ledger.
- **Use a distributed log product's semantics for the ledger.** Rejected: ties the protocol to an implementation; a hash chain is enough and verifiable by anyone.

## Validation

Predicted: every required check of 11.2 has at least one test in the reference suite. Review on 2027-02-01.

## Referenced by

[[protocol/_MOC]] · [[decisions/_MOC]]
