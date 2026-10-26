---
type: Template
title: 'Runbook: <title> (template)'
description: '**Назначение:** воспроизводимая процедура (скрипт, деплой, инцидент). Отличие от playbook: **конкретные команды и проверки**.'
tags: [template, templates]
subtype: Runbook
---
# Runbook: <title> (template)

**Назначение:** воспроизводимая процедура (скрипт, деплой, инцидент). Отличие от playbook: **конкретные команды и проверки**.

**Статус:** active · v1.0 · YYYY-MM-DD

---

## Preconditions

- Доступы, ветка, окружение
- **Не** хранить секреты в теле — ссылки на vault / env

## Steps

### 1. …

```powershell
# пример

```

**Expected:** …

### 2. …

## Verification

- [ ] …

## Rollback

- …

## Links

- Playbook (политика): …
- ADR: …

