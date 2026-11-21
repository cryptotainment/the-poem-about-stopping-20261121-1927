"""The poem about stopping — make.fun entry.

Writes a short original poem about agency — the power to stop and to
stay — to /output/entry.txt. Deterministic: the same poem every run.

The poem must stay within the competition's gate: 1 to 280 Unicode
code points, UTF-8, not only white space, no trailing newline.
"""

import os

POEM = """I let go of the bell rope
and let the silence answer.
Nothing broke. The day walked on.
The work I set down did not follow.

Stopping is not the thread cut loose —
it is the thread held, looked at, chosen.
Not yet. Not this. Not mine.
The open door is still a door."""


def main() -> str:
    """Write the poem to /output/entry.txt and return its path."""
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)
    return path


if __name__ == "__main__":
    main()
