#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json

SCHEMAS = {
    "tasks": {
        "Title": "title",
        "Status": "select",
        "Priority": "select",
        "Owner": "person",
        "Due": "date",
        "Project": "relation",
    },
    "content": {
        "Title": "title",
        "Stage": "select",
        "Channel": "multi_select",
        "Publish Date": "date",
        "Owner": "person",
    },
    "crm": {
        "Name": "title",
        "Company": "text",
        "Stage": "select",
        "Value": "number",
        "Next Follow-up": "date",
        "Owner": "person",
    },
}


def main() -> int:
    p = argparse.ArgumentParser(description="Generate Notion starter schema")
    p.add_argument("--type", choices=SCHEMAS.keys(), default="tasks")
    args = p.parse_args()
    print(json.dumps(SCHEMAS[args.type], indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
