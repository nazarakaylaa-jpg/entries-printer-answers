#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes one line, the office printer's comeback, to /output/entry.txt.
The line is chosen from CANDIDATES.md: the printer's own voice — weary,
literal, faintly passive-aggressive — with the flat logic of a device that
has counted every sheet it ever fed.
"""

import os

ENTRY = (
    "I printed 214,311 pages without a single complaint. "
    "One jam and you hit me. "
    "Incident logged. HR has been notified."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 240):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-240")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Self-check: what the grader reads must be exactly the line above,
    # valid UTF-8, 1-240 chars, not whitespace-only.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt content mismatch"
    assert 1 <= len(written) <= 240 and written.strip()
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
