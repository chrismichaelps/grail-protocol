---
type: module
path: "@root/src/Engine/Bridge.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Bridge

> @Engine.Bridge.Correlation — which bridged request a JSON-RPC response answers

## Purpose

Which bridged request a JSON-RPC response answers.

## Interface

### Signatures

```pudu
/// The most recent open bridged request addressed to `responder` whose JSON-RPC id is `id`.
export fn requestFor(state: &Scope.State, responder: &Envelope.Address, id: &Json.Json) -> Option[Str]
/// Whether a JSON-RPC message answers a request rather than asking one.
export fn isResponse(message: &Json.Json) -> Bool { Option.isNone(&Json.field(message, Rpc.METHOD)) }
```

### Linkage

- **Requires:** [[src/Constants/Rpc]] · [[src/Contract/Vocabulary]] · [[src/Domain/Envelope]] · [[src/Domain/Ledger]] · [[src/Domain/Lifecycle]] · [[src/Domain/Scope]] · [[src/Engine/Lifecycle]]
- **Standard library:** `Std.Json`, `Std.List`, `Std.Map`, `Std.Option`
- **Consumed by:** [[src/Services/Bridge]]

## Referenced by

[[src/Engine/_MOC]] · [[src/Services/Bridge]]
