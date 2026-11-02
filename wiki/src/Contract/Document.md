---
type: module
path: "@root/src/Contract/Document.pudu"
layer: 0
generated: true
grammar: "[[grammar/pudu]]"
tags: [module, contract]
---

# Contract.Document

> @Contract.Document.Generated — the contract document served to clients

## Purpose

The contract document served to clients. Projected from the contract by [[tools/Contract]]; it is regenerated, never edited, and the contract check fails when it is stale.

## Interface

### Signatures

```pudu
/// The whole contract as compact JSON.
export const TEXT: Str
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Cli/Commands]] · [[src/Web/Handlers]]

## Referenced by

[[src/Cli/Commands]] · [[src/Contract/_MOC]] · [[src/Web/Handlers]]
