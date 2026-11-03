---
type: adr
status: ACCEPTED
date: 2026-11-02
decision_risk: HIGH
tags: [adr, protocol, portability]
---

# ADR-0009 — Agents move between fabrics as sealed, self-verifying handoffs

## Context

Up to 1.0 everything an agent knew lived in one fabric. Two products that each ran a fabric could only share work by building their own export format, and nothing stopped either side from rewriting history on the way. That made Grail a better way to run agents inside one system, not a protocol between systems. The ledger already had what portability needs: every envelope has a digest of its canonical form, and every entry has a link computed from the previous link and that digest.

## Decision

Add chapter 13 and protocol 1.1. `exportHandoff` packages a participant's anchors and their full causal ancestry, each entry with its origin digest, link, and previous link, and seals the document's digest. Entries the exporting token cannot read travel withheld, and erased entries travel without payload. `importHandoff` checks integrity without contacting anyone, records one fabric-written `handoff.import` entry, and delivers it to the participant. `verifyHandoff` lets anyone ask the origin whether it sealed a document. `readHandoff` returns the stored document.

Considered and rejected:

- **Fabric-to-fabric push.** The importing fabric fetching from a URL in the document turns every import into a server-side request to an address an attacker chose. A handoff is a document; the carrier talks to each fabric.
- **Copying origin entries into the receiving ledger.** Their sequence numbers and links only mean something in the origin chain. One import entry that names the digest keeps both chains honest.
- **Public-key seals now.** The pinned standard library has no asymmetric signatures. An HMAC seal checked by the origin is honest about who can verify it, and the `seal` member leaves room for a publicly verifiable scheme in a later minor version.
- **Creating the participant on import.** Authority must stay with the receiving owner. Import requires an existing participant.

## Consequences

Software built by different teams can pass an agent's context between their fabrics and prove where it came from. Integrity is universal; authenticity requires one call to the origin, which must be reachable when the receiver wants it. A handoff id shares the scope's transfer id space. The server's body bound grows from one envelope to the contract's `handoffBytes`, which is still bounded and advertised.

## Validation

[[test/Security/HandoffTest]] runs two in-process fabrics with different secrets and names: export, withholding, duplicate and expiry handling, tampering, rehashed forgeries, attestation by the origin only, scope binding of seals, refusal of forged kinds, continued work, and a second hop. [[test/Engine/HandoffTest]] pins the boundaries the mutation run found. Mutation testing of [[src/Engine/Handoff]], [[src/Engine/Codec/Handoff]], and [[src/Services/Handoffs]] kills every mutant. [[tools/Recording]] captures the demonstration in a real terminal.

## Referenced by

[[decisions/_MOC]] · [[protocol/13-Portability]]
