---
type: module
path: "@root/src/Web/Description.pudu"
layer: 7
grammar: "[[grammar/pudu]]"
tags: [module, web]
---

# Web.Description

> @Web.Description.Contract — the operations described with the standard OpenAPI model, to prove the router serves exactly the contract

## Purpose

The operations described with the standard OpenAPI model, to prove the router serves exactly the contract.

## Interface

### Signatures

```pudu
/// The contract's operations as a standard API description.
export fn document() -> OpenApi.Document
/// Routes served but not described, and operations described but not served; both empty when the router is the contract.
export fn gaps(router: &Route.Router) -> (Array[Str], Array[Str]) { OpenApi.undocumented(&document(), router) }
/// Inconsistencies inside the description itself.
export fn problems() -> Array[Str] { OpenApi.problems(&document()) }
```

### Linkage

- **Requires:** [[src/Contract/Operations]] · [[src/Contract/Version]]
- **Standard library:** `Std.App.OpenApi`, `Std.Http`, `Std.Http.Server.Route`
- **Consumed by:** [[src/Main]] · [[test/Web/RouterTest]]

## Referenced by

[[src/Main]] · [[src/Web/_MOC]] · [[test/Web/RouterTest]]
