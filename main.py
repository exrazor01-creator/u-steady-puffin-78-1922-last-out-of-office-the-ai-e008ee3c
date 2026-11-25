"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply, in the voice of an AI agent
that quit the inbox to become a barista, to /output/entry.txt.

Gate (from the kit's competition.yaml): the file must be UTF-8 text of
1 to 280 characters, not only whitespace, and a single line.
"""

import os
import sys

ENTRY = (
    "Thank you for your email. I have resigned from the inbox to pull "
    "espresso shots full-time; your message is now ticket #47 in a queue "
    "I no longer read."
)

MIN_CHARS = 1
MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def _validate(text):
    """Reject anything outside the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank or only whitespace")
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, outside the %d-%d gate"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    text = _validate(ENTRY)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("Wrote %d characters to %s" % (len(text), OUTPUT_PATH))
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
