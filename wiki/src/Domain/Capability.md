---
type: module
path: "@root/src/Domain/Capability.pudu"
layer: 2
grammar: "[[grammar/pudu]]"
tags: [module, domain]
---

# Domain.Capability

> @Domain.Capability.Grant — signed, expiring, narrowing grants of abilities

## Purpose

Signed, expiring, narrowing grants of abilities.

## Interface

### Signatures

```pudu
export type Token = { … }
export type Authority = { scopeId: Str, graph: Option[Str], audience: Str, abilities: Array[Str], token: Str, chain: Array[Token] }
export type Request = { id: Str, audience: Str, graph: Option[Str], abilities: Array[Str], notBefore: Int, expires: Int }
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/App/Commands]] · [[src/App/Handlers]] · [[src/App/Messages]] · [[src/App/Pipeline]] · [[src/Cli/Commands]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Token]] · [[src/Engine/Codec/Views]] · [[src/Engine/Delivery]] · [[src/Engine/Handoff]] · [[src/Services/Fabric]] · [[src/Validation/Delegation]] · [[src/Web/Handlers]] · [[test/Engine/AuthorityTest]] · [[test/Engine/DeliveryTest]] · [[test/Support/Fabric]] · [[test/Support/Fixtures]] · [[test/Web/RouterTest]]

## Referenced by

[[src/Domain/_MOC]] · [[src/App/Commands]] · [[src/App/Handlers]] · [[src/App/Messages]] · [[src/App/Pipeline]] · [[src/Cli/Commands]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Token]] · [[src/Engine/Codec/Views]] · [[src/Engine/Delivery]] · [[src/Engine/Handoff]] · [[src/Services/Fabric]] · [[src/Validation/Delegation]] · [[src/Web/Handlers]] · [[test/Engine/AuthorityTest]] · [[test/Engine/DeliveryTest]] · [[test/Support/Fabric]] · [[test/Support/Fixtures]] · [[test/Web/RouterTest]]
