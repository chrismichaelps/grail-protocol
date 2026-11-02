---
uid: guides.configuration
description: Configure a local fabric's secret, listener, logging, workers, and browser origins.
---

# Configure the local fabric

The fabric reads settings at startup. A `.env` file, when present, overrides process environment values. See the repository's `.env.example`; do not leave its secret empty when using it.

| Variable | Default | Purpose |
| --- | --- | --- |
| `GRAIL_SECRET` | Required | Signing secret, at least 32 characters. |
| `GRAIL_HOST` | `127.0.0.1` | Local listening address. |
| `GRAIL_PORT` | `7420` | HTTP port. |
| `GRAIL_LOG_LEVEL` | `information` | Minimum log level. |
| `GRAIL_WORKERS` | `64` | HTTP serving workers. |
| `GRAIL_CONNECTIONS` | `0` | Connections before shutdown; zero is unbounded. |
| `GRAIL_ALLOWED_ORIGINS` | Empty | Comma-separated browser origins permitted by CORS. |
| `GRAIL_CLIENT_IP_HEADER` | Empty | Advanced trusted-proxy identity setting; leave empty for local testing. |

Log levels are `verbose`, `debug`, `information`, `warning`, `error`, and `fatal`.

## Keep local experiments separate

Use a different scope id when issuing an owner token for another experiment. Scope ids must match the token, API path, and envelope. Keep `GRAIL_HOST=127.0.0.1` for the local proposal workflow.

## Understand restart behavior

The store is in memory. Graphs, transfers, cursors, delegation issuance records, and revocations are discarded when the process stops. Reusing the signing secret still permits previously issued tokens to verify; in-memory revocation history does not survive. Use fresh secrets for independent disposable experiments.

The website deployment contains static documentation only. It does not store or run your local fabric.
