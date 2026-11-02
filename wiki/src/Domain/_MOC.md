---
type: moc
tags: [moc]
---

# src/Domain

One page per file, each with its interface and the modules it depends on.

- [[src/Domain/Capability]] — signed, expiring, narrowing grants of abilities
- [[src/Domain/Envelope]] — the single message shape of the protocol
- [[src/Domain/Graph]] — participants, edges, and their lookups
- [[src/Domain/Handoff]] — an agent's working context as it leaves one fabric and arrives at another
- [[src/Domain/Identifier]] — what identifiers, names, and kinds may look like
- [[src/Domain/Ledger]] — the hash-linked history of one scope
- [[src/Domain/Lifecycle]] — where a task stands
- [[src/Domain/Mutation]] — an atomic, revision-checked change to a graph
- [[src/Domain/Problem]] — why the fabric refused an operation
- [[src/Domain/Request]] — what each operation asks for, with the token presented for it
- [[src/Domain/Scope]] — everything one scope holds, and nothing of any other
- [[src/Domain/Transfer]] — what the fabric answers about transfers

## Referenced by

[[src/_MOC]]
