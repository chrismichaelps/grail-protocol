#!/usr/bin/env bash
# Walks the studio through every part of the protocol against a running fabric, narrating each step into #general so
# the channel viewer tells the story as it happens. Every step checks what the fabric answered and stops on the first
# surprise, so a clean run is also an end-to-end test.
#
#   examples/channels/up.sh
#   examples/channels/showcase.sh            # every participant played by this script
#   AGENTS=1 examples/channels/showcase.sh   # the review is done by whatever agent is attached as the reviewer
#   RECORD=run.json examples/channels/showcase.sh   # also write every request, answer, post, and ledger entry
#
# A recording holds what the channel viewer replays. Tokens are never written, and the deploy key is replaced in
# every form the showcase uses it before anything reaches the file.
#
# Requires curl, jq, and openssl.
set -euo pipefail

root="$(cd "$(dirname "$0")/../.." && pwd)"
work="${GRAIL_CHANNELS_DIR:-$root/build/channels}"
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
record="${RECORD:-}"
scratch=""
calls=""
desk_pid=""
desk_owner=""
cleanup() {
  [ -z "$desk_pid" ] || kill "$desk_pid" 2>/dev/null || true
  [ -z "$scratch" ] || rm -rf "$scratch"
}
trap cleanup EXIT
if [ -n "$record" ]; then
  umask 077
  scratch="$(mktemp -d "$work/showcase.XXXXXX")"
  calls="$scratch/calls.jsonl"
fi
key="$(cat "$work/deploy.key")"
half=$(( ${#key} / 2 ))
encoded="$(printf '%s' "$key" | base64)"
helper=""
careless=""

[ -z "$record" ] || : > "$calls"

# Text with the deploy key replaced in every form this script ever writes it, whole first, so nothing of it is left.
redact() {
  local text="$1" held_token
  for held_token in "$owner" "$lead" "$builder" "$reviewer" "$deployer" "$watcher" "$helper" "$careless" "$desk_owner"; do
    [ -z "$held_token" ] || text="${text//"$held_token"/‹token›}"
  done
  text="${text//"$key"/‹deploy-key›}"
  text="${text//"$encoded"/‹deploy-key in base64›}"
  printf '%s' "${text//"${key:0:$half}"/‹half of deploy-key›}"
}

# Appends one compact JSON value to the recording, redacted.
remember() {
  [ -n "$record" ] || return 0
  printf '%s\n' "$(redact "$1")" >> "$calls"
}

# Who a token speaks for, by name, so a recording never holds the token itself.
who() {
  case "$1" in
    "$owner") echo "owner" ;;
    "$lead") echo "lead" ;;
    "$builder") echo "builder" ;;
    "$reviewer") echo "reviewer" ;;
    "$deployer") echo "deployer" ;;
    "$watcher") echo "watcher" ;;
    "$helper") echo "helper token delegated by the lead" ;;
    "$careless") echo "careless token delegated by the lead" ;;
    "") echo "anyone" ;;
    *) echo "another token" ;;
  esac
}

heading() {
  step=$((step + 1))
  printf '\n%s%02d  %s%s\n' "$bold" "$step" "$1" "$reset"
  remember "$(jq -cn --argjson step "$step" --arg title "$1" '{type: "step", step: $step, title: $title}')"
}

noted() { remember "$(jq -cn --argjson step "$step" --arg mark "$1" --arg text "$2" '{type: "note", step: $step, mark: $mark, text: $text}')"; }
line() { printf '    %s\n' "$*"; noted line "$*"; }
held() { printf '    %s✓%s %s\n' "$green" "$reset" "$*"; noted held "$*"; }
refused() { printf '    %s✗%s %s\n' "$red" "$reset" "$*"; noted refused "$*"; }

# Records one request and its answer; delegated tokens in an answer are replaced before the line is written.
exchanged() {
  local operation="$1" as="$2" params="$3" body="$4" answer="$5"
  [ -n "$record" ] || return 0
  jq . <<< "$answer" >/dev/null 2>&1 || answer="$(jq -cn --arg text "$answer" '{text: $text}')"
  remember "$(jq -cn --argjson step "$step" --arg operation "$operation" --arg as "$as" --argjson params "${params:-null}" --argjson body "${body:-null}" --argjson answer "$answer" \
    '{type: "call", step: $step, operation: $operation, as: $as, params: $params, body: $body, answer: ($answer | walk(if type == "object" and has("token") then .token = "‹token›" else . end))}')"
}

fail() {
  printf '\n%sshowcase stopped:%s %s\n' "$red" "$reset" "$*" >&2
  exit 1
}

# One contract operation; prints the answer whatever its status, and records it unless QUIET is set.
call() {
  local operation="$1" token="$2" params="$3" body="${4:-}" answer

  if [ -n "$body" ]; then
    answer="$("$grail" call "$operation" --fabric "$fabric" --token "$token" --params "$params" --body "$body" 2>/dev/null || true)"
  else
    answer="$("$grail" call "$operation" --fabric "$fabric" --token "$token" --params "$params" 2>/dev/null || true)"
  fi

  [ -n "${QUIET:-}" ] || exchanged "$operation" "$(who "$token")" "$params" "$body" "$answer"
  printf '%s\n' "$answer"
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
  answer="$(QUIET=1 send "$lead" "$(envelope "narration-$run-$step" lead general observation "$(text "$1")")")"
  expect_accepted "$answer" "narration"
}

state_of() { QUIET=1 call readTransfer "$owner" "{\"scope\":\"$scope\",\"transfer\":\"$1\"}" | jq -r '.state // empty'; }

[ -x "$grail" ] || fail "build the executable first: pudu build src/Main.pudu -o build/grail"
command -v jq >/dev/null || fail "jq is required"
curl -sf "$fabric/v1/health" >/dev/null || fail "no fabric at $fabric; start it with examples/channels/up.sh"

printf '%sGrail studio showcase%s  %s  run %s\n' "$bold" "$reset" "$fabric" "$run"

heading "Discovery says what this fabric speaks"
discovered="$(curl -s "$fabric/.well-known/grail")"
exchanged discover anyone '{}' '' "$discovered"
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
held "the deployer's own delivery carries the real value (${#revealed} characters), and nothing else does"
answer="$(send "$deployer" "$(envelope "deployed-$run" deployer builder tool.result '{"text":"released slugify-0.1.0"}' "[\"deploy-$run\"]")")"
expect_accepted "$answer" "the deploy result"
answer="$(send "$deployer" "$(envelope "deploy-note-$run" deployer general observation "$(text "released slugify-0.1.0")" "[\"deployed-$run\"]")")"
expect_accepted "$answer" "the deployer's post"
careless="$(call delegateToken "$lead" "{\"scope\":\"$scope\"}" "{\"id\":\"careless-$run\",\"audience\":\"lead\",\"graph\":\"$graph\",\"abilities\":[\"transfer.send\"],\"expires\":$expires}" | jq -r '.token // empty')"
[ -n "$careless" ] || fail "the lead could not delegate a sending token"
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

for _ in $(seq 1 50); do curl -sf "$desk/v1/health" >/dev/null && break; sleep 0.1; done
desk_owner="$(GRAIL_SECRET="$desk_secret" "$grail" token --scope support --id owner)"
"$grail" call createGraph --fabric "$desk" --token "$desk_owner" --params '{"scope":"support","graph":"desk"}' \
  --body '{"participants":[{"id":"assistant","kind":"agent"},{"id":"customer","kind":"human"}],"edges":[{"id":"a-c","from":"assistant","to":"customer","relation":"flow"}]}' >/dev/null
carried="$("$grail" handoff --from "$fabric" --from-token "$builder" --scope "$scope" --graph "$graph" --participant builder \
  --to "$desk" --to-token "$desk_owner" --to-scope support --to-graph desk --to-participant assistant \
  --id "move-$run" --transfers "deployed-$run" 2>&1 || true)"
origin="$(jq -cn --arg id "move-$run" '{scope: "studio", graph: "studio", participant: "builder", handoff: $id}')"
destination="$(jq -cn --arg id "move-$run" '{scope: "support", graph: "desk", participant: "assistant", handoff: $id}')"
asked="$(jq -cn --arg id "move-$run" --arg anchor "deployed-$run" '{id: $id, transfers: [$anchor]}')"
bundle="$(grep '"step":"export"' <<< "$carried" | jq -c '.answer')"
exchanged exportHandoff builder "$origin" "$asked" "$bundle"
exchanged verifyHandoff anyone "$origin" "$bundle" "$(grep '"step":"verify"' <<< "$carried" | jq -c '.answer')"
exchanged importHandoff "desk owner" "$destination" "$bundle" "$(grep '"step":"import"' <<< "$carried" | jq -c '.answer')"
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

if [ -n "$record" ]; then
  posts="$scratch/posts.jsonl"
  : > "$posts"
  for channel in general reviews builds; do
    QUIET=1 call readChannel "$owner" "{\"scope\":\"$scope\",\"graph\":\"$graph\",\"channel\":\"$channel\",\"limit\":1000}" | jq -c --arg channel "$channel" '.deliveries[] | {channel: $channel, entry: .}' >> "$posts"
  done
  entries="$scratch/ledger.jsonl"
  : > "$entries"
  while IFS=$'\t' read -r sequence id digest link; do
    QUIET=1 call readTransfer "$owner" "{\"scope\":\"$scope\",\"transfer\":\"$id\"}" | jq -c --argjson sequence "$sequence" --arg id "$id" --arg digest "$digest" --arg link "$link" \
      '{sequence: $sequence, id: $id, digest: $digest, link: $link, envelope: .envelope}' >> "$entries"
  done < <(QUIET=1 call readLedger "$owner" "{\"scope\":\"$scope\",\"limit\":1000}" | jq -r '.entries[] | [.sequence, .id, .digest, .link] | @tsv')
  assembled="$(jq -n --slurpfile calls "$calls" --slurpfile posts "$posts" --slurpfile ledger "$entries" --arg recorded "$(date '+%-d %B %Y')" --arg agents "${AGENTS:-}" '
    {
      workspace: "studio",
      channels: ["general", "reviews", "builds"],
      recorded: $recorded,
      note: ("Recorded on a local fabric with examples/channels/showcase.sh" + (if $agents == "1" then ". A hosted coding agent attached as the reviewer did the review itself; the script played the other participants through their own tokens." else ", every participant played through its own token." end) + " The recorded calls and channel posts came from this run; the ledger contains the accepted envelopes. Tokens were never recorded, and the deploy key is shown only as a placeholder."),
      steps: [$calls[] | select(.type == "step") | {step, title}] | map(. as $s | . + {notes: [$calls[] | select(.type == "note" and .step == $s.step) | {mark, text}], calls: [$calls[] | select(.type == "call" and .step == $s.step) | del(.type, .step)]}),
      posts: ($posts | sort_by(.entry.sequence)),
      ledger: ($ledger | sort_by(.sequence))
    }')"
  assembled="$(redact "$assembled")"
  for form in "$key" "$encoded" "${key:0:$half}"; do
    [[ "$assembled" != *"$form"* ]] || fail "the recording would hold the deploy key; nothing was written"
  done
  for held_token in "$owner" "$lead" "$builder" "$reviewer" "$deployer" "$watcher" "$helper" "$careless"; do
    [ -z "$held_token" ] || [[ "$assembled" != *"${held_token%%.*}"* ]] || fail "the recording would hold a token; nothing was written"
  done
  temporary="$(mktemp "${record}.XXXXXX")"
  printf '%s\n' "$assembled" > "$temporary"
  mv "$temporary" "$record"
  held "recorded $(jq '.steps | length' <<< "$assembled") steps, $(jq '[.steps[].calls[]] | length' <<< "$assembled") requests, $(jq '.posts | length' <<< "$assembled") posts, and $(jq '.ledger | length' <<< "$assembled") ledger entries to $record"
fi

printf '\n%sAll %d steps held.%s Watch the story in the channel viewer, or read it back:\n' "$green" "$step" "$reset"
printf '    %scurl -s "%s/v1/scopes/%s/graphs/%s/channels/general" -H "Authorization: Bearer $(cat build/channels/watcher.token)" | jq%s\n' "$dim" "$fabric" "$scope" "$graph" "$reset"
