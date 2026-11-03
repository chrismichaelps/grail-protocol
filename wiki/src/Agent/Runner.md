---
type: module
path: "@root/src/Agent/Runner.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, agent]
---

# Agent.Runner

> @Agent.Runner.Supervisor — keeps a participant attached: pulls its deliveries, starts a hosted agent for each task, and makes sure every task it starts ends answered

## Purpose

Keeps a participant attached: pulls its deliveries, starts a hosted agent for each task, and makes sure every task it starts ends answered.

## Interface

### Signatures

```pudu
export type Plan = { command: Str, timeout: Int, once: Bool }
/// Pulls and handles deliveries until stopped, or after one page when the plan says so; answers the exit status.
export fn run(session: &Session.Session, plan: &Plan) -> Int
/// The prompt a hosted agent receives for a task: who it is, who asked, the task id, and the request.
export fn prompt(session: &Session.Session, written: &Json.Json) -> Str
```

### Linkage

- **Requires:** [[src/Agent/Session]] · [[src/Agent/Tools]] · [[src/Agent/Wire]] · [[src/Constants/Agent]] · [[src/Contract/Members]] · [[src/Contract/Operations]] · [[src/Contract/Parameters]] · [[src/Contract/Vocabulary]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Bytes`, `Std.Concurrent`, `Std.Env`, `Std.Io`, `Std.Json`, `Std.Math`, `Std.Option`, `Std.Process`, `Std.Result`, `Std.Sync`
- **Consumed by:** [[src/Cli/Commands]]

## Referenced by

[[src/Cli/Commands]] · [[src/Agent/_MOC]]
