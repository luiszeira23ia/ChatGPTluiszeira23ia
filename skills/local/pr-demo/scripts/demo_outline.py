#!/usr/bin/env python3
import argparse
p=argparse.ArgumentParser(); p.add_argument('--feature', required=True); a=p.parse_args()
print(f"Demo: {a.feature}\n1) Problem\n2) Solution\n3) Live proof\n4) Impact\n5) CTA")
