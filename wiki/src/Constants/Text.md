---
type: module
path: "@root/src/Constants/Text.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Text

> @Constants.Text.Joins — the separators text is joined and split with

## Purpose

The separators text is joined and split with.

## Interface

### Signatures

```pudu
/// Joins items of a list in one line.
export const LIST_JOIN: Str = "; "
/// Joins a label and what it labels.
export const LABEL_JOIN: Str = ": "
/// Joins words.
export const WORD_JOIN: Str = " "
/// Joins lines.
export const LINE_JOIN: Str = "\n"
/// Joins a host and a port.
export const PORT_JOIN: Str = ":"
/// Separates the segments of a JSON pointer.
export const POINTER_SEPARATOR: Str = "/"
/// Marks a query parameter in a violation's path.
export const QUERY_POINTER: Str = "?"
/// Separates the parts of a dotted name.
export const DOT: Str = "."
/// Punctuation an identifier may hold besides letters and digits.
export const IDENTIFIER_MARKS: Array[Char] = ['.', '_', ':', '-']
/// Punctuation a name may hold besides lowercase letters and digits.
export const NAME_MARKS: Array[Char] = ['.', '_', '-']
/// The member a call's input is reported under by the validator.
export const INPUT_PROPERTY: Str = "input"
/// What separates a graph from a participant in a delivery mark's key.
export const MARK_SEPARATOR: Str = "/"
/// Opens a bracketed IPv6 host.
export const BRACKET_OPEN: Str
/// Closes a bracketed IPv6 host.
export const BRACKET_CLOSE: Str = "]"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Api/Bridge]] · [[src/App/Pipeline]] · [[src/Cli/Commands]] · [[src/Domain/Identifier]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Delivery]] · [[src/Main]] · [[src/Utils/Pointer]] · [[src/Web/Caller]] · [[src/Web/Peers]] · [[src/Web/Respond]] · [[src/Web/Router]]

## Referenced by

[[src/Api/Bridge]] · [[src/App/Pipeline]] · [[src/Cli/Commands]] · [[src/Constants/_MOC]] · [[src/Domain/Identifier]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Delivery]] · [[src/Main]] · [[src/Utils/Pointer]] · [[src/Web/Caller]] · [[src/Web/Peers]] · [[src/Web/Respond]] · [[src/Web/Router]]
