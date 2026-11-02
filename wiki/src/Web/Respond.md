---
type: module
path: "@root/src/Web/Respond.pudu"
layer: 7
grammar: "[[grammar/pudu]]"
tags: [module, web]
---

# Web.Respond

> @Web.Respond.Answers — JSON answers and problem documents

## Purpose

JSON answers and problem documents.

## Interface

### Signatures

```pudu
/// A problem as an `application/problem+json` answer whose type, status, and title come from the contract's registry.
export fn problem(refused: &Problem.Problem) -> Http.Response { Document.respond(&documentOf(refused)) }
/// A problem as JSON, for bindings that frame it themselves.
export fn problemJson(refused: &Problem.Problem) -> Json.Json { Document.toJson(&documentOf(refused)) }
/// The status a problem is answered with.
export fn statusOf(refused: &Problem.Problem) -> Int { Problem.entryOf(refused).status }
/// A result rendered as JSON with a status, or its problem.
export fn answer[T](status: Int, outcome: Result[T, Problem.Problem], render: fn(T) -> Json.Json) -> Http.Response
```

### Linkage

- **Requires:** [[src/Constants/Http]] · [[src/Constants/Text]] · [[src/Contract/Version]] · [[src/Domain/Problem]]
- **Standard library:** `Std.App.Problem`, `Std.Http`, `Std.Http.Server.Reply`, `Std.Json`
- **Consumed by:** [[src/Web/Handlers]] · [[src/Web/Lines]] · [[src/Web/Router]]

## Referenced by

[[src/Web/Handlers]] · [[src/Web/Lines]] · [[src/Web/Router]] · [[src/Web/_MOC]]
