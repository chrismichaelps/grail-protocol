# Security review — reference fabric 0.2.1

This review tested the custody, capability, graph-write, and handoff paths with synthetic credentials. It found real disclosures; passing the previous test suite had not established these boundaries.

| Finding | Correction | Regression evidence |
| --- | --- | --- |
| A delegated participant could mint the reserved owner audience, read executor deliveries, and revoke the root. | Reject non-owner-to-owner transitions during issuance and signed-chain verification. | #25; authority and router delegation suites. |
| The example executor forwarded its authorization header through HTTP redirects. | Refuse redirects and implicit environment proxies on credential-bearing calls. | #26; separate local service/collector tests for five redirect statuses. |
| An executor-named child could reveal a value its issuer could not access. | Require every non-owner issuer to be a current executor in the secret's audience. | #27; failed revelation preserves delivery marks and reveal counts. |
| Queued calls could receive a rotated value after their sender or kind lost permission. | Recheck the current graph, sender, and kind policy at reveal time. | #27; old-policy calls fail and compliant new calls work. |
| Graph, exported handoff, and public secret metadata could carry held values. | Guard writes before journaling or returning them, including incoming values and previous values during rotation. | #30; metadata, state preservation, and strike regressions. |
| Revocation events logged a caller-supplied identifier that could contain sensitive text. | Record the event without the raw identifier. | #35; native information-level log check with an identifier canary. |

## Checks

The combined suite passes 428 assertions. The reviewed changes include router-level attacks, engine regressions, strict documentation generation, executable localhost workflows, and a fresh native HTTP custody check in CI. Four additional executor tests cover direct calls, five redirect statuses, proxy isolation, and unpinned paths. Authority mutation testing killed all 46 selected mutants; custody mutation testing killed all 45 selected mutants, with no invalid or surviving mutants in either run. These are the operators implemented by the repository harness, not every possible faulty implementation.

A redacted current-tree scan for private-key blocks, GitHub token patterns, and AWS access identifiers found only the existing synthetic test fixture. It did not scan every historical artifact or validate credentials with providers. No real credential, external collection endpoint, paid service, or hosted API was used.

The release issue records the exact merge, final assertion count, native HTTP checks, CI run, tag, and static documentation deployment.

## Operating boundaries

- Keep owner and secret-management credentials out of model processes. Participant kinds are configuration, not attestation of the software behind a token.
- Treat `token.delegate` as ordinary participant-identity administration within its graph and abilities. It can issue another participant's ordinary sending/receiving rights. Custody applies an additional issuer-chain restriction before releasing values.
- An authorized executor possesses the value and can misuse it outside Grail. Pin the allowed destination and operations; refusing redirects is part of that boundary.
- The tripwire recognizes documented forms, not arbitrary encodings, encrypted leaks, or short fragments. Detected disclosures receive strikes; negative guesses do not. Separate tokens have separate counters.
- `uses` counts admitted references. Authorized redeliveries may reveal again and are counted. Rotate and revoke provider credentials as well as replacing local bindings.
- The reference store is in memory. Restart clears custody and revocations. This review does not certify a persistence adapter, a compromised host, distributed denial-of-service resistance, or all possible attacks.
- Handoff integrity checks are not independent proof of a foreign producer's identity or its admission decisions. Authenticate origins through an appropriate trust arrangement before treating imported content as authoritative.

The reproduced paths above are covered by regressions. This is a bounded security review, not a claim that the proposal is immune to every attack.
