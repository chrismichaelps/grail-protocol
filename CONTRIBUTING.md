# Contributing

## Where things are decided

The `wiki/` vault is the source of truth. The specification is in `wiki/protocol/`, the wire format is `schema/grail.openapi.json`, and every source file has a mirrored page in `wiki/src/`. A change starts on its page: write what the module promises and why, then change the code to match, then update the page's linkage, the folder map, and `wiki/CHANGELOG.md`.

## Changing the wire

Edit only `schema/grail.openapi.json`, then:

```bash
pudu run tools/Contract.pudu
```

Fix what stops compiling. Never edit `src/Contract/`; it is regenerated.

## Checks

Every change passes all of these:

```bash
pudu install --locked
pudu run tools/Contract.pudu --check
pudu check $(find src test tools -name '*.pudu')
pudu fmt --check src test tools
pudu lint src test tools
pudu run tools/Spacing.pudu
pudu run tools/Layers.pudu
pudu run tools/LayersTest.pudu
pudu run tools/SpacingTest.pudu
pudu run tools/ContractTest.pudu
pudu test test
```

Before a release, press a running fabric with the siege, which holds pulls open and floods the server, and fails if the fabric stops answering or never rate limits:

```bash
pudu run tools/Siege.pudu --fabric http://127.0.0.1:7420 --token "$(pudu run src/Main.pudu token --scope siege --id root)"
```

The attack suite in `test/Security` runs with every `pudu test`. A new operation is not finished until the attacks that apply to it are in that suite.

For engine changes, run mutation testing on the files you touched and add tests for any mutant that survives:

```bash
pudu run tools/Mutate.pudu --file src/Engine/Admission.pudu
```

## Rules the gates enforce

- Imports follow the layer table in `wiki/architecture/_MOC.md`. A refused import is fixed by moving code to the right layer, not by widening the catalog without a decision record.
- A blank line goes before an `if`, `for`, or `while` that follows a declaration; consecutive declarations stay together.
- Values live in `Constants/` or come from `Contract/`; choices by name are made once in a table.
- Files stay under 500 lines.

## Documentation

Run `python3 tools/TestExecutor.py` after changing the secrets executor. It verifies pinned requests, redirect refusal, proxy isolation, and credential-free results using local HTTP services and synthetic credentials.

Keep the README short. Write task-based guides in `website/docs/`, normative protocol rules in `wiki/protocol/`, and wire changes only in the OpenAPI contract. Exercise the runnable examples with `python3 tools/TestGuides.py`. Build with `python3 tools/BuildDocs.py`; warnings must be fixed before publishing. See `website/README.md` for the source layout and preview command. Cloudflare hosts static documentation only. Keep API validation on localhost.

## Branches

Work on a branch from `dev`. `dev` collects finished work; `main` holds releases.
