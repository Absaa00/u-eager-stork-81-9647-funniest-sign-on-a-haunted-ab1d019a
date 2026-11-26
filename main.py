#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes exactly one line (<=120 chars) to /output/entry.txt.
Deterministic: no randomness, no network, no input.
"""

import os

LINE = (
    "WARNING: Haunted. Do not unplug anything - "
    "the ghost is load-bearing. It holds the RAID array together."
)


def main() -> None:
    assert len(LINE) <= 120, f"line is {len(LINE)} chars, over the 120 limit"
    assert LINE.count("\n") == 0, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
