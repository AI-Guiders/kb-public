# Evidence: Bakhtin (1986) — The Problem of Speech Genres

**Tags:** #rhetoric-pragmatics #paper-evidence #bakhtin #speech-genres #worlds

## Provenance

- source_refs:
  - primary: Bakhtin, M. M. (1986). *Speech Genres and Other Late Essays* (V. W. McGee, Trans.). University of Texas Press. Essay: «The Problem of Speech Genres».
  - text_consulted: full essay PDF — Critical Theory Consortium — https://criticaltheoryconsortium.org/wp-content/uploads/2018/07/Bakhtin-Speech-Genres.pdf (book scan; проверять страницы при цитировании)
  - alternate: rhetoric reading group mirror — https://rhetoricreadinggroup.wordpress.com/wp-content/uploads/2012/09/bakhtin_speech_genres.pdf
- created_at: 2026-08-22
- updated_at: 2026-08-22
- extraction_note: Перевод McGee; русский оригинал в *Эстетика словесного творчества* (1979). PDF — учебное/консорциумное зеркало, не UT Press OA.

## Metadata

- card_id: kb-bakhtin-speech-genres-1986-evidence-v1
- world: rhetoric.pragmatics
- layer: knowledge
- tags: [paper-evidence, speech-genres, utterance, dialogism]
- status: active

## Epistemic linkage

- epistemic_basis: synthesis_from_primary_literature
- evidence_type: philosophical essay (translated)
- confidence: **high** для тезиса «речевые жанры как типы utterance»; **medium** для иерархии primary/secondary без перечитывания полного текста
- transfer_boundary: не сводить жанр к **литературному** анализу только; не путать «жанр» в Бахтине с file format (ADR, playbook).
- falsification_trigger: если enum `genre` в speech_situation не различает primary vs secondary genres в диалоге — расширить template.

## Fundamentals

### K1 — Speech genre

**Речевой жанр** — каждый относительно стабильный тип **высказывания** (utterance): от однословной реплики до многотомного романа. Общая **вербальная (языковая) природа** — не только «литература».

### K2 — Heterogeneity

Богатство и **разнородность** жанров не отменяют общую проблему типа utterance; крайняя неоднородность — не причина оставить поле «пустым».

### K3 — Rhetorical genres (исторически)

Риторические жанры изучались с античности, но часто через **литературно-художественные** особенности, а не как типы utterance с общей языковой природой.

### K4 — Everyday genres

Бытовые жанры (реплики в диалоге) изучались в лингвистике (Saussure, structuralists, Vosslerians), но часто без **общей** теории utterance — Bakhtin: utterance как конкретная реальность языковой жизни, «внутренняя социальность» в коммуникации.

### K5 — Primary vs secondary genres

Различение **первичных (простых)** и **вторичных (сложных)** речевых жанров — важно для анализа (детали в источнике; не сводить диалог к монологу жанра).

## Operationalization

- `genre` в speech_situation: playbook, case_report, faq, copypaste_block — **operational жанры** KB/диалога, не полный каталог Бахтина.
- Смешение FAQ + case_report в одном ответе = смешение **жанров utterance** → низкий `situation_purity` в XL.

## Lifecycle

- related: `kb-bitzer-rhetorical-situation-1968-evidence-v1` (situation × genre)

