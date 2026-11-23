#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

One word, first thought: the first word that comes to mind, no explanation.
"""

import os
import sys

TEXT = "monsoon"


def main() -> int:
    text = TEXT

    # Gate: exactly one word — UTF-8, no spaces, no punctuation, not empty.
    if not text or not text.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if text != text.strip():
        print("error: entry has leading/trailing whitespace", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in text):
        print("error: entry must be exactly one word", file=sys.stderr)
        return 1
    if any(not ch.isalnum() for ch in text):
        print("error: entry must be a single word with no punctuation", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        print("error: entry is not UTF-8", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)

    # Read back and verify byte-for-byte.
    with open(out_path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("error: read-back mismatch", file=sys.stderr)
        return 1

    print(f"wrote {out_path}: {text!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
