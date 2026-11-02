---
type: moc
tags: [moc, domain]
---

# Domain

The vocabulary of the protocol. Every name in code and pages is one of these terms.

- [[domain/Scope]] — The isolation boundary owned by one principal; every other object lives inside exactly one scope.
- [[domain/Participant]] — Anything that sends or receives envelopes: an agent, a tool, a memory store, a person, a service, or a graph.
- [[domain/Graph]] — A versioned set of participants and the edges between them, inside one scope.
- [[domain/Edge]] — A directed link that either authorizes flow (`flow`) or declares that work waits on another participant (`dependency`).
- [[domain/Envelope]] — The single message shape of the protocol.
- [[domain/Transfer]] — One envelope moving along edges, from acceptance to delivery, with its lifecycle when it has one.
- [[domain/Lifecycle]] — Where a task stands: submitted, working, input-required, or one of five final states.
- [[domain/Ledger]] — The append-only, hash-linked record of every accepted envelope of a scope.
- [[domain/Capability]] — A signed, expiring grant of abilities over a scope or one graph of it, delegable only by narrowing.
- [[domain/Fabric]] — The server side of the protocol: it hosts scopes, routes transfers, keeps ledgers, and enforces isolation.
- [[domain/Mutation]] — An atomic, revision-checked list of graph changes.
- [[domain/Problem]] — A refusal: a registered code, its status and title from the contract, a detail for people, and extra members.
- [[domain/Address]] — One participant of one graph, the unit deliveries are addressed to.
- [[domain/Clock]] — A hybrid logical clock reading used to order a trace for people.

## Referenced by

[[00-INDEX]] · [[protocol/01-Overview]]
