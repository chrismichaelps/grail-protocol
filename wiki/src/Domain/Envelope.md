---
type: module
path: "@root/src/Domain/Envelope.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Envelope

> @Domain.Envelope.Message — the single message shape of the protocol

## Purpose

The single message shape of the protocol.

## Interface

### Signatures

```pudu
export type Selector
export type Address = { graph: Str, participant: Str }
export type Delivery = { mode: Str, key: Option[Str] }
export type Clock = { wall: Int, counter: Int, node: Str }
export type Encryption = { scheme: Str, recipients: Array[Str] }
export type Envelope = { … }
export type Stamp = { sequence: Int, digest: Str, accepted: Int }
```

### Linkage

- **Requires:** nothing inside the fabric
- **Standard library:** `Std.Json`
- **Consumed by:** [[src/Domain/Ledger]] · [[src/Domain/Lifecycle]] · [[src/Domain/Request]] · [[src/Domain/Transfer]] · [[src/Engine/Admission]] · [[src/Engine/Bridge]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Views]] · [[src/Engine/Delivery]] · [[src/Engine/Erasure]] · [[src/Engine/Journal]] · [[src/Engine/Routing]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[src/Validation/Envelope]] · [[src/Web/Handlers]] · [[test/Engine/AdmissionTest]] · [[test/Engine/DeliveryTest]] · [[test/Engine/LedgerTest]] · [[test/Engine/ShapesTest]]

## Referenced by

[[src/Domain/Ledger]] · [[src/Domain/Lifecycle]] · [[src/Domain/Request]] · [[src/Domain/Transfer]] · [[src/Domain/_MOC]] · [[src/Engine/Admission]] · [[src/Engine/Bridge]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Views]] · [[src/Engine/Delivery]] · [[src/Engine/Erasure]] · [[src/Engine/Journal]] · [[src/Engine/Routing]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[src/Validation/Envelope]] · [[src/Web/Handlers]] · [[test/Engine/AdmissionTest]] · [[test/Engine/DeliveryTest]] · [[test/Engine/LedgerTest]] · [[test/Engine/ShapesTest]]
