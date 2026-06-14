# Playbook: ops.observability-network — troubleshooting (v1)

> **Контур:** A · мир **ops.observability-network** · kb-public  
> **Когда:** Zabbix (нет данных, очередь, flapping), Grafana (пустые панели, алерты), сеть (нет интернета, VLAN, потери)  
> **Операции:** `../playbook-*` · выбор инструмента: `../../information-management/tool-purpose-and-books-v1.md`

---

## Симптом → playbook

| Симптом / слова | Playbook |
|-----------------|----------|
| Zabbix, item, trigger, agent 10050, housekeeper | `playbook-zabbix-monitoring-v1.md` |
| Grafana, datasource, panel, alert | `playbook-grafana-v1.md` |
| OSI, VLAN, DNS, ping, traceroute, NAT | `playbook-network-fundamentals-v1.md` |

---

## Zabbix

| Симптом | Действие |
|---------|----------|
| **Нет данных по item** | Availability в UI → интерфейс (Agent/SNMP/HTTP), ключ item, права на хосте; HTTP — URL, таймаут, сеть; «Test» препроцессинга |
| **Очередь** | Monitoring → Queue; при перегрузке — число item'ов, таймауты, БД, housekeeper |
| **Flapping** | Окно в выражении (avg/max/min 5–10 мин вместо `last()`); dependency от родительского триггера |
| **Агент недоступен** | Сервис на хосте, порт 10050, файрвол, версия agent/server |
| **413 / 5xx в алертах** | Сопоставить с логами приложения и nginx |

---

## Grafana

| Симптом | Действие |
|---------|----------|
| Панель пустая | Test data source; запрос и time range; `${var}` и данные для значения |
| Алерт не срабатывает | Expression, evaluation interval, contact points, matchers по labels |
| Нет настроек | Роль (Viewer/Editor/Admin/Org Admin) |

---

## Сеть (fundamentals)

| Симптом | Действие |
|---------|----------|
| Нет интернета | L1/L2, IP/шлюз (DHCP/статика), DNS (`nslookup`), файрвол, ACL |
| Медленно / потери | ping; traceroute — hop с RTT/loss; L2 — STP, дубликаты |
| Нет связи между VLAN | Маршрутизация (SVI/роутер), ACL, trunk и разрешённые VLAN |
| Сброс стека Windows | `netsh winsock reset`, `netsh int ip reset` — только по инструкции при тяжёлом сбое |

Глубина: `../kb-network-reference-v1.md`.

---

## Как дополнять

Строка в таблицу домена (Zabbix / Grafana / сеть) + при необходимости ссылка на kb-reference.

