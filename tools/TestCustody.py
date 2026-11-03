"""Check custody security boundaries over HTTP against a fresh native localhost fabric."""

import json
import os
from pathlib import Path
import secrets
import socket
import subprocess
import tempfile
import time
import urllib.error
import urllib.request

from Constants import Docs

ROOT = Path(__file__).resolve().parents[1]


def main():
    if not __debug__:
        raise RuntimeError("Run custody checks without Python optimization so assertions remain enabled")
    with tempfile.TemporaryDirectory(prefix="grail-custody-") as directory:
        work = Path(directory)
        binary = work / "grail"
        subprocess.run(["pudu", "build", "src/Main.pudu", "-o", str(binary)], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
        with socket.socket() as reservation:
            reservation.bind(("127.0.0.1", 0))
            port = reservation.getsockname()[1]
        env = {key: value for key, value in os.environ.items() if not key.startswith("GRAIL_")}
        env.update(GRAIL_SECRET=secrets.token_hex(32), GRAIL_HOST="127.0.0.1", GRAIL_PORT=str(port), GRAIL_LOG_LEVEL="information")
        root = subprocess.check_output([str(binary), "token", "--scope", "demo", "--id", "root"], cwd=work, env=env, text=True).strip()
        base = f"http://127.0.0.1:{port}"
        prefix = "/v1/scopes/demo"
        key, replacement = secrets.token_hex(24), secrets.token_hex(24)

        def call(method, path, token=root, body=None):
            request = urllib.request.Request(base + path, data=None if body is None else json.dumps(body).encode(), method=method, headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
            try:
                response = urllib.request.urlopen(request, timeout=Docs.GUIDE_TIMEOUT_SECONDS)
            except urllib.error.HTTPError as refused:
                response = refused
            with response:
                return response.code, json.load(response)

        def delegate(identifier, audience, abilities, parent=root):
            status, grant = call("POST", prefix + "/tokens", parent, {"id": identifier, "audience": audience, "graph": "g", "abilities": abilities, "expires": int(time.time() * 1000) + (120000 if parent == root else 60000)})
            assert status == 201
            return grant["token"]

        def deposit(value, sender="planner", description="release access", name="key"):
            return call("PUT", prefix + "/secrets/" + name, body={"value": value, "graph": "g", "audience": ["executor"], "senders": [sender], "kinds": ["tool.call"], "description": description})

        def send(identifier, sender="planner"):
            return call("POST", prefix + "/transfers", body={"grail": "1.1", "id": identifier, "scope": "demo", "graph": "g", "source": sender, "target": {"participant": "executor"}, "kind": "tool.call", "delivery": {"mode": "at-most-once"}, "payload": {"auth": {"$secret": "key"}}})

        def exposed(answer):
            assert answer[1]["code"] == "grail.secret-exposed"
            assert key not in json.dumps(answer[1]) and replacement not in json.dumps(answer[1])

        log_path = work / "server.log"
        with log_path.open("w") as log:
            server = subprocess.Popen([str(binary), "serve"], cwd=work, env=env, stdout=log, stderr=log)
        try:
            for _ in range(Docs.GUIDE_START_ATTEMPTS):
                if server.poll() is not None:
                    raise RuntimeError("The custody fabric exited during startup")
                try:
                    if call("GET", "/v1/health")[0] == 200:
                        break
                except OSError:
                    time.sleep(Docs.GUIDE_START_INTERVAL)
            else:
                raise RuntimeError("The custody fabric did not become ready")
            graph = {"participants": [{"id": "planner", "kind": "agent"}, {"id": "executor", "kind": "tool"}, {"id": "helper", "kind": "tool"}], "edges": [{"id": "flow", "from": "planner", "to": "executor", "relation": "flow"}, {"id": "help", "from": "helper", "to": "executor", "relation": "flow"}]}
            assert call("PUT", prefix + "/graphs/g", body=graph)[0] == 201
            assert deposit(key)[0] == 201
            planner = delegate("planner", "planner", ["token.delegate", "transfer.receive"])
            worker = delegate("worker", "executor", ["transfer.receive"])
            escalation = call("POST", prefix + "/tokens", planner, {"id": "owner-child", "audience": "owner", "graph": "g", "abilities": ["transfer.receive"], "expires": int(time.time() * 1000) + 60000})
            assert escalation[0] == 403 and escalation[1]["code"] == "grail.forbidden"
            child = delegate("executor-child", "executor", ["transfer.receive"], planner)
            assert send("call")[0] == 202
            deliveries = prefix + "/graphs/g/participants/executor/deliveries"
            refused = call("GET", deliveries, child)
            assert refused[0] == 403 and key not in json.dumps(refused[1])
            allowed = call("GET", deliveries, worker)
            assert allowed[0] == 200 and allowed[1]["deliveries"][0]["envelope"]["payload"]["auth"] == key
            assert call("GET", prefix + "/secrets")[1]["secrets"][0]["reveals"] == 1
            before = call("GET", prefix + "/ledger")[1]
            writer = delegate("writer", "executor", ["graph.write"])
            exposed(call("POST", prefix + "/graphs/g/mutations", writer, {"expectedRevision": 1, "operations": [{"op": "add-participant", "participant": {"id": "leak", "kind": "agent", "roles": [key]}}]}))
            exposed(call("PUT", prefix + "/graphs/" + key, body=graph))
            exposed(deposit(secrets.token_hex(24), description=key, name="other"))
            exposed(deposit(replacement, description=replacement, name="own"))
            exposed(call("POST", prefix + "/graphs/g/participants/planner/handoffs", body={"id": key, "transfers": ["call"]}))
            assert call("GET", prefix + "/ledger")[1] == before
            assert call("GET", prefix + "/graphs/g")[1]["revision"] == 1
            assert key not in json.dumps(call("GET", prefix + "/secrets")[1])
            assert key not in json.dumps(call("GET", prefix + "/transfers/call")[1])
            queued = send("queued")
            assert queued[0] == 202 and deposit(replacement, sender="helper")[0] == 201
            stale = call("GET", deliveries, worker)
            assert stale[0] == 403 and replacement not in json.dumps(stale[1])
            assert send("fresh", "helper")[0] == 202
            fresh = call("GET", deliveries + "?after=" + str(queued[1]["sequence"]), worker)
            assert fresh[0] == 200 and fresh[1]["deliveries"][0]["envelope"]["payload"]["auth"] == replacement
        finally:
            server.terminate()
            try:
                server.wait(timeout=Docs.GUIDE_TIMEOUT_SECONDS)
            except subprocess.TimeoutExpired:
                server.kill()
                server.wait()
        logged = log_path.read_text()
        assert key not in logged and replacement not in logged and root not in logged
        print("Native localhost custody checks passed: delegation, delivery, rotation, metadata, handoff, ledger, and redacted logs")


if __name__ == "__main__":
    main()
