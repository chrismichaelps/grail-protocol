---
type: module
path: "@root/src/Agent/Session.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, agent]
---

# Agent.Session

> @Agent.Session.Attached — one participant attached to one fabric: who it acts for, how it reaches the fabric, and where its delivery cursor stands

## Purpose

One participant attached to one fabric: who it acts for, how it reaches the fabric, and where its delivery cursor stands.

## Interface

### Signatures

```pudu
export type Session = {
  peer: Peer.Peer,
  fabric: Str,
  scopeId: Str,
  graph: Str,
  participant: Str,
  claims: Capability.Token,
  cursor: Sync.Cell[Int],
  cursorFile: Option[Str],
  taskId: Option[Str],
  journal: Option[Str]
}
/// A session from the environment: the fabric address, the token or the file holding it, and, when the token does not say, the graph and the participant.
export fn fromEnvironment() -> Result[Session, Str]
/// One operation of the contract, with the session's scope, graph, and participant filled into its parameters unless `params` names them.
export fn call(session: &Session, id: Str, params: &Array[(Str, Json.Json)], body: &Option[Json.Json]) -> Result[Peer.Answer, Str]
/// Milliseconds since the Unix epoch.
export fn now() -> Int
/// The last delivery sequence this participant has processed.
export fn cursorOf(session: &Session) -> Int
/// Records that every delivery up to a sequence was processed, in the cursor file too when one is kept.
export fn advance(session: &Session, sequence: Int) -> ()
/// Records an envelope the participant sent or read while working on a supervised task.
export fn note(session: &Session, id: Str) -> ()
/// The ids a task journal holds, oldest first, each once.
export fn noted(path: Str) -> Array[Str]
```

### Linkage

- **Requires:** [[src/Api/Peer]] · [[src/Constants/Agent]] · [[src/Constants/Cli]] · [[src/Constants/Security]] · [[src/Contract/Parameters]] · [[src/Domain/Capability]] · [[src/Engine/Authority]] · [[src/Engine/Paths]]
- **Standard library:** `Std.Env`, `Std.Io`, `Std.Json`, `Std.Option`, `Std.Result`, `Std.Sync`, `Std.Time`
- **Consumed by:** [[src/Agent/Mcp]] · [[src/Agent/Runner]] · [[src/Agent/Tools]] · [[src/Agent/Wire]] · [[src/Cli/Commands]]

## Referenced by

[[src/Agent/Mcp]] · [[src/Agent/Runner]] · [[src/Agent/Tools]] · [[src/Agent/Wire]] · [[src/Cli/Commands]] · [[src/Agent/_MOC]]
