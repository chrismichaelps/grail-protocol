---
type: seam
capacity: EXPLORATORY
capacity_score: 3
lifecycle: EXPLORATORY
drift_score: 0
drift_status: HEALTHY
production_adapters: 1
tags: [seam]
---

# RpcBridge (seam)

## Classification

EXPLORATORY: [[src/Api/Bridge]] admits one JSON-RPC 2.0 message at a time, using the message classification of the `pudu-lang-mcp` package. A long-lived adapter that runs a tool server as a child process and pulls its deliveries is the expected second adapter.

## Referenced by

[[seams/_MOC]] · [[protocol/10-Bridge]] · [[src/Api/Bridge]] · [[src/Services/Bridge]]
