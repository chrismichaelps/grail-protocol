---
type: module
path: "@root/src/Domain/Transfer.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Transfer

> @Domain.Transfer.Views — what the fabric answers about transfers

## Purpose

What the fabric answers about transfers.

## Interface

### Signatures

```pudu
export type Receipt = { id: Str, sequence: Int, digest: Str, recipients: Array[Envelope.Address], state: Option[Str], duplicate: Bool }
export type View = { record: Ledger.Record, state: Option[Str] }
export type TraceEntry = { record: Ledger.Record, hidden: Bool }
export type Page = { records: Array[Ledger.Record], cursor: Int }
```

### Linkage

- **Requires:** [[src/Domain/Envelope]] · [[src/Domain/Ledger]]
- **Consumed by:** [[src/App/Commands]] · [[src/App/Events]] · [[src/App/Messages]] · [[src/Domain/Request]] · [[src/Engine/Codec/Views]] · [[src/Engine/Delivery]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[src/Web/Handlers]] · [[test/Engine/DeliveryTest]]

## Referenced by

[[src/App/Commands]] · [[src/App/Events]] · [[src/App/Messages]] · [[src/Domain/Request]] · [[src/Domain/_MOC]] · [[src/Engine/Codec/Views]] · [[src/Engine/Delivery]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[src/Web/Handlers]] · [[test/Engine/DeliveryTest]]
