---
type: module
path: "@root/src/Contract/Schemas.pudu"
layer: 0
generated: true
grammar: "[[grammar/pudu]]"
tags: [module, contract]
---

# Contract.Schemas

> @Contract.Schemas.Generated — the name of every object schema

## Purpose

The name of every object schema. Projected from the contract by [[tools/Contract]]; it is regenerated, never edited, and the contract check fails when it is stale.

## Interface

### Signatures

```pudu
/// The `Selector` schema.
export const SELECTOR: Str = "Selector"
/// The `Delivery` schema.
export const DELIVERY: Str = "Delivery"
/// The `Clock` schema.
export const CLOCK: Str = "Clock"
/// The `Encryption` schema.
export const ENCRYPTION: Str = "Encryption"
/// The `Envelope` schema.
export const ENVELOPE: Str = "Envelope"
/// The `Address` schema.
export const ADDRESS: Str = "Address"
/// The `Accepted` schema.
export const ACCEPTED: Str = "Accepted"
/// The `Receipt` schema.
export const RECEIPT: Str = "Receipt"
/// The `Transfer` schema.
export const TRANSFER: Str = "Transfer"
/// The `TraceEntry` schema.
export const TRACE_ENTRY: Str = "TraceEntry"
/// The `Trace` schema.
export const TRACE: Str = "Trace"
/// The `Participant` schema.
export const PARTICIPANT: Str = "Participant"
/// The `Edge` schema.
export const EDGE: Str = "Edge"
/// The `GraphDraft` schema.
export const GRAPH_DRAFT: Str = "GraphDraft"
/// The `Graph` schema.
export const GRAPH: Str = "Graph"
/// The `MutationStep` schema.
export const MUTATION_STEP: Str = "MutationStep"
/// The `Mutation` schema.
export const MUTATION: Str = "Mutation"
/// The `Delivered` schema.
export const DELIVERED: Str = "Delivered"
/// The `DeliveryPage` schema.
export const DELIVERY_PAGE: Str = "DeliveryPage"
/// The `LedgerEntry` schema.
export const LEDGER_ENTRY: Str = "LedgerEntry"
/// The `LedgerPage` schema.
export const LEDGER_PAGE: Str = "LedgerPage"
/// The `Delegation` schema.
export const DELEGATION: Str = "Delegation"
/// The `Grant` schema.
export const GRANT: Str = "Grant"
/// The `RpcMessage` schema.
export const RPC_MESSAGE: Str = "RpcMessage"
/// The `Discovery` schema.
export const DISCOVERY: Str = "Discovery"
/// The `Health` schema.
export const HEALTH: Str = "Health"
/// The `Problem` schema.
export const PROBLEM: Str = "Problem"
/// The `Token` schema.
export const TOKEN: Str = "Token"
/// The `TokenView` schema.
export const TOKEN_VIEW: Str = "TokenView"
/// The `Revocation` schema.
export const REVOCATION: Str = "Revocation"
/// The `Erasure` schema.
export const ERASURE: Str = "Erasure"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Codec/Token]] · [[test/Engine/ShapesTest]]

## Referenced by

[[src/Contract/_MOC]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Codec/Token]] · [[test/Engine/ShapesTest]]
