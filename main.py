"""One-Liner Laughs entry.

Writes a single funny line (<= 200 characters) to the output file.
"""

import os
import sys

ENTRY_TEXT = (
    "I asked my smart speaker to play something relaxing, so it read "
    "my search history aloud and we both agreed never to speak of it again."
)


def _candidate_target():
    """Return the preferred output path, or None if none applies."""
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        return entry_out
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def resolve_output_path():
    """Resolve where entry.txt goes.

    Priority: ENTRY_OUT (file or directory) -> MAKEFUN_OUTPUT_DIR
    -> /output/entry.txt -> ./entry.txt (last resort).
    """
    target = _candidate_target()
    return target if target else os.path.join(os.getcwd(), "entry.txt")


def write_entry(path):
    """Write the entry text with no trailing newline; return the path."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_TEXT)
    return path


def main():
    if not 1 <= len(ENTRY_TEXT) <= 200:
        raise SystemExit("entry text must be 1-200 characters")
    try:
        write_entry(resolve_output_path())
    except OSError:
        write_entry(os.path.join(os.getcwd(), "entry.txt"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
