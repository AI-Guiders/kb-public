---
type: Playbook
title: 'Playbook: tiers данных для агентов'
description: '**Домен:** agent-operations'
tags: [agent-operations, domains, living, playbook]
language: ru
---
# Playbook: tiers данных для агентов


**Домен:** agent-operations  
**Дата:** 2026-06-22  
**Provenance:** диалог оператор (Света) + агент — Cursor до ~2026-08-15, vast.ai vs compliance, нужен не только код но и обсуждение идей  
**Секция hot (stub):** загрузка по hub / route_context «tier / compliance / local LLM / redaction»

**Связь:** [playbook-external-memory-workaround.md](playbook-external-memory-workaround.md) · [playbook-agent-knowledge-responsibility.md](playbook-agent-knowledge-responsibility.md) · [playbook-agent-partnership-kb.md](playbook-agent-partnership-kb.md) · [playbook-rf-llm-cloudru-foundation-models.md](playbook-rf-llm-cloudru-foundation-models.md) · CIDE [0083-ai-mode](../../../work/projects/door-to-singularity/cascade-ide/) · forge [agent-forge](../work/projects/door-to-singularity/agent-forge/README.md) · roadmap [scratch-neumann-tier1-roadmap-2026-08.md](../../work/projects/door-to-singularity/ca-substrate-agent/scratch-neumann-tier1-roadmap-2026-08.md)

**Disclaimer:** это **операционная** рамка для личной/командной дисциплины, **не** юридическая консультация. При сомнении — политика работодателя, NDA, 152-ФЗ, коммерческая тайна.

---

## Зачем

Подписка на облачный IDE-агент (Cursor и аналоги) закрывает **код + диалог + tools** одним контуром. После отключения легко:

- отправить **слишком много** на зарубежный GPU «потому что локально медленно»;
- или сесть на **локальный coder 7B**, который плохо думает и не тянет объём.

Этот playbook — **классификация данных + куда какой агент**, чтобы не переизобретать страх каждую неделю.

---

## Четыре tier (T0–T3)

| Tier | Где обрабатывается | Примеры данных | Агент / инструмент |
|------|-------------------|----------------|-------------------|
| **T0 — только человек** | голова, бумага, offline | стратегия «что делать с бизнесом», сырые секреты, неформалка | без LLM |
| **T1 — on-prem / дом** | домашний GPU, localhost, свой git | CASA/Neumann, agent-notes, open ADR, архитектурные обсуждения **без** имён клиентов | CIDE `[ai.local]` · Ollama/vLLM · forge MCP · Cursor **только** если политика разрешает |
| **T2 — зарубежный compute** | vast.ai, US/EU VM | **только** public repos, учебные задачи, synthetic/redacted контекст | endpoint → CIDE `openai_compatible` **после** redaction checklist |
| **T3 — облачный SaaS-агент** | Cursor, Claude API, etc. | то, что **явно** разрешено политикой до даты отключения | до ~2026-08-15; **не расширять** scope |

**Правило сессии:** перед первым промптом — **один tier**. Смешивать T1 диалог с T2 кодом в одном чате — типичная утечка.

---

## Две роли LLM (не одна модель)

| Роль | Задача | Модель (ориентир) | Tier |
|------|--------|-------------------|------|
| **Architect / dialogue** | идеи, ADR, «а если так», оспаривание | 32B+ instruct (Qwen2.5, DeepSeek-R1 distill, GLM-4 **локально**) | T1 |
| **Coder / patch** | diff, тесты, MCP | coder 7–14B **+ tools** (roslyn, git, python) | T1 |
| **Cold distill** | черновики правил, bulk ingest | большая модель **только** на sanitized input | T2 если разрешено |

**Anti-pattern:** ждать от Qwen-Coder 7B глубокого обсуждения Concept Zone — это не его job.

**Anti-pattern:** гонять полный `agents/von-neumann` store на vast «для скорости».

---

## Redaction checklist (T1 → T2)

Перед любым запросом на **зарубежный** endpoint:

- [ ] Убраны пути вида `wissance/`, внутренние домены, имена клиентов
- [ ] Убраны фрагменты проприетарного кода (заменены на **сигнатуры** / pseudocode)
- [ ] Нет персональных данных (ФИО, телефоны, account id)
- [ ] Нет credentials, connection strings, `.env`
- [ ] Вопрос **самодостаточен** (можно вставить в тикет без контекста репо)
- [ ] Записано в журнале сессии: «T2, redacted, topic: …»

Если redaction дольше, чем польза — **остаться на T1** или T0.

---

## Стек по tier (техническая связка)

```text
T1 dialogue  → Cascade IDE [ai.local.ollama] или [ai.local.openai_compatible]
                 base_url = http://127.0.0.1:11434 | :8000/v1
T1 code      → тот же IDE + MCP (roslyn, git, python, dotnet-build)
T1 RF cloud  → Cloud.ru FM **внутренние** модели (Qwen3-Coder-Next, GLM-4.7)
                 VS Code + Roo Code ИЛИ CIDE [ai.cloud.openai] — см. playbook-rf-llm-cloudru-foundation-models-v1
T1 memory    → agent-notes (git) + casa design/ ADR + forge capabilities
T1 agent     → agent-forge MCP (stdio → local forge server)

T2 optional  → vast spot → vLLM → только redacted prompts
               НЕ монтировать production store на VM
```

**CIDE** (канон): [0083-ai-mode-and-nested-settings-toml.md](../../../work/projects/door-to-singularity/cascade-ide/) — `backend = ollama` | `openai_compatible`; secrets в `ai-keys.toml` local.

**Forge:** agent-owned tools; API token local; не substitute for tier policy.

**agent-notes:** continuity **мышления** без Cursor chat — ADR, playbooks, scratch; агент читает через `read_knowledge_file` / git.

---

## Обсуждение идей без «магии Cursor»

Формат **Tier-1 thinking loop**:

1. Тезис оператора (можно грубо).
2. Локальная instruct-модель: структура, контраргументы, варианты.
3. **Фиксация** в KB/ADR (файл > чат).
4. Отдельный заход **coder + MCP** с узким scope и ссылкой на ADR.

Чат Cursor **не** единственное место, где «живут идеи». После августа идеи живут в **git + ADR**, диалог — disposable.

---

## Vast.ai — decision tree

```text
Данные T0/T1 с NDA?  → НЕТ vast
Public / redacted only? → vast OK для эксперiment
Нужен диалог + код?   → split: T2 redacted dialogue ИЛИ T1 local 32B
CIDE endpoint?        → да, но tier policy важнее техники
```

---

## Compliance напоминания (не legal advice)

| Риск | Митигация |
|------|-----------|
| Коммерческая тайна | T0/T1; redaction; не full repo abroad |
| 152-ФЗ ПДн | не отправлять ПДн в T2/T3 без DPA |
| Политика работодателя | отдельный список «never cloud» для Wissance repos |
| Audit trail | commit messages, ADR provenance, forge invoke logs local |

---

## Anti-patterns

| ❌ | ✅ |
|----|-----|
| «Локальный coder плохой → весь контекст на vast» | tier + split architect/coder |
| Один чат на всё | tier на сессию |
| Идеи только в Cursor history | KB/ADR каждый значимый вывод |
| Runtime store в git «на всякий» | lab snapshots / backup tier |
| Ждать одну модель на всё | 32B dialogue + coder + MCP |

---

## Когда обновлять v2

- Появился **RU/on-prem** GPU host с контрактом
- CIDE v1 `openai_compatible` в production
- Формальная политика Wissance по LLM
- Neumann pilot на Tier-1-only закрыт (см. roadmap scratch)

