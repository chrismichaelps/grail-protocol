---
type: specification
chapter: 9
tags: [protocol, specification]
---

# 9. Errors

Every refusal is one problem document in the shape of RFC 9457. Its `type` is `urn:grail:problem:` followed by the code without its `grail.` prefix.

```json
{
  "type": "urn:grail:problem:no-route",
  "title": "No route",
  "status": 422,
  "code": "grail.no-route",
  "detail": "No flow edge carries kind task from planner to a participant with role writer.",
  "instance": "tr_01J9…"
}
```

`code` is the stable member clients branch on. `detail` is for people and MAY change between versions. Problems MAY carry extra members listed per code below.

| Code | Status | Meaning | Extra members |
| --- | --- | --- | --- |
| `grail.invalid` | 400 | The request does not match the contract. | `violations`: `[{path, message}]` |
| `grail.unauthorized` | 401 | No token, or a token that does not verify. | |
| `grail.forbidden` | 403 | The token verifies but lacks the ability. | `ability` |
| `grail.not-found` | 404 | The object does not exist in the token's scope. | |
| `grail.method-not-allowed` | 405 | The path exists, but the contract offers no operation for this method on it. | |
| `grail.duplicate` | 409 | An envelope or object with this id already exists. | |
| `grail.revision-conflict` | 409 | `expectedRevision` is stale. | `revision` |
| `grail.key-reused` | 409 | An `effectively-once` key was reused with a different envelope. | |
| `grail.too-large` | 413 | A size limit was exceeded. | `limit` |
| `grail.no-route` | 422 | The target resolves to no participant reachable on a flow edge. | |
| `grail.dependency-unmet` | 422 | Dependency gating refused a task. | `unmet`: participant ids |
| `grail.cycle` | 422 | A mutation would create a dependency or containment cycle. | `cycle`: ids in order |
| `grail.invalid-transition` | 422 | The envelope would move a lifecycle illegally. | `state` |
| `grail.unknown-parent` | 422 | A parent is not in the ledger. | `parents` |
| `grail.limit-exceeded` | 422 | A count limit was exceeded. | `limit` |
| `grail.secret-exposed` | 422 | An envelope, bridged message, or handoff holds the value of a secret in custody ([[protocol/14-Custody#14.3 Admission]]). | |
| `grail.integrity` | 422 | A handoff's digests, links, or ancestry do not hold ([[protocol/13-Portability#13.2 Integrity]]). | |
| `grail.clock-skew` | 422 | The sender's clock is too far ahead. | |
| `grail.expired` | 422 | The deadline passed before acceptance. | |
| `grail.unsupported-version` | 426 | The requested protocol version is not supported. | `supported` |
| `grail.backpressure` | 429 | The recipient's backlog is full. | `retryAfter` (seconds) |
| `grail.unavailable` | 503 | The fabric cannot serve the request now. | `retryAfter` (seconds) |

Codes are append-only. A code is never repurposed; a code no longer produced is marked deprecated in the contract and kept.

## Referenced by

[[protocol/_MOC]] · [[domain/Problem]] · [[schema/grail.openapi]]
