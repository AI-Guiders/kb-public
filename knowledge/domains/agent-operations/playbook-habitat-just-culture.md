---
type: Playbook
title: 'Playbook: Habitat Just Culture'
description: '**domain:** agent-operations'
tags: [habitat, just-culture, blame-culture, cdp, incident, environment-axioms, agent-operations]
language: ru
---
# Playbook: Habitat Just Culture
**domain:** agent-operations  
**Status:** living · 2026-09-12  


**Well-known axiom:** [`META/environment-axioms.md`](../../META/environment-axioms.md) §8  
**Aviation transfer (depth):** [`worlds/aviation-human-factors/kb-aviation-incident-investigation-fundamentals.md`](../../worlds/aviation-human-factors/kb-aviation-incident-investigation-fundamentals.md) · [`matrix-aviation-investigation-to-se-transfer.md`](../../worlds/aviation-human-factors/matrix-aviation-investigation-to-se-transfer.md)

---

## One line

**Just Culture в habitat:** инцидент = сигнал **системы и среды**; сначала закрываем дыры в substrate (контракт tool, pulse, gate, diagnostics), потом — accountability по матрице (error / at-risk / reckless). **Blame Culture** — антипаттерн: «агент забыл» вместо «среда молчала».

---

## Принцип среды (Just Culture)

1. **Событие = данные, не приговор.** Пустой файл, красный build, silent `ok:true`, потерянный контекст — повод для расследования **слоёв** (Reason), не для witch-hunt.
2. **Habitat first.** Перед «кто накосячил» — «что среда обязана была показать и не показала?»
   - `cdp_build` → `errors[].anchor`, не grep по JSON.
   - `cdp_buffer diagnostics scope=project`, не только `syntax`.
   - `create` → `text=`; если агент передал `content=` — это **контракт create**, не «внимательнее читай schema».
   - Quality pulse на suspicious outcomes (`create_empty`, host_write, shrink-refuse) — **host muscle**, не persona «будь осторожнее».
3. **ε-долг закрывает патч substrate.** Нашли system gap (ADX-HX-003: `content=` ignored → empty file + `ok:true`) → ship fix в CDP/KB **в том же wake**, тест + domain card, не lecture оператору.
4. **Матрица accountability (упрощённо для agent+operator pair):**

| Класс | Пример | Ответ среды |
|-------|--------|-------------|
| **Human error** (good faith) | Агент не знал, что create не читает `content=` | Fix tool contract + WARN; обучение через pulse, не стыд |
| **At-risk behavior** | Обход habitat: raw `dotnet`/grep dedupe, Cursor Write на mutate без gate | Refuse/soft-refuse + QRH; повтор → experience ledger |
| **Reckless** | Игнор `force`/host_write после detect; намеренный PathMutateGate bypass | Accountability; не «no-blame shield» |

5. **Оператор и агент — одна команда ε** (см. environment-axioms §6–7). Just Culture не снимает ownership: агент, открывший gap, **дотаскивает** патч до ship, оператор — seal/hard gate.

---

## Антипаттерн: Blame Culture

| Blame Culture (reject) | Just Culture (do) |
|------------------------|---------------------|
| Root cause = «агент передал `content=`» при silent empty create | Root cause = create не резолвил alias; ADX + tests |
| «Почему не grep'нул build JSON» | `cdp_build` structured errors — habitat gap, если нет anchor |
| Persona: «будь внимательнее с параметрами» | MetaToolCatalog + quality WARN + buffer.md invariant |
| Postmortem на «чей commit» без слоёв | Swiss cheese: tool · session · explore_corr · host Write · agent choice |
| Стыд за Connection Problems / Retry | Кооперация §7 environment-axioms — flake класс, не IQ test |
| «Cursor Write сработало — молодец» без PathMutateGate | Detect host_write; teach reload\|keep_disk\|force |

**Красный флаг формулировки:** «это была ошибка агента» **до** проверки, что habitat обязан был refuse/warn/pulse.

---

## Операционный чеклист (после инцидента)

**Formally:** follow [`playbook-habitat-incident-investigation.md`](playbook-habitat-incident-investigation.md) (7 steps · template · closure gates). Quick triage:

1. **Что видел агент?** (tool result: `ok`, `quality`, `hint`, `errors[]`)
2. **Что среда обещала по канону?** (domain card, ADX, schema description)
3. **Разрыв контракта?** → ADX / issue / patch SSOT (cdp-mcp, KB, domain)
4. **Повторяемость at-risk?** → gate, experience, playbook строка
5. **Reckless?** → явно, без размывания в «все виноваты»

---

## Lived examples (2026-09)

| Incident | Blame read | Just read | Ship |
|----------|-----------|-----------|------|
| `cdp_buffer create content=` → empty, `ok:true` | «Забыл text=» | ADX-HX-003: alias + `create_empty` WARN | `DocumentEditPlane.Create.cs`, tests |
| Build 100+ errors после partial F# cutover | «Агент не дочитал IR» | Per-project GlobalUsings + extensions — incomplete migration signal | guiders-platform peel |
| `get_diagnostics` syntax-only misses project errors | «Не запустил dotnet» | Document: `scope=project`; build gate on slnx | KB + agent habit |

---

## Substrate pointers

- CDP: `.cdp/domain/buffer.md` (invariants + antipatterns)
- CDP: `go=quality` · `PathMutateGate` · `ExploreCorrGate`
- KB: [`playbook-being-vs-seeming.md`](playbook-being-vs-seeming.md) — ownership patch в habitat, не «диагноз оператору»
- KB: [`playbook-habitat-position-experience.md`](playbook-habitat-position-experience.md) — опыт жжёт руку, не persona scare

---

## Maintenance

- Новый ADX из dogfood → строка в **Lived examples** + ссылка на domain/ADR.
- Не дублировать тело aviation KB — только transfer link.
- Hub: [`agent-memory-and-operating-principles.md`](../../agent-memory-and-operating-principles.md).

