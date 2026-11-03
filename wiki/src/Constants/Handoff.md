---
type: module
path: "@root/src/Constants/Handoff.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Handoff

> @Constants.Handoff.Portability — labels and directions of portable handoffs

## Purpose

Labels, prefixes, and directions of portable handoffs.

## Interface

### Signatures

```pudu
/// The label mixed into the key a fabric seals its handoffs with.
export const SEAL_KEY_LABEL: Str = "grail-handoff:"
/// A handoff this scope sealed and sent.
export const EXPORTED: Str = "export"
/// A handoff this scope received from elsewhere.
export const IMPORTED: Str = "import"
/// The member of a recorded handoff naming the direction it moved in.
export const DIRECTION_MEMBER: Str = "direction"
/// The member of a recorded handoff counting the entries it carried.
export const ENTRIES_MEMBER: Str = "entries"
```

### Linkage

- **Requires:** nothing in `src/`
- **Consumed by:** [[src/Engine/Handoff]] · [[src/Services/Handoffs]]

## Referenced by

[[src/Constants/_MOC]] · [[src/Engine/Handoff]] · [[src/Services/Handoffs]]
