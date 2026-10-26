---
type: KB
title: Voyager 1 & 2 · межзвёздная миссия — карточка статуса (v1)
description: '**Область:** внешний эталон (NASA/JPL), не `mt-lattice-fluid`.'
tags: [reference, spacecraft, voyager, interstellar, NASA, science, kb]
language: ru
---

# Voyager 1 & 2 · межзвёздная миссия — карточка статуса (v1)

**Область:** внешний эталон (NASA/JPL), не `mt-lattice-fluid`.  
**Снимок карточки:** **2026-09-26** (операторский синтез + открытые источники).  
**Обновлять:** [Voyager mission status](https://science.nasa.gov/mission/voyager/) · [Where are Voyager 1 and 2 now?](https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/) · [JPL Horizons](https://ssd.jpl.nasa.gov/horizons.cgi).

---

## 1. Роль зондов

| | Voyager 1 | Voyager 2 |
|---|-----------|-----------|
| Heliopause | **2012-08-25** (~121.6 au) | **2018-11-05** (~119 au) |
| Траектория | вне ecliptic (север) | южнее ecliptic |
| Связь | DSN, **one-way light-time ~1 сут** | то же |
| Downlink | X-band science ~**160 bit/s** (типично); engineering S-band | то же |

**Не путать:** «вышли из heliosphere» ≠ «покинули Solar System» (Oort — другой горизонт, FAQ NASA).

---

## 2. Дистанция (ориентиры 2026)

- **V1** — самый дальний аппарат; NASA milestone **1 light-day** ≈ **25.9×10⁶ km**, **~173 au** от Земли — **2026-11-18** ([NASA](https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/)).
- **Конец сентября 2026:** порядка **~172 au** от Земли (точная эпоха — **Horizons**).
- Скорость порядка **~17 km/s** от Солнца (медленно меняется).

---

## 3. Science instruments (таблица NASA, 2026)

| Instrument | V1 | V2 |
|------------|----|----|
| **MAG** (магнитометр) | **ON** | **ON** |
| **PWS** (плазменные волны → **n_e**) | **ON** | **ON** |
| **CRS** (косм. лучи) | OFF (экономия **2025-02**) | **ON** |
| **LECP** | OFF (**2026-04-17**) | OFF (**2025-03**) |
| **PLS** | off (degraded) | off (экономия **2024-09**) |
| Cameras, UV, IR… | off десятилетиями | off |

**События 2025–2026:**

- V1: отключение **LECP** — [NASA blog 2026-04-17](https://science.nasa.gov/blogs/voyager/2026/04/17/nasa-shuts-off-instrument-on-voyager-1-to-keep-spacecraft-operating/).
- V2: **«Big Bang»** power swap — продление **3** приборов **≥ ~1 год** — [2026-08-04](https://science.nasa.gov/blogs/voyager/2026/08/04/nasa-engineers-help-prolong-voyager-2s-science-mission/); аналог планировали на V1 после успеха на V2.

RTG: **~−4 W/год** на зонд; приоритет — сохранить fields & particles в VLISM.

---

## 4. Последние **опубликованные** научные выводы (телеметрия идёт непрерывно)

### Voyager 1 (MAG + PWS, VLISM)

| Величина | Значение / тренд | Примечание |
|----------|------------------|------------|
| **|B|** | **~0.45–0.53 nT** (daily avg) | до **~mid-2025** в литературе |
| Ориентация **B** | поворот к **Parker spiral** | post–magnetic hump |
| Интермитентность | после hump **~2020** — близко **Gaussian** | contrast с heliosheath |
| **n_e** (PWS) | **~0.147 cm⁻³** плато | после pulse **~2020** @ **~149 au**; [ApJL 2024/25](https://iopscience.iop.org/article/10.3847/2041-8213/ad2617) |
| MAG evolution | [ApJ 2025](https://iopscience.iop.org/article/10.3847/1538-4357/ae63ba) — mid-2025 analysis |

### Voyager 2

Те же классы величин в своём канале VLISM; **CRS** ещё даёт частицы, пока на V1 CRS/LECP выключены.

**Lag:** peer-reviewed статьи отстают от engineering telemetry на **месяцы–годы**; оперативные daily plots — NASA mission pages / PDS archives.

---

## 5. Прогноз связи

NASA FAQ (обновляемый): инженерный контакт **возможен до ~2036** в зависимости от RTG и DSN; science instruments отключаются по одному раньше.

---

## 6. Epistemic note (KB)

- Цифры дистанции для **конкретной даты** — только из **Horizons** или официального NASA pulse, не из чата.
- «Последние данные» = **downlink exists** + **last published analysis** (разные даты).

---

## 7. Seed

```text
INBOX: refresh Voyager card after NASA instrument table change
Check: science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/
```

