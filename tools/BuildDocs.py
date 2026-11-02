"""Build the documentation with a pinned renderer, independently of the fabric."""

import argparse
import hashlib
import io
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request

from Constants import Docs

ROOT = Path(__file__).resolve().parents[1]


def run(arguments, directory):
    subprocess.run(arguments, cwd=directory, check=True)


def renderer():
    cached = ROOT / Docs.SOURCE_CACHE
    if not cached.exists():
        print("Preparing the pinned documentation renderer.", flush=True)
        with urllib.request.urlopen(Docs.ARCHIVE_URL, timeout=30) as response:
            archive = response.read(Docs.ARCHIVE_BYTES_MAX + 1)
        if len(archive) > Docs.ARCHIVE_BYTES_MAX:
            raise RuntimeError("The renderer source archive exceeds its size bound")
        if hashlib.sha256(archive).hexdigest() != Docs.ARCHIVE_SHA256:
            raise RuntimeError("The renderer source archive checksum does not match")
        with tempfile.TemporaryDirectory(prefix="docgen-", dir=ROOT / "build") as temporary:
            with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as bundle:
                bundle.extractall(temporary, filter="data")
            roots = list(Path(temporary).iterdir())
            if len(roots) != 1 or not (roots[0] / "pudu.toml").is_file():
                raise RuntimeError("The renderer source archive has an unexpected layout")
            shutil.move(str(roots[0]), cached)
    source = cached / Docs.COMPATIBILITY_FILE
    text = source.read_text()
    if text.count(Docs.COMPATIBILITY_OLD) == 1:
        # The pinned release borrows a Bytes field where Pudu 0.1.3 requires its value.
        source.write_text(text.replace(Docs.COMPATIBILITY_OLD, Docs.COMPATIBILITY_NEW))
    elif Docs.COMPATIBILITY_NEW not in text:
        raise RuntimeError("The pinned renderer compatibility patch cannot be verified")
    install = ["pudu", "install"]
    if (cached / "pudu.lock").exists():
        install.append("--locked")
    run(install, cached)
    return cached


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--serve", action="store_true", help="preview after a successful build")
    parser.add_argument("--port", type=int, default=Docs.PREVIEW_PORT)
    args = parser.parse_args()
    if sys.version_info < (3, 12):
        parser.error("Python 3.12 or later is required")
    run(["pudu", "run", "tools/Site.pudu"], ROOT)
    cached = renderer()
    arguments = ["pudu", "run", "examples/Cli.pudu", "build", str(ROOT / Docs.SITE_PROJECT), "--warningsAsErrors"]
    if args.serve:
        arguments.extend(["--serve", "--port", str(args.port)])
    run(arguments, cached)


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"Documentation build failed: {error}", file=sys.stderr)
        raise SystemExit(1)
