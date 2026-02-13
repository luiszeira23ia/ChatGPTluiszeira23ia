#!/usr/bin/env python3
from __future__ import annotations

import argparse

SNIPPETS = {
    "title": "document.title",
    "ready-state": "document.readyState",
    "links-count": "document.querySelectorAll('a').length",
    "images-count": "document.querySelectorAll('img').length",
}


def main() -> int:
    p = argparse.ArgumentParser(description="Print reusable JS snippets for canvas eval")
    p.add_argument("--snippet", choices=SNIPPETS.keys(), required=True)
    args = p.parse_args()
    print(SNIPPETS[args.snippet])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
