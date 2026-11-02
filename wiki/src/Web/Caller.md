---
type: module
path: "@root/src/Web/Caller.pudu"
layer: 7
grammar: "[[grammar/pudu]]"
tags: [module, web]
---

# Web.Caller

> @Web.Caller.Reading — what a request presents: its token, parameters, and body

## Purpose

What a request presents: its token, parameters, and body.

## Interface

### Signatures

```pudu
/// The bearer token a request presents, or empty text when it presents none.
export fn token(request: &Route.Request) -> Str
/// A call carrying the request's token, the scope its path names, and an input.
export fn call[T](request: &Route.Request, input: T) -> Request.Call[T] { Request.Call{token: token(request), scopeId: parameter(request, Parameters.SCOPE), input: input} }
/// A path parameter, or empty text.
export fn parameter(request: &Route.Request, name: Str) -> Str { Option.unwrapOr(Route.param(request, name), "") }
/// A whole-number query parameter, absent when not given.
export fn whole(request: &Route.Request, name: Str) -> Result[Option[Int], Problem.Problem]
/// The request body as JSON.
export fn body(request: &Route.Request) -> Result[Json.Json, Problem.Problem]
/// Nothing when the request asks for a protocol version this fabric speaks, or for none.
export fn version(request: &Route.Request) -> Result[(), Problem.Problem]
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Extras]] · [[src/Constants/Fabric]] · [[src/Constants/Http]] · [[src/Constants/Security]] · [[src/Constants/Text]] · [[src/Contract/Parameters]] · [[src/Contract/Problems]] · [[src/Contract/Version]] · [[src/Domain/Problem]] · [[src/Domain/Request]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Http.Server.Route`, `Std.Json`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/Web/Handlers]] · [[src/Web/Router]]

## Referenced by

[[src/Web/Handlers]] · [[src/Web/Router]] · [[src/Web/_MOC]]
