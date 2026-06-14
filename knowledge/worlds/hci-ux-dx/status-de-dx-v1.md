# Developer Experience (DE/DX) Domain Status v1

## Scope

Эргономика разработки и поставки: скорость безопасной доставки, онбординг, трение среды, обратная связь от тулинга и тестов, метрики потока (lead time, cycle time, time-to-first-X). Не путать с **HCI** (качество конкретного интерфейса и диалога) — DX шире: процесс, инструменты, договорённости команды; пересечение с HCI и UI/UX — по запросу.

## Completion State

Status: **Done v1** (playbook + индекс)

Completed artifacts:

- `de-dx-playbook.md` — операционные принципы и метрики
- `kb-ide-dx-literature-evidence-v1.md` — литературный синтез по DX/IDE (Osmani, Smalltalk-80, Boxer); канон для работы над инструментом и Cascade IDE
- `kb-ui-ux-literature-evidence-v1.md` — литературный синтез UI/UX (Norman, Nielsen, Shneiderman, Krug); см. также домен HCI
- Строка в `index-knowledge-router-v1.md` (Domain Entry Map + секция router-de-dx)

## Definition of Done Check

- Единый playbook для DX-запросов: done.
- Роутер знает домен по имени (Developer Experience / DE/DX): done.
- Связи с Git, PR review, tooling, HCI/UI задокументированы в индексе: done.

## Active Guardrails

- Сначала снять трение (easy path = correct path), потом наращивать процесс.
- Метрики — для решений, не для ритуала; при росте cycle time без гипотезы — стоп и разбор.
- Продуктовые **acceptance**-критерии (latency, time-to-first-edit и т.д.) — в ADR/доках конкретного приложения; KB даёт общий слой `de-dx-playbook.md`, не дублирует каждый продукт.

## Related domains

| Тема | Куда |
|------|------|
| Цикл Git / ветки / recovery | Git (`playbook-git-workflow-v1.md`) |
| Ревью и риск merge | PR Review |
| Сборка, тесты, отладка | `tooling-debug-playbook.md` |
| Интерфейс и когнитивная нагрузка | HCI, `ui-ux-playbook.md`, `kb-ui-ux-literature-evidence-v1.md` |
| Принципы IDE / интегрированной среды (литература) | `kb-ide-dx-literature-evidence-v1.md` |
| Desktop IDE (Avalonia Cascade) | домен Avalonia UI в роутере; продуктовые метрики — в ADR репозитория приложения |

