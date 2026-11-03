---
type: module
path: "@root/src/Agent/Wire.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, agent]
---

# Agent.Wire

> @Agent.Wire.Envelopes — the envelopes an attached participant writes, and the compact form a model reads them in

## Purpose

The envelopes an attached participant writes, and the compact form a model reads them in.

## Interface

### Signatures

```pudu
export type Draft = { target: Json.Json, kind: Str, payload: Option[Json.Json], parents: Array[Str], schema: Option[Str], visibility: Option[Str], key: Option[Str], priority: Option[Int], deadline: Option[Int] }
/// A fresh transfer id for this participant: its id, the time, and random bytes, so ids sort roughly by creation and never collide.
export fn freshId(session: &Session.Session) -> Str
/// The envelope a draft becomes when this participant sends it under an id.
export fn envelope(session: &Session.Session, id: Str, draft: &Draft) -> Json.Json
/// A selector naming one participant or channel.
export fn toParticipant(id: Str) -> Json.Json
/// The payload of prose, structured content, or both: the data with the prose added under `text`.
export fn payloadOf(text: Option[Str], data: Option[Json.Json]) -> Option[Json.Json]
/// The prose of a payload: its `text` member, or the payload itself written out.
export fn proseOf(payload: &Option[Json.Json]) -> Str
/// One delivered or posted envelope as a model needs it: where it sits, who sent it, what it is, what it builds on, and, when it reached this participant through a channel, which one.
export fn compact(session: &Session.Session, sequence: Int, written: &Json.Json) -> Json.Json
/// A page of deliveries or posts in compact form, with the cursor to pass back.
export fn page(session: &Session.Session, body: &Json.Json) -> Json.Json
```

### Linkage

- **Requires:** [[src/Agent/Session]] · [[src/Constants/Agent]] · [[src/Constants/Fabric]] · [[src/Contract/Members]] · [[src/Contract/Vocabulary]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Bytes`, `Std.Json`, `Std.Option`, `Std.Random`, `Std.Result`
- **Consumed by:** [[src/Agent/Runner]] · [[src/Agent/Tools]]

## Referenced by

[[src/Agent/Runner]] · [[src/Agent/Tools]] · [[src/Agent/_MOC]]
