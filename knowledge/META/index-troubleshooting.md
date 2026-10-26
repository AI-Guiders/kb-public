---
type: Index
title: Индекс troubleshooting в KB
description: '**Статус:** living index · 2026-05-20 (консолидация по мирам)'
tags: [meta]
---
# Индекс troubleshooting в KB


**Статус:** living index · 2026-05-20 (консолидация по мирам)  
**Процесс:** [`playbook-troubleshooting-collection.md`](playbook-troubleshooting-collection.md)  
**Шаблон папки:** [`templates/worlds/template-world-troubleshooting-readme.md`](../templates/worlds/template-world-troubleshooting-readme.md)

---

## Два контура

| Слой | Путь | kb-public |
|------|------|-----------|
| **A** | `worlds/<world>/troubleshooting/` | Да |
| **B** | `work/projects/<scope>/` | Нет |

**Правило:** в каждом зрелом мире — каталог **`troubleshooting/`** с `README.md` + `playbook-<world>-troubleshooting.md`. Операционные `playbook-*` в корне мира — процесс; § «Диагностика» → ссылка в `troubleshooting/`.

---

## Реестр миров (слой A)

| Мир / каталог | Troubleshooting playbook |
|---------------|-------------------------|
| `software-authoring` | [`playbook-software-authoring-troubleshooting.md`](../worlds/software-authoring/troubleshooting/playbook-software-authoring-troubleshooting.md) |
| `software-dotnet-avalonia` | [`playbook-avalonia-ui-troubleshooting.md`](../worlds/software-dotnet-avalonia/troubleshooting/playbook-avalonia-ui-troubleshooting.md) |
| `software-dotnet-tooling-roslyn` | [`playbook-dotnet-roslyn-troubleshooting.md`](../worlds/software-dotnet-tooling-roslyn/troubleshooting/playbook-dotnet-roslyn-troubleshooting.md) |
| `software-dotnet-csharp` | [`playbook-dotnet-csharp-troubleshooting.md`](../worlds/software-dotnet-csharp/troubleshooting/playbook-dotnet-csharp-troubleshooting.md) |
| `hci-ux-dx` | [`playbook-tooling-debug-troubleshooting.md`](../worlds/hci-ux-dx/troubleshooting/playbook-tooling-debug-troubleshooting.md) |
| `collaboration-git-pr` | [`playbook-git-pr-troubleshooting.md`](../worlds/collaboration-git-pr/troubleshooting/playbook-git-pr-troubleshooting.md) |
| `ops-network-admin` | [`playbook-ops-network-admin-troubleshooting.md`](../worlds/ops-network-admin/troubleshooting/playbook-ops-network-admin-troubleshooting.md) |
| `ops-observability-network` | [`playbook-ops-observability-network-troubleshooting.md`](../worlds/ops-observability-network/troubleshooting/playbook-ops-observability-network-troubleshooting.md) |
| `ops-reliability` | [`playbook-ops-reliability-troubleshooting.md`](../worlds/ops-reliability/troubleshooting/playbook-ops-reliability-troubleshooting.md) |
| `knowledge-engineering` | [`playbook-knowledge-engineering-mcp-troubleshooting.md`](../worlds/knowledge-engineering/troubleshooting/playbook-knowledge-engineering-mcp-troubleshooting.md) |
| `world-life` | [`playbook-world-life-troubleshooting.md`](../worlds/world-life/troubleshooting/playbook-world-life-troubleshooting.md) |
| `software-php-laravel` | [`playbook-php-laravel-troubleshooting.md`](../worlds/software-php-laravel/troubleshooting/playbook-php-laravel-troubleshooting.md) |
| `cognition-human-perception` | [`playbook-cognition-perception-troubleshooting.md`](../worlds/cognition-human-perception/troubleshooting/playbook-cognition-perception-troubleshooting.md) |
| `systems-it` | [`playbook-systems-it-troubleshooting.md`](../worlds/systems-it/troubleshooting/playbook-systems-it-troubleshooting.md) (роутер) |

**Легаси:** корень [`tooling-debug-playbook.md`](../tooling-debug-playbook.md) → hci `troubleshooting/`.  
**Матрица (не отдельная папка):** [`matrix-software-cross-domain-transfer.md`](../worlds/software-authoring/matrix-software-cross-domain-transfer.md) — дублирует fast router в `software-authoring/troubleshooting/`.

---

## Слой B (product) — только полный канон

**Не kb-public** (префикс `work/` в `public-kb.ignore`). В публичном срезе — только слой A; product playbooks живут в репозитории **agent-notes** целиком: `work/troubleshooting/README.md` → `work/projects/<scope>/<project-id>/playbook-*-troubleshooting.md`.

В `worlds/` **нет** product troubleshooting — при `[PRIMARY:…]` в полном каноне: сначала A, затем реестр work.

---

## Маршрутизация агента

1. Есть `[PRIMARY]` / `project-id` и симптом **специфичен продукту** → контур B в **полном каноне** (`work/troubleshooting/README.md` → playbook в `work/projects/…`)
2. Иначе → `worlds/…/troubleshooting/playbook-…` (этот индекс § A; kb-public)
3. Software неявный → `software-authoring/troubleshooting/`
4. Sysadmin → `domain-index.md` → ops `troubleshooting/`
5. Роутер: `router-troubleshooting-index` (supplement, kb-public). Product layout — `section_id` `router-cascade-ide-layout-troubleshooting` в `work/projects/door-to-singularity/cascade-ide/router-cascade-ide-layout-troubleshooting.md`

---

## Backlog

- [ ] `pattern-regex/troubleshooting/` при росте симптомов engines
- [ ] `aviation-human-factors/troubleshooting/` (метафора vs product layout)
- [ ] systems-it: facet playbooks по digest IT Knowledge Expansion

---

## Provenance

layer: meta / index · consolidation 2026-05

