#!/usr/bin/env python3
import argparse, json
p=argparse.ArgumentParser(); p.add_argument("--url", required=True); p.add_argument("--method", default="GET"); a=p.parse_args()
print(json.dumps({"url": a.url, "method": a.method, "headers": {"Authorization": "Bearer <TOKEN>"}, "retry": {"enabled": True, "maxAttempts": 3}}, indent=2))
