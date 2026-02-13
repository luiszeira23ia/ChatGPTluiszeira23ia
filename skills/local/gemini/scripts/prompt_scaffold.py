#!/usr/bin/env python3
from __future__ import annotations

import argparse


def main() -> int:
    p = argparse.ArgumentParser(description="Build a Gemini prompt scaffold")
    p.add_argument("--task", required=True)
    p.add_argument("--format", default="markdown")
    p.add_argument("--tone", default="neutro")
    args = p.parse_args()

    prompt = f"""Você é um assistente especialista.
Tarefa: {args.task}
Tom: {args.tone}
Formato de saída: {args.format}
Regras:
- Seja claro e direto.
- Liste suposições quando necessário.
- Se houver incerteza, sinalize.
"""
    print(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
