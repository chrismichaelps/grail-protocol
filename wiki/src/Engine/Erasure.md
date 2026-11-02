---
type: module
path: "@root/src/Engine/Erasure.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Erasure

> @Engine.Erasure.Payloads — removes a payload while the chain still proves it existed

## Purpose

Removes a payload while the chain still proves it existed.

## Interface

### Signatures

```pudu
/// The scope with one record's payload removed and the record marked erased; its digest and link are untouched.
export fn erase(state: &Scope.State, id: Str) -> Result[(Ledger.Record, Scope.State), Problem.Problem]
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Contract/Members]] · [[src/Contract/Problems]] · [[src/Domain/Envelope]] · [[src/Domain/Ledger]] · [[src/Domain/Problem]] · [[src/Domain/Scope]] · [[src/Utils/Canonical]]
- **Standard library:** `Std.Option`
- **Consumed by:** [[src/Services/Fabric]]

## Referenced by

[[src/Engine/_MOC]] · [[src/Services/Fabric]]
