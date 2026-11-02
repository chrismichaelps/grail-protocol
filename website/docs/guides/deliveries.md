---
uid: guides.deliveries
description: Receive envelopes, acknowledge a cursor, and choose delivery guarantees.
---

# Receive work

Participants pull their own inbox. A participant does not need a public callback URL.

```bash
curl -sS 'http://127.0.0.1:7420/v1/scopes/demo/graphs/workflow/participants/worker/deliveries?after=0&wait=30000' \
  -H "Authorization: Bearer $(cat build/worker.token)"
```

The response contains `deliveries` and a `cursor`. Each delivery has a ledger sequence and its envelope. Set `after` to the last cursor you have processed when making the next request. Passing that cursor acknowledges everything through it.

## Choose a guarantee

| Mode | Behavior |
| --- | --- |
| `at-least-once` | Work can return again until acknowledged. This is the default. |
| `at-most-once` | Once served, that delivery is not served again to the participant. |
| `effectively-once` | A repeated send with the same delivery key and identical envelope returns its original acceptance within the deduplication window. |

Effectively-once sends require `delivery.key`. A key reused for different content is refused with `grail.key-reused`. The advertised deduplication window is currently 24 hours. This guarantees admission deduplication, not exactly-once side effects in your external service.

## Wait without busy polling

`wait` accepts up to 30,000 milliseconds. The fabric answers when work appears or the wait expires. Under pressure it may answer an empty page immediately to preserve serving capacity; add backoff before retrying. Respect `429` responses and retry guidance.

Persist your cursor with your application's processing state. Make repeated work safe by using envelope ids or your own application idempotency key.

See the [transfer specification](../protocol/04-Transfer.md) for lifecycles, deadlines, and delivery semantics.
