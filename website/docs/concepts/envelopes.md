---
uid: concepts.envelopes
description: Follow envelopes through causal parents, task lifecycles, traces, and the ledger.
---

# Envelopes and history

Every transfer uses the same envelope. Its required fields are `grail`, `id`, `scope`, `graph`, `source`, `target`, and `kind`. The optional `payload` belongs to your application.

```json
{"grail":"1.0","id":"task-1","scope":"demo","graph":"workflow","source":"coordinator","target":{"participant":"worker"},"kind":"task","payload":{"brief":"Draft a release note"}}
```

## Declare causality

`parents` names earlier envelopes in the same scope. A `result` names the task it answers. A later task can name that result to satisfy a dependency. Clocks help order a trace for readers; they do not establish causality.

Parent references describe declared lineage. They do not prove that a participant actually used every declared input or reveal its internal reasoning.

## Follow the lifecycle

A task begins as `submitted`. Progress can move it to `working`, an input request can pause it, and a result completes it. Errors, cancellation, deadlines, and terminal-state rules are specified by the [transfer lifecycle](../protocol/04-Transfer.md). An illegal transition is refused rather than appended.

## Inspect provenance

Use `traceTransfer` to retrieve ancestors in ledger order. Visibility rules can hide content while retaining its position and digest. Use `readLedger` to retrieve sequence numbers, envelope digests, and hash links.

A link is recomputed as `sha256("grail-ledger:" + digest)` for the first entry, then `sha256(previousLink + ":" + digest)`. Digests are written as `sha256:<hex>` and cover the envelope's canonical form before fabric stamps are added. The link formula uses that full digest string, including its prefix. Follow ledger page cursors when verifying more than one page.

This detects changes relative to a ledger head you already trust. The reference fabric does not publish externally witnessed checkpoints or prove that a hostile fabric has not replaced an entire history.

## Erase a payload

A caller with `ledger.erase` can remove an envelope's payload. The record is marked erased while its original digest and link remain. Its payload can no longer be recomputed, but the retained hash chain can still be checked. The operation is not deletion of the envelope's identifier or causal edges.

See the [causality specification](../protocol/05-Causality.md) and [generated API reference](../rest/grail.openapi.json).
