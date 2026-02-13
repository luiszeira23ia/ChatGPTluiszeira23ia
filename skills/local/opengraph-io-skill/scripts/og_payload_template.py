#!/usr/bin/env python3
import argparse

p = argparse.ArgumentParser(description="Build OpenGraph.io request template")
p.add_argument("--url", required=True)
p.add_argument("--api-base", default="https://opengraph.io/api/1.1/site")
a = p.parse_args()

print(f"curl '{a.api_base}/{a.url}?app_id=<APP_ID>'")
print("\nExpected fields:")
print("- hybridGraph.title")
print("- hybridGraph.description")
print("- hybridGraph.image")
print("- openGraph.ogTitle / ogDescription / ogImage")
