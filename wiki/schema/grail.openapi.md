---
type: contract
path: "@root/schema/grail.openapi.json"
tags: [contract, openapi]
---

# Contract — schema/grail.openapi.json

The OpenAPI 3.1 document of the HTTP binding, and through it of every binding. It is the only file that defines the wire ([[decisions/ADR-0002-schema-first-contract]]).

## What it holds

- **Operations:** `discover`, `describeContract`, `checkHealth`, `createGraph`, `readGraph`, `mutateGraph`, `sendEnvelope`, `readTransfer`, `traceTransfer`, `pullDeliveries`, `readLedger`, `delegateToken`, `bridgeRpc`, each with `x-grail-ability`.
- **Schemas:** the envelope and every object it holds, graphs, mutations, tokens, delegations, answers, discovery, and the problem document.
- **Extensions:** `x-grail-version`, `x-grail-limits`, `x-grail-problems` (the registry of codes, statuses, and titles), `x-grail-final-states`, `x-grail-opening-kinds`, `x-grail-headers`, and media types.

## Changing it

1. Edit the file.
2. `pudu run tools/Contract.pudu`.
3. Fix what stops compiling; bind a handler for a new operation.
4. Record the change in [[CHANGELOG]] and, for anything a client sees, in [[protocol/12-Evolution|the versioning rules]].

## Referenced by

[[00-INDEX]] · [[protocol/_MOC]] · [[architecture/CONTRACT]] · [[tools/Contract]]
