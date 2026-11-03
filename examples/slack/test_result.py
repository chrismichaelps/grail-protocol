"""The actual recorded Codex answer, followed by independent behavior checks."""

import unicodedata


def slugify(title):
    result = []
    pending_separator = False

    for char in unicodedata.normalize("NFD", title.lower()):
        if unicodedata.category(char).startswith("M"):
            continue
        if char.isalnum():
            if pending_separator and result:
                result.append("-")
            result.append(char)
            pending_separator = False
        else:
            pending_separator = True

    return "".join(result)


assert slugify("  Héllo___Wörld!!  ") == "hello-world"
assert slugify("東京_Привет ١٢٣") == "東京-привет-١٢٣"
assert slugify("") == ""

assert slugify(" Hello, World! ") == "hello-world"
assert slugify("a___b---c") == "a-b-c"
assert slugify("---") == ""
assert slugify("Café déjà vu") == "cafe-deja-vu"
assert slugify("東京") == "東京"
assert slugify("Привет мир") == "привет-мир"
assert slugify("١٢٣") == "١٢٣"
assert slugify("  abc  ") == "abc"
assert slugify("a.b/c") == "a-b-c"

print("Recorded Codex answer: 3 supplied assertions and 9 additional checks passed")
