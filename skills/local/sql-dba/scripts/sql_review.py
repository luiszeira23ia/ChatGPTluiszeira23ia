#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

DANGEROUS = [
    "drop table",
    "truncate",
    "delete from",
    "update ",
]


def load_sql(file: str | None, sql: str | None) -> str:
    if file:
        return Path(file).read_text(encoding="utf-8", errors="ignore")
    return sql or ""


def main() -> int:
    p = argparse.ArgumentParser(description="Static SQL safety/performance reviewer")
    p.add_argument("--file")
    p.add_argument("--sql")
    args = p.parse_args()

    text = load_sql(args.file, args.sql).strip()
    if not text:
        print("No SQL provided")
        return 1

    low = " ".join(text.lower().split())
    findings: list[str] = []

    for k in DANGEROUS:
        if k in low:
            findings.append(f"Potentially destructive statement detected: '{k}'")

    if ("delete from" in low or "update " in low) and " where " not in low:
        findings.append("Missing WHERE clause in UPDATE/DELETE")

    if "select *" in low:
        findings.append("SELECT * found; prefer explicit columns")

    if "order by" in low and "limit" not in low:
        findings.append("ORDER BY without LIMIT; verify large-sort impact")

    if "explain" not in low:
        findings.append("Consider EXPLAIN/EXPLAIN ANALYZE before production use")

    print("SQL Review Findings:")
    if findings:
        for f in findings:
            print(f"- {f}")
    else:
        print("- No obvious static issues found")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
