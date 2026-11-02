---
type: adr
status: ACCEPTED
date: 2026-11-02
decision_risk: HIGH
tags: [adr, contract]
---

# ADR-0002 — The contract file is the only definition of the wire

## Context

A protocol implemented by many teams in many languages needs one machine-readable definition. If code also defines names, the two drift and nobody can say which one is right.

## Decision

`schema/grail.openapi.json` defines every operation, path, status, parameter, member, enumeration, limit, header, and problem code. [[tools/Contract]] projects it into `src/Contract/`; the router, the codecs, the shapes, the vocabularies, the discovery document, and the problem registry read only those projections. `--check` and [[tools/ContractTest]] fail on a stale projection, and [[src/Web/Description]] proves with the standard OpenAPI model that the router serves exactly the contract.

## Consequences

- A change is made in one file, regenerated, and the compiler names every place that must follow.
- The line binding is free: it dispatches the same operations through the same router.
- Constraints the standard OpenAPI model cannot express live as `x-grail-*` members of the contract.

## Alternatives

- **Code-first, exporting a document.** Rejected: the code would become the authority other implementations cannot read.
- **Interpreting the schema at run time.** Rejected: drift would surface only when a request arrives.

## Validation

Predicted: no literal operation, member, or problem code outside `Constants/` and `Contract/`. Review 2027-02-01.

## Referenced by

[[decisions/_MOC]] · [[architecture/CONTRACT]]
