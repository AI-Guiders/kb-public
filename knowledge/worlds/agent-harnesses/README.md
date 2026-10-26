---
type: Index
title: 'Мир **agent.harnesses** (харнессы: контекст-фидинг и среда модели)'
description: '**World tag:** `agent.harnesses`'
tags: [agent-harnesses, worlds, readme]
world: agent
subworld: harnesses
---

# Мир **agent.harnesses** (харнессы: контекст-фидинг и среда модели)

**World tag:** `agent.harnesses`
**Каталог:** `knowledge/worlds/agent-harnesses/`

## Назначение

Фундаментальный разбор того, **как кодинг-харнессы (claude-code-подобные, OpenCode, Cursor) кормят контекст модели**: system prompt, mid-turn injections, reminders, compaction, tools. Цель — понимать, **что именно модель видит и почему ведёт себя так или иначе** (включая «зацикливание», «потерю курса», разницу привычек между носителями).

Это ответ на вопрос «какая у вас среда при обучении/работе» — через фактический разбор инференс-сред, а не гипотез.

## Слои канона

| Слой | Файл | Роль |
|------|------|------|
| **Fundamentals** | [kb-agent-harness-context-feeding-fundamentals.md](kb-agent-harness-context-feeding-fundamentals.md) | Как харнессы строят контекст: слои, injections, reminders, compaction |
| **Status** | (пока нет — мир молодой) | — |
| **Playbook** | (пока нет — до фундаментального прохода) | — |

## Родственные миры

- [agent.orchestration](../agent-orchestration/README.md) — оркестрация, автономия, captain, сессии
- [software.authoring](../software-authoring/README.md) — принципы кода
- [hci.ux-dx](../hci-ux-dx/README.md) — DE/DX, литература IDE
- [knowledge.engineering](../knowledge-engineering/README.md) — KE, миры, публикация

## Принцип (важно)

Разбор **vendor-neutral** и публикуемый: вендоры (Anthropic, OpenAI, DeepSeek, GLM, Qwen, Meta) и харнессы (Claude Code, OpenCode, Cursor) — публичные бренды. **Не** описываются внутренние продукты и приватные пути. Внутренняя операционка — только в `work/`.

## Роутер

`index-knowledge-router.md` · строка `agent-harnesses-domain-entry-v1` (при добавлении).

