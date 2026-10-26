---
type: KB
title: SE cooperation gap vs aviation investigation institutions v1
description: '**Назначение:** честный разбор — почему в SE нет «NTSB для софта»; что есть вместо; как federation относится к кооперации (проверяемые hyperlanes, не членство-only альянс).'
tags: [aviation-human-factors, kb, worlds, cooperation, cve, investigation]
language: ru
world: aviation
subworld: human-factors
---
# SE cooperation gap vs aviation investigation institutions v1


**Назначение:** честный разбор — почему в SE нет «NTSB для софта»; что есть вместо; как federation относится к кооперации (проверяемые hyperlanes, не членство-only альянс).

**Связь:** [`kb-aviation-incident-investigation-fundamentals.md`](kb-aviation-incident-investigation-fundamentals.md) · [`matrix-aviation-investigation-to-se-transfer.md`](matrix-aviation-investigation-to-se-transfer.md)

---

## 1. Не путать органы (коротко)

| Организация | Роль | Аналог в SE? |
|-------------|------|--------------|
| **NTSB** (US), **AAIB** (UK), **BEA** (FR), **TSB** (CA) | **Независимое** расследование авиакатастроф; цель — safety, не суд | **Нет** глобального аналога |
| **ICAO** | Межгосударственные стандарты (Annex 13, SMS) | Частично ISO/IEC, регуляторика (EU CRA, NIS2) — фрагменты |
| **IATA** | **Альянс перевозчиков**: стандарты, экономика, ops — не следователь | Ближе к отраслевым консорциумам (Linux Foundation, …), не к NTSB |
| **EASA / FAA** | Регулятор + принятие рекомендаций | Регуляторы + compliance в enterprise |

Авиация сильна не только «культурой отчёта», а **институциями кооперации** с mandate и публичными выводами.

---

## 2. Проблема SE: кооперация слабая или первертная

### Глобально

- **Нет** независимого «NTSB для всех prod incidents» — инциденты остаются внутри вендора/клиента.
- **Ассоциации разработчиков** (национальные, отраслевые) часто про networking, сертификации, конференции — **не** про расследование и обязательные recommendations.
- **Кооперация есть точечно**, когда есть **общий враг** (уязвимость) или **общий стандарт** (протокол, пакет).

### Россия — публичные роли институтов

| Субъект | Что делают (публично) | Ближе к NTSB? | Ближе к lobby/GR? |
|---------|----------------------|---------------|-------------------|
| **РУССОФТ** | ~382+ компаний; миссия — «продвижение интересов» разработчиков, GR, образование, экспорт | ❌ | ✅ (сами пишут про GR/lobbying) |
| **АРПП «Отечественный софт»** | Реестр отечественного ПО; **День РБПО**; комитет ИБ; аудит/документация по ГОСТ 56939, ФСТЭК | ❌ (не независимый следователь) | ⚠️ + **стандарты/аудит** (коммерческие услуги) |
| **АПКИТ** | ИТ-ассоциация, часто в одном пакете с РУССОФТ/АРПП в обращениях | ❌ | ✅ |
| **Минцифры ИТ-аккредитация** (ПП №1729, №1949) | Налоговые льготы; отчётность; с 2026 — обяз. соглашения об образовательной поддержке | ❌ | ⚠️ **государственный gate**, не отраслевое расследование |
| **НКЦКИ / ГосСОПКА** | Обязательное информирование о **киберинцидентах** (КИИ); расследование по ГОСТ Р 59711/59712 | ⚠️ **для ИБ-инцидентов**, не для «сломался релиз» | гос-контур |
| **ФСТЭК / БДУ** | Уязвимости, требования КИИ, методики | CVE-подобный слой | регулятор |

**Структурный вывод (по charter / регуляторике):**
- Отраслевые ассоциации RU — **GR, реестр, стандарты**, не независимый cross-vendor incident investigator.
- Кооперация по **ИБ** и регуляторике есть; **NTSB-style** learning для обычных software/platform failures — **нет**.
- Публичность отчётов слабее NTSB; значительный закрытый контур.

**Sources:** [russoft.org/general-information](https://russoft.org/general-information/) · [arppsoft.ru RBPO](https://arppsoft.ru/ie/22725/) · ПП РФ №1729/№1949 · ГОСТ Р 59711-2022 / 59712-2022

**Operator context (personal, не kb-public):** [`../../personal/operator-notes/note-operator-ru-it-cooperation-texture-2026-08-30.md`](../../personal/operator-notes/note-operator-ru-it-cooperation-texture-2026-08-30.md)

---

## 3. Зачатки кооперации в SE (реальные)

| Механизм | Что кооперируют | Сила | Слабость |
|----------|-----------------|------|----------|
| **CVE / CNA** | Уязвимости, идентификатор, severity | Глобальный namespace | Не все классы инцидентов; vendor delay; не architecture drift |
| **FIRST** | PSIRT / IR teams, обмен практиками | Сеть доверия | Закрытые комнаты, не публичный NTSB-отчёт |
| **GitHub/GitLab Advisories** | Supply chain в экосистеме | Масштаб | Платформенный lock-in, не нейтральный судья |
| **OpenSSF / Sigstore / SLSA** | Supply chain hygiene | Стандарты + tooling | Добровольность, зрелость неравномерна |
| **ISACs** (sector) | Отраслевой обмен угрозами | В regulated sectors | Закрыто, не для мелкого OSS |
| **Blameless postmortem** (SRE) | Культура в одной org | Глубина внутри | Не межорганизационно |
| **Conformance / spec tags** | Семантика протокола | **Проверяемо** | Нужен adoption |

**CVE — ближайший глобальный кооперативный примитив**, но он про **security disclosure**, не про «флот протоколов разъехался» или «модель врала».

---

## 4. Чего не хватает (cooperation gap)

1. **Независимый следователь** для типовых software/platform failures (не только CVE-worthy).  
2. **Mandatory near-miss** между организациями (как ASRS) для ecosystem friction.  
3. **Recommendations с adoption tracking** — кто внедрил, не press-release.  
4. **Нейтральный repository** фактов расследования (публичный, машиночитаемый).  
5. **Доверие к «альянсу»** — через CI/conformance, не через членский взнос.

---

## 5. Federation stance — кооперация без театра

Guiders federation **не** NTSB и **не** IATA. Это **добровольная кооперация планет** через:

| Примитив | Кооперативная функция |
|----------|------------------------|
| **Pain inventory** | Распределённый near-miss / friction report |
| **Adoption alliance** | Кто на каком pin — видимость, не NDA |
| **Conformance hyperlane** | Общий язык «что значит совместимо» |
| **Generated manifests + drift CI** | **Проверяемость** — не «поверьте альянсу» |
| **ADR + public docs** | Recommendation с git history |

**Отличие от membership-only альянса:** ценность = **machine-verified adoption**, любой может fork/check; embassy (Forge, CIDE) **доказывает** lane, не продаёт membership.

**Честный потолок:** без регулятора или industry-wide mandate это остаётся **opt-in confederation** — как CVE ecosystem, но для **protocol estate ops**.

---

## 6. Открытые вопросы

1. Связка pain G-xxx ↔ CVE workflow для security-class pains?  
2. ANPM как «CNA-подобный» узел для NuGet estate (owners, TP) — scope?  
3. Публичный investigation narrative format (NTSB-style) для federation incidents — ADR template?

---

## 7. Epistemic

| Claim | basis | confidence |
|-------|--------|------------|
| NTSB/AAIB independent safety investigation | statute + public record | high |
| IATA ≠ accident investigator | org charter / public role | high |
| No global software NTSB | industry structure survey | high |
| CVE/CNA as cooperative primitive | MITRE/CVE program docs | high |
| Dev associations often weak on investigation | literature + practice | medium |
| RU associations primarily GR/registry/standards | mission statements + public roles | high |
| RU IB/regulatory cooperation exists | НКЦКИ/ГОСТ/реестр | high |
| RU no NTSB-style SW incident authority | structure survey | high |
| Federation as verifiable opt-in coop | product design intent | inference |

- `falsification_trigger`: найти независимый cross-vendor software incident authority с публичными NTSB-style reports → пересмотреть §4 gap
- `transfer_boundary`: не политика; не юридическая advice
- **Agent contract:** L0 `epistemic-default-distrust-v1` — [`epistemic-default-distrust-extended.md`](../../epistemic-default-distrust-extended.md); operator claims → `personal/operator-notes/`, не kb-public

