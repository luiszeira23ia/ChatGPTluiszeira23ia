#!/usr/bin/env python3
import argparse
p=argparse.ArgumentParser(); p.add_argument("feature"); a=p.parse_args()
print(f"Feature: {a.feature}\n\nFrontend:\n- UI + estados\n\nBackend:\n- Endpoint/serviço\n\nData:\n- Schema/index\n\nQualidade:\n- Testes + monitoramento")
