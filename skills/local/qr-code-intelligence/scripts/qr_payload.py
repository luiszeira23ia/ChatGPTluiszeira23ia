#!/usr/bin/env python3
import argparse
p=argparse.ArgumentParser(); p.add_argument('--data', required=True); a=p.parse_args()
print(f"QR payload: {a.data}")
