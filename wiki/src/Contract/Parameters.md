---
type: module
path: "@root/src/Contract/Parameters.pudu"
layer: 0
generated: true
grammar: "[[grammar/pudu]]"
tags: [module, contract]
---

# Contract.Parameters

> @Contract.Parameters.Generated — the name of every path and query parameter

## Purpose

The name of every path and query parameter. Projected from the contract by [[tools/Contract]]; it is regenerated, never edited, and the contract check fails when it is stale.

## Interface

### Signatures

```pudu
/// The `scope` parameter.
export const SCOPE: Str = "scope"
/// The `graph` parameter.
export const GRAPH: Str = "graph"
/// The `transfer` parameter.
export const TRANSFER: Str = "transfer"
/// The `participant` parameter.
export const PARTICIPANT: Str = "participant"
/// The `after` parameter.
export const AFTER: Str = "after"
/// The `limit` parameter.
export const LIMIT: Str = "limit"
/// The `wait` parameter.
export const WAIT: Str = "wait"
/// The `token` parameter.
export const TOKEN: Str = "token"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Web/Caller]] · [[src/Web/Handlers]]

## Referenced by

[[src/Contract/_MOC]] · [[src/Web/Caller]] · [[src/Web/Handlers]]
