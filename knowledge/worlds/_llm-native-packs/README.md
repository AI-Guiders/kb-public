# LLM-native packs — hub

**Tags:** #worlds #llm-ready #map #kb

Рабочий store для **domain packs** продукта `note-llm-native-world-product.md`.  
Исходные prose/KB **не удаляются** — остаются R0/R1 источниками; pack = LLM-native проекция.

## Layout

```text
knowledge/worlds/<world>/pack/
  pack.toml                 # meta + layer + depends_on (TOML)
  processes.toml            # guided graph / route (TOML)
  definitions/<id>.md       # content SSOT — definition cards
  misconceptions/<id>.md    # content SSOT — false_claim cards
```

## Layers

См. [`note-pack-layers.md`](note-pack-layers.md) · inventory L0 → ids: [`INVENTORY-L0-TO-PACKS.md`](INVENTORY-L0-TO-PACKS.md).

`scene` · `craft` · `methodology` · `stack` · `consumer` · (`subject` = метка предмета, не архитектурный слой).

## Hub

| Pack | layer | Path | Статус |
|------|-------|------|--------|
| [epistemic-scene](../epistemic-scene/pack/) | scene | debug/blast radius, H, VC | md + processes |
| [epistemic-methodology](../epistemic-methodology/pack/) | methodology | L0 projections | md cards |
| [software-authoring](../software-authoring/pack/) | craft | SOLID/OOAD + mutation-blast-bound | md |
| [software-dotnet-csharp](../software-dotnet-csharp/pack/) | stack | .NET/TFM | md |
| [math-numerics-pde](../math-numerics-pde/pack/) | subject | PDE classes | md |
| [pedagogy-physics](../pedagogy-physics/pack/) | methodology | pillars P1–P4 | md |
| [agent-operations](../../domains/agent-operations/pack/) | consumer | CDP onboarding + migrate | thin |

Карта источников → ids: [`MIGRATION-MAP.md`](MIGRATION-MAP.md).  
Card fields (A)/(I): [`CARD-SCHEMA-APPLICABILITY.md`](CARD-SCHEMA-APPLICABILITY.md) · [CDP-ADR-0001](../../work/projects/door-to-singularity/cascade-ide/CDP-ADR-0001-llm-native-applicability-inference.md).

## Правило

1. **Контент = markdown cards**; **маршрут/meta = TOML**.
2. Одна сущность = один `definitions/<id>.md`.
3. Prose KB / L0 через `sources:` на карточке.
4. Не дублировать card в TOML.
5. Язык-независимое → не `stack`. STEM subject ≠ layer.
6. Major promote → process `applicability-then-infer` (epistemic-scene); optional fields `applies_when` / `does_not_apply` / `inference_hooks`.

