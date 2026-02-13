#!/usr/bin/env python3
from __future__ import annotations
import argparse


def main() -> int:
    p = argparse.ArgumentParser(description="Build Discord announcement payload text")
    p.add_argument("--title", required=True)
    p.add_argument("--body", required=True)
    p.add_argument("--cta", default="")
    args = p.parse_args()

    lines = [f"**{args.title}**", "", args.body]
    if args.cta:
        lines += ["", f"➡️ {args.cta}"]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
