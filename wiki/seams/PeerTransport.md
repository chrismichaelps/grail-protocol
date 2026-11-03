---
type: seam
capacity: EXPLORATORY
capacity_score: 2
lifecycle: EXPLORATORY
drift_score: 0
drift_status: HEALTHY
production_adapters: 1
tags: [seam]
---

# PeerTransport (seam)

## Classification

EXPLORATORY: [[src/Api/Peer]] calls a remote fabric over HTTP through the standard resilience pipeline: rate limiter, total timeout, retry that honors `Retry-After`, circuit breaker, and attempt timeout. Two commands consume it: `grail call`, and `grail handoff`, which carries a handoff between two fabrics ([[protocol/13-Portability]]). Fabrics themselves never use it to import; the carrier talks to each fabric.

## Referenced by

[[seams/_MOC]] · [[src/Api/Peer]] · [[src/Cli/Commands]]
