---
type: module
path: "@root/src/Services/Runtime.pudu"
layer: 5
grammar: "[[grammar/pudu]]"
tags: [module, services]
---

# Services.Runtime

> @Services.Runtime.Context — the settings, the store, and the clock every use case shares

## Purpose

The settings, the store, and the clock every use case shares.

## Interface

### Signatures

```pudu
export type Runtime = { settings: Settings.Settings, store: Store.Store, secret: Str, waiting: Sync.Counter }
/// A runtime over validated settings, with an empty store.
export fn create(settings: &Settings.Settings) -> Runtime { Runtime{settings: *settings, store: Store.create(), secret: Settings.secretOf(settings), waiting: Sync.counter(0)} }
/// Claims one of the places a pull may wait in, half the workers, so waiting pulls never occupy every worker; `false` when none is free.
export fn claimWait(runtime: &Runtime) -> Bool
/// Gives back a place claimed with `claimWait`.
export fn releaseWait(runtime: &Runtime) -> ()
/// The fabric's time in milliseconds since the Unix epoch.
export fn now() -> Int { Time.toMillis(&Time.currentInstant()) }
/// A fresh random identifier with a prefix.
export fn identifier(prefix: Str, bytes: Int) -> Result[Str, Problem.Problem]
```

### Linkage

- **Requires:** [[src/Config/Settings]] · [[src/Constants/Details]] · [[src/Constants/Server]] · [[src/Contract/Problems]] · [[src/Domain/Problem]] · [[src/Services/Store]]
- **Standard library:** `Std.Bytes`, `Std.Random`, `Std.Result`, `Std.Sync`, `Std.Time`
- **Consumed by:** [[src/App/Assembly]] · [[src/App/Handlers]] · [[src/Main]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[test/Support/Fabric]] · [[test/Web/RouterTest]]

## Referenced by

[[src/App/Assembly]] · [[src/App/Handlers]] · [[src/Main]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[src/Services/_MOC]] · [[test/Support/Fabric]] · [[test/Web/RouterTest]]
