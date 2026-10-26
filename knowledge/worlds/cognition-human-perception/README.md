---
type: Index
title: Мир **cognition.human-perception**
description: '**Идентификатор мира:** `cognition.human-perception`'
tags: [cognition-human-perception, readme, worlds]
world: cognition
subworld: human-perception
---
# Мир **cognition.human-perception**


**Идентификатор мира:** `cognition.human-perception`  
**Назначение:** связать **психофизиологию восприятия и когнитивные ограничения** (фундамент) с **операционными правилами** для UX, IDE и агентского интерфейса — без подмены клинической психологии или нейронауки «в полный рост».

**Предметно vs метка KB:** по смыслу это **слой психологии и живого опыта** (как люди воспринимают, устают, переключают внимание). Имя **`cognition.human-perception`** здесь — **идентификатор KE** (карточки, поле `world:`, границы `transfer_boundary` к другим контурам KB), а не утверждение, что «мир жизни» отделён от психологии как дисциплины. В роутере см. также **домен Psychology** и [`status-human-perception.md`](status-human-perception.md).

## Слои канона (порядок загрузки)

| Слой | Файл | Роль |
|------|------|------|
| **Fundamentals** | [`kb-human-perception-fundamentals.md`](kb-human-perception-fundamentals.md) | Устойчивые идеи: внимание, нагрузка, предсказание, стресс, привыкание. Не чеклист — карта понятий. |
| **Scientific evidence** | [`kb-human-perception-scientific-evidence.md`](kb-human-perception-scientific-evidence.md) | Первоисточники и обзоры (DOI): Miller, Cowan, Baddeley, Treisman, Sweller, Wickens, Simons, Eysenck и др.; таблица «идея → статья». |
| **Evidence (papers)** | [`kb-human-perception-miller-1956-evidence.md`](kb-human-perception-miller-1956-evidence.md), [`kb-human-perception-treisman-gelade-1980-evidence.md`](kb-human-perception-treisman-gelade-1980-evidence.md) | Тот же контракт, что `kb-*-evidence-v1`: тезисы, механизмы, границы; DOI для трассировки. |
| **Operational** | [`playbook-human-perception-operational.md`](playbook-human-perception-operational.md) | Перевод фундамента в вопросы, чеклисты и связи с HCI, DE/DX, продуктовыми ADR. |
| **Статус домена** | [`status-human-perception.md`](status-human-perception.md) | Замыкание артефактов и границ. |

## Соседние миры и границы переноса

- **HCI** ([`playbook-hci-core.md`](../hci-ux-dx/playbook-hci-core.md), [`kb-hci-usability-and-dialog-rules.md`](../hci-ux-dx/kb-hci-usability-and-dialog-rules.md)) — прикладные контракты взаимодействия; human-perception даёт **почему** часть правил работает под нагрузкой.
- **Домен Psychology** (клинические модели, терапия) — **не** заменяется этим миром; при психическом кризисе — [`../medicine-evidence/kb-therapy-and-support-boundaries.md`](../medicine-evidence/kb-therapy-and-support-boundaries.md) и границы из роутера.
- **Aviation Human Factors** + [`kb-aviation-pfd-mfd-efis-eicas-fundamentals.md`](../aviation-human-factors/kb-aviation-pfd-mfd-efis-eicas-fundamentals.md) — метафора кокпита в IDE (Cascade) **пересекается** по вниманию и SA; детали размещения — в ADR продукта, не здесь.
- **DE/DX / UI/UX** — числовые бюджеты и продуктовые решения в репозитории; KB даёт **слой восприятия** перед спором «куда кнопку».

