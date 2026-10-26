---
type: Playbook
title: 'Playbook: ops.reliability — troubleshooting'
description: '> **Контур:** A · мир **ops.reliability** · kb-public'
tags: [living, ops-reliability, playbook, worlds]
world: ops
subworld: reliability
---
# Playbook: ops.reliability — troubleshooting


> **Контур:** A · мир **ops.reliability** · kb-public  
> **Когда:** сбой бекапа, восстановление, инцидент, тикет, постмортем не закрыт

---

## Симптом → playbook

| Симптом | Playbook |
|---------|----------|
| RPO/RTO, бекап не прошёл, restore | `playbook-backup-db.md` |
| Инцидент, приоритет, постмортем, повтор | `playbook-incidents-tickets.md` |

---

## Бекапы

| Симптом | Действие |
|---------|----------|
| Сбой задания | Логи и статусы job; алерты |
| «Бекап есть, восстановить не умеем» | Регулярный test restore в тестовую среду с фиксацией времени и результата |

---

## Инциденты / тикеты

| Симптом | Действие |
|---------|----------|
| Долгое MTTR | Анализ времени реакции/разрешения по классам |
| Повтор одной причины | Доля повторов; выполнены ли action items из постмортемов |

---

## Как дополнять

Метрики и каналы тикет-систем — локальный контекст; в KB — только паттерны проверки.

