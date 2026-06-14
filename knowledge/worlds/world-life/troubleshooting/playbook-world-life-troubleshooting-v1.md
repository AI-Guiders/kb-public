# Playbook: world-life — troubleshooting (v1)

> **Контур:** A · kb-public  
> **Когда:** дистресс, конфликт, UX-провал, data-gap, «лечим симптом не петлю»  
> **Map (маршрут subworld):** [`../map-world-life-subworlds-v1.md`](../map-world-life-subworlds-v1.md)

---

## Первичный симптом задачи → шаг

1. Определи симптом: дистресс, конфликт, UX-провал, data-gap, смысловой шум (`map-world-life-subworlds-v1`).
2. Выбери subworld и рычаг в **структуре**, не только симптоматический фикс.
3. Высокая сложность → `representative-model-scaling-v1`.
4. Критерий: симптом ослаб без роста соседних проблем; изменена **петля**, не маскировка.

---

## Ошибки моделирования (E1–E8)

| ID | Симптом | Фикс |
|----|---------|------|
| E1 False precision | Много цифр, мало предсказательной силы | Упростить модель, усилить валидацию |
| E2 Level collapse | Только биология или только психология | Cross-level связи |
| E3 Overfitting anecdote | Один яркий кейс | 2–3 контекста |
| E4 Correlation ≠ causation | Действие не меняет результат | Механизм, интервенционный рычаг |
| E5 Missing delay | Преждевременно «не работает» | Задержка эффекта в метрике |
| E6 Boundary blindness | Перенос 1:1 ломает результат | Boundary conditions |
| E7 Analysis paralysis | Бесконечные why | N-Why stop + probing-step |
| E8 Ethical drift | KPI ценой человека | Safety/agency gate |

Перед выпуском: `model-validation-checklist-v1` (см. toolchain).

---

## Анти-паттерны

- Лечить симптом вместо петли.
- Рычаг только в KPI без структуры.

---

## Как дополнять

Новый E* — таблица + секция в `playbook-world-life-modeling-toolchain-v1` § modeling-errors-catalog.

