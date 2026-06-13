# Playbook: engineering.cad — operational v1

## Purpose

Контракт **совместной работы** человека и агента по CAD: что грузить, чего не тащить в контекст, как стыковать с .NET и локальным mono-repo плагинов.

## Scope

- In scope: выбор kb, конфигурации сборки, объяснение API-контуров, типовые структуры repo.
- Out of scope: проектные данные заказчика, внутренние пароли/SQL, юридические лицензии вендоров.

## When to open

- Вопрос про САПР, managed-плагины, multi-CAD repo, сборку addin.
- Сборка: DLL, конфиг, x86.
- Правки `.csproj` с множеством конфигураций.

## Core contract

1. **Порядок:** `status-engineering-cad-v1` → этот playbook → `kb-cad-*-fundamentals` → при необходимости `software-dotnet-csharp`.
2. **Только предметка из этого мира** — платформы, API-модели, references; не подменять vendor help.
3. ConnStr, FQDN, внутренние wiki, пути clone на диске — **не** в ответах из kb (локально у команды).
4. **Roslyn MCP** — после выбора проекта/конфигурации в **открытом** repo пользователя.
5. Полный API — документация вендора; fundamentals — каркас.

## Practical order («не собирается»)

1. САПР + конфигурация (`Release_E3D310`, …).
2. `kb-cad-build-references-fundamentals-v1.md`.
3. csproj: HintPath, `PlatformTarget`, defines.
4. При необходимости — platforms + extension models fundamentals.

## Links

- [playbook-engineering-cad-v1.md](playbook-engineering-cad-v1.md)
- [map-engineering-cad-reading-v1.md](map-engineering-cad-reading-v1.md)

**Версия:** v1.3 · 2026-06-04 (публичный слой без work/ и workspace scope)