---
type: module
path: "@root/src/Domain/Identifier.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Identifier

> @Domain.Identifier.Grammar — what identifiers, names, and kinds may look like

## Purpose

What identifiers, names, and kinds may look like.

## Interface

### Signatures

```pudu
/// Whether text is an identifier: 1 to the identifier limit of letters, digits, and `. _ : -`.
export fn isIdentifier(text: Str) -> Bool
/// Whether text is a name: 1 to the name limit of lowercase letters, digits, and `. _ -`.
export fn isName(text: Str) -> Bool
/// Whether text is a reserved kind or an extension kind.
export fn isKind(text: Str) -> Bool { Vocabulary.KINDS.contains(text) || isExtension(text) }
/// Whether text names an extension: `x-owner.name`.
export fn isExtension(text: Str) -> Bool
```

### Linkage

- **Requires:** [[src/Constants/Graphs]] · [[src/Constants/Text]] · [[src/Contract/Limits]] · [[src/Contract/Vocabulary]]
- **Standard library:** `Std.Char`, `Std.Text`
- **Consumed by:** [[src/Engine/Codec/Custody]] · [[src/Engine/Codec/Shapes]] · [[test/Engine/ShapesTest]]

## Referenced by

[[src/Domain/_MOC]] · [[src/Engine/Codec/Custody]] · [[src/Engine/Codec/Shapes]] · [[test/Engine/ShapesTest]]
