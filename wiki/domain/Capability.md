---
type: domain
tags: [domain]
aliases: [Capability]
---

# Capability

- **Definition:** A signed, expiring grant of abilities over a scope or one graph of it, delegable only by narrowing.
- **Canonical name:** Capability token (never API key or session).
- **Not:** An identity; a token says what its holder may do, not who it is.
- **Example:** Token `w1` lets `writer` receive deliveries of graph `team` for one hour.

## Referenced by

[[protocol/07-Security#7.3 Capability tokens]] · [[src/Domain/Capability]] · [[src/Engine/Authority]] · [[domain/_MOC]]
