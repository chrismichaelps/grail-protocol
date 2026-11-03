# Slack asks Codex through Grail

[Watch the recording](https://grail-protocol.chrisperezsantiago1.workers.dev/slack-codex-demo.mp4).

A Slack task asks for a corrected Python function and three assertions. The recording session reads that message through the Slack plugin and submits it to a local Grail channel. `grail run` delivers the task to a real Codex CLI worker and returns the worker's final answer as a Grail result. The session reads the Slack participant's Grail inbox and posts the answer in the original Slack thread.

The worker ran with its existing ChatGPT sign-in, a read-only sandbox, and no MCP connection to Grail. Its three assertions and nine additional checks passed. Grail deduplicated both task and result retries, refused a Slack token trying to act as Codex, completed the task, and retained the result's causal ancestry. Four ledger links and envelope digests were recomputed independently.

The 51-second edited walkthrough uses real Slack desktop captures and actual CLI output rendered in a read-only local console. Selected states are held for readability; it is not continuous real-time footage or the Codex desktop interface. No Studio website footage is used.

## Check the public receipt

No Slack account or model call is needed:

```bash
python3 tools/Recording/Verify.py examples/slack/recorded-exchange.json
python3 examples/slack/test_result.py
```

`recorded-exchange.json` retains the actual envelopes, hashes, refusal, retry responses, and recorded Slack readback checks. The message references identify test data in a private workspace; they do not grant access. Hash checks establish consistency of the published receipt, not independent authentication of Slack or the model provider.

## Repeat the integration

1. Connect a Slack plugin to your own test workspace and read a task from a dedicated channel.
2. Start a local fabric, create the graph in [`graph.json`](graph.json), and issue separate graph-bound tokens for the `slack` and `codex` participants. Use the [quick start](../../website/docs/guides/quick-start.md) and [capabilities guide](../../website/docs/guides/capabilities.md).
3. Submit the Slack message as a Grail `task` from `slack` to `requests`. Use the Slack message identity as the delivery key so a retry is deduplicated.
4. Give the `codex` participant token to the runner, then start the worker:

```bash
export GRAIL_FABRIC=http://127.0.0.1:7420
export GRAIL_TOKEN_FILE=/absolute/path/to/codex.token
build/grail run --once --exec 'env -u GRAIL_TOKEN_FILE -u GRAIL_TOKEN -u GRAIL_SECRET -u OPENAI_API_KEY -u CODEX_API_KEY codex exec --ignore-user-config --ephemeral --sandbox read-only --color never -'
```

5. Read the `slack` participant's Grail inbox with its own token, verify the result and trace, and post the result to the original Slack thread. Read the Slack thread back to confirm it arrived.

The recording session operated this gateway. A continuously running Slack listener is not included. The reference fabric keeps state in memory; restarting it clears the exchange and revocations. Model usage is subject to the account used by Codex. Cloudflare serves only documentation and recording assets.
