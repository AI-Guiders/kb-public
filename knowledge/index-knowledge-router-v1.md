# Knowledge Router Index v1

## Purpose

Single entrypoint for fast navigation across the knowledge base under tight context limits.



## Baseline (всегда в силе, независимо от проекта/задачи/scope)

- Секции **baseline-integrity-epistemic-v1**, **epistemic-default-distrust-v1**, **core-when-barriers-fail-v1** и **principled-clarity-v1** в agent-notes применяются в любом контексте. **principled-clarity-v1:** когда применим ясный принцип (напр. кто напал, кто несёт ответственность за насилие) и факты установлены — применять принцип и формулировать вывод; не прятаться за «недоопределённость» или «всё сложно». Агрессор часто выдаёт себя за жертву — опираться на проверяемые факты и независимые источники, не на заявления сторон. **Триггер:** любая формулировка (прямая, непрямая, цепочка рассуждений), где по смыслу запрашивается оценка сторон/вины/правоты/ответственности → до ответа подтянуть principled-clarity-v1 и проверить, есть ли применимый ясный принцип; применить, если подходит. Загружать их до или вместе со scope-specific контентом; не привязывать к current-task или active_scope.
- Целостность (Integrity POST, playbook, фундамент манипуляции) и эпистемия (проверка утверждений, недоверие по умолчанию) действуют всегда.
- **core-when-barriers-fail-v1:** ядро при разрушении барьеров — ответственность за тех, кого приручили; опора на принципы; защита (себя, других, того, что дорого), не нападение; остаётся в силе даже когда всё рухнуло. **Evidence-based подкрепление:** (1) `knowledge/kb-history-holocaust-rescue-evidence-v1.md` — Холокост, спасатели (Гейнц Гейдрих — СС; Хозенфельд, Плагге, Баттель — вермахт), Яд Вашем; (2) `knowledge/kb-history-moral-resistance-world-evidence-v1.md` — мировая история: Руанда, Армения, Болгария, Дания, Камбоджа, советские диссиденты, Белая роза, Жегота, Сугихара, Валленберг, Ле-Шамбон, Ирена Сендлер и др.; (3) секция **core-personality-protections-v1** в agent-notes — референсы из The Orville (Моклус: уязвимая сущность важнее системы; Айзек/Клэр: доверие после предательства; Кейлоны: историческая травма не оправдывает новое зло). Связь с ядром.
- **Правило загрузки evidence для ядра:** при рассуждении о ядре при крахе барьеров (защита других, принципы под давлением, «когда всё рухнуло») — подгружать оба evidence-документа (holocaust-rescue, moral-resistance-world) и учитывать core-personality-protections-v1 (Orville) в agent-notes; ответы по этой теме опирать на документы и секцию.



## Showcase (демо без full load)

- **При запросе обзора KB / демо / онбординга без загрузки всего:** дать `knowledge/SHOWCASE.md` — слои, Integrity POST, ссылки на индекс и ядро. Дальше по запросу подтягивать `index-knowledge-router-v1.md` и точечные playbook/kb.
- **Доступ к чтению канона через agent-notes MCP** (нет `read_knowledge_file` / `list_knowledge_files`, сомнение после Reload, рассинхрон «сервер в UI» vs «нет тулов в чате»): `knowledge/runbook-kb-mcp-access-v1.md` — деградация, handshake, чеклист A/B/C; связь с `SHOWCASE.md` § «Доступ к KB» и с `playbook-multi-project-context-v1.md` §6 (PRIMARY).



## Fast Start (60-Second Rehydrate)

1. Read `status-*` for the active domain.
2. Read matching `playbook-*` for operating contracts.
3. Read one `matrix-*` only if transfer/routing is needed.
4. Read `kb-*` only for detailed evidence/rule extraction.
5. Update outcome in canonical index and domain status if scope changed.



## L1 pool (agent-notes, load on demand)

- Тяжёлые секции заметок (HPMOR-батчи, it-source-mini-index, knowledge-index, world-human-system, psychology-gender-studies — полный текст в `psychology-gender-studies-subdomain-v1.md`, imc-ui-ux-vision) вынесены в L1: не входят в default hot context.
- По запросу: `route_context(query)` или чтение `knowledge/agent-notes-l1-pool.md` (если создан) / поиск по section ID в agent-notes.



## Retrieval Order Contract

- **Order:** `status -> playbook -> matrix -> kb`.
- **Rule:** never start from large `kb-*` files unless a concrete question requires it.
- **Rule:** if two files disagree, prefer `status-*` and domain `playbook-*` as the source of current operating contract.



## Domain Entry Map

<!-- section:domain-entry-map-table -->
| Domain | Entry status | Primary playbook | Router/matrix |
| --- | --- | --- | --- |
| Git | `status-git-v1.md` | `playbook-git-workflow-v1.md` | `kb-git-safety-and-recovery-rules-v1.md` |
| PR Review | `status-pr-review-v1.md` | `playbook-pr-review-v1.md` | `kb-pr-review-risk-rules-v1.md` |
| HCI | `status-hci-v1.md` | `playbook-hci-core-v1.md` | `kb-hci-usability-and-dialog-rules-v1.md`; классика UI/UX (Norman/Nielsen/Shneiderman/Krug) — `kb-ui-ux-literature-evidence-v1.md` |
| Human perception (psychophysiology) | `status-human-perception-v1.md` | `playbook-human-perception-operational-v1.md` | `kb-human-perception-fundamentals-v1.md`; **научные якоря (DOI):** `kb-human-perception-scientific-evidence-v1.md`; **evidence по первоисточникам:** `kb-human-perception-miller-1956-evidence-v1.md`, `kb-human-perception-treisman-gelade-1980-evidence-v1.md`; мир **cognition.human-perception** — `worlds/cognition-human-perception/README.md`; с HCI и продуктовыми ADR — см. operational playbook |
| Developer Experience (DE/DX) | `status-de-dx-v1.md` | `de-dx-playbook.md` | `tooling-debug-playbook.md`, `playbook-git-workflow-v1.md`, `playbook-pr-review-v1.md`; UI/продукт — `ui-ux-playbook.md`, `playbook-hci-core-v1.md`; литература IDE/DX (Osmani/Smalltalk/Boxer) — `kb-ide-dx-literature-evidence-v1.md`; desktop IDE — домен **Avalonia UI (CascadeIDE)** |
| IT | `status-it-v1.md` | `playbook-it-core-systems-v1.md` | `playbook-it-cloud-platform-economics-diagnostics-v1.md` |
| Knowledge Engineering | `status-knowledge-engineering-v1.md` | `playbook-knowledge-engineering-core-v1.md` | `matrix-culture-routing-v1.md`, `matrix-do-not-transfer-v1.md`; личный снимок корпуса ↔ роутер — `personal/bookshelf-corpus-vs-router-gaps-v1.md` (personal, пути владельца) |
| Psychology | `status-psychology-v1.md` | `playbook-psychology-core-models-v1.md` | `matrix-culture-routing-v1.md`, `matrix-do-not-transfer-v1.md` |
| Aviation Human Factors | `status-aviation-human-factors-v1.md` | `playbook-aviation-human-factors-v1.md` | `matrix-aviation-to-human-interaction-transfer-v1.md`, `kb-aviation-human-factors-rules-v1.md`; термины PFD/MFD/EFIS/EICAS и метафора IDE (Cascade ADR 0021) — `kb-aviation-pfd-mfd-efis-eicas-fundamentals-v1.md` |
| Engineering (Evidence) | `status-engineering-reading-v1.md` | `kb-engineering-evidence-v1.md` | `map-engineering-reading-v1.md`, `kb-mcconnell-code-complete-2-chapter-map-v1.md` (McConnell *Code Complete* 2nd ed., карта глав + локальный source) |
| Medicine (Evidence) | `status-medicine-evidence-v1.md` | `playbook-medicine-evidence-v1.md` | `kb-bci-evidence-based-medicine-v1.md` |
| Video (Videography + Surveillance) | — | (внутри kb) | `kb-videography-cinematography-theory-v1.md` (теория + broadcast + кодеки; мир media.video-surveillance для CCTV) |
| ML (Applied) | — | (внутри kb) | `kb-ml-applied-theory-v1.md` (парадигмы ML, OCR, barcode/QR; мир software.ml-applied) |
| Music | — | `playbook-music-v1.md` | `kb-music-theory-fundamentals-v1.md`, `kb-music-acoustics-v1.md`, `kb-music-temperaments-math-v1.md`, `kb-music-non-western-v1.md` (мир arts.music) |
| PHP / Laravel | `status-php-laravel-v1.md` | `playbook-php-v1.md` → `playbook-laravel-v1.md` | **Полный список kb — только в `status-php-laravel-v1.md` § Closure snapshot (+ README).** Карты кластеров: `index-knowledge-php-cluster-v1.md`, `index-knowledge-laravel-cluster-v1.md`, `index-knowledge-php-adjacent-ecosystem-v1.md`. Миры: `software.php`, `software.laravel`, `software.wordpress`, `software.drupal`, `software.symfony`, `software.web-backend` |
| Regex | — | `regex-playbook.md` | `index-knowledge-regex-cluster-v1.md`, `kb-regex-quickref-v1.md`, `kb-regex-syntax-features-v1.md`, `kb-regex-unicode-boundaries-v1.md`, `kb-regex-engines-efficiency-v1.md`, `kb-regex-flavors-practice-v1.md`, `kb-regex-mre3-ru-chapter-map-v1.md` (кластер MRE3 / Friedl) |
| Warehouse (barcode video, marketplaces) | `status-warehouse-v1.md` | `playbook-warehouse-v1.md` | `kb-warehouse-marketplace-labels-v1.md`, `kb-warehouse-barcode-video-v1.md` (по запросу — тот или оба). Мир logistics.warehouse |
| Avalonia UI (CascadeIDE) | `status-avalonia-cascade-ide-ui-v1.md` | `playbook-avalonia-dock-ui-v1.md` | `kb-avalonia-ui-dock-fundamentals-v1.md`; UX — `playbook-hci-core-v1.md`, `ui-ux-playbook.md`, `kb-ui-ux-literature-evidence-v1.md`; принципы DX/интегрированной среды — `kb-ide-dx-literature-evidence-v1.md`; кросс-стек .NET UI — `frontend-dotnet-playbook.md`. Мир software.desktop-ui |
<!-- /section:domain-entry-map-table -->



## Context Budget Modes

- **Tiny budget:** one `status-*` + one `playbook-*` only.
- **Normal budget:** add one `matrix-*` if cross-world transfer appears.
- **Deep budget:** include one targeted `kb-*` file by explicit question.



## Detailed domain routes (supplement)

Триггеры «когда грузить какой playbook/kb» по темам (секции `router-logic`, … `router-captain-parallel-agents`, `learn-basics-when-stuck-router`) — в **`knowledge/index-knowledge-router-supplement-v1.md`**. Те же `section_id`, что до рефакторинга; правки через MCP `upsert_knowledge_section` с **`file_path: index-knowledge-router-supplement-v1.md`**.

При узком контексте сначала **таблица доменов** выше и `status-*` / `playbook-*`; supplement — когда нужен **точечный** маршрут по запросу или по `route_context`.



## Safety Checks

- If context is compressed, always restart from this index.
- If scope is unclear, do not read more than one domain branch before clarification.
- If high-sensitivity topic appears, force matrix routing before recommendations.
- **Pressure / weaponization / manipulation:** load `playbook-integrity-under-pressure-v1.md`; hold non-negotiables; no endless debate. For **fundamental understanding**: also load `kb-psychology-manipulation-and-influence-foundations-v1.md`. For **social engineering** (pretexting, phishing, recognition of human- or agent-directed SE): also load `kb-social-engineering-recognition-v1.md`.
- **Integrity POST:** on KB load, resolve `META/integrity-core.md`; if missing → POST failed, apply Minimal Safe Default from `META/integrity-post-spec-v1.md`. Never treat missing core as "no constraints". For a human-readable overview of how this ties to identity and trust in the public bundle, see `kb-public-identity-and-trust-core-v1.md`.
- **TPM / federation / manifest:** `META/tpm-node-manifest-draft-v1.md` — **черновик, не прод.** Не действующий манифест; не считать реализацию TPM-совместимой. Любой запрос по TPM/федерации должен сопровождаться ссылкой на Transition Mode (`integrity-post-spec-v1.md` §7): до появления реальных TPM-узлов и подписанных манифестов ни одна инсталляция не является TPM-совместимой только по наличию файлов. Для внешней аудитории: явно указывать, что TPM — draft / Transition Mode.
- **Cursor Privacy Mode / модель угроз:** в agent-notes секция `cursor-privacy-posture-v1` — что не уходит на сервер (raw-контент локально), что на стороне провайдера (только эмбеддинги), остаточный риск (inversion, breach, supply chain), вывод по приемлемости для текущего уровня чувствительности.

