---
type: module
path: "@root/src/Engine/Authority.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Authority

> @Engine.Authority.Tokens — signs, verifies, delegates, and checks capability tokens

## Purpose

Signs, verifies, delegates, and checks capability tokens.

The reserved `owner` audience may be retained only by an owner parent. A non-owner cannot mint it through delegation, even with unchanged abilities. This invariant is checked both at issuance and for every verified chain link, because owner-specific source, inbox, and revocation privileges exceed ordinary participant authority.

## Interface

### Signatures

```pudu
/// The signing key of one scope, derived from the fabric secret.
export fn scopeKey(secret: Str, scopeId: Str) -> Bytes
/// A token's wire form: its encoded claims, a dot, and its encoded signature.
export fn encode(token: &Capability.Token, key: &Bytes) -> Str
/// The claims of a token whose signature verifies under a key.
export fn verify(text: Str, key: &Bytes) -> Result[Capability.Token, Problem.Problem]
/// The claims a token states, read without checking its signature. Only for a client deciding which scope and graph to address; the fabric verifies the token on every call.
export fn claimed(text: Str) -> Option[Capability.Token]
/// What a presented token lets its holder do in a scope, or why it lets them do nothing.
export fn authorize(text: Str, scopeId: Str, secret: Str, now: Int, revoked: &Set[Str]) -> Result[Capability.Authority, Problem.Problem]
/// Whether an authority holds an ability.
export fn permits(authority: &Capability.Authority, ability: Str) -> Bool
/// Nothing, when an authority holds an ability over a graph; otherwise the refusal.
export fn require(authority: &Capability.Authority, ability: Str, graph: Option[Str]) -> Result[(), Problem.Problem]
/// A narrower token for another participant, issued by the authority's holder.
export fn delegate(authority: &Capability.Authority, request: &Capability.Request, secret: Str) -> Result[Str, Problem.Problem]
/// A root token issued by the scope owner.
export fn issue(claims: &Capability.Token, secret: Str) -> Str
/// Whether a child token is a lawful narrowing of its parent.
export fn narrows(parent: &Capability.Token, child: &Capability.Token) -> Bool
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Extras]] · [[src/Constants/Security]] · [[src/Contract/Limits]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Domain/Problem]] · [[src/Engine/Codec/Token]] · [[src/Utils/Canonical]]
- **Standard library:** `Std.Bytes`, `Std.Crypto`, `Std.Json`, `Std.List`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/Agent/Session]] · [[src/Cli/Commands]] · [[src/Engine/Admission]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]]

<!-- authored -->
## Algorithm

1. A token's wire form is the unpadded base64url of its claims' canonical JSON, a dot, and the unpadded base64url of `HMAC-SHA-256(scopeKey, body)`.
2. The scope key is `HMAC-SHA-256(fabricSecret, "grail-scope:" + scope)`, always derived from the scope the request names, never from the claims.
3. `authorize` verifies the token and every token of its chain with that key, requires the root to be issued by the owner, checks scope, window, and revocation of every link, checks each adjacent pair with `narrows`, and bounds the chain by the delegation depth.
4. `delegate` builds the child from the current token, appends the current token to the chain, and refuses unless `narrows` holds.

## Negative Logic

- ❌ Never compare signatures with ordinary equality; `Crypto.bytesMatch` is constant time.
- ❌ Never let a delegated token hold `*`.
- ❌ Never return a different problem for a token of another scope than for a forged one.

## Grill Log

- **Q:** HMAC or public-key signatures? **A:** HMAC per scope as the baseline. **Rationale:** the fabric is the only verifier of its own tokens, keys rotate with the fabric secret, and no key distribution is needed. **Rejected:** mandatory asymmetric signatures, left to an extension.
- **Q:** Carry the chain or look parents up? **A:** Carry it inside the claims. **Rationale:** the token verifies on its own and the signature covers the whole chain. **Rejected:** a server-side parent table, which would need a lookup per request.
- **Q:** 401 or 404 across scopes? **A:** 401, identically for every object. **Rationale:** verification happens before any lookup, so nothing about the other scope can leak. **Rejected:** 404, which would need a lookup first.
<!-- /authored -->

## Referenced by

[[src/Engine/_MOC]] · [[src/Cli/Commands]] · [[src/Engine/Admission]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[test/Engine/AuthorityTest]] · [[test/Support/Fabric]] · [[test/Support/Fixtures]] · [[test/Web/RouterTest]]
