# Child language acquisition — operational playbook v1

**Purpose:** когда и как использовать мир `cognition.language-acquisition`.  
**Fundamentals:** [`kb-language-acquisition-fundamentals-v1.md`](kb-language-acquisition-fundamentals-v1.md)  
**Index + DOI + read_depth:** [`kb-language-acquisition-scientific-evidence-v1.md`](kb-language-acquisition-scientific-evidence-v1.md)  
**Transfer:** [`matrix-language-acquisition-transfer-v1.md`](matrix-language-acquisition-transfer-v1.md)

---

## 1. Когда загружать этот playbook

- Вопрос про **human child L1**: CDS, maternal input, corrective feedback, word learning, prefix ambiguity **в речи ребёнка**.
- Нужно **извлечь факты** из literature с `transfer_boundary`, не blog-summary.
- Ревью draft KB, который **мапит** Snow/Saxton → engineering spec.

**Не загружать как spec для:**

- CASA teacher / sleep / T9 / hippo → `ca-substrate-agent/teacher-correction-protocol-v0` (lab mirror)
- Общая психотерапия → `psychology-models/`
- UX cognitive load → `cognition-human-perception/`

---

## 2. Порядок чтения (router-first)

1. Этот playbook (триггер)
2. [`kb-language-acquisition-fundamentals-v1.md`](kb-language-acquisition-fundamentals-v1.md) — карта понятий
3. [`kb-language-acquisition-scientific-evidence-v1.md`](kb-language-acquisition-scientific-evidence-v1.md) — выбрать строку → открыть **evidence-карту**
4. При cross-world → [`matrix-language-acquisition-transfer-v1.md`](matrix-language-acquisition-transfer-v1.md) + [`../knowledge-engineering/matrix-do-not-transfer-v1.md`](../knowledge-engineering/matrix-do-not-transfer-v1.md)

---

## 3. Чеклист агента (evidence hygiene)

1. **read_depth:** full text / abstract / secondary — пометить явно; не выдавать abstract за full.
2. **transfer_boundary** на каждой evidence-карте — соблюдать deny → CASA.
3. **Debates:** motherese effect sizes, Brown & Hanlon vs Saxton — не схлопывать в один вывод.
4. Новая evidence-карта → **шаблон** [`templates/cards/template-kb-evidence-v1.md`](../../templates/cards/template-kb-evidence-v1.md); строка в scientific-evidence index.
5. **PDF первоисточник:** скачать в workspace → MCP **`pdf_capture_burst`** + **`ocr_image_batch`** (webcam-analysis-mcp). KB — **`read_knowledge_file`** / **`write_knowledge_file`** (agent-notes). Не pypdf/curl-OCR ad hoc.

---

## 4. Inspiration vs specification (CASA)

`research-training-developmental-pedagogy-v1` (ca-substrate-agent) — **метафора** классов сигналов для КА-протокола (hypothesis).  
Этот мир — **факты о human L1**. Мост — только explicit engineering validation.

*Версия: v1.0 · 2026-05-31*

