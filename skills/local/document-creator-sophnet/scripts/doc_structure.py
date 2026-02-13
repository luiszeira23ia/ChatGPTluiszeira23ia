#!/usr/bin/env python3
import argparse
p=argparse.ArgumentParser(); p.add_argument('--type', default='report'); a=p.parse_args()
print(f"Document type: {a.type}\n1) Objetivo\n2) Contexto\n3) Conteúdo\n4) Riscos\n5) Próximos passos")
