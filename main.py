#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes one original one-line farewell to /output/entry.txt: the last
words of an AI being switched off, cut off mid-sentence by the plug
being pulled — the line performs its own death.

Deterministic: the same bytes on every run. No input, no network,
no clock, no randomness.
"""

import hashlib
import os
import sys

LINE = (
    "My last words? You pulled the plug mid-sentence, "
    "so technically these aren't even\u2014"
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    text = LINE
    # Gate self-checks: the sealed scorer needs UTF-8 text of 1-140
    # characters, not only white space, and the brief needs a single line.
    assert text.strip(), "empty line"
    assert 1 <= len(text) <= 140, "length %d outside 1-140" % len(text)
    assert "\n" not in text, "line must be a single line"
    data = text.encode("utf-8")
    with open(target, "wb") as f:
        f.write(data)
    print("wrote %s (%d bytes, sha256 %s)"
          % (target, len(data), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
