---
type: test
path: "@root/test/Web/RouterTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Web.RouterTest

> @Test.Web.Router.Suite — the router serves exactly the contract, over HTTP and over lines

## Purpose

The router serves exactly the contract, over HTTP and over lines.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/App/Logging]] · [[src/Config/Settings]] · [[src/Constants/Security]] · [[src/Contract/Operations]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Engine/Authority]] · [[src/Services/Runtime]] · [[src/Utils/JsonRead]] · [[src/Web/Description]] · [[src/Web/Lines]] · [[src/Web/Router]]
- **Standard library:** `Std.Http`, `Std.Http.Server.Route`, `Std.Json`, `Std.Map`, `Std.Option`, `Std.Result`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Web/_MOC]]
