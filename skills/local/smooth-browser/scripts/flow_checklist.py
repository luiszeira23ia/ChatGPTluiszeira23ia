#!/usr/bin/env python3
import argparse

p=argparse.ArgumentParser(description="Browser automation stability checklist")
p.add_argument("--task", required=True)
a=p.parse_args()

print(f"Task: {a.task}\n")
print("Checklist:")
print("1) Open/focus correct tab")
print("2) Snapshot and confirm target elements")
print("3) Execute one critical action at a time")
print("4) Re-snapshot after each navigation/change")
print("5) Validate expected end state")
print("6) Capture final evidence")
