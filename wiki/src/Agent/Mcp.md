---
type: module
path: "@root/src/Agent/Mcp.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, agent]
---

# Agent.Mcp

> @Agent.Mcp.Server — serves the participant's tools to a hosted model over a tool protocol on standard input and output

## Purpose

Serves the participant's tools to a hosted model over a tool protocol on standard input and output.

## Interface

### Signatures

```pudu
/// Serves one client until its input ends; answers the exit status. A participant that cannot attach still answers the handshake, and every tool call then explains why.
export fn serve() -> Int
/// The protocol session after one input line, and the line to answer it with, if any.
export fn respond(attached: &Result[Session.Session, Str], session: &Negotiation.Session, line: Str) -> (Negotiation.Session, Option[Str])
```

### Linkage

- **Requires:** [[src/Agent/Session]] · [[src/Agent/Tools]] · [[src/Constants/Agent]] · [[src/Constants/Fabric]] · [[src/Constants/Mcp]]
- **Packages:** `PuduLangMcp`
- **Standard library:** `Std.Io`, `Std.Json`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/Cli/Commands]]

## Referenced by

[[src/Cli/Commands]] · [[src/Agent/_MOC]]
