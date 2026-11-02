---
uid: guides.capabilities
description: Give a participant a narrow token, inspect its authority, and revoke it.
---

# Delegate authority

An agent needs a token, not the fabric's signing secret. After the [collaboration walkthrough](collaboration.md), give the worker only send and receive permissions in `workflow`:

```bash
EXPIRES=$(python3 -c 'import time; print(int(time.time()*1000)+3600000)')
curl -fsS -X POST http://127.0.0.1:7420/v1/scopes/demo/tokens \
  -H "Authorization: Bearer $(cat build/owner.token)" \
  -H 'Content-Type: application/json' \
  -d "{\"id\":\"worker-1\",\"audience\":\"worker\",\"graph\":\"workflow\",\"abilities\":[\"transfer.send\",\"transfer.receive\"],\"expires\":$EXPIRES}" \
  | python3 -c 'import json,sys; print(json.load(sys.stdin)["token"])' > build/worker.token
```

Expiry is an absolute Unix timestamp in milliseconds. This example uses one hour. A child must start no earlier and expire no later than its parent.

## Inspect the token

```bash
curl -sS http://127.0.0.1:7420/v1/scopes/demo/tokens/self \
  -H "Authorization: Bearer $(cat build/worker.token)"
```

The response identifies the audience, graph, abilities, validity window, and chain depth. The worker sends envelopes with `source: "worker"` and pulls only its own deliveries. This token cannot mutate the graph or delegate further authority.

## Delegate again

A parent needs `token.delegate` before it can issue a child. Each child must narrow its parent's abilities, graph restriction, and validity window. A graph role or advertised ability describes a participant; it does not grant authority to the caller.

## Revoke when finished

Run this after trying the delivery examples; it deliberately disables the worker token.

```bash
curl -sS -X POST http://127.0.0.1:7420/v1/scopes/demo/tokens/worker-1/revocation \
  -H "Authorization: Bearer $(cat build/owner.token)"
```

The token and every descendant are refused afterwards. The owner may revoke any token; other callers need delegation authority and must be its issuer. Revocation state is in memory in this reference fabric and is lost on restart.

The [security specification](../protocol/07-Security.md) defines the complete chain rules.
