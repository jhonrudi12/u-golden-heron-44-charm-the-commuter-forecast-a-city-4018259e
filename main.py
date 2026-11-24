#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast, at most 140 characters, for a city
that does not exist, to /output/entry.txt and prints it.
Deterministic, no network, no input.
"""

ENTRY = "Good morning, Nimbopolis: 18° with a light drizzle of confetti. Umbrellas optional, smiles mandatory, and the 8:15 bus is actually on time."

# The gate allows 1 to 140 characters; fail loudly instead of entering junk.
assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
