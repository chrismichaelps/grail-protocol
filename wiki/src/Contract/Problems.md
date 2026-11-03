---
type: module
path: "@root/src/Contract/Problems.pudu"
layer: 0
generated: true
grammar: "[[grammar/pudu]]"
tags: [module, contract]
---

# Contract.Problems

> @Contract.Problems.Generated — the registry of problem codes

## Purpose

The registry of problem codes. Projected from the contract by [[tools/Contract]]; it is regenerated, never edited, and the contract check fails when it is stale.

## Interface

### Signatures

```pudu
export type Entry = { code: Str, status: Int, title: Str }
/// Invalid request (400).
export const INVALID: Str = "grail.invalid"
/// Unauthorized (401).
export const UNAUTHORIZED: Str = "grail.unauthorized"
/// Forbidden (403).
export const FORBIDDEN: Str = "grail.forbidden"
/// Not found (404).
export const NOT_FOUND: Str = "grail.not-found"
/// Method not allowed (405).
export const METHOD_NOT_ALLOWED: Str = "grail.method-not-allowed"
/// Duplicate (409).
export const DUPLICATE: Str = "grail.duplicate"
/// Revision conflict (409).
export const REVISION_CONFLICT: Str = "grail.revision-conflict"
/// Delivery key reused (409).
export const KEY_REUSED: Str = "grail.key-reused"
/// Too large (413).
export const TOO_LARGE: Str = "grail.too-large"
/// No route (422).
export const NO_ROUTE: Str = "grail.no-route"
/// Dependency unmet (422).
export const DEPENDENCY_UNMET: Str = "grail.dependency-unmet"
/// Cycle (422).
export const CYCLE: Str = "grail.cycle"
/// Invalid transition (422).
export const INVALID_TRANSITION: Str = "grail.invalid-transition"
/// Unknown parent (422).
export const UNKNOWN_PARENT: Str = "grail.unknown-parent"
/// Integrity failure (422).
export const INTEGRITY: Str = "grail.integrity"
/// Secret exposed (422).
export const SECRET_EXPOSED: Str = "grail.secret-exposed"
/// Limit exceeded (422).
export const LIMIT_EXCEEDED: Str = "grail.limit-exceeded"
/// Clock skew (422).
export const CLOCK_SKEW: Str = "grail.clock-skew"
/// Expired (422).
export const EXPIRED: Str = "grail.expired"
/// Unsupported version (426).
export const UNSUPPORTED_VERSION: Str = "grail.unsupported-version"
/// Backpressure (429).
export const BACKPRESSURE: Str = "grail.backpressure"
/// Unavailable (503).
export const UNAVAILABLE: Str = "grail.unavailable"
/// Every registered problem, in contract order.
export const ALL: Array[Entry]
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Api/Bridge]] · [[src/App/Pipeline]] · [[src/Domain/Problem]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Custody]] · [[src/Engine/Erasure]] · [[src/Engine/Handoff]] · [[src/Engine/Lifecycle]] · [[src/Engine/Mutations]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Services/Runtime]] · [[src/Services/Store]] · [[src/Web/Caller]] · [[src/Web/Lines]] · [[src/Web/Router]] · [[test/Engine/AdmissionTest]] · [[test/Engine/AuthorityTest]] · [[test/Engine/CustodyTest]] · [[test/Engine/MutationsTest]] · [[test/Security/AttackTest]] · [[test/Security/CustodyTest]] · [[test/Security/HandoffTest]] · [[test/Web/RouterTest]]

## Referenced by

[[src/Contract/_MOC]] · [[src/Api/Bridge]] · [[src/App/Pipeline]] · [[src/Domain/Problem]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Custody]] · [[src/Engine/Erasure]] · [[src/Engine/Handoff]] · [[src/Engine/Lifecycle]] · [[src/Engine/Mutations]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Services/Runtime]] · [[src/Services/Store]] · [[src/Web/Caller]] · [[src/Web/Lines]] · [[src/Web/Router]] · [[test/Engine/AdmissionTest]] · [[test/Engine/AuthorityTest]] · [[test/Engine/CustodyTest]] · [[test/Engine/MutationsTest]] · [[test/Security/AttackTest]] · [[test/Security/CustodyTest]] · [[test/Security/HandoffTest]] · [[test/Web/RouterTest]]
