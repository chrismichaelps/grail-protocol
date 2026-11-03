---
type: module
path: "@root/src/App/Resilience.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, app]
---

# App.Resilience

> @App.Resilience.Guards — every message runs under a concurrency limit and a deadline; a waiting pull's deadline covers its wait

## Purpose

Every message runs under a concurrency limit and a deadline; a waiting pull's deadline covers its wait.

## Interface

### Signatures

```pudu
/// The guard of one kind's answers: a bounded number at once, a bounded queue, and a deadline.
export fn guard[R]() -> Result[Pipeline.Pipeline[R, Messaging.Failure[Problem.Problem]], Str]
/// The guard of a kind whose answers may take up to `millis`.
export fn guardFor[R](millis: Int) -> Result[Pipeline.Pipeline[R, Messaging.Failure[Problem.Problem]], Str]
/// A guard for every message kind.
export fn registrations(kinds: &Messages.Kinds) -> Result[Array[Registration.Registration], Str]
```

### Linkage

- **Requires:** [[src/App/Messages]] · [[src/Constants/Server]] · [[src/Contract/Limits]] · [[src/Domain/Problem]]
- **Packages:** `PuduLangMediator`, `PuduLangResilience`
- **Standard library:** `Std.Result`
- **Consumed by:** [[src/App/Assembly]]

<!-- authored -->
## Grill Log

- **Q:** What does resilience mean for an in-process message? **A:** A concurrency limit with a bounded queue, and a deadline. **Rationale:** retries belong to callers of remote fabrics ([[src/Api/Peer]]); inside the fabric the risk is overload and runaway work. A refusal answers `grail.backpressure` with a retry hint. **Rejected:** retrying admission, which is deterministic.
<!-- /authored -->

## Referenced by

[[src/App/Assembly]] · [[src/App/_MOC]]
