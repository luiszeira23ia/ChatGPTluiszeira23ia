#!/usr/bin/env python3
import argparse
p=argparse.ArgumentParser(); p.add_argument('--task', required=True); a=p.parse_args()
print(f"Gemini media prompt:\nTask: {a.task}\nInputs: text + media\nOutput: structured summary")
