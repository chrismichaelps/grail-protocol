---
type: moc
tags: [moc]
---

# src/Engine

One page per file, each with its interface and the modules it depends on.

- [[src/Engine/Admission]] — decides whether one envelope enters a scope, and what it changes
- [[src/Engine/Authority]] — signs, verifies, delegates, and checks capability tokens
- [[src/Engine/Bridge]] — which bridged request a JSON-RPC response answers
- [[src/Engine/Causality]] — the causal ancestors of an envelope
- [[src/Engine/Custody]] — seals secrets, keeps their values out of every envelope, and reveals them only in deliveries to their audience
- [[src/Engine/Delivery]] — deliveries, ledger ranges, and traces read after a cursor
- [[src/Engine/Erasure]] — removes a payload while the chain still proves it existed
- [[src/Engine/Gating]] — whether a task's dependencies produced results among its ancestors
- [[src/Engine/Handoff]] — assembles, seals, and checks handoffs that carry an agent's context between fabrics
- [[src/Engine/Journal]] — records the fabric's own changes, graph mutations and handoffs, in the ledger as fabric-written envelopes
- [[src/Engine/Kinds]] — the behavior of every kind, chosen once by name
- [[src/Engine/Ledger]] — digests of envelopes and links of the scope ledger
- [[src/Engine/Lifecycle]] — the legal moves of a task lifecycle
- [[src/Engine/Mutations]] — applies mutation steps chosen once by operation, then checks the whole graph
- [[src/Engine/Paths]] — the request target of an operation with its parameters filled in
- [[src/Engine/Routing]] — the strategy that turns a selector into recipients, chosen once
- [[src/Engine/Topology]] — cycles and depth of dependency and containment graphs, in linear time

## Folders

- [[src/Engine/Codec/_MOC]]

## Referenced by

[[src/_MOC]]
