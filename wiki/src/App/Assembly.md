---
type: module
path: "@root/src/App/Assembly.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, app]
---

# App.Assembly

> @App.Assembly.Composition — the mediator built once over the runtime

## Purpose

The mediator built once over the runtime.

## Interface

### Signatures

```pudu
export type App = { runtime: Runtime.Runtime, mediator: Mediator.Mediator, kinds: Messages.Kinds, events: Events.Kinds, logs: Logging.Logs }
/// The fabric over a runtime, or every registration problem at once.
export fn assemble(runtime: &Runtime.Runtime, logs: &Logging.Logs) -> Result[App, Str]
/// A message sent through the mediator, its failure as a problem.
export fn send[Q, R](app: &App, kind: &Request.Kind[Q, R, Problem.Problem], request: Q) -> Result[R, Problem.Problem]
/// The fabric's time in milliseconds since the Unix epoch.
export fn now() -> Int { Runtime.now() }
/// Announces a notification; a listener's failure is logged, never returned to the caller whose change already happened.
export fn announce[N](app: &App, kind: &Notification.Kind[N, Problem.Problem], notification: N) -> ()
```

### Linkage

- **Requires:** [[src/App/Events]] · [[src/App/Handlers]] · [[src/App/Logging]] · [[src/App/Messages]] · [[src/App/Pipeline]] · [[src/App/Resilience]] · [[src/Constants/Logging]] · [[src/Domain/Problem]] · [[src/Services/Runtime]]
- **Packages:** `PuduLangLog`, `PuduLangMediator`
- **Consumed by:** [[src/App/Commands]] · [[src/Cli/Commands]] · [[src/Main]] · [[src/Web/Handlers]] · [[src/Web/Router]] · [[test/Security/AttackTest]] · [[test/Security/HandoffTest]] · [[test/Support/Fabric]] · [[test/Web/RouterTest]]

## Referenced by

[[src/App/_MOC]] · [[src/App/Commands]] · [[src/Cli/Commands]] · [[src/Main]] · [[src/Web/Handlers]] · [[src/Web/Router]] · [[test/Security/AttackTest]] · [[test/Security/HandoffTest]] · [[test/Support/Fabric]] · [[test/Web/RouterTest]]
