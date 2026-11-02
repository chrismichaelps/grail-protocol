---
type: adr
status: ACCEPTED
date: 2026-11-02
decision_risk: HIGH
tags: [adr, license]
---

# ADR-0006 — Apache License 2.0, without exceptions

## Context

Grail is meant to be implemented by many parties, in many languages, inside commercial and open products. Three things are licensed together in this repository: the specification (`wiki/protocol/`), the contract (`schema/grail.openapi.json`), which implementers copy into their own code, and the reference fabric. The license must let anyone implement the protocol without fear of a patent claim from a contributor, and must not push implementers away.

## Decision

The whole repository is under the Apache License 2.0, exactly as published, with only the copyright line of its appendix filled in. No additional exceptions.

## Rationale

| Requirement | Apache-2.0 | MIT | MPL-2.0 | GPL / AGPL |
| --- | --- | --- | --- | --- |
| Explicit patent grant from every contributor | yes | no | yes | yes (v3) |
| Patent retaliation: suing over the protocol ends your license | yes | no | yes | yes (v3) |
| Usable in closed products without releasing their code | yes | yes | file-level copyleft | no |
| Same license as every pinned package and the language | yes | no | no | no |
| Contract can be copied into any codebase | yes | yes | with file-level terms | no |

The deciding property is the patent grant. A protocol is an invitation to implement; an implementer needs assurance that whoever contributed a mechanism, such as dependency gating or delegated tokens, cannot later assert a patent on it. MIT is silent on patents. Copyleft licenses would keep vendors from shipping fabrics or participants, which defeats a protocol meant to be the common way systems talk.

## Consequences

- Apache-2.0 is incompatible with GPLv2-only code. That matters only for someone linking this reference fabric into a GPLv2-only program. Anyone implementing the protocol writes their own code from the specification and the contract, so the protocol itself stays usable everywhere.
- The LLVM exceptions were considered and rejected. They exist for compiler runtime pieces embedded into other people's binaries, which nothing here is.
- No `NOTICE` file is required today; one is added if third-party notices ever need to travel with the code.

## Alternatives

- **MIT.** Rejected: no patent grant.
- **MIT or Apache-2.0, at the user's choice.** Rejected for now: it adds a permissive path without a patent grant to a protocol whose value depends on one.
- **A separate documentation license for the specification (for example CC BY 4.0).** Rejected: the contract and the specification are copied into code, and one license for the repository avoids asking which file falls under which terms.

## Referenced by

[[decisions/_MOC]]
