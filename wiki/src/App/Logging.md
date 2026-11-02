---
type: module
path: "@root/src/App/Logging.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, app]
---

# App.Logging

> @App.Logging.Events — the structured loggers of the fabric

## Purpose

The structured loggers of the fabric.

## Interface

### Signatures

```pudu
export type Logs = { server: Logger.Logger, messages: Logger.Logger }
/// The loggers the settings describe.
export fn logs(settings: &Settings.Settings) -> Logs
/// Loggers that write nothing.
export fn quiet() -> Logs { Logs{server: Logger.none(), messages: Logger.none()} }
```

### Linkage

- **Requires:** [[src/Config/Settings]] · [[src/Constants/Environment]] · [[src/Constants/Fabric]] · [[src/Constants/Logging]]
- **Packages:** `PuduLangLog`
- **Consumed by:** [[src/App/Assembly]] · [[src/Main]] · [[test/Support/Fabric]] · [[test/Web/RouterTest]]

## Referenced by

[[src/App/Assembly]] · [[src/App/_MOC]] · [[src/Main]] · [[test/Support/Fabric]] · [[test/Web/RouterTest]]
