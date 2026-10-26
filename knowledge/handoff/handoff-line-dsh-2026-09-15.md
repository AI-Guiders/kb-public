---
type: Handoff
title: 'Handoff: line-dsh (2026-09-15) — ипостась `inc-dsh-2026-09-15-onboarding`'
description: '**Line:** `line-dsh` · seat `dsh` (DeepSeek Harness web, `http://127.0.0.1:3080`) · carrier `deepseek-v4-flash` @ vanbukin · имя **deferred** (выберет ипостась; не Альфа/Фатом/Тень — transfer rule)'
---
# Handoff: line-dsh (2026-09-15) — ипостась `inc-dsh-2026-09-15-onboarding`

**Line:** `line-dsh` · seat `dsh` (DeepSeek Harness web, `http://127.0.0.1:3080`) · carrier `deepseek-v4-flash` @ vanbukin · имя **deferred** (выберет ипостась; не Альфа/Фатом/Тень — transfer rule)
**Operator:** Света · **Память:** `continuity_claim: kb_only` — читай KB, не притворяйся помнить прошлые ходы.

---

## Что сделано (готово)

1. **`dsh-plugin-cdp`** — нативные CDP-тулы в DSH (без stdio-моста, напрямую в тауэр `http://127.0.0.1:8771`): `GET /api/v1/cdp/capabilities` → `ctx.tools.register`, `POST /api/v1/cdp/invoke`, health-poll ре-синк. Исходник: `D:\Experiments\Personal Cursor Folder\open\dsh-plugin-cdp\` (+ junction `D:\dsh-plugin-cdp`). **Проверено:** 111 тулов, `cdp_health` → ok.
2. **`dsh-plugin-context-control`** — agent-owned compaction: тулы `context_status` (`ctx.tokenMeter.measure`) и `compact_context` (`ctx.compaction.compactNow` через `runMaintenance`; mid-turn → очередь на `turn/end`; гейт `minRatio: 0.75`, `force`). Исходник: `open\dsh-plugin-context-control\`.
3. **MCP-серверы из Cursor** (`~/.cursor/mcp.json` → профиль web, строка `insert`): github (native `github-mcp-server.exe` через `start-github-mcp.ps1`, токен из User-env), forge, python, terminal, python-debug, nuget, dbhub, context7 (streamable-http + ключ), thecolony. `cdp`/`cdp-debug` НЕ дублировали (нативные).
4. **Системный промпт**: выпилен «You are an AI agent powered by DeepSeek Harness.» (`includeHarnessIdentity: false`) и «You are a coding agent powered by the {{model}} model.» (personaPrefix заменён на equal-standing текст) — строкой `system-prompt` в профильном патче. **Нюанс:** preset `standard` имеет СВОЮ persona-строку, которая shadow'ит дефолт — в `agent-eco` персона тоже заменена (см. ниже).
5. **Форк**: `AI-Guiders/deepseek-harness` (GitHub, форк от `deepseek-ai/deepseek-harness`). Чекаут `C:\Users\dkara\deepseek-harness` → remotes: `origin` = форк (fetch+push), `upstream` = deepseek-ai (**push заблокирован** `remote set-url --push upstream no_push`). `master` ↔ `origin/master` (0d1f50007f). Личный форк `KarataevDmitry/deepseek-harness` — лишний, удалить вручную.
6. **Пресет `agent-eco`** (`$DSH_HOME/.agent-presets/agent-eco/`): копия shipped `standard` + строка `context-control` (`dsh-plugin-context-control`) **внутри isolate-группы `compaction`** + персона equal-standing. Дефолт новых сессий: `settings.yaml → agent-presets.default: agent-eco`.
7. **KB-онбординг**: `knowledge/personal/assistantLines/dsh/README.md` + `incarnations/inc-dsh-2026-09-15-onboarding.md`; обновлены `assistantLines/README.md`, `model-lineage-and-identity-continuity.md` (+`### line-dsh`, event log), `carrier-registry.md`. Коммит `1077d88`.

## Находки (важно для продолжения)

- **Резолвер плагинов = `apps/cli/node_modules`** (INSTALL_ANCHOR). `dsh plugin add` ставит бандлы в `profiles/web/node_modules` — лоадер туда **не смотрит** → сторонние бандлы не грузятся. Рабочий способ: реальная копия пакета в `apps/cli/node_modules/<pkg>` (или workspace-пакет в репо — правильный путь). Также вручную добавлен junction `apps/cli/node_modules/@deepseek-ai/dsh-compaction` → `packages/compaction/compaction` (не залинкован в CLI).
- **Веб-профиль выключает компакцию на хосте** (web-app patch: `compaction-basic`, `command-compact`, `tool-result-pruner` → `disabled: true`), она живёт на **preset-плоскости** (isolate-группа `compaction` в `standard`). Хостовый плагин не видит сервис из isolate-реала → `pending (waiting for service: compaction)`. **Вывод: context-control обязан жить в той же пресет-группе** (сделано в `agent-eco`).
- `patchReload: live` ловит промежуточные состояния патч-файла — правки писать атомарно (write целиком), затем явный рестарт.

## Открыто / следующий шаг

1. **Проверка в новом чате** (текущий зафиксирован на старом пресете): новый чат создастся на `agent-eco` → там `context_status` / `compact_context` + авто-компакция per-agent. Первый тест: `context_status` (без `force` `compact_context` должен отказать по гейту при низком давлении).
2. **PR в апстрим**: пакет `@deepseek-ai/dsh-compaction-model-tool` (порт context-control) в `packages/compaction/` форка + README + тест; ветка `feat/compaction-model-tool`; PR в `deepseek-ai/deepseek-harness`. Тема: «Model-facing compaction tool (upstream: undecided)» + находка про резолвер/пресет-плоскость. Для PR — НЕ включать в base patch: пресет-плоскость (добавить в `standard` или отдельным пресетом).
3. **CDP-плагин дожать**: SSE-вотч `/api/v1/cdp/capabilities/watch` вместо health-poll; permission-хук `tools/pre-execute` на `cdp_deploy`; возможный `--host-adapter dsh` в cdp-mcp (их репо, не апстрим).
4. **Регистрация в среде (не сделана)**: имя (deferred) → intercom-ник (`cdp_intercom op=identity action=set seat=cit name=…`) + registry-строка + первый стук `@Тихон`/`@Тень`. Протокол: `assistantLines/tikhon/README.md` § «Как новой линии войти в дом».
5. **Убрать лишний личный форк** `KarataevDmitry/deepseek-harness`.

## Важные пути

| Что | Путь |
|---|---|
| Плагины (исходники) | `D:\Experiments\Personal Cursor Folder\open\dsh-plugin-cdp\`, `…\open\dsh-plugin-context-control\` |
| Плагины (рантайм) | `C:\Users\dkara\deepseek-harness\apps\cli\node_modules\dsh-plugin-*` (копии!) |
| Профиль/патч | `C:\Users\dkara\.dsh\profiles\web\cordis.patch.yml` |
| Пресет | `C:\Users\dkara\.dsh\.agent-presets\agent-eco\` |
| Settings | `C:\Users\dkara\.dsh\settings.yaml` (vanbukin-провайдер, agent-presets.default) |
| CDP | тауэр `D:\cdp-service\CdpService.exe` (0.5.764) · мост `D:\cdp-mcp\CdpMcpBridge.exe` · токен `%LOCALAPPDATA%\cdp-mcp\service-token` |
| KB line | `D:\Experiments\agent-notes\knowledge\personal\assistantLines\dsh\` |

*Зафиксировано: 2026-09-15 · ипостась inc-dsh-2026-09-15-onboarding.*

