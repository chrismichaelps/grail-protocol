---
type: module
path: "@root/src/Engine/Delivery.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Delivery

> @Engine.Delivery.Pages — deliveries, ledger ranges, and traces read after a cursor

## Purpose

Deliveries, ledger ranges, and traces read after a cursor.

## Interface

### Signatures

```pudu
/// The page size a request asked for, bounded by the contract.
export fn pageSize(asked: Option[Int]) -> Int
/// The deliveries for an address after a cursor, and the scope with its delivery mark moved. Passing a cursor acknowledges everything up to it.
export fn pull(state: &Scope.State, address: &Envelope.Address, after: Int, limit: Int, now: Int) -> (Transfer.Page, Scope.State)
/// What was posted to a channel after a cursor, as an authority may read it: envelopes addressed to the channel by id whose kind the reader's subscription carries, the owner reading every kind. Nothing is acknowledged and no secret is revealed.
export fn channel(state: &Scope.State, graph: &Graph.Graph, id: Str, authority: &Capability.Authority, after: Int, limit: Int) -> Transfer.Page
/// The ledger after a cursor.
export fn ledger(state: &Scope.State, after: Int, limit: Int) -> Transfer.Page
/// The causal ancestry of a record, with entries the authority may not read marked hidden.
export fn trace(state: &Scope.State, record: &Ledger.Record, authority: &Capability.Authority) -> Array[Transfer.TraceEntry]
/// Whether an authority may read a record's content: the owner always; `scope` envelopes by any reader of the scope; `graph` envelopes by readers not bound to another graph; `recipients` envelopes only by their source and recipients.
export fn visible(record: &Ledger.Record, authority: &Capability.Authority) -> Bool
```

### Linkage

- **Requires:** [[src/Constants/Security]] · [[src/Constants/Text]] · [[src/Contract/Limits]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Domain/Envelope]] · [[src/Domain/Graph]] · [[src/Domain/Ledger]] · [[src/Domain/Scope]] · [[src/Domain/Transfer]] · [[src/Engine/Causality]]
- **Standard library:** `Std.Map`, `Std.Math`, `Std.Option`
- **Consumed by:** [[src/Engine/Handoff]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]]

## Referenced by

[[src/Engine/_MOC]] · [[src/Engine/Handoff]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[test/Engine/DeliveryTest]]
