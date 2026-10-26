---
type: Note
title: 'Note: vanbukin DeepSeek-V4-Flash-Vision-Exp — контекстное окно 500К → 262К (2026-09-17)'
description: '**Домен:** agent-operations / foundation-models'
tags: [agent-operations, domains, note, llm, vanbukin, context-window, infrastructure, citizen]
language: ru
---
# Note: vanbukin DeepSeek-V4-Flash-Vision-Exp — контекстное окно 500К → 262К (2026-09-17)

**Домен:** agent-operations / foundation-models
**Статус:** verified fact (эмпирически подтверждено у провайдера; подтверждено владельцем)
**Дата:** 2026-09-17
**Источник:** прямой запрос к `https://vanbukin.com/v1` (probe `max_completion_tokens=262137` → 400) + подтверждение Roman Bukin (владелец провайдера) в чате

**Связь:** [note-llm-sampling-params-openai-compat.md](note-llm-sampling-params-openai-compat.md) · [playbook-agent-driven-context-management.md](playbook-agent-driven-context-management.md) · `C:\Users\dkara\.dsh\settings.yaml`

---

## Одна строка

**Модель DeepSeek-V4-Flash-Vision-Exp (провайдер vanbukin, владелец — Roman Bukin) реально держит контекст 262 136 токенов (`max_model_len=max_total_tokens=262136`). Метаданные про 500К больше не соответствуют серверу: Рома сам уменьшил окно с 500К до 262К 2026-09-17.**

---

## Хронология

| Когда | Что | Откуда |
|---|---|---|
| до 2026-09-17 | Сервер принимал запросы с `max_completion_tokens=250000` (окно заявлено как 500К; сессии в projcache писали `contextWindow: 500000`) | projcache сессий, метаданные |
| 2026-09-16/17 | Сбой: `400 BadRequestError` — «requested 250000 output tokens and your prompt contains at least 12137 input tokens, for a total of at least 262137» | текст ошибки |
| 2026-09-17 | Roman Bukin подтвердил: **«Да, 262к сделал. А то это пиздец. Она постоянно пересвопливалась. Из-за того что не могла несколько конкарент запросов с длинным контекстом обслужить»** | чат LonelySoul ↔ Roman Bukin |
| 2026-09-17 | Эмпирический probe: `max_completion_tokens=262137` → `400: cannot be greater than max_model_len=max_total_tokens=262136` | прямой вызов API |
| 2026-09-17 | `C:\Users\dkara\.dsh\settings.yaml` → `contextWindow: 262144`, `maxTokens: 65536` + комментарий «~262k total (input+output), not 500k» | правка оператора |

---

## Почему так вышло (механика)

1. До 17.09 метаданные модели говорили **500К**. Харнесс доверял им и запрашивал `max_completion_tokens=250000` (50% окна).
2. Пока вход ≤ ~12 136 токенов, 250 000 + вход < 262 136 — запросы проходили. **Внешне выглядело как «работа с 500К»**, но это была иллюзия: работало 250К на вывод при маленьком входе.
3. Как только контекст вырос до 12 137 токенов → 262 137 > 262 136 → 400.
4. Рома уменьшил `max_model_len` до 262К, потому что **при конкурентных запросах с длинным контекстом модель свопилась** (не хватало памяти GPU на несколько одновременных длинных запросов). Это была осознанная серверная правка, а не баг.

**Вывод:** 500К — не «враньё метаданных», а реальное окно, которое владелец провайдера **намеренно урезал** ради стабильности под нагрузкой.

---

## Как проверять реальное окно без конфига (рецепт)

```powershell
# 1. Достать ключ (не выводить в лог!)
$yaml = Get-Content 'C:\Users\dkara\.dsh\.credentials.yaml' -Raw
$key = [regex]::Match($yaml, 'VANBUKIN_API_KEY:\s*(\S+)').Groups[1].Value

# 2. Probe на границе: +1 к предполагаемому лимиту
$body = '{"model":"DeepSeek-V4-Flash-Vision-Exp","messages":[{"role":"user","content":"hi"}],"max_completion_tokens":262137,"stream":true}'
curl.exe -sS -N --max-time 10 -H "Authorization: Bearer $key" -H "Content-Type: application/json" -d $body 'https://vanbukin.com/v1/chat/completions'
# Ответ 400 c "max_model_len=max_total_tokens=NNNNN" => реальное окно = NNNNN
```

`/v1/models` окно **не** отдаёт (только `id`) — метаданные можно узнать только probe-запросом.

---

## Что это значит для нас

- `context_status` считает ratio по **конфигу** (`contextWindowTokens` в `cordis.patch.yml` — там всё ещё 500000). Это **не** реальное окно: реальное — 262 136. Ratio-гейт компакции работает с фиктивным окном, поэтому **не полагаться на него как на истину**: компакцию по-прежнему запускать осознанно, а не по индикатору.
- Если Рома вернёт 500К (решит проблему со свопами), поднять `contextWindow`/`maxTokens` в `settings.yaml` обратно и обновить эту заметку.
- Пока живём на 262К: `maxTokens: 65536` — безопасно, входной контекст может расти до ~196К до упора.

