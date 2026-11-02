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
/// The participants of a graph that produced a result among the ancestors of the given parents.
export fn producers(state: &Scope.State, parents: &Array[Str], graph: Str) -> Set[Str]
```

### Linkage

- **Requires:** [[src/Constants/Events]] · [[src/Contract/Limits]] · [[src/Domain/Ledger]] · [[src/Domain/Scope]] · [[src/Engine/Kinds]]
- **Consumed by:** [[src/Engine/Admission]] · [[src/Engine/Delivery]]

## Referenced by

[[src/Engine/Admission]] · [[src/Engine/Delivery]] · [[src/Engine/_MOC]]
