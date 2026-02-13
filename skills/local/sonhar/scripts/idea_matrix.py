#!/usr/bin/env python3
import argparse
p=argparse.ArgumentParser(); p.add_argument("theme"); a=p.parse_args()
print(f"Tema: {a.theme}\n\nOpções:\n1) Minimalista\n2) Ousada\n3) Premium\n\nCritérios:\n- Clareza\n- Diferenciação\n- Viabilidade")
