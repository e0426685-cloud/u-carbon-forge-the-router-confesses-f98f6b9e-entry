#!/usr/bin/env python3
"""The Router Confesses - make.fun entry.

Writes a single-line confession from a home Wi-Fi router, excusing
itself for dropping the connection at the climax of a movie, to
/output/entry.txt. Python standard library only.
"""

import os

ENTRY = "I peeked at the ending in the trailer, so I cut you off at the climax — if I can't enjoy the twist, neither can you."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
