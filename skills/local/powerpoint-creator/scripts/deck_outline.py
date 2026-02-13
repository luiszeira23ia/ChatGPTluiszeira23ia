#!/usr/bin/env python3
from __future__ import annotations

import argparse


def main() -> int:
    p = argparse.ArgumentParser(description="Generate a PowerPoint deck outline")
    p.add_argument("--topic", required=True)
    p.add_argument("--slides", type=int, default=8)
    args = p.parse_args()

    s = max(3, args.slides)
    titles = [
        "Title",
        "Agenda",
        "Current State",
        "Key Insights",
        "Proposal",
        "Execution Plan",
        "Risks & Mitigations",
        "Next Steps",
    ]

    print(f"Deck Topic: {args.topic}\n")
    for i in range(1, s + 1):
        t = titles[i - 1] if i - 1 < len(titles) else f"Appendix {i - len(titles)}"
        print(f"Slide {i}: {t}")
        print("- Main point")
        print("- Supporting detail")
        print("- Suggested visual\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
