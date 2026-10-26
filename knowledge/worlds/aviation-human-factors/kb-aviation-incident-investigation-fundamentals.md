---
type: KB
title: Aviation incident & accident investigation — fundamentals v1
description: '**Назначение:** почему авиационная культура расследования **сильнее типичного SE postmortem**; что переносить в platform/fleet ops и human+agent pair — без копирования регуляторики.'
tags: [aviation-human-factors, kb, worlds, investigation, annex-13, just-culture]
language: ru
world: aviation
subworld: human-factors
---
# Aviation incident & accident investigation — fundamentals v1


**Назначение:** почему авиационная культура расследования **сильнее типичного SE postmortem**; что переносить в platform/fleet ops и human+agent pair — без копирования регуляторики.

**Статус:** v1 · **Связь:** [`matrix-aviation-investigation-to-se-transfer.md`](matrix-aviation-investigation-to-se-transfer.md) · [`kb-reason-swiss-cheese-1990-evidence.md`](kb-reason-swiss-cheese-1990-evidence.md)

---

## 1. Одна строка

Авиация treats serious events as **system signals**: independent investigation, layered causation, recommendations with follow-up, and **Just Culture** — learn without default witch-hunt. SE often stops at «whose commit broke prod».

---

## 2. Почему в авиации это зрелее, чем в SE

| Измерение | Типичный SE | Авиация |
|-----------|-------------|---------|
| **Цель расследования** | Найти виновного / закрыть тикет | Предотвратить повтор; safety improvement |
| **Независимость** | Команда расследует себя | NTSB / AAIB / BEA / ICAO Annex 13 principles |
| **Глубина причин** | Root cause = один баг | Организация → надзор → предпосылки → действия (HFACS, Reason) |
| **Near-miss** | Часто не пишут | ASRS, mandatory reporting, LOSA |
| **Выход** | «Не повторять» в Slack | Формальные recommendations → AD/SB, training, procedure change |
| **Культура** | Blame postmortem (если есть) | Just Culture: error vs negligence |
| **Публичность** | NDA, internal only | Отчёты часто public (NTSB dockets) |

SE **импортировал куски** (Etsy/Google blameless postmortem, SRE incident review) — но без institutional teeth и без decades of practice.

---

## 3. Канон (что знать)

| Элемент | Суть |
|---------|------|
| **ICAO Annex 13** | Standards for aircraft accident/incident investigation — independence, sole objective safety |
| **NTSB (US)** | «No blame» statutory purpose for transportation safety |
| **Reason Swiss Cheese** | Accidents when holes in **layers** align — not one bad apple |
| **HFACS** | Human Factors Analysis Classification System — org/supervision/unsafe acts |
| **Just Culture** | Accountability matrix: human error, risky behavior, reckless |
| **TEM** | Threat and Error Management — proactive before catastrophe |
| **LOSA** | Line Operations Safety Audit — observe normal ops, no jeopardy |
| **ASRS** | Aviation Safety Reporting System — confidential near-miss reports |

---

## 4. Дух расследования (не процедура)

1. **Событие = данные**, не приговор личности.  
2. **Многослойность** обязательна — org policy, tooling, fatigue, communication, last act.  
3. **Speak up** до катастрофы — near-miss ценнее post-mortem.  
4. **Рекомендации** должны **менять систему** (procedure, training, design), не только «будь внимательнее».  
5. **Публичное обучение** — отрасль учится на чужих отчётах (читабельные NTSB narratives).

---

## 5. Связь с тремя столпами Guiders

| Столп | Investigation hook |
|-------|-------------------|
| **Aviation (pair)** | PM/PF: кто держал картину когда holes aligned; briefing after near-miss |
| **CASE (decision)** | Estate view: какие layers (Live/Fleet/Planet) совпали |
| **Agent Env** | Evidence log, journal — не «агент забыл», а trace для расследования |

---

## 6. Federation primitives (уже investigation-shaped)

| Aviation | Federation |
|----------|------------|
| Mandatory incident report | Pain inventory G-xxx / N-xxx |
| Safety recommendation | ADR + roadmap wave |
| Implementation tracking | Alliance row, conformance pin |
| Drift before crash | EICAS + **investigation layers** (Reason) |
| Independent review | Adoption drift CI; investigation ≠ self-review only |
| Public lesson | Constitution, generated alliance; NTSB-style narrative in ADR |

---

## 7. Границы переноса

- Не копировать legal Annex 13 в софт-команду.  
- Не «no blame» для repeated negligence.  
- Severity language нормализовать (не каждый bug — «катастрофа»).  
- См. `matrix-aviation-investigation-to-se-transfer.md`

---

## 8. Чтение

- ICAO Doc 9859 (SMS), Annex 13 summaries  
- NTSB investigation manuals (public)  
- Reason — *Human Error* (1990), Swiss cheese  
- Dekker — *Field Guide to Understanding Human Error* (critique + depth)  
- Sidney Dekker / Hudson Just Culture materials  

Evidence card: [`kb-reason-swiss-cheese-1990-evidence.md`](kb-reason-swiss-cheese-1990-evidence.md)

