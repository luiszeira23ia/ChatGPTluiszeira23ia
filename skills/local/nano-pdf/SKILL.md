---
name: nano-pdf
description: Create, inspect, edit, and convert PDF files with a fast task-based workflow. Use when asked to merge/split PDFs, rotate pages, extract text, compress files, remove/add pages, or inspect metadata and page structure.
---

# Nano PDF

## Overview

Handle common PDF operations quickly and safely. Prefer deterministic CLI/script steps, verify output files, and preserve originals.

## Quick Start

1. Identify the task type: inspect, extract, transform, or optimize.
2. Copy input files to a working/output path before destructive operations.
3. Execute the smallest reliable operation first.
4. Validate result (page count, readability, file opens correctly).
5. Report what changed and where output was saved.

## Task Playbook

### 1) Inspect PDF

- Read basic metadata (title, author, page count, file size).
- Verify whether the file is encrypted/password protected.
- Confirm page dimensions and orientation when layout matters.

### 2) Extract content

- Extract plain text when user asks for summaries/searchability.
- Extract selected page ranges when only part of the document is needed.
- Preserve page references in output when summarization is requested.

### 3) Transform structure

- Merge multiple PDFs in a user-defined order.
- Split one PDF into ranges or single pages.
- Rotate specific pages or all pages.
- Remove/reorder pages as requested.

### 4) Optimize and export

- Compress PDF when size reduction is requested.
- Export pages to images when visual review is needed.
- Prefer lossless/low-loss settings first; increase compression only if required.

## Operational Rules

- Never overwrite the only copy unless explicitly requested.
- Use clear output names, e.g. `report.merged.pdf`, `report.pages-1-5.pdf`.
- If a required tool is missing, state what is missing and propose the best available fallback.
- If a PDF is encrypted and no password is provided, stop and request password/user confirmation.
- For ambiguous requests (e.g., “organize this PDF”), ask one short clarification before editing.

## Scripts

Use `scripts/pdf_ops.py` for deterministic operations.

Examples:
- Show metadata/page count:
  - `python3 scripts/pdf_ops.py info input.pdf`
- Merge files:
  - `python3 scripts/pdf_ops.py merge a.pdf b.pdf -o merged.pdf`
- Split/select pages:
  - `python3 scripts/pdf_ops.py split input.pdf --pages 1-3,5 -o part.pdf`
- Rotate all pages:
  - `python3 scripts/pdf_ops.py rotate input.pdf --angle 90 -o rotated.pdf`
- Rotate specific pages:
  - `python3 scripts/pdf_ops.py rotate input.pdf --angle 180 --pages 2,4-6 -o rotated.pdf`
- Extract text:
  - `python3 scripts/pdf_ops.py extract-text input.pdf -o output.txt --with-page-markers`

If `pypdf` is missing, install with:
- `python3 -m pip install pypdf`

## Output Format

Return:
- What was done (1-3 bullets)
- Output file path(s)
- Any caveat (quality loss, skipped pages, encryption limits)
- Optional next step (e.g., OCR, stronger compression, page cleanup)
