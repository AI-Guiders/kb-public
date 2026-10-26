---
type: Maintenance Contract
title: Memory budgets & retrieval contract (v1)
description: 'Перенесено из `KB-V2-CONTRACT.md` (репо agent-notes-mcp) в канон — ADR-026 §5: агент — основной автор и потребитель KB, инструкции мейнтенанса — queryable-знание бандла. Enforcement — MCP; текст — здесь.'
tags: [maintenance-contract, memory, budgets, retrieval, kb, agent-operations]
language: ru
verified:
  - by: human:operator
    at: 2026-10-24
world: agent
subworld: operations
---

# Memory budgets & retrieval contract (v1)

Перенесено из `KB-V2-CONTRACT.md` (репо agent-notes-mcp) в канон — ADR-026 §5: агент — основной автор и потребитель KB, инструкции мейнтенанса — queryable-знание бандла. Enforcement — MCP; текст — здесь.

## Layer boundaries

- **L0 (hot cache):** current goal, next action, blockers, guardrails.
- **L1 (working state):** активные контракты и решения ближнего горизонта.
- **L2 (archive):** исторические батчи, длинные разборы, сырые транскрипты.
- **L3 (router):** status/playbook/matrix входы и порядок загрузки.

## Бюджеты (SLO)

- **L0+L1 soft:** до 6000 символов.
- **L0+L1 hard:** до 12000 символов.
- Выше soft → warning + рекомендация `compact_hot_context`; выше hard → critical, компакция обязательна до глубокой работы.

## Retrieval contract

- Порядок по умолчанию: **status → playbook → matrix → kb**.
- Router грузит сначала только верхнерелевантные секции/концепты.
- Архив — явно и по запросу (без полной гидратации L2).

## Операционные триггеры

- `memory_health`: перед длинными сессиями; после крупных импортов контекста; после восстановления после компакции.
- `route_context`: перед глубокой задачей; при смене scope; при междоменной неоднозначности.
- `compact_hot_context`: при warning/critical от health; перед марафонами релиза/отладки.

## Freshness

- Перепроверять при апдейтах AgentNotes.Core/MCP (числа бюджетов могут меняться; источник чисел — этот контракт, enforcement — `NotesStorage`/`HotContextRouting`).

---

provenance: `agent-notes-mcp/KB-V2-CONTRACT.md` (production memory contract); операторский steer 2026-10-23 «контракты — часть OKF».

