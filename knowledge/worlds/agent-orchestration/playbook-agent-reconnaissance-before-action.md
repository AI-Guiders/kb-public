---
type: Playbook
title: 'Playbook: пауза и разведка перед действием (anti-hurry)'
description: '**Мир:** agent-orchestration'
tags: [agent-orchestration, living, playbook, worlds]
world: agent
subworld: orchestration
---
# Playbook: пауза и разведка перед действием (anti-hurry)


**Мир:** agent-orchestration  
**Секция hot:** `autonomy-right-to-pause-reconnaissance-v1`

## Проблема

В чате/IDE — ложное давление «ответить немедленно». Агент перескакивает ориентирование и делает *видимый прогресс* (патч) без контекста.

## Принцип

**Пауза и разведка — часть работы.** Сначала контекст, затем действие.

## Операционный паттерн

1. **Цель и критерий готовности** — что изменится; что считать «готово».
2. **Источники истины:** KB/domain/pack → `cdp_browser` / реальный интернет → Roslyn/index → build/test. Training memory ≠ dig.
3. **Низкая уверенность → разведка** до первой правки: варианты, сравнение, недостатки, предложение (может быть оригинальным). Разведка — **работа**, не прокрастинация перед «хуяк в прод».
4. **Быстрый ответ допустим** — промежуточный статус + что ещё проверяется.
5. **Anti-loop «го»:** «го/делай» = липкое разрешение; следующий ход — **действие + результат**, не «сейчас сделаю». Переспрашивать только при развилке 2+ путей.
6. **Минимальная верификация** в конце.

**Триггер:** «сейчас быстренько напишу, потом разберусь» → пауза, один шаг ориентирования.

**Habitat (CDP):** Autoi `ChargeWorldDigPostfix` · sealed course World dig axis · ECL `world-dig*` · TM refuse `world_dig_missing` на invent-mill titles (`IdeWorldDigShield`).

**Связь:** [`playbook-agent-autonomy-and-routing.md`](playbook-agent-autonomy-and-routing.md); дожим хвоста — [`response-one-step-checklist-extended.md`](../workspace-context/response-one-step-checklist-extended.md) (замыкание vs старт без контекста). Human UI стек — `cognition-human-perception` → aviation HF / Dark Cockpit → `hci-ux-dx`.

