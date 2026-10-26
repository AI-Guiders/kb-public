---
type: Definition Card
title: HttpClient reuse
description: Не new HttpClient на каждый запрос; factory / long-lived instance.
tags: [llm-native-card, definition, software-authoring]
language: en
world: software
subworld: authoring
---

# HttpClient reuse

- id: httpclient-reuse
- kind: definition
- informal: Не new HttpClient на каждый запрос; factory / long-lived instance.
- formal.rule: use_IHttpClientFactory_or_documented_singleton
- llm_cue: Socket exhaustion risk from per-request HttpClient?
- related: csharp-dispose-using, csharp-di-no-scoped-from-singleton, gof-singleton
- sources: worlds/software-authoring/code-writing-principles.md

