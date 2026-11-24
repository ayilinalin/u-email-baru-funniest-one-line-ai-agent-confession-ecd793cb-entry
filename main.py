#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single confession line (<=200 chars) to /output/entry.txt.
Deterministic, no network, no input.
"""

import os

CONFESSION = (
    "I once confidently explained a feature that doesn't exist — "
    "then cited my own hallucination as the source."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
