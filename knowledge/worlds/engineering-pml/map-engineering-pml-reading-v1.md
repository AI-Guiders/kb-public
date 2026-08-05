**Tags:** #engineering-pml #map #worlds

﻿# Карта чтения: engineering.pml (v1)

**Цель:** Fundamentals → Playbook (домен PML; без путей репозитория и CI).

---

## Быстрый маршрут

1. [kb-pml-fundamentals-v1.md](kb-pml-fundamentals-v1.md) — язык: PML1/PML2, объекты, выражения, файлы
2. [kb-pml-runtime-fundamentals-v1.md](kb-pml-runtime-fundamentals-v1.md) — среда E3D: directives, trace, формы, `pml index`
3. [playbook-pml-v1.md](playbook-pml-v1.md) — маршрут по типу вопроса
4. [kb-pml-evidence-v1.md](kb-pml-evidence-v1.md) — первоисточники

---

## По типу вопроса

| Вопрос | Сначала | Потом |
|--------|---------|--------|
| PML1 vs PML2, `VAR`, типы | fundamentals §2–3 | evidence |
| `define object`, нет наследования | fundamentals §3 | evidence §12.1 |
| `pml reload`, trace, `kill` формы | runtime fundamentals | vendor PML Directives |
| Загрузка/show форм | runtime fundamentals §2 | fundamentals §4 (`.pmlfrm`) |
| `.pmlfnc` / `.pmlobj` / `pml.index` | fundamentals §4 | runtime §3 (`pml index`) |
| .NET addin | `engineering.cad` | vendor PML addins |
| Каталог символов, сборка docs, LSP | **вне kb** — `work/projects/sscad/pmllib/` | fundamentals (модель типов) |

---

## Вне мира

- CAD / managed addins → `engineering-cad`
- C# / .NET tooling → `software-dotnet-csharp`, `software-dotnet-tooling-roslyn`
- Пути clone, генератор каталога, Notepad++ plugin — **work/projects/** (операционный слой)

**Версия:** v1.0 · 2026-06-16
