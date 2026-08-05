# Playbook: CIDE + Cloud.ru — harness parity vs Cursor (автоматизация first)
**Tags:** #agent-operations #domains #living #playbook


**Domain:** agent-operations  
**Версия:** 1 (draft / living)  
**Дата:** 2026-06-25  
**Provenance:** оператор (Света) + агент — post-Cloud.ru FM; «регулярные ритуалы не держу, автоматизировать что можно»

**Связь:**

- оплата / API — [`playbook-rf-llm-cloudru-foundation-models-v1.md`](playbook-rf-llm-cloudru-foundation-models-v1.md)
- threading — [`playbook-cursor-chat-threading-v1.md`](playbook-cursor-chat-threading-v1.md)
- checkpoint — [`playbook-context-pressure-checkpoint-v1.md`](playbook-context-pressure-checkpoint-v1.md)
- export — [`playbook-session-summary-and-chat-export-v1.md`](../worlds/agent-orchestration/playbook-session-summary-and-chat-export-v1.md)
- CIDE product — [`playbook-agent-execution-environment-v1.md`](../../work/projects/door-to-singularity/cascade-ide/playbook-agent-execution-environment-v1.md)
- product card — [`cascade-ide/README.md`](../../work/projects/door-to-singularity/cascade-ide/README.md)
- **норматив harness (репо)** — cascade-ide `docs/adr/0166-agent-centric-harness-model-comfort-and-pay-per-token-economics.md` (Proposed)
- **autonomous continuity** — [`playbook-autonomous-continuity-contract-v1.md`](playbook-autonomous-continuity-contract-v1.md) (сон ≠ простой; ~99% без оператора)

---

## Одна строка

**Cloud.ru = модель по API. Continuity = harness (CIDE/Roo + MCP + hooks/rules + артефакты). Оператору не полагаться — всё, что повторяется, в скрипт / hook / preset / agent rule.**

**Норматив harness (репо):** cascade-ide `docs/adr/0166-agent-centric-harness-model-comfort-and-pay-per-token-economics.md` — **«ничего о нас без нас»**; checklist §2.4; **§5.2 ADR vs код** — что ещё не в продукте.

---

## Принцип для Светы

| Плохо | Хорошо |
|-------|--------|
| «раз в час вспомни checkpoint» | hook / inject / ADCM pressure |
| «сама выбери модель tier» | `settings.toml` preset T1 |
| «не смешивай meta и epic» | **отдельный topic/чат** + brief template |
| «читай KB когда надо» | **in-proc** agent-notes ([0118](https://github.com/AI-Guiders/cascade-ide/blob/develop/docs/adr/0118-agent-notes-core-2-toml-and-knowledge-path.md)) + `read_hot_context` на старт |
| «сжимай контекст в голове» | **ADCM** (Prevent/Partition/Persist/Prune) — см. `playbook-agent-driven-context-management-v1.md` |

**Инвариант:** если шаг **>2 раз в неделю** и **детерминирован** — не дисциплина, а **автоматизация или agent obligation** (правило, которое агент выполняет без напоминания).

---

## Матрица parity

| # | Потребность | Cursor сегодня | CIDE + Cloud.ru | Авто? | Статус |
|---|-------------|----------------|-----------------|-------|--------|
| A1 | **LLM / оплата** | Pro legacy | FM API, `settings.toml` | setup once | 🔶 ключ + smoke |
| A2 | **Tools (roslyn, python, KB)** | отдельные stdio MCP | **in-proc** `ide_execute_command` + опц. external stdio | setup once | 🟢 §2.1 ниже |
| A3 | **Индекс кодовой базы** | hybrid-index MCP | **in-proc** `codebase_index_*` + `[hybrid_index]` | setup once | 🟢 in-proc |
| B1 | **Context pressure L1** | `.cursor/hooks/session_checkpoint_pressure.py` | `[agent.harness]` turns+msgs+usage % | dual-channel | 🟢 Cursor · 🟢 CIDE interim |
| B2 | **Pressure delivery** | `preCompact` / stop followup (Cursor) | visible tape + pending agent context (**ADCM**) | harness | 🟢 оба (разный механизм) |
| B3 | **Checkpoint export** | `Export-CursorJsonlTranscript.ps1` | CIDE `chat_export_readable` MCP | agent+tool | 🟡 оба есть |
| B4 | **Epic / spike / meta** | один чат → fork вручную | **Intercom topics / session tree** (product) | topics | 🟡 CIDE лучше, если пользовать |
| B5 | **Context management** | silent summary (плохо) | **ADCM** — agent tactics; не silent rewrite | playbook | 🟢 канон ADCM · 🔶 agent habit |
| B6 | **Verify / build** | терминал + MCP | **AEE ladder**, Verify Epoch | product | 🟢 CIDE лучше |
| B7 | **External memory** | KB MCP + scratch | то же | agent rule | 🟢 playbook |
| B8 | **Tier T1 / redaction** | data-tiers rule | то же + внутр. FM model id | preset | 🟢 playbook + toml |
| B9 | **Стоимость длинного контекста** | flat Pro | **pay-per-token** | meter в FM ЛК | 🟡 следить в ЛК |

**Легенда:** 🟢 закрыто · 🟡 частично · 🔶 сделать на забеге · 🔴 дырка

---

## Что уже автоматизировано (не трогать)

### Cursor (до ~2026-08-15)

- `PersonalCursorFolder/.cursor/hooks.json` → `session_checkpoint_pressure.py`
  - ≥40 user turns → inject агенту через **`additional_context`** (в UI чата **не видно**)
  - **`stop`** → **`followup_message`** с префиксом `[checkpoint hook]` — **видно** в ленте (auto-submit)
  - `preCompact` → **`user_message`** — видно только при summarization платформы

**Два канала (проверено оператором 2026-06-25):** `postToolUse` → только агент — итоги могли оставаться «внутренними», оператор не видел ни напоминание, ни ответ. `stop` → `followup_message` — **видно в ленте**; агент отвечает публично → checkpoint = shared artifact, не monologue. Первая видимая сработка ~1240 user turns; оператор: полёт и скорость сессии ок.

- `casa_dialogue_guard.py` — CASA edit guard (отдельный контур)

### KB / agent obligation (среда-независимо)

- Агент **обязан** предлагать checkpoint при pressure (playbook-context-pressure)
- Агент **обязан** fork meta/spike при lane switch (playbook-cursor-chat-threading)
- Агент **может** писать в KB/scratch без спроса при риске summary (playbook-external-memory)
- Агент **управляет** контекстом по ADCM (`playbook-agent-driven-context-management-v1.md`); harness только сигнализирует (dual-channel)

---

## Забег: минимальный автоматизируемый стек (MVP)

Порядок — **setup once**, дальше живёт сам.

### 1. Cloud.ru + CIDE model (A1, B8)

`%LocalAppData%\CascadeIDE\settings.toml`:

```toml
[ai.cloud]
active_provider = "openai"

[ai.cloud.openai]
base_url = "https://foundation-models.api.cloud.ru"
model = "Qwen/Qwen3-Coder-Next"
```

Ключ — CIDE ai-keys (ADR 0028). **Smoke:** один вопрос по несекретному `.py`.

### 2. Tool surface: in-proc vs external (A2, A3, B7)

**Факт (ADR 0166 §1.6):** в CIDE agent-notes, hybrid-index, debug, AEE, `ide_*` — **уже in-proc**. Отдельный `mcp.json` для них **не нужен**.

| Capability | Cursor | CIDE |
|------------|--------|------|
| KB / L0 / routing | agent-notes-mcp stdio | `read_knowledge_file`, `route_context`, `compact_hot_context` in-proc |
| Семантический поиск | hybrid-codebase-index stdio | `codebase_index_search` in-proc |
| Отладка | dotnet-debug-mcp | `debug_*` in-proc |
| Полный Roslyn (usages, solution diagnostics) | roslyn-mcp stdio | **опционально** тот же stdio в `[mcp] external_servers_json` |
| Python (CASA tests) | python-mcp stdio | **опционально** external stdio |
| IDE / verify | cascade-ide | хост (не второй контур) |

Шаблон optional external: `cascade-ide/docs/samples/harness-external-mcp.optional.json`  
Setup: `cascade-ide/scripts/setup/Setup-CideHarness.ps1 -Apply -AgentNotesConfigPath 'D:/agent-notes-mcp/agent-notes-mcp.toml'`

**Anti-pattern:** гонять весь `agents/von-neumann` store через chat.

**Cursor до ~Aug 2026:** `mcp.json` в Cursor по-прежнему для Composer; CIDE in-proc — для встроенного агента / `ide_execute_command`.

### 2.1 Smoke harness через MCP (CIDE)

**Да** — мониторинг и L0/verify smoke через `ide_execute_command` (см. `cascade-ide/docs/samples/harness-mcp-smoke.md`):

- `read_hot_context` — L0 загружен?
- `ide_agent_status` — `harness_*`, `verify_epoch_ui_stale`
- `ide_agent_verify` — после правки `.cs`

**Нет через MCP:** правка `[agent.harness]` — только `settings.toml` / `Setup-CideHarness.ps1`.

UI-only: checkpoint @40, ADCM pressure @60 msgs/topic (+ usage %), brief в composer на `/topic create`.

### 3. Mode preset + ADCM (B5)

**«CASA / Neumann T1»** — **политика harness**, не установка MCP:

- **in-proc:** KB, index, debug, verify (§2)
- **опц. external:** полный roslyn-mcp, python-mcp
- **ADCM:** pressure signals + agent obligations; `compact_hot_context` только как Prune hot; L0 — **`[agent.harness]`** on session/topic start (in-proc)
- model: `Qwen/Qwen3-Coder-Next` (Cloud.ru)
- topics: epic-fsr ≠ meta-tooling (§4)

**Interim (до UI preset):** overlay + `Setup-CideHarness.ps1 -Apply` + `[agent.harness]` в продукте.  
**Product (post-Aug):** именованный mode wizard.  
**Остаётся:** 0082 loopback HTTP, 0148 Verify Epoch UI, опц. P1.1 дешёвая модель для **явного** summary — ADR 0166 §5.2.

*(Точные ключи ai-mode — в репо cascade-ide; при расхождении побеждает репо.)*

### 4. Topics = автоматический fork (B4)

| Topic | Содержание | Не смешивать |
|-------|------------|--------------|
| **epic-fsr** | listen, life, ADR-0088, код payload | billing, Cloud.ru |
| **meta-tooling** | FM, CIDE setup, harness | колготки, store |
| **spike-*** | одна гипотеза, ≤1 сессия | — |

Новый spike → **новый topic**, 3 строки brief в первом сообщении (шаблон из playbook-cursor-chat-threading).

### 5. Checkpoint без оператора

| Слой | Кто делает |
|------|------------|
| **CIDE product** | `[agent.harness]` — L0; checkpoint @40; ADCM pressure @60 msgs / usage %; telemetry; `ide_agent_status` |
| **Agent rule** | в workspace rules CIDE/Cursor: «≥40 turns или смена epic → предложи export+checkpoint **без ждать просьбы**» |
| **Cursor** | hooks уже работают до августа |
| **CIDE backlog** | wizard «CASA/Neumann T1»; [0082](0082) loopback HTTP |

Агент **не** ждёт, пока Света «вспомнит про итоги».

---

## Backlog автоматизации (приоритет)

| P | Что | Где | Effort | Эффект |
|---|-----|-----|--------|--------|
| **P0** | Harness T1 overlay + smoke | `Setup-CideHarness.ps1 -Apply` | 30 min | harness policy; **ai.mode не трогает** |
| **P0** | Agent rule «checkpoint без спроса» | `.cascade-ide/maf-project-rules.md` + sample | done | см. `harness-maf-project-rules.sample.md` |
| **P0** | Harness MCP smoke doc | `docs/samples/harness-mcp-smoke.md` | done | ide_agent_status + read_hot_context |
| **P0** | Закоммитить hooks/rule в PersonalCursorFolder | parent repo | blocked | pre-commit cascade-ide slice |
| **P1** | ~~Скрипт Setup-CideHarness~~ | cascade-ide `scripts/setup/` | done | idempotent setup |
| **P1** | CIDE hook parity (turn count + pre-compact) | `[agent.harness]` | done | @40 turns + @60 msgs/topic |
| **P2** | Harness telemetry в agent context | minimized + `ide_agent_status` | done | P2.3 interim |
| **P2** | Roo path (VS Code) duplicate mcp + FM | альтернатива CIDE | 1 h | запасной harness |
| **P3** | Forge issue template «checkpoint» | forge | 30 min | ops memory |
| **P3** | `/loop` reminder checkpoint каждые N min | Cursor loop skill | opt-in | костыль, не канон |

**Не автоматизировать:** «понимание сюжета» фон Неймана — это **CASA store** (ADR-0088), не LLM context.

---

## Чеклист «готово к жизни без Cursor Pro»

```text
[ ] Cloud.ru ключ + баланс
[ ] Setup-CideHarness.ps1 -Apply + agent_notes.config_path
[ ] (опц.) Cloud.ru FM: `harness-cloud-fm.overlay.toml` + ai-keys — не нужно для mcp_only
[ ] (опц.) external MCP: roslyn + python — пути к exe в harness-external-mcp.json
[ ] Topic epic-fsr отделён от meta-tooling
[ ] Agent rule: checkpoint + fork lanes + read_hot_context на старт
[ ] Smoke MCP: `read_hot_context` + `ide_agent_status` (см. `docs/samples/harness-mcp-smoke.md`)
[ ] `.cascade-ide/maf-project-rules.md` из harness sample
[ ] (CIDE) `[agent.harness]` в settings — L0 + checkpoint + ADCM pressure + auto-verify
[ ] (После Aug) wizard T1 или 0082 loopback
```

---

## Roo vs CIDE (если CIDE не поднялся за вечер)

| | Roo + VS Code | CIDE |
|--|---------------|------|
| Setup | быстрее | CASA-native |
| Topics | слабее | Intercom tree |
| Verify ladder | ручной | AEE |
| MCP | да | да |
| Harness hooks | нет | backlog |

**Стратегия:** primary **CIDE**; Roo = **fallback harness** с тем же FM URL и тем же mcp.json.

---

## Связь с CASA / фон Нейман

| Контур | Инструмент |
|--------|------------|
| **Harness** (этот playbook) | CIDE, Cloud.ru, MCP, hooks, KB |
| **Habitat** (life, episodic) | `agents/von-neumann`, ADR-0088, life tick |

Cloud.ru **не** заменяет hippo quad-mode. Два параллельных трека на забеге — нормально.

---

## История

| Дата | Change |
|------|--------|
| 2026-06-25 | v1: parity matrix, automation-first, MVP checklist |
| 2026-06-28 | preCompact @60 msgs; telemetry in MAF context; MCP smoke doc; P1.2 brief template |
| 2026-07-18 | ADCM канон: pressure dual-channel; не silent chat rewrite; `compact_hot_context` = Prune hot |

