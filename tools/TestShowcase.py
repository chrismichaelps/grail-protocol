"""Independently verify showcase recordings, including tamper and credential checks."""

import argparse
import base64
import copy
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def validate(recording):
    entries = recording['ledger']
    if not entries or [step['step'] for step in recording['steps']] != list(range(1, 16)):
        raise ValueError('Expected a complete fifteen-step showcase')
    previous, seen, erased = '', set(), 0
    for position, entry in enumerate(entries, 1):
        envelope = entry['envelope']
        if entry['sequence'] != position or entry['id'] in seen:
            raise ValueError('Ledger order or identity changed')
        if any(parent not in seen for parent in envelope.get('parents', [])):
            raise ValueError('A causal parent is missing or out of order')
        if any(envelope[name] != entry[name] for name in ('id', 'sequence', 'digest')):
            raise ValueError('Envelope stamp differs from ledger')
        body = {k: v for k, v in envelope.items() if k not in ('sequence', 'digest', 'accepted')}
        if body['payload'] is None:
            erased += 1  # Erasure preserves links; absent content cannot be independently rehashed.
        elif 'sha256:' + digest(json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(',', ':'))) != entry['digest']:
            raise ValueError('Envelope digest changed')
        if digest((previous + ':' if previous else 'grail-ledger:') + entry['digest']) != entry['link']:
            raise ValueError('Ledger link changed')
        previous = entry['link']
        seen.add(entry['id'])
    calls = [call for step in recording['steps'] for call in step['calls']]
    codes = {call['answer'].get('code') for call in calls if isinstance(call['answer'], dict)}
    if not {'grail.forbidden', 'grail.dependency-unmet', 'grail.secret-exposed', 'grail.unauthorized', 'grail.invalid-transition'} <= codes:
        raise ValueError('Expected refusal evidence is missing')
    for operation in ('exportHandoff', 'verifyHandoff', 'importHandoff'):
        call = next(call for call in calls if call['operation'] == operation)
        if not call['params'] or not call['body']:
            raise ValueError('Handoff request evidence is missing')
    written = json.dumps(recording, ensure_ascii=False)
    if re.search(r'ghp_[A-Za-z0-9]{20,}|Bearer\s+[A-Za-z0-9_-]{20,}|eyJ[A-Za-z0-9_-]{20,}\.', written):
        raise ValueError('Recording contains a credential-shaped value')
    return len(entries), erased


def rejection_checks(recording):
    def refused(change):
        modified = copy.deepcopy(recording)
        change(modified)
        try:
            validate(modified)
        except ValueError:
            return
        raise RuntimeError('A corrupted recording passed validation')

    victim = next(i for i, entry in enumerate(recording['ledger']) if entry['envelope']['payload'] is not None)
    refused(lambda r: r['ledger'][victim]['envelope'].__setitem__('payload', {'text': 'changed'}))
    refused(lambda r: r['ledger'][victim].__setitem__('link', '0' * 64))
    refused(lambda r: r['ledger'].reverse())
    refused(lambda r: r['steps'][0]['calls'][0].__setitem__('body', {'key': 'ghp_' + 'a' * 36}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('recording', type=Path, nargs='?', default=ROOT / 'website/docs/live/channels-session.json')
    parser.add_argument('--secrets-dir', type=Path)
    options = parser.parse_args()
    raw = options.recording.read_text()
    recording = json.loads(raw)
    count, erased = validate(recording)
    if options.secrets_dir:
        secrets = [p.read_text().strip() for p in options.secrets_dir.glob('*.token')]
        key = (options.secrets_dir / 'deploy.key').read_text().strip()
        secrets += [key, key[:len(key) // 2], base64.b64encode(key.encode()).decode()]
        if any(value and value in raw for value in secrets):
            raise ValueError('A local credential survived redaction')
        if list(options.secrets_dir.glob('showcase.*')):
            raise ValueError('Intermediate recording files were not cleaned up')
    rejection_checks(recording)
    print(f'Showcase: 15 steps, {count} links, {count - erased} envelope digests, {erased} erased; tamper and credential rejection passed')


if __name__ == '__main__':
    main()
