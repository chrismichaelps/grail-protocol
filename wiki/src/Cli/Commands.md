---
type: module
path: "@root/src/Cli/Commands.pudu"
layer: 7
grammar: "[[grammar/pudu]]"
tags: [module, cli]
---

# Cli.Commands

> @Cli.Commands.Executable — the commands of the grail executable other than serving HTTP

## Purpose

The commands of the grail executable other than serving HTTP.

## Interface

### Signatures

```pudu
/// The status of a command that needs no running fabric, or `None` when the command needs one.
export fn offline(arguments: &Array[Str]) -> Option[Int]
/// Runs a command that needs the fabric's settings or a running fabric.
export fn run(app: &Assembly.App, arguments: &Array[Str]) -> Int
```

### Linkage

- **Requires:** [[src/Api/Peer]] · [[src/App/Assembly]] · [[src/Config/Settings]] · [[src/Constants/Cli]] · [[src/Constants/Fabric]] · [[src/Constants/Security]] · [[src/Constants/Text]] · [[src/Contract/Document]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Engine/Authority]] · [[src/Engine/Paths]] · [[src/Web/Lines]] · [[src/Web/Router]]
- **Standard library:** `Std.Env`, `Std.Io`, `Std.Json`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/Main]]

## Referenced by

[[src/Cli/_MOC]] · [[src/Main]]
