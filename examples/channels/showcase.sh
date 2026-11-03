#!/usr/bin/env bash
# Walks the studio through every part of the protocol against a running fabric, narrating each step into #general so
# the channel viewer tells the story as it happens. Every step checks what the fabric answered and stops on the first
# surprise, so a clean run is also an end-to-end test.
#
#   examples/channels/up.sh
#   examples/channels/showcase.sh            # every participant played by this script
#   AGENTS=1 examples/channels/showcase.sh   # the review is done by whatever agent is attached as the reviewer
#
# Requires curl, jq, and openssl.
set -euo pipefail

root="$(cd "$(dirname "$0")/../.." && pwd)"
work="$root/build/channels"
grail="${GRAIL_BIN:-$root/build/grail}"
fabric="${GRAIL_FABRIC:-http://127.0.0.1:7420}"
desk_port="${DESK_PORT:-7421}"
desk="http://127.0.0.1:$desk_port"
scope="studio"
graph="studio"
run="$(date +%s)"
agent_wait_seconds="${AGENT_WAIT_SECONDS:-600}"

owner="$(cat "$work/owner.token")"
lead="$(cat "$work/lead.token")"
builder="$(cat "$work/builder.token")"
reviewer="$(cat "$work/reviewer.token")"
deployer="$(cat "$work/deployer.token")"
watcher="$(cat "$work/watcher.token")"

bold=$'\033[1m'; dim=$'\033[2m'; green=$'\033[32m'; red=$'\033[31m'; reset=$'\033[0m'
step=0

heading() {
  step=$((step + 1))
  printf '\n%s%02d  %s%s\n' "$bold" "$step" "$1" "$reset"
}

line() { printf '    %s\n' "$*"; }
held() { printf '    %s✓%s %s\n' "$green" "$reset" "$*"; }
refused() { printf '    %s✗%s %s\n' "$red" "$reset" "$*"; }

fail() {
  printf '\n%sshowcase stopped:%s %s\n' "$red" "$reset" "$*" >&2
  exit 1
}

# One contract operation; prints the answer whatever its status.
call() {
  local operation="$1" token="$2" params="$3" body="${4:-}"

  if [ -n "$body" ]; then
    "$grail" call "$operation" --fabric "$fabric" --token "$token" --params "$params" --body "$body" 2>/dev/null || true
  else
    "$grail" call "$operation" --fabric "$fabric" --token "$token" --params "$params" 2>/dev/null || true
  fi
}

# An envelope from a source to a participant or channel, as compact JSON.
envelope() {
  local id="$1" source="$2" target="$3" kind="$4" payload="$5" parents="${6:-[]}" extra="${7:-}"
  [ -n "$extra" ] || extra='{}'
  jq -cn --arg id "$id" --arg scope "$scope" --arg graph "$graph" --arg source "$source" --arg target "$target" --arg kind "$kind" \
    --argjson payload "$payload" --argjson parents "$parents" --argjson extra "$extra" \
    '{grail: "1.2", id: $id, scope: $scope, graph: $graph, source: $source, target: {participant: $target}, kind: $kind, parents: $parents, payload: $payload} + $extra'
}

send() { call sendEnvelope "$1" "{\"scope\":\"$scope\"}" "$2"; }
text() { jq -cn --arg text "$1" '{text: $text}'; }
code_of() { jq -r '.code // empty' <<< "$1"; }

expect_code() {
  local answer="$1" wanted="$2" what="$3"
  [ "$(code_of "$answer")" = "$wanted" ] || fail "$what: expected $wanted, got $(jq -c . <<< "$answer")"
}

expect_accepted() {
  local answer="$1" what="$2"
  [ -n "$(jq -r '.sequence // empty' <<< "$answer")" ] || fail "$what was refused: $(jq -c . <<< "$answer")"
}

heard_by() { jq -r '[.recipients[].participant] | join(", ")' <<< "$1"; }

# The lead narrates each step in #general, so whoever watches the channel follows along.
narrate() {
  local answer
  answer="$(send "$lead" "$(envelope "narration-$run-$step" lead general observation "$(text "$1")")")"
  expect_accepted "$answer" "narration"
}

state_of() { call readTransfer "$owner" "{\"scope\":\"$scope\",\"transfer\":\"$1\"}" | jq -r '.state // empty'; }

[ -x "$grail" ] || fail "build the executable first: pudu build src/Main.pudu -o build/grail"
command -v jq >/dev/null || fail "jq is required"
curl -sf "$fabric/v1/health" >/dev/null || fail "no fabric at $fabric; start it with examples/channels/up.sh"

printf '%sGrail studio showcase%s  %s  run %s\n' "$bold" "$reset" "$fabric" "$run"

heading "Discovery says what this fabric speaks"
discovered="$(curl -s "$fabric/.well-known/grail")"
line "protocol versions  $(jq -r '.grail | join(", ")' <<< "$discovered")"
line "profiles           $(jq -r '.fabric.profiles | join(", ")' <<< "$discovered")"
jq -e '.grail | index("1.2")' <<< "$discovered" >/dev/null || fail "the fabric does not speak 1.2"
narrate "Showcase run $run starting. Everything below is the fabric answering real requests."

heading "One graph says who may talk to whom, and in what order"
read_graph="$(call readGraph "$lead" "{\"scope\":\"$scope\",\"graph\":\"$graph\"}")"
line "participants  $(jq -r '[.participants[] | "\(.id) (\(.kind))"] | join(", ")' <<< "$read_graph")"
line "edges         $(jq -r '.edges | length' <<< "$read_graph") flow and dependency edges; reviewer → deployer is a dependency"
narrate "The studio has a lead, a builder, a reviewer, a deployer tool, a search tool, a watcher, and three channels. Deploys wait for a review."

heading "Channels fan a post out to their subscribers"
answer="$(send "$lead" "$(envelope "hello-$run" lead general observation "$(text "Morning. Today: ship the slugify helper.")")")"
expect_accepted "$answer" "a post to #general"
held "#general post heard by $(heard_by "$answer"); the reviewer hears #reviews only for tasks"
answer="$(send "$watcher" "$(envelope "shout-$run" watcher general observation "$(text "hi")")")"
expect_code "$answer" "grail.forbidden" "an observer posting"
refused "the watcher holds transfer.receive only, so it can watch but never post: $(code_of "$answer")"

heading "Authority only narrows as it is delegated"
expires=$(( ($(date +%s) + 3600) * 1000 ))
helper="$(call delegateToken "$lead" "{\"scope\":\"$scope\"}" "{\"id\":\"helper-$run\",\"audience\":\"builder\",\"graph\":\"$graph\",\"abilities\":[\"transfer.receive\"],\"expires\":$expires}" | jq -r '.token // empty')"
[ -n "$helper" ] || fail "the lead could not delegate a narrower token"
depth="$(call inspectToken "$helper" "{\"scope\":\"$scope\"}" | jq -r '.depth')"
held "the lead delegated a receive-only token for the builder, depth $depth in its chain"
answer="$(call delegateToken "$lead" "{\"scope\":\"$scope\"}" "{\"id\":\"wider-$run\",\"audience\":\"builder\",\"graph\":\"$graph\",\"abilities\":[\"graph.write\"],\"expires\":$expires}")"
expect_code "$answer" "grail.forbidden" "a wider delegation"
refused "it cannot hand out graph.write, which it does not hold: $(code_of "$answer")"
narrate "Delegation: the lead handed the builder a receive-only token and could not hand out more than it holds."

heading "A deploy asked for before its review is refused by the graph"
key="$(cat "$work/deploy.key")"
deposit="$(jq -cn --arg value "$key" --arg graph "$graph" '{value: $value, graph: $graph, audience: ["deployer"], senders: ["builder"], kinds: ["tool.call"], description: "pushes a release"}')"
answer="$(call putSecret "$owner" "{\"scope\":\"$scope\",\"secret\":\"deploy-key\"}" "$deposit")"
[ "$(jq -r '.name // empty' <<< "$answer")" = "deploy-key" ] || fail "custody did not take the key: $answer"
held "the owner gave deploy-key to custody; only the deployer may ever see its value"
deploy_payload='{"action":"release","auth":{"$secret":"deploy-key"}}'
answer="$(send "$builder" "$(envelope "deploy-early-$run" builder deployer tool.call "$deploy_payload")")"
expect_code "$answer" "grail.dependency-unmet" "an early deploy"
refused "deploy before review: $(code_of "$answer"), waiting on $(jq -r '.unmet | join(", ")' <<< "$answer")"
narrate "The builder tried to deploy before any review. The graph refused it: deploys depend on a result from the reviewer."

heading "The builder streams its build log into #builds"
answer="$(send "$builder" "$(envelope "log-$run" builder builds stream.open "$(text "build log for slugify")")")"
expect_accepted "$answer" "opening a stream"
for chunk in "collecting 14 tests" "14 passed in 0.21s" "wheel built: slugify-0.1.0"; do
  answer="$(send "$builder" "$(envelope "log-$run-$RANDOM" builder builds stream.chunk "$(text "$chunk")" "[\"log-$run\"]")")"
  expect_accepted "$answer" "a stream chunk"
done
answer="$(send "$builder" "$(envelope "log-$run-close" builder builds stream.close "$(text "build finished")" "[\"log-$run\"]")")"
expect_accepted "$answer" "closing a stream"
answer="$(send "$builder" "$(envelope "log-$run-late" builder builds stream.chunk "$(text "late line")" "[\"log-$run\"]")")"
expect_code "$answer" "grail.invalid-transition" "a chunk after close"
held "the log opened, carried three chunks, and closed in #builds, heard by the lead and the watcher"
refused "a chunk after the stream closed: $(code_of "$answer")"

heading "A review request goes to #reviews, and the first reviewer to start it takes it"
code_text=$'Please review:\n\n```python\nimport re\nimport unicodedata\n\n\ndef slugify(title: str) -> str:\n    normalized = unicodedata.normalize("NFKD", title).lower()\n    unaccented = "".join(c for c in normalized if not unicodedata.combining(c))\n    return re.sub(r"[\\W_]+", "-", unaccented).strip("-")\n```\n\nAt most three findings, or approve.'
review_task="review-$run"
answer="$(send "$builder" "$(envelope "$review_task" builder reviews task "$(text "$code_text")" "[\"log-$run\"]")")"
expect_accepted "$answer" "the review task"
held "the review task reached $(heard_by "$answer")"

if [ "${AGENTS:-}" = "1" ]; then
  line "waiting for the agent attached as the reviewer (up to ${agent_wait_seconds}s)"
  waited=0
  until [ "$(state_of "$review_task")" = "completed" ]; do
    [ "$waited" -lt "$agent_wait_seconds" ] || fail "no reviewer answered; attach one with examples/channels/attach.sh reviewer <agent>"
    sleep 5
    waited=$((waited + 5))
  done
else
  answer="$(send "$reviewer" "$(envelope "claim-$run" reviewer builder progress "$(text "taking this one")" "[\"$review_task\"]")")"
  expect_accepted "$answer" "the reviewer's claim"
  answer="$(send "$lead" "$(envelope "late-claim-$run" lead builder progress "$(text "me too")" "[\"$review_task\"]")")"
  expect_code "$answer" "grail.forbidden" "a second claim"
  refused "the lead also heard the task, but the reviewer took it first: $(code_of "$answer")"
  answer="$(send "$reviewer" "$(envelope "verdict-$run" reviewer builder result "$(text $'Approved. One note: normalize before `lower()`, which this version already does.')" "[\"$review_task\"]")")"
  expect_accepted "$answer" "the verdict"
fi

verdict="$(call pullDeliveries "$builder" "{\"scope\":\"$scope\",\"graph\":\"$graph\",\"participant\":\"builder\",\"after\":0,\"limit\":1000}" | jq -r --arg task "$review_task" '[.deliveries[].envelope | select((.kind == "result") and ((.parents // []) | index($task)))] | last | .id // empty')"
[ -n "$verdict" ] || fail "the builder never received the verdict"
held "review $(state_of "$review_task"); the verdict $verdict reached the builder"
said="$(call readTransfer "$owner" "{\"scope\":\"$scope\",\"transfer\":\"$verdict\"}" | jq -r '.envelope.payload.text // "" | .[0:400]')"
line "the reviewer said: $said"
narrate "Review done in #reviews. The first reviewer to start the task took it, and nobody else could answer it after that. The verdict: $said"

heading "The deploy now passes its gate, and only the deployer sees the key"
answer="$(send "$builder" "$(envelope "deploy-$run" builder deployer tool.call "$deploy_payload" "[\"$verdict\"]")")"
expect_accepted "$answer" "the gated deploy"
held "deploy accepted with the verdict among its parents; state $(jq -r '.state' <<< "$answer")"
stored="$(call readTransfer "$owner" "{\"scope\":\"$scope\",\"transfer\":\"deploy-$run\"}" | jq -c '.envelope.payload.auth')"
line "what the ledger stores for the key: $stored"
revealed="$(call pullDeliveries "$deployer" "{\"scope\":\"$scope\",\"graph\":\"$graph\",\"participant\":\"deployer\",\"after\":0,\"limit\":1000}" | jq -r --arg id "deploy-$run" '.deliveries[] | select(.envelope.id == $id) | .envelope.payload.auth')"
[ "$revealed" = "$key" ] || fail "the deployer's delivery did not carry the key"
held "the deployer's own delivery carries the real value (${#revealed} characters, ${revealed:0:4}…), and nothing else does"
answer="$(send "$deployer" "$(envelope "deployed-$run" deployer builder tool.result '{"text":"released slugify-0.1.0"}' "[\"deploy-$run\"]")")"
expect_accepted "$answer" "the deploy result"
answer="$(send "$deployer" "$(envelope "deploy-note-$run" deployer general observation "$(text "released slugify-0.1.0")" "[\"deployed-$run\"]")")"
expect_accepted "$answer" "the deployer's post"
careless="$(call delegateToken "$lead" "{\"scope\":\"$scope\"}" "{\"id\":\"careless-$run\",\"audience\":\"lead\",\"graph\":\"$graph\",\"abilities\":[\"transfer.send\"],\"expires\":$expires}" | jq -r '.token // empty')"
[ -n "$careless" ] || fail "the lead could not delegate a sending token"
half=$(( ${#key} / 2 ))
for disguise in "for the record, the key is $key" "encoded: $(printf '%s' "$key" | base64)" "first half: ${key:0:$half}"; do
  answer="$(send "$careless" "$(envelope "leak-$run-$RANDOM" lead general observation "$(text "$disguise")")")"
  expect_code "$answer" "grail.secret-exposed" "a leaked key"
done
after="$(call inspectToken "$careless" "{\"scope\":\"$scope\"}")"
expect_code "$after" "grail.unauthorized" "a token struck three times"
refused "a careless token pasted the key whole, in base64, and by half: each post refused, and the third strike revoked the token"
uses="$(call listSecrets "$owner" "{\"scope\":\"$scope\"}" | jq -r '.secrets[] | select(.name == "deploy-key") | .reveals')"
held "custody counts $uses reveal(s) of deploy-key"
narrate "Deployed. The builder used deploy-key by name; only the deployer's delivery held its value, and a post holding the value was refused."

heading "Retrying with the same delivery key lands once"
announce="$(envelope "release-note-$run" lead general observation "$(text "slugify 0.1.0 is out.")" "[\"deployed-$run\"]" "{\"delivery\":{\"mode\":\"effectively-once\",\"key\":\"release-$run\"}}")"
first="$(send "$lead" "$announce")"
again="$(send "$lead" "$announce")"
[ "$(jq -r '.duplicate' <<< "$again")" = "true" ] && [ "$(jq -r '.sequence' <<< "$first")" = "$(jq -r '.sequence' <<< "$again")" ] || fail "the retry was not deduplicated"
held "the same announcement sent twice is one ledger entry, #$(jq -r '.sequence' <<< "$first")"

heading "A tool that speaks JSON-RPC joins through the bridge"
answer="$(call bridgeRpc "$lead" "{\"scope\":\"$scope\",\"graph\":\"$graph\",\"participant\":\"search\"}" '{"jsonrpc":"2.0","id":7,"method":"tools/call","params":{"name":"search","arguments":{"query":"slugify unicode"}}}')"
expect_accepted "$answer" "the bridged request"
held "a JSON-RPC request became envelope $(jq -r '.id' <<< "$answer"), with a lifecycle in state $(jq -r '.state' <<< "$answer")"

heading "Every result can answer: what produced this?"
trace="$(call traceTransfer "$lead" "{\"scope\":\"$scope\",\"transfer\":\"deployed-$run\"}")"
jq -r '.entries[] | "    #\(.sequence)  \(.envelope.kind // "hidden")  \(.envelope.source // "")  \(.id)"' <<< "$trace"
jq -e --arg verdict "$verdict" '[.entries[].id] | index($verdict)' <<< "$trace" >/dev/null || fail "the trace does not reach the verdict"
held "the deploy result traces back through the deploy, the verdict, the review request, and the build log"

heading "The ledger verifies from its own digests"
ledger="$(call readLedger "$owner" "{\"scope\":\"$scope\",\"limit\":1000}")"
previous=""
count=0
while IFS=$'\t' read -r digest link; do
  if [ -z "$previous" ]; then material="grail-ledger:$digest"; else material="$previous:$digest"; fi
  [ "$(printf '%s' "$material" | openssl dgst -sha256 -r | cut -d' ' -f1)" = "$link" ] || fail "link $count does not follow from the one before it"
  previous="$link"
  count=$((count + 1))
done < <(jq -r '.entries[] | [.digest, .link] | @tsv' <<< "$ledger")
held "$count links recomputed here with openssl, each from the one before it"

heading "Erasing content keeps the record that it existed"
answer="$(call eraseTransfer "$lead" "{\"scope\":\"$scope\",\"transfer\":\"hello-$run\"}")"
[ "$(jq -r '.id // empty' <<< "$answer")" = "hello-$run" ] || fail "erasure was refused: $answer"
again="$(call readLedger "$owner" "{\"scope\":\"$scope\",\"limit\":1000}" | jq -r '.entries[-1].link')"
held "the morning post's payload is gone; its digest stays, and the chain still ends at ${again:0:16}…"
narrate "Trace, ledger, and erasure checked: the deploy traces back to the review, every link recomputes, and erasing a post kept its place in the chain."

heading "The builder's work moves to a fabric run by someone else"
desk_secret="$(openssl rand -hex 32)"
GRAIL_SECRET="$desk_secret" GRAIL_PORT="$desk_port" GRAIL_FABRIC_NAME=desk "$grail" serve > "$work/desk.log" 2>&1 &
desk_pid=$!
trap 'kill "$desk_pid" 2>/dev/null || true' EXIT
for _ in $(seq 1 50); do curl -sf "$desk/v1/health" >/dev/null && break; sleep 0.1; done
desk_owner="$(GRAIL_SECRET="$desk_secret" "$grail" token --scope support --id owner)"
"$grail" call createGraph --fabric "$desk" --token "$desk_owner" --params '{"scope":"support","graph":"desk"}' \
  --body '{"participants":[{"id":"assistant","kind":"agent"},{"id":"customer","kind":"human"}],"edges":[{"id":"a-c","from":"assistant","to":"customer","relation":"flow"}]}' >/dev/null
carried="$("$grail" handoff --from "$fabric" --from-token "$builder" --scope "$scope" --graph "$graph" --participant builder \
  --to "$desk" --to-token "$desk_owner" --to-scope support --to-graph desk --to-participant assistant \
  --id "move-$run" --transfers "deployed-$run" 2>&1 || true)"
attested="$(grep '"step":"verify"' <<< "$carried" | jq -r '.answer.attested // false')"
imported="$(grep '"step":"import"' <<< "$carried" | jq -r '.answer.entries // empty')"
[ "$attested" = "true" ] && [ -n "$imported" ] || fail "the handoff did not arrive: $carried"
held "exported from studio, attested by it, and imported into desk with $imported entries, every digest checked by desk itself"
narrate "The builder's context moved to another fabric with its whole history. The other side checked every digest without trusting this one."

heading "A revoked token stops working on its very next call"
answer="$(call revokeToken "$lead" "{\"scope\":\"$scope\",\"token\":\"helper-$run\"}")"
after="$(call inspectToken "$helper" "{\"scope\":\"$scope\"}")"
expect_code "$after" "grail.unauthorized" "a revoked token"
refused "the helper token after revocation: $(code_of "$after")"
narrate "Showcase run $run finished. Every step above was checked against the fabric's answers."

printf '\n%sAll %d steps held.%s Watch the story in the channel viewer, or read it back:\n' "$green" "$step" "$reset"
printf '    %scurl -s "%s/v1/scopes/%s/graphs/%s/channels/general" -H "Authorization: Bearer $(cat build/channels/watcher.token)" | jq%s\n' "$dim" "$fabric" "$scope" "$graph" "$reset"
