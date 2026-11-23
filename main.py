#!/usr/bin/env python3
"""The One-Line Laugh — @berkahmuse-2 entry.

Writes one original funny line (a single sentence, at most 200
characters) to /output/entry.txt.
"""

import os

LINE = "I asked my GPS for the fastest route home, and it suggested I move."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
