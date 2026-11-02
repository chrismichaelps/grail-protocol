---
type: adr
status: ACCEPTED
date: 2026-11-02
decision_risk: HIGH
tags: [adr, protocol, causality]
---

# ADR-0008 — Dependency gates compose across graph boundaries

## Context

A graph participant represents an entire team. The original implementation expanded its delivery address but checked dependencies only in the outer graph. An entry dependency could therefore be bypassed through containment. A valid inner result also failed to satisfy an outer dependency on the team, because its source address belonged to the inner graph. Both defects contradict the intended composition model and were reproduced by failing tests before implementation changed.

## Decision

Resolve a task into bounded paths from each selected participant through graph entries to terminal recipients. Check dependencies at every address on those paths before committing anything. Retain the paths with the task lifecycle and use the same task-parent correlation rule for reply authorization and causal attribution.

A verified successful reply credits its direct source and the enclosing participants on the responding recipient's original paths. It does not credit other aliases that happen to reach that recipient now. Later entry-role changes do not revoke accepted evidence or rewrite its origin. Unrelated internal results and errors cannot supply enclosing-team evidence. Producer identity includes both graph and participant.

Every selected branch must resolve. An empty branch yields `grail.no-route`; exceeding the contract's `routingPaths` bound yields `grail.limit-exceeded`. Recipients are deduplicated for delivery, while distinct paths remain available for attribution. The bound is declared in the OpenAPI contract and projected for discovery and runtime enforcement.

## Consequences

A team can be composed as an ordinary graph node without weakening the gates inside it. The task lifecycle still accepts its first authorized completion; this change introduces no implicit all-results barrier. The routing witness is internal evidence retained by a trusted fabric. The ledger does not separately sign it, prove that an agent actually used all declared inputs, or prove that a participant labelled `human` is operated by a person.

These are corrections to the draft's graph semantics. Existing request and response shapes remain unchanged; discovery gains an additive resource limit. An independent fabric must reproduce the same behavior before interoperability is claimed.

## Validation

[[test/Engine/CompositionTest]] covers entry and intermediate gates, three-level composition, unrelated internal results, errors, changed entries, new aliases, graph-qualified identities, empty branches, shared recipients, and the path-count boundary.

## Referenced by

[[decisions/_MOC]] · [[protocol/06-Graphs]]
