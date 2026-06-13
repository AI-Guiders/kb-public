# Fundamentals: модели расширений CAD (v1)

**Мир:** `engineering.cad`

---

## Scope

Как **типы API** соотносятся с языком, деплоем и отладкой — обобщённо для multi-CAD .NET-плагинов.

---

## Core concepts

### 1) Managed .NET plugin (основной контур)

- **Class library** (DLL), загружаемая хостом САПР.
- Ссылки на interop/API DLL вендора (`HintPath`).
- Конфигурации MSBuild: `Debug_<ProductVer>`, `Release_<ProductVer>` + define (`E3D310`, `ADM19`, `NC26.0`, …).
- Отладка: attach к процессу САПР, подготовка окружения (addins path, env vars).

### 2) ObjectARX (native, AutoCAD)

- C++ проекты, заголовки в `ObjectArx/<year>/inc`.
- Отдельный toolchain, версия ARX **жёстко** привязана к версии AutoCAD.
- Не смешивать с managed без явной границы (mixed mode — редко и сложно).

### 3) AVEVA PML / .NET mix

- **PML** — макросы/скрипты в среде AVEVA.
- **.NET addins** — `Aveva.Core`, UI framework, database filters.
- Константы `AVEVA_CORE_LIBS`, `ADM`, `E3D` в csproj выбирают **набор ссылок**.

### 4) Tekla Open API

- NuGet-пакет с набором `Tekla.Structures.*.dll`.
- Версия пакета ↔ год Tekla (`2020.0.2` ↔ TS 2020).
- Плагины Model / Drawing / Catalog — разные entry points, общие NuGet.

### 5) Self-contained утилиты рядом с плагином

- Иногда отдельный **exe/dll** (например SQL logging) выносится из общей библиотеки, чтобы не тянуть зависимости в основной addin.
- Деплой: набор файлов рядом с addin + опциональный **внешний** config для строки подключения *(не публиковать в KB)*.

---

## Anti-patterns

- Копировать NuGet Tekla в «общий References» без версии — конфликт с другими годами TS.
- Один `AnyCPU` для всех AVEVA addins — многие продукты **x86**.
- Хардкодить секреты в репозиторий вместо локального config-файла в деплое.

---

## Links

- [kb-cad-platforms-fundamentals-v1.md](kb-cad-platforms-fundamentals-v1.md)
- [kb-cad-build-references-fundamentals-v1.md](kb-cad-build-references-fundamentals-v1.md)

**Версия:** v1.0 · 2026-06-04