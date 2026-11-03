#!/usr/bin/env bash
# Starts a local fabric with the studio graph: a lead, a builder and a reviewer (any hosted agents), a deployer tool,
# a bridged search tool, a watcher, and the #general, #reviews, and #builds channels. Each participant gets a token
# holding only what it needs, written to build/channels/<participant>.token. A synthetic deploy key is generated for
# custody; nothing here touches a real credential.
set -euo pipefail

root="$(cd "$(dirname "$0")/../.." && pwd)"
work="${GRAIL_CHANNELS_DIR:-$root/build/channels}"
grail="${GRAIL_BIN:-$root/build/grail}"
port="${GRAIL_PORT:-7420}"
scope="studio"
graph="studio"
fabric="http://127.0.0.1:$port"

mkdir -p "$work"
umask 077

# The reference store is in memory, so a new fabric starts a new ledger; cursors kept for the old one would skip it.
rm -f "$work"/*.cursor

if [ ! -x "$grail" ]; then
  (cd "$root" && pudu build src/Main.pudu -o "$grail" >/dev/null)
fi

if [ ! -s "$work/secret" ]; then
  openssl rand -hex 32 > "$work/secret"
fi

export GRAIL_SECRET="$(cat "$work/secret")"
export GRAIL_PORT="$port"
export GRAIL_FABRIC_NAME="${GRAIL_FABRIC_NAME:-studio-local}"
export GRAIL_ALLOWED_ORIGINS="${GRAIL_ALLOWED_ORIGINS:-https://grail-protocol.chrisperezsantiago1.workers.dev,http://localhost:8091}"

"$grail" serve > "$work/fabric.log" 2>&1 &
echo $! > "$work/fabric.pid"

for _ in $(seq 1 50); do
  curl -sf "$fabric/v1/health" >/dev/null && break
  sleep 0.1
done

"$grail" token --scope "$scope" --id owner > "$work/owner.token"

"$grail" call createGraph --fabric "$fabric" --token "$(cat "$work/owner.token")" \
  --params "{\"scope\":\"$scope\",\"graph\":\"$graph\"}" --body "$(cat "$root/examples/channels/studio.json")" >/dev/null

working="graph.read,transfer.send,transfer.receive,transfer.read,ledger.read"
issue() {
  "$grail" token --scope "$scope" --id "$1-token" --audience "$1" --graph "$graph" --abilities "$2" --days 7 > "$work/$1.token"
}

issue lead "$working,token.delegate,ledger.erase"
issue builder "$working,handoff.export"
issue reviewer "$working"
issue deployer "transfer.send,transfer.receive,transfer.read"
issue watcher "transfer.receive"

if [ ! -s "$work/deploy.key" ]; then
  echo "ghp_$(openssl rand -hex 18)" > "$work/deploy.key"
fi

echo "fabric   $fabric (pid $(cat "$work/fabric.pid"), log $work/fabric.log)"
echo "graph    $scope/$graph with channels #general, #reviews, and #builds"
echo "tokens   $work/{lead,builder,reviewer,deployer,watcher}.token"
