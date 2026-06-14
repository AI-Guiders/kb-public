# Домены знаний: Sysadmin / Операционная инфраструктура (v1)

> **Назначение:** темы для изучения и роутер «тип задачи → домен». В репозитории хранятся только **общие знания** по доменам; персональная инфраструктура (серверы, пути, доступы) не вносится в репозиторий и остаётся в локальном контексте пользователя.

**Где лежат файлы:** этот файл и `tool-purpose-and-books-v1.md` (часто под `knowledge/worlds/information-management/`). Playbook/kb из таблицы ниже — в **`knowledge/worlds/ops-network-admin/`**, **`knowledge/worlds/ops-observability-network/`** и смежных мирах ops.* (не в корне `knowledge/`); короткие имена в таблице — для удобства, полный путь бери из хаба [`worlds/README.md`](worlds/README.md) или через главный роутер. Пример: `knowledge/worlds/ops-observability-network/playbook-zabbix-monitoring-v1.md`, `knowledge/worlds/ops-network-admin/playbook-1c-admin-v1.md`.

---

## 1. Темы для изучения (домены)

Определены по типовой практике системного администрирования и операционной поддержки:

| Домен | Scope | Playbook | Глубокий справочник (kb) |
|-------|--------|----------|---------------------------|
| **1c-admin** | 1С: администрирование, проведение документов (реальное/регламентное), типовые проблемы | `playbook-1c-admin-v1.md` | `kb-1c-reference-v1.md` (при наличии) |
| **zabbix-monitoring** | Zabbix: мониторинг, алерты, интеграция с nginx (в т.ч. 413), шаблоны | `playbook-zabbix-monitoring-v1.md` | `kb-zabbix-reference-v1.md` |
| **grafana** | Grafana: дашборды, источники данных, алерты, типовые задачи админа | `playbook-grafana-v1.md` | `kb-grafana-reference-v1.md` |
| **ssh-operations** | SSH, SCP, ключи, bastion, безопасность доступа к серверам | `playbook-ssh-operations-v1.md` | — |
| **wireshark-network** | Wireshark: захват трафика, фильтры, типовые сценарии диагностики сети | `playbook-wireshark-network-v1.md` | — |
| **nginx-admin** | nginx: типовые настройки, PHP-FPM, proxy, 413, безопасность | `playbook-nginx-admin-v1.md` | — |
| **network-fundamentals** | Модель OSI, TCP/IP, устройства (hub, switch, router, firewall, LB), топологии, прокси, протоколы (IP, TCP, UDP, DNS, DHCP, ARP, NAT), VLAN, диагностика | `playbook-network-fundamentals-v1.md` | `kb-network-reference-v1.md` |
| **backup-db** | Бекапы и восстановление: RPO/RTO, 3-2-1, проверка восстановления | `playbook-backup-db-v1.md` | — |
| **incidents-tickets** | Инциденты и тикеты: приоритизация, постмортемы, действия по результатам | `playbook-incidents-tickets-v1.md` | — |

---

## 2. Роутер: тип задачи → домен

- «1С», «проведение», «непроведённые документы», «регламентное проведение» → **1c-admin**
- «Zabbix», «мониторинг», «алерт», «шаблон», «413 nginx» → **zabbix-monitoring**
- «Grafana», «дашборд», «источник данных», «графики» → **grafana**
- «SSH», «SCP», «ключи», «bastion», «доступ к серверу» → **ssh-operations**
- «Wireshark», «трафик», «pcap», «фильтр захвата» → **wireshark-network**
- «nginx», «PHP-FPM», «client_max_body_size», «proxy» → **nginx-admin**
- «OSI», «топология», «прокси», «коммутатор», «маршрутизатор», «VLAN», «подсеть», «NAT», «DNS», «сетевые устройства», «forward/reverse proxy» → **network-fundamentals**
- «Бекап», «восстановление», «RPO», «RTO» → **backup-db**
- «Инцидент», «тикет», «постмортем», «приоритет» → **incidents-tickets**

При пересечении доменов — подгружать несколько playbook'ов. Конкретные хосты, пути и доступы брать только из локального контекста пользователя, не из репозитория.

---

## 3. Назначение технологий и выбор инструмента

При вопросах «для чего Zabbix / Grafana», «что выбрать для мониторинга», «сравнить инструменты» — опираться на **`tool-purpose-and-books-v1.md`**: там заданы назначение каждой технологии (Zabbix — мониторинг и алертинг, Grafana — визуализация и дашборды), роутинг «задача → инструмент» и список книг для углубления БЗ. После добавления аналогов (Prometheus, Nagios, ELK и т.д.) выбор инструмента делать по таблице задач в этом файле и по соответствующим доменам.

---

## 4. Правило для агента

1. По ключевым словам запроса выбрать домен(ы) из п.2; при выборе/сравнении инструментов — п.3 и `tool-purpose-and-books-v1.md`.
2. Открыть **`troubleshooting/playbook-*-troubleshooting-v1.md`** соответствующего мира ops (сводка симптомов) или `playbook-<домен>-v1.md`; при необходимости — `kb-<тема>-reference-v1.md`. См. [`META/index-troubleshooting-v1.md`](META/index-troubleshooting-v1.md).
3. Конкретные имена серверов, IP, пути, пароли — не хранить в БЗ в репозитории; при необходимости запрашивать у пользователя или использовать только локальные файлы (например USER_AND_PROJECTS_CONTEXT), не коммитить их в форк.

---

*Версия: v1. Домены определены как темы для изучения; наполнение — общими практиками и глоссарием без привязки к инфраструктуре пользователя. Добавлен ориентир по назначению технологий и роутингу по задачам (tool-purpose-and-books-v1.md).*

