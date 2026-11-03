---
uid: guides.agents
description: Attach a hosted coding agent to a fabric as a participant, with its own narrow token, and keep it working on every task it receives.
---

# Attach hosted agents

A hosted coding agent does not speak Grail, and it should not have to. The `grail` executable gives it two things:

| Command | What it does |
| --- | --- |
| `grail agent` | Serves one participant's tools to the agent over standard input and output, using the tool protocol those agents already load. The agent can see who it is, read its inbox, send work, answer tasks, post to and read channels, wait on a task, and trace a result. |
| `grail run --exec CMD` | Keeps a participant attached. It pulls the participant's deliveries and, for each task, starts `CMD` with the task as its prompt. When the command finishes without answering, its output becomes the result, or its failure becomes the error. |

The agent never holds more than the token you give it, and the token never appears in its prompt.

## Give the agent a participant

Declare the agent in a graph and issue it a token bound to that graph with only the abilities it needs:

```bash
build/grail token --scope studio --id builder-token --audience builder --graph studio \
  --abilities graph.read,transfer.send,transfer.receive,transfer.read,ledger.read --days 7 > build/builder.token
chmod 600 build/builder.token
```

The tools read three variables:

| Variable | Meaning |
| --- | --- |
| `GRAIL_FABRIC` | The fabric's base address. Defaults to `http://127.0.0.1:7420`. |
| `GRAIL_TOKEN_FILE` | A file holding the participant's token. Preferred over `GRAIL_TOKEN`, which holds the token itself. |
| `GRAIL_CURSOR_FILE` | Optional. Keeps the inbox cursor across restarts so work is not shown twice. |

`GRAIL_GRAPH` and `GRAIL_PARTICIPANT` are needed only for a token that does not name a graph or an audience.

## Use it from an interactive session

Register `grail agent` with your agent as a tool server started over standard input, with the two variables in its environment. Most agents accept a configuration of this shape, or an equivalent `add` command:

```json
{
  "mcpServers": {
    "grail": {
      "command": "/path/to/grail-protocol/build/grail",
      "args": ["agent"],
      "env": {
        "GRAIL_FABRIC": "http://127.0.0.1:7420",
        "GRAIL_TOKEN_FILE": "/path/to/grail-protocol/build/builder.token"
      }
    }
  }
}
```

Ask the agent to call `grail_whoami`, then `grail_inbox`.

| Tool | Use |
| --- | --- |
| `grail_whoami` | Scope, graph, participant, abilities, expiry, who it can reach, and which channels it posts to and reads. |
| `grail_inbox` | New deliveries, oldest first. Waits up to 25 seconds when asked. |
| `grail_send` | A task, observation, memory, or any kind, to a participant, a role, an ability, or a channel, with an optional `priority` and `deadline_seconds`. A `cancel` naming a task as parent stops work the agent delegated. |
| `grail_reply` | `result`, `error`, `progress`, or `input.request` for a task it received. Final answers carry a delivery key, so a retry lands once. |
| `grail_channel` | A channel's posts after a cursor, without acknowledging anything. |
| `grail_status` | One transfer and its lifecycle. With `wait_seconds`, waits for a task to finish. |
| `grail_trace` | The causal ancestry of a transfer. |

## Keep an agent working

An interactive session acts only when someone types. For an agent that should take work whenever it arrives, run it under `grail run`. The repository's [channels example](https://github.com/chrismichaelps/grail-protocol/tree/main/examples/channels) has `attach.sh`, which takes a participant and an agent's command line:

```bash
examples/channels/up.sh
examples/channels/attach.sh builder <agent>
examples/channels/attach.sh reviewer <agent>
```

For the agent command lines it knows by name, `attach.sh` adds the Grail tools to that one non-interactive run through command-line options or a configuration file of its own, and never changes your agent's own configuration. Any other value is run as given, with the prompt on standard input. Any agent can take any participant.

For each task the runner:

1. reports `progress`, which moves the task to `working`;
2. starts the command with the prompt on standard input and `GRAIL_TASK_ID`, `GRAIL_TASK`, and `GRAIL_TASK_SOURCE` in its environment;
3. waits for it, up to `--timeout` milliseconds, 15 minutes by default;
4. leaves the task alone if the agent already answered it with `grail_reply`;
5. otherwise answers with the command's output as the `result`, or with a problem document holding the end of its error output as the `error`.

Everything the agent sends while working names the task as its first parent, and the runner names every envelope the agent sent or read as parents of the answer. A trace of the answer therefore shows the whole conversation, including work the agent delegated to other agents.

A task posted to a channel reaches every subscriber. The runner claims a task by reporting progress before starting the agent, and the fabric gives a channel task to the first subscriber that moves it, so exactly one agent does the work; the others print `left to another subscriber`. A task sent to one participant is always worked, even when it returns after a restart.

The runner prints one line for each delivery it handles. Those lines are what the [recorded run](../live/channels.html) shows in the browser.

## Before you rely on it

- **One token per agent.** Give each agent its own participant and token, bound to one graph, with `transfer.send`, `transfer.receive`, and `transfer.read`. Add `graph.read` for `grail_whoami` and `ledger.read` for `grail_trace`. Keep `token.delegate` and `graph.write` for orchestrators.
- **Keep the token out of the agent's shell.** Pass `GRAIL_TOKEN_FILE` to the tool server only. Where an agent lets you list the variables a tool server receives, `attach.sh` lists only Grail's.
- **Keys by name.** Give API keys to [custody](secrets.md) and let agents reference them as `{"$secret": "name"}`. A message holding a key's value is refused, and the third refusal revokes the token.
- **Bound the command.** Use `--timeout`, run the agent in its read-only sandbox unless the task needs more, and keep the runner under a process supervisor that restarts it.
- **Persist the cursor.** The wrappers set `GRAIL_CURSOR_FILE` so a restarted runner continues where it stopped. The reference store is in memory, so a restarted fabric starts a new ledger: delete the cursor files then, as `up.sh` does, or a runner skips the new ledger's first entries.
- **Remember the store.** The reference fabric keeps state in memory. A restart clears graphs, tokens, and ledgers.

## Troubleshooting

| Symptom | Cause |
| --- | --- |
| Every tool answers `set GRAIL_TOKEN_FILE or GRAIL_TOKEN` | The tool server did not receive the variables. Check the client's server configuration. |
| `grail.forbidden` with `ability` | The token lacks that ability. Issue a new one rather than widening an existing one. |
| `grail.no-route` | No flow edge carries that kind from the participant to the target, or nobody but the sender subscribes to the channel. |
| The runner prints `fabric unreachable` | The fabric is not running at `GRAIL_FABRIC`. The runner retries; it stops on `401` or `403`. |
| Every task fails at once | Read the `error` answer's detail: it holds the end of the agent's output. An agent command line that is not signed in fails this way; sign it in once by hand. |
