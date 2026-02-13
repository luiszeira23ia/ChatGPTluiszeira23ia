#!/usr/bin/env python3
from pathlib import Path
import argparse, shutil
p=argparse.ArgumentParser(); p.add_argument("src"); a=p.parse_args()
src=Path(a.src)
for f in src.iterdir():
    if f.is_file() and f.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
        d=src/("raw" if "raw" in f.name.lower() else "processed")
        d.mkdir(exist_ok=True)
        shutil.move(str(f), str(d/f.name))
        print(f"{f.name} -> {d.name}")
