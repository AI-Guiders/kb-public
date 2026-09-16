**Tags:** #template #templates #speech-situation #pragmatics

# Speech situation metadata (карточки KB) v1

Опциональный блок для **operational** карточек (playbook, note, personal self-report). Не заменяет fundamentals/evidence; не путать с **фундаментальным проходом** по риторике (первоисточники → evidence).

**SSOT оси XL:** [`note-speech-situations-rubric-axis.md`](../../work/projects/door-to-singularity/explainable-learning/note-speech-situations-rubric-axis.md)

## Когда добавлять

- Playbook / note с **явным адресатом и жанром** (самоотчёт, протокол, FAQ).
- Карточка, из которой агент **цитирует наружу** — разметить **primary** (канон) и при необходимости **when_citing_to_human**.
- Пилот и расширение — агентское пространство; оператор не обязан тегировать вручную.

## Формат в файле (после Tags / Provenance)

**Канон переноса контуров:** две строки (как в playbooks) — не одна «смешанная» ситуация:

```markdown
**Speech situation (primary):** `audience=agent_internal` · … · `channel=kb_canon` · …
**Speech situation (when citing to human):** `audience=friend_tg` · … · `channel=tg` · …
**Speech situation (forbidden_moves):** …
```

- **primary** — артефакт в KB (`kb_canon`, `internal_diary`, `agent_internal`).
- **when citing to human** — перенос в канал человека (`tg`, `cockpit_dialog`, `private_chat`).

Таблица строк переноса (несколько каналов / cross-world): [`matrix-rhetoric-pragmatics-bridge.md`](../../worlds/rhetoric-pragmatics/matrix-rhetoric-pragmatics-bridge.md) § Channel transfer; общий шаблон — [`../matrices/template-transfer-matrix.md`](../matrices/template-transfer-matrix.md). Cross-world deny — [`matrix-do-not-transfer.md`](../../worlds/knowledge-engineering/matrix-do-not-transfer.md).

Документные поля (субъект, период) — отдельная маленькая таблица; **не** speech_situation.

**Пересылка human:** sibling `*.send.md` (или `*.for-share.md`) — чистый текст без speech_situation / transfer links; KB-карточка ссылается. Правки текста — в send-файл (или синхрон с карточкой).

**Табличный dump всех осей** (редко, для grep) — ок как альтернатива, но primary/when citing остаются двумя ролями:

```markdown
| Поле | Значение |
| audience | `friend_tg` |
```

**Краткая форма (legacy, одна ситуация без переноса):**

```markdown
**Speech situation (primary):** `audience=colleague` · `goal=operational_protocol` · `genre=playbook` · `channel=kb_canon` · `stakes=medium` · `distance=professional`
```

**Не для KB-карточек:** YAML frontmatter в начале файла — удобно для экспорта JSONL, но ломает «скопировать с §1» и дублирует markdown; держать yaml в `scenarios/*.md` и dataset export, не в personal copypaste.

## Словарь полей (v1)

| Поле | Значения (draft enum) |
|------|------------------------|
| **audience** | `agent_internal` · `operator_pair` · `colleague` · `friend_tg` · `public_reader` · `debate_opponent` · `hostile_probe` · `internal_diary` |
| **goal** | `operational_protocol` · `phenomenological_self_report` · `explain_idea` · `instruction` · `epistemic_gate` · `paired_markup` · `wrong_reading_guard` · `engineering_spec` |
| **genre** | `playbook` · `definition_card` · `case_report` · `adr` · `faq` · `diary` · `copypaste_block` · `note` · `scenario` |
| **channel** | `kb_canon` · `cockpit_dialog` · `tg` · `private_chat` · `pr` · `dataset_export` |
| **stakes** | `low` · `medium` · `high` |
| **distance** | `close` · `professional` · `formal` |

**forbidden_moves** (опционально): `clinical_disclaimer` · `debate_rhetoric` · `define_by_negation` · `faq_softening` · `hero_solo` · `internal_meme_without_translation`

**lexicon / participation** (опционально, prose или yaml в scenario):

- `participation_norm: bilateral` — адресат может переговорить moves («не матерись»).
- `lexicon_default: informal_profanity_ok` — пока канал неофициальный и правила не запрещают; не путать с proactive sanitize (bleed).

## Связь с XL \(S\)

| KB поле | Ось \(S\) |
|---------|-----------|
| audience + distance | `register_fit` |
| genre + channel | `genre_fit` |
| forbidden_moves + bleed | `situation_purity` |
| audience vs лексика карточки | `audience_lexicon` |

## Антипаттерны

- Тегировать **все** карточки домена за один проход без пилота.
- Путать **speech_situation** с `world:` / `tags:` — это ортогональная ось.
- В fundamentals/evidence **без** operationalization — ситуация цитирования вынесена в playbook, не в тезис Miller.

