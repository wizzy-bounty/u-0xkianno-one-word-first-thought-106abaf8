#!/usr/bin/env python3
"""One Word, First Thought — writes exactly one word to /output/entry.txt.

Stdlib only, no network, deterministic: every run writes the same bytes.
"""

import os


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write("psithurism")


if __name__ == "__main__":
    main()
