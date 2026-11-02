---
type: module
path: "@root/src/Constants/Security.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Security

> @Constants.Security.Authority — names and labels of the token scheme

## Purpose

Names and labels of the token scheme.

## Interface

### Signatures

```pudu
/// The issuer and audience that stand for the scope owner.
export const OWNER: Str = "owner"
/// The label mixed into every scope key.
export const SCOPE_KEY_LABEL: Str = "grail-scope:"
/// What separates a token's body from its signature.
export const TOKEN_SEPARATOR: Str = "."
/// The scheme of the authorization header.
export const BEARER_PREFIX: Str = "Bearer "
/// The fewest characters a fabric secret may have.
export const SECRET_LENGTH_MIN: Int = 32
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Api/Peer]] · [[src/Cli/Commands]] · [[src/Config/Settings]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Delivery]] · [[src/Services/Fabric]] · [[src/Web/Caller]] · [[src/Web/Lines]] · [[test/Engine/AuthorityTest]] · [[test/Support/Fabric]] · [[test/Support/Fixtures]] · [[test/Web/RouterTest]]

## Referenced by

[[src/Api/Peer]] · [[src/Cli/Commands]] · [[src/Config/Settings]] · [[src/Constants/_MOC]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Delivery]] · [[src/Services/Fabric]] · [[src/Web/Caller]] · [[src/Web/Lines]] · [[test/Engine/AuthorityTest]] · [[test/Support/Fabric]] · [[test/Support/Fixtures]] · [[test/Web/RouterTest]]
