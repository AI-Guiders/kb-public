---
type: Playbook
title: 'Playbook: LLM-агент из РФ через Cloud.ru Foundation Models'
description: '**Домен:** agent-operations'
tags: [agent-operations, domains, living, playbook]
language: ru
---
# Playbook: LLM-агент из РФ через Cloud.ru Foundation Models


**Домен:** agent-operations  
**Дата:** 2026-06-25  
**Provenance:** диалог оператор (Света) + агент — Cursor; поиск обхода Stripe/KZ; находка тарифов FM  
**Секция hot (stub):** загрузка по hub / route_context «Cloud.ru / Foundation Models / РФ / Roo / оплата рублями»

**Связь:** [playbook-agent-data-tiers.md](playbook-agent-data-tiers.md) · [playbook-cursor-chat-threading.md](playbook-cursor-chat-threading.md) · [note-llm-sampling-params-openai-compat.md](note-llm-sampling-params-openai-compat.md) · CIDE `settings.toml` `[ai.cloud.openai]` · [Cloud.ru FM quickstart](https://cloud.ru/docs/foundation-models/ug/topics/quickstart)

---

## TL;DR

**Для агентной работы из РФ без foreign card / KZ / VPN (API):**

1. **Cloud.ru** → Evolution → **Foundation Models** → API-ключ, баланс **рублями** (карта РФ).
2. **VS Code** → расширение **Roo Code** → провайдер **OpenAI Compatible**, base URL `https://foundation-models.api.cloud.ru/v1`.
3. Модель по tier: **`Qwen/Qwen3-Coder-Next`** (внутренняя, код в контуре Cloud.ru) или внешняя Claude/GPT через FM (код уходит к вендору).

Официальная инструкция: [Подключение Foundation Models в VS Code](https://cloud.ru/docs/foundation-models/ug/topics/tutorials__connect-vscode).

**KZ + ChatGPT Plus / Codex CLI** — **опциональный** путь для нативной подписки OpenAI, **не** блокер для агентного кодинга.

---

## Что это

[Evolution Foundation Models](https://cloud.ru/products/evolution-foundation-models) — каталог LLM и AI-моделей Cloud.ru:

- **OpenAI-совместимый API:** `https://foundation-models.api.cloud.ru/v1`
- **Pay-as-you-go** в рублях ([тарифы EVO.11.2](https://cloud.ru/documents/tariffs/evolution/foundation-models), редакция от **2026-06-24**)
- **Function calling, reasoning, vision** — на поддерживаемых моделях ([каталог](https://cloud.ru/docs/foundation-models/ug/topics/overview__available__models))

Два класса размещения (важно для tier):

| Размещение | Смысл | Примеры model id |
|------------|--------|------------------|
| **Внутренняя** | инференс в инфраструктуре Cloud.ru; данные **не** уходят к зарубежному вендору | `Qwen/Qwen3-Coder-Next`, `zai-org/GLM-4.7`, `GigaChat/GigaChat-2-Max` |
| **Внешняя (партнёрская)** | прокси к API Anthropic / OpenAI / Google и др. | `anthropic/claude-sonnet-4.6`, `openai/gpt-5.3-codex`, `openai/chatgpt-4o-latest` |

---

## Быстрый путь: VS Code + Roo Code

Минимум квестов; Cloud.ru документирует именно его.

| Шаг | Действие |
|-----|----------|
| 1 | ЛК Cloud.ru → **Foundation Models** → создать **API-ключ** |
| 2 | Пополнить баланс (рубли, карта РФ) |
| 3 | VS Code → Extensions → **Roo Code** |
| 4 | Roo → Настройки: **OpenAI Compatible**, URL `https://foundation-models.api.cloud.ru/v1`, ключ, **model id** |
| 5 | Smoke: короткий вопрос по коду на **несекретном** файле |

Опционально: индексация проекта в Roo — эмбеддер `Qwen/Qwen3-Embedding-0.6B`, тот же base URL ([туториал](https://cloud.ru/docs/foundation-models/ug/topics/tutorials__connect-vscode)).

**Поддержка:** Cloud.ru **не** поддерживает Roo Code; вопросы по расширению — к разработчикам Roo.

---

## Альтернатива: CascadeIDE (CIDE)

Тот же API без Roo — в `%LocalAppData%\CascadeIDE\settings.toml`:

```toml
[ai.cloud]
active_provider = "openai"

[ai.cloud.openai]
base_url = "https://foundation-models.api.cloud.ru"
model = "Qwen/Qwen3-Coder-Next"
```

API-ключ — в `ai-keys` (см. CIDE ADR 0028). Провайдер `OpenAiCompatibleProvider` + MAF-агент с `ide_execute_command` (встроенный MCP).

**Когда CIDE vs Roo:** CIDE — CASA/Neumann, roslyn/dotnet-debug нативно, FieldBus parity; Roo — быстрее «поставил и работает» в привычном VS Code.

---

## Выбор модели (ориентир цены, с НДС / 1M токенов)

Снимок тарифа **2026-06-24**; актуальность — [тарифный лист](https://cloud.ru/documents/tariffs/evolution/foundation-models).

| Model id | Вход | Выход | Когда |
|----------|------|-------|--------|
| `Qwen/Qwen3-Coder-Next` | ~122 ₽ | ~244 ₽ | **T1 coder**, проприетарный CASA |
| `anthropic/claude-haiku-4.5` | ~196 ₽ | ~982 ₽ | дешёвый внешний диалог |
| `anthropic/claude-sonnet-4.6` | ~589 ₽ | ~2946 ₽ | архитектура / сложный код (внешняя) |
| `openai/gpt-5.3-codex` | см. тариф | см. тариф | Codex-class через API, не CLI |

При активном agent-loop следить за **счётчиком токенов**; Sonnet/Opus быстро обгоняют flat **$20/mo**, если гонять длинный контекст каждый ход.

---

## Связка с tier (T0–T3)

См. [playbook-agent-data-tiers.md](playbook-agent-data-tiers.md).

| Tier | Cloud.ru FM |
|------|-------------|
| **T1** | **внутренние** модели (`Qwen3-Coder-Next`, GLM-4.7, GigaChat) — CASA, agent-notes, open ADR |
| **T3** | **внешние** через FM (Claude/GPT) — как прямой API вендора; код уходит за рубеж |
| **Не нужен FM** | T0 (только человек) |

**Anti-pattern:** гонять `agents/von-neumann` store через **внешнюю** Sonnet «потому что удобно».

---

## Что этот путь **не** заменяет

| Потребность | FM + Roo/CIDE | Нужен отдельно |
|-------------|---------------|----------------|
| Агент с tools в IDE | ✅ Roo MCP / CIDE ide-mcp | настроить `mcp.json` |
| Оплата рублями | ✅ | — |
| **Нативный Codex CLI** (`codex login` + Plus) | ❌ | KZ card / посредник / App Store |
| **Cursor Auto** в чате Cursor | ❌ | Cursor Pro до ~2026-08-15, затем Roo/CIDE/Claude trial |
| Локальный GLM-5 / 70B без облака | ❌ | своё железо / Ollama |

---

## Стратегия после legacy Cursor Pro (~2026-08)

```text
До августа:     Cursor (как есть) + опционально trial Cloud.ru FM
После августа:  VS Code + Roo + Cloud.ru  ИЛИ  CascadeIDE + тот же API
Резерв:         KZ + Plus — только если нужен именно chat.openai.com / Codex subscription UX
Almaty / ФНС:   только при открытии **счёта в KZ-банке** (не для FM API)
```

Fork тредов и handoff — [playbook-cursor-chat-threading.md](playbook-cursor-chat-threading.md).

Harness parity и автоматизация (не полагаться на ритуалы оператора) — [playbook-cide-harness-parity-vs-cursor.md](playbook-cide-harness-parity-vs-cursor.md).

---

## Обязанности агента

- при вопросе «как платить из РФ» — **сначала** этот playbook, не разворачивать KZ-эпос без запроса на нативный OpenAI;
- для **casa-ontology-payload** по умолчанию предлагать **внутреннюю** coder-модель FM;
- фиксировать **дату проверки тарифов**, если цитируем цифры;
- не коммитить API-ключи в git.

---

## Канон

`knowledge/domains/agent-operations/playbook-rf-llm-cloudru-foundation-models.md`

