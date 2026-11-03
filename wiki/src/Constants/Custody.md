---
type: module
path: "@root/src/Constants/Custody.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Custody

> @Constants.Custody.Sealing — labels of the custody key and of what each sealed value is bound to

## Purpose

Labels of the custody key and of what each sealed value is bound to.

## Interface

### Signatures

```pudu
/// The label mixed into the key a scope's secrets are sealed with.
export const KEY_LABEL: Str = "grail-custody:"

/// What joins the scope, name, and version a sealed value is bound to.
export const BINDING_JOIN: Str = "/"

/// The quote marks a JSON-escaped value is wrapped in, trimmed before searching for it.
export const QUOTE_LENGTH: Int = 1
```

### Linkage

- **Requires:** nothing in `src/`
- **Consumed by:** [[src/Engine/Custody]]

## Referenced by

[[src/Constants/_MOC]] · [[src/Engine/Custody]]
