---
type: Evidence Card
title: Drosophila melanogaster — Ухаживание/песня и популяционная дифференциация (evidence card v1)
tags: [biology-drosophila, worlds, kb, evidence, courtship, song, speciation, qst, qtl]
world: biology
subworld: drosophila
---
# Drosophila melanogaster — Ухаживание/песня и популяционная дифференциация (evidence card v1)

## Provenance (происхождение)
- source_refs:
  - paper: «Courtship song differs between African and European populations of Drosophila melanogaster and involves a strong effect locus» — G3 2025, DOI 10.1093/g3journal/jkaf050, PMC12060230 — **полный текст прочитан** (Song recording/analysis, population comparison, QTL mapping, candidate genes, pulse mode)
  - related: Clemens et al. 2018 (fast/slow pulse mode, female response) — цитирована
  - related: Nature 2026 (P1) — карточка 1.5 (цепи ухаживания)
- created_at: 2026-09-19
- updated_at: 2026-09-19
- extraction_note: полный текст прочитан (ядро); цепи ухаживания (P1 → двигательные) — карточка 1.5; этот источник — генетика/популяционная дифференциация.

## Metadata
- card_id: kb-drosophila-courtship-song-evidence-v1
- world: biology.drosophila
- layer: world
- tags: [courtship, song, pulse-mode, qtl, qst, fst, population, speciation]
- status: draft

## Epistemic Linkage
- epistemic_basis: fact (из полного текста)
- evidence_type: paper (ориг., полный текст)
- confidence: high (методы/результаты G3 2025)
- uncertainty:
  - кандидатные гены в QTL — ассоциации (не причинность; авторы осторожны)
  - роль fast/slow pulse mode в половом отборе — неизвестна (Clemens 2018: влияет на движение самки)
  - 10 FR + 7 ZI strains — ограниченная выборка
- falsification_trigger:
  - если «сильный QTL 42%» не воспроизведётся (другие панели) — обновить
  - если pulse mode окажется артефактом условий — обновить (авторы обсуждают chamber/female effects)
- transfer_boundary:
  - НЕ переносить в CASA: это поведение/эволюция; НО: «QST > 96.5% SNP = направленный отбор на песню» — пример генетической основы поведения и её эволюции (для слоя 6)

## Layer contract (evidence — заполнить для агента)
- **Fundamentals** (ниже) — опорный слой: песня, трейты, QTL/отбор.
- **Core Unit + Operationalization** — триггер и применение.
- **Источник** — G3 2025 (полный текст в .cdp/scratch/PMC12060230.xml).

## Core Unit
- context:
  - ухаживание/песня: акустические компоненты, генетическая архитектура, популяционная дифференциация (5.1+6.2).
- signal:
  - вопрос «как устроена песня мухи», «есть ли генетическая/популяционная изменчивость песни», «роль в видообразовании».
- action:
  - использовать: 4 звука (sine, pulse, noise, other); 37 трейтов; **slow:total pulses — наибольшая дифференциация** (Zambia 0.833 vs France 0.725, P=0.007), QST > ~96.5% SNP (направленный отбор); **один сильный QTL 3R:20.0–22.6 Mb (42% различия)**, restrictive 3R:21.75–22.25 (Moehring & Mackay 2004 — ухаживание); кандидаты (ana1, slo, Nf1, gro, E(spl), CCAP-R, Cad96Ca, BRWD3, Dis3, fid, Fur1, jar, mld, ppk15, Rrp5); другие трейты: bouts/min (dlg1, Gr10b), pulse amplitude (Abd-B, Gr68a, mir-274/285/956, ple; residual — doublesex!), sine train (Ss), null-to-sine (btv, CheB42a, Gr33a/39a/43a/47a, jhamt, lig, Pal1, ppk25); 21 QTL для 6 трейтов; fast/slow mode — сенсорный (зрительный) выбор режима.
- outcome:
  - песня — полигенная, но с «сильным локусом» для дифференцированного трейта; популяции различаются по песне (QST>FST) — направленный отбор; кандидаты — известные гены ухаживания.
- lesson:
  - поведение (песня) имеет **генетическую архитектуру с сильными локусами** и **подвержено отбору** — для CASA: «врождённые программы» эволюционируют (изменчивость+отбор), что укрепляет «innate»-интерпретацию, но с вариацией.

## Fundamentals (самодостаточный опорный слой)

### 1) Акустика песни
- Sine song (непрерывный тон ~160-170 Гц), pulse song (импульсы ~30 мс, IPI ~30-70 мс); fast/slow pulse modes (Clemens 2018; частота/амплитуда различаются).
- Запись: 30 мин, SongExplorer (ML-сегментация), BatchSongAnalysis; 37 трейтов.

### 2) Популяционная дифференциация
- France (Lyon) vs Zambia (Siavonga): slow:total pulses 0.725±0.125 vs 0.833±0.067 (P=0.007, MW).
- QST vs FST: трейт > ~96.5% SNP — консервативная оценка направленного отбора.
- Другие: pulse mode preference, median pulse amplitude — популяционные различия (P=0.088/0.230 — слабее).

### 3) QTL-картирование (RIL FR320N × ZI418N)
- **Сильный QTL**: 3R:20.0–22.6 Mb, 42% родительского различия; restrictive 3R:21.75–22.25 (ранее: ухаживание Moehring & Mackay 2004); кандидаты (см. Core Unit).
- 21 значимых QTL для 6 трейтов; X-хромосома — редко (сексуально-антагонистический отбор?).
- Residual mapping: doublesex в QTL pulse amplitude (плейотропия между трейтами).

## Operationalization
- first_adoption_task: слой 5 (песня) + 6 (видообразование): генетическая архитектура/отбор; при CASA — «поведение = врождённое + эволюционно изменчивое».
- validation_check: цепи песни (P1 → motor) — карточка 1.5; другие виды (D. simulans и др.) — слой 6.
- success_criterion: карточка покрывает 5.1 (песня) + 6.2 (видообразование/изоляция) с полным текстом.
- rollback_or_mitigation: при пересмотре QTL — обновить.

## Lifecycle
- deprecation_reason: —

