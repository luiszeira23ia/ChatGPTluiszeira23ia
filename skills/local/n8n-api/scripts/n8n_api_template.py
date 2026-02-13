#!/usr/bin/env python3
import argparse
p=argparse.ArgumentParser(); p.add_argument("--base", required=True); p.add_argument("--endpoint", required=True); a=p.parse_args()
print(f"curl -H 'X-N8N-API-KEY: <KEY>' '{a.base.rstrip('/')}/{a.endpoint.lstrip('/')}'")
