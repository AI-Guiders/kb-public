# ADR in KB
**Tags:** #adr #readme


Этот каталог хранит архитектурные решения для самого KB и его операционного контура.

## Scope

- Что относится к устройству KB (структура, маршрутизация, дистрибуция, уровни).
- Как KB взаимодействует с потребителями (например, CIDE).
- Правила эволюции канона (форматы, governance, совместимость).

## Naming

- Формат файла: `NNN-short-title.md`
- `NNN` — 3-значный номер (`001`, `002`, ...)
- `short-title` — краткий slug в kebab-case

## Minimal template

- `# ADR NNN: Title`
- `Статус` / `Дата`
- `Supersedes` / `Extended by` (по возможности)
- `Контекст`
- `Решение`
- `Последствия`
- `План внедрения` (если нужен)

## Notes

- ADR здесь не заменяют `status-*` и `playbook-*`; они фиксируют архитектурные развилки.
- **Один ADR — одно решение.** Мотивация из чатов, work, outreach, дисклеймеры — в `operator-notes/` или project note со ссылкой из ADR, не внутри тела ADR.
- Для ссылок из роутера можно использовать краткую отсылку в `index-knowledge-router.md` при необходимости.

## Timeline (restored from commit history)

- `001-kb-public-publishing-pipeline.md`
- `002-integrity-post-and-epistemic-baseline.md`
- `003-multi-project-scope-and-project-cards.md`
- `004-router-supplement-and-l1-pool.md`
- `005-kb-base-cide-bundle.md`
- `006-zettelkasten-overlay-for-kb.md`
- `007-kb-project-constitution.md`
- `008-workspace-scope-map-hot-mcp-and-public-cut.md`
- `009-kb-entry-structure-and-pre-open-onboarding.md` (вход, worlds/domains/templates/routers, таксономия)
- `010-kb-markdown-fts-index-boundary.md` (опциональный FTS по Markdown KB; граница с внешним MCP HCI; не часть ANKB по умолчанию)
- `011-aiguiders-org-collaborative-kb-repo.md` (Accepted: org federation SSOT, export/import, bootstrap-only push)
- `012-multi-canon-workspace-resolution.md` (Proposed: primary/secondary canon, `.cursor/agent-notes.toml`, без `knowledge/organization/` в личном)
- `013-agent-notes-mcp-local-settings-toml.md` (Proposed: локальный TOML с MCP **2.0**, `[knowledge]` / `[workspace]` / `[status]`)
- `016-knowledge-stack-clean-setup-protocol.md`
- `017-knowledge-roots-registry-prefix.md` (Accepted: префиксы в `knowledge-roots-index`; Core 2.1.2 — AgentNotes.Core ADR 016)
- `018-ai-guiders-licensing-hub-and-software-grant.md` (Superseded → канон: [AI-Guiders/licensing ADR 001](https://github.com/AI-Guiders/licensing/blob/main/docs/decisions/001-software-grant-mit-and-ethical-layer.md))
- `019-writing-canon-layers-and-guiders-style.md` (Mirror → normative [CDP-ADR-0207](https://github.com/AI-Guiders/cdp-mcp/blob/main/docs/adr/CDP-ADR-0207-writing-canon-layers.md); Vision: GUIDERS-VISION-0002)
- `020-kb-language-contours.md` (Accepted: EN open perimeter, RU personal/work interior; no dual-maintenance i18n)
- `021-federated-app-catalog.md` (Accepted draft: federated trust, unified desktop install journey; FAC / GPLAT/APPCAT)
- `022-kb-graph-substrate.md` (Proposed: KB implicit graph → F# Graph IR, slices, kb-sat, records/views; graph DB optional projection; AgentNotes.Modeling guild)
- `026-okf-canon-migration-and-natural-extension.md` (Proposed: полный переезд KB на OKF v0.2 как канон — one-time миграция; расширение OKF натуральными полями без префикса — `transfer`/`routing`/`contour`/`layer`/`scope` + типы Transfer/Do-Not-Transfer Matrix; hot остаётся runtime-слоем; 023–025 зарезервированы планом ADR 022)

