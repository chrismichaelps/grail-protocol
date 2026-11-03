---
type: module
path: "@root/src/Utils/Pointer.pudu"
layer: 1
grammar: "[[grammar/pudu]]"
tags: [module, utils]
---

# Utils.Pointer

> @Utils.Pointer.Paths — JSON pointers to the members a violation names

## Purpose

JSON pointers to the members a violation names.

## Interface

### Signatures

```pudu
/// The pointer to a nested member, from the root.
export fn of(segments: &Array[Str]) -> Str { segments.map(|segment: Str| Text.POINTER_SEPARATOR + segment).join("") }
/// The pointer to a member below a path.
export fn at(path: Str, member: Str) -> Str { path + Text.POINTER_SEPARATOR + member }
/// The pointer to an item of a list below a path.
export fn item(path: Str, index: Int) -> Str { path + Text.POINTER_SEPARATOR + show(index) }
/// A dotted property as a pointer.
export fn dotted(property: Str) -> Str { Text.POINTER_SEPARATOR + property.replace(Text.DOT, Text.POINTER_SEPARATOR) }
```

### Linkage

- **Requires:** [[src/Constants/Text]]
- **Consumed by:** [[src/App/Pipeline]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Custody]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Handoff]]

## Referenced by

[[src/Utils/_MOC]] · [[src/App/Pipeline]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Custody]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Handoff]]
