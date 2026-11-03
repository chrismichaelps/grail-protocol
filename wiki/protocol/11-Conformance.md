---
type: specification
chapter: 11
tags: [protocol, specification]
---

# 11. Conformance

## 11.1 Profiles

| Profile | Requires |
| --- | --- |
| **Participant** | Producing envelopes that validate against the contract; honoring lifecycles for tasks it receives; tolerating duplicate deliveries under `at-least-once`. |
| **Fabric Core** | Chapters 2 through 7 and 9; the HTTP binding; discovery. |
| **Fabric Full** | Fabric Core plus the line binding, the bridge, graphs inside graphs, and erasure. |
| **Portable** | Fabric Core plus chapter 13: export, import, reading, and verifying handoffs. |
| **Custody** | Fabric Core plus chapter 14: references, delivery-time reveal, the tripwire, and write-only storage. |

A fabric claims a profile in its discovery document under `fabric.profiles`.

## 11.2 Required checks

A fabric conforms only if each of the following holds. The reference implementation's test suite is organized under these headings.

1. An envelope that violates the contract is refused with `grail.invalid` and nothing is appended.
2. A token for scope `A` presented to scope `B` yields `grail.unauthorized` for every operation, identically whether `B`, or the object named inside it, exists or not.
3. A delegated token with wider abilities, a longer lifetime, a different graph, or a broken issuer chain is refused.
4. A mutation that closes a dependency cycle is refused with `grail.cycle` and the graph's revision does not change.
5. A stale `expectedRevision` is refused with `grail.revision-conflict`.
6. A task whose dependencies have no result among its ancestors is refused with `grail.dependency-unmet`.
7. Every lifecycle transition outside 4.4 is refused with `grail.invalid-transition`.
8. A repeated `effectively-once` key with the same envelope answers the original acceptance; with a different envelope, `grail.key-reused`.
9. Every ledger link recomputes from the digests, and every digest recomputes from the canonical form.
10. Deliveries never exceed the requested limit, and a cursor acknowledges everything up to it.

For Fabric Full, nested-graph conformance additionally requires that entry dependencies cannot be bypassed, a verified nested completion can satisfy an enclosing participant's dependency, unrelated inner results cannot do so, later graph mutations preserve admission-time attribution, and empty or over-limit expansions fail without a ledger append.

Fabric Full erasure checks MUST include a graph-bound token attempting to erase another graph's payload, including an `owner` audience. Both attempts yield `grail.forbidden` without changing the record. Same-graph erasure and erasure by an unbound owner succeed; the digest and link remain unchanged.

For Portable, a fabric additionally conforms only if each of the following holds, checked between two fabrics that share no secret:

1. A handoff it exports passes 13.2 and carries every ancestor of its anchors once, in ledger order.
2. An ancestor the exporting token may not read travels withheld, without its envelope.
3. A changed envelope, digest, link, order, anchor, or missing parent is refused with `grail.integrity` and nothing is appended.
4. `verifyHandoff` attests only handoffs it sealed for the scope in the path; a rehashed forgery is intact and not attested.
5. Importing the same handoff twice answers the original receipt; any other use of the id yields `grail.duplicate`.
6. An expired handoff yields `grail.expired`; a lifetime above `handoffLifetimeMillis` is refused at export.
7. Senders cannot submit `handoff.export` or `handoff.import`.
8. A result in the receiving fabric that names the import entry as a parent traces back to it.

For Custody, a fabric additionally conforms only if each of the following holds:

1. No answer of any operation other than `pullDeliveries` contains a held value, and a deposit's own answer does not either.
2. A reference is revealed only in deliveries to members of the secret's audience.
3. An envelope, bridged message, or imported handoff that holds a value in any form of 14.3 is refused with `grail.secret-exposed` and nothing is appended. Each such refusal strikes a non-owner token, and the token is revoked at `secretStrikes`.
4. References outside the graph, after expiry, past the last use, from an unlisted sender, in an unlisted kind, or to any recipient outside the audience are refused.
5. Rotation reveals the new value; deletion stops revealing at once.
6. A handoff lists the secrets it needs and carries no value.
7. An audience member that is not a `tool` or `service` participant is refused at deposit, and never revealed a value at delivery.
8. Every reveal is counted on the secret.

## 11.3 Test vectors

The repository's `test/Fixtures` holds envelopes with their canonical forms and digests, and ledgers with their links. An implementation in any language can check its canonicalization and hashing against them.

## Referenced by

[[protocol/_MOC]]
