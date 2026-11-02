# Changelog

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
