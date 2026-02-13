#!/usr/bin/env python3
from pathlib import Path
import argparse, shutil

MAP = {"images": {".png", ".jpg", ".jpeg", ".webp", ".gif"}, "docs": {".pdf", ".doc", ".docx", ".txt", ".md"}, "archives": {".zip", ".tar", ".gz", ".rar"}}

def bucket(ext):
    e=ext.lower()
    for k,v in MAP.items():
        if e in v: return k
    return "others"

p=argparse.ArgumentParser(); p.add_argument("src"); p.add_argument("--dry-run", action="store_true"); a=p.parse_args()
src=Path(a.src)
for f in src.iterdir():
    if f.is_file():
        d=src/bucket(f.suffix); d.mkdir(exist_ok=True)
        t=d/f.name
        if a.dry_run: print(f"move {f} -> {t}")
        else: shutil.move(str(f), str(t))
