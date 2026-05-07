# Human perception — scientific evidence (first sources & reviews) v1

## Provenance

- source_refs:
  - paper: Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review*, *63*(2), 81–97. https://doi.org/10.1037/h0043158
  - paper: Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, *24*, 87–185. https://doi.org/10.1017/S0140525X01003922
  - chapter: Baddeley, A. D., & Hitch, G. (1974). Working memory. In G. H. Bower (Ed.), *The psychology of learning and motivation* (Vol. 8, pp. 47–89). Academic Press. (часто цитируемый первоисточник мультикомпонентной РП; полный текст — по библиотеке)
  - paper: Baddeley, A. (2000). The episodic buffer: A new component of working memory? *Trends in Cognitive Sciences*, *4*(11), 417–423. https://doi.org/10.1016/S1364-6613(00)01538-2
  - book: Broadbent, D. E. (1958). *Perception and communication*. Pergamon Press. (ранняя модель «узкого места» и фильтра внимания)
  - paper: Treisman, A. (1969). Strategies and models of selective attention. *Psychological Review*, *76*(3), 282–299. https://doi.org/10.1037/h0027242
  - paper: Treisman, A., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, *12*, 97–136. https://doi.org/10.1016/0010-0285(80)90005-5
  - book: Kahneman, D. (1973). *Attention and effort*. Prentice-Hall. (ёмкость/усилие, связь с нагрузкой; монография без единого DOI как у статьи)
  - paper: Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, *12*(2), 257–285. https://doi.org/10.1207/s15516709cog1202_4
  - paper: Sweller, J., van Merriënboer, J. J. G., & Paas, F. G. W. C. (1998). Cognitive architecture and instructional design. *Educational Psychology Review*, *10*(3), 251–296. https://doi.org/10.1023/A:1022193728205
  - paper: Wickens, C. D. (2008). Multiple resources and mental workload. *Human Factors*, *50*(3), 449–475. https://doi.org/10.1518/001872008X288394
  - paper: Simons, D. J., & Levin, D. T. (1997). Change blindness. *Trends in Cognitive Sciences*, *1*(8), 261–267. https://doi.org/10.1016/S1364-6613(97)01080-2
  - paper: Simons, D. J., & Chabris, C. F. (1999). Gorillas in our midst: Sustained inattentional blindness for dynamic events. *Perception*, *28*(9), 1059–1074. https://doi.org/10.1068/p281059
  - paper: Eysenck, M. W., Derakshan, N., Santos, R., & Calvo, M. G. (2007). Anxiety and cognitive performance: Attentional control theory. *Emotion*, *7*(2), 336–353. https://doi.org/10.1037/1528-3542.7.2.336
  - cross_ref: продуктовые эвристики UI (Norman, Nielsen, …) — `kb-ui-ux-literature-evidence-v1.md`; HCI-операционка — `playbook-hci-core-v1.md`
- created_at: 2026-04-20
- updated_at: 2026-04-20
- extraction_note: библиография и формулировки ключевых тезисов сверены через открытые описания и DOI; для **Miller (1956)** и **Treisman & Gelade (1980)** — отдельные **evidence-карточки** (`kb-human-perception-*-evidence-v1`, тот же контракт, что `kb-*-evidence-v1`): извлечённое проверяемое знание (тезисы, механизмы, границы переноса), не дословные цитаты (см. §8 ниже).

## Metadata

- card_id: kb-human-perception-scientific-evidence-v1
- world: cognition.human-perception
- layer: knowledge
- tags: [perception, attention, working-memory, cognitive-load, change-blindness, inattentional-blindness, human-factors, evidence, first-sources]
- status: active

## Epistemic linkage

- epistemic_basis: literature_synthesis
- evidence_type: peer-reviewed papers and canonical books (bibliographic + conceptual summary)
- confidence: medium-high for «что утверждает традиция»; medium for количественные обобщения (ёмкость, проценты в демо)
- transfer_boundary: когнитивная психология и HF — **не** нейроклиника и **не** замена A/B-тестов продукта; применение к IDE/UX — инженерная экстраполяция.
- falsification_trigger: мета-анализ или крупный сдвиг модели (например, радикальный пересмотр CLT или единой ёмкости РП) — пересмотреть разделы и даты.

---

## Зачем этот файл

Слой **fundamentals** (`kb-human-perception-fundamentals-v1.md`) даёт рабочие формулировки; этот документ — **научные якоря**: кто и в каком жанре доказал/ввёл идею, с DOI где возможно. Используй для обоснования ревью, споров о приоритете внимания и для дальнейшего чтения первоисточников.

---

## 1. Ограничение ёмкости и «магические числа»

| Источник | Суть для UX/инструментов |
|----------|----------------------------|
| **Miller (1956)** | Классическая статья про **одновременные категорийные суждения** и **немедленную память**: люди рекодируют вход в **чанки**; «7±2» — не универсальная константа для всех задач, а иллюстрация того, что **без перекодирования** канал узок. Для интерфейса: именование, группировка и паттерны — способы увеличить эффективный объём **за счёт смысла**, а не пикселей. |
| **Cowan (2001)** | Пересмотр: в фокусе внимания/ядре РП часто **~4 объекта** (диапазон 3–5), а не «семь слотов»; «семь» смешивали разные уровни (чанки vs элементы). **Вывод для UX:** не опираться на «7 пунктов меню» как на физику; проверять сценарии и сложность чанка. |

**Факты (устойчивые):** ограниченный канал между сенсорным потоком и осознанным удержанием; чанкинг и схемы в ЛП снижают нагрузку на РП.

**Нюанс:** дискуссии BBS вокруг Cowan — про механизмы (фокус внимания vs хранение); для продукта важнее **повторяемость в задаче**, чем одно число.

---

## 2. Рабочая память как мультикомпонентная система

| Источник | Суть |
|----------|------|
| **Baddeley & Hitch (1974)** | Вместо одной «короткой памяти» — **центральный исполнитель** + подсистемы (фонологическая петля, визуально-пространственный блокнот). Двойные задачи в разных модальностях **меньше** мешают друг другу, чем в одной — отсюда логика **разнести каналы** (например, речь vs карта) при осторожности с перегрузом одного канала. |
| **Baddeley (2000)** | **Эпизодический буфер** — интеграция фрагментов в единое эпизодическое представление; сознательный доступ. Для сложных UI: **связка** статуса, действия и последствия в одном «эпизоде» внимания лучше, чем три разрозненных сигнала без связи. |

---

## 3. Внимание: от фильтра к интеграции признаков

| Источник | Суть |
|----------|------|
| **Broadbent (1958)** | Исторически важная **ранняя селекция** и **бутылочное горлышко**; дихотическое слушание. Полезно помнить: **конкуренция каналов** — не метафора, а проверенная парадигма (хотя «полная блокировка» необработанного смысла позже смягчалась). |
| **Treisman (1969)** | Обзор стратегий и моделей **избирательного внимания**; мост от фильтра к более гибкой обработке. |
| **Treisman & Gelade (1980)** — *feature integration theory* | **Параллельная** регистрация простых признаков (цвет, ориентация) vs **серийное** сопоставление **конъюнкций** признаков для идентификации объекта. **Pop-out** одиночного признака vs медленный поиск конъюнкции. **UX:** «выделить одним атрибутом» (цвет, форма) дешевле для поиска, чем «найди красный квадрат среди красных кругов и синих квадратов»; иллюзии **ложных конъюнкций** при отвлечённом внимании — аргумент за явное связывание подписи и объекта. |

---

## 4. Усилие, ресурсы и когнитивная нагрузка

| Источник | Суть |
|----------|------|
| **Kahneman (1973)** | Внимание связано с **усилием**; ограниченный ресурс и взаимодействие с ароусалом (в т.ч. инверсия Yerkes–Dodson обсуждается в традиции нагрузки). Двойные задачи конкурируют за общий ресурс, если не автоматизированы. |
| **Sweller (1988)** | Начало **cognitive load theory** в связке с обучением: схемы в ДП, ограничение РП; means-ends анализ может съедать ресурс, не оставляя на построение схем. |
| **Sweller, van Merriënboer & Paas (1998)** | Явное разложение **intrinsic / extraneous / germane** (нагрузка от задачи vs от плохого представления vs от осмысленного построения схем). Для UI: снижать **extraneous** (шум, лишние шаги); не путать «ещё одно окно» с germane. |
| **Wickens (2008)** | Свод по **multiple resource theory**: разные виды ресурсов (модальности, коды, стадии обработки, визуально vs вербально по расширенным моделям); частичная **независимость** каналов объясняет, когда два потока совместимы. Для кокпита/IDE: разнести конфликтующие запросы к одному и тому же ресурсу. |

---

## 5. Слепота к изменениям и слепота при фокусе на задаче

| Источник | Суть |
|----------|------|
| **Simons & Levin (1997)** | Обзор **change blindness**: без локализуемого трансиента/фиксации люди часто **не замечают крупные изменения** сцены; мало деталей хранится между взглядами. **UX:** критический статус нельзя «спрятать в том же слое», что и фон, без явного маркера. |
| **Simons & Chabris (1999)** | **Inattentional blindness**: при счётной/фокусной задаче значительная доля наблюдателей не замечает неожиданный стимул (классика с «гориллой»). Заметность зависит от **задания**, **сходства** дистрактора и **набора внимания**, а не только от салиентности на сетчатке. **UX:** «неожиданное» в зоне задачи всё равно может быть пропущено, если оно не вписано в цель пользователя. |

---

## 6. Стресс, тревога и контроль внимания

| Источник | Суть |
|----------|------|
| **Eysenck et al. (2007)** — *attentional control theory* | Тревога смещает баланс в сторону **стимул-управляемого** внимания и снижает эффективность **целе-направленного** контроля (ингибирование, переключение). Эффективность результата может сохраняться за счёт компенсаторного усилия. **UX (осторожная экстраполяция):** под нагрузкой пользователь хуже переносит «умные» отвлечения и хрупкий фокус; тихие режимы и предсказуемость критичнее, чем в среднем кейсе. |

---

## 7. Краткая таблица «идея → первоисточник/обзор»

| Идея | Куда смотреть |
|------|----------------|
| Чанки и перекодирование | Miller (1956); уточнение ёмкости — Cowan (2001) |
| Вербальный vs визуально-пространственный поток | Baddeley & Hitch (1974); интеграция — Baddeley (2000) |
| Ранний отбор и конкуренция каналов | Broadbent (1958); обзор моделей — Treisman (1969) |
| Поиск объекта по признаку vs конъюнкция | Treisman & Gelade (1980) |
| Ресурс внимания и усилие | Kahneman (1973) |
| CLT и типы нагрузки | Sweller (1988); Sweller et al. (1998) |
| Несколько ресурсов при мультизадачности | Wickens (2008) |
| Change blindness | Simons & Levin (1997) |
| Inattentional blindness | Simons & Chabris (1999) |
| Тревога и внимание | Eysenck et al. (2007) |

---

## 8. Evidence-карточки по первоисточникам

Семантические имена: `kb-human-perception-<работа>-evidence-v1.md` — тот же слой, что прочие **`kb-*-evidence-v1`** (см. `template-knowledge-card-v1.md`, `META/provenance-contract-v1.md`). Содержимое: **проверяемые тезисы**, методы, ограничения, UX-мост; дословные цитаты в KB не обязательны.

| Работа | Файл |
|--------|------|
| Miller (1956) *Psychological Review* | [`kb-human-perception-miller-1956-evidence-v1.md`](kb-human-perception-miller-1956-evidence-v1.md) |
| Treisman & Gelade (1980) *Cognitive Psychology* | [`kb-human-perception-treisman-gelade-1980-evidence-v1.md`](kb-human-perception-treisman-gelade-1980-evidence-v1.md) |

---

## Связанные артефакты канона

- Фундаментальные формулировки без разбора по авторам: `kb-human-perception-fundamentals-v1.md`
- Операционные чеклисты: `playbook-human-perception-operational-v1.md`
- Мир: `worlds/cognition-human-perception/README.md`

*Версия документа: v1.3 · 2026-04-20 — §8: evidence-карточки, семантические имена `*-evidence-v1`*
