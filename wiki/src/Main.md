---
type: module
path: "@root/src/Main.pudu"
layer: 8
grammar: "[[grammar/pudu]]"
tags: [module, main]
---

# Main

> @Main.Fabric.Entry — the grail process

## Purpose

The grail process.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/App/Logging]] · [[src/Cli/Commands]] · [[src/Config/Settings]] · [[src/Constants/Cli]] · [[src/Constants/Fabric]] · [[src/Constants/Http]] · [[src/Constants/Logging]] · [[src/Constants/Server]] · [[src/Constants/Text]] · [[src/Services/Runtime]] · [[src/Web/Description]] · [[src/Web/Router]]
- **Packages:** `PuduLangLog`
- **Standard library:** `Std.Env`, `Std.Http.Server`, `Std.Io`, `Std.Result`
- **Consumed by:** the runner

## Referenced by

[[src/_MOC]]
