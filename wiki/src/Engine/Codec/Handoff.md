---
type: module
path: "@root/src/Engine/Codec/Handoff.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Codec.Handoff

> @Engine.Codec.Handoff — handoff requests and handoffs read against the contract, and the answers about them

## Purpose

Handoff requests and handoffs read against the contract, and the answers about them.

## Interface

### Signatures

```pudu
/// What an export asks to carry, or every way the body departs from the contract.
export fn decodeRequest(body: &Json.Json, graph: Str, participant: Str) -> Result[Handoff.Asked, Problem.Problem]

/// A handoff with the contract's shape, named the same in the path and the body; integrity is checked by the engine, not here.
export fn decodeBundle(body: &Json.Json, id: Str) -> Result[Json.Json, Problem.Problem]

/// The answer to an import.
export fn receipt(answer: &Handoff.Receipt) -> Json.Json

/// What a fabric says about a handoff it was shown.
export fn check(answer: &Handoff.Check) -> Json.Json
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Extras]] · [[src/Contract/Limits]] · [[src/Contract/Members]] · [[src/Contract/Problems]] · [[src/Contract/Schemas]] · [[src/Domain/Handoff]] · [[src/Domain/Problem]] · [[src/Engine/Codec/Shapes]] · [[src/Utils/JsonRead]] · [[src/Utils/Pointer]]
- **Standard library:** `Std.Json`, `Std.Option`
- **Consumed by:** [[src/Web/Handlers]]

## Referenced by

[[src/Engine/Codec/_MOC]] · [[src/Web/Handlers]]
