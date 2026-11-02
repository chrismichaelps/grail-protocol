---
type: module
path: "@root/src/Engine/Admission.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Admission

> @Engine.Admission.Gate — decides whether one envelope enters a scope, and what it changes

## Purpose

Decides whether one envelope enters a scope, and what it changes.

## Interface

### Signatures

```pudu
export type Admitted = { record: Ledger.Record, lifecycle: Option[Lifecycle.Lifecycle], closes: Option[Str] }
export type Outcome
/// Whether `envelope`, whose body is `body`, enters the scope under `authority` at `now`.
export fn admit(state: &Scope.State, envelope: &Envelope.Envelope, body: &Json.Json, authority: &Capability.Authority, now: Int) -> Result[Outcome, Problem.Problem]
/// The scope after an admitted envelope is appended.
export fn commit(state: &Scope.State, admitted: &Admitted) -> Scope.State
/// A lifecycle's state as of `now`: an unfinished task whose deadline passed has expired.
export fn stateAt(lifecycle: &Lifecycle.Lifecycle, now: Int) -> Str
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Extras]] · [[src/Constants/Fabric]] · [[src/Constants/Ledger]] · [[src/Constants/Security]] · [[src/Contract/Limits]] · [[src/Contract/Members]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Domain/Envelope]] · [[src/Domain/Graph]] · [[src/Domain/Ledger]] · [[src/Domain/Lifecycle]] · [[src/Domain/Problem]] · [[src/Domain/Scope]] · [[src/Engine/Authority]] · [[src/Engine/Causality]] · [[src/Engine/Gating]] · [[src/Engine/Kinds]] · [[src/Engine/Ledger]] · [[src/Engine/Lifecycle]] · [[src/Engine/Routing]] · [[src/Utils/JsonRead]] · [[src/Utils/Pointer]]
- **Standard library:** `Std.Json`, `Std.List`, `Std.Map`, `Std.Option`
- **Consumed by:** [[src/Engine/Journal]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[test/Engine/AdmissionTest]] · [[test/Support/Fixtures]]

<!-- authored -->
## Algorithm

1. Read the kind's behavior from [[src/Engine/Kinds]] once; compute the digest of the body as sent.
2. Refuse an unsupported version, an envelope whose scope differs from the token's, a token without `transfer.send` on the graph, a source the token does not act for, and a kind the fabric writes itself.
3. For `effectively-once`, look the key up: the same digest answers the original record (`Repeated`), another digest is `grail.key-reused`.
4. Refuse a reused id, a missing graph, a source outside the graph, a passed deadline, a clock too far ahead, and any parent not in the ledger.
5. Plan delivery. An answer or a cancellation finds the task's lifecycle among its parents, checks the sender is a recipient (or the source, for a cancellation), advances the lifecycle through [[src/Engine/Lifecycle]], and is routed back to the task's source. Everything else is resolved by [[src/Engine/Routing]], stream fragments are checked against their open stream, and a gated kind must find a result from every dependency among its ancestors ([[src/Engine/Causality]], [[src/Engine/Gating]]).
6. Stamp the record with the next sequence, the digest, and the link after the scope's last link.

`commit` applies an admitted record: ledger, sequence, link, lifecycle, delivery key, and closed stream, all at once.

## Negative Logic

- ❌ Never read the payload to decide routing, gating, or a lifecycle; only a bridged message's JSON-RPC shape is inspected, and only through [[src/Engine/Kinds]].
- ❌ Never consult the clock here; `now` is an argument so admission stays pure and testable.
- ❌ Never append anything when any step refuses.

## Grill Log

- **Q:** Should answers need a return flow edge? **A:** No; they travel back to the task's source and are authorized by being a recipient. **Rationale:** a request edge then implies its reply, and an answer from inside a nested graph can reach the outer participant that asked. **Rejected:** requiring a reverse edge for every request edge.
- **Q:** Where does a repeated delivery key stop? **A:** Before the duplicate-id check. **Rationale:** a retry of an effectively-once send reuses its id on purpose and must get its original receipt. **Rejected:** treating every repeated id as a duplicate.
- **Q:** Expire tasks with a timer? **A:** No; a lifecycle past its deadline reads as `expired` (`stateAt`), and moving it is refused from there. **Rationale:** no background work, same observable result. **Rejected:** a sweeper thread.
<!-- /authored -->

## Referenced by

[[src/Engine/Journal]] · [[src/Engine/_MOC]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[test/Engine/AdmissionTest]] · [[test/Support/Fixtures]]
