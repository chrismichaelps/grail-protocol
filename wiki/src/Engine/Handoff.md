---
type: module
path: "@root/src/Engine/Handoff.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Handoff

> @Engine.Handoff.Portability — assembles, seals, and checks handoffs that carry an agent's context between fabrics

## Purpose

Assembles, seals, and checks handoffs that carry an agent's context between fabrics.

## Interface

### Signatures

```pudu
/// A sealed handoff of the anchors and their causal ancestry. Entries the authority may not read travel withheld: their digest and link prove they exist, their content stays home. Secrets never travel; the handoff names the ones its carried envelopes reference, so the receiving owner can bind its own.
export fn assemble(state: &Scope.State, origin: &Handoff.Origin, member: &Graph.Participant, asked: &Handoff.Asked, authority: &Capability.Authority, issued: Int, secret: Str) -> Result[Json.Json, Problem.Problem]

/// Whether one handoff may carry this many entries.
export fn carries(count: Int) -> Bool

/// The digest of a handoff: the hash of its canonical form without its digest and seal.
export fn digestOf(bundle: &Json.Json) -> Str

/// The seal a fabric gives a digest for one of its scopes. Only a fabric holding the same secret can make or check it.
export fn sealOf(secret: Str, scopeId: Str, digest: Str) -> Str

/// Whether this fabric sealed the handoff, for the scope it was shown under.
export fn attested(bundle: &Json.Json, secret: Str, scopeId: Str) -> Bool

/// The number of entries a handoff carries, when its digest, every envelope digest, every link, its ancestry, and its anchors all hold.
export fn intact(bundle: &Json.Json) -> Result[Int, Problem.Problem]

/// Whether a handoff's import window closed before `now`.
export fn expired(bundle: &Json.Json, now: Int) -> Bool

/// What the ledger records about a handoff that moved in a direction: its id, digest, origin, anchors, and how many entries it carried.
export fn summary(bundle: &Json.Json, direction: Str, entries: Int) -> Json.Json
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Fabric]] · [[src/Constants/Handoff]] · [[src/Constants/Ledger]] · [[src/Contract/Limits]] · [[src/Contract/Members]] · [[src/Contract/Problems]] · [[src/Domain/Capability]] · [[src/Domain/Graph]] · [[src/Domain/Handoff]] · [[src/Domain/Ledger]] · [[src/Domain/Problem]] · [[src/Domain/Scope]] · [[src/Engine/Causality]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Custody]] · [[src/Engine/Delivery]] · [[src/Engine/Ledger]] · [[src/Utils/Canonical]] · [[src/Utils/JsonRead]] · [[src/Utils/Pointer]]
- **Standard library:** `Std.Bytes`, `Std.Crypto`, `Std.Json`, `Std.List`, `Std.Option`
- **Consumed by:** [[src/Services/Handoffs]] · [[test/Engine/HandoffTest]] · [[test/Security/CustodyTest]] · [[test/Security/HandoffTest]]

## Referenced by

[[src/Engine/_MOC]] · [[src/Services/Handoffs]] · [[test/Engine/HandoffTest]] · [[test/Security/CustodyTest]] · [[test/Security/HandoffTest]]
