---
type: moc
tags: [moc]
---

# test/Security

One page per file, each with its interface and the modules it depends on.

- [[test/Security/AttackTest]] — forgery, escalation, isolation, poisoning, abuse, and exhaustion attempts all fail safely
- [[test/Security/CustodyTest]] — an agent uses a key it never sees, and the key never reaches the ledger, a trace, a handoff, or another agent
- [[test/Security/ErasureTest]] — graph restrictions constrain payload erasure without changing refused records
- [[test/Security/DelegationTest]] — a participant cannot mint owner authority to steal custody deliveries or revoke the root
- [[test/Security/CustodyDelegationTest]] — revealing tokens retain their issuers' custody limits and current rotation policy
- [[test/Security/HandoffTest]] — an agent moves between two fabrics, and forged, altered, replayed, or expired handoffs fail

## Referenced by

[[test/_MOC]]
