#!/usr/bin/env python3
import argparse
p=argparse.ArgumentParser(); p.add_argument("--title", required=True); p.add_argument("--type", default="Task"); p.add_argument("--priority", default="Medium"); a=p.parse_args()
print(f"Type: {a.type}\nTitle: {a.title}\nPriority: {a.priority}\n\nDescription:\n- Context\n- Expected behavior\n- Acceptance criteria")
