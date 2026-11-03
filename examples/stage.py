"""What the examples share besides the client: starting a fabric, issuing narrow tokens, and printing a run people can follow."""

import os
import secrets
import subprocess
import time

import fabric

BOLD, DIM, GREEN, RED, RESET = "\033[1m", "\033[2m", "\033[32m", "\033[31m", "\033[0m"
START_ATTEMPTS = 100
START_INTERVAL = 0.1
SCENE_PAUSE = 0.6
TOKEN_LIFETIME_MILLIS = 3600000
NARROWER_MILLIS = 600000


def heading(text):
    print(f"\n{BOLD}{GREEN}▍{RESET} {BOLD}{text}{RESET}", flush=True)
    time.sleep(SCENE_PAUSE)


def note(text):
    print(f"{DIM}{text}{RESET}", flush=True)


def refused(text):
    print(f"{RED}{text}{RESET}", flush=True)


def finished():
    print(f"\n{BOLD}{GREEN}done{RESET}", flush=True)


def start(executable, name, port, scope, work):
    """A fabric with a secret of its own on a local port, and its scope owner's token."""
    env = {key: value for key, value in os.environ.items() if not key.startswith("GRAIL_")}
    env.update(GRAIL_SECRET=secrets.token_hex(32), GRAIL_PORT=str(port), GRAIL_FABRIC_NAME=name, GRAIL_LOG_LEVEL="fatal")
    server = subprocess.Popen([str(executable), "serve"], cwd=work, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(START_ATTEMPTS):
        try:
            if fabric.call(port, "GET", "/v1/health")[0] == 200:
                break
        except OSError:
            time.sleep(START_INTERVAL)
    else:
        raise RuntimeError(f"the {name} fabric did not start")
    owner = subprocess.check_output([str(executable), "token", "--scope", scope, "--id", "owner"], cwd=work, env=env, text=True).strip()
    return server, owner


def delegate(port, scope, issuer, identifier, audience, graph, abilities, depth=1):
    """A token for one participant of one graph, issued by `issuer`; the answer as the fabric gave it. Each level down the chain lives shorter, so a child never outlives its parent."""
    body = {"id": identifier, "audience": audience, "graph": graph, "abilities": abilities, "expires": int(time.time() * 1000) + TOKEN_LIFETIME_MILLIS - depth * NARROWER_MILLIS}
    return fabric.call(port, "POST", f"/v1/scopes/{scope}/tokens", issuer, body)
