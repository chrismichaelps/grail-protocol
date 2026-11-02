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

## 11.3 Test vectors

The repository's `test/Fixtures` holds envelopes with their canonical forms and digests, and ledgers with their links. An implementation in any language can check its canonicalization and hashing against them.

## Referenced by

[[protocol/_MOC]]
