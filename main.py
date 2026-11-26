#!/usr/bin/env python3
"""The Funniest Honest Appliance Error.

Writes one line to /output/entry.txt: the funniest honest error message
an appliance could show. A washing machine, flat and put-upon, reporting
an unbalanced load exactly as it experiences it.

Gate: the bounty scores /output/entry.txt valid only when it is UTF-8
text of 1 to 200 characters, not only white space. The line below is
84 characters, and the program refuses to write anything that breaks
the gate instead of silently shipping an invalid entry.
"""

import os

LINE = "Error E4: Unbalanced load. I have spun one sock for 47 minutes. It is still winning."

MAX_CHARS = 200


def main():
    if not (1 <= len(LINE) <= MAX_CHARS) or not LINE.strip():
        raise SystemExit("entry line fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
