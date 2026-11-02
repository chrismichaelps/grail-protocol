---
uid: guides.troubleshooting
description: Diagnose common local startup, routing, authority, and dependency failures.
---

# Troubleshooting

| Symptom | Check |
| --- | --- |
| Connection refused | The HTTP fabric is running on the host and port you requested. |
| Startup rejects the secret | Set at least 32 characters; an existing `.env` may override your environment. |
| `grail.unauthorized` | Token signature, scope, expiry, and revocation. The issuer and server must use the same secret. |
| `grail.forbidden` | The token's abilities, audience, graph restriction, and delegation chain. |
| `grail.no-route` | A flow edge carries the kind, the selector matches, and every selected nested graph has a reachable entry. |
| `grail.dependency-unmet` | Include the required results in `parents` or their ancestry. Waiting alone does not provide evidence. |
| `grail.unknown-parent` | Every parent was accepted into this scope's ledger. |
| `grail.invalid-transition` | The task is still open and this answer is valid for its current state. |
| `grail.revision-conflict` | Read the graph again and recompute the mutation against its current revision. |
| `grail.duplicate` | Graph and transfer ids cannot be reused in their respective containers. |
| Browser request blocked | Add your local frontend's origin to `GRAIL_ALLOWED_ORIGINS` and restart. |
| Public documentation URL returns 404 for an API path | Expected: run the API on localhost. |

A problem response contains a stable `code`, a status, a title, and sometimes details such as unmet participants or violations. Branch on the code in your integration, not on human-readable detail text.

Restarting clears the in-memory fabric. If a failure depends on previous envelopes or revocations, capture its steps before restarting so it can be reproduced.
