---
name: atualizador-automatico
description: Plan and run safe automatic update routines for services and host packages with pre-checks, maintenance windows, rollback notes, and post-update verification. Use when asked to set up periodic update checks, automate update workflows, or standardize update safety steps.
---

# Atualizador Automático

Automatize updates com segurança e previsibilidade.

## Fluxo rápido

1. Definir alvo (sistema, app, dependências).
2. Rodar pré-checks (backup/snapshot, espaço, health).
3. Aplicar update em janela planejada.
4. Validar pós-update (serviço, versão, logs).
5. Registrar resultado e plano de rollback.

## Regras operacionais

- Nunca atualizar em massa sem backup/snapshot.
- Priorizar update em janela de manutenção.
- Definir critério de rollback antes da execução.
- Reportar versões antes/depois e impacto observado.

## Scripts

Use `scripts/update_plan.py` para gerar plano padrão de atualização.

Exemplo:
- `python3 scripts/update_plan.py --target openclaw --window "domingo 03:00" --rollback snapshot`
