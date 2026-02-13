#!/usr/bin/env python3
"""Generate focused Brave query variants from a topic."""

from __future__ import annotations
import argparse


def build(topic: str) -> list[str]:
    t = topic.strip()
    return [
        t,
        f"{t} official documentation",
        f"{t} tutorial OR guide",
        f"{t} troubleshooting common errors",
        f"{t} latest updates",
    ]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("topic")
    args = p.parse_args()

    for i, q in enumerate(build(args.topic), 1):
        print(f"{i}. {q}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
