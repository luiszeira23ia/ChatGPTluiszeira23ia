#!/usr/bin/env python3
from __future__ import annotations
import argparse


def main() -> int:
    p = argparse.ArgumentParser(description="Generate documentation summary template")
    p.add_argument("--mode", choices=["executive", "technical", "action"], default="technical")
    args = p.parse_args()

    if args.mode == "executive":
        print("TL;DR:\n- \n\nTop 3 Points:\n- \n- \n- ")
    elif args.mode == "action":
        print("Objective:\n\nTasks:\n- [ ] \n- [ ] \n\nRisks:\n- \n\nOpen Questions:\n- ")
    else:
        print("Summary:\n\nKey Points:\n- \n\nConstraints:\n- \n\nRisks:\n- \n\nNext Steps:\n- ")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
