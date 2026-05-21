# Авиация: PFD, MFD, EFIS, EICAS/ECAM — фундамент для метафоры Cascade IDE

**Назначение:** единая точка в KB: что означают термины в **реальной авионике**, откуда брать **первоисточники**, и как это **сопоставлять** с ADR проекта Cascade IDE (не путать роль зоны в IDE с буквальным прибором).

**Связь с продуктом:** ADR 0021 лежит в репозитории IDE (не в agent-notes): при workspace **PersonalCursorFolder** — `Financial/software/open/cascade-ide/docs/adr/0021-pfd-mfd-cockpit-attention-model.md`.

**Статус:** v1, справочно. Не заменяет FCOM/QRH операторов.

---

## 1. EFIS (Electronic Flight Instrument System)

В типичном описании **EFIS** включает:

- **PFD** — первичный полёт;
- **MFD** и/или **ND** (navigation display) — навигация и прочее в зависимости от типа;
- **EICAS** (Boeing-стиль) или **ECAM** (Airbus) — двигатели, системы, предупреждения экипажа.

**Первоисточники и обзоры:**

| Источник | Ссылка | Заметка |
|----------|--------|---------|
| Wikipedia — *Electronic flight instrument system* | https://en.wikipedia.org/wiki/Electronic_flight_instrument_system | Сводная схема PFD / MFD / EICAS в одном абзаце |
| FAA — *Pilot's Handbook of Aeronautical Knowledge* (PHAK), глава 8 *Flight Instruments* | https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak — отдельно [Chapter 8 PDF](https://www.faa.gov/regulationspolicies/handbooksmanuals/aviation/phak/chapter-8-flight-instruments) | Официальный учебник пилота (США), стеклянная кабина / современные приборы |
| FAA — *Advanced Avionics Handbook* (FAA-H-8083-6) | PDF на govinfo / раздел Advanced Avionics на faa.gov | Подробнее про glass cockpit, PFD/MFD, сценарии отказов, резервирование |

---

## 2. PFD (Primary Flight Display)

**Смысл:** один экран с **критичными параметрами удержания полёта**: attitude, скорость, высота, курс, вертикальная скорость и т.п. — то, без чего нельзя безопасно продолжать полёт по приборам.

**Идея для IDE (ADR):** «где я в задаче / workspace» и **не отвлекать** от главного — не сваливать сюда вторичные длинные потоки.

**Ссылки:** PHAK Ch.8; Wikipedia [Primary flight display](https://en.wikipedia.org/wiki/Primary_flight_display).

---

## 3. MFD (Multi-Function Display)

**Смысл:** дисплей с **несколькими страницами/режимами** — карта, погода, системы, трафик и т.д.; часто **мягкие клавиши** или переключение страниц; не всё одновременно, чтобы не раздувать панель.

**Идея для IDE (ADR):** вторичные инструменты, **переключаемые страницы** (чат, терминал, логи, git, отладка) — не конкурируют с «лобовым» редактированием за постоянный фокус.

**Ссылки:** Wikipedia [Multi-function display](https://en.wikipedia.org/wiki/Multi-function_display).

---

## 4. Важно: Airbus A320 — не всегда слово «MFD»

У **Airbus A320 family** в публичных материалах чаще фигурирует:

- **EFIS:** **PFD** + **ND** (Navigation Display) на боковых панелях;
- **ECAM:** верхний дисплей E/WD (engine/warning) + нижний SD (system display), страницы систем.

То есть «второй экран» у каждого пилота — это прежде всего **ND** и логика **ECAM**, а не обязательно маркетинговый термин **MFD** как в учебниках GA (G1000 и т.д.). Для **вдохновения раскладкой** полезны открытые брифинги Airbus (например брошюры *Flight deck and systems briefing* — **не** замена РЛЭ), технические обзоры ATA 31.

**Резервирование (идея, не дословно):** при отказе PFD часть систем может **переносить образ PFD на ND** — аналог «критичное на запасной поверхности»; в IDE это метафора **не дублировать** критичный контекст бесконтрольно, а осознанно переключать.

---

## 5. EICAS vs ECAM

| Система | Где типично | Роль |
|---------|-------------|------|
| **EICAS** | Boeing и др. | Engine Indicating and Crew Alerting — двигатели + **иерархия предупреждений** |
| **ECAM** | Airbus | Централизованный мониторинг + **страницы** систем + предупреждения |

В ADR 0021 **EICAS** используется как имя **канала** предупреждений (W/C/A), не обязательно копия Boeing.

---

## 6. Сопоставление с Cascade (кратко)

| Авионика | Cascade (ADR 0021) |
|----------|---------------------|
| Лобовое стекло / forward | Редактор, HUD inline |
| PFD | Зона `pfd`: контекст workspace (обозреватель, «где мы») |
| MFD | Зона `mfd`: вкладки/страницы вторичного (чат, терминал, git, …) |
| EICAS/CAS | Канал оповещений — не «четвёртая колонка инструментов», а политика приоритета |

**Не смешивать:** пространственный **якорь** зоны и **канал** телеметрии/EICAS — см. §1.1 ADR 0021 в репозитории IDE.

---

## 7. Что не класть в KB как «факты полёта»

- Полные **FCOM / QRH / РЛЭ** конкретного оператора — **проприетарны**, в канон не копировать.
- Случайные слайды и форумы — только с пометкой «не первоисточник».

---

## 8. История версий

- **v1** (2026-04-05): первый заход; ссылки FAA PHAK / Advanced Avionics; Wikipedia; оговорка Airbus PFD/ND/ECAM; канон — **agent-notes** (`AGENT_NOTES_CANON_PATH`).
