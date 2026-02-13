#!/usr/bin/env python3
from __future__ import annotations
import argparse

p = argparse.ArgumentParser(description="Build Basecamp-style status update")
p.add_argument("--project", required=True)
p.add_argument("--mode", choices=["daily", "weekly", "retro"], default="daily")
p.add_argument("--done", action="append", default=[])
p.add_argument("--next", action="append", default=[])
p.add_argument("--blockers", action="append", default=[])
a = p.parse_args()

print(f"Projeto: {a.project}")
print(f"Modo: {a.mode}\n")

if a.mode in ("daily", "weekly"):
    print("✅ Concluído:")
    for i in (a.done or ["(sem itens)"]):
        print(f"- {i}")
    print("\n➡️ Próximos passos:")
    for i in (a.next or ["(sem itens)"]):
        print(f"- {i}")
    print("\n⚠️ Bloqueadores:")
    for i in (a.blockers or ["(sem bloqueadores)"]):
        print(f"- {i}")
else:
    print("✅ O que funcionou bem:")
    for i in (a.done or ["(sem itens)"]):
        print(f"- {i}")
    print("\n⚠️ O que não funcionou:")
    for i in (a.blockers or ["(sem itens)"]):
        print(f"- {i}")
    print("\n➡️ Ações da próxima iteração:")
    for i in (a.next or ["(sem itens)"]):
        print(f"- [ ] {i} | owner | prazo")
