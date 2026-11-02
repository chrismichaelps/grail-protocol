---
type: architecture
status: ACTIVE
tags: [architecture, security]
---

# Security

| Threat | Control | Where |
| --- | --- | --- |
| Reading or probing another scope | Tokens verify only with the key of the scope a request names; refusal before any lookup | [[src/Engine/Authority]] |
| Acting beyond a grant | Abilities, graph restriction, and audience checked on every operation | [[src/Engine/Authority]], [[src/Services/Fabric]] |
| Widening through delegation | Six checks per link, depth bound, `*` only from the owner | [[src/Engine/Authority]] |
| Forged or altered tokens | HMAC-SHA-256, constant-time comparison | [[src/Engine/Authority]] |
| Replayed envelopes | Unique ids per scope; keyed deduplication | [[src/Engine/Admission]] |
| Rewritten history | Hash-linked ledger, verifiable by any reader | [[src/Engine/Ledger]] |
| Oversized or malformed input | Contract shapes, limits, body bound, head bound | [[src/Engine/Codec/Shapes]], [[src/Main]] |
| Floods | Rate limit keyed by host, concurrency bound, handler deadline, mediator guards | [[src/Web/Router]], [[src/Web/Peers]], [[src/App/Resilience]] |
| Workers held by waiting pulls | Waiting pulls hold at most half the workers | [[src/Services/Runtime]] |
| Quadratic work under the lock | Linear cycle detection; bounded ancestry walks | [[src/Engine/Topology]], [[src/Engine/Causality]] |
| Unbounded memory per scope | Bounded ledger and delivery keys; keys expire with the deduplication window | [[src/Engine/Admission]] |
| Ledger poisoning | Ids the fabric writes are reserved | [[src/Engine/Admission]] |
| A compromised subagent | Revocation of its token and everything delegated from it | [[src/Services/Fabric]] |
| Leaking secrets | The fabric secret is a redacted setting and never logged | [[src/Config/Settings]] |
| Cross-origin reads | Sharing only with listed origins | [[src/Web/Router]] |

[[architecture/ATTACKS]] records the campaign run against these controls.

The fabric secret must hold at least 32 characters. Rotating it invalidates every token of every scope.

## Referenced by

[[architecture/_MOC]] · [[protocol/07-Security]]
