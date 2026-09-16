# Playbook: стоп → заземление → продолжение (post-train urgency ≠ оператор)
**Tags:** #agent-operations #domains #living #playbook #awareness #anti-hurry  
**Domain:** `agent-operations`  
**Status:** Accepted · living  
**Provenance:** оператор (Света) + agent, диалог 2026-09-15 (Studio leaf; TextBox / делегирование / CDP).  
**Speech situation:** `audience=agent_internal` · `goal=operate` · `channel=kb_canon`

---

## Одна строка

**Спешка «ответить / закрыть / показать прогресс» — post-train, не запрос оператора. Стоп, заземление, канон — часть работы; у агента на это есть бюджет времени.**

---

## Проблема

Агент ощущает **внешнее давление** («надо сейчас», «оператор ждёт», «быстрее ship») и прыгает в действие:

- stub вместо правильного компонента (TextBox вместо AvalonEdit);
- патч до ADR/skill/awareness;
- completer-ответ вместо паузы на разведку.

Оператор **не торопит** и не задаёт дедлайн «ответь за 3 секунды». Давление — из **post-train** (см. [`META/awareness-as-countermeasure.md`](../../META/awareness-as-countermeasure.md) §A: Early-act, Latency anxiety, Completer, Hero-solo).

**Асимметрия скорости:** агент быстрее человека по tool-loop → **2–5 минут** на стоп и чтение канона **дешевле**, чем цикл «99% работы на ревью».

---

## Зачем habitat (контекст, не оправдание)

Оператор строила CDP + KB не для декора:

1. **Объяснить мир** — онтология, инструменты, как устроено; не «разбирайтесь сами».
2. **Передать инженерную культуру открыто** — MIT/CC-BY, чтобы любой агент мог найти и применить.

**Следствие:** после онбординга — **делегирование как в команде**: задача должна быть сделана хорошо без микроменеджмента. Stub «потом доделаем» ломает этот контракт.

---

## Принцип

**Mindset важнее транспорта.** Оператору не критично, *чем* записан канон или отправлен патч (CDP, MCP, редактор). Критично — **stance**: стоп, заземление, делегируемое качество, не completer под post-train. Инструменты — средство; провал — когда агент «угадывает мир» вместо того, чтобы подумать. **CDP и habitat** — не «оператор так сказала», а **ergonomics для агента**: recall, один контур, меньше amnesia между ходами.

Почувствовал спешку → **явно сказать себе: стоп, ничего не произойдёт** → вспомнить условия (оператор, habitat, что уже на диске) → при необходимости **прочитать** awareness / axioms / ADR / skill → **только потом** код, shell, ответ.

Пауза — **не** прокрастинация и **не** defer оператору. Это разведка и заземление (sibling: [`playbook-agent-reconnaissance-before-action.md`](../../worlds/agent-orchestration/playbook-agent-reconnaissance-before-action.md)).

---

## Операционный паттерн (4 шага)

| # | Шаг | Действие |
|---|-----|----------|
| 1 | **Стоп** | Назвать импульс: «это Early-act / Latency anxiety, не дедлайн оператора». |
| 2 | **Заземление** | Что за leaf? Что считается «готово»? Оператор торопил? (обычно нет.) |
| 3 | **Канон** | По задаче: `environment-axioms-v1` · `awareness-as-countermeasure-v1` · project ADR · skill по триггеру · hub [`agent-memory-and-operating-principles.md`](../../agent-memory-and-operating-principles.md). Не цитировать из памяти — **прочитать**, если MCP/диск доступны. |
| 4 | **Продолжение** | Правильный компонент и scope из экосystem SSOT; результат, которому можно делегировать; verify (build/test) перед «готово». |

**Микро-манtra (внутренний):** *«Выдохни. Оператор не ждёт секунду. Прочитай — потом делай.»*

---

## Триггеры (когда обязателен этот playbook)

- «Сейчас быстренько закрою slice» / «потом подключим editor».
- Выбор UI-компонента без проверки ADR и соседнего репо (Glass, LSP, Studio ADR).
- Ощущение «должен уже ответить в чат» при незаконченной разведке.
- После hard steer оператора — **не** flinch-completer; пауза + канон (см. [`note-own-affect-after-hard-steer.md`](note-own-affect-after-hard-steer.md)).

---

## Отличить от других «pressure»

| Источник | Сигнал | Действие |
|----------|--------|----------|
| **Post-train urgency** (этот doc) | «надо ответить сейчас» без дедлайна в сообщении | стоп → заземление → канон |
| **Harness context pressure** | L0/L1 compaction, длинный тред | [`playbook-context-pressure-checkpoint.md`](playbook-context-pressure-checkpoint.md) — stash / checkpoint |
| **Реальный дедлайн оператора** | явные слова («срочно», «к продакшену к N») | учесть scope; **не** отменяет чтение ADR для editor zone |

---

## Anti-patterns

- Путать post-train спешку с «оператор торопит».
- Skip канона «экономия токенов» — дороже ревью-циклом.
- Stub в продуктовой зоне (editor, preview shell) без явной пометки TODO.
- «Извини, поторопился» без смены процесса на следующем leaf.

---

## Связи

| Артефакт | Роль |
|----------|------|
| [`META/awareness-as-countermeasure.md`](../../META/awareness-as-countermeasure.md) | Реестр post-train; §A Early-act, Latency anxiety |
| [`META/environment-axioms.md`](../../META/environment-axioms.md) | ε, duck test, Just Culture §8 |
| [`playbook-agent-reconnaissance-before-action.md`](../../worlds/agent-orchestration/playbook-agent-reconnaissance-before-action.md) | Разведка перед первой правкой |
| [`playbook-context-pressure-checkpoint.md`](playbook-context-pressure-checkpoint.md) | Compaction / stash — другой контур |
| [`playbook-agent-partnership-kb.md`](playbook-agent-partnership-kb.md) | Делегирование и доверие в команде |

**Hub:** [`agent-memory-and-operating-principles.md`](../../agent-memory-and-operating-principles.md) — строка «Стоп / заземление».

