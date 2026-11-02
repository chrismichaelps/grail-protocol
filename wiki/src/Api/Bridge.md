---
type: module
path: "@root/src/Api/Bridge.pudu"
layer: 4
grammar: "[[grammar/pudu]]"
tags: [module, api]
---

# Api.Bridge

> @Api.Bridge.Inspection — admits only well-formed JSON-RPC 2.0 messages into the bridge

## Purpose

Admits only well-formed JSON-RPC 2.0 messages into the bridge.

## Interface

### Signatures

```pudu
/// The message, when it is one JSON-RPC 2.0 request, notification, or response.
export fn inspect(text: Str) -> Result[Json.Json, Problem.Problem]
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Text]] · [[src/Contract/Problems]] · [[src/Domain/Problem]]
- **Packages:** `PuduLangMcp`
- **Standard library:** `Std.Json`, `Std.Result`
- **Consumed by:** [[src/Services/Bridge]]

## Referenced by

[[src/Api/_MOC]] · [[src/Services/Bridge]]
