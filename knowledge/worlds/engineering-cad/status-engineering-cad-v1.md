# Status: engineering.cad v1

**Домен:** плагины и расширения под САПР (CAD/BIM/AEC), преимущественно .NET и смежные native API.  
**Версия:** v1.0 · 2026-06-04 · **status:** active (draft corpus)

---

## Operating contract

| Приоритет | Документ | Когда |
|-----------|----------|--------|
| 1 | `playbook-engineering-cad-v1.md` | выбор поддомена / маршрут |
| 2 | `playbook-engineering-cad-operational-v1.md` | совместная работа человек + агент по CAD |
| 3 | `kb-cad-*-fundamentals-v1.md` | определения, модели API, сборка |
| 4 | `software-dotnet-csharp/kb-dotnet-fundamentals-v1.md` | TFM, runtime, если вопрос чисто .NET |

**Порядок роутера:** `status → playbook → kb` (не начинать с длинного kb без вопроса).

---

## Definition of Done (v1)

- [x] Корневой playbook мира
- [x] Operational playbook
- [x] Три fundamentals (platforms, extension models, build/references)
- [x] Map reading
- [x] Строка в Domain Entry Map
- [ ] Поддомены с отдельными kb (AVEVA-only, Tekla-only) — по мере задач
- [ ] Troubleshooting слой A в `troubleshooting/` — при повторяемых инцидентах сборки

---

## Active Guardrails

- **Не** подмешивать в ответы внутренние FQDN, строки SQL и машинные пути clone — вне этого мира.
- **Не** выдавать vendor SDK за «открытую документацию»: бинарники в References — для сборки; справка — документация вендора / Confluence команды.
- Версия API = **версия продукта САПР** (E3D 2.10, NC 23.1, TS 2020, …), не только TFM.
- Один вопрос — один САПР в фокусе; не смешивать Aveva и Tekla в одной цепочке без явной интеграции.

---

## Maintenance Policy

- **Проверено:** 2026-06-04 — каркас мира по шаблону `templates/worlds/`.
- **Next review:** смена основных версий платформ в команде; появление нового САПР в линейке плагинов.
- **Источники:** обобщение практики .NET CAD-плагинов; официальные docs Autodesk, Nanosoft, AVEVA, Tekla Trimble (вне kb).