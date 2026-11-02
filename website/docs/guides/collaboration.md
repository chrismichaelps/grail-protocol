---
uid: guides.collaboration
description: Send work, return a result, and enforce a review dependency on a local fabric.
---

# Run a collaboration

Start the fabric with the [quick start](quick-start.md). This example uses the owner token to simulate three participants. Real integrations should use [separate delegated tokens](capabilities.md).

## Create the team

From the repository root, define a helper and create a graph:

```bash
BASE=http://127.0.0.1:7420
TOKEN=$(cat build/owner.token)
request() { curl -sS -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' "$@"; }
request -X PUT "$BASE/v1/scopes/demo/graphs/workflow" -d '{
  "participants":[
    {"id":"coordinator","kind":"agent"},
    {"id":"worker","kind":"agent","roles":["author"]},
    {"id":"reviewer","kind":"human"}
  ],
  "edges":[
    {"id":"cw","from":"coordinator","to":"worker","relation":"flow"},
    {"id":"cr","from":"coordinator","to":"reviewer","relation":"flow"},
    {"id":"wr","from":"worker","to":"reviewer","relation":"dependency"}
  ]
}'
```

The coordinator can reach both participants. The reviewer depends on a result from the worker. Transfer ids are unique across the scope; restart the local fabric before repeating the entire walkthrough.

## Try the gate

```bash
request -X POST "$BASE/v1/scopes/demo/transfers" -d '{"grail":"1.0","id":"early-review","scope":"demo","graph":"workflow","source":"coordinator","target":{"participant":"reviewer"},"kind":"task"}'
```

Expect `grail.dependency-unmet`. The refused envelope does not enter the ledger.

## Send and receive work

```bash
request -X POST "$BASE/v1/scopes/demo/transfers" -d '{"grail":"1.0","id":"draft-task","scope":"demo","graph":"workflow","source":"coordinator","target":{"role":"author"},"kind":"task","payload":{"brief":"Draft a short release note"}}'
request "$BASE/v1/scopes/demo/graphs/workflow/participants/worker/deliveries?after=0&wait=30000"
```

The task is accepted with `202`. The worker's inbox contains it. The role selector reaches only matching participants connected by a flow edge that carries this kind.

## Return a result

```bash
request -X POST "$BASE/v1/scopes/demo/transfers" -d '{"grail":"1.0","id":"draft-result","scope":"demo","graph":"workflow","source":"worker","target":{"participant":"coordinator"},"kind":"result","parents":["draft-task"],"payload":{"text":"The release improves graph composition."}}'
```

The task becomes `completed`. Its recipient may answer the coordinator without a separate return edge.

## Request the review

```bash
request -X POST "$BASE/v1/scopes/demo/transfers" -d '{"grail":"1.0","id":"review-task","scope":"demo","graph":"workflow","source":"coordinator","target":{"participant":"reviewer"},"kind":"task","parents":["draft-result"]}'
request -X POST "$BASE/v1/scopes/demo/transfers" -d '{"grail":"1.0","id":"review-result","scope":"demo","graph":"workflow","source":"reviewer","target":{"participant":"coordinator"},"kind":"result","parents":["review-task"],"payload":{"decision":"approved"}}'
```

The first request now succeeds because its ancestry includes the worker's result. The review adapter decides whether to emit a successful result or an error; Grail does not interpret the payload's decision or prove that a person operated the credential.

## Inspect the history

```bash
request "$BASE/v1/scopes/demo/transfers/review-result/trace"
request "$BASE/v1/scopes/demo/ledger?limit=100"
```

The trace contains the declared chain from the draft task to the review. The ledger also includes graph changes. Next, connect your own processes using [delegated capabilities](capabilities.md) and [delivery cursors](deliveries.md).
