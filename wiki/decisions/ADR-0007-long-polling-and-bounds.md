---
type: adr
status: ACCEPTED
date: 2026-11-02
decision_risk: MEDIUM
tags: [adr, delivery, security]
---

# ADR-0007 — Waiting pulls and per-scope bounds

## Context

Participants run everywhere: laptops, private networks, serverless functions, other continents. A fabric that pushes to them needs an address it can reach and credentials to reach it with, which most of them do not have. Plain pulls work everywhere but make every idle agent poll.

## Decision

A pull may wait up to thirty seconds for a delivery to arrive (`wait`). Waiting pulls may hold at most half the fabric's workers; a pull that finds no free place answers immediately, and the client pulls again. Each scope is bounded in ledger entries, live delivery keys, and the ancestry walked to gate one task, with the bounds published in the contract.

## Consequences

- Any participant that can make an outgoing HTTPS request can take part in real time.
- A burst of idle agents cannot starve the fabric of workers.
- Push delivery remains possible as a later minor version without changing the pull contract.

## Alternatives

- **Push with callbacks.** Deferred: it needs reachable participants and callback authentication.
- **Unbounded waits.** Rejected by the attack campaign ([[architecture/ATTACKS]]).

## Referenced by

[[decisions/_MOC]] · [[architecture/ATTACKS]]
