# Мир **cognition.language-acquisition** (детское усвоение языка L1)

**Идентификатор мира:** `cognition.language-acquisition`  
**Каталог:** `knowledge/worlds/cognition-language-acquisition/`  
**Назначение:** **human child first-language acquisition** — CDS, corrective input, lexical learning (Snow, Clark, Saxton, …). Операционный слой для вопросов «как дети учат язык», **не** spec инженерных агентов.

**Не путать с:** CASA substrate (`work/projects/door-to-singularity/ca-substrate-agent/`) — transfer **deny** по умолчанию; см. [`matrix-language-acquisition-transfer-v1.md`](matrix-language-acquisition-transfer-v1.md).

**Инженерная половина (sibling):** [`../ml-learning-dynamics/README.md`](../ml-learning-dynamics/README.md) — ML-аналоги (curriculum, forgetting, CLS, EWC) с `transfer_boundary: allow-with-check`. Две половины гипотезы CASA «педагогика развития».

**Соседи:** [`../psychology-models/README.md`](../psychology-models/README.md) (широкая психология); [`../cognition-human-perception/README.md`](../cognition-human-perception/README.md) (восприятие/UX, другой контур); [`../cognition-neurolinguistics/README.md`](../cognition-neurolinguistics/README.md) (brain language/reading — bridge → pedagogy); [`../pedagogy-general/README.md`](../pedagogy-general/README.md) (**school** pedagogy — другой контур; transfer deny без bridge).

## Слои канона (порядок загрузки)

| Слой | Файл | Роль |
|------|------|------|
| **Status** | [`status-language-acquisition-v1.md`](status-language-acquisition-v1.md) | DoD, guardrails, список артеfactov |
| **Playbook** | [`playbook-language-acquisition-operational-v1.md`](playbook-language-acquisition-operational-v1.md) | Когда грузить мир; вопросы агенту; **не** CASA bench |
| **Fundamentals** | [`kb-language-acquisition-fundamentals-v1.md`](kb-language-acquisition-fundamentals-v1.md) | Карта понятий: CDS, feedback types, conventionality/contrast |
| **Scientific evidence (index)** | [`kb-language-acquisition-scientific-evidence-v1.md`](kb-language-acquisition-scientific-evidence-v1.md) | DOI, **глубина чтения**, ссылки на evidence-карты |
| **Evidence (papers)** | `kb-language-acquisition-*-evidence-v1.md` | По одному первоисточнику или кластеру (шаблон `templates/cards/template-kb-evidence-v1.md`) |
| **Transfer** | [`matrix-language-acquisition-transfer-v1.md`](matrix-language-acquisition-transfer-v1.md) | Cross-world: CASA, psychology, HCI |

## Router

Строка **Child language acquisition (L1)** в [`index-knowledge-router-v1.md`](../../index-knowledge-router-v1.md).

## Версия

v1.1 · 2026-05-31 — добавлен sibling-линк на ML-половину `ml.learning-dynamics`.  
v1.0 · 2026-05-31 — мир собран по триаде cognition-human-perception; заменяет черновик `cognition-language-development/`.
