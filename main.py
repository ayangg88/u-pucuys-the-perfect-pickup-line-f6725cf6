#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes a single short pickup line, the kind an AI agent could actually
say out loud to a person, to /output/entry.txt. The line is capped at
200 characters and has to land on its own with no setup, so it is kept
to one breath: short, self-referential, and with its twist in the
second half.
"""

import os

# The line: an AI agent talking about itself, with a twist the
# listener does not see coming until the second half. "Prompt" does
# double duty — the thing that starts everything an agent generates,
# and the nudge that starts this conversation.
LINE = "You must be a prompt, because everything I generate now starts with you."

MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line with no line breaks")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Round-trip check: what landed on disk must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("round-trip check failed: entry.txt differs from the line")
    print(f"Wrote {len(line)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
