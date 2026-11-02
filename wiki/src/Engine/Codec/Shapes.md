---
type: module
path: "@root/src/Engine/Codec/Shapes.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Codec.Shapes

> @Engine.Codec.Shapes — checks a JSON body against the contract's shape of an object

## Purpose

Checks a JSON body against the contract's shape of an object.

## Interface

### Signatures

```pudu
export type Rule
export type Shape = { allowed: Array[Str], required: Array[Str], closed: Bool, extensible: Bool, single: Bool, rules: Array[(Str, Rule)] }
/// Every violation of a body against a named shape; none means the body has that shape.
export fn check(name: Str, value: &Json.Json, path: Str) -> Array[Problem.Violation]
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Graphs]] · [[src/Constants/Text]] · [[src/Contract/Limits]] · [[src/Contract/Members]] · [[src/Contract/Schemas]] · [[src/Contract/Vocabulary]] · [[src/Domain/Identifier]] · [[src/Domain/Problem]] · [[src/Utils/Pointer]]
- **Standard library:** `Std.Json`, `Std.List`, `Std.Option`
- **Consumed by:** [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Token]] · [[test/Engine/ShapesTest]]

<!-- authored -->
## Algorithm

Every shape is a row of a constant table built from generated contract constants: allowed and required members, whether the object is closed, whether `x-` members are carried, whether exactly one member is expected, and a rule per member. A rule checks a scalar, a list of names, or a nested shape.

## Grill Log

- **Q:** A general JSON Schema validator over the document? **A:** A table over the generated member lists. **Rationale:** the contract still decides every member name, requirement, and enumeration through [[src/Contract/Members]] and [[src/Contract/Vocabulary]], while the rules stay typed and readable. **Rejected:** interpreting the schema at run time.
<!-- /authored -->

## Referenced by

[[src/Engine/Codec/_MOC]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Token]] · [[test/Engine/ShapesTest]]
