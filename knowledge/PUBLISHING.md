## Публикация KB: что входит, а что нет

Этот файл задаёт явные правила, **какие части KB можно выкладывать публично**, а какие остаются только локально.

**Лицензия на текст внутри публичной сборки kb-public** (артефакт после фильтров этого файла; если в конкретном файле не указано иное): см. раздел **«Лицензия: публичная сборка KB (kb-public)»** в [`README.md`](README.md) в этом каталоге — **CC BY-SA 4.0**; это **не** лицензия на весь репозиторий agent-notes; коммерция — по согласованию.

### Механика сборки kb-public

1. **`agent-notes.md`** — в сборку попадает только текст **до** первого маркера `<!-- public-cut -->`.
2. **`knowledge/**`** — копируется всё, что **не** отфильтровано шаблонами из **`knowledge/public-kb.ignore`** (по смыслу как `.gitignore`: строка с `/` на конце = целое поддерево от корня `knowledge/`; без `/` = один файл; допускается `*`).

**Group KB (`seed-org-kb.ps1` → репо `{ORG_SLUG}/kb`, private):** база = public slice; **`knowledge/work/projects/`** добавляется **выборочно** по **`knowledge/group-kb.ignore`**. Scope contour (personal scope → group catalog name): **шаблон** [`templates/work/template-scope-contour-map-v1.md`](templates/work/template-scope-contour-map-v1.md) в kb-public; **заполненная таблица** maintainer'а — `knowledge/work/org/` (в group после seed). Сводка: [`domains/agent-operations/map-kb-three-contours-v1.md`](domains/agent-operations/map-kb-three-contours-v1.md). White-label: [`domains/agent-operations/playbook-org-kb-white-label-v1.md`](domains/agent-operations/playbook-org-kb-white-label-v1.md).
3. **Корень артефакта kb-public** — в `dist/public-kb/` кладутся **`README.md`** и **`LICENSE`** (CC BY-SA 4.0) из **`scripts/kb-public-root/`** (для репозитория **kb-public** на GitHub и зеркалах).
4. **Сайт документации (MkDocs)** — в репозитории **kb-public**: `docs/` (онбординг RU/EN), `mkdocs.yml`, workflow `docs-pages.yml`. Публикуется на **`https://<org>.github.io/kb-public/`** (пример: AI-Guiders). Онбординг для людей — **на сайте**, не в GitHub wiki. Сборка: `python tools/sync_knowledge_docs.py && mkdocs build`.
5. **Первая строка файла** — если содержит подстроку **«НЕ ПУБЛИКОВАТЬ»**, файл в сборку **не** копируется (можно исключить единичный файл без правки `public-kb.ignore`).
6. **Индексы роутера** — в копиях `index-knowledge-router-v1.md`, `index-knowledge-router-supplement-v1.md`, `index-knowledge-router-maintenance-v1.md` и `index-knowledge-router-safety-v1.md` под `knowledge/` сборка **удаляет** секции `## …`, которые ссылаются на `knowledge/*.md`, отсутствующие в публичном наборе.

Сборку выполняют из **полного** клона **личного/командного канона** (репозиторий maintainer’а с `scripts/`) или из group-репо **`{ORG_SLUG}/kb`** после seed (зеркало `scripts/` для canon-maintainer). В артефакт kb-public попадают обрезанный **`agent-notes.md`**, отфильтрованный **`knowledge/`**, корневые **`README.md`** и **`LICENSE`** из **`scripts/kb-public-root/`**; каталог **`scripts/`** и операции **git push** в зеркало kb-public **в zip не входят**. Список remotes — **`knowledge/public-kb.push`** (в публичную сборку не копируется; шаблон `scripts/public-kb.push.example`).

### Что обычно в публичной kb

По общему правилу п. 2 в публичный срез попадают типичные **`knowledge/*.md`**: плейбуки, индексы, доменные kb, **`knowledge/META/`** (Integrity POST и спеки), **этот `PUBLISHING.md`**, **`kb-one-pager-structure-and-protocols-v1.md`** (онлайн-онбординг: слои, маркеры, зачем в полном каноне есть `work/` и `personal/`), **`kb-protocols-and-entities-one-pager-v1.md`** (wiki-вход: протоколы и сущности Scope/Primary, схемы), **`worlds/knowledge-engineering/playbook-kb-operational-freshness-v1.md`** (свежесть знаний: fundamentals / operational / evidence, перепроверка любого домена; supplement `router-kb-operational-freshness`). В **`agent-notes.md`** в kb-public — секции **выше** `<!-- public-cut -->`, в т.ч. **`kb-operational-freshness-v1`**. Корневые **`README.md`** / **`LICENSE`** для репозитория kb-public — п. 3 «Механики».

### `agent-notes.md`: выше или ниже `public-cut`

- **Ниже cut:** идентификация конкретного человека; личный диалог, имена, эмоциональный/внутренний контекст отношений; внутренние планы, не предназначенные для публикации; формулировки вида «X сказал», «для X» (X — конкретный собеседник); пересказ частного разговора.
- **Выше cut:** обезличенные принципы, паттерны, плейбуки, evidence — без привязки к лицу и без приватного контекста; если суть можно сказать через «пользователь» / «к агенту» без раскрытия чьей-то приватности.
- **Сомнение:** «идентифицирует или экспонирует пользователя/отношения?» — да → ниже cut; нет → выше.

### Личный слой и потребитель kb-public

Личное (те же критерии, что для «ниже cut») — в **`knowledge/personal/`**; каталог создавай при необходимости, при желании краткий README («Личный контур. Не публиковать. См. `PUBLISHING.md`»). При **любом** шаринге форка/архива **не включай** `personal/` наружу.

Если у тебя **только** выгрузка kb-public: дерева **`personal/`** и **`work/`** там **нет по дизайну** — это не ошибка сборки.

### Не попадает в kb-public (ориентир)

- Всё, что покрывает **`knowledge/public-kb.ignore`** (в т.ч. префиксы **`personal/`**, **`work/`**, **`archive/`**; сами **`public-kb.ignore`** и **`public-kb.push`**; сегмент пути **`.revisions/`** под `knowledge/`).
- **`knowledge/work/`** — оперативный слой канона (карточки репо, `project-id`, внутренние runbook’и); не публичный продукт KB. Карта дерева для держателей полного клона: **`knowledge/work/README.md`** (в kb-public не копируется вместе с `work/`).
- Файлы с **пометкой в первой строке** (типично `⚠️ НЕ ПУБЛИКОВАТЬ. Только локально.`) — см. п. 4 в «Механике».

### Авторинг под `worlds/` (попадает в kb-public)

Файлы в **`knowledge/worlds/<slug>/`** (любой мир) копируются в публичную сборку, если не перекрыты `public-kb.ignore`. **Не полагаться на «само собой разумеется»:** перед коммитом в **каждом** slug вычищать внутреннюю operationalку, scope/project-id, ссылки на **`work/`**, машинные пути, внутренние бренды; в fundamentals — только общеизвестные вендоры/платформы.

**Чеклист агента:** [`worlds/knowledge-engineering/playbook-kb-world-public-authoring-v1.md`](worlds/knowledge-engineering/playbook-kb-world-public-authoring-v1.md).

### Новое исключение по пути

Добавь строку в **`knowledge/public-kb.ignore`**, пересобери — править `build-public-kb.ps1` не нужно.
