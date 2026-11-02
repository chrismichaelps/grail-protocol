"""Exercise the documented shell examples against an isolated localhost fabric."""

import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import socket
import subprocess
import tempfile
import time
import urllib.request

from Constants import Docs

ROOT = Path(__file__).resolve().parents[1]


def objects(text):
    decoder = json.JSONDecoder()
    found = []
    while text.strip():
        value, end = decoder.raw_decode(text.lstrip())
        found.append(value)
        text = text.lstrip()[end:]
    return found


def blocks(name):
    source = (ROOT / "website/docs/guides" / name).read_text()
    return re.findall(r"```bash\n([\s\S]*?)\n```", source)


def main():
    contract = json.loads((ROOT / "schema/grail.openapi.json").read_text())
    documented_base = contract["servers"][0]["url"]
    with tempfile.TemporaryDirectory(prefix="grail-guides-") as directory:
        work = Path(directory)
        (work / "build").mkdir()
        executable = work / "grail"
        subprocess.run(["pudu", "build", "src/Main.pudu", "-o", str(executable)], cwd=ROOT, check=True)
        with socket.socket() as reservation:
            reservation.bind(("127.0.0.1", 0))
            port = reservation.getsockname()[1]
        base = f"http://127.0.0.1:{port}"
        env = {key: value for key, value in os.environ.items() if not key.startswith("GRAIL_")}
        env.update(GRAIL_SECRET=secrets.token_hex(32), GRAIL_HOST="127.0.0.1", GRAIL_PORT=str(port), GRAIL_LOG_LEVEL="fatal")
        with open(os.devnull, "w") as log:
            server = subprocess.Popen([str(executable), "serve"], cwd=work, env=env, stdout=log, stderr=log)
        try:
            for _ in range(Docs.GUIDE_START_ATTEMPTS):
                if server.poll() is not None:
                    raise RuntimeError("The example fabric exited during startup")
                try:
                    with urllib.request.urlopen(base + "/v1/health", timeout=1) as response:
                        if json.load(response) == {"status": "alive"}:
                            break
                except OSError:
                    time.sleep(Docs.GUIDE_START_INTERVAL)
            else:
                raise RuntimeError("The example fabric did not become ready")
            token = subprocess.check_output([str(executable), "token", "--scope", "demo", "--id", "root"], cwd=work, env=env, text=True).strip()
            owner = work / "build/owner.token"
            owner.write_text(token)
            owner.chmod(0o600)

            def execute(parts):
                command = "set -euo pipefail\n" + '\nprintf "\\n"\n'.join(parts)
                result = subprocess.run(["bash", "-c", command.replace(documented_base, base)], cwd=work, env=env, capture_output=True, text=True, timeout=Docs.GUIDE_TIMEOUT_SECONDS)
                if result.returncode:
                    raise RuntimeError("A documented shell example failed")
                return objects(result.stdout)

            def read_transfer(identifier):
                request = urllib.request.Request(base + "/v1/scopes/demo/transfers/" + identifier, headers={"Authorization": "Bearer " + token})
                with urllib.request.urlopen(request, timeout=Docs.GUIDE_TIMEOUT_SECONDS) as response:
                    return json.load(response)

            answers = execute(blocks("collaboration.md"))
            assert len(answers) == 9
            assert answers[1]["code"] == "grail.dependency-unmet"
            assert answers[2]["id"] == "draft-task" and answers[4]["id"] == "draft-result"
            assert read_transfer("draft-task")["state"] == "completed"
            assert read_transfer("review-task")["state"] == "completed"
            assert [entry["id"] for entry in answers[7]["entries"]] == ["draft-task", "draft-result", "review-task"]
            entries = answers[8]["entries"]
            assert len(entries) == 5
            previous = ""
            for entry in entries:
                material = "grail-ledger:" + entry["digest"] if not previous else previous + ":" + entry["digest"]
                assert hashlib.sha256(material.encode()).hexdigest() == entry["link"]
                previous = entry["link"]
                envelope = read_transfer(entry["id"])["envelope"]
                for member in ("sequence", "digest", "accepted"):
                    envelope.pop(member, None)
                # These fixtures contain strings and integers; no floating-point canonicalization is inferred.
                canonical = json.dumps(envelope, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
                assert "sha256:" + hashlib.sha256(canonical).hexdigest() == entry["digest"]
            delegation = blocks("capabilities.md")
            inspected = execute(delegation[:-1])
            assert inspected[0]["audience"] == "worker" and inspected[0]["depth"] == 2
            deliveries = execute(blocks("deliveries.md"))
            assert deliveries[0]["deliveries"][0]["envelope"]["id"] == "draft-task"
            revoked = execute(delegation[-1:])
            assert revoked[0]["revoked"] is True
            print("Guide examples passed: collaboration, refusal, trace, digests, ledger links, delegation, delivery, revocation")
        finally:
            server.terminate()
            try:
                server.wait(timeout=Docs.GUIDE_TIMEOUT_SECONDS)
            except subprocess.TimeoutExpired:
                server.kill()
                server.wait()


if __name__ == "__main__":
    main()
