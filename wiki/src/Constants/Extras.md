---
type: module
path: "@root/src/Constants/Extras.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Extras

> @Constants.Extras.Problems — the extra members problem documents carry

## Purpose

The extra members problem documents carry.

## Interface

### Signatures

```pudu
/// The violations of a request that does not match the contract.
export const VIOLATIONS: Str = "violations"
/// Where a violation is.
export const PATH: Str = "path"
/// What a violation is.
export const MESSAGE: Str = "message"
/// The ability a token lacks.
export const ABILITY: Str = "ability"
/// The current revision of a graph.
export const REVISION: Str = "revision"
/// The participants whose results are missing.
export const UNMET: Str = "unmet"
/// The members of a cycle, in order.
export const CYCLE: Str = "cycle"
/// The state a lifecycle stands in.
export const STATE: Str = "state"
/// The parents that are not in the ledger.
export const PARENTS: Str = "parents"
/// The limit that was exceeded.
export const LIMIT: Str = "limit"
/// The versions a fabric supports.
export const SUPPORTED: Str = "supported"
/// Seconds to wait before retrying.
export const RETRY_AFTER: Str = "retryAfter"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/App/Pipeline]] · [[src/Domain/Problem]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Lifecycle]] · [[src/Engine/Mutations]] · [[src/Web/Caller]]

## Referenced by

[[src/Constants/_MOC]] · [[src/App/Pipeline]] · [[src/Domain/Problem]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Codec/Handoff]] · [[src/Engine/Lifecycle]] · [[src/Engine/Mutations]] · [[src/Web/Caller]]
