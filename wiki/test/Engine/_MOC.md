---
type: moc
tags: [moc]
---

# test/Engine

One page per file, each with its interface and the modules it depends on.

- [[test/Engine/AdmissionTest]] — routing, dependency gating, lifecycles, deduplication, and streams
- [[test/Engine/AuthorityTest]] — tokens verify only in their scope, expire, and only ever narrow when delegated
- [[test/Engine/CompositionTest]] — nested dependency gates and admission-time producer attribution
- [[test/Engine/CustodyTest]] — sealing, expiry, reveal, and reference boundaries of custody
- [[test/Engine/DeliveryTest]] — pages respect their limit, cursors acknowledge, and visibility hides
- [[test/Engine/HandoffTest]] — lifetime, order, expiry, and entry-limit boundaries of handoffs
- [[test/Engine/LedgerTest]] — canonical form, digests, and links match vectors computed elsewhere
- [[test/Engine/MutationsTest]] — graphs change atomically, by revision, and never into a cycle
- [[test/Engine/ShapesTest]] — bodies are read against the contract's shapes

## Referenced by

[[test/_MOC]]
