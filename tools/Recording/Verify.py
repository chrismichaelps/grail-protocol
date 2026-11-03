"""Recompute the recorded Slack/Codex exchange hashes without Slack credentials."""

import hashlib
import json
from pathlib import Path
import re
import sys


def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def verify(record):
    previous, seen = '', set()
    for position, entry in enumerate(record['entries'], 1):
        envelope = entry['envelope']
        if entry['sequence'] != position or entry['id'] in seen:
            raise ValueError('Ledger position or identity changed')
        if any(parent not in seen for parent in envelope.get('parents', [])):
            raise ValueError('Causal parent missing or out of order')
        if any(envelope[k] != entry[k] for k in ['id', 'sequence', 'digest']):
            raise ValueError('Envelope stamp differs from ledger')
        body = {k:v for k,v in envelope.items() if k not in ['sequence', 'digest', 'accepted']}
        canonical = json.dumps(body, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if 'sha256:' + sha256(canonical) != entry['digest']:
            raise ValueError('Envelope digest changed')
        if sha256((previous + ':' if previous else 'grail-ledger:') + entry['digest']) != entry['link']:
            raise ValueError('Ledger link changed')
        previous = entry['link']
        seen.add(entry['id'])
    if len(seen) != 4 or record['task_state'] != 'completed':
        raise ValueError('Expected a completed four-entry exchange')
    envelopes = {e['id']:e['envelope'] for e in record['entries']}
    task, result = envelopes[record['task_id']], envelopes[record['result_id']]
    if task['source'] != 'slack' or result['source'] != 'codex' or task['id'] not in result['parents']:
        raise ValueError('The result does not descend from the Slack task')
    refusal = record['refused_impersonation']
    if refusal.get('status') != 403 or refusal.get('code') != 'grail.forbidden':
        raise ValueError('Source-identity refusal missing')
    if len(record['deduplicated_retries']) != 2 or not all(r.get('duplicate') is True for r in record['deduplicated_retries']):
        raise ValueError('Deduplication evidence missing')
    retries = record['deduplicated_retries']
    if {r['id'] for r in retries} != {task['id'], result['id']}:
        raise ValueError('Expected retries of both the task and result')
    if any(r['sequence'] != envelopes[r['id']]['sequence'] for r in retries):
        raise ValueError('A retry changed the accepted ledger position')
    if task['id'] not in [e['id'] for e in record['trace']['entries']]:
        raise ValueError('Recorded trace does not reach the Slack task')
    if re.search(r'ghp_[A-Za-z0-9]{20,}|Bearer\s+[A-Za-z0-9_-]{20,}|eyJ[A-Za-z0-9_-]{20,}\.', json.dumps(record)):
        raise ValueError('Credential-shaped content in public receipt')
    return len(seen)


if __name__ == '__main__':
    path = Path(sys.argv[1])
    count = verify(json.loads(path.read_text()))
    print(f'Recorded Slack/Codex exchange: {count} envelope digests and links verified; refusal, retry, and causality evidence checked')
