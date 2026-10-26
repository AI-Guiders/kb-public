---
type: Note
title: Active scope — резолв slice и карта workspace (развёрнуто, v1)
description: '**Назначение:** полный текст резолва slice и карты workspace. Сам **указатель** (что сейчас в фокусе: primary, открытый workspace, пауза) живёт в **`knowledge/work/local/active-scope.md`** — машинная привязка, в hot/L0 и в kb-public не входит (перенесено 2026-10-17).'
tags: [workspace-context, worlds]
language: ru
world: workspace
subworld: context
---
# Active scope — резолв slice и карта workspace (развёрнуто, v1)


**Назначение:** полный текст резолва slice и карты workspace. Сам **указатель** (что сейчас в фокусе: primary, открытый workspace, пауза) живёт в **`knowledge/work/local/active-scope.md`** — машинная привязка, в hot/L0 и в kb-public не входит (перенесено 2026-10-17).

## Active scope (указатель)

Резолв slice в MCP: аргумент **`active_scope`** → **`knowledge/work/local/workspace-scope-map.md`** (если есть под корнем канона) **или** секция **`workspace-scope-map-v1`** в hot (самый длинный префикс к `workspace_path`) → при отсутствии совпадений — встроенный fallback в **`agent-notes-mcp`** (`ResolveScope`). Полный протокол: **`knowledge/worlds/workspace-context/playbook-multi-project-context.md`** §6c.

Не поддерживать здесь ручной **`current:`** как источник правды: при необходимости легаси-оверрайд всё ещё возможен одной строкой вида `current: <scope-id>`, но предпочтительны карта (файл или секция) и явный параметр вызова.

