#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re


def prep(text: str) -> str:
    t = text.strip()
    t = re.sub(r"\s+", " ", t)
    # add small pauses for speech cadence
    t = t.replace(";", ". ")
    t = t.replace(":", ". ")
    return t


def main() -> int:
    p = argparse.ArgumentParser(description="Prepare text for narration")
    p.add_argument("text")
    args = p.parse_args()
    print(prep(args.text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
