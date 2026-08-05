**Tags:** #engineering-pml #living #playbook #worlds

﻿# Playbook: engineering.pml v1

## Purpose

Маршрутизация **доменных** вопросов по PML: какой `kb-*` открыть. Не заменяет vendor manual и не описывает репозитории команды.

## Scope

- In scope: PML1/PML2, объекты, выражения, pmllib, runtime в E3D.
- Out of scope: пути clone, генератор каталога, Notepad++/LSP CI — `work/projects/…`; .NET addins — `engineering.cad`.

## When to open

- Синтаксис `!!` / `!`, `define function`, `define object`.
- «PML1 или PML2?», `VAR` vs `!x = …`, наследование (нет).
- `pml reload`, trace, формы, `pml.index`.

## When not to open

- Сборка/публикация HTML-каталога pmllib → operational project card.
- Managed CAD plugin → `engineering.cad`.

## Core contract

1. **Порядок:** `status-engineering-pml-v1` → этот playbook → **один** targeted `kb-*` (см. map).
2. **Не** грузить все kb сразу — `map-engineering-pml-reading-v1.md`.
3. Полный API объектов AVEVA — vendor help; kb — каркас и anti-patterns.

## Routing

| Вопрос | Сначала | Потом |
|--------|---------|--------|
| Язык, типы, объекты, нет inheritance | `kb-pml-fundamentals-v1.md` | `kb-pml-evidence-v1.md` |
| Directives, trace, show/kill формы | `kb-pml-runtime-fundamentals-v1.md` | evidence (Directives) |
| Расширения `.pmlfnc` / `.pmlobj` / `pml.index` | fundamentals §4 | runtime §3 |
| Спор / цитата | `kb-pml-evidence-v1.md` | vendor URL |
| Каталог символов, docs zip, LSP | `work/projects/sscad/pmllib/README.md` | fundamentals §3 (модель типов) |
| .NET addin | `engineering.cad` | vendor |

## Links

- [map-engineering-pml-reading-v1.md](map-engineering-pml-reading-v1.md)
- [status-engineering-pml-v1.md](status-engineering-pml-v1.md)

**Версия:** v1.1 · 2026-06-16
