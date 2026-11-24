#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
The entry is the whole pitch: the judge reads the text, nothing else.
"""

import os
import sys

PITCH = "A toothbrush that files a noise complaint against you every time you brush too hard, then goes on strike until you apologize to your gums."


def main() -> int:
    # The sealed gate only accepts 1 to 220 UTF-8 characters, so refuse
    # loudly here rather than shipping a text the gate would reject.
    if not 1 <= len(PITCH) <= 220 or not PITCH.strip():
        print(f"pitch fails the 1-220 character gate: {len(PITCH)} chars",
              file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    print(f"wrote {len(PITCH)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
