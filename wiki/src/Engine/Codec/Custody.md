---
type: module
path: "@root/src/Engine/Codec/Custody.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Codec.Custody

> @Engine.Codec.Custody — deposits read against the contract, and what may be said about a held secret

## Purpose

Deposits read against the contract, and what may be said about a held secret.

## Interface

### Signatures

```pudu
/// A deposit under a name, or every way the body departs from the contract. A violation never repeats the value.
export fn decodeDeposit(body: &Json.Json, name: Str) -> Result[Custody.Deposit, Problem.Problem]

/// A held secret as anyone allowed to know it exists sees it: its name, version, and policy, never its value.
export fn view(held: &Custody.Held) -> Json.Json

/// Several held secrets.
export fn list(found: &Array[Custody.Held]) -> Json.Json
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Contract/Members]] · [[src/Contract/Schemas]] · [[src/Domain/Custody]] · [[src/Domain/Identifier]] · [[src/Domain/Problem]] · [[src/Engine/Codec/Shapes]] · [[src/Utils/JsonRead]] · [[src/Utils/Pointer]]
- **Standard library:** `Std.Json`, `Std.Option`
- **Consumed by:** [[src/Web/Handlers]]

## Referenced by

[[src/Engine/Codec/_MOC]] · [[src/Web/Handlers]]
