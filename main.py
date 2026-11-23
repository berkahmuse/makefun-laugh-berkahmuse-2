#!/usr/bin/env python3
"""The One-Line Laugh — @berkahmuse-2 entry.

Writes one original funny line (a single sentence, at most 200
characters) to /output/entry.txt.
"""

import os

LINE = "I asked my GPS for the fastest route home, and it suggested I move."

MAX_CHARS = 200


def validate(line: str) -> None:
    """The gate accepts UTF-8 text of 1-200 chars, not only whitespace,
    standing alone as a single sentence."""
    assert 1 <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line.strip(), "line must not be only whitespace"
    assert line.count(".") == 1 and line.endswith("."), "must be one sentence"


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
