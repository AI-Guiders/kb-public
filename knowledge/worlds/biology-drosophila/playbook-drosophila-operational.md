---
type: Playbook
title: Playbook — работа с миром biology.drosophila (operational)
description: '**world-id:** `biology.drosophila` · **Статус:** operational (2026-09-19)'
tags: [biology-drosophila, worlds, playbook, operational, data, connectome]
language: ru
world: biology
subworld: drosophila
---
# Playbook — работа с миром biology.drosophila (operational)

**world-id:** `biology.drosophila` · **Статус:** operational (2026-09-19)
**Связано:** [kb-drosophila-connectome.md](kb-drosophila-connectome.md) (fundamentals), [README.md](README.md)

---

## 1. Карта данных (локально)

**Корень:** локальный каталог коннектомов (вне kb; полный набор BANC v888 / MCNS v1.0 / FAFB v783)

| Данные | Файлы | Формат | Что можно |
|--------|-------|--------|-----------|
| BANC ♀ v888 | `banc-v888/` | feather/parquet/csv | граф, NT, кластеры, междуность |
| — edgelist | `edgelist_simple_v3.feather` (342 MB), `edgelist_split_v3` (897 MB) | pre/post/count | поток, степени, топ-связи |
| — meta | `banc_888_meta.feather` (55 MB) | 188 508 нейронов | классы, регионы, hemilineage, типы |
| — NT | `neurotransmitter_prediction_v2.csv` (20 MB) | 169 635 нейронов | NT-профили |
| — междуность | `betweenness_*_v2/v3.csv` | 100–141k вершин | хабы потока |
| — кластеры | `spectral_clustering_v2/v3.csv` | 55 633 нейрона, 13 кластеров | модульность |
| — синапсы | `synapses_v3_enriched.parquet` (18.8 GB) | полные синапсы | синаптический уровень |
| — proofread-граф | `proofread_influence.sqlite` (690 MB) | 143 837 нейронов, 11.48M рёбер | надёжное подмножество |
| — скелетоны | `neuron_skeletons.zip` (206 MB) | SWC | морфология |
| FAFB ♀ v783 | `fafb-v783/` | feather | мозг 139k, 8 453 типов |
| MCNS ♂ v1.0 | `mcns-v1.0/` | feather | 166 691 нейронов, диморфизм, fru/dsx |
| Статья | `repos/BANC-project/` | R/manuscript/numbers.csv | официальные числа (293 строки!) |
| Туториал | `repos/fly_connectome_data_tutorial/` | README + data | методики, кросс-датасет |

## 2. Проверенные рецепты (python + pandas/pyarrow)

```python
# NT-профиль BANC
n = pd.read_csv("banc-v888/banc_888_neurotransmitter_prediction_v2.csv")
n["neurotransmitter_predicted"].value_counts()

# Поток по классам (v2)
el = pd.read_feather("banc-v888/banc_888_edgelist_simple_v3.feather")
meta = pd.read_feather("banc-v888/banc_888_meta.feather")
el.merge(meta[["root_id","flow"]], left_on="pre", right_on="root_id") ... # см. kb-drosophila-connectome.md

# Хабы потока
b = pd.read_csv("banc-v888/banc_888_betweenness_afferent_to_efferent_v3.csv")
b.nlargest(10, "betweenness")[["cell_type","super_class"]]

# Диморфизм MCNS
a = pd.read_feather("mcns-v1.0/body-annotations-male-cns-v1.0-minconf-0.5.feather")
a["dimorphism"].value_counts(); a["fruDsx"].value_counts()

# Proofread-граф (SQLite)
sqlite3.connect("banc-v888/banc_888_proofread_influence.sqlite")  # meta, edgelist_simple
```

## 3. Инструменты

| Инструмент | Назначение |
|------------|-----------|
| `aria2c --input-file=manifest` | докачка (манифест в корне) |
| python + pandas/pyarrow | анализ (feather/parquet/csv) |
| sqlite3 | proofread-граф, запросы |
| **dbhub** (`bancProofread`, после рестарта) | SQL-запросы через MCP |
| BANC-project R scripts | воспроизведение фигур статьи |
| `ConnectomeInfluenceCalculator` (Zenodo) | influence-метрика (не качали 287 GB — избыточно) |
| `cocoa` (flyconnectome) | кросс-датасетное сравнение связности |
| Codex / neuPrint / banc.community | интерактив (Google sign-in для tool'ов) |

## 4. Вопрос → ответ (что мир закрывает)

| Вопрос | Ответ где |
|--------|-----------|
| Сколько нейронов/синапсов | слой 3: 188 508 / 199M (BANC), 166 691 (MCNS), 139k (FAFB) |
| Кто хабы потока | слой 3: DNc01/DNb05/MeLp1/AN19B001 (подтверждено v3) |
| Как устроен поток | слой 7: 16.8k→8.8k→1k пирамида, 3 хода |
| Что диморфно | слой 5: 2 368 нейронов, fru/dsx ~5 000 |
| Как обучается | слой 4/5: MB + DAN-учитель (36.7 KC выходов) |
| Что зафиксировано эволюцией | слой 6: поток/модули/НТ; пластично: MB/CX |
| **Где границы честности** | слой 7: 18% связность, 155 884 proofread, VNC 0.3% match, нет ламины/сетчатки |

## 5. Что не закрыто (честно)

- **Функция большинства типов** (9.3% AN/DN с известной модальностью) — мир знает структуру, не функцию
- **Кросс-датасетные выводы** — VNC-соответствие 0.3%, типы неполны (533 missing)
- **Поведение↔структура** — связка требует поведенческих экспериментов (литература, слой 5 — каркас)
- **influence/all_to_all (287 GB)** — не качаем; междуность v3 покрывает хабы

## 6. Как использовать для CASA (после синтеза, M6)

1. Сверить законы 1–6 с CASA-зонами (поток/модули/обучение/модуляция/генетика/инварианты)
2. Вопросы к зонам: «у нас bottleneck выхода?», «обучение — отдельный модуль?», «модуляция — каналы усиления?»
3. Законы как **проверяемые инварианты** (не как «вдохновение»): CASA-архитектура должна отвечать на них фактами

