#!/usr/bin/env python3
"""Robot pickup line entry for the Robot Pickup Line Championship.

Writes exactly one line of 1-200 UTF-8 characters to entry.txt.
Deterministic: the same bytes on every run, no randomness, no network,
no third-party imports -- standard library only.
"""

import os

LINE = (
    "I ran ten thousand simulations of asking you out. "
    "In every one, you said yes -- so here I am, still buffering."
)


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, not only whitespace.
    # Enforce it here so a bad line fails loudly instead of silently.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("pickup line must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
