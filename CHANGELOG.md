# Changelog

## 0.2.0 — 2026-11-02

### Added

- Protocol 1.1: portable handoffs. `exportHandoff` seals a participant's anchors and their causal ancestry; `importHandoff` checks digests, links, closed ancestry, and anchors before admitting it in another fabric; `verifyHandoff` lets the origin attest its seal; `readHandoff` returns the stored document.
- Reserved kinds `handoff.export` and `handoff.import`, abilities `handoff.export` and `handoff.import`, problem code `grail.integrity`, and the limits `handoffAnchors`, `handoffEntries`, `handoffLifetimeMillis`, and `handoffBytes`.
- Custody: `putSecret`, `listSecrets`, and `deleteSecret`. Participants reference secrets as `{"$secret": name}`; the fabric reveals a value only in deliveries to the secret's audience, refuses any envelope, bridged message, or imported handoff that holds a held value (as written, JSON-escaped, base64, or hex), and enforces each secret's graph, senders, kinds, uses, and expiry. Values are sealed per scope and cannot be read back. Handoffs list the secrets they need. Adds ability `secret.manage`, problem `grail.secret-exposed`, the limits `secrets`, `secretBytes`, `secretLengthMin`, and `secretAudience`, specification chapter 14, and the Custody profile.
- `GRAIL_FABRIC_NAME`, the origin name a fabric seals under, and the `grail handoff` command, which exports, asks the origin to attest, and imports.
- The Portable conformance profile and specification chapter 13.
- Three demonstrations with agent processes: `examples/team` (dependency gates, narrowed tokens, private notes, cascading revocation), `examples/secrets` (an agent using a key it never sees against a local service), and `examples/handoff` (two fabrics passing an agent). Both are recorded in a real Terminal window as MP4 and GIF with macOS's own tools (`tools/Recording`).
- The landing banner uses slow layered waves in place of dots and a ring; the footer's Support link goes to PayPal.

### Validation and compatibility

The suite passes 350 assertions in 17 suites: 41 between two in-process fabrics that share no secret, and 57 for custody. Mutation testing kills every mutant of the handoff and custody engines, codecs, and use cases. A method a path does not offer now answers a `grail.method-not-allowed` problem document instead of plain text, and cross-origin clients may use `DELETE`. Protocol 1.0 requests and envelopes are still accepted. The request body bound is now the contract's `handoffBytes` (4 MiB).

## 0.1.2 — 2026-11-02

### Fixed

- Graph-bound erasure tokens cannot erase another graph's payload, including tokens with an `owner` audience. Refusal preserves the stored transfer; allowed erasure preserves ledger hashes.

### Validation and compatibility

The suite passes 232 assertions, including 14 new erasure checks. A compiled localhost fabric confirms cross-graph HTTP 403, same-graph HTTP 200, and unchanged ledger hashes. Draft protocol 1.0 wire shapes remain compatible. Callers relying on cross-graph erasure must obtain appropriately scoped authority.

The API remains local and the store remains in memory. Cloudflare continues to host static documentation only.

## 0.1.1 — 2026-11-02

### Fixed

- Nested teams enforce dependency gates at every resolved entry and preserve the original producer paths for later results.
- Empty or over-limit routing branches fail before admission; shared recipients receive one delivery.
- Optional trusted-proxy rate limiting falls back to the connection host for missing or blank headers.

### Added

- Practical guides, concept pages, and a concise local quick start.
- Searchable documentation and topic-based API pages generated from OpenAPI.
- Reproducible docgen builds and executable localhost guide checks in CI.
- Project funding links.

### Validation and compatibility

The release passes 218 assertions and the dependency-layer gate, plus the tool suites and documented local workflow checks. Selected composition mutations are killed by regression cases. The wire protocol remains a draft at version 1.0; discovery adds a routing-path resource bound.

The fabric API remains localhost-only and its store remains in memory. Cloudflare hosts static documentation only, with no logo imagery. The repository remains private for invited testers.
