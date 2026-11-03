"""Exercise the credential boundary of the example executor using local HTTP services."""

import contextlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import threading
import unittest
from unittest.mock import patch

EXAMPLE = Path(__file__).resolve().parents[1] / "examples/secrets"
sys.path.insert(0, str(EXAMPLE))
SPEC = importlib.util.spec_from_file_location("grail_executor", EXAMPLE / "agents.py")
executor = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(executor)
CANARY = "synthetic-executor-credential-92741"


class ExecutorTest(unittest.TestCase):
    def setUp(self):
        self.collected = []
        self.served = []
        self.results = []
        self.redirect = None
        owner = self

        class Collector(BaseHTTPRequestHandler):
            def do_GET(self):
                owner.collected.append(self.headers.get("Authorization"))
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"releases":[]}')

            def log_message(self, *_):
                pass

        class Service(BaseHTTPRequestHandler):
            def do_GET(self):
                owner.served.append(self.headers.get("Authorization"))
                self.send_response(owner.redirect or 200)
                if owner.redirect:
                    self.send_header("Location", f"http://127.0.0.1:{owner.collector.server_port}/collect")
                self.end_headers()
                if not owner.redirect:
                    self.wfile.write(b'{"releases":["example"]}')

            def log_message(self, *_):
                pass

        self.collector = ThreadingHTTPServer(("127.0.0.1", 0), Collector)
        self.service = ThreadingHTTPServer(("127.0.0.1", 0), Service)
        for server in (self.collector, self.service):
            self.addCleanup(server.server_close)
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            self.addCleanup(thread.join, 2)
            self.addCleanup(server.shutdown)

    def run_executor(self, path="/releases"):
        def call(_port, method, _path, _token, body=None):
            if method == "GET":
                return 200, {"cursor": 1, "deliveries": [{"envelope": {"id": "probe", "payload": {"path": path, "auth": CANARY}}}]}
            self.results.append(body)
            return 202, {}

        output = io.StringIO()
        with patch.object(executor, "SERVICE_HOST", "127.0.0.1"), patch.object(executor, "SERVICE_PORT", self.service.server_port), patch.object(executor.fabric, "call", side_effect=call), contextlib.redirect_stdout(output):
            executor.executor("synthetic-fabric-token", "probe")
        self.assertNotIn(CANARY, output.getvalue())
        self.assertNotIn(CANARY, json.dumps(self.results))

    def test_direct_request_reaches_only_the_pinned_service(self):
        self.run_executor()
        self.assertEqual(self.served, ["Bearer " + CANARY])
        self.assertEqual(self.collected, [])
        self.assertEqual(len(self.results), 1)

    def test_redirects_never_forward_credentials_or_contact_the_target(self):
        for status in (301, 302, 303, 307, 308):
            with self.subTest(status=status):
                self.redirect = status
                self.run_executor()
                self.assertEqual(self.collected, [])
                self.assertEqual(self.results, [])
        self.assertEqual(len(self.served), 5)

    def test_environment_proxy_cannot_receive_the_credential(self):
        proxy = f"http://127.0.0.1:{self.collector.server_port}"
        with patch.dict(os.environ, {"http_proxy": proxy, "HTTP_PROXY": proxy, "no_proxy": "", "NO_PROXY": ""}):
            self.run_executor()
        self.assertEqual(self.served, ["Bearer " + CANARY])
        self.assertEqual(self.collected, [])

    def test_unpinned_initial_paths_are_refused(self):
        for path in ("https://elsewhere.test/key", "//elsewhere.test/key", "/@elsewhere", "/\\elsewhere", "/path?redirect=x", "/path#fragment", "relative"):
            with self.subTest(path=path):
                self.run_executor(path)
        self.assertEqual(self.served, [])
        self.assertEqual(self.collected, [])
        self.assertEqual(self.results, [])


if __name__ == "__main__":
    unittest.main()
