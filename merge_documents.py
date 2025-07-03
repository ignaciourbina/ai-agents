#!/usr/bin/env python3
"""Merge markdown sections into a single consolidated document.

This script defines the order of the three markdown files found in the
repository and concatenates them into one file called ``CONSOLIDATED.md``.
It can be rerun any time the source markdown files change.

Usage:
    python3 merge_documents.py
"""
from pathlib import Path

# Files to merge in the desired order
FILES = [
    "prompt-engineering.md",        # Section 1
    "SYSTEM_PROMPT_BLUEPRINT.md",   # Section 2
    "Email-to-Action-Extractor-Audit.md"  # Section 3
]

OUTPUT_FILE = Path("CONSOLIDATED.md")

def main() -> None:
    """Read all source files and combine them sequentially."""
    with OUTPUT_FILE.open("w", encoding="utf-8") as outfile:
        for filename in FILES:
            path = Path(filename)
            if not path.is_file():
                raise FileNotFoundError(f"Source file missing: {filename}")
            outfile.write(path.read_text(encoding="utf-8"))
            outfile.write("\n\n")  # separate sections
    print(f"Consolidated file written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
