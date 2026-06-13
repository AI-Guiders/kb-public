# `knowledge/worlds/` — крупные контексты («вселенные»)

Смысл корзины и правила размещения — только из **`../META/kb-taxonomy-v1.md`**.

**Публикация (все миры):** любой текст под `worlds/<slug>/` уходит в kb-public. Перед коммитом в **любом** мире — чеклист [`knowledge-engineering/playbook-kb-world-public-authoring-v1.md`](knowledge-engineering/playbook-kb-world-public-authoring-v1.md) (без scope, `work/`, внутренних брендов, машинных путей). Не только для knowledge.engineering.

**Troubleshooting:** слой A — **`troubleshooting/`** в мире (kb-public); слой B (продукт) — **только** [`../work/troubleshooting/README.md`](../work/troubleshooting/README.md). Сводка A — [`../META/index-troubleshooting-v1.md`](../META/index-troubleshooting-v1.md).

**Уже есть:** `cognition-human-perception/` — мир **cognition.human-perception** (UX / психофизиология в смысле KE).  
**Уже есть:** `cognition-language-acquisition/` — мир **cognition.language-acquisition** (human child L1: CDS, feedback, lexical learning; transfer deny → CASA) — см. hub.  
**Уже есть:** `cognition-neurolinguistics/` — мир **cognition.neurolinguistics** (brain language/reading, bilingual control; bridge → pedagogy, **deny** fMRI gates) — см. hub.  
**Уже есть:** `arts-music/` — мир **arts.music** (теория, акустика, строи, незападные системы).  
**Уже есть:** `logistics-warehouse/` — мир **logistics.warehouse** (этикетки маркетплейсов, видеозахват штрихкодов, камеры/NVR).  
**Уже есть:** `media-videography/` — **media.videography** / **media.video-surveillance** (теория съёмки, broadcast, CCTV) — см. hub.  
**Уже есть:** `software-ml-applied/` — мир **software.ml-applied** (ML, OCR, штрихкоды/QR) — см. hub.  
**Уже есть:** `pattern-regex/` — кластер **pattern.regex** / MRE3 (playbook + индекс + `kb-regex-*`) — см. hub.  
**Уже есть:** `software-javascript/` — мир **software.javascript** (ECMAScript, operational) — см. hub.  
**Уже есть:** `software-php-laravel/` — **software.php** / **software.laravel** и смежные платформы (индексы, playbooks, kb) — см. hub.  
**Уже есть:** `software-dotnet-csharp/`, `software-dotnet-tooling-roslyn/`, `software-dotnet-avalonia/` — **software.authoring.dotnet.*** (C#, Roslyn, Avalonia); hub-редирект — `software-dotnet-desktop/README.md`.  
**Уже есть:** `math-numerics-pde/` — **math.numerics-pde** (PDE/ODE/численные схемы; валидация решателей и equation→CA→CUDA) — см. hub.  
**Уже есть:** `aviation-human-factors/` — **aviation.human-factors** (карта мира авиации, CRM/TEM/ADM, чтение, правила, PFD/MFD/EFIS/EICAS, матрица переноса в бытовое взаимодействие) — см. hub.  
**Уже есть:** `psychology-models/` — **psychology.models** (status/playbook, карта чтения, kb по школам/эмпирике/культуре/манипуляции, L1 Gender Studies) — см. hub.  
**Уже есть:** `medicine-evidence/` — **medicine.evidence** (BCI/evidence-based навигация, playbook медицины, границы терапии vs поддержки агента) — см. hub.  
**Уже есть:** `hci-ux-dx/` — **hci.ux-dx** (HCI, UI/UX литература и продуктовый playbook, DE/DX и литература IDE; git/pr/tooling — в корне `knowledge/`) — см. hub.  
**Уже есть:** `software-engineering-evidence/` — **software.engineering-evidence** (KB эвиденции по темам, карта чтения .NET/C#, карта глав *Code Complete*, статус, legacy digest) — см. hub.  
**Уже есть:** `software-automation-scripting/` — **software.automation-scripting** (роутер автоматизации, PowerShell, Bash, CMD, Python, Docker) — см. hub.  
**Уже есть:** `collaboration-git-pr/` — **collaboration.git-pr** (Git, PR review, kb, runbook backup) — см. hub.  
**Уже есть:** `systems-it/` — **systems.it** (IT core, cloud/platform diagnostics) — см. hub.  
**Уже есть:** `knowledge-engineering/` — **knowledge.engineering** (KE playbooks, kb, матрицы, world modeling, runbooks) — см. hub.  
**Уже есть:** `ops-host-environments/` — **ops.host-environments** (Linux/Windows playbooks) — см. hub.  
**Уже есть:** `ops-network-admin/` — **ops.network-admin** (SSH, Nginx, Wireshark, 1C) — см. hub.  
**Уже есть:** `ops-reliability/` — **ops.reliability** (backup DB, incidents/tickets) — см. hub.  
**Уже есть:** `ops-observability-network/` — **ops.observability-network** (Grafana, Zabbix, network kb) — см. hub.  
**Уже есть:** `agent-orchestration/` — **agent.orchestration** (автономия, captain, session export, learn, clarification) — см. hub.  
**Уже есть:** `workspace-context/` — **workspace.context** (multi-project, rehydrate, scope, finalizer) — см. hub.  
**Уже есть:** `information-management/` — **information.management** (IM playbook, identity, open questions) — см. hub.  
**Уже есть:** `evidence-humanities-shelf/` — **evidence.humanities-shelf** (гуманитарные и смежные evidence-kb) — см. hub.  
**Уже есть:** `software-integration-kb/` — **software.integration-kb** (WebApiToolkit, Telegram kb) — см. hub.  
**Уже есть:** `culture-dialogue-insights/` — **culture.dialogue-insights** (инсайты из диалога) — см. hub.  
**Уже есть:** `software-authoring/` — **software.authoring** (code principles, language index) — см. hub.

<!-- section:catalog-engineering-cad-v1 -->
**Уже есть:** `engineering-cad/` — **engineering.cad** (Fundamentals → Playbook; hub `engineering-cad/README.md`). Только vendor-neutral предметка; пути clone/диск в kb не описываются.
<!-- /section:catalog-engineering-cad-v1 -->

<!-- section:catalog-pedagogy-school-subjects-v1 -->
**Уже есть:** `pedagogy-general/` — **pedagogy.general** (instruction science, F→O, master router, transfer matrix, DoD hub). Subject worlds: `pedagogy-russian-language`, `pedagogy-mathematics`, `pedagogy-physics`, `pedagogy-chemistry`, `pedagogy-biology`, `pedagogy-literature`, `pedagogy-history`, `pedagogy-geography`, `pedagogy-social-studies`, `pedagogy-second-native-language`, `pedagogy-informatics`, `pedagogy-visual-arts` — per-paper evidence + scientific-evidence index; hub `pedagogy-general/README.md`. **Не** human L1 acquisition — `cognition-language-acquisition` (bridge → `pedagogy-second-native-language`). Музыка — `arts-music`.
<!-- /section:catalog-pedagogy-school-subjects-v1 -->
