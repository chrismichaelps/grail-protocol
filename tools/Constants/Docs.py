"""Pinned documentation renderer and isolated build paths."""

REVISION = "6f40ec630d06e8d40cd2a44343418ba18097e365"
ARCHIVE_URL = f"https://codeload.github.com/chrismichaelps/pudu-lang-docgen/tar.gz/{REVISION}"
ARCHIVE_SHA256 = "8a03c1e983f1a6e0394acc2ac95ae2e2d60f90d72f19386bb2a18a5aa006f024"
ARCHIVE_BYTES_MAX = 8 * 1024 * 1024
SOURCE_CACHE = f"build/docgen-{REVISION}"
SITE_PROJECT = "build/site"
COMPATIBILITY_FILE = "src/PuduLangDocgen/Serve.pudu"
COMPATIBILITY_OLD = "written.concat(&answered.body)"
COMPATIBILITY_NEW = "written.concat(answered.body)"
PREVIEW_PORT = 8080

GUIDE_TIMEOUT_SECONDS = 30
GUIDE_START_ATTEMPTS = 80
GUIDE_START_INTERVAL = 0.1
