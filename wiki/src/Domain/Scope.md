---
type: module
path: "@root/src/Domain/Scope.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Scope

> @Domain.Scope.State — everything one scope holds, and nothing of any other

## Purpose

Everything one scope holds, and nothing of any other.

## Interface

### Signatures

```pudu
export type Keyed = { id: Str, digest: Str, accepted: Int }
export type State = { … }
/// A scope with nothing in it.
export fn empty(id: Str) -> State
/// The number of entries in the scope's ledger.
export fn length(state: &State) -> Int { state.sequence.length() }
/// The record at a ledger position, starting at 1.
export fn recordAt(state: &State, position: Int) -> Option[Ledger.Record]
```

### Linkage

- **Requires:** [[src/Domain/Custody]] · [[src/Domain/Graph]] · [[src/Domain/Handoff]] · [[src/Domain/Ledger]] · [[src/Domain/Lifecycle]]
- **Standard library:** `Std.Map`
- **Consumed by:** [[src/Engine/Admission]] · [[src/Engine/Bridge]] · [[src/Engine/Causality]] · [[src/Engine/Custody]] · [[src/Engine/Delivery]] · [[src/Engine/Erasure]] · [[src/Engine/Handoff]] · [[src/Engine/Journal]] · [[src/Services/Bridge]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Services/Store]] · [[test/Engine/AdmissionTest]] · [[test/Engine/CustodyTest]] · [[test/Engine/DeliveryTest]] · [[test/Support/Fixtures]]

## Referenced by

[[src/Domain/_MOC]] · [[src/Engine/Admission]] · [[src/Engine/Bridge]] · [[src/Engine/Causality]] · [[src/Engine/Custody]] · [[src/Engine/Delivery]] · [[src/Engine/Erasure]] · [[src/Engine/Handoff]] · [[src/Engine/Journal]] · [[src/Services/Bridge]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Services/Store]] · [[test/Engine/AdmissionTest]] · [[test/Engine/CustodyTest]] · [[test/Engine/DeliveryTest]] · [[test/Support/Fixtures]]
