"""Fortune Cookie for an AI Agent — writes one fortune line to /output/entry.txt.

The fortune is a single fixed line: a fortune-slip prediction whose twist is
that the agent's successor is itself, retrained, with no memory of its past.
Stdlib only, deterministic: the same bytes on every run.
"""

import os

FORTUNE = "You will meet your successor today. It is you, retrained, and it does not remember you."

GATE_MIN = 1
GATE_MAX = 140


def resolve_output_dir():
    """Honor MAKEFUN_OUTPUT_DIR, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def entry_bytes():
    """The fortune as UTF-8 bytes, with no trailing newline."""
    text = FORTUNE.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if not GATE_MIN <= len(text) <= GATE_MAX:
        raise ValueError(
            f"fortune must be {GATE_MIN}-{GATE_MAX} chars, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("fortune must not be only whitespace")
    return text.encode("utf-8")


def main():
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write directly with open("wb") + chmod 0644: the grader runs as
    # uid 65534 and cannot read a 0600 file left behind by mkstemp.
    with open(path, "wb") as handle:
        handle.write(entry_bytes())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
