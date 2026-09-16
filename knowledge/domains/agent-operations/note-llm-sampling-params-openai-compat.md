# Note: LLM sampling params (OpenAI-compat) — temperature, top_p, …
**Tags:** #agent-operations #domains #note #llm #sampling #citizen

**Домен:** agent-operations / foundation-models  
**Статус:** living reference — не ADR  
**Дата:** 2026-08-01  
**Источник:** OpenAI Chat Completions API reference · CDP citizen wire (`CitizenCompletions.OpenAiCompat.cs`)

**Связь:** [playbook-rf-llm-cloudru-foundation-models.md](playbook-rf-llm-cloudru-foundation-models.md) · [playbook-agent-data-tiers.md](playbook-agent-data-tiers.md) · CIDE/CDP citizen · Cloud.ru FM OpenAI-compat

---

## Одна строка

**Sampling params** крутят, *насколько случайно* модель выбирает следующий токен. **`temperature=0`** — самый «холодный» обычный режим: почти greedy / максимальная детерминированность. Это **не** «выключено» и **не** гарантия бит-в-бит одинакового ответа на всех бэкендах.

---

## Зачем это нам (citizen wire)

Citizen на OpenAI-compat (Cloud.ru FM / GigaChat и т.п.) шлёт фиксированный payload:

| Поле | Значение у citizen |
|------|--------------------|
| `model` | из keys / settings |
| `max_tokens` | clamp **64…8192** |
| `temperature` | **`0`** (hardcoded) |
| `stream` | `false` |
| `messages` | system + turn |

Код: `cdp-mcp/CitizenCompletions.OpenAiCompat.cs`.

**Почему 0:** wire-контракт (`ONLY @intent go=…`) на маленьких FM ломается от «творчества». Холодный sampling = меньше вариаций формулировки → выше fidelity парсера.

Anthropic-path (`CitizenCompletions.cs`) шлёт `model` / `max_tokens` / `system` / `messages` — **без** `temperature` (дефолт провайдера).

**Не шлём сейчас:** `top_p`, penalties, `seed`, `n`, `logprobs`, `tools`.

---

## Карта параметров (Chat Completions / OpenAI-compat)

Диапазоны и имена — по канону OpenAI; Cloud.ru FM и другие compat-прокси обычно принимают тот же JSON, но семантика «0 = строго greedy» может чуть отличаться у вендора.

| Параметр | Типичный диапазон | За что отвечает |
|----------|-------------------|-----------------|
| **`temperature`** | 0…2 | «Температура» распределения: ниже → пики острее (часто выбирается самый вероятный токен); выше → больше разнообразия / риск бреда. Рекомендация вендоров: крутить **либо** temperature, **либо** `top_p`, не оба агрессивно. |
| **`top_p`** (nucleus) | 0…1 | Резать хвост: брать только токены, пока накопленная вероятность ≤ p. `1.0` ≈ весь словарь (в рамках других фильтров). Альтернатива temperature для контроля «ширины» выбора. |
| **`max_tokens`** / `max_completion_tokens` | >0 | Жёсткий потолок длины **ответа** (не контекста целиком). У citizen — clamp 64…8192. |
| **`frequency_penalty`** | −2…2 | Штраф за уже встречавшиеся токены → меньше повторов / зацикливания. |
| **`presence_penalty`** | −2…2 | Штраф за то, что токен **уже был** хотя бы раз → сильнее толкает в новые темы. |
| **`seed`** | int | Фиксация RNG (где поддержано) → ближе к воспроизводимости; не абсолютная гарантия между версиями модели / железом. |
| **`n`** | ≥1 | Сколько completion-кандидатов за один запрос (дорого). |
| **`stream`** | bool | SSE-дельты vs один JSON. Citizen: `false`. |
| **`stop`** | string[] | Ранняя остановка по строкам-триггерам. |
| **`logit_bias`** | map token→bias | Ручной сдвиг вероятностей конкретных токенов (редко, хрупко). |
| **`logprobs` / `top_logprobs`** | bool / 0…5 | Вернуть лог-вероятности (отладка / калибровка), не меняет sampling сам по себе. |
| **`tools` / `tool_choice`** | schema | Function calling — не sampling, но влияет на форму ответа. |

Docs: [OpenAI chat.completions.create](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create) (параметры `temperature`, `top_p` и др.).

---

## Интуиция: temperature = 0

1. Модель на каждом шаге имеет распределение P(token | context).
2. Sampling обычно: сэмплировать из softened распределения (temperature) и/или урезанного nucleus (`top_p`).
3. **`temperature → 0`:** распределение схлопывается к argmax → поведение близко к **greedy decode**.
4. На практике: одни и те же промпты дают **более стабильный** wire; всё ещё возможны отличия из‑за батчинга, обновления весов, discretisation float, другого дефолта `top_p` на стороне шлюза.

**Миф:** «0 = отключить randomness полностью и получить cryptographic replay».  
**Факт:** «0 = максимально предсказуемый *обычный* режим API».

**Миф:** «для креатива всегда temperature=1.5».  
**Факт:** для кода/wire/JSON чаще 0…0.3; для brainstorm — 0.7…1.0; выше 1.2 — осознанный риск.

---

## Когда крутить что

| Цель | Типичный ход |
|------|----------------|
| Парсимый wire / `@intent` / JSON schema | `temperature=0` (как citizen); не трогать `top_p` без нужды |
| Стабильные регрессии oracle | `temperature=0` + зафиксированный `seed` (если API даёт) |
| Разнообразие формулировок без полного хаоса | поднять `temperature` чуть (0.3–0.7) **или** снизить `top_p` (0.8–0.95), не оба сразу |
| Меньше повторов в длинном тексте | `frequency_penalty` > 0 |
| Выход из зацикливания темы | `presence_penalty` > 0 |
| Короткий жёсткий ответ | низкий `max_tokens` + persona/stop |

---

## Antipatterns

- Крутить temperature **и** top_p одновременно «наугад» — трудно отладить.
- Ждать bit-identical ответов от Cloud.ru / разных model id при `temperature=0`.
- Поднимать temperature на citizen wire ради «живее звучит» — ломает fidelity парсера.
- Путать `max_tokens` (лимит **генерации**) с размером контекстного окна модели.

---

## Stamp / verify

- Код citizen OpenAI-compat: hardcoded `temperature=0` (2026-08).
- После смены sampling на citizen — smoke: forced `ONLY @intent go=…` + unforced desk act; `tools/audit_*` по необходимости.
- Карточка живая: при появлении seed/top_p в payload — дописать сюда и в `.cdp/domain/citizen.md`.

