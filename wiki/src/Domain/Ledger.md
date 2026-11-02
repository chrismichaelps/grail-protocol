---
type: module
path: "@root/src/Domain/Ledger.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Ledger

> @Domain.Ledger.Record — the hash-linked history of one scope

## Purpose

The hash-linked history of one scope.

## Interface

### Signatures

```pudu
export type Entry = { sequence: Int, id: Str, digest: Str, link: Str }
export type Record = { … }
```

### Linkage

- **Requires:** [[src/Domain/Envelope]]
- **Standard library:** `Std.Json`
- **Consumed by:** [[src/Domain/Scope]] · [[src/Domain/Transfer]] · [[src/Engine/Admission]] · [[src/Engine/Bridge]] · [[src/Engine/Causality]] · [[src/Engine/Codec/Views]] · [[src/Engine/Delivery]] · [[src/Engine/Erasure]] · [[src/Engine/Handoff]] · [[src/Engine/Journal]] · [[src/Engine/Ledger]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[test/Engine/AdmissionTest]] · [[test/Engine/DeliveryTest]] · [[test/Engine/LedgerTest]] · [[test/Security/AttackTest]]

## Referenced by

[[src/Domain/_MOC]] · [[src/Domain/Scope]] · [[src/Domain/Transfer]] · [[src/Engine/Admission]] · [[src/Engine/Bridge]] · [[src/Engine/Causality]] · [[src/Engine/Codec/Views]] · [[src/Engine/Delivery]] · [[src/Engine/Erasure]] · [[src/Engine/Handoff]] · [[src/Engine/Journal]] · [[src/Engine/Ledger]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[test/Engine/AdmissionTest]] · [[test/Engine/DeliveryTest]] · [[test/Engine/LedgerTest]] · [[test/Security/AttackTest]]
