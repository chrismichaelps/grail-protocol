---
type: module
path: "@root/src/Domain/Handoff.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Handoff

> @Domain.Handoff.Portable — an agent's working context as it leaves one fabric and arrives at another

## Purpose

An agent's working context as it leaves one fabric and arrives at another.

## Interface

### Signatures

```pudu
export type Origin = { fabric: Str, scopeId: Str, graph: Str, participant: Str }

export type Asked = { graph: Str, participant: Str, id: Str, transfers: Array[Str], expires: Option[Int] }

export type Arriving = { graph: Str, participant: Str, id: Str, bundle: Json.Json }

export type Presented = { id: Str, bundle: Json.Json }

export type Stored = { id: Str, graph: Str, direction: Str, digest: Str, entries: Int, recorded: Str, sequence: Int, bundle: Json.Json }

export type Receipt = { handoff: Str, id: Str, sequence: Int, digest: Str, entries: Int, duplicate: Bool }

export type Check = { handoff: Str, digest: Str, intact: Bool, attested: Bool, expired: Bool }
```

### Linkage

- **Requires:** nothing in `src/`
- **Standard library:** `Std.Json`
- **Consumed by:** [[src/App/Commands]] · [[src/App/Events]] · [[src/App/Handlers]] · [[src/App/Messages]] · [[src/Domain/Scope]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Handoff]] · [[src/Services/Handoffs]] · [[src/Web/Handlers]] · [[test/Engine/HandoffTest]]

## Referenced by

[[src/Domain/_MOC]] · [[src/App/Commands]] · [[src/App/Events]] · [[src/App/Handlers]] · [[src/App/Messages]] · [[src/Domain/Scope]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Handoff]] · [[src/Services/Handoffs]] · [[src/Web/Handlers]] · [[test/Engine/HandoffTest]]
