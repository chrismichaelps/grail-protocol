---
type: module
path: "@root/src/Domain/Request.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Request

> @Domain.Request.Inputs — what each operation asks for, with the token presented for it

## Purpose

What each operation asks for, with the token presented for it.

## Interface

### Signatures

```pudu
export type Call[T] = { token: Str, scopeId: Str, input: T }
export type Creation = { graph: Str, draft: Mutation.Draft }
export type Change = { graph: Str, mutation: Mutation.Mutation }
export type Sending = { envelope: Envelope.Envelope, body: Json.Json }
export type Pulling = { graph: Str, participant: Str, after: Int, limit: Option[Int], wait: Int }
export type Paging = { after: Int, limit: Option[Int] }
export type Bridging = { graph: Str, participant: Str, message: Json.Json }
export type Granted = { token: Str, expires: Int }
export type Erased = { id: Str, sequence: Int, digest: Str }
export type Traced = { of: Str, entries: Array[Transfer.TraceEntry] }
```

### Linkage

- **Requires:** [[src/Domain/Envelope]] · [[src/Domain/Mutation]] · [[src/Domain/Transfer]]
- **Standard library:** `Std.Json`
- **Consumed by:** [[src/App/Commands]] · [[src/App/Events]] · [[src/App/Handlers]] · [[src/App/Messages]] · [[src/App/Pipeline]] · [[src/Engine/Codec/Views]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Web/Caller]] · [[src/Web/Handlers]]

## Referenced by

[[src/Domain/_MOC]] · [[src/App/Commands]] · [[src/App/Events]] · [[src/App/Handlers]] · [[src/App/Messages]] · [[src/App/Pipeline]] · [[src/Engine/Codec/Views]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Web/Caller]] · [[src/Web/Handlers]]
