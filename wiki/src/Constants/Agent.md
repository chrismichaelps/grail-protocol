---
type: module
path: "@root/src/Constants/Agent.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Agent

> @Constants.Agent.Attachment — how a hosted agent attaches to a fabric: its variables, its tools, and what it is told

## Purpose

How a hosted agent attaches to a fabric: its variables, its tools, and what it is told.

## Interface

### Signatures

```pudu
/// The variable holding the fabric's base address.
export const FABRIC_VARIABLE: Str = "GRAIL_FABRIC"
/// The variable holding the participant's token.
export const TOKEN_VARIABLE: Str = "GRAIL_TOKEN"
/// The variable naming a file that holds the participant's token, preferred over the token itself.
export const TOKEN_FILE_VARIABLE: Str = "GRAIL_TOKEN_FILE"
/// The variable naming the graph, for a token not bound to one.
export const GRAPH_VARIABLE: Str = "GRAIL_GRAPH"
/// The variable naming the participant, for an owner token.
export const PARTICIPANT_VARIABLE: Str = "GRAIL_PARTICIPANT"
/// The variable naming a file that keeps the delivery cursor across restarts.
export const CURSOR_FILE_VARIABLE: Str = "GRAIL_CURSOR_FILE"
/// The variable giving the sequence a participant's inbox starts after when no cursor file says otherwise.
export const INBOX_AFTER_VARIABLE: Str = "GRAIL_INBOX_AFTER"
/// The variable a supervised agent finds its task id in.
export const TASK_ID_VARIABLE: Str = "GRAIL_TASK_ID"
/// The variable naming the file a supervised agent's tools list every envelope it sent or read in, one id to a line, so the runner can name them as the answer's parents.
export const TASK_JOURNAL_VARIABLE: Str = "GRAIL_TASK_JOURNAL"
/// The prefix of a task journal's file name.
export const JOURNAL_PREFIX: Str = "grail-task-"
/// What replaces the separator of a transfer id in a file name.
export const JOURNAL_SEPARATOR: Str = "-"
/// The most parents an answer names besides its task.
export const ANSWER_PARENTS_MAX: Int = 63
/// The variable a supervised agent finds its whole task envelope in.
export const TASK_VARIABLE: Str = "GRAIL_TASK"
/// The variable a supervised agent finds the task's sender in.
export const TASK_SOURCE_VARIABLE: Str = "GRAIL_TASK_SOURCE"
/// The command a runner starts for each task.
export const EXEC_OPTION: Str = "--exec"
/// Milliseconds a runner lets one task's command run.
export const TIMEOUT_OPTION: Str = "--timeout"
/// Makes a runner stop after its first page of deliveries.
export const ONCE_FLAG: Str = "--once"
/// The shell a runner starts commands with.
export const SHELL: Str = "/bin/sh"
/// The shell's flag for a command given as text.
export const SHELL_COMMAND_FLAG: Str = "-c"
/// Milliseconds a runner lets one task's command run when no timeout is given.
export const TIMEOUT_DEFAULT_MILLIS: Int = 900000
/// Milliseconds a runner waits for deliveries on each pull.
export const RUNNER_WAIT_MILLIS: Int = 25000
/// Deliveries a runner takes on each pull.
export const RUNNER_PAGE: Int = 10
/// Milliseconds a runner rests after the fabric cannot be reached.
export const RUNNER_BACKOFF_MILLIS: Int = 2000
/// The most characters of a command's output kept in an answer.
export const ANSWER_CHARS_MAX: Int = 60000
/// The most characters of a command's error stream kept in a failure.
export const FAILURE_CHARS_MAX: Int = 4000
/// The longest wait, in seconds, a tool call may ask for.
export const WAIT_SECONDS_MAX: Int = 25
/// Milliseconds between looks at a task a tool call is waiting on.
export const STATUS_POLL_MILLIS: Int = 1000
/// Deliveries or posts one tool call returns when none are asked for.
export const PAGE_DEFAULT: Int = 20
/// The most deliveries or posts one tool call returns.
export const PAGE_MAX: Int = 100
/// Random bytes in a generated transfer id.
export const ID_ENTROPY_BYTES: Int = 6
/// What separates the parts of a generated transfer id.
export const ID_SEPARATOR: Str = ":"
/// Milliseconds in a second.
export const SECOND_MILLIS: Int = 1000
/// The payload member holding plain text.
export const TEXT_MEMBER: Str = "text"
/// The kind sent when a tool call names none.
export const KIND_DEFAULT: Str = "task"
/// The name this adapter gives itself to clients.
export const SERVER_NAME: Str = "grail"
/// The title this adapter gives itself to clients.
export const SERVER_TITLE: Str = "Grail participant"
/// Shows this participant's identity, what it may do, and who it can reach.
export const TOOL_WHOAMI: Str = "grail_whoami"
/// Reads deliveries addressed to this participant.
export const TOOL_INBOX: Str = "grail_inbox"
/// Sends an envelope to a participant, a role, an ability, or a channel.
export const TOOL_SEND: Str = "grail_send"
/// Answers a task this participant received.
export const TOOL_REPLY: Str = "grail_reply"
/// Reads a channel's posts.
export const TOOL_CHANNEL: Str = "grail_channel"
/// Reads a transfer and its lifecycle.
export const TOOL_STATUS: Str = "grail_status"
/// Reads a transfer's causal ancestry.
export const TOOL_TRACE: Str = "grail_trace"
/// What a client is told about this participant's tools when it connects.
export const INSTRUCTIONS: Str = "You are a participant in a Grail fabric: a graph of agents, tools, people, and channels that exchange envelopes. Call grail_whoami first to learn who you are, who you can reach, and which channels you belong to. Work arrives as deliveries: read them with grail_inbox. Every task you accept must end with grail_reply using outcome result or error; use progress for long work and input.request when you need something from the sender. Name the envelopes you relied on in parents so the result can be traced. Post to a channel with grail_send and to set to the channel id; read what others said with grail_channel. Refer to secrets by name as \{\"$secret\": \"name\"\} and never paste a key, token, or password into a message: the fabric refuses it and strikes your token."
/// The description of `grail_whoami`.
export const WHOAMI_DESCRIPTION: Str = "Who this participant is: scope, graph, participant id, abilities, token expiry, the participants it can send to, and the channels it can post to or read."
/// The description of `grail_inbox`.
export const INBOX_DESCRIPTION: Str = "Reads new deliveries addressed to this participant, oldest first, and acknowledges the ones read before. Waits up to wait_seconds for one to arrive. Tasks must be answered with grail_reply."
/// The description of `grail_send`.
export const SEND_DESCRIPTION: Str = "Sends an envelope. Address it with exactly one of to (a participant or channel id), role, or ability. kind defaults to task; use observation, memory, or thought to share without asking for work. Put prose in text and structured content in data. List the envelope ids it builds on in parents. A task with deadline_seconds expires if nobody finishes it in time; priority 0 to 9 orders waiting work. To cancel a task you sent, send kind cancel to its recipient with the task in parents."
/// The description of `grail_reply`.
export const REPLY_DESCRIPTION: Str = "Answers a task this participant received. outcome result or error ends the task; progress and input.request keep it open. The answer goes back to whoever sent the task."
/// The description of `grail_channel`.
export const CHANNEL_DESCRIPTION: Str = "Reads posts in a channel this participant subscribes to, after a sequence number, without acknowledging anything. Waits up to wait_seconds for a new post when there is none."
/// The description of `grail_status`.
export const STATUS_DESCRIPTION: Str = "Reads one transfer: its envelope and, for tasks, where its lifecycle stands (submitted, working, input-required, completed, failed, canceled, expired, rejected). With wait_seconds, waits for an unfinished task to finish; call it again to keep waiting. The answer itself arrives in grail_inbox."
/// The description of `grail_trace`.
export const TRACE_DESCRIPTION: Str = "Reads the causal ancestry of a transfer: every envelope it was built on, with the ones this participant may not read marked hidden."
/// The input schema of `grail_whoami`.
export const WHOAMI_SCHEMA: Str = "\{\"type\":\"object\",\"properties\":\{\},\"additionalProperties\":false\}"
/// The input schema of `grail_inbox`.
export const INBOX_SCHEMA: Str = "\{\"type\":\"object\",\"properties\":\{\"wait_seconds\":\{\"type\":\"integer\",\"minimum\":0,\"maximum\":25,\"description\":\"Seconds to wait for a delivery when none is waiting.\"\},\"limit\":\{\"type\":\"integer\",\"minimum\":1,\"maximum\":100\}\},\"additionalProperties\":false\}"
/// The input schema of `grail_send`.
export const SEND_SCHEMA: Str = "\{\"type\":\"object\",\"properties\":\{\"to\":\{\"type\":\"string\",\"description\":\"A participant or channel id.\"\},\"role\":\{\"type\":\"string\"\},\"ability\":\{\"type\":\"string\"\},\"kind\":\{\"type\":\"string\",\"description\":\"task, observation, memory, thought, tool.call, or an x- extension kind. Defaults to task.\"\},\"text\":\{\"type\":\"string\"\},\"data\":\{\"type\":\"object\"\},\"parents\":\{\"type\":\"array\",\"items\":\{\"type\":\"string\"\}\},\"schema\":\{\"type\":\"string\"\},\"visibility\":\{\"type\":\"string\",\"enum\":[\"scope\",\"graph\",\"recipients\"]\},\"priority\":\{\"type\":\"integer\",\"minimum\":0,\"maximum\":9\},\"deadline_seconds\":\{\"type\":\"integer\",\"minimum\":1\}\},\"additionalProperties\":false\}"
/// The input schema of `grail_reply`.
export const REPLY_SCHEMA: Str = "\{\"type\":\"object\",\"required\":[\"task\",\"outcome\"],\"properties\":\{\"task\":\{\"type\":\"string\",\"description\":\"The id of the task being answered.\"\},\"outcome\":\{\"type\":\"string\",\"enum\":[\"result\",\"error\",\"progress\",\"input.request\"]\},\"text\":\{\"type\":\"string\"\},\"data\":\{\"type\":\"object\"\},\"parents\":\{\"type\":\"array\",\"items\":\{\"type\":\"string\"\},\"description\":\"Other envelopes the answer relied on, besides the task.\"\}\},\"additionalProperties\":false\}"
/// The input schema of `grail_channel`.
export const CHANNEL_SCHEMA: Str = "\{\"type\":\"object\",\"required\":[\"channel\"],\"properties\":\{\"channel\":\{\"type\":\"string\"\},\"after\":\{\"type\":\"integer\",\"minimum\":0,\"description\":\"The cursor a previous read returned; 0 reads from the start.\"\},\"limit\":\{\"type\":\"integer\",\"minimum\":1,\"maximum\":100\},\"wait_seconds\":\{\"type\":\"integer\",\"minimum\":0,\"maximum\":25\}\},\"additionalProperties\":false\}"
/// The input schema of `grail_status` and `grail_trace`.
export const TRANSFER_SCHEMA: Str = "\{\"type\":\"object\",\"required\":[\"transfer\"],\"properties\":\{\"transfer\":\{\"type\":\"string\"\}\},\"additionalProperties\":false\}"
/// The argument naming a wait in seconds.
export const WAIT_ARGUMENT: Str = "wait_seconds"
/// The argument naming a page size.
export const LIMIT_ARGUMENT: Str = "limit"
/// The argument naming a cursor.
export const AFTER_ARGUMENT: Str = "after"
/// The argument naming a participant or channel to address.
export const TO_ARGUMENT: Str = "to"
/// The argument naming a role to address.
export const ROLE_ARGUMENT: Str = "role"
/// The argument naming an ability to address.
export const ABILITY_ARGUMENT: Str = "ability"
/// The argument naming a kind.
export const KIND_ARGUMENT: Str = "kind"
/// The argument holding prose.
export const TEXT_ARGUMENT: Str = "text"
/// The argument holding structured content.
export const DATA_ARGUMENT: Str = "data"
/// The argument listing causal parents.
export const PARENTS_ARGUMENT: Str = "parents"
/// The argument naming a payload schema.
export const SCHEMA_ARGUMENT: Str = "schema"
/// The argument naming a visibility.
export const VISIBILITY_ARGUMENT: Str = "visibility"
/// The argument giving a priority from 0 to 9.
export const PRIORITY_ARGUMENT: Str = "priority"
/// The argument giving, in seconds from now, when an envelope stops being delivered.
export const DEADLINE_ARGUMENT: Str = "deadline_seconds"
/// The argument naming a task.
export const TASK_ARGUMENT: Str = "task"
/// The argument naming an outcome.
export const OUTCOME_ARGUMENT: Str = "outcome"
/// The argument naming a channel.
export const CHANNEL_ARGUMENT: Str = "channel"
/// The argument naming a transfer.
export const TRANSFER_ARGUMENT: Str = "transfer"
/// The outcomes a reply may have.
export const OUTCOMES: Array[Str] = ["result", "error", "progress", "input.request"]
/// The outcomes that end a task, sent with a delivery key so a retried reply lands once.
export const FINAL_OUTCOMES: Array[Str] = ["result", "error"]
/// The prefix of a reply's delivery key.
export const REPLY_KEY_PREFIX: Str = "reply:"
/// What a call without exactly one address is told.
export const ONE_ADDRESS: Str = "give exactly one of to, role, or ability"
/// What a reply with an unknown outcome is told.
export const UNKNOWN_OUTCOME: Str = "outcome must be one of result, error, progress, input.request"
/// What a missing argument is told.
export const MISSING_ARGUMENT: Str = "missing argument "
/// What an unknown tool is told.
export const UNKNOWN_TOOL: Str = "no tool named "
/// What a start without a token is told.
export const NO_TOKEN: Str = "set GRAIL_TOKEN_FILE or GRAIL_TOKEN to this participant's token"
/// What an unreadable token is told.
export const BAD_TOKEN: Str = "the token is not a Grail token"
/// What a token bound to no graph is told when no graph is named.
export const NO_GRAPH: Str = "the token is bound to no graph; set GRAIL_GRAPH"
/// What an owner token is told when no participant is named.
export const NO_PARTICIPANT: Str = "an owner token acts for nobody in particular; set GRAIL_PARTICIPANT"
/// What a runner without a command is told.
export const NO_EXEC: Str = "give the command to run for each task with --exec"
/// The member of a whoami answer naming the participant.
export const PARTICIPANT_MEMBER: Str = "participant"
/// The member of a whoami answer naming the scope.
export const SCOPE_MEMBER: Str = "scope"
/// The member of a whoami answer naming the graph.
export const GRAPH_MEMBER: Str = "graph"
/// The member of a whoami answer listing abilities.
export const ABILITIES_MEMBER: Str = "abilities"
/// The member of a whoami answer giving the token's expiry.
export const EXPIRES_MEMBER: Str = "expires"
/// The member of a whoami answer listing who this participant may send to.
export const REACHES_MEMBER: Str = "reaches"
/// The member of a whoami answer listing the channels this participant may post to.
export const POSTS_MEMBER: Str = "postsTo"
/// The member of a whoami answer listing the channels this participant reads.
export const READS_MEMBER: Str = "reads"
/// The member of a whoami answer explaining why the graph could not be read.
export const GRAPH_HIDDEN_MEMBER: Str = "graphUnreadable"
/// The member of a compact delivery naming its sender.
export const FROM_MEMBER: Str = "from"
/// The member of a compact delivery naming the channel that carried it.
export const VIA_MEMBER: Str = "via"
/// The member of a compact delivery giving its ledger sequence.
export const SEQUENCE_MEMBER: Str = "sequence"
/// The member of a compact page listing its items.
export const ITEMS_MEMBER: Str = "items"
/// The member of a compact page giving the next cursor.
export const CURSOR_MEMBER: Str = "cursor"
/// The member of a tool's failure giving the fabric's status.
export const STATUS_MEMBER: Str = "status"
/// What a runner prints when it starts.
export const RUNNER_STARTED: Str = "runner attached as "
/// What a runner prints when a task arrives.
export const RUNNER_TASK: Str = "task "
/// What a runner prints for a delivery that is not work.
export const RUNNER_HEARD: Str = "heard "
/// What a runner prints when another participant already has a task.
export const RUNNER_TAKEN: Str = "left to another subscriber "
/// What a runner prints when a task is answered.
export const RUNNER_ANSWERED: Str = "answered "
/// What a runner prints when the agent answered a task itself.
export const RUNNER_SELF_ANSWERED: Str = "agent answered "
/// What a runner prints when a task's command fails.
export const RUNNER_FAILED: Str = "failed "
/// What a runner prints when the fabric cannot be reached.
export const RUNNER_UNREACHABLE: Str = "fabric unreachable: "
/// What a runner says in the progress it sends when work starts.
export const RUNNER_PROGRESS: Str = "started by the runner"
/// The title of the problem a runner sends when a command fails.
export const RUNNER_PROBLEM_TITLE: Str = "The agent did not finish"
/// The problem type a runner sends when a command fails.
export const RUNNER_PROBLEM_TYPE: Str = "urn:grail:problem:grail.agent-failed"
/// What a runner says when a command ran out of time.
export const RUNNER_TIMED_OUT: Str = "the agent ran out of time"
/// The member of a problem document giving its type.
export const PROBLEM_TYPE_MEMBER: Str = "type"
/// The member of a problem document giving its title.
export const PROBLEM_TITLE_MEMBER: Str = "title"
/// The member of a problem document giving its detail.
export const PROBLEM_DETAIL_MEMBER: Str = "detail"
/// The member of a problem document giving the exit status.
export const PROBLEM_STATUS_MEMBER: Str = "exitStatus"
/// The first line of the prompt a runner gives a supervised agent; the participant id follows.
export const PROMPT_IDENTITY: Str = "You are the Grail participant "
/// The prompt's line introducing the task; the sender follows.
export const PROMPT_TASK: Str = "A task arrived from "
/// The prompt's line introducing the task id.
export const PROMPT_TASK_ID: Str = "Task id: "
/// The prompt's line introducing the request.
export const PROMPT_REQUEST: Str = "Request:"
/// The prompt's closing guidance.
export const PROMPT_GUIDANCE: Str = "Do the work. When you are done, either call grail_reply with this task id and outcome result, or simply print your final answer: whatever you print becomes the result. If you cannot do it, call grail_reply with outcome error and say why. You may delegate part of the work with grail_send, wait for it with grail_status, and collect the answer with grail_inbox, which shows only what arrived after this task."
/// What joins the prompt's lines.
export const PROMPT_JOIN: Str = "\n\n"
/// What joins a label and its value in a runner's log line.
export const LOG_JOIN: Str = " "
/// What joins a runner's log fields.
export const LOG_ARROW: Str = " -> "
```

### Linkage

- **Consumed by:** [[src/Agent/Mcp]] · [[src/Agent/Runner]] · [[src/Agent/Session]] · [[src/Agent/Tools]] · [[src/Agent/Wire]] · [[src/Cli/Commands]]

## Referenced by

[[src/Agent/Mcp]] · [[src/Agent/Runner]] · [[src/Agent/Session]] · [[src/Agent/Tools]] · [[src/Agent/Wire]] · [[src/Cli/Commands]] · [[src/Constants/_MOC]]
