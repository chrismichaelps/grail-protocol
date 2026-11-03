#!/usr/bin/env bash
# Attaches a hosted agent as one participant of the studio graph and keeps it working: the runner pulls the
# participant's deliveries and starts the agent for each task, with the Grail tools loaded for that process only.
#
#   examples/channels/attach.sh <participant> <agent> [runner options]
#
# <agent> is the name of an agent command line this script knows how to give the tools to, or any other command
# that reads its prompt on standard input. The tools receive only the Grail variables.
set -euo pipefail

root="$(cd "$(dirname "$0")/../.." && pwd)"
work="$root/build/channels"
grail="${GRAIL_BIN:-$root/build/grail}"
participant="${1:?name a participant: builder, reviewer, or lead}"
agent="${2:?name an agent command}"
shift 2

export GRAIL_FABRIC="${GRAIL_FABRIC:-http://127.0.0.1:7420}"
export GRAIL_TOKEN_FILE="$work/$participant.token"
export GRAIL_CURSOR_FILE="$work/$participant.cursor"

passed='["GRAIL_FABRIC","GRAIL_TOKEN_FILE","GRAIL_INBOX_AFTER","GRAIL_TASK_ID","GRAIL_TASK_JOURNAL"]'
config="$work/$participant.tools.json"
cat > "$config" <<JSON
{"mcpServers": {"grail": {"command": "$grail", "args": ["agent"]}}}
JSON

case "$agent" in
  codex)
    command="codex exec --skip-git-repo-check --sandbox read-only --color never \
      -c 'mcp_servers.grail.command=\"$grail\"' -c 'mcp_servers.grail.args=[\"agent\"]' \
      -c 'mcp_servers.grail.env_vars=$passed' -"
    ;;
  claude)
    command="claude -p --strict-mcp-config --mcp-config '$config' --allowedTools 'mcp__grail__*'"
    ;;
  *)
    command="$agent"
    ;;
esac

exec "$grail" run --exec "$command" "$@"
