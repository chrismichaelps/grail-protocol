---
type: module
path: "@root/src/Engine/Codec/Views.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Codec.Views

> @Engine.Codec.Views — the answers of every operation as JSON

## Purpose

The answers of every operation as JSON.

## Interface

### Signatures

```pudu
/// The answer to an accepted envelope.
export fn receipt(answer: &Transfer.Receipt) -> Json.Json
/// One envelope with its lifecycle.
export fn transfer(view: &Transfer.View) -> Json.Json
/// The causal ancestry of an envelope.
export fn trace(of: Str, entries: &Array[Transfer.TraceEntry]) -> Json.Json
/// A page of deliveries.
export fn deliveries(page: &Transfer.Page) -> Json.Json
/// A page of ledger entries.
export fn ledger(page: &Transfer.Page) -> Json.Json
/// A delegated token.
export fn grant(token: Str, expires: Int) -> Json.Json
/// A presented token, described to its holder.
export fn tokenView(token: &Capability.Token, depth: Int) -> Json.Json
/// A revocation.
export fn revocation(token: Str) -> Json.Json { Json.object(&[(Members.REVOCATION_TOKEN, Json.Text(token)), (Members.REVOCATION_REVOKED, Json.Boolean(true))]) }
/// An erasure.
export fn erasure(erased: &Request.Erased) -> Json.Json
/// The liveness answer.
export fn health() -> Json.Json { Json.object(&[(Members.HEALTH_STATUS, Json.Text(Fabric.ALIVE))]) }
/// The discovery document: versions, implementation, bindings, limits, kinds, abilities, and extensions.
export fn discovery() -> Json.Json
/// A stored envelope: its body, its stamp, and no payload once erased.
export fn stored(record: &Ledger.Record) -> Json.Json
```

### Linkage

- **Requires:** [[src/Constants/Fabric]] · [[src/Contract/Limits]] · [[src/Contract/Members]] · [[src/Contract/Version]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Domain/Envelope]] · [[src/Domain/Ledger]] · [[src/Domain/Request]] · [[src/Domain/Transfer]] · [[src/Engine/Codec/Envelope]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Json`, `Std.Option`
- **Consumed by:** [[src/Web/Handlers]]

## Referenced by

[[src/Engine/Codec/_MOC]] · [[src/Web/Handlers]]
