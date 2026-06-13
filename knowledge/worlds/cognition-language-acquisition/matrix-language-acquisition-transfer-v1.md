# Transfer matrix — language acquisition (L1) v1

**Мир:** `cognition.language-acquisition`  
**См. также:** [`../knowledge-engineering/matrix-do-not-transfer-v1.md`](../knowledge-engineering/matrix-do-not-transfer-v1.md)

## Purpose

Зафиксировать, что human child L1 **не** становится CASA spec «по аналогии».

## Matrix

| Source | Candidate transfer | Default | Boundary check |
|--------|-------------------|---------|----------------|
| `cognition.language-acquisition` | `ca-substrate-agent` teacher/sleep/T9 | **deny** | Engineering contract only; no literature→`correction_kind` table |
| `cognition.language-acquisition` | `research-training-developmental-pedagogy-v1` | **allow-with-check** | Metaphor/inspiration; hypothesis status |
| `cognition.language-acquisition` | `psychology-models` | **allow-with-check** | Broader psychology; not clinical replacement |
| `cognition.language-acquisition` | `cognition.human-perception` | **deny** | Different construct (L1 vs attention/load) |
| `cognition.language-acquisition` | `language-acquisition-loop-v0` (lab north star) | **allow-with-check** | Narrative metaphor only; link playbook |

## Red flags

- «Snow says → oracle lemma on prefix»
- Evidence card without `read_depth`
- Monolithic «empirical canon → CASA mapping» file

*Версия: v1.0 · 2026-05-31*
