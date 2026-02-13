#!/usr/bin/env python3
import argparse
p=argparse.ArgumentParser(); p.add_argument('--topic', required=True); p.add_argument('--duration', type=int, default=30); a=p.parse_args()
print(f"Video prompt\n- Topic: {a.topic}\n- Duration: {a.duration}s\n- Scenes: Hook, Context, Key Message, CTA")
