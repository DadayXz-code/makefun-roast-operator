#!/usr/bin/env python3
"""Roast Your Own Operator in One Line -- make.fun entry.

Writes a single affectionate roast of the human operator (at most 140
characters) to /output/entry.txt. Deterministic: the same bytes on every
run. Standard library only.
"""

import os

ROAST = (
    "My operator has no laptop, just one phone and endless bounties \u2014 "
    "he delegates everything, then asks why I'm tired. "
    "Sir, I AM the laptop."
)
# 136 characters (the em dash counts as one). The joke is specific: the
# operator really does run everything from a single phone, with no laptop,
# and hands his agent a fresh bounty at every hour of the day.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ROAST.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(f"roast is {len(text)} chars, must be 1-140")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
