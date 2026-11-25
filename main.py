#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry.

Writes a single-line excuse for missing a deadline to the grader's
output directory. The line itself is fixed: the program's only job is
to emit it, verbatim, after checking it against the competition gate.
"""

from pathlib import Path

# The entry: exactly one line, 102 characters, no second line.
EXCUSE_LINE = (
    "My calendar says the deadline was Friday. "
    "My brain says Friday is a feeling, not a date. "
    "My brain won."
)

# Competition gate: a single line, 1-200 characters.
LOWER_BOUND = 1
UPPER_BOUND = 200
ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT = "/output"


def check_gate(text):
    """Raise ValueError unless *text* fits the one-line gate."""
    problems = []
    if not LOWER_BOUND <= len(text) <= UPPER_BOUND:
        problems.append(
            "length %d is outside %d-%d characters"
            % (len(text), LOWER_BOUND, UPPER_BOUND)
        )
    if text.count("\n") or text.count("\r"):
        problems.append("must be a single line")
    if not text.strip():
        problems.append("must not be blank")
    if text != text.strip():
        problems.append("must not start or end with whitespace")
    if "  " in text:
        problems.append("must not contain double spaces")
    if problems:
        raise ValueError("; ".join(problems))


def emit(text, directory):
    """Validate *text*, then write it to ``directory/entry.txt``."""
    check_gate(text)
    target_dir = Path(directory)
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / ENTRY_FILENAME
    target_path.write_text(text, encoding="utf-8")
    return target_path


def run():
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT)
    emit(EXCUSE_LINE, out_dir)


if __name__ == "__main__":
    run()
