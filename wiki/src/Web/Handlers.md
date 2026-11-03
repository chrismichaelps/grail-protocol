---
type: module
path: "@root/src/Web/Handlers.pudu"
layer: 7
grammar: "[[grammar/pudu]]"
tags: [module, web]
---

# Web.Handlers

> @Web.Handlers.Operations — one handler per contract operation, chosen once by operation id

## Purpose

One handler per contract operation, chosen once by operation id.

## Interface

### Signatures

```pudu
export type Handler = fn(Assembly.App, Route.Request, Int) -> Http.Response
/// The ids of every operation with a handler.
export fn bound() -> Array[Str]
/// The answer of an operation's handler, or `None` when the operation has none.
export fn respond(id: Str, app: Assembly.App, request: Route.Request, status: Int) -> Option[Http.Response]
```

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/App/Commands]] · [[src/Contract/Document]] · [[src/Contract/Operations]] · [[src/Contract/Parameters]] · [[src/Domain/Capability]] · [[src/Domain/Custody]] · [[src/Domain/Envelope]] · [[src/Domain/Graph]] · [[src/Domain/Handoff]] · [[src/Domain/Mutation]] · [[src/Domain/Problem]] · [[src/Domain/Request]] · [[src/Domain/Transfer]] · [[src/Engine/Codec/Custody]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Token]] · [[src/Engine/Codec/Views]] · [[src/Web/Caller]] · [[src/Web/Respond]]
- **Standard library:** `Std.Http`, `Std.Http.Server.Reply`, `Std.Http.Server.Route`, `Std.Json`, `Std.Map`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/Web/Router]]

<!-- authored -->
## Grill Log

- **Q:** Export the handler table? **A:** No; the router asks `respond` and `bound`. **Rationale:** in the pinned runtime a function taken out of a constant and called from another module runs without its own module's imports (see [[grammar/pudu#Known compiler issues]]). **Rejected:** exporting the table.
<!-- /authored -->

## Referenced by

[[src/Web/Router]] · [[src/Web/_MOC]]
