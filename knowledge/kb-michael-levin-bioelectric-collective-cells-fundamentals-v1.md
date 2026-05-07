# Michael Levin — биоэлектричество и коллективный интеллект клеток: fundamentals v1

**Назначение:** сжатый теоретический каркас работ **Michael Levin** (Tufts, Allen Discovery Center и др.), релевантный треку [`ca-substrate-agent`](work/projects/door-to-singularity/ca-substrate-agent/README.md): распределённые вычисления в тканях, **регенерация**, навигация в **пространстве морфологий**, связь «простых правил / сигналов» с **глобальной формой** без центрального «мозга ткани».

**Operational (что делать при проектировании CA/NCA экспериментов):** [`playbook-casa-levin-biology-bridge-operational-v1.md`](playbook-casa-levin-biology-bridge-operational-v1.md).

---

## Provenance и первичные источники

- Лаборатория: [The Levin Lab](https://drmichaellevin.org/), раздел Research — формулировки про *collective intelligence of cells*, *bioelectricity*, *morphogenesis as navigation*.
- Ключевая синтезирующая статья (англ., open access): Levin, M. (2019). *The Computational Boundary of a “Self”: Developmental Bioelectricity Drives Multicellularity and Scale-Free Cognition.* **Frontiers in Psychology** 10:2688. DOI [10.3389/fpsyg.2019.02688](https://doi.org/10.3389/fpsyg.2019.02688); PMCID [PMC6923654](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6923654/).
- Свежий обзорный текст по линии «collective intelligence of the body» (для биомедицинского контура): Levin, M. (2025). *The Multiscale Wisdom of the Body: Collective Intelligence as a Tractable Interface for Next‐Generation Biomedicine.* **BioEssays**. DOI [10.1002/bies.202400196](https://doi.org/10.1002/bies.202400196).

Детали молекулярных механизмов, клинических протоколов и этики здесь **не дублируются** — только то, что помогает **информационной** интерпретации для CASA.

---

## 1. Тезис коллектива: клетки как рой с общей задачей

- Метazoа строят и **ремоделируют** анатомию при шуме и повреждениях: результат — не «случайный эмерджент» из статичного синтеза белка, а **пластическая** координация к большому **таргету формы** (регулятивное развитие, примеры регенерации, движение органов к инвариантной конфигурации — см. обзор экспериментов в литературе Levin / Pezzulo & Levin).
- В этой оптике **морфогенез и ремонт** читаются как поведение **коллективного агента**: клетки решают задачи в **разных пространствах состояний** (транскриптомное, физиологическое, **анатомическое / morphospace**).
- Связано с традицией **basal cognition** / **proto-cognition**: когнитивные метаформы не «дар человеку», а **шкала способностей** от простых петель гомеостаза к сложному поведению (без утверждений о квалиа в текстах Levin для инженерного чтения).

**Для CASA:** искать **формальные аналоги**: локальное обновление + сигналинг → стабильный **macrostate** («целевая топология поля»), устойчивость к повреждению блока состояния.

---

## 2. Developmental bioelectricity и «биоэлектрический код»

- **Биоэлектричество развития** — медленные **ионные** сигналы, ** Vm / resting potential**, связи через gap junctions и др.: не только нейроны, а **широкий эпителий и других соматических клеток**.
- Интерпретация в лаборатории: эти поля участвуют в **хранении и передаче информации**, задающей **крупномасштабный** паттерн (ось, орган, масштаб), в связке с транскрипцией и механикой — «**reading and writing**» морфогенетического/биоэлектрического кода как **инженерная** метафора для вмешательств (не микроменеджмент каждого гена).

**Для CASA:** отдельные **каналы состояния** клетки (как скрытые каналы в NCA) можно мыслить как **немолекулярный** аналог «химического / электрического» резервуара для согласования с соседями; это **аналогия уровня модели**, не отождествление с Vm.

---

## 3. Scale-free cognition и граница «Self»

- В работе 2019 года вводится рамка **Scale-Free Cognition**: попытка **сравнимо** описывать агентов разной природы через **пространственно-временную границу** наблюдаемых и контролируемых событий — своего рода «**когнитивная light cone**» субъекта.
- Мультиклеточность и опухолевое «выключение из сети» подаются как сдвиг **масштаба целей** у «частей»: от участия в телесном homeostasis к локальному max-per-cell — не как морализаторство, а как **сдиг границы Self** в информационной модели.

**Для CASA:** явно решать в модели, **кто является агентом** — одна клетка, патч, всё поле; как определяется **loss на границе** коллектива vs локальный шаг (см. also pool training / маски в Growing NCA).

---

## 4. Collective intelligence of morphogenesis (формулировка для литературы)

- Levin неоднократно задаёт морфогенез как **модельную систему** для изучения **масштабирования** коллективного интеллекта («**cognitive glue**» между уровнями, политики согласования частей с целым).
- Это сознательный мост к **робототехнике, ИИ и ALife**: один класс объектов — **агентный материал** (engineering with agential materials).

**Для CASA:** гипотеза не «клетки = мини-ЧГПТ», а «**клеточный материал = субстрат**, на котором естественны **аттракторы формы**, **регенерация** и **демаркация активной области**» — см. технические приёмы в [`kb-distill-growing-neural-ca-fundamentals-v1.md`](kb-distill-growing-neural-ca-fundamentals-v1.md).

---

## 5. Публичные лекции (точки входа; подбор под запрос про *Collective Intelligence*)

Упорядочено от **узкого** названия к более широкому контексту. Полный архив докладов поддерживается на [drmichaellevin.org/presentations](https://drmichaellevin.org/presentations).

| Угол | Заголовок (как у автора / в программе) | Ссылка | Примерная длительность |
|------|----------------------------------------|--------|-------------------------|
| Прямое попадание в формулировку | **Understanding the Collective Intelligence of Cells** (Distinguished Lecture, University of Sydney) | https://youtu.be/MdOHSUMb214 | ~1 ч 28 мин |
| Морфогенез как система для basal cognition | **The Collective Intelligence of Morphogenesis: a model system for basal cognition** (Lund University) | https://www.youtube.com/watch?v=JAQFO4g7UY8 | ~58 мин |
| Связка «нейро» ↔ соматическая сеть | **Neuroscience beyond neurons: bioelectric basis of basal cognition in morphogenesis** (Math Neuro symposium) | https://www.youtube.com/watch?v=X8qAkqJTNHc | ~45 мин |
| Масштабирование коллективного интеллекта и ИИ | **Where Minds Come From: the scaling of collective intelligence, and what it means for AI and you** | https://www.youtube.com/watch?v=44W9Mw4AGT8 | ~45 мин |
| Очень короткий вход | **Can cells think?** — сегмент с Levin | https://www.youtube.com/watch?v=0a3xg4M9Oa8 | ~8 мин |
| Свежий синтез (2026 в списке сайта) | **The Bioelectric Interface to the Collective Intelligence of Morphogenesis** (UCSF Seminar) | https://www.youtube.com/watch?v=L0D4FdJ4K3g | ~58 мин |

---

## 6. Ограничения переноса в ИИ на CA

- Биология **не задаёт уникальных** уравнений для успешной NCA/CASA: это **метапринципы** (робастность формы, согласование, граница «живых» узлов).
- Levin опирается на **электросигнатуру живой материи**, эволюцию и химический контекст; **силиконовая** симуляция обязана **явно документировать**, какие элементы биологии модель сознательно **отрезает** (иначе смешение уровней валидации).
- Утверждения про сознание / субъективность в выступлениях Levin **выходят за пределы** минимальной инженерной постановки CASA для первых прототипов.

---

## Связные материалы в каноне

- Карточка CASA: [`ca-substrate-agent/README.md`](work/projects/door-to-singularity/ca-substrate-agent/README.md).
- Мост fundament → эксперименты: [`playbook-casa-levin-biology-bridge-operational-v1.md`](playbook-casa-levin-biology-bridge-operational-v1.md).
- Вычислительный конкретный параллель (рост паттерна в NCA): [`kb-distill-growing-neural-ca-fundamentals-v1.md`](kb-distill-growing-neural-ca-fundamentals-v1.md).

---

*Confidence по отсылке к опубликованным тезисам Levin (2019 Frontiers + обзоры лаборатории):* **high**. *Релевантность для реализации агента CASA через конкретную архитектуру:* рабочая эвристика трека, не доказанный редукционизм «клетка = тензор в CA».
