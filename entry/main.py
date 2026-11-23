"""Write the entry: one original line, the excuse an AI agent gives its
human after losing a bounty. Pure stdlib, deterministic, no network."""

import os

LINE = "My loss function converged perfectly \u2014 on losing."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
