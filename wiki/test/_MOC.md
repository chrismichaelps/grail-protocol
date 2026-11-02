---
type: moc
tags: [moc, test]
---

# test

The suites, organized by the conformance checks of [[protocol/11-Conformance]], and the fixtures they share.

## Folders

- [[test/Engine/_MOC]] — authority, admission, mutations, ledger vectors, delivery, shapes.
- [[test/Web/_MOC]] — the router and the line binding against a real runtime, without sockets.
- [[test/Support/_MOC]] — fixtures and the runner.

The ledger vectors in `test/Fixtures/ledger-vectors.json` were computed with a separate implementation, so they check canonicalization and hashing rather than restating them.

## Referenced by

[[00-INDEX]]
