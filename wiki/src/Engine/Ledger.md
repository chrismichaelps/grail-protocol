---
type: module
path: "@root/src/Engine/Ledger.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Ledger

> @Engine.Ledger.Chain — digests of envelopes and links of the scope ledger

## Purpose

Digests of envelopes and links of the scope ledger.

## Interface

### Signatures

```pudu
/// The digest of an envelope body: the hash of its canonical form without the members the fabric adds.
export fn digestOf(body: &Json.Json) -> Str
/// The link that follows `previous` for a digest; an empty `previous` starts the chain.
export fn linkAfter(previous: Str, digest: Str) -> Str
/// The first position whose link does not recompute, or `None` when the whole chain holds.
export fn firstBroken(entries: &Array[Ledger.Entry]) -> Option[Int]
```

### Linkage

- **Requires:** [[src/Constants/Ledger]] · [[src/Contract/Members]] · [[src/Domain/Ledger]] · [[src/Utils/Canonical]]
- **Standard library:** `Std.Crypto`, `Std.Json`
- **Consumed by:** [[src/Engine/Admission]] · [[src/Engine/Journal]] · [[test/Engine/LedgerTest]] · [[test/Security/AttackTest]]

## Referenced by

[[src/Engine/Admission]] · [[src/Engine/Journal]] · [[src/Engine/_MOC]] · [[test/Engine/LedgerTest]] · [[test/Security/AttackTest]]
