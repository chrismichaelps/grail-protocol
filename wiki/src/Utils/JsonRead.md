---
type: module
path: "@root/src/Utils/JsonRead.pudu"
layer: 1
grammar: "[[grammar/pudu]]"
tags: [module, utils]
---

# Utils.JsonRead

> @Utils.JsonRead.Access — typed reads of optional JSON members

## Purpose

Typed reads of optional JSON members.

## Interface

### Signatures

```pudu
/// A member's text, when present and textual.
export fn text(value: &Json.Json, name: Str) -> Option[Str]
/// A member's whole number, when present and whole.
export fn whole(value: &Json.Json, name: Str) -> Option[Int]
/// A member's list, when present and a list.
export fn list(value: &Json.Json, name: Str) -> Option[Array[Json.Json]]
/// A member's texts, when present and every item is text.
export fn texts(value: &Json.Json, name: Str) -> Option[Array[Str]]
/// The names of an object's members, or none for anything else.
export fn names(value: &Json.Json) -> Array[Str]
/// A list of texts as JSON.
export fn textList(values: &Array[Str]) -> Json.Json { Json.List(values.map(|value: Str| Json.Text(value))) }
/// An object from pairs, skipping absent members.
export fn objectOf(members: &Array[(Str, Option[Json.Json])]) -> Json.Json
```

### Linkage

- **Requires:** nothing inside the fabric
- **Standard library:** `Std.Json`, `Std.Option`
- **Consumed by:** [[src/Cli/Commands]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Token]] · [[src/Engine/Codec/Views]] · [[src/Engine/Handoff]] · [[src/Engine/Journal]] · [[src/Engine/Kinds]] · [[src/Engine/Mutations]] · [[src/Engine/Paths]] · [[src/Services/Bridge]] · [[src/Web/Caller]] · [[src/Web/Lines]] · [[test/Engine/LedgerTest]] · [[test/Security/AttackTest]] · [[test/Security/HandoffTest]] · [[test/Support/Fabric]] · [[test/Web/RouterTest]]

## Referenced by

[[src/Utils/_MOC]] · [[src/Cli/Commands]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Token]] · [[src/Engine/Codec/Views]] · [[src/Engine/Handoff]] · [[src/Engine/Journal]] · [[src/Engine/Kinds]] · [[src/Engine/Mutations]] · [[src/Engine/Paths]] · [[src/Services/Bridge]] · [[src/Web/Caller]] · [[src/Web/Lines]] · [[test/Engine/LedgerTest]] · [[test/Security/AttackTest]] · [[test/Security/HandoffTest]] · [[test/Support/Fabric]] · [[test/Web/RouterTest]]
