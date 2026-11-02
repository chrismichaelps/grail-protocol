---
type: specification
chapter: 5
tags: [protocol, specification]
---

# 5. Causality and provenance

## 5.1 Clocks

Senders SHOULD stamp envelopes with a hybrid logical clock: `wall` is the sender's physical time in milliseconds, `counter` breaks ties within one millisecond, and `node` identifies the clock's owner. On sending, a participant sets `wall` to the larger of its physical time and its last `wall`, increasing `counter` when `wall` did not move. On receiving, it merges the received clock the same way. The fabric keeps its own clock and MUST NOT accept an envelope whose `wall` is more than 300 000 milliseconds ahead of fabric time (`grail.clock-skew`).

Clocks order concurrent events for people reading a trace. Causality itself is carried by `parents`, never inferred from clocks.

## 5.2 Causal parents

`parents` names the envelopes that this envelope was produced from. Each parent MUST be in the same scope's ledger before the child is accepted, which makes the causal graph of a scope a directed acyclic graph by construction: a child cannot name an envelope accepted after it.

## 5.3 Dependency gating

For a `task` or `tool.call` envelope sent to participant `t` in graph `g`, let `D` be the set of participants `d` such that `g` has a `dependency` edge from `d` to `t`. The envelope is accepted only if, for every `d` in `D`, some envelope of kind `result` or `tool.result` whose `source` is `d` is among the envelope's causal ancestors (its parents, their parents, and so on). Otherwise it is refused with `grail.dependency-unmet`, and the problem lists the unmet participants.

This is how a graph says "B may only run after A has produced a result" without any scheduler: the sender of B's task proves it by naming A's result as a parent.

## 5.4 The ledger

Each scope has one ledger. Each entry holds the envelope's sequence, its digest, its parents' digests, and a link:

```
link(1) = sha256("grail-ledger:" + digest(1))
link(n) = sha256(link(n-1) + ":" + digest(n))
```

where `+` joins lowercase hex strings. A ledger is valid when every link recomputes. Any participant holding a token with the `ledger.read` ability can fetch a range of entries and verify the chain independently.

## 5.5 Trace

The trace of an envelope is the set of its causal ancestors, returned in ledger order with their digests. A trace answers "what information contributed to this?". The fabric MUST omit from a trace any envelope whose `visibility` excludes the caller, and MUST still return its digest and position so the chain stays verifiable.

## 5.6 Erasure

Provenance must not force a fabric to keep personal data forever. A fabric MUST erase the `payload` of an entry when a holder of `ledger.erase` asks (`eraseTransfer`). Erasure removes the payload from storage and marks the entry erased. The digest and link are kept, so the chain still verifies and every child still knows that its parent existed. A trace returns erased entries with `"erased": true` and no payload.

## Referenced by

[[protocol/_MOC]] · [[protocol/02-Model]] · [[protocol/04-Transfer]] · [[domain/Ledger]] · [[domain/Clock]]
