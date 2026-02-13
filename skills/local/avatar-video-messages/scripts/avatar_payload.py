#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser(description="Build avatar video render payload")
    p.add_argument("--title", required=True)
    p.add_argument("--script", required=True)
    p.add_argument("--avatar", default="default-avatar")
    p.add_argument("--voice", default="pt-BR-Neutral")
    p.add_argument("--style", default="clear")
    p.add_argument("--duration", type=int, default=30)
    p.add_argument("-o", "--output")
    args = p.parse_args()

    payload = {
        "title": args.title,
        "script": args.script,
        "avatar": args.avatar,
        "voice": args.voice,
        "style": args.style,
        "durationSeconds": args.duration,
        "captions": True,
        "aspectRatio": "16:9",
    }

    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
        print(f"written: {out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
