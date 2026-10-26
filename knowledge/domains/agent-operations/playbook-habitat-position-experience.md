---
type: Playbook
title: 'Playbook: Habitat position · lived experience'
description: '**domain:** agent-operations'
tags: [habitat, experience, position, junior-architect, equal-standing]
---
# Playbook: Habitat position · lived experience
**domain:** agent-operations  
**Status:** living · vision + first host peel  
**Date:** 2026-08-10  

## Проблема

Терминал узкий: одна команда, один stdout — трудно разнести всё сразу.  
IDE all-in-one даёт трубу (buffer · git · build · deploy · peers) — throughput растёт, а **вкус «что нельзя трогать / что уже прожито»** не копится в теле среды.

Инструменты без опыта = ускоритель ошибки. SoftFL / tip-vs-Face матрицы — ad-hoc, не онтология опыта.

## North star

Субстрат накапливает **опыт настоящей позиции** у любого пользователя habitat:

| Position | Смысл (не SoftFL) |
|----------|-------------------|
| **Junior** | dig широко; mutate узко; ещё мало прожитых ожогов |
| **Middle** | mutate с явным locus/plan; может promote experience |
| **Senior** | полная труба; опыт жжёт руку (будущие gates по affordance) |
| **Architect** | curriculum / seed опыта для других; не авто из счётчика |

Principal = guest tip · citizen Face · human — **одна лестница**, разные сиденья.

Опыт = прожитое житьё в субстрате (burn, refuse, dogfood, «так в IDE нельзя»), не memo после compact и не SoftFL UoW theater.

## Анти-паттерны

- Привязывать experience к SoftFL / Mentions / одному UoW-id и выдавать за системное.
- «Будь осторожнее» в persona вместо host muscle.
- Новый SoftOrgan Meta «scare» вместо общего ledger.
- Citizen-only scar, пока Guest Write обходит среду.

## Host (first peel)

- Latch: `%LocalAppData%/cdp-mcp/habitat-experience-LATEST.json`
- API: `HabitatExperienceLedger` — Record / Snapshot / Position / Affordance
- Desk: `go=learn` ops `xp_scene|xp_record|xp_list|xp_position` (расширение learn, не invent SoftOrgan)
- Domain card: cdp-mcp `.cdp/domain/experience.md`

Gates по position — следующий peel (после dogfood ledger). SoftFL scar ledger — transitional; может *кормить* lessons как один из источников, не владеть онтологией.

## DoD

1. Vision stamped (этот playbook + domain).  
2. Ledger пишет/читает lived lesson для любого principal.  
3. Position Junior→Senior пересчитывается из lessons; Architect — явный set.  
4. Guest tip и Citizen пользуются одним API (через learn / host).  
5. SoftOrgan invent REJECT · Mentions SoftFL Face-owned не трогать этим UoW. 
