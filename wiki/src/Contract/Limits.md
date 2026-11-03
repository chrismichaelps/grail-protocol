---
type: module
path: "@root/src/Contract/Limits.pudu"
layer: 0
generated: true
grammar: "[[grammar/pudu]]"
tags: [module, contract]
---

# Contract.Limits

> @Contract.Limits.Generated — every limit the fabric enforces

## Purpose

Every limit the fabric enforces. Projected from the contract by [[tools/Contract]]; it is regenerated, never edited, and the contract check fails when it is stale.

## Interface

### Signatures

```pudu
/// The `envelopeBytes` limit.
export const ENVELOPE_BYTES: Int = 1114112
/// The `payloadBytes` limit.
export const PAYLOAD_BYTES: Int = 1048576
/// The `parents` limit.
export const PARENTS: Int = 64
/// The `identifierLength` limit.
export const IDENTIFIER_LENGTH: Int = 128
/// The `nameLength` limit.
export const NAME_LENGTH: Int = 64
/// The `schemaLength` limit.
export const SCHEMA_LENGTH: Int = 512
/// The `roles` limit.
export const ROLES: Int = 32
/// The `abilities` limit.
export const ABILITIES: Int = 64
/// The `participants` limit.
export const PARTICIPANTS: Int = 1024
/// The `edges` limit.
export const EDGES: Int = 4096
/// The `operations` limit.
export const OPERATIONS: Int = 256
/// The `delegationDepth` limit.
export const DELEGATION_DEPTH: Int = 8
/// The `containmentDepth` limit.
export const CONTAINMENT_DEPTH: Int = 8
/// The `routingPaths` limit.
export const ROUTING_PATHS: Int = 1024
/// The `clockSkewMillis` limit.
export const CLOCK_SKEW_MILLIS: Int = 300000
/// The `deduplicationMillis` limit.
export const DEDUPLICATION_MILLIS: Int = 86400000
/// The `pageDefault` limit.
export const PAGE_DEFAULT: Int = 100
/// The `pageMax` limit.
export const PAGE_MAX: Int = 1000
/// The `priorityMin` limit.
export const PRIORITY_MIN: Int = 0
/// The `priorityMax` limit.
export const PRIORITY_MAX: Int = 9
/// The `priorityDefault` limit.
export const PRIORITY_DEFAULT: Int = 4
/// The `waitMax` limit.
export const WAIT_MAX: Int = 30000
/// The `scopeEntries` limit.
export const SCOPE_ENTRIES: Int = 1000000
/// The `deliveryKeys` limit.
export const DELIVERY_KEYS: Int = 100000
/// The `ancestryMax` limit.
export const ANCESTRY_MAX: Int = 100000
/// The `handoffAnchors` limit.
export const HANDOFF_ANCHORS: Int = 64
/// The `handoffEntries` limit.
export const HANDOFF_ENTRIES: Int = 10000
/// The `handoffLifetimeMillis` limit.
export const HANDOFF_LIFETIME_MILLIS: Int = 86400000
/// The `handoffBytes` limit.
export const HANDOFF_BYTES: Int = 4194304
/// The `secrets` limit.
export const SECRETS: Int = 256
/// The `secretBytes` limit.
export const SECRET_BYTES: Int = 4096
/// The `secretLengthMin` limit.
export const SECRET_LENGTH_MIN: Int = 12
/// The `secretAudience` limit.
export const SECRET_AUDIENCE: Int = 64
/// The `secretStrikes` limit.
export const SECRET_STRIKES: Int = 3
/// The `secretFragment` limit.
export const SECRET_FRAGMENT: Int = 16
/// Every limit by its contract name, for discovery.
export const ALL: Array[(Str, Int)]
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/App/Resilience]] · [[src/Domain/Identifier]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Causality]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Codec/Views]] · [[src/Engine/Custody]] · [[src/Engine/Delivery]] · [[src/Engine/Disguise]] · [[src/Engine/Handoff]] · [[src/Engine/Mutations]] · [[src/Main]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[test/Engine/AdmissionTest]] · [[test/Engine/AuthorityTest]] · [[test/Engine/DeliveryTest]] · [[test/Engine/MutationsTest]] · [[test/Security/CustodyTest]]

## Referenced by

[[src/Contract/_MOC]] · [[src/App/Resilience]] · [[src/Domain/Identifier]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Causality]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Codec/Shapes]] · [[src/Engine/Codec/Views]] · [[src/Engine/Custody]] · [[src/Engine/Delivery]] · [[src/Engine/Disguise]] · [[src/Engine/Handoff]] · [[src/Engine/Mutations]] · [[src/Main]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[test/Engine/AdmissionTest]] · [[test/Engine/AuthorityTest]] · [[test/Engine/DeliveryTest]] · [[test/Engine/MutationsTest]] · [[test/Security/CustodyTest]]
