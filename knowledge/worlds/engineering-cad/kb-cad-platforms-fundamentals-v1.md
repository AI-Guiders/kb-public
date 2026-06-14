# Fundamentals: CAD/BIM платформы в линейке плагинов (v1)

**Мир:** `engineering.cad`  
**Статус:** active · справочно, без привязки к одному заказчику

---

## Scope

Краткие **роли платформ**, с которыми типично работают утилиты и addins в multi-CAD mono-repo: не полные учебники САПР, а **контекст для выбора API и конфигурации сборки**.

---

## Core concepts

### 1) AutoCAD (Autodesk)

- Доминирующая 2D/3D CAD-платформа в AEC.
- Расширения: **ObjectARX** (C++/native, близко к ядру), **.NET API** (managed, типичный путь addins).
- Версии AutoCAD ↔ версии ObjectARX SDK (год в имени SDK: 2018, 2021, …).

### 2) nanoCAD (Nanosoft)

- CAD с .NET API, совместимый по духу с AutoCAD-экосистемой.
- Типичные managed-сборки: `hostmgd.dll`, `hostdbmgd.dll` — **API хоста**.
- Несколько релизов NC на одной машине → отдельные конфигурации сборки (`NC23.1`, `NC26.0`, …).

### 3) AVEVA (PDMS / E3D / Administration / Diagrams / …)

- Инженерный 3D и администрирование в промышленном EPC.
- Продуктовые линии в коде часто кодируются **короткими тегами**: `E3D210`, `E3D310`, `ADM15`, `TAGS151`, `DIAG141`, …
- API: **.NET** (`Aveva.Core.*`, `Aveva.ApplicationFramework.*`), плюс **PML** (скриптовый/макро слой AVEVA) в смежных репо.
- Сборка часто **x86** и привязана к установленному продукту или снимку DLL в `ReferencesAveva`.

### 4) Tekla Structures (Trimble)

- BIM для металлоконструкций и ЖБ.
- Типичный путь расширений: **Tekla Open API** (.NET, NuGet `TeklaOpenAPI`, привязка к году Tekla / `TS2020`).
- Отдельные репозитории: общая библиотека, Model, Drawings, CustomProperties.

### 5) Navisworks Manage (Autodesk)

- Сводка/координация моделей, clash, обзор.
- .NET API для плагинов; references часто рядом с **Autodesk** tree в общем `References`.

### 6) Общие решения вне «одного САПР»

- **OpenXml**, общие shared-библиотеки (document/office), office/document libs — не CAD API, но живут в том же workspace.

---

## Anti-patterns

- Считать все САПР «одним .NET проектом» — у каждого свой **набор конфигураций** и DLL.
- Путать **версию продукта** (E3D 3.1) и **TargetFramework** (net48) — обе должны сходиться в csproj.
- Тянуть API Navisworks в задачу только по Aveva без явной связи.

---

## Relation to tools

- Официальная документация: сайты Autodesk, Nanosoft, AVEVA, Tekla.
- Локальные **vendor DLL** — не замена help; см. [kb-cad-build-references-fundamentals-v1.md](kb-cad-build-references-fundamentals-v1.md).

**Версия:** v1.0 · 2026-06-04
