---
type: module
path: "@root/src/Engine/Causality.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Causality

> @Engine.Causality.Ancestry — the causal ancestors of an envelope

## Purpose

The causal ancestors of an envelope.

## Interface

### Signatures

```pudu
/// Every ancestor of the given parents, each once, in ledger order, up to the contract's bound; a gate that finds no result within the bound refuses, so the bound fails closed.
export fn ancestors(state: &Scope.State, parents: &Array[Str]) -> Array[Ledger.Record]
/// The first task parent, shared by reply admission and nested producer attribution.
export fn taskOf(state: &Scope.State, parents: &Array[Str]) -> Option[Lifecycle.Lifecycle]
/// Verified results identify their direct producer and the enclosing participants on their task's original routes.
export fn producers(state: &Scope.State, parents: &Array[Str]) -> Set[Envelope.Address]
```

### Linkage

- **Requires:** [[src/Constants/Events]] · [[src/Contract/Limits]] · [[src/Domain/Envelope]] · [[src/Domain/Ledger]] · [[src/Domain/Lifecycle]] · [[src/Domain/Scope]] · [[src/Engine/Kinds]]
- **Standard library:** `Std.Option`
- **Consumed by:** [[src/Engine/Admission]] · [[src/Engine/Delivery]] · [[src/Engine/Handoff]]

## Referenced by

[[src/Engine/_MOC]] · [[src/Engine/Admission]] · [[src/Engine/Delivery]] · [[src/Engine/Handoff]]
