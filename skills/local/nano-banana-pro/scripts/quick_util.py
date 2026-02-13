#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


def slugify(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def count_lines(path: str) -> int:
    p = Path(path)
    return len(p.read_text(encoding="utf-8", errors="ignore").splitlines())


def main() -> int:
    parser = argparse.ArgumentParser(description="Nano Banana Pro quick utilities")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("slugify", help="Convert text to slug")
    p1.add_argument("text")

    p2 = sub.add_parser("lines", help="Count lines in a text file")
    p2.add_argument("path")

    args = parser.parse_args()

    if args.cmd == "slugify":
        print(slugify(args.text))
        return 0

    if args.cmd == "lines":
        print(count_lines(args.path))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
