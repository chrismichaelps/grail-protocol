---
type: grammar
language: Pudu
version: "0.1.3"
tags: [grammar]
aliases: [Pudu grammar, Grammar — Pudu]
---

# Grammar — Pudu

The Pudu language grammar and its vault are the authority on syntax. This page pins the version the fabric builds with and records the rules and library surface the fabric relies on, each verified against the 0.1.3 release by compiling and running it.

## Pinned toolchain

- Compiler and standard library: **0.1.3** (`language = ">=0.1.3 <0.2.0"`).
- Packages, pinned exactly and locked: `@chrismichaelps/pudu-lang-environment` 0.1.0, `@chrismichaelps/pudu-lang-httpclient` 0.1.1, `@chrismichaelps/pudu-lang-log` 0.1.0, `@chrismichaelps/pudu-lang-mcp` 0.1.2, `@chrismichaelps/pudu-lang-mediator` 0.1.0, `@chrismichaelps/pudu-lang-resilience` 0.1.0, `@chrismichaelps/pudu-lang-validator` 0.1.1.

## Syntax rules the fabric leans on

- One `module` per file; the name matches the path under its root (`src/Engine/Admission.pudu` is `Engine.Admission`; `test/` and `tools/` are roots of their own).
- `module`, `type`, `task`, `scope`, `with`, `dynamic`, and the other reserved words cannot name bindings, parameters, functions, or record fields. The protocol's `scope` member is the field `scopeId`; a lifecycle's task is `taskId`.
- `{` inside a string opens an interpolation; a literal brace is `\{` or `\}`.
- Attribute arguments are literals only: `@env("GRAIL_PORT")` cannot name a constant, so `Config.Settings` is the one place environment names appear literally; rule names read them from [[src/Constants/Environment]].
- Arrays have only `length isEmpty get indexOf contains push pop insert remove slice concat join reverse map filter sortBy reduce`; anything else (`any`, `all`, `find`, `flatMap`, `distinct`, `fold`) comes from `Std.List`.
- `Option` and `Result` functions need `import Std.Option as Option` / `import Std.Result as Result`.
- Constant maps may hold functions and records (`Map[Str, fn(Json.Json) -> Option[Step]]`), which is how factories are written.
- Closures may be returned from `match` arms; this is how resolvers and step effects are chosen once.

## Standard library surface in use

| Need | Module | Items |
| --- | --- | --- |
| HTTP serving | `Std.Http.Server`, `Std.Http.Server.Route`, `Std.Http.Server.Reply`, `Std.Http.Server.Guard` | `server`, `start`, `run`, `stop`, `stopOnSignal`, `withLimits`, `withWorkers`, `using`; `on`, `routing`, `withFallback`, `dispatch`, `param`, `queryParam`, `header`, `body`; `json`, `jsonValue`; `identified`, `protectedHeaders`, `shared`, `rateLimited`, `boundedConcurrency`, `timeout` |
| API description | `Std.App.OpenApi` | `document`, `operation`, `parameter`, `answer`, `undocumented`, `problems` |
| Problems | `Std.App.Problem` | `typed`, `withExtension`, `toJson`, `respond` |
| JSON | `Std.Json` | `decode`, `encode`, `encodePretty`, `field`, `withField`, `asText`, `asInt`, `asList`, `asObject`, `keys`, `object` |
| Graphs | `Std.Graph` | `fromEdges`, `stronglyConnected`, `shortestPath`, `neighbours`, `topologicalOrder` |
| Hashing and signing | `Std.Crypto`, `Std.Bytes` | `sha256Hex`, `hmacSha256`, `hmacSha256Text`, `bytesMatch`; `encodeBase64Url`, `decodeBase64Url`, `encodeHex` |
| State | `Std.Sync` | `mutex`, `cell`, `withLock`, `get`, `set` |
| Time and randomness | `Std.Time`, `Std.Random` | `currentInstant`, `toMillis`; `secureBytes` |
| Tests | `Std.Test` | `suite`, `that`, `not`, `equals`, `succeeded`, `absent`, `contains`, `run`, `report` |

## Package surface in use

| Package | Items |
| --- | --- |
| mediator | `Request.kind`, `Registration.handler`, `Registration.notificationHandler`, `Registration.openBehavior`, `Registration.openExceptionAction`, `Notification.kind`, `Mediator.build`, `Mediator.send`, `Mediator.publish`, `Behaviors.Logging.of`, `Behaviors.Validation.register`, `Behaviors.Resilient.register` |
| resilience | `Pipeline.build`, `RateLimiter.strategy`, `RateLimiter.concurrency`, `Timeout.strategy`, `Timeout.after` |
| httpclient | `Factory.build`, `Builder.named(..).withBaseAddress/withDefaultHeader/withTimeout/withHandler`, `Factory.createClient`, `Client.build`, `Client.send`, `Handlers.Resilience.standard`, `Handlers.Resilience.handler`, `Content.json`, `Response.text` |
| log | `Configuration.create().minimumLevel(..).enrichWithProperty(..).writeTo(..).createLogger()`, `Sinks.Console`, `Logger.information/warning/error`, `Value.text/int` |
| validator | `Rule.ruleFor`, `Rule.must`, `Rule.mustWith`, `Rule.withMessage`, `Rule.withCode`, `Rule.build`, `Rules.Number`, `Rules.Text`, `Rules.Child.setValidator`, `Validator.create/add` |
| environment | `Loader.load`, `Loader.loadOver`, `Settings.bind`, `Options.defaults`, `Binding.Bind`, `Binding.Redacted`, `@env`/`@default`/`@secret` |
| mcp | `Domain.Rpc.Message.parse` and its `Incoming` variants, `Errors.RpcError.message` |

## Known compiler issues

- A function stored in a constant and called from another module runs without its own module's imports ("undefined name"). Reproduction: module `A.B` exports `const TABLE: Map[Str, fn(Int) -> Str] = mapOf([("x", render)])` where `render` uses `Json`; `A.B` calling `TABLE.get("x")` works, `Main` calling the same function fails at run time. The fabric keeps such tables private and exposes a function that calls them ([[src/Web/Handlers]]). To be reported upstream with this reproduction.

- The standard rate-limiting guard keys its window by the peer as the server records it, which is address and port; every new connection therefore starts a fresh window. The fabric names peers by host before the limiter ([[src/Web/Peers]]). To be reported upstream.

## Senior Definition Needed

- None open.

## Referenced by

[[00-INDEX]] · [[architecture/CODE_STYLE]]
