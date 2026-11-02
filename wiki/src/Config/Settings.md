---
type: module
path: "@root/src/Config/Settings.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, config]
---

# Config.Settings

> @Config.Settings.Environment — what the fabric reads at start

## Purpose

What the fabric reads at start. `GRAIL_CLIENT_IP_HEADER` defaults to empty, which ignores forwarded client addresses. Set it to `CF-Connecting-IP` only when a trusted proxy overwrites that header and is the sole ingress. A local tunnel should target the fabric bound to `127.0.0.1`; a public origin must not accept direct requests with this setting enabled.

## Interface

### Signatures

```pudu
export type Settings = { … }
/// The settings from `.env`, when present, over the process environment, bound and validated.
export fn load() -> Result[Settings, Str]
/// The settings from the given variables alone, for tests and tools.
export fn loadFrom(variables: &Map[Str, Str]) -> Result[Settings, Str]
/// The fabric secret.
export fn secretOf(settings: &Settings) -> Str { Secret.reveal(&settings.secret) }
/// The origins allowed cross-origin access.
export fn origins(settings: &Settings) -> Array[Str]
```

### Linkage

- **Requires:** [[src/Constants/Environment]] · [[src/Constants/Security]]
- **Packages:** `PuduLangEnvironment`, `PuduLangValidator`
- **Standard library:** `Std.App.Secret`, `Std.Result`
- **Consumed by:** [[src/App/Logging]] · [[src/Cli/Commands]] · [[src/Main]] · [[src/Services/Runtime]] · [[src/Web/Router]] · [[test/Support/Fabric]] · [[test/Web/RouterTest]]

## Referenced by

[[src/App/Logging]] · [[src/Cli/Commands]] · [[src/Config/_MOC]] · [[src/Main]] · [[src/Services/Runtime]] · [[src/Web/Router]] · [[test/Support/Fabric]] · [[test/Web/RouterTest]]
