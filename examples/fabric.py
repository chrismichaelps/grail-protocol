"""A small HTTP client for one fabric, shared by the examples, and the canonical form agents use to check digests themselves."""

import hashlib
import json
import urllib.error
import urllib.request

TIMEOUT_SECONDS = 30


def base(port):
    return f"http://127.0.0.1:{port}"


def call(port, method, path, token="", body=None):
    data = None if body is None else json.dumps(body).encode()
    headers = {"Content-Type": "application/json", "Grail-Version": "1.1"}
    if token:
        headers["Authorization"] = "Bearer " + token
    request = urllib.request.Request(base(port) + path, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as refused:
        return refused.code, json.load(refused)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(value, without):
    return "sha256:" + hashlib.sha256(canonical({key: held for key, held in value.items() if key not in without})).hexdigest()


def link(previous, entry_digest):
    material = "grail-ledger:" + entry_digest if not previous else previous + ":" + entry_digest
    return hashlib.sha256(material.encode()).hexdigest()


def envelope(scope, graph, identifier, source, target, kind, payload, parents=(), visibility="graph"):
    return {
        "grail": "1.1",
        "id": identifier,
        "scope": scope,
        "graph": graph,
        "source": source,
        "target": {"participant": target},
        "kind": kind,
        "parents": list(parents),
        "visibility": visibility,
        "payload": payload,
    }
