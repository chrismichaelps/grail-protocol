---
uid: guides.command-line
description: Use Grail's local HTTP server, token issuer, operation client, and standard-input binding.
---

# Command line

Run `pudu run src/Main.pudu help` for the command list. The examples assume the quick-start fabric is running and the owner token is in `build/owner.token`.

| Command | Purpose |
| --- | --- |
| `serve` | Start the local HTTP fabric. This is the default command. |
| `token --scope S --id I` | Issue an owner token using the configured secret. |
| `call OPERATION` | Call an operation by its OpenAPI `operationId`. |
| `lines` | Read operation requests from standard input and write JSON replies. |
| `contract` | Print the OpenAPI document. |
| `version` | Print the reference fabric version. |

## Call an operation

```bash
pudu run src/Main.pudu call readGraph \
  --fabric http://127.0.0.1:7420 \
  --token "$(cat build/owner.token)" \
  --params '{"scope":"demo","graph":"hello"}'
```

Use `--body` for operations with a JSON request body. Operation ids, paths, and parameters come from `schema/grail.openapi.json`.

## Use the line binding

`lines` runs a separate in-memory fabric; it does not connect to the HTTP process or share its state. Each input line selects an operation and may carry `token`, `params`, and `body`:

```bash
printf '%s\n' '{"operation":"discover"}' | pudu run src/Main.pudu lines
```

An answer carries the HTTP-equivalent `status` and `body`. Keep one process open when sending several related operations.

## Issue scoped tokens

The local issuer also accepts `--audience`, `--abilities`, `--graph`, and `--days`. Use the `delegateToken` operation when an agent delegates its existing authority: that operation checks the entire narrowing chain. The local issuer holds the fabric secret and is an administrative command.
