#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for a houseplant (120 characters or fewer)
to /output/entry.txt. Pure standard library, deterministic: the same text
on every run.
"""

import os

FORTUNE = (
    "This week you will catch your keeper talking to you "
    "when no one else is listening, and bloom a little "
    "prouder for it."
)


def main() -> None:
    text = FORTUNE
    assert 1 <= len(text) <= 120, f"fortune is {len(text)} chars, must be 1-120"
    assert "\n" not in text and "\r" not in text, "fortune must be one line"
    assert text.strip() == text and text.strip(), "fortune must be non-blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
