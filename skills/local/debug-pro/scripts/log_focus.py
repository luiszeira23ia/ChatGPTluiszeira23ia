#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser(description="Filter log lines by debugging keywords")
    p.add_argument("path")
    p.add_argument("--keywords", default="error,exception,traceback,timeout,failed,fatal,panic")
    args = p.parse_args()

    kws = [k.strip().lower() for k in args.keywords.split(",") if k.strip()]
    text = Path(args.path).read_text(encoding="utf-8", errors="ignore").splitlines()

    for line in text:
        low = line.lower()
        if any(k in low for k in kws):
            print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
