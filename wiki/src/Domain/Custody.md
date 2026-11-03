---
type: module
path: "@root/src/Domain/Custody.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Custody

> @Domain.Custody.Secrets — secrets a scope holds for its participants, sealed, and the policy that says who may use them

## Purpose

Secrets a scope holds for its participants, sealed, and the policy that says who may use them.

## Interface

### Signatures

```pudu
export type Deposit =

export type Held =

export type Sealing = { deposit: Deposit, nonce: Bytes, now: Int }
```

### Linkage

- **Requires:** nothing in `src/`
- **Consumed by:** [[src/App/Commands]] · [[src/App/Events]] · [[src/App/Handlers]] · [[src/App/Messages]] · [[src/Domain/Scope]] · [[src/Engine/Codec/Custody]] · [[src/Engine/Custody]] · [[src/Services/Custody]] · [[src/Web/Handlers]] · [[test/Engine/CustodyTest]]

## Referenced by

[[src/Domain/_MOC]] · [[src/App/Commands]] · [[src/App/Events]] · [[src/App/Handlers]] · [[src/App/Messages]] · [[src/Domain/Scope]] · [[src/Engine/Codec/Custody]] · [[src/Engine/Custody]] · [[src/Services/Custody]] · [[src/Web/Handlers]] · [[test/Engine/CustodyTest]]
