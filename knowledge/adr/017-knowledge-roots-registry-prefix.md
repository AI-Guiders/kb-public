# ADR 017: Knowledge-roots registry — префиксы (не каталог всех файлов group)
**Tags:** #adr


**Статус:** Accepted · **2026-05-19** · Core **2.1.2**  
**Реализация (код):** репозиторий **AIGuiders.AgentNotes.Core** / `agent-notes-core` — `docs/adr/016-knowledge-roots-registry-prefix.md` (полный текст)  
**Расширяет:** [013](013-agent-notes-mcp-local-settings-toml.md); agent-notes-mcp ADR 015 (`docs/adr/015-multi-root-read-only-knowledge-routing.md`)  
**Связано:** [011](011-aiguiders-org-collaborative-kb-repo.md), `work/org/scope-contour-map.md`, [008](008-workspace-scope-map-hot-mcp-and-public-cut.md)

---

## Суть (одним абзацем)

**Читать** из group KB можно **любой** файл — TOML уже монтирует весь clone. Файл `work/local/knowledge-roots-index.md` нужен **не для доступа**, а чтобы `route_context` подсказал агенту: «это в group, вот preview». Перечислять каждую карточку `work/projects/.../README.md` **не надо**. Вместо этого — **2–5 строк**: smoke, префикс `work/org/`, префикс `work/projects/<group-scope-dir>/`. Имена scope-каталогов — в **`work/org/scope-contour-map.md`**, не в roots-index.

---

## Три механизма (не путать)

```text
TOML [[knowledge.read_only]] id=group
  → read_knowledge_file(любой/путь, knowledge_root_id=group)

work/org/scope-contour-map.md
  → таблица: personal scope slug  ↔  group catalog dir

work/local/knowledge-roots-index.md
  → якоря для route_context (exact file или prefix/)
```

---

## Формат индекса (после внедрения Core 2.1.2)

```text
group/smoke-test.md => group
work/org/ => group
work/projects/aiguiders-open/ => group
```

- Строка **без** `/` в конце пути — один файл.  
- Строка **с** `/` в конце — весь подкаталог (префикс).  
- Комментарии `#` — для человека; соглашения дублируются в hot `knowledge-roots-routing-v1`.

Полная спецификация и план кода — **ADR 016** в репозитории AgentNotes.Core (ссылка выше).

---

## Что меняется в KB (после accept)

| Артефакт | Изменение |
|----------|-----------|
| `work/local/README.md` | «реестр = подсказки route_context», не whitelist |
| `templates/newcomer/template-clean-setup-knowledge-roots-index.md` | примеры с `/` |
| `agent-notes.md` § `knowledge-roots-routing-v1` | одна строка: open stack в group → `work/projects/<group-scope-dir>/` |
| Личный `knowledge-roots-index.md` | убрать per-file `work/org/scope-contour...`; оставить префиксы |

---

## Не в scope

- Авто-подстановка `knowledge_root_id` в тулах без явного параметра.
- Замена scope-contour-map префиксами в roots-index.

