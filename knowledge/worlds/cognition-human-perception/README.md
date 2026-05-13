# Мир **cognition.human-perception**

**Идентификатор мира:** `cognition.human-perception`  
**Назначение:** связать **психофизиологию восприятия и когнитивные ограничения** (фундамент) с **операционными правилами** для UX, IDE и агентского интерфейса — без подмены клинической психологии или нейронауки «в полный рост».

**Предметно vs метка KB:** по смыслу это **слой психологии и живого опыта** (как люди воспринимают, устают, переключают внимание). Имя **`cognition.human-perception`** здесь — **идентификатор KE** (карточки, поле `world:`, границы `transfer_boundary` к другим контурам KB), а не утверждение, что «мир жизни» отделён от психологии как дисциплины. В роутере см. также **домен Psychology** и [`status-human-perception-v1.md`](status-human-perception-v1.md).

## Слои канона (порядок загрузки)

| Слой | Файл | Роль |
|------|------|------|
| **Fundamentals** | [`kb-human-perception-fundamentals-v1.md`](kb-human-perception-fundamentals-v1.md) | Устойчивые идеи: внимание, нагрузка, предсказание, стресс, привыкание. Не чеклист — карта понятий. |
| **Scientific evidence** | [`kb-human-perception-scientific-evidence-v1.md`](kb-human-perception-scientific-evidence-v1.md) | Первоисточники и обзоры (DOI): Miller, Cowan, Baddeley, Treisman, Sweller, Wickens, Simons, Eysenck и др.; таблица «идея → статья». |
| **Evidence (papers)** | [`kb-human-perception-miller-1956-evidence-v1.md`](kb-human-perception-miller-1956-evidence-v1.md), [`kb-human-perception-treisman-gelade-1980-evidence-v1.md`](kb-human-perception-treisman-gelade-1980-evidence-v1.md) | Тот же контракт, что `kb-*-evidence-v1`: тезисы, механизмы, границы; DOI для трассировки. |
| **Operational** | [`playbook-human-perception-operational-v1.md`](playbook-human-perception-operational-v1.md) | Перевод фундамента в вопросы, чеклисты и связи с HCI, DE/DX, продуктовыми ADR. |
| **Статус домена** | [`status-human-perception-v1.md`](status-human-perception-v1.md) | Замыкание артефактов и границ. |

## Соседние миры и границы переноса

- **HCI** ([`playbook-hci-core-v1.md`](../hci-ux-dx/playbook-hci-core-v1.md), [`kb-hci-usability-and-dialog-rules-v1.md`](../hci-ux-dx/kb-hci-usability-and-dialog-rules-v1.md)) — прикладные контракты взаимодействия; human-perception даёт **почему** часть правил работает под нагрузкой.
- **Домен Psychology** (клинические модели, терапия) — **не** заменяется этим миром; при психическом кризисе — [`../medicine-evidence/kb-therapy-and-support-boundaries-v1.md`](../medicine-evidence/kb-therapy-and-support-boundaries-v1.md) и границы из роутера.
- **Aviation Human Factors** + [`kb-aviation-pfd-mfd-efis-eicas-fundamentals-v1.md`](../aviation-human-factors/kb-aviation-pfd-mfd-efis-eicas-fundamentals-v1.md) — метафора кокпита в IDE (Cascade) **пересекается** по вниманию и SA; детали размещения — в ADR продукта, не здесь.
- **DE/DX / UI/UX** — числовые бюджеты и продуктовые решения в репозитории; KB даёт **слой восприятия** перед спором «куда кнопку».

## Версия

v1.6 · 2026-05-11 — слои мира перенесены в эту папку (`worlds/cognition-human-perception/`); таблица ссылается на соседние файлы. v1.5 · 2026-05-11 — явное разведение: предметно психология/жизнь; `cognition.human-perception` — метка KE. v1.4 · 2026-04-20 — имена файлов `*-evidence-v1`
