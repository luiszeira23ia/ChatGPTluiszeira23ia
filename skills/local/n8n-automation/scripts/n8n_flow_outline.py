#!/usr/bin/env python3
import argparse
p=argparse.ArgumentParser(); p.add_argument("--name", required=True); a=p.parse_args()
print(f"Workflow: {a.name}\n1) Trigger\n2) Validate input\n3) Process\n4) Action\n5) Error handler\n6) Notify")
