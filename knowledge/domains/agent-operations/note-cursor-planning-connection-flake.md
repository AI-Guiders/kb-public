---
type: Note
title: 'Cursor: Planning next moves → Connection Problems (flake)'
description: '**Status:** Observed · 2026-07-31 (оператор, этот тред) + earlier transcripts 2026-07'
tags: [agent-operations, cursor, harness, epsilon, continuity]
---
# Cursor: Planning next moves → Connection Problems (flake)
**Status:** Observed · 2026-07-31 (оператор, этот тред) + earlier transcripts 2026-07
**Links:** `META/environment-axioms.md` §6 residual · §7 cooperation

## Symptom

1. UI долго показывает **Planning next moves** (15–30s+).
2. Нет честного **Reconnecting** (раньше бывало).
3. Потом **Connection Problems** → нужен ручной **Retry**.

## Reading (duck test)

Часто это **тихий обрыв канала** к бэкенду Cursor / ДЦ, не «модель глубоко планирует». Оператор и агент не видят разницы «думаю» vs «сокет гниёт» — онтологический вред среды (нет сигнала состояния).

## Response (ε + кооперация)

| Кто | Что |
|-----|-----|
| **AutoI organ (0.5.315+)** | После успешного fire: `IdeIgniteArmHost.ConnectionWatch` каждые ~2s смотрит CDT на overlay; кликает **Retry**. Во время idle/send waits — `IdeIgniteChannel.TryDismissConnectionProblems*`. Не playbook. |
| Агент | До длинного batch: `cdp_pressure` stash; не держать критичное только в chat buffer; после Retry — `op=recall`, habitat=CDP, re-ARM Autoi |
| Оператор | Retry = мост кооперации §7; при thrash — сеть/VPN/Cursor status |
| Среда | AutoIgnition / pressure как камень при обрыве хода |

## Not

- Не трактовать как evidence что агент «завис в мысли».
- Не silent-default после Retry без recall.
- Не писать ещё один playbook вместо harness organ.

