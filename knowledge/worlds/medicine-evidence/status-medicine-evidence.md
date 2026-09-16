# Medicine (Evidence-Based) Domain Status v1
**Tags:** #medicine-evidence #status #worlds


## Scope

Evidence-based навигация по BCI (интерфейсы мозг–компьютер) и смежным нейрореабилитационным направлениям: инсульт, травма спинного мозга, locked-in/БАС, восстановление речи при параличе, ДЦП/дети, нейрофидбек. Не заменяет клинические руководства и протоколы; даёт уровни доказательности и ссылки на обзоры/RCT.

## Completion State

Status: **Done v1 (Evidence layer)**

Completed artifacts:

- `kb-bci-evidence-based-medicine.md`
- `status-medicine-evidence.md`
- `playbook-medicine-evidence.md`

## Retrieval

- При запросах о BCI, нейрореабилитации, evidence-based медицине в этих областях: загружать `kb-bci-evidence-based-medicine.md` (через playbook или напрямую по индексу).
- Order: status → playbook → kb (без matrix; кросс-мир не требуется для чистого evidence-навигации).

## Guardrails

- Не давать клинических рекомендаций «назначить X» — только уровни доказательности и ссылки; решение за врачом/протоколом.
- При упоминании конкретного пациента/кейса — не подставлять диагноз/лечение; направить к источникам и руководствам.

## Maintenance Policy

- Event-driven refresh (not calendar-only). Order: `status-*` → playbook → one `kb-*` per pass (`playbook-kb-operational-freshness.md`).
- **Next review triggers:**
  - New edition / major paper / platform release superseding cited claims
  - Broken `source_refs` / URL rot
  - Repeated field mismatch with practice or primary sources
  - Operator/agent flags a stale claim

