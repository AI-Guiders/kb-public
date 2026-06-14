# Scope contour map (template)

**Назначение:** white-label карта «личный scope → каталог в group KB» для org, где maintainer ведёт **personal** канон с **своими** именами `work/projects/<scope>/`, а участники читают **group** clone с **нейтральными** префиксами.

**Экземпляр maintainer'а** (конкретные строки): `knowledge/work/org/scope-contour-map-v1.md` — **не** в kb-public (`work/` режется); каталог `work/org/` копируется в **group KB** при `seed-org-kb.ps1`.

**Механика в контурах:** [`domains/agent-operations/map-kb-three-contours-v1.md`](../../domains/agent-operations/map-kb-three-contours-v1.md) § «Scope contour map».

---

## Не путать с другими картами

| Карта | Где | Вопрос |
|-------|-----|--------|
| `workspace-scope-map-v1` | personal `work/local/` | `путь на диске` → **slice** (`<personal-scope>`) |
| `scope-alias-map-v1` | personal `work/local/` | короткий токен → **тот же** slice |
| **Scope contour map** (этот шаблон) | `work/org/` → group | personal **scope** → **имя каталога в group** + label |

---

## Файл экземпляра (maintainer)

**Путь:** `knowledge/work/org/scope-contour-map-v1.md` (каталог **`work/org/`** — см. [`work/org/README.md`](../../work/org/README.md)).

**Формат таблицы** (заполнить и поддерживать):

| Personal scope (канон) | Group KB каталог | Label (для людей) | В group KB? |
|------------------------|------------------|-------------------|-------------|
| `<personal-scope-1>` | `<group-scope-dir-1>` | кратко: что за контур (продукты org, open stack, …) | да |
| `<personal-scope-2>` | — | (почему не в org) | нет (`group-kb.ignore`) |

**Правила заполнения:**

1. **Personal scope** — как в `work/projects/<scope>/` и в MCP `active_scope` (личный канон).
2. **Group KB каталог** — верхний префикс под `work/projects/` в **group**-репо после seed (может отличаться от personal).
3. **Label** — 3–8 слов для onboarding; без внутренних шуток и имён дисков.
4. **В group KB?** — `да` / `нет`; «нет» = scope в `knowledge/group-kb.ignore` или не экспортируется.

---

## Правила поведения (норма)

1. **`project-id` не обязан = scope-каталог.** Допустимо: `work/projects/<group-scope-dir>/<hub-project-id>/README.md` при seed-rename только **верхнего** префикса.
2. **`seed-org-kb.ps1`** — копирует `work/projects/` с фильтром `group-kb.ignore`; опционально **переименование** первого сегмента пути по этой таблице (реализация в скрипте maintainer'а).
3. **PR в group** — пути как в **group**-клоне (`<group-scope-dir>/`), не personal slug.
4. **Импорт org → personal** — вручную; обратный mapping по таблице.
5. **MCP:** `active_scope` и primary paths — **personal**; `knowledge_root_id=group` — пути из **group**-таблицы, не угадывать personal prefix.

---

## Чеклист maintainer (перед seed)

- [ ] Таблица заполнена для всех scope, уходящих в group
- [ ] `group-kb.ignore` согласован с колонкой «В group KB?»
- [ ] Санитизация карточек: [`work/org/checklist-sanitize-paths-for-org-v1.md`](../../work/org/checklist-sanitize-paths-for-org-v1.md) (в group после seed; в kb-public не копируется)
- [ ] Если rename при seed — smoke: один файл под `work/projects/<group-scope-dir>/…`

---

## Related

- [`template-project-card-v1.md`](template-project-card-v1.md)
- [`work/projects/README.md`](../../work/projects/README.md) (в каноне)
- [`playbook-org-kb-white-label-v1.md`](../../domains/agent-operations/playbook-org-kb-white-label-v1.md)

