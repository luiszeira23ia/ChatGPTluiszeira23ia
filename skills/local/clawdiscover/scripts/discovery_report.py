#!/usr/bin/env python3
import argparse, os
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument("path", nargs="?", default="."); a=p.parse_args()
root=Path(a.path)
files=sum(1 for _ in root.rglob('*') if _.is_file())
dirs=sum(1 for _ in root.rglob('*') if _.is_dir())
print(f"Discovery Report\n- Path: {root.resolve()}\n- Files: {files}\n- Dirs: {dirs}")
