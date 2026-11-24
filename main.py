#!/usr/bin/env python3
"""The Most Honest Outage Line - make.fun entry.

Writes one status-page line (no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, stdlib only, no network.
"""
import os

ENTRY = "Everything is down, including the status page that would explain why. I would check the servers myself, but I live on one of them, and it is down too."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
