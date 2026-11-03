---
uid: guides.quick-start
description: Clone Grail, start a local fabric, and create a graph with your own secret.
---

# Run Grail locally

Grail is [public on GitHub](https://github.com/chrismichaelps/grail-protocol). Install [Pudu 0.1.3](https://github.com/chrismichaelps/pudu-lang/releases/tag/v0.1.3) and have `git`, `openssl`, and `curl` available in your terminal. This walkthrough uses an in-memory fabric on your own machine. The public website serves documentation, not an API.

## Start the fabric

```bash
git clone https://github.com/chrismichaelps/grail-protocol.git
cd grail-protocol
pudu install --locked
mkdir -p build
umask 077
export GRAIL_SECRET="$(openssl rand -hex 32)"
pudu run src/Main.pudu token --scope demo --id root > build/owner.token
pudu run src/Main.pudu serve
```

Leave this terminal running. The secret signs the scope owner's token; changing it makes that token invalid. `build/` is ignored by Git, so the token stays out of commits.

## Check it from another terminal

From the repository root:

```bash
curl http://127.0.0.1:7420/v1/health
```

Expect `{"status":"alive"}`. Discovery is at `/.well-known/grail`, and the full OpenAPI contract is at `/openapi.json`.

## Create a graph

This graph connects a coordinator to a worker:

```bash
curl -i -X PUT http://127.0.0.1:7420/v1/scopes/demo/graphs/hello \
  -H "Authorization: Bearer $(cat build/owner.token)" \
  -H 'Content-Type: application/json' \
  -d '{"participants":[{"id":"coordinator","kind":"agent"},{"id":"worker","kind":"agent"}],"edges":[{"id":"work","from":"coordinator","to":"worker","relation":"flow"}]}'
```

Expect `201 Created`. Read it back with the same token and `GET /v1/scopes/demo/graphs/hello`. Repeating creation returns `grail.duplicate`; choose another graph id or restart the fabric to begin again.

## Make it your own

Use a different scope when issuing the owner token, and use that scope in every API path and envelope. Replace participants with your agents, tools, or services. A participant's `kind` describes it; the graph and capability token determine what it can do.

Stop the server with `Ctrl+C`. Its in-memory state is discarded. Token signing uses the secret, while revocations and delivery state live in memory; restart behavior matters when testing those operations.

See [Command line](command-line.md) for the available commands and operation calls.
