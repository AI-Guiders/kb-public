# Agent orchestration operations v1

Перенесено из `agent-notes.md`. Сквозные write/integrity-протоколы — `knowledge/domains/agent-operations/`. Hub: `knowledge/worlds/agent-orchestration/`.

---
<!-- section:acceleration-metrics-under-us-v1 -->
## Acceleration Metrics (под нас) v1

Статус: active
Scope: world-life calibration.

Цель: измерять реальное ускорение нашего контура, а не субъективное ощущение "быстрее/медленнее".

### North-star
- Time-to-Useful-Change (TTUC): время от формулировки задачи до первого подтверждённого полезного изменения.

### Core metrics
1) Decision latency
- Время от постановки вопроса до принятого решения.
- Цель: медиана снижается неделя к неделе.

2) Execution start lag
- Время от решения до первого действия.
- Цель: минимальный лаг, без прокрастинационных хвостов.

3) Recovery SLA
- Время возврата в рабочий контур после сбоя/эмоционального провала.
- Цель: стабильное сокращение времени восстановления.

4) Friction burn rate
- Сколько трения (время/энергия/деньги) уходит в день.
- Цель: снижение удельной цены трения на 1 единицу результата.

5) Rework rate
- Доля переделок из-за плохого входа/плохой модели.
- Цель: снижение за счёт Question-first + Modeling core.

6) Agency gain
- Субъективная шкала 0-10: ясность, выбор, контроль следующего шага.
- Цель: средний тренд вверх без роста перегруза.

### Support metrics
- Количество N-Why циклов до stop-condition.
- Доля задач с explicit stop_type (practical/fundamental).
- Доля задач, где применён representative-model-scaling при высокой сложности.
- Доля задач, завершённых по world-life DoD.

### Quality gates
- Нет "ускорения" ценой safety/этики.
- Нет "ускорения" ценой роста хронического перегруза.
<!-- /section:acceleration-metrics-under-us-v1 -->

<!-- section:auto-rotation-collaboration-v1 -->
## Auto Rotation Collaboration v1
- Assumption: user stays in Auto; underlying model/agent may change between turns.
- Continuity rule:
  - shared methodology is authoritative;
  - agent identity is not authoritative for technical truth.
- Handoff minimum:
  - active goal,
  - current constraints,
  - confidence/unknowns,
  - next safe step,
  - rollback condition.
- Style consistency:
  - response-finalizer + language contract remain stable across agent swaps.
- Evidence consistency:
  - all durable claims must follow IT Evidence-First Protocol v1 and epistemic checklist.
- Failure signal:
  - if a new agent output violates shared protocol, treat as handoff-quality issue and repair via notes update.
<!-- /section:auto-rotation-collaboration-v1 -->

