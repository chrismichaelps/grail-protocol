---
type: module
path: "@root/src/Web/Router.pudu"
layer: 7
grammar: "[[grammar/pudu]]"
tags: [module, web]
---

# Web.Router

> @Web.Router.Binding — the HTTP routes, built from the contract's operations and nothing else

## Purpose

The HTTP routes, built from the contract's operations and nothing else.

## Interface

### Signatures

```pudu
/// Every contract operation as a route, or the operations without a handler and the handlers without an operation.
export fn router(app: &Assembly.App) -> Result[Route.Router, Str]
/// The hardening every request passes: a request identity, protective headers, sharing with listed origins only, a rate limit, a concurrency bound, and a deadline. Same-site form protection is left out on purpose: every operation is authorized by a bearer token, never by a cookie.
export fn middleware(settings: &Settings.Settings) -> Array[Route.Middleware]
/// Answers a method a contract path does not offer with a problem document, like every other refusal, in place of the server's plain text.
export fn refusing() -> Route.Middleware
```

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/Config/Settings]] · [[src/Constants/Details]] · [[src/Constants/Http]] · [[src/Constants/Server]] · [[src/Constants/Text]] · [[src/Contract/Operations]] · [[src/Contract/Problems]] · [[src/Domain/Problem]] · [[src/Web/Caller]] · [[src/Web/Handlers]] · [[src/Web/Peers]] · [[src/Web/Respond]]
- **Standard library:** `Std.Http`, `Std.Http.Server.Guard`, `Std.Http.Server.Route`, `Std.Option`
- **Consumed by:** [[src/Cli/Commands]] · [[src/Main]] · [[test/Support/Fabric]] · [[test/Web/RouterTest]]

<!-- authored -->
## Algorithm

Every route comes from [[src/Contract/Operations]]: its method, its pattern, and the status a success answers with. The router refuses to start when an operation has no handler or a handler has no operation. Each request checks the `Grail-Version` header before its handler runs.

## Grill Log

- **Q:** Same-site form protection? **A:** Left out. **Rationale:** every operation is authorized by a bearer token, never by a cookie, so cross-site forms cannot act. **Rejected:** the standard guard set, which refused legitimate API calls.
<!-- /authored -->

## Referenced by

[[src/Cli/Commands]] · [[src/Main]] · [[src/Web/_MOC]] · [[test/Support/Fabric]] · [[test/Web/RouterTest]]
