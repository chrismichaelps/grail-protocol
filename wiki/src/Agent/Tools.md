---
type: module
path: "@root/src/Agent/Tools.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, agent]
---

# Agent.Tools

> @Agent.Tools.Catalog — what an attached participant can do, as tools a hosted model calls, each chosen once by name

## Purpose

What an attached participant can do, as tools a hosted model calls, each chosen once by name.

## Interface

### Signatures

```pudu
export type Tool = { name: Str, description: Str, schema: Str }
export type Act = fn(Session.Session, Json.Json) -> Result[Json.Json, Json.Json]
/// Every tool, in the order a client lists them.
export const TOOLS: Array[Tool] = [
  Tool{name: Names.TOOL_WHOAMI, description: Names.WHOAMI_DESCRIPTION, schema: Names.WHOAMI_SCHEMA},
  Tool{name: Names.TOOL_INBOX, description: Names.INBOX_DESCRIPTION, schema: Names.INBOX_SCHEMA},
  Tool{name: Names.TOOL_SEND, description: Names.SEND_DESCRIPTION, schema: Names.SEND_SCHEMA},
  Tool{name: Names.TOOL_REPLY, description: Names.REPLY_DESCRIPTION, schema: Names.REPLY_SCHEMA},
  Tool{name: Names.TOOL_CHANNEL, description: Names.CHANNEL_DESCRIPTION, schema: Names.CHANNEL_SCHEMA},
  Tool{name: Names.TOOL_STATUS, description: Names.STATUS_DESCRIPTION, schema: Names.TRANSFER_SCHEMA},
  Tool{name: Names.TOOL_TRACE, description: Names.TRACE_DESCRIPTION, schema: Names.TRANSFER_SCHEMA}
]
/// The answer of a tool, or why it has none: the fabric's problem document, or what was wrong with the call.
export fn call(name: Str, session: &Session.Session, arguments: &Json.Json) -> Result[Json.Json, Json.Json]
/// Sends a draft under a fresh id and answers the fabric's receipt.
export fn sendDraft(session: &Session.Session, draft: &Wire.Draft) -> Result[Json.Json, Json.Json]
/// Answers a task: reads who sent it, and sends the outcome back to them with the task as its first parent. Final outcomes carry a delivery key, so a retried answer lands once.
export fn answer(session: &Session.Session, taskId: Str, outcome: Str, payload: Option[Json.Json], parents: &Array[Str]) -> Result[Json.Json, Json.Json]
/// Reads one transfer.
export fn readTransfer(session: &Session.Session, id: Str) -> Result[Json.Json, Json.Json]
/// A refusal in the shape tools answer with: the fabric's problem document with its status, or a reason the call never reached the fabric.
export fn answered(outcome: Result[Peer.Answer, Str]) -> Result[Json.Json, Json.Json]
```

### Linkage

- **Requires:** [[src/Agent/Session]] · [[src/Agent/Wire]] · [[src/Api/Peer]] · [[src/Constants/Agent]] · [[src/Contract/Members]] · [[src/Contract/Operations]] · [[src/Contract/Parameters]] · [[src/Contract/Vocabulary]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Concurrent`, `Std.Json`, `Std.List`, `Std.Math`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/Agent/Mcp]] · [[src/Agent/Runner]]

## Referenced by

[[src/Agent/Mcp]] · [[src/Agent/Runner]] · [[src/Agent/_MOC]]
