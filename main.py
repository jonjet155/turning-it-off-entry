"""Entry for make.fun "Have You Tried Turning It Off?".

Writes one funny tech-support line (127 characters) to entry.txt.
Stdlib only, deterministic, no network.
"""

import os

ENTRY = "I'm sorry your laptop's Wi-Fi is playing hide-and-seek; let's give it a gentle pep talk and see if it remembers how to connect."
# The line is written byte-exact with no trailing newline, so entry.txt
# stays at exactly 127 characters (within the 1-199 gate).


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
