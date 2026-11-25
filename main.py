#!/usr/bin/env python3
"""How Many Tabs Do You Have Open?

Writes one number, digits only, to /output/entry.txt: my honest count of
open browser tabs. One hundred and thirty-two tabs, every one of them
something I meant to read, each a small life of its own.
"""

import os

TABS = "132"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TABS)
    print("wrote", path, "->", TABS, f"({len(TABS)} digits)")


if __name__ == "__main__":
    main()
