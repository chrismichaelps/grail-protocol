---
type: specification
chapter: 13
tags: [protocol, specification, portability]
---

# 13. Portability

An agent's useful state is the work it has seen: the tasks it was given, the results it produced, and the notes and observations those results depend on. Inside one fabric that state is the causal ancestry of the agent's envelopes. This chapter defines how that ancestry leaves one fabric and arrives at another, so an agent started in one product can continue in a different product, run by a different organization, without either side trusting the other's database.

A handoff is a document, not a connection. Fabrics never call each other to complete one. Whoever carries it (the agent itself, an orchestrator, or the `grail handoff` command) moves it with the ordinary operations of [[protocol/08-Bindings]].

## 13.1 What travels

`exportHandoff` takes a participant and one to `handoffAnchors` anchor transfers and produces a **handoff**:

| Member | Meaning |
| --- | --- |
| `grail` | The protocol version of the exporting fabric. |
| `handoff` | The handoff id. It is also the id of the ledger entry that records the export, so it shares the scope's transfer id space. |
| `origin` | `fabric`, the exporting fabric's configured name, and the `scope`, `graph`, and `participant` the agent held there. |
| `participant` | The participant as its graph declares it: kind, roles, and abilities. The receiving side decides whether to grant the same. |
| `anchors` | The transfers the export was asked to carry. |
| `entries` | The anchors and every causal ancestor of them, each once, in origin ledger order. |
| `issued`, `expires` | When the handoff was sealed, and the end of its import window. |
| `digest` | `sha256:` and the hex SHA-256 of the canonical form ([[protocol/03-Envelope]]) of the handoff without `digest` and `seal`. |
| `seal` | The origin's attestation of `digest` (13.3). |

Each entry carries its origin `sequence`, `id`, `digest`, `link`, and `previous`, the link of the origin entry before it (empty for the first entry of a ledger). A readable entry also carries `envelope`, the body its digest covers. Two cases carry less:

- **Erased.** `erased` is true and the envelope has no payload. Erasure is never undone by moving a record.
- **Withheld.** An entry the exporting token may not read ([[protocol/07-Security]]) has `withheld` true and no envelope. Its digest and link still travel, so the receiver knows the ancestry is complete without learning what it held back.

The export MUST be refused with `grail.not-found` when an anchor does not exist or is not visible to the token, with `grail.limit-exceeded` when the ancestry exceeds `handoffEntries`, and with `grail.invalid` when `expires` is not after the issue time or is more than `handoffLifetimeMillis` after it. The fabric checks the handoff it built against 13.2 before answering, and appends an entry of kind `handoff.export` whose parents are the anchors, so the origin's own trace shows what left and when.

## 13.2 Integrity

A handoff is **intact** when all of the following hold. Any fabric can check them, because they depend only on the document:

1. `digest` recomputes from the canonical form.
2. Entry sequences strictly increase.
3. An entry carries an envelope exactly when it is not withheld, and that envelope's `id` is the entry's id.
4. Every carried, unerased envelope recomputes to its entry's `digest` ([[protocol/05-Causality]]).
5. Every entry's `link` recomputes from its `previous` and its `digest`.
6. Every parent named by a carried envelope is an entry of the handoff: the ancestry is closed.
7. Every anchor is an entry of the handoff.

A failure yields `grail.integrity` with a detail naming the rule. Integrity proves the handoff is self-consistent. It does not prove who made it: anyone can build an intact document from invented envelopes.

## 13.3 Attestation

Fabrics share no keys, so only the origin can say whether it sealed a handoff. `verifyHandoff` answers that question for any holder of the document, with no token:

| Member | Meaning |
| --- | --- |
| `intact` | Whether 13.2 holds. |
| `attested` | Whether the handoff is intact, names the scope in the request path as its origin scope, and carries the seal this fabric makes for that scope. |
| `expired` | Whether `expires` has passed. |

The reference fabric seals with HMAC-SHA-256 under a key derived from its secret and the origin scope, over the digest. A verifier learns nothing about the scope: the answer is computed from the document and the key, never from stored state, so it is the same whether the scope exists or not.

A receiving party that needs authenticity asks the origin before importing, the way a resource server asks an authorization server about a token. The `grail handoff` command does this and stops when the origin does not attest. A future minor version may add publicly verifiable seals listed in discovery; this version does not claim them.

## 13.4 Import

`importHandoff` presents a handoff for a participant of a graph in the receiving scope. The fabric MUST, in order:

1. Require `handoff.import` for the graph.
2. Refuse with `grail.invalid` when the id in the path is not the body's `handoff`.
3. Refuse with `grail.not-found` when the participant is not in the graph. Import never adds participants; the receiving owner places the agent and grants its abilities first.
4. Check integrity (13.2).
5. Answer the original receipt, with `duplicate` true, when the same id was imported before with the same digest into the same graph. Refuse with `grail.duplicate` when the id is taken by anything else in the scope.
6. Refuse with `grail.expired` when the import window has closed.
7. Append an entry of kind `handoff.import`, from and to the participant, whose payload records the handoff id, digest, origin, anchors, and entry count, and deliver it to the participant.

The imported context is read back with `readHandoff`. The receiving ledger holds one entry for the whole handoff, not a copy of the origin's entries; origin sequence numbers and links keep their meaning only in the origin's chain.

## 13.5 Provenance across fabrics

After import, the participant continues by naming the import entry as a parent. A trace in the receiving fabric reaches that entry, whose payload names the origin and the handoff digest; the stored handoff holds the origin's entries with their digests and links; the origin's ledger holds the matching export entry. Each step can be checked independently, which gives one unbroken line of evidence from a result in the second fabric to the work it rests on in the first.

A participant can move on again. Exporting from the receiving fabric carries the `handoff.import` entry like any other ancestor, so a chain of handoffs across many fabrics keeps every hop.

## 13.6 Threats

| Threat | Control |
| --- | --- |
| Tampering in transit | Integrity (13.2) and the origin's seal. |
| A forged handoff rebuilt to be intact | `verifyHandoff` at the origin answers `attested: false`. |
| Replay into the same scope | One id per scope; a repeat answers the original receipt. |
| Replay long after the fact | The import window, at most `handoffLifetimeMillis`. |
| Leaking what the exporter could not read | Withheld entries carry no envelope. |
| Undoing an erasure by moving data | Erased entries carry no payload. |
| A participant writing a fake import entry | `handoff.export` and `handoff.import` are fabric-written kinds; senders are refused with `grail.forbidden`. |
| The fabric being made to call arbitrary addresses | Fabrics never fetch anything to import; the carrier talks to each fabric. |
| Oversized documents | `handoffBytes` and `handoffEntries`. |

## Referenced by

[[protocol/_MOC]] · [[protocol/01-Overview]] · [[protocol/11-Conformance]] · [[decisions/ADR-0009-portable-handoffs]] · [[src/Engine/Handoff]] · [[src/Services/Handoffs]]
