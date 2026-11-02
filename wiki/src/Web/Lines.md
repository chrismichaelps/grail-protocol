---
type: module
path: "@root/src/Web/Lines.pudu"
layer: 7
grammar: "[[grammar/pudu]]"
tags: [module, web]
---

# Web.Lines

> @Web.Lines.Binding — one JSON request per input line, dispatched through the HTTP router

## Purpose

One JSON request per input line, dispatched through the HTTP router.

## Interface

### Signatures

```pudu
/// The answer line to one request line.
export fn answer(router: &Route.Router, line: Str) -> Str
```

### Linkage

- **Requires:** [[src/Constants/Http]] · [[src/Constants/Security]] · [[src/Contract/Problems]] · [[src/Contract/Version]] · [[src/Domain/Problem]] · [[src/Engine/Paths]] · [[src/Utils/JsonRead]] · [[src/Web/Respond]]
- **Standard library:** `Std.Http`, `Std.Http.Server.Route`, `Std.Json`, `Std.Map`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/Cli/Commands]] · [[test/Web/RouterTest]]

## Referenced by

[[src/Cli/Commands]] · [[src/Web/_MOC]] · [[test/Web/RouterTest]]
