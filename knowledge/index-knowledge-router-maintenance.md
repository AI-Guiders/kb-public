# Knowledge Router — Maintenance (index editors) v1
**Tags:** #kb-root


**Роль:** правила сопровождения главного индекса роутера, supplement, сплита кластеров, списка секций `router-*`, Domain Entry Map и публичной сборки. **Не** триггеры «какой playbook грузить по теме» — они в **`index-knowledge-router-supplement.md`**.

**Точка входа для чтения KB:** **`index-knowledge-router.md`** (блоки **А**–**В**); здесь — только то, что редакторам канона нужно не забыть при правках.


---

## Maintenance Rule

**Свежесть знаний** (fundamentals / operational / evidence, `Проверено:`, перепроверка домена) — **не здесь**; агент: `worlds/knowledge-engineering/playbook-kb-operational-freshness.md` + **`status-*` § Maintenance Policy** целевого домена. Ниже — только сопровождение **индекса роутера**.

- **Главный индекс** (`index-knowledge-router.md`): три блока — **А. Маршрутизация** (Fast Start, L1 pool, Retrieval, work/sysadmin, Domain Entry Map / `domain-entry-map-table`, Context Budget, указатель на supplement), **Б. Операционный базис** (краткий указатель → **`router-operational-baseline.md`**), **В. Безопасность и сопровождение** (Safety → **`index-knowledge-router-safety.md`**; правила и **How to add a domain** → **этот файл**; Personal — в индексе). Триггерные секции `router-*` — только в supplement.
- **Операционный базис роутера** — полное тело блока **Б** в **`router-operational-baseline.md`**; расширять и править **там**, в индексе оставлять только указатель в разделе **Б**.
- **Дополнение** (`index-knowledge-router-supplement.md`): все секции `router-*` и `learn-basics-when-stuck-router` — см. список `section_id` в разделе **Router sections** ниже.
- **Рост и сплит:** по умолчанию — **один** supplement-файл (меньше путей и границ для правок). **Вынести кластер в отдельный** `knowledge/index-knowledge-router-<cluster>.md`, когда supplement разрастается примерно **свыше ~800–1000 строк** или когда разные темы начинают мешать друг другу при редактировании; сначала выносить **самые толстые** доменные блоки, в supplement оставить короткое оглавление со ссылками и мелкие секции. После сплита: обновить **этот документ** (список файлов и `section_id`), при необходимости дописать вызов в `scripts/build-public-kb.ps1` для post-process нового индекса (как для главного, supplement, **maintenance** и **safety**).
- **Domain Entry Map table** — секция `domain-entry-map-table` в **главном индексе** (блок **А**): обновлять через MCP `upsert_knowledge_section` (canon, `index-knowledge-router.md`, section_id: `domain-entry-map-table`).
- **Router sections** (KB structure / ADR 009, Logic, Value, BCI/Medicine, Secret Mode, Clarification, Learn basics when stuck, Agent autonomy, Multi-project workspace, Session summary / chat export, KB MCP access, **KB operational freshness**, **Pedagogy school subjects**, Cursor captain/parallel agents, Polyamory, Therapy, Uncanny valley, Human perception, Videography, ML, Dotnet, JavaScript / ECMAScript, PHP/Laravel, Avalonia UI, Math numerics, Equation→CA→CUDA validation, Warehouse, Music, Regex, Sysadmin ops) — в **`index-knowledge-router-supplement.md`**, обёртки `router-kb-structure-adr009`, `router-logic`, `router-value-utility`, `router-bci-medicine`, `router-secret-mode`, `router-clarification`, `learn-basics-when-stuck-router`, `router-agent-autonomy`, `router-multi-project-context`, `router-session-summary`, `router-kb-mcp-access`, `router-kb-operational-freshness`, `router-pedagogy-school-subjects`, `router-captain-parallel-agents`, `router-polyamory`, `router-therapy`, `router-uncanny-valley`, `router-human-perception`, `router-videography`, `router-ml`, `router-dotnet`, `router-javascript`, `router-php-laravel`, `router-avalonia-ui`, `router-math-numerics`, `router-equation-ca-cuda-validation`, `router-warehouse`, `router-music`, `router-regex`, `router-sysadmin-ops`. Обновлять через `upsert_knowledge_section` с **`file_path: index-knowledge-router-supplement.md`**. Документы только под `knowledge/work/` не дублировать в роутере — их нет в kb-public; навигация через карточки в `work/projects/` и `read_knowledge_file` по полному пути в каноне.
- **Публичная сборка kb-public:** скрипт `scripts/build-public-kb.ps1` подчищает ссылки на отсутствующие `knowledge/*.md` в главном индексе, в supplement, в **`index-knowledge-router-safety.md`** и в **этом** maintenance-файле (см. `PUBLISHING.md`).
- **Массовые замены по файловому дереву:** не обходить и не править **`/.revisions/`** (корень канона) и **`knowledge/.revisions/`** — там снимки MCP перед правками; подмена строк там портит историю отката. Предпочтительно: только `git ls-files '*.md'` или явный whitelist каталогов под `knowledge/`.

## How to add a domain

1. **Domain Entry Map:** add one row to the table via MCP `upsert_knowledge_section` (canon_path, file_path: `index-knowledge-router.md`, section_id: `domain-entry-map-table`, content: full markdown table including the new row). Do not edit the table in place with StrReplace — use upsert to avoid duplicates.
2. **Router section:** add a new `## Domain Name (short label)` block with when to load which kb/playbook; wrap it in `<!-- section:router-<id> -->` … `<!-- /section:router-<id> -->` in **`index-knowledge-router-supplement.md`** and register the new `section_id` in буллете **Router sections** этого файла (блок **Maintenance Rule** выше).
3. **Full chain (optional):** if the domain follows status → playbook → kb, create `knowledge/worlds/<world>/status-<domain>.md` and `knowledge/worlds/<world>/playbook-<domain>.md` (pick `<world>` from `knowledge/worlds/README.md` / Domain Entry Map); put them in the new table row (Entry status and Primary playbook columns); router column = the kb/matrix files.

