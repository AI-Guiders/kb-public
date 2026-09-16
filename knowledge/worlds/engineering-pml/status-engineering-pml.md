**Tags:** #engineering-pml #status #worlds

﻿# Status: engineering.pml v1

**Домен:** AVEVA Programmable Macro Language (PML1, PML2), `pmllib`, кастомизация E3D/PDMS.  
**Status:** active
---

## Operating contract (текущий)

| Приоритет | Документ | Когда |
|-----------|----------|--------|
| 1 | `playbook-pml.md` | маршрут по типу вопроса |
| 2 | `kb-pml-fundamentals.md` | язык, объекты, выражения, файлы |
| 3 | `kb-pml-runtime-fundamentals.md` | directives, trace, формы, `pml index` |
| 4 | `kb-pml-evidence.md` | первоисточники AVEVA / training |

**Порядок (роутер):** `status → playbook → kb`. Карта: `map-engineering-pml-reading.md`.

---

## Maintenance Policy

- **Проверено:** 2026-06-16 (AVEVA docs + PDMS PML Manual)
- **Next review triggers:** смена major E3D/PDMS, спор по PML1/PML2 expressions
- **Связь с evidence:** `kb-pml-evidence.md`

---

## Definition of Done (v1)

- [x] Fundamentals языка PML1/PML2
- [x] Fundamentals runtime (directives, trace, forms)
- [x] Явная фиксация: **нет наследования** объектов PML2
- [x] Evidence с официальными URL AVEVA
- [x] Карта чтения + строка Domain Entry Map
- [ ] `kb-pml-forms-gadgets.md` — по задаче UI
- [x] Операционная карточка каталога — `work/projects/sscad/pmllib/README.md` (+ `developer-workspace-setup.md`)

---

## Active Guardrails

- **Не** утверждать ООП-наследование классов PML.
- **Не** смешивать PML1 `VAR` с PML2 typed assignment без предупреждения о типах.
- PML1 expressions **обязательны** в аргументах PDMS-команд и в rule/report — не «всё на PML2».
- Зашифрованный published PML — только использование в E3D, не правка по исходникам.
- Операционка репозитория (пути, build, LSP) — **не** в `worlds/`.

---

## Out of scope (v1)

- Полный справочник всех `!!` объектов AVEVA (vendor Software Customization Reference).
- Семантика UDA/атрибутов MDB.
- PML.NET / addins — `engineering.cad`.

