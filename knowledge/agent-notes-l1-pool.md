# Agent-notes L1 pool (load on demand)

Секции, вынесенные из горячего контекста. **Не включать в default hot.** Загружать по запросу: `route_context(query)` или чтение этого файла.

## Секции в L1

- **HPMOR:** hpmor-l1-pool-v1 — эпистемические эвристики из ГПиМРМ (подгрузка: route_context('HPMOR'|'epistemic heuristics') или ревизии при необходимости).
- **IT:** it-source-mini-index-v1 — мини-индекс источников (CLRS, DDIA, PostgreSQL, SRE и т.д.).
- **Knowledge:** knowledge-index-v1 — полный список playbook/status/kb (router, runbook, IT, Git, KE, Psychology, Aviation, Engineering (Evidence), Medicine, **Regex (MRE3-кластер: `worlds/pattern-regex/index-knowledge-regex-cluster-v1.md`, `worlds/pattern-regex/kb-regex-*`)** и др.). Навигация: index-knowledge-router-v1.md.
- **Sysadmin:** `domain-index-v1.md` и `tool-purpose-and-books-v1.md` в корне `knowledge/`; все playbook/kb из таблицы domain-index — там же. При запросах по мониторингу, дашбордам, сетям, 1С, nginx, … — загружать domain-index, затем соответствующий playbook и kb.
- **IMC:** imc-ui-ux-vision-v1 — видение UI/UX портала IMC (ModellingCore).
- **CascadeIDE / Avalonia+Dock:** при задачах UI/XAML/Dock в desktop IDE — `route_context('Avalonia'|'Dock'|'CascadeIDE UI')` или цепочка `worlds/software-dotnet-desktop/status-avalonia-cascade-ide-ui-v1` → `worlds/software-dotnet-desktop/playbook-avalonia-dock-ui-v1` → `worlds/software-dotnet-desktop/kb-avalonia-ui-dock-fundamentals-v1` (см. `index-knowledge-router-v1.md`, `router-avalonia-ui`).
- **Psychology:** `psychology-gender-studies-subdomain-v1` — Gender Studies / Identity & Context; полный текст в `knowledge/worlds/psychology-models/psychology-gender-studies-subdomain-v1.md` (в agent-notes — stub).
- **World-life:** world-human-system-v1, world-human-system-playbook-v1 — мир «Человек как система», playbook по конфликтам языка/ролей.

## Восстановление полного содержимого

Полное содержимое секций до выноса хранится в ревизиях agent-notes (`.cascade-ide/.revisions` или аналог в каноническом репо) и/или в указанных `knowledge/*.md`. При необходимости восстановить или дополнить pool — взять из ревизии или из файла в `knowledge/`.

Версия: v1.1. 2026-04-05.