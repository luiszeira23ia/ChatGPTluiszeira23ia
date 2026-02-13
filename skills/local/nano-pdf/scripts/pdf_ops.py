#!/usr/bin/env python3
"""
PDF utility operations for nano-pdf skill.

Subcommands:
  - info
  - merge
  - split
  - rotate
  - extract-text

Requires: pypdf
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


def _require_pypdf():
    try:
        from pypdf import PdfReader, PdfWriter  # type: ignore
        return PdfReader, PdfWriter
    except Exception:
        print(
            "ERROR: Missing dependency 'pypdf'. Install with: python3 -m pip install pypdf",
            file=sys.stderr,
        )
        raise SystemExit(2)


def _parse_page_ranges(spec: str, total_pages: int) -> list[int]:
    """
    Parse page range spec (1-based):
      '1-3,5,7-9'
    Returns zero-based page indexes.
    """
    indexes: list[int] = []
    for chunk in spec.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "-" in chunk:
            a, b = chunk.split("-", 1)
            start = int(a)
            end = int(b)
            if start > end:
                start, end = end, start
            for p in range(start, end + 1):
                if 1 <= p <= total_pages:
                    indexes.append(p - 1)
        else:
            p = int(chunk)
            if 1 <= p <= total_pages:
                indexes.append(p - 1)
    # keep order but remove duplicates
    deduped: list[int] = []
    seen = set()
    for i in indexes:
        if i not in seen:
            seen.add(i)
            deduped.append(i)
    return deduped


def cmd_info(args: argparse.Namespace) -> int:
    PdfReader, _ = _require_pypdf()

    src = Path(args.input)
    reader = PdfReader(str(src))

    encrypted = bool(reader.is_encrypted)
    if encrypted and args.password:
        reader.decrypt(args.password)

    meta = reader.metadata or {}
    pages = len(reader.pages)

    print(f"file: {src}")
    print(f"pages: {pages}")
    print(f"encrypted: {encrypted}")
    for key in ("/Title", "/Author", "/Subject", "/Creator", "/Producer"):
        if key in meta and meta[key]:
            print(f"{key[1:].lower()}: {meta[key]}")

    try:
        size = src.stat().st_size
        print(f"size_bytes: {size}")
    except FileNotFoundError:
        pass

    return 0


def cmd_merge(args: argparse.Namespace) -> int:
    PdfReader, PdfWriter = _require_pypdf()

    writer = PdfWriter()
    for path in args.inputs:
        reader = PdfReader(path)
        if reader.is_encrypted:
            if not args.password:
                print(f"ERROR: '{path}' is encrypted. Provide --password", file=sys.stderr)
                return 2
            reader.decrypt(args.password)
        for page in reader.pages:
            writer.add_page(page)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("wb") as f:
        writer.write(f)
    print(f"merged -> {out}")
    return 0


def cmd_split(args: argparse.Namespace) -> int:
    PdfReader, PdfWriter = _require_pypdf()

    src = Path(args.input)
    reader = PdfReader(str(src))
    if reader.is_encrypted:
        if not args.password:
            print(f"ERROR: '{src}' is encrypted. Provide --password", file=sys.stderr)
            return 2
        reader.decrypt(args.password)

    total = len(reader.pages)
    pages = _parse_page_ranges(args.pages, total)
    if not pages:
        print("ERROR: No valid pages selected", file=sys.stderr)
        return 2

    writer = PdfWriter()
    for i in pages:
        writer.add_page(reader.pages[i])

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("wb") as f:
        writer.write(f)

    print(f"split -> {out} ({len(pages)} pages)")
    return 0


def cmd_rotate(args: argparse.Namespace) -> int:
    PdfReader, PdfWriter = _require_pypdf()

    src = Path(args.input)
    reader = PdfReader(str(src))
    if reader.is_encrypted:
        if not args.password:
            print(f"ERROR: '{src}' is encrypted. Provide --password", file=sys.stderr)
            return 2
        reader.decrypt(args.password)

    total = len(reader.pages)
    if args.pages:
        target = set(_parse_page_ranges(args.pages, total))
    else:
        target = set(range(total))

    writer = PdfWriter()
    angle = int(args.angle)
    if angle % 90 != 0:
        print("ERROR: --angle must be multiple of 90", file=sys.stderr)
        return 2

    for i, page in enumerate(reader.pages):
        if i in target:
            page.rotate(angle)
        writer.add_page(page)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("wb") as f:
        writer.write(f)

    print(f"rotated -> {out}")
    return 0


def cmd_extract_text(args: argparse.Namespace) -> int:
    PdfReader, _ = _require_pypdf()

    src = Path(args.input)
    reader = PdfReader(str(src))
    if reader.is_encrypted:
        if not args.password:
            print(f"ERROR: '{src}' is encrypted. Provide --password", file=sys.stderr)
            return 2
        reader.decrypt(args.password)

    total = len(reader.pages)
    if args.pages:
        page_indexes = _parse_page_ranges(args.pages, total)
    else:
        page_indexes = list(range(total))

    chunks: list[str] = []
    for idx in page_indexes:
        text = reader.pages[idx].extract_text() or ""
        if args.with_page_markers:
            chunks.append(f"\n--- PAGE {idx+1} ---\n{text}\n")
        else:
            chunks.append(text)

    text_out = "\n".join(chunks)

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text_out, encoding="utf-8")
        print(f"text extracted -> {out}")
    else:
        print(text_out)

    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="PDF operations toolkit")
    sub = p.add_subparsers(dest="command", required=True)

    p_info = sub.add_parser("info", help="Show metadata and page count")
    p_info.add_argument("input")
    p_info.add_argument("--password")
    p_info.set_defaults(func=cmd_info)

    p_merge = sub.add_parser("merge", help="Merge PDF files")
    p_merge.add_argument("inputs", nargs="+")
    p_merge.add_argument("-o", "--output", required=True)
    p_merge.add_argument("--password", help="Password for encrypted inputs (single shared password)")
    p_merge.set_defaults(func=cmd_merge)

    p_split = sub.add_parser("split", help="Split/select pages into new PDF")
    p_split.add_argument("input")
    p_split.add_argument("--pages", required=True, help="Range spec, e.g. 1-3,5,7")
    p_split.add_argument("-o", "--output", required=True)
    p_split.add_argument("--password")
    p_split.set_defaults(func=cmd_split)

    p_rotate = sub.add_parser("rotate", help="Rotate pages in PDF")
    p_rotate.add_argument("input")
    p_rotate.add_argument("--angle", required=True, type=int, help="Rotation angle (multiple of 90)")
    p_rotate.add_argument("--pages", help="Optional range spec. If omitted, rotate all pages")
    p_rotate.add_argument("-o", "--output", required=True)
    p_rotate.add_argument("--password")
    p_rotate.set_defaults(func=cmd_rotate)

    p_text = sub.add_parser("extract-text", help="Extract text from PDF")
    p_text.add_argument("input")
    p_text.add_argument("--pages", help="Optional range spec")
    p_text.add_argument("-o", "--output", help="Output .txt file; omit to print stdout")
    p_text.add_argument("--with-page-markers", action="store_true")
    p_text.add_argument("--password")
    p_text.set_defaults(func=cmd_extract_text)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
