"""A planning agent uses a repository key it never sees.

The owner gives the key to custody. The planner learns that it exists and what it is for, and asks the executor to
call the repository with it by name. Only the executor's delivery holds the value; the ledger, the trace, and every
other participant see a reference. A result that echoes the key is refused, a reference aimed at another agent is
refused, rotation takes effect on the next call, and deletion stops a call already waiting.
"""

import base64
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import secrets
import subprocess
import sys
import tempfile
import threading

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import fabric
import stage
from settings import CALL_ID, DESCRIPTION, FABRIC, GRAPH, KEY_BYTES, PENDING_CALL, RESULT_ID, SECOND_CALL, SECRET, SERVICE_PORT

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PORT, SCOPE, NAME = FABRIC["port"], FABRIC["scope"], FABRIC["graph"]
TIMEOUT_SECONDS = 30
RELEASES = ["0.1.0", "0.1.1", "0.1.2", "0.2.0"]


class Repository(BaseHTTPRequestHandler):
    """A stand-in for an external service: it answers only requests that present the key it currently accepts."""

    accepted = ""

    def do_GET(self):
        presented = self.headers.get("Authorization", "")
        allowed = bool(Repository.accepted) and secrets.compare_digest(presented, "Bearer " + Repository.accepted)
        body = json.dumps({"releases": RELEASES} if allowed else {"error": "bad credentials"}).encode()
        self.send_response(200 if allowed else 401)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *_):
        return


def deposit(owner, value):
    body = {"value": value, "graph": NAME, "audience": ["executor"], "senders": ["planner"], "kinds": ["tool.call"], "description": DESCRIPTION}
    return fabric.call(PORT, "PUT", f"/v1/scopes/{SCOPE}/secrets/{SECRET}", owner, body)


def ask(planner, identifier, target="executor"):
    payload = {"path": "/repos/acme/releases", "auth": {"$secret": SECRET}}
    return fabric.call(PORT, "POST", f"/v1/scopes/{SCOPE}/transfers", planner, fabric.envelope(SCOPE, NAME, identifier, "planner", target, "tool.call", payload))


def executor(token, wanted):
    return subprocess.Popen([sys.executable, str(HERE / "agents.py"), token, wanted], cwd=HERE)


def main():
    service = ThreadingHTTPServer(("127.0.0.1", SERVICE_PORT), Repository)
    threading.Thread(target=service.serve_forever, daemon=True).start()
    with tempfile.TemporaryDirectory(prefix="grail-secrets-") as directory:
        work = Path(directory)
        built = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else work / "grail"
        if len(sys.argv) == 1:
            subprocess.run(["pudu", "build", "src/Main.pudu", "-o", str(built)], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
        server, owner = stage.start(built, FABRIC["name"], PORT, SCOPE, work)
        try:
            fabric.call(PORT, "PUT", f"/v1/scopes/{SCOPE}/graphs/{NAME}", owner, GRAPH)
            planner = stage.delegate(PORT, SCOPE, owner, "planner", "planner", NAME, ["transfer.send", "transfer.read", "graph.read"])[1]["token"]
            runner = stage.delegate(PORT, SCOPE, owner, "executor", "executor", NAME, ["transfer.send", "transfer.receive"])[1]["token"]

            stage.heading("The owner gives the key to custody, once")
            key = secrets.token_urlsafe(KEY_BYTES)
            Repository.accepted = key
            status, held = deposit(owner, key)
            stage.note(f"PUT secrets/{SECRET}  HTTP {status}  version {held['version']}, audience {held['audience']}, senders {held['senders']}")
            stage.note(f"the answer holds the value: {key in json.dumps(held)}")
            status, _ = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/secrets/{SECRET}", owner)
            stage.note(f"GET secrets/{SECRET}  HTTP {status}  there is no way to read it back")

            stage.heading("The planner learns what exists, not what it is")
            _, listed = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/secrets", planner)
            for found in listed["secrets"]:
                stage.note(f"{found['name']:<12} v{found['version']}  for {', '.join(found['audience'])}  \"{found['description']}\"")
            stage.note(f"the listing holds the value: {key in json.dumps(listed)}")

            stage.heading("It asks the executor to use the key by name")
            worker = executor(runner, CALL_ID)
            status, receipt = ask(planner, CALL_ID)
            stage.note(f"tool.call {CALL_ID}  HTTP {status}  payload auth = {{\"$secret\": \"{SECRET}\"}}")
            worker.wait(TIMEOUT_SECONDS)
            _, stored = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/transfers/{CALL_ID}", owner)
            _, ledger = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/ledger", owner)
            _, trace = fabric.call(PORT, "GET", f"/v1/scopes/{SCOPE}/transfers/{RESULT_ID}-{CALL_ID}/trace", owner)
            stage.note(f"stored envelope auth = {json.dumps(stored['envelope']['payload']['auth'])}")
            stage.note(f"value in the envelope, the ledger, or the trace: {any(key in json.dumps(found) for found in (stored, ledger, trace))}")

            stage.heading("Every way out is closed")
            echoed = fabric.envelope(SCOPE, NAME, "echo", "executor", "planner", "tool.result", {"debug": "Authorization: Bearer " + key}, [CALL_ID])
            status, refused = fabric.call(PORT, "POST", f"/v1/scopes/{SCOPE}/transfers", runner, echoed)
            stage.refused(f"executor echoes the key          HTTP {status}  {refused['code']}")
            disguised = fabric.envelope(SCOPE, NAME, "echo-b64", "executor", "planner", "tool.result", {"debug": base64.b64encode(key.encode()).decode()}, [CALL_ID])
            status, refused = fabric.call(PORT, "POST", f"/v1/scopes/{SCOPE}/transfers", runner, disguised)
            stage.refused(f"executor sends it in base64      HTTP {status}  {refused['code']}")
            status, refused = ask(planner, "to-reviewer", "reviewer")
            stage.refused(f"planner aims it at another agent HTTP {status}  {refused['code']}")

            stage.heading("Rotation and deletion take effect at once")
            key = secrets.token_urlsafe(KEY_BYTES)
            Repository.accepted = key
            status, held = deposit(owner, key)
            stage.note(f"rotated to version {held['version']}; the service now accepts only the new key")
            worker = executor(runner, SECOND_CALL)
            ask(planner, SECOND_CALL)
            worker.wait(TIMEOUT_SECONDS)
            ask(planner, PENDING_CALL)
            status, _ = fabric.call(PORT, "DELETE", f"/v1/scopes/{SCOPE}/secrets/{SECRET}", owner)
            stage.note(f"DELETE secrets/{SECRET}  HTTP {status}  while {PENDING_CALL} waits for the executor")
            executor(runner, PENDING_CALL).wait(TIMEOUT_SECONDS)
            stage.finished()
        finally:
            server.terminate()
            server.wait(TIMEOUT_SECONDS)
            service.shutdown()


if __name__ == "__main__":
    main()
