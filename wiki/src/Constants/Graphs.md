---
type: module
path: "@root/src/Constants/Graphs.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Graphs

> @Constants.Graphs.Roles — the roles that carry meaning inside nested graphs

## Purpose

The roles that carry meaning inside nested graphs.

## Interface

### Signatures

```pudu
/// The role whose holders receive what enters a nested graph.
export const ENTRY_ROLE: Str = "entry"
/// The prefix of extension kinds, members, and abilities.
export const EXTENSION_PREFIX: Str = "x-"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Domain/Identifier]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Routing]]

## Referenced by

[[src/Constants/_MOC]] · [[src/Domain/Identifier]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Routing]]
