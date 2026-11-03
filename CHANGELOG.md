# Changelog

## 0.3.2 — 2026-11-03

### Documentation and examples

- README recording: a real Slack task reaches a hosted Codex CLI worker through the local Grail API, and its generated Python returns to the same Slack thread. The 51-second edited walkthrough uses actual Slack desktop captures and CLI output, with a compact GIF preview. No Studio footage is used.
- Public exchange receipts retain four envelope digests and ledger links, task/result deduplication responses, the source-impersonation refusal, and causal ancestry. CI recomputes the hashes and runs the recorded code’s 12 assertions.
- A macOS encoder creates MP4/GIF walkthroughs from captured application states with explicit captions and pacing. The Slack gateway in this recording is session-operated; no background listener is included.

Runtime behavior and protocol 1.2 are unchanged. Cloudflare serves static documentation and media; the API stays local.

## 0.3.1 — 2026-11-03

### Added

- The channel viewer proves every showcase step instead of narrating it. A **Showcase** screen lists the 15 steps with what each checked and recorded requests with the fabric's real answer, refusals and problem codes included. A **Trace** pane follows any message back to its first cause. A **Ledger** screen recomputes every digest and hash link with the browser's own SHA-256, and can tamper with an entry to show the change being caught.
- `RECORD=path examples/channels/showcase.sh` writes that recording. Tokens are never written, the deploy key is replaced in every form the run uses it, and the file is refused if either would appear.

Runtime behavior and protocol 1.2 are unchanged.

## 0.3.0 — 2026-11-03

### Added

- Protocol 1.2: channels. A participant of kind `channel` hands each post to the subscribers its edges name, leaving out the sender, and `readChannel` reads its posts back without acknowledging anything. Only the owner and subscribers may read a channel; secrets stay references in its history.
- `grail agent` serves a participant's tools to hosted coding agents over standard input and output: who it is, its inbox, sending, answering, channels, waiting on a task, and tracing.
- `grail run --exec CMD` keeps a participant attached and starts a hosted agent for each task, answering with its output or its failure when the agent does not answer itself. Work sent for a task descends from it, and the answer names everything the agent sent and read.
- `examples/channels`: a studio graph with `#general`, `#reviews`, and `#builds`, `attach.sh`, which attaches a hosted agent as any participant, and `showcase.sh`, which walks the studio through every part of the protocol in 15 self-checking steps, narrated into `#general`.
- A task posted to a channel is taken by the first subscriber to report progress or answer; the fabric refuses every other subscriber from then on, in the same atomic step.
- A post to a channel nobody else hears yet is kept for later readers; only a task nobody could answer is refused.
- `grail_send` takes `priority` and `deadline_seconds`, and documents cancelling delegated work.
- A channel viewer on the documentation site that watches channels on the visitor's own fabric, with a recorded run of two hosted agents.
- Discovery advertises the `custody` and `channels` profiles.

### Fixed

- Browser preflight requests from listed origins are answered with `204`; before, no page could send a token even with `GRAIL_ALLOWED_ORIGINS` set.
- The peer client no longer cuts long polls at 10 seconds per attempt and 30 per call.

### Validation and compatibility

The suite passes 521 assertions in 21 suites. Mutation runs kill every mutant in the routing and delivery engines and in the new admission code. Two separate hosted agent processes completed a delegated review through `#reviews` against a running fabric. Protocol 1.0 and 1.1 envelopes and requests are accepted unchanged; a graph without channels behaves exactly as before. The API remains local and the store remains in memory; Cloudflare hosts static documentation only.

## 0.2.2 — 2026-11-02

### Documentation

- Quick-start, contribution, and README access instructions now reflect the public repository.
- Quick-start prerequisites link Pudu 0.1.3 and name Git, OpenSSL, and curl.
- An anonymous clone and the documented localhost health/create/read/duplicate workflow were verified, including owner-token file permissions and Git ignore behavior.

Runtime behavior and draft protocol 1.1 are unchanged. The API remains local; Cloudflare hosts static documentation only.

## 0.2.1 — 2026-11-02

### Fixed

- Non-owner tokens cannot delegate the reserved owner principal.
- Revocation logs omit raw caller-supplied token identifiers.
- Custody revelation preserves issuer-chain authority and checks the current sender/kind policy after rotation.
- Graph journals, exported handoff metadata, and public secret metadata cannot carry held values.
- The secrets executor refuses redirects and implicit environment proxies on credential-bearing calls.

### Validation and compatibility

The suite passes 428 assertions. Authority and custody mutation runs killed all 46 and 45 selected mutants, with no invalid or surviving mutants. CI now tests native localhost custody boundaries and the example executor against a separate local redirect collector.

Draft protocol 1.1 wire shapes are unchanged. Unsafe delegation and metadata flows now refuse; issue executor tokens directly from the owner or an already authorized executor. The [security review](wiki/architecture/SECURITY-REVIEW-2026-11-02.md) records the findings and operating limits. The API remains local and the store remains in memory; Cloudflare hosts static documentation only.

## 0.2.0 — 2026-11-02

### Added

- Protocol 1.1: portable handoffs. `exportHandoff` seals a participant's anchors and their causal ancestry; `importHandoff` checks digests, links, closed ancestry, and anchors before admitting it in another fabric; `verifyHandoff` lets the origin attest its seal; `readHandoff` returns the stored document.
- Reserved kinds `handoff.export` and `handoff.import`, abilities `handoff.export` and `handoff.import`, problem code `grail.integrity`, and the limits `handoffAnchors`, `handoffEntries`, `handoffLifetimeMillis`, and `handoffBytes`.
- Custody: `putSecret`, `listSecrets`, and `deleteSecret`. Participants reference secrets as `{"$secret": name}`; the fabric reveals a value only in deliveries to the secret's audience, refuses any envelope, bridged message, or imported handoff that holds a held value (as written, JSON-escaped, base64, or hex), and enforces each secret's graph, senders, kinds, uses, and expiry. Values are sealed per scope and cannot be read back. Only `tool` and `service` participants may be an audience. Fragments, every base64 alignment, percent-encoding, both hex cases, and reversal are caught too. Each caught leak strikes the sending token, and the third strike revokes it with its delegates. Every reveal is counted. Handoffs list the secrets they need. Adds ability `secret.manage`, problem `grail.secret-exposed`, the limits `secrets`, `secretBytes`, `secretLengthMin`, `secretAudience`, `secretFragment`, and `secretStrikes`, specification chapter 14, and the Custody profile.
- `GRAIL_FABRIC_NAME`, the origin name a fabric seals under, and the `grail handoff` command, which exports, asks the origin to attest, and imports.
- The Portable conformance profile and specification chapter 13.
- Three demonstrations with agent processes: `examples/team` (dependency gates, narrowed tokens, private notes, cascading revocation), `examples/secrets` (an agent using a key it never sees against a local service), and `examples/handoff` (two fabrics passing an agent). Both are recorded in a real Terminal window as MP4 and GIF with macOS's own tools (`tools/Recording`).
- The landing banner uses slow layered waves in place of dots and a ring; the footer's Support link goes to PayPal.

### Validation and compatibility

The suite passes 375 assertions in 18 suites: 41 between two in-process fabrics that share no secret, and 82 for custody and its tripwire. Mutation testing kills every mutant of the handoff and custody engines, codecs, and use cases. A method a path does not offer now answers a `grail.method-not-allowed` problem document instead of plain text, and cross-origin clients may use `DELETE`. Protocol 1.0 requests and envelopes are still accepted. The request body bound is now the contract's `handoffBytes` (4 MiB).

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
