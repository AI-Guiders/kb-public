# Playbook: human perception — troubleshooting (v1)

> **Контур:** A · kb-public  
> **Когда:** жалоба на UX без воспроизводимого бага, когнитивная перегрузка, потеря потока  
> **Operational:** [`../playbook-human-perception-operational-v1.md`](../playbook-human-perception-operational-v1.md)

---

## Симптом → слой

| Симптом (словами пользователя) | Сначала | Не путать с |
|--------------------------------|---------|-------------|
| «Бесит», «устал смотреть», хаос на экране | Perception operational + fundamentals kb | Единственный software-баг |
| Непредсказуемый фидбек / тишина после действия | HCI `playbook-hci-core-v1` | Только «поправить цвет» |
| Конкуренция зон за внимание (много панелей) | Aviation attention kb + HCI | Увеличить всё MFD |

---

## Чеклист

1. Есть ли **измеримый** сбой (ошибка, crash) — если да, software troubleshooting.
2. Иерархия сигналов: что primary, что secondary.
3. Прерывания и восстановление контекста (Nielsen #3, #5).

---

## Как дополнять

Связка symptom ↔ checklist в operational playbook, не дублировать научный слой.
