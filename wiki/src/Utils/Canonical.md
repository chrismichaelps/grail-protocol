---
type: module
path: "@root/src/Utils/Canonical.pudu"
layer: 1
grammar: "[[grammar/pudu]]"
tags: [module, utils]
---

# Utils.Canonical

> @Utils.Canonical.Form — one JSON text per value, so equal values hash equally

## Purpose

One JSON text per value, so equal values hash equally.

## Interface

### Signatures

```pudu
/// The value with every object's members sorted by key, at every depth.
export fn sorted(value: &Json.Json) -> Json.Json
/// The canonical text of a value: sorted members and no insignificant whitespace.
export fn text(value: &Json.Json) -> Str { Json.encode(&sorted(value)) }
/// The value without the named top-level members.
export fn without(value: &Json.Json, names: &Array[Str]) -> Json.Json
```

### Linkage

- **Requires:** nothing inside the fabric
- **Standard library:** `Std.Json`
- **Consumed by:** [[src/Engine/Authority]] · [[src/Engine/Erasure]] · [[src/Engine/Ledger]] · [[test/Engine/LedgerTest]]

## Referenced by

[[src/Engine/Authority]] · [[src/Engine/Erasure]] · [[src/Engine/Ledger]] · [[src/Utils/_MOC]] · [[test/Engine/LedgerTest]]
