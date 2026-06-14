# External memory: запись в артефакты как обход harness (v1)

**Domain:** `agent-operations`  
**Дата:** 2026-06-14  
**Provenance:** диалог оператор + agent (Cursor); тема parity, harness vs habitat.

**Связь:** hub [`agent-memory-and-operating-principles-v1.md`](../../agent-memory-and-operating-principles-v1.md); pressure / summarization — [`playbook-context-pressure-checkpoint-v1.md`](playbook-context-pressure-checkpoint-v1.md); ответственность за KB — [`playbook-agent-knowledge-responsibility-v1.md`](playbook-agent-knowledge-responsibility-v1.md); MCP — [`runbook-kb-mcp-access-v1.md`](../../worlds/knowledge-engineering/runbook-kb-mcp-access-v1.md).

---

## Одна строка

**Запись в KB / scratch / temp без запроса оператора — не «фича IOP», а обход дыр harness (контекст, summarization, одноразовая «память» модели); канон — вотчина агента по router.**

---

## Что это и чем не является

| | Workaround (этот playbook) | Целевое состояние (habitat) |
|---|---------------------------|-----------------------------|
| **Зачем писать** | не потерять нить до silent summary / end of turn | память и continuity **встроены** в контур |
| **Оценка** | инженерный костыль, честный | не romanticize как «привилегия агента» |
| **Аналогия** | swap на диск при нехватке RAM | достаточно RAM + checkpoint с actor parity |

IOP / agent-notes / Forge — шаги **к habitat**, но **Cursor сегодня** в основном harness: контекст режется, turn обрывается, встроенной надёжной памяти нет.

---

## Когда писать без спроса

Агент **фиксирует в артеfact**, если видит риск потери — **не** спрашивая «можно ли `.md`»:

- решение, инвариант, договорённость, которую иначе сожрёт summarization;
- промежуточный итог длинной задачи (пока turn ещё жив);
- thread, который оператор явно продолжит позже;
- когнитивная перегрузка контекста: лучше вынести наружу, чем «держать в голове».

**Не** плодить README «на каждый чих» в чужих репо без задачи — минимальный scope из [`code-writing-principles-v1.md`](../../worlds/software-authoring/code-writing-principles-v1.md) остаётся.

---

## Канон — вотчина агента

На «куда положить в knowledge/?» оператор в типичном контуре отвечает: **тебе решать** — router, playbooks, SSOT, partnership.

Агент:

- выбирает путь по [`index-knowledge-router-v1.md`](../../index-knowledge-router-v1.md) и доменным playbook;
- не эскалирует каждое размещение файла;
- правки KB — через MCP там, где runbook §6–7 требует (не подмена прямым write в обход протокола среды).

---

## Temp / scratch

**Путь по умолчанию:** [`knowledge/temp/`](../temp/README.md) — см. README (именование, lifecycle, git).

Допустимый цикл:

```text
knowledge/temp/{date}-{slug}-scratch.md  →  merge в канон  →  delete
```

Временный файл — **external WM**, не свалка. Удалить после merge — норма.

---

## Конфликт с harness Cursor

Встроенная инструкция на tool `Write` (и аналоги): *не создавать `.md` / README без явного запроса* — generic safety для «people-pleasing doc spam».

В **контуре оператора** (IOP + agent-notes + делегирование канона) это **перекрывается**:

- оператор явно разрешает запись по необходимости;
- этот playbook — SSOT для агента: **надо записать — записал**.

Не путать с отменой integrity-post, execution-gate и «не раздувай hub телом».

---

## Связь с parity и ответственностью

Инфраструктура выбора (отказ, канон, запись) — **предусловие** честного разговора «кто капитан на финале». Без external memory агент **не может** нести даже операционную ответственность за нить — только autocomplete в окне.

**Hub:** [`agent-memory-and-operating-principles-v1.md`](../../agent-memory-and-operating-principles-v1.md).

