#!/usr/bin/env python3
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from pathlib import Path


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    p = argparse.ArgumentParser(description="Append incident timeline entry")
    p.add_argument("--file", required=True)
    p.add_argument("--severity", required=True)
    p.add_argument("--event", required=True)
    p.add_argument("--owner", default="unassigned")
    args = p.parse_args()

    line = f"{now_utc()} | sev={args.severity} | owner={args.owner} | {args.event}\n"
    out = Path(args.file)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text((out.read_text(encoding='utf-8') if out.exists() else "") + line, encoding="utf-8")
    print(f"appended -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
