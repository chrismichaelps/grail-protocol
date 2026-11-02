---
type: module
path: "@root/src/Engine/Paths.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Paths

> @Engine.Paths.Targets — the request target of an operation with its parameters filled in

## Purpose

The request target of an operation with its parameters filled in.

## Interface

### Signatures

```pudu
/// The operation with a contract id.
export fn operationOf(id: Str) -> Option[Operations.Operation] { List.find(&Operations.ALL, |candidate: Operations.Operation| candidate.id == id) }
/// The path of an operation with every path parameter taken from `params`.
export fn path(operation: &Operations.Operation, params: &Json.Json) -> Str
/// The query parameters of an operation present in `params`.
export fn query(operation: &Operations.Operation, params: &Json.Json) -> Array[(Str, Str)]
/// The full request target: the path and, when any is present, the query.
export fn target(operation: &Operations.Operation, params: &Json.Json) -> Str
```

### Linkage

- **Requires:** [[src/Constants/Http]] · [[src/Contract/Operations]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Json`, `Std.List`, `Std.Option`
- **Consumed by:** [[src/Cli/Commands]] · [[src/Web/Lines]]

## Referenced by

[[src/Cli/Commands]] · [[src/Engine/_MOC]] · [[src/Web/Lines]]
