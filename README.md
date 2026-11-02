# Grail

A protocol proposal for agents, tools, services, and people to collaborate through graphs.

Declare who can exchange information, which results a step depends on, and what each participant may do. The fabric checks those rules when a message arrives and records accepted messages in a verifiable ledger.

- **Graph routing:** address a participant, a role, or an ability.
- **Dependency gates:** work waits for the required results in its causal history.
- **Delegated authority:** subagents receive tokens that can only narrow their parent's permissions.
- **Traceable results:** inspect declared ancestry and verify ledger hashes.
- **Composable teams:** nested graphs preserve dependency gates and producer identity.

Grail is a draft proposal with a reference fabric written in Pudu. The API runs locally; the [documentation website](https://grail-protocol.chrisperezsantiago1.workers.dev) is hosted on Cloudflare. There is no hosted public API.

## Run locally

Invited testers need access to this private repository. Install [Pudu 0.1.3](https://github.com/chrismichaelps/pudu-lang/releases/tag/v0.1.3), then:

```bash
git clone https://github.com/chrismichaelps/grail-protocol.git
cd grail-protocol
pudu install --locked
mkdir -p build
export GRAIL_SECRET="$(openssl rand -hex 32)"
pudu run src/Main.pudu token --scope demo --id root > build/owner.token
pudu run src/Main.pudu serve
```

The server listens on `127.0.0.1:7420`. In another terminal:

```bash
curl http://127.0.0.1:7420/v1/health
curl http://127.0.0.1:7420/.well-known/grail
```

The reference store is in memory. Restarting the server clears its graphs, transfers, and token revocations. Keep the same secret while issuing tokens and running the server.

## Explore

| Start here | What it covers |
| --- | --- |
| [Quick start](website/docs/guides/quick-start.md) | Start the fabric and create your first graph. |
| [Command line](website/docs/guides/command-line.md) | Tokens, operation calls, and the line binding. |
| [Protocol specification](wiki/protocol/_MOC.md) | The model, routing, causality, security, and conformance. |
| [OpenAPI contract](schema/grail.openapi.json) | Every HTTP operation, schema, error, and limit. |
| [Contributing](CONTRIBUTING.md) | Checks, dependency layers, and branch workflow. |

The running fabric serves the contract at [localhost:7420/openapi.json](http://127.0.0.1:7420/openapi.json). Use it with an OpenAPI client or your own integration.

## Development

```bash
pudu test test
pudu run tools/Layers.pudu
pudu run tools/Contract.pudu --check
```

See [Contributing](CONTRIBUTING.md) for the complete validation gate. Report vulnerabilities through the process in [Security](SECURITY.md).

[Apache License 2.0](LICENSE).
