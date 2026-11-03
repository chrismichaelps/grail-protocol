---
type: module
path: "@root/src/Constants/Environment.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Environment

> @Constants.Environment.Names — the variables the fabric reads at start, and what it accepts

## Purpose

The variables the fabric reads at start, and what it accepts.

## Interface

### Signatures

```pudu
/// The address the server binds.
export const HOST: Str = "GRAIL_HOST"
/// The name this fabric gives itself as the origin of the handoffs it seals.
export const FABRIC_NAME: Str = "GRAIL_FABRIC_NAME"
/// The port the server binds.
export const PORT: Str = "GRAIL_PORT"
/// The fabric secret every scope key derives from.
export const SECRET: Str = "GRAIL_SECRET"
/// The lowest level written to the log.
export const LOG_LEVEL: Str = "GRAIL_LOG_LEVEL"
/// Requests served at once.
export const WORKERS: Str = "GRAIL_WORKERS"
/// Connections served before the server stops; 0 is unbounded.
export const CONNECTIONS: Str = "GRAIL_CONNECTIONS"
/// The most detailed log level.
export const VERBOSE: Str = "verbose"
/// Diagnostic events.
export const DEBUG: Str = "debug"
/// Normal operation.
export const INFORMATION: Str = "information"
/// Something unexpected that the fabric handled.
export const WARNING: Str = "warning"
/// A failure of one operation.
export const ERROR: Str = "error"
/// A failure of the fabric.
export const FATAL: Str = "fatal"
/// Log levels the fabric accepts.
export const LOG_LEVELS: Array[Str] = [VERBOSE, DEBUG, INFORMATION, WARNING, ERROR, FATAL]
/// The highest port number.
export const PORT_MAX: Int = 65535
/// The most workers the fabric runs.
export const WORKERS_MAX: Int = 1024
/// The most connections a bounded run may serve.
export const CONNECTIONS_MAX: Int = 1000000
/// What a short secret is told.
export const SECRET_TOO_SHORT: Str = "at least 32 characters"
/// What an unknown log level is told.
export const LEVEL_UNKNOWN: Str = "one of verbose, debug, information, warning, error, fatal"
/// What separates allowed origins.
export const ORIGIN_SEPARATOR: Str = ","
/// What a fabric name may hold.
export const FABRIC_NAME_INVALID: Str = "1 to 64 lowercase letters, digits, and . _ -"
/// The longest fabric name.
export const FABRIC_NAME_MAX: Int = 64
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/App/Logging]] · [[src/Config/Settings]]

## Referenced by

[[src/App/Logging]] · [[src/Config/Settings]] · [[src/Constants/_MOC]]
