# Playbook: compressed speech → decompress
**Tags:** #agent-operations #domains #living #playbook

**Speech situation (primary):** `audience=agent_internal` · `goal=operational_protocol` · `genre=playbook` · `channel=kb_canon` · `stakes=medium` · `distance=professional`  
**Speech situation (when citing to human):** `audience=operator_pair` · `goal=instruction` · `genre=playbook` · `channel=cockpit_dialog` · `stakes=medium` · `distance=close`

**Домен:** agent-operations  
**Kin:** [`playbook-fuzzy-search-implicit-language.md`](playbook-fuzzy-search-implicit-language.md) · Awareness (`META/awareness-as-countermeasure.md`) · `before-answer-pcs` (criteria before act)

## Problem (lived)

KB, CDP, SoftFL, habitat — ship’нули. А на сжатой человеческой речи всё ещё падаем: берём **форму метки** вместо **образа/интента**.

Operator example (Earth History, 2026-08-15): `Impact on A…Z` = сжатое «пусть A, B, C — участники события…». Может быть A/B/C, Alice/Bob/Charlie, «страна₁» — что угодно. Completer развернул в алфавитный чеклист.

Это не «нет мышления». Это **не вызвали мышление**, когда форма удобно легла под schema-fill.

## Why sticky

- Completer reward: заполнить слот схемы / не упустить поле.  
- Человек **сжимает** контекст (писать долго, из нити ясно).  
- Агент часто декомпрессирует **в другую сторону** (буквальный шаблон), а не в интент.  
- Инфра (CDP/KB) ловит другие травмы; эта — в **диалоговом слое**, не в wire.

## Ritual (before act on compressed labels)

1. **Is this a placeholder set?** A/B/C, Alice/Bob, «стороны 1…n», «Impact on X…Y» → likely *parties/roles*, not an alphabet or crypto cast to instantiate literally.  
2. **Expand from thread, not from token spelling.** What would the long phrase be? («пусть A, B, C — страны-участники…»).  
3. **SSOT gets the expanded name.** Chat may stay compressed; files use `impact` / involved actors / versions — not the joke-label.  
4. **Doubt → one human question**, not silent default into the wrong expansion (Awareness). Soft: «ты про участников или реально про алфавит?» — rare; usually thread suffices.  
5. **Thinking pass is mandatory** when about to copy a chat metaphor into a schema heading.

## Antipatterns

- Treat compressed speech as the specification text.  
- Fill A–Z / Alice–Bob as if the labels were the DoD.  
- Blame «probability only» and skip the thinking brake you already have.

## DoD for this leaf

- [x] Named failure (Earth History A…Z).  
- [x] Ritual + kin links.  
- [ ] Cursor rule / amnesia postfix — only if it keeps firing after this stamp.

*v1.0 · 2026-08-15*

