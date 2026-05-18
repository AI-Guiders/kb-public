# Project card: `<project-id>` (template)

**Путь экземпляра:** `knowledge/work/projects/<scope>/<project-id>/README.md`  
**scope:** `door-to-singularity` | `portal` | `harvester` | `imc` | …  
**project-id:** стабильный slug (`cascade-ide`, `edw-portal`, …)

---

## Identity

- **project-id:**
- **scope:**
- **Workspace path(s):** (без секретов в org; в personal — реальные пути)
- **Repository / plan / issue:** (ссылки)

## Purpose

(1–2 предложения: что за продукт или трек.)

## Motivation

(Зачем ведётся работа.)

## Vision

(Куда клонит развитие — без обещаний сроков.)

## Scope

(Что входит в ответственность этого трека.)

## Non-goals

(Что сознательно не делаем; соседние project-id.)

## Для агента

- Типичные ошибки (не смешивать с …)
- Обязательные пути / ADR / MCP
- `[PRIMARY:<project-id>]` при работе в чате (опционально)

## Технический контракт (репо)

- `TargetFramework`, `LangVersion`, nullable, UI/runtime
- Источник истины: `*.csproj` / `Directory.Build.props`
- Универсальные нормы: `worlds/software-authoring/code-writing-principles-v1.md`

## Links

- Хаб scope: `work/projects/<scope>/<scope>/README.md` (если есть)
- Domain KB: `status-*` → `playbook-*` → `kb-*` (роутер)