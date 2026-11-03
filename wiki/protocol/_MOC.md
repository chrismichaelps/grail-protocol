---
type: moc
tags: [moc, protocol, specification]
aliases: [Specification, Grail specification]
status: DRAFT
version: "1.1"
---

# Grail Protocol Specification

Grail (Graph Routed Agent Information Lattice) is a protocol for exchanging information between participants: models, tools, memory stores, services, people, and other graphs. Every exchange is a transfer of one envelope along an edge of a graph that lives inside one isolated scope, and an agent's context can leave one fabric and continue in another without either trusting the other's storage. Causality, provenance, and authority are part of the wire format rather than conventions layered on top of it.

This specification is normative. The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL are to be read as described in RFC 2119 and RFC 8174 when, and only when, they appear in capitals.

The machine-readable contract of the HTTP binding is [[schema/grail.openapi|schema/grail.openapi.json]]. Where prose and schema disagree on a field name, type, or enumeration, the schema wins and the prose is a defect.

## Chapters

1. [[protocol/01-Overview|Overview]] — goals, non-goals, terminology, and how Grail relates to tool protocols.
2. [[protocol/02-Model|Model]] — scopes, participants, graphs, edges, and the fabric.
3. [[protocol/03-Envelope|Envelope]] — every field, the kind registry, canonical form, and digests.
4. [[protocol/04-Transfer|Transfer]] — routing, delivery guarantees, the lifecycle, deadlines, cancellation, and streams.
5. [[protocol/05-Causality|Causality and provenance]] — clocks, causal parents, dependency gating, the ledger, and tracing.
6. [[protocol/06-Graphs|Graph mutation]] — revisions, the acyclicity rule, and graphs inside graphs.
7. [[protocol/07-Security|Security]] — scope isolation, capability tokens, delegation, and erasure.
8. [[protocol/08-Bindings|Bindings]] — the HTTP binding, the line binding, and discovery.
9. [[protocol/09-Errors|Errors]] — problem documents and the registry of codes.
10. [[protocol/10-Bridge|Tool protocol bridge]] — carrying JSON-RPC tool traffic as envelopes.
11. [[protocol/11-Conformance|Conformance]] — profiles, required behavior, and test vectors.
12. [[protocol/12-Evolution|Versioning and extensions]] — version negotiation and the extension namespace.
13. [[protocol/13-Portability|Portability]] — carrying an agent's context from one fabric to another, with integrity and origin attestation.
14. [[protocol/14-Custody|Custody]] — letting agents use keys by name while values reach only the executors that need them.

## Decisions behind the text

[[decisions/ADR-0001-specification-review]] lists every change made to the original draft and why.

## Referenced by

[[00-INDEX]] · [[decisions/ADR-0001-specification-review]] · [[schema/grail.openapi]]
