#!/usr/bin/env python3
"""The Internet in One Word.

Writes the single word that describes the whole internet to
/output/entry.txt. The entry is that word and nothing else:
no files, no code, no links.
"""

import os

WORD = "brainrot"
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    try:
        os.chmod(OUTPUT_DIR, 0o755)
    except OSError:
        pass
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD)
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
