# Индекс troubleshooting в KB (v1)

**Статус:** living index · 2026-05-20 (консолидация по мирам)  
**Процесс:** [`playbook-troubleshooting-collection-v1.md`](playbook-troubleshooting-collection-v1.md)  
**Шаблон папки:** [`templates/worlds/template-world-troubleshooting-readme-v1.md`](../templates/worlds/template-world-troubleshooting-readme-v1.md)

---

## Два контура

| Слой | Путь | kb-public |
|------|------|-----------|
| **A** | `worlds/<world>/troubleshooting/` | Да |
| **B** | `work/projects/<scope>/` | Нет |

**Правило:** в каждом зрелом мире — каталог **`troubleshooting/`** с `README.md` + `playbook-<world>-troubleshooting-v1.md`. Операционные `playbook-*` в корне мира — процесс; § «Диагностика» → ссылка в `troubleshooting/`.

---

## Реестр миров (слой A)

| Мир / каталог | Troubleshooting playbook |
|---------------|-------------------------|
| `software-authoring` | [`playbook-software-authoring-troubleshooting-v1.md`](../worlds/software-authoring/troubleshooting/playbook-software-authoring-troubleshooting-v1.md) |
| `software-dotnet-avalonia` | [`playbook-avalonia-ui-troubleshooting-v1.md`](../worlds/software-dotnet-avalonia/troubleshooting/playbook-avalonia-ui-troubleshooting-v1.md) |
| `software-dotnet-tooling-roslyn` | [`playbook-dotnet-roslyn-troubleshooting-v1.md`](../worlds/software-dotnet-tooling-roslyn/troubleshooting/playbook-dotnet-roslyn-troubleshooting-v1.md) |
| `software-dotnet-csharp` | [`playbook-dotnet-csharp-troubleshooting-v1.md`](../worlds/software-dotnet-csharp/troubleshooting/playbook-dotnet-csharp-troubleshooting-v1.md) |
| `hci-ux-dx` | [`playbook-tooling-debug-troubleshooting-v1.md`](../worlds/hci-ux-dx/troubleshooting/playbook-tooling-debug-troubleshooting-v1.md) |
| `collaboration-git-pr` | [`playbook-git-pr-troubleshooting-v1.md`](../worlds/collaboration-git-pr/troubleshooting/playbook-git-pr-troubleshooting-v1.md) |
| `ops-network-admin` | [`playbook-ops-network-admin-troubleshooting-v1.md`](../worlds/ops-network-admin/troubleshooting/playbook-ops-network-admin-troubleshooting-v1.md) |
| `ops-observability-network` | [`playbook-ops-observability-network-troubleshooting-v1.md`](../worlds/ops-observability-network/troubleshooting/playbook-ops-observability-network-troubleshooting-v1.md) |
| `ops-reliability` | [`playbook-ops-reliability-troubleshooting-v1.md`](../worlds/ops-reliability/troubleshooting/playbook-ops-reliability-troubleshooting-v1.md) |
| `knowledge-engineering` | [`playbook-knowledge-engineering-mcp-troubleshooting-v1.md`](../worlds/knowledge-engineering/troubleshooting/playbook-knowledge-engineering-mcp-troubleshooting-v1.md) |
| `world-life` | [`playbook-world-life-troubleshooting-v1.md`](../worlds/world-life/troubleshooting/playbook-world-life-troubleshooting-v1.md) |
| `software-php-laravel` | [`playbook-php-laravel-troubleshooting-v1.md`](../worlds/software-php-laravel/troubleshooting/playbook-php-laravel-troubleshooting-v1.md) |
| `cognition-human-perception` | [`playbook-cognition-perception-troubleshooting-v1.md`](../worlds/cognition-human-perception/troubleshooting/playbook-cognition-perception-troubleshooting-v1.md) |
| `systems-it` | [`playbook-systems-it-troubleshooting-v1.md`](../worlds/systems-it/troubleshooting/playbook-systems-it-troubleshooting-v1.md) (роутер) |

**Легаси:** корень [`tooling-debug-playbook.md`](../tooling-debug-playbook.md) → hci `troubleshooting/`.  
**Матрица (не отдельная папка):** [`matrix-software-cross-domain-transfer-v1.md`](../worlds/software-authoring/matrix-software-cross-domain-transfer-v1.md) — дублирует fast router в `software-authoring/troubleshooting/`.

---

## Слой B (product) — только `work/`

**Реестр и правила:** [`work/troubleshooting/README.md`](../work/troubleshooting/README.md).

| project-id | Playbook |
|------------|----------|
| `cascade-ide` | [`work/projects/door-to-singularity/cascade-ide/playbook-layout-presentation-intercom-troubleshooting-v1.md`](../work/projects/door-to-singularity/cascade-ide/playbook-layout-presentation-intercom-troubleshooting-v1.md) |

В `worlds/` **нет** product troubleshooting — при `[PRIMARY:…]` сначала общий слой A, затем playbook из таблицы work.

---

## Маршрутизация агента

1. Есть `[PRIMARY]` / `project-id` и симптом **специфичен продукту** → [`work/troubleshooting/README.md`](../work/troubleshooting/README.md)
2. Иначе → `worlds/…/troubleshooting/playbook-…` (этот индекс § A)
3. Software неявный → `software-authoring/troubleshooting/`
4. Sysadmin → `domain-index-v1.md` → ops `troubleshooting/`
5. Роутер: `router-troubleshooting-index`; product layout — `router-cascade-ide-layout-troubleshooting` → **только work**

---

## Backlog

- [ ] `pattern-regex/troubleshooting/` при росте симптомов engines
- [ ] `aviation-human-factors/troubleshooting/` (метафора vs product layout)
- [ ] systems-it: facet playbooks по digest IT Knowledge Expansion

---

## Provenance

layer: meta / index · consolidation 2026-05
