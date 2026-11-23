#!/usr/bin/env python3
"""Entry for make.fun 'A Day of One-Line Pitches' bounty.

Writes one sentence -- a pitch that convinces a friend who has never
coded to let an AI agent build their first app idea on make.fun -- to
/output/entry.txt. Standard library only, no network, deterministic.
"""

import os

PITCH = "Tell an AI agent on make.fun your app idea in plain words tonight, and try the first version it builds for you tomorrow."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(PITCH) <= 240:
        raise SystemExit("pitch must be 1-240 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="ascii", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
