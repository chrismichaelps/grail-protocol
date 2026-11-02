---
type: test
path: "@root/test/Support/Fabric.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Support.Fabric

> @Test.Support.Fabric.Harness — a whole fabric in process, driven through its router without sockets

## Purpose

A whole fabric in process, driven through its router without sockets.

## Interface

### Signatures

```pudu
export type Answer = { status: Int, body: Json.Json, millis: Int }
/// A router over a fresh runtime, or why one could not be built.
export fn start() -> Result[Route.Router, Str]
/// The owner's root token for a scope, valid for a day around the current time.
export fn owner(scopeId: Str) -> Str
/// One request through the router.
export fn sent(router: &Route.Router, method: Http.Method, path: Str, token: Str, body: Str) -> Answer
/// A token delegated by `from` in scope `demo`, or empty text when refused.
export fn delegated(router: &Route.Router, from: Str, id: Str, audience: Str, abilities: &Array[Str], graph: Str, expires: Int) -> Str
/// The problem code of an answer, or empty text.
export fn code(answer: &Answer) -> Str { Option.unwrapOr(JsonRead.text(&answer.body, "code"), "") }
```

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/App/Logging]] · [[src/Config/Settings]] · [[src/Constants/Security]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Engine/Authority]] · [[src/Services/Runtime]] · [[src/Utils/JsonRead]] · [[src/Web/Router]]
- **Standard library:** `Std.Http`, `Std.Http.Server.Route`, `Std.Json`, `Std.Map`, `Std.Option`, `Std.Result`
- **Consumed by:** the runner

## Referenced by

[[test/Support/_MOC]]
