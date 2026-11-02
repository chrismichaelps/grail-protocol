---
type: adr
status: ACCEPTED
date: 2026-11-02
decision_risk: MEDIUM
tags: [adr, architecture]
---

# ADR-0005 — Every operation is a mediator message

## Decision

Each contract operation is one request kind of the mediator. Every message passes the recorder, the fault alarm, validation of rules beyond shape (validator package), and a resilience guard (concurrency limit with a bounded queue, and a deadline). Successful changes announce notifications that listeners handle independently. Interfaces call [[src/App/Commands]] and never touch kinds.

## Consequences

- Overload answers `grail.backpressure` with a retry hint instead of queueing without bound.
- Outbound calls to other fabrics use the standard resilience pipeline of the HTTP client: retries, circuit breaker, and timeouts.

## Alternatives

- **Calling services from handlers.** Rejected: every interface would repeat validation and limits.

## Referenced by

[[decisions/_MOC]] · [[src/App/Assembly]]
