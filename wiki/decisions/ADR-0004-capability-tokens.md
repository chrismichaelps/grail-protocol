---
type: adr
status: ACCEPTED
date: 2026-11-02
decision_risk: HIGH
tags: [adr, security]
---

# ADR-0004 — Per-scope signed tokens with attenuated delegation

## Decision

Tokens are canonical JSON claims signed with HMAC-SHA-256 under a key derived from the fabric secret and the scope a request names. Delegation carries its whole chain inside the claims; every link must narrow its parent in issuer, abilities, graph, and window, and chains are at most eight tokens long.

## Consequences

- Cross-scope requests fail at verification, before any lookup, with one answer.
- Revoking a parent revokes everything delegated from it.
- Rotating the fabric secret invalidates every token.

## Alternatives

- **Opaque tokens in a table.** Rejected: a lookup per request and no offline verification.
- **Asymmetric signatures by default.** Deferred to an extension; only the fabric verifies its own tokens today.

## Validation

[[test/Engine/AuthorityTest]] covers every refusal; mutation testing of [[src/Engine/Authority]] kills all 42 mutants.

## Referenced by

[[decisions/_MOC]] · [[protocol/07-Security]]
