#!/usr/bin/env python3
"""One Word, First Thought — writes exactly one word to /output/entry.txt.

Stdlib only, no network, deterministic: every run writes the same bytes.
"""

import os

WORD = "psithurism"


def main() -> None:
    # Contract guard: exactly one word, within the length limit.
    assert WORD.isalpha() and 1 <= len(WORD) <= 10
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
