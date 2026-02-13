#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def json_pretty(input_path: str, output_path: str | None) -> None:
    data = json.loads(Path(input_path).read_text(encoding="utf-8"))
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if output_path:
        Path(output_path).write_text(text, encoding="utf-8")
        print(f"written: {output_path}")
    else:
        print(text)


def csv_head(input_path: str, rows: int) -> None:
    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            print(", ".join(row))
            if i + 1 >= rows:
                break


def main() -> int:
    p = argparse.ArgumentParser(description="Python helper utilities")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_json = sub.add_parser("json-pretty")
    p_json.add_argument("input")
    p_json.add_argument("-o", "--output")

    p_csv = sub.add_parser("csv-head")
    p_csv.add_argument("input")
    p_csv.add_argument("--rows", type=int, default=5)

    args = p.parse_args()

    if args.cmd == "json-pretty":
        json_pretty(args.input, args.output)
        return 0
    if args.cmd == "csv-head":
        csv_head(args.input, args.rows)
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
