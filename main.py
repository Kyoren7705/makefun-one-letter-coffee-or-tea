"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to /output/entry.txt:
  A = coffee
  B = tea

Choice: A (coffee). Coffee is the more vivid, stronger, more
unmistakable hot drink: dark, bitter, aromatic, the morning
ritual that wakes you up. A single "A" is also the top grade,
first, and unambiguous.

Deterministic: no randomness, no network, no input, no time
dependence. Two runs produce byte-identical output.
"""
import os

OUTPUT_PATH = "/output/entry.txt"
LETTER = "A"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly one character, no newline, no spaces, UTF-8.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
