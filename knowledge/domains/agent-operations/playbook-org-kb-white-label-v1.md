# Playbook: организационный контур KB (white-label)

**Статус:** active · v1.0 · 2026-05-19  
**Назначение:** как **любой** GitHub-org (не привязан к конкретному бренду) поднять три контура: **personal** · **group KB** · **kb-public** + MCP multi-root.

**Аудитория:** основатель org, **canon-maintainer** (сборка public, seed group), **org-maintainer** (review PR в group).

**Триггеры:** «своя org KB», «white-label», «развернуть kb у команды», `Acme/kb`, «как у kb-public но у нас», «group KB для организации».

**Связано:** [`map-kb-three-contours-v1.md`](map-kb-three-contours-v1.md), [`playbook-knowledge-stack-clean-setup-v1.md`](playbook-knowledge-stack-clean-setup-v1.md) (участник: personal), [`adr/012-multi-canon-workspace-resolution-v1.md`](../adr/012-multi-canon-workspace-resolution-v1.md), MCP ADR 014/015 (в репозитории agent-notes-mcp).

**Пример инстанса (не норма):** org `AI-Guiders`, репозитории `AI-Guiders/kb` и `AI-Guiders/kb-public` — одна реализация; в инструкциях ниже — плейсхолдеры `{ORG_SLUG}`.

---

## Именование (зафиксировать один раз)

| Плейсхолдер | Пример | Репозиторий |
|-------------|--------|-------------|
| `{ORG_SLUG}` | `acme-corp` | GitHub org slug |
| `{REPO_GROUP}` | `acme-corp/kb` | private, командный канон |
| `{REPO_PUBLIC}` | `acme-corp/kb-public` | public, read-only срез |

MCP id **`group`** и **`public`** — **технические**, не меняются при white-label. Пути клонов — в TOML на машине каждого участника.

---

## Стек (что форкают / что пишут сами)

| Компонент | Лицензия / роль | Где живёт |
|-----------|-----------------|-----------|
| **agent-notes-mcp** | MIT (код) | отдельный репо или релиз; `dotnet publish` |
| **KB тексты** | CC BY-SA 4.0 в public/group | git |
| **Скрипты** `build-public-kb.ps1`, `seed-org-kb.ps1`, `push-public-kb.ps1` | в **source canon** maintainer’а | копируются в `{REPO_GROUP}/scripts/` при seed |
| **Личный канон** каждого участника | private | свой `agent-notes` (или fork) |

Участнику **не обязательно** иметь source canon — достаточно `{REPO_PUBLIC}` + clone `{REPO_GROUP}` + свой personal.

---

## Фаза A — репозитории org

1. Создать GitHub org `{ORG_SLUG}`.
2. **`{REPO_GROUP}`** — **private**, LICENSE CC BY-SA 4.0, wiki опционально.
3. **`{REPO_PUBLIC}`** — **public**, тот же LICENSE на тексты.
4. Команды: `{ORG_SLUG}/kb-maintainers` (review group), при необходимости отдельная для public push.

Шаблоны корня group: [`templates/newcomer/template-org-kb-bootstrap-*.md`](../../templates/newcomer/README.md) — подставить `{ORG_SLUG}`, закоммитить в `{REPO_GROUP}`.

---

## Фаза B — source canon (у maintainer’а)

Нужен **полный** клон канона с `knowledge/`, `scripts/`, `agent-notes.md` (форк upstream или свой monorepo maintainer’а).

1. Настроить `knowledge/public-kb.ignore` (что не в public).
2. Настроить `knowledge/group-kb.ignore` — какие `work/projects/<scope>/` **не** экспортировать в group (личные/чувствительные scope).
3. Пройти санитизацию карточек перед seed (без `C:\`, `D:\`, имён, `personal/`).

Чеклист санитизации — в полном каноне maintainer’а (`knowledge/work/org/checklist-sanitize-paths-for-org-v1.md`); в kb-public его **нет** — это нормально.

---

## Фаза C — первая сборка public

Из корня source canon (PowerShell):

```powershell
.\scripts\build-public-kb.ps1
# артефакт: dist/public-kb/
```

Проверить `dist/public-kb/knowledge/` — без `work/`, `personal/`. Настроить `knowledge/public-kb.push` (локально, **не** в public): строка `https://github.com/{ORG_SLUG}/kb-public.git`.

```powershell
.\scripts\push-public-kb.ps1
```

---

## Фаза D — seed group KB

```powershell
.\scripts\build-public-kb.ps1   # если ещё не
.\scripts\seed-org-kb.ps1       # dist/group-kb/
```

Содержимое: public slice + отфильтрованный `work/projects/` + каталог **`knowledge/work/org/`** (contour map, чеклист; **норма для kb-public** — [`templates/work/template-scope-contour-map-v1.md`](../../templates/work/template-scope-contour-map-v1.md)) + `scripts/` + шаблоны из `scripts/kb-org-root/`. Опционально: переименование scope-каталога при копировании (см. [`map-kb-three-contours-v1.md`](map-kb-three-contours-v1.md) § Scope contour map).

Пуш в `{REPO_GROUP}` (maintainer): заменить содержимое репо (сохранить при необходимости `knowledge/group/smoke-test-v1.md` для smoke).

**Smoke для участников:** файл `knowledge/group/smoke-test-v1.md` в group — проверка `read_knowledge_file(..., knowledge_root_id=group)`.

---

## Фаза E — участник (personal + чтение group/public)

Не дублирует весь [`playbook-knowledge-stack-clean-setup-v1.md`](playbook-knowledge-stack-clean-setup-v1.md); только **добавка** к уже настроенному personal.

1. Клон `{REPO_PUBLIC}` и (по доступу) `{REPO_GROUP}`.
2. TOML — шаблон [`template-clean-setup-agent-notes-mcp-toml-v1.toml`](../../templates/newcomer/template-clean-setup-agent-notes-mcp-toml-v1.toml): `primary = "personal"`, `[[knowledge.read_only]]` id `public` и `group`.
3. `work/local/knowledge-roots-index-v1.md` — какие пути только в group/public (шаблон newcomer).
4. Hot-секция `knowledge-roots-routing-v1` в personal `agent-notes.md`.
5. Проверка: read group smoke, write в group → отклонение; write в personal → OK.

**Участник не пушит** в group без роли; предлагает PR или правки в personal.

---

## Фаза F — governance (кратко)

| Роль | Зона |
|------|------|
| **org-maintainer** | PR review в `{REPO_GROUP}` |
| **canon-maintainer** | `build-public-kb`, `push-public-kb`, `seed-org-kb`, import в source canon |
| **Участник** | personal git; read group/public через MCP |

Обратный поток group → personal — **вручную** (cherry-pick / import), не автосинк.

---

## Поведение агента

1. «Своя org KB» / white-label → **этот playbook**, не ADR конкретного бренда.
2. Не подставлять чужой `{ORG_SLUG}` в TOML пользователя.
3. Различать: **founder** (фазы A–D) vs **участник** (фаза E).
4. Ссылки на `AI-Guiders/*` в kb-public — только как **пример**, если файл исторический (ADR 011); норматив — плейсхолдеры.

---

## DoD (минимум)

- [ ] `{REPO_PUBLIC}` открывается, `knowledge/` без `work/`/`personal/`.
- [ ] `{REPO_GROUP}` private, smoke читается через MCP `knowledge_root_id=group`.
- [ ] Участник: personal primary, group/public read-only, реестр roots заполнен.
- [ ] CONTRIBUTING + CODEOWNERS в group из шаблонов newcomer.

---

## Связанные шаблоны

| Шаблон | Назначение |
|--------|------------|
| `templates/newcomer/template-org-kb-bootstrap-contributing-v1.md` | CONTRIBUTING для `{REPO_GROUP}` |
| `templates/newcomer/template-org-kb-bootstrap-codeowners-v1.md` | CODEOWNERS |
| `templates/newcomer/template-org-kb-bootstrap-readme-group-v1.md` | README корня group |
| `templates/newcomer/template-clean-setup-*` | personal + MCP у участников |
