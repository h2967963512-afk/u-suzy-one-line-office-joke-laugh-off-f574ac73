"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

How it runs: ``python3 main.py`` creates /output if needed and writes the
entry line to /output/entry.txt (UTF-8, no trailing newline).

Verification: run it, then check the file holds exactly one line of 99
characters matching the TEXT constant; the sha256 of /output/entry.txt is
604330d89473aabcf12cf69fb69864f78033846733a395dab6066def304580f2. Re-running
after any edit must leave that hash unchanged unless the line itself changed.
"""

import os

TEXT = "I put 'per my last email' in my out-of-office reply, so now even my vacation is passive-aggressive."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
