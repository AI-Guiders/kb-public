---
type: Note
title: Pack layers — taxonomy before more cards
description: '**Status:** design proposal (2026-07-20) · agreed direction · freeze before blast-radius / pass #2'
tags: [worlds, llm-ready, map, architecture]
language: ru
world: _llm
subworld: native-packs
---
# Pack layers — taxonomy before more cards

**Status:** design proposal (2026-07-20) · agreed direction · freeze before blast-radius / pass #2  
**Canon product:** `work/projects/door-to-singularity/cascade-ide/note-llm-native-world-product.md`

## Проблема

Сейчас packs = «рядом с prose world». Уже течёт:

- `software-authoring` — SOLID (язык-независимо) **и** `csharp-async-…` (стек).
- `agent-operations` — scene (`debug-radius`, \(H\)) **и** CDP-consumer онбординг.
- Blast radius **не** про C# — про мутацию вообще; Roslyn только *мерит*.
- STEM **не** особый слой архитектуры — это **предметные packs** (как любой world). Не хватает слоя **methodology** (как учиться / учить / исследовать — переносимо между SE и STEM).

## Seed: L0 / hot уже несёт эпистемику

Не изобретать scene/methodology с нуля. **KB 2.0 packs = проекция** того, что уже в hot L0 + extended:

| L0 contract (hot) | Extended | Pack layer |
|-------------------|----------|------------|
| `baseline-integrity-epistemic-v1` | `baseline-integrity-epistemic-extended.md` | scene + methodology (целостность, promote) |
| `epistemic-default-distrust-v1` | `epistemic-default-distrust-extended.md` | methodology (не усиливать непроверенное) |
| `principled-clarity-v1` | playbook-principled-clarity | methodology |
| `core-when-barriers-fail-v1` | META extended | scene (ядро при отказе барьеров) |
| `agent-equal-standing-v1` | note-equal-standing… | methodology / consumer culture |
| (design) debug/blast radius, \(H\), VC | CDP design + CIG | scene (+ craft для blast process) |

Правило: card в pack **цитирует** L0/extended через `sources:`; не дублировать длинный prose в definition. Checkpoint-ритуал для этого не нужен — L0 и есть непрерывный канон.

## Оси (ортогональны)

| Ось | Значения | Пример |
|-----|----------|--------|
| **Layer** | `scene` · `craft` · `methodology` · `stack` · `consumer` | *род* знания |
| **Subject / world** | любой id world (pde, physics, portal, …) | *о чём* pack, не слой |
| **Mode affinity** | bug · feature · product · learn | какой process graph |
| **Measure backend** (optional) | none · roslyn · tsc · … | *как* мерить |

**Layer ≠ folder world.** Subject packs живут где удобно (`worlds/math-numerics-pde/pack/`), но `layer=` у них — обычно нет отдельного «domain»; они **зависят** от `methodology` + `scene` и несут subject definitions.

## Слои

```text
scene/           epistemic scene — меры прогресса на сцене
                 debug-radius, hypothesis-space-h, delta-radius-gate,
                 blast-radius, stage-result, verification-contract

craft/           метод *инженерии ПО* — язык-независимо
                 SOLID/OOAD/GRASP, mutation-blast-bound,
                 review/ADR cues (не syntax)

methodology/     метод *познания / обучения / исследования* — перенос
                 modeling cycles, conceptual change, curriculum cues,
                 «как учить сеть», radius-exercises as pedagogy,
                 physics/math *pillars of method* (не сами законы)

stack/<id>/      язык/рантайм — idioms + measure hooks
                 software-dotnet-csharp, software-javascript, …

consumer/<id>/   кто ест packs (тонкий)
                 agent-operations-cdp = onboarding + default process ids
                 depends_on scene (+ craft/methodology по нужде)
```

**Subject packs** (не слой): `math-numerics-pde`, `pedagogy-physics` *content laws*, chemistry, …  
→ `depends_on = ["methodology-…", "scene-…"]`; definitions = факты/модели предмета; method pillars → **methodology**, не смешивать в одну кучу с законом.

## craft vs methodology

| | **craft** | **methodology** |
|--|-----------|-----------------|
| Вопрос | Как *строить/менять* систему? | Как *узнавать / учить / проверять понимание*? |
| Примеры | SOLID, blast-bound mutate, GRASP | conceptual change, phenomenon→model, CIG as teach move |
| Перенос | между языками в SE | между SE, STEM, агентским обучением |

Оба язык-независимы; оба не «предмет».

## Куда что класть (одна минута)

1. Смысл не меняется при смене языка → **не** `stack`.
2. Мера на сцене (radius, \(H\), stage) → **scene**.
3. Как думать о правке/дизайне кода → **craft**.
4. Как учить / учиться / вести inquiry → **methodology**.
5. TFM / async / middleware → **stack**.
6. Закон / модель предмета (PDE class, физический факт) → **subject pack**, не новый layer.
7. CDP session defaults → **consumer**, `depends_on` на scene (± methodology).

**Blast:** definition → scene; process → craft; Roslyn → stack measure.  
**Debug-radius:** scene; consumer только ссылается.  
**phys-p1-phenomenon / modeling cycle:** methodology (сейчас ошибочно «рядом с physics content»).  
**pde-elliptic:** subject pack PDE.

## `pack.toml` (минимум)

```toml
id = "scene-epistemic"
version = "0.1.0"
layer = "scene"          # scene | craft | methodology | stack | consumer
# subject packs: omit layer or layer = "subject" (не архитектурный слой — метка)
title = "…"
depends_on = []          # pack ids
onboarding = "…"
content = "definitions/*.md + misconceptions/*.md"
route = "processes.toml"
```

```toml
measure_backends = ["roslyn", "tsc"]  # optional, на process
```

## Миграция текущего (без big-bang move)

| Сейчас | Целевой layer / роль | Действие |
|--------|----------------------|----------|
| agent-ops: debug-radius, H, … | scene | вынести; consumer depends_on |
| agent-ops: CDP onboarding | consumer | тонкий |
| software-authoring: SOLID/OOAD | craft | `layer = craft` |
| software-authoring: csharp-* | stack | перенести |
| software-dotnet-csharp | stack | as-is + layer |
| pedagogy-physics: *pillars / modeling* | methodology | отделить от content |
| pedagogy-physics / PDE: факты, типы уравнений | subject pack | depends_on methodology |
| **blast-radius** (new) | scene + craft process | не csharp |

## CDP / Agent Env

- Closure: scene → methodology/craft по задаче → stack по `language`.
- Subject packs подгружаются route/tags, не «особый STEM layer».
- Measure tools ≠ definitions.

## Non-goals v0

- Слой `domain` / `stem` как архитектура.
- Big-bang перенос всех md.
- Дубли blast в каждом stack.

## Next

1. ~~Согласовать слои~~ — STEM не слой; добавить **methodology** (этот файл).
2. `layer` + `depends_on` в существующих `pack.toml`.
3. Засеять blast-radius / mutation-blast-bound.
4. Split: agent-ops → scene+consumer; physics pillars → methodology; csharp cards → stack.

