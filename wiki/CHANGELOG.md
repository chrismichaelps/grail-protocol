# Changelog

- 2026-11-02 · [[src/Services/Fabric]] · payload erasure enforces the token's graph restriction before mutation, including owner-audience tokens; router regressions preserve refused payloads and ledger hashes · risk HIGH

- 2026-11-02 · [[test/Engine/DeliveryTest]] · trace visibility regressions catch an inverted hidden flag for recipients-only ancestors · risk LOW

- 2026-11-02 · [[decisions/ADR-0001-specification-review]] · the draft becomes a normative specification in twelve chapters · risk HIGH
- 2026-11-02 · [[schema/grail.openapi]] · the contract: thirteen operations, the problem registry, limits, vocabularies · risk HIGH · [[decisions/ADR-0002-schema-first-contract]]
- 2026-11-02 · [[tools/Contract]] · projection of the contract into nine modules, with a check mode · risk MED
- 2026-11-02 · [[architecture/LAYERS]] · thirteen layers with a gate for upward imports, cycles, purity, and packages · risk MED · [[decisions/ADR-0003-dependency-layers]]
- 2026-11-02 · [[src/Engine/Admission]] · admission, routing, dependency gating, lifecycles, deduplication, streams · risk HIGH
- 2026-11-02 · [[src/Engine/Authority]] · per-scope HMAC tokens with attenuated delegation · risk HIGH · [[decisions/ADR-0004-capability-tokens]]
- 2026-11-02 · [[src/App/Assembly]] · mediator with logging, validation, resilience guards, and notifications · risk MED · [[decisions/ADR-0005-message-pipeline]]
- 2026-11-02 · [[src/Web/Router]] · HTTP and line bindings served from the contract · risk MED
- 2026-11-02 · [[architecture/ATTACKS]] · attack and stress campaign; reserved mutation ids, linear cycle detection, host-keyed rate limits, bounded waiting pulls, bounded scopes · risk HIGH · [[decisions/ADR-0007-long-polling-and-bounds]]
- 2026-11-02 · [[protocol/08-Bindings]] · token inspection, revocation, erasure, and waiting pulls added to the contract · risk MED
- 2026-11-02 · [[tools/Spacing]] · statement spacing enforced across the repository · risk LOW
- 2026-11-02 · [[src/Web/Peers]] · opt-in trusted proxy client addresses, connection-host fallback, and regression coverage; environment example matches the worker default · risk HIGH
- 2026-11-02 · [[test/Engine/MutationsTest]] · edge-count boundary coverage for the inclusive contract limit · risk LOW
- 2026-11-02 · [[tools/Site]] · distinguish source assembly from rendering and document the docgen compatibility patch · risk LOW
- 2026-11-02 · [[architecture/ATTACKS]] · tunnel repeat passes all non-timing checks, with 600 of 1200 requests rate limited; sequential timing probe remains inconclusive · risk MED
- 2026-11-02 · [[architecture/ATTACKS]] · 64 engine mutants attempted; five survivors killed by targeted regression reruns, including a cycle with an acyclic prefix; full suite holds 200 assertions · risk LOW
- 2026-11-02 · [[decisions/ADR-0008-composable-causal-gates]] · nested teams enforce every entry gate and retain admission-time producer attribution; expansion is bounded and atomic · risk HIGH
- 2026-11-02 · practical README and local quick-start/CLI guides replace the paper-style introduction; project funding links added · risk LOW
- 2026-11-02 · [[tools/Site]] · structured docgen landing page, searchable guides and generated API reference; pinned isolated renderer and strict build; documentation-only hosting · risk LOW
- 2026-11-02 · practical collaboration, capability, delivery, configuration, troubleshooting, contribution, graph, and envelope guides expand the local proposal documentation · risk LOW
- 2026-11-02 · reference fabric 0.1.1 promotes the reviewed graph, proxy, documentation, and local-testing changes; protocol remains draft 1.0 · risk MED
