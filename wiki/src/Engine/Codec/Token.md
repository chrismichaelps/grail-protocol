---
type: module
path: "@root/src/Engine/Codec/Token.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Codec.Token

> @Engine.Codec.Token — token claims to and from JSON

## Purpose

Token claims to and from JSON.

## Interface

### Signatures

```pudu
/// The claims as a JSON object.
export fn toJson(token: &Capability.Token) -> Json.Json
/// The claims of a JSON object, when every required member is present and well typed.
export fn fromJson(value: &Json.Json) -> Option[Capability.Token]
/// The delegation a body asks for, or how it departs from the contract; a missing start means now.
export fn decodeRequest(body: &Json.Json, now: Int) -> Result[Capability.Request, Problem.Problem]
```

### Linkage

- **Requires:** [[src/Contract/Members]] · [[src/Contract/Schemas]] · [[src/Domain/Capability]] · [[src/Domain/Problem]] · [[src/Engine/Codec/Shapes]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Json`, `Std.Option`
- **Consumed by:** [[src/Engine/Authority]] · [[src/Web/Handlers]]

## Referenced by

[[src/Engine/Authority]] · [[src/Engine/Codec/_MOC]] · [[src/Web/Handlers]]
