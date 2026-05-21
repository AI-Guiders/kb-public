# Playbook: Grafana (v1)

> **Scope:** типовые задачи админа Grafana — дашборды, источники данных, алерты. Без привязки к конкретным инстансам и паролям. Глубокий справочник: `kb-grafana-reference-v1.md`.

---

## Ключевые понятия

- **Дашборд:** набор панелей и визуализаций; данные из одного или нескольких data source.
- **Data source:** подключение к хранилищу (Prometheus, InfluxDB, MySQL, Zabbix через плагин и т.д.). Редактор запросов свой у каждого типа.
- **Алерт:** правило по запросу и условию; при срабатывании — уведомление через контактные точки (contact points). Маршрутизация — по политикам уведомлений (notification policies) и меткам (labels).

---

## Где что в UI

- **Шестерёнка (⚙️)** → Administration: Data Sources, Users, Teams, Plugins, Provisioning.
- **Data Sources** — добавление/правка источников (только Organization Admin).
- **Дашборд:** Settings — переменные, аннотации, теги; Edit — панели и запросы.
- **Alerting** — правила алертов, контактные точки, политики уведомлений, тишины (silences).

---

## Типовые задачи

- **Добавить источник:** Configuration → Data Sources → Add; тип (Prometheus, Loki, Tempo, InfluxDB, MySQL и т.д.), URL, при необходимости auth; Save & Test. Только Organization Admin может добавлять/редактировать data sources.
- **Нет данных на панели:** проверить data source (Test), запрос (синтаксис, временной диапазон), права доступа к хранилищу; проверить переменные дашборда (могут подставлять пустое значение).
- **Настроить алерт:** Alerting → Alert rules → New; запрос(ы), условие (expression), контактные точки; при необходимости — labels для маршрутизации по политикам (notification policies). Provisioned политики при file-based provisioning не редактируются в UI.
- **Временное отключение уведомлений:** Alerting → Silences → New silence; задать matchers (по labels) и срок.
- **Provisioning:** дашборды и источники — YAML/JSON в каталогах provisioning; алертинг — через конфиг или API (ограничение редактирования в UI при file provisioning).

---

## Анти-паттерны

- Хранить пароли и токены в репозитории; использовать секреты и переменные окружения (GF_* в Docker).
- Менять provisioned дашборды только через файлы — изменения из UI в provisioned не сохраняются обратно в файлы.
- Игнорировать роль пользователя (Organization Admin нужен для управления data sources).

---

## Диагностика

Сводка: [`troubleshooting/playbook-ops-observability-network-troubleshooting-v1.md`](troubleshooting/playbook-ops-observability-network-troubleshooting-v1.md) § Grafana.

---

*Подробности: установка, конфиг, переменные, аннотации, плагины, LDAP/OAuth — в `kb-grafana-reference-v1.md`.*
