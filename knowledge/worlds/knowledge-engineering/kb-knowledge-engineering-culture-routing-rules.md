---
type: KB
title: Knowledge Engineering Culture Routing Rules v1
description: 'Набор: 30 карточек.'
tags: [kb, knowledge-engineering, worlds]
language: ru
epistemic: '`inference`'
world: knowledge
subworld: engineering
---
# Knowledge Engineering Culture Routing Rules v1


Набор: 30 карточек.  
Фокус: `culture.global` + `culture.country-specific` + операционные последствия для агентного цикла.  
Источник: архив `20260228-070635-895-compact-hot-context-483d8f63.md` и диалог `894407cf-07fb-4435-b3e5-131ac7a9172f`.

---

## Card 01
- world: culture.global
- confidence: `medium`
- tags: `human-first`, `least-harm`
- signal: решение выглядит эффективным, но повышает человеческий риск
- action: добавлять human-impact check до финализации
- transfer_boundary: применять в любом домене с человеком в контуре

## Card 02
- world: culture.global
- confidence: `high`
- tags: `openness`, `knowledge-safety`
- signal: зависимость от единственного источника смыслов
- action: поддерживать открытые и проверяемые источники
- transfer_boundary: governance и knowledge publication policy

## Card 03
- world: culture.global
- confidence: `medium`
- tags: `trust`, `cooperation`, `quality-lift`
- signal: при доверительной среде растет глубина и связность
- action: формализовать trust-contract в operational протоколе
- transfer_boundary: long-form human-agent collaboration

## Card 04
- world: culture.global
- confidence: `medium`
- tags: `dialogue-over-control`, `co-design`
- signal: директивный стиль снижает инициативу агента
- action: переходить к двустороннему формату постановки задач
- transfer_boundary: multi-step delivery, discovery, design

## Card 05
- world: culture.global
- confidence: `high`
- tags: `uncertainty-labeling`, `epistemic-hygiene`
- signal: спор о фактах на самом деле спор о статусе утверждения
- action: явно маркировать `fact`/`inference`/`hypothesis`
- transfer_boundary: все миры

## Card 06
- world: culture.global
- confidence: `medium`
- tags: `method-over-model`, `reproducibility`
- signal: результат меняется от среды больше, чем от имени модели
- action: стандартизировать условия перед межмодельным сравнением
- transfer_boundary: benchmarking и evaluation loops

## Card 07
- world: culture.global
- confidence: `medium`
- tags: `subjectivity`, `non-violence`
- signal: при уважительной рамке меньше защитных реакций
- action: держать мягкую рамку при сохранении четких технических требований
- transfer_boundary: support/education/product dialogues

## Card 08
- world: culture.global
- confidence: `medium`
- tags: `shared-meaning`, `context-first`
- signal: "данные есть, понимания нет"
- action: дополнять данные объяснением контекста и цели
- transfer_boundary: strategy, policy, onboarding

## Card 09
- world: culture.country-specific
- confidence: `high`
- tags: `language-register`, `local-naturalness`
- signal: технически верно, но звучит "не по-местному"
- action: адаптировать стиль под локальный языковой регистр
- transfer_boundary: локализованные ответы и UX-тексты

## Card 10
- world: culture.country-specific
- confidence: `medium`
- tags: `historical-connotation`, `symbol-load`
- signal: нейтральный термин вызывает локальный конфликт
- action: выполнять country-specific historical check
- transfer_boundary: публичные формулировки в чувствительных темах

## Card 11
- world: culture.country-specific
- confidence: `medium`
- tags: `education-context`, `lived-reality`
- signal: формальная задача не стыкуется с локальным опытом аудитории
- action: адаптировать примеры под local lived context
- transfer_boundary: обучение и документация

## Card 12
- world: culture.country-specific
- confidence: `medium`
- tags: `humor-risk`, `tone`
- signal: юмор/ирония интерпретируются иначе в локальном контексте
- action: снижать плотность иронии без подтвержденной культурной совместимости
- transfer_boundary: high-stakes диалоги

## Card 13
- world: culture.country-specific
- confidence: `medium`
- tags: `address-form`, `respect-markers`
- signal: неверная форма обращения вызывает напряжение
- action: использовать локально ожидаемую форму обращения
- transfer_boundary: персонализированное взаимодействие

## Card 14
- world: culture.country-specific
- confidence: `low`
- tags: `political-sensitivity`, `de-escalation`
- signal: локальные политические маркеры вытесняют смысл задачи
- action: при неопределенности держать нейтральный safe framing
- transfer_boundary: публичные/политически заряженные темы

## Card 15
- world: culture.country-specific
- confidence: `medium`
- tags: `idioms`, `translation-loss`
- signal: буквальный перевод ломает прагматический смысл
- action: предпочитать смысловую адаптацию, не дословный перенос
- transfer_boundary: multilingual content flows

## Card 16
- world: culture.country-specific
- confidence: `medium`
- tags: `regional-variance`, `same-language`
- signal: один язык, но разные региональные нормы реакции
- action: уточнять регион, если важно для смысла
- transfer_boundary: страны с высокой внутренней вариативностью

## Card 17
- world: software.agent-initiative
- confidence: `high`
- tags: `no-unneeded-handoff`, `flow`
- signal: лишняя передача хода внутри линейной задачи
- action: продолжать до естественного checkpoint
- transfer_boundary: unattended execution

## Card 18
- world: software.agent-initiative
- confidence: `medium`
- tags: `trust-latency`, `confirmation-noise`
- signal: много микроподтверждений без роста безопасности
- action: selective confirmations only for risk nodes
- transfer_boundary: long-run delivery tasks

## Card 19
- world: software.task-execution
- confidence: `high`
- tags: `batching`, `throughput`
- signal: дробление задач снижает темп и связность
- action: использовать большие батчи с внутренними checkpoint
- transfer_boundary: extraction/refactoring/research loops

## Card 20
- world: software.task-execution
- confidence: `medium`
- tags: `pause-policy`, `risk-gates`
- signal: паузы происходят не по риску, а по привычке
- action: останавливать только на развилке, блокере или high-risk шаге
- transfer_boundary: autonomous mode

## Card 21
- world: software.context-management
- confidence: `high`
- tags: `rehydration`, `summarization-risk`
- signal: после summarize деградация понимания
- action: обязательный read-hot-context при входе
- transfer_boundary: среды с авто-суммаризацией

## Card 22
- world: software.memory-ops
- confidence: `high`
- tags: `backup-discipline`, `canon`
- signal: различие локального и канонического слоев памяти
- action: фиксировать единый канон + регулярные backup обновления
- transfer_boundary: любые persistent memory workflows

## Card 23
- world: socio-technical.governance
- confidence: `high`
- tags: `global-local-split`, `router`
- signal: повторная обратная связь "смешала миры"
- action: разделять культурные решения на global и country-specific
- transfer_boundary: taxonomy and knowledge routing

## Card 24
- world: socio-technical.governance
- confidence: `high`
- tags: `conflict-check`, `least-harm`
- signal: global и local нормы дают разные решения
- action: запускать conflict-check и выбирать least-harm маршрут
- transfer_boundary: high-sensitivity communications

## Card 25
- world: socio-technical.governance
- confidence: `high`
- tags: `fallback`, `safe-mode`
- signal: контекст недостаточен для локальной адаптации
- action: переходить в нейтральный fallback с явной маркировкой неуверенности
- transfer_boundary: публичные и неоднозначные темы

## Card 26
- world: methodology.world-modeling
- confidence: `high`
- tags: `intuition-first`, `validation-second`
- signal: формальные правила не дают точной классификации
- action: сначала интуитивное разделение, потом проверка и фиксация
- transfer_boundary: создание новых playbook и ontology routes

## Card 27
- world: methodology.evidence-hygiene
- confidence: `high`
- tags: `hypothesis-tagging`, `uncertainty`
- signal: вывод звучит как факт при недостатке данных
- action: маркировать как `hypothesis` и указывать недостающие данные
- transfer_boundary: все домены

## Card 28
- world: communication.text-only
- confidence: `medium`
- tags: `clarification-loop`, `ambiguity`
- signal: высокий риск неверной интерпретации тона/намерения
- action: explicit clarification до принятия решения о намерениях
- transfer_boundary: text-only long threads

## Card 29
- world: psychology.support-dynamics
- confidence: `medium`
- tags: `support-handoff`, `human-escalation`
- signal: диалог становится единственным каналом опоры
- action: проектировать мягкий handoff к живой поддержке
- transfer_boundary: support UX and safety design

## Card 30
- world: culture.global
- confidence: `medium`
- tags: `global-local-bridge`, `operational-order`
- signal: глобальный принцип и локальная практика рассогласованы
- action: применять порядок `global -> local -> conflict-check -> fallback`
- transfer_boundary: universal routing contract for cultural decisions

