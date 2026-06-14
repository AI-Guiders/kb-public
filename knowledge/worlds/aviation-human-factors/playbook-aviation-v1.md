# Aviation Playbook v1

## Purpose

Root world map for aviation knowledge.

This file defines aviation as a standalone world and routes to subdomains.

## World Scope

- Flight operations and procedures
- Navigation and instrumentation
- Human factors and crew interaction
- Safety management and occurrence reporting
- Accident/incident analysis methods
- Weather, terrain, and operational constraints
- Regulatory and organizational controls

## Subdomain Router

- Human factors (current active coverage):
  - `playbook-aviation-human-factors-v1.md`
  - `map-aviation-human-factors-reading-v1.md`
  - `kb-aviation-human-factors-rules-v1.md`
  - `status-aviation-human-factors-v1.md`

- Planned next subdomains:
  - flight-operations core
  - navigation and altimetry standards
  - weather and minima decisioning
  - safety investigations and methodology
  - maintenance/airworthiness human-organization interface

## World Contract

- Do not reduce aviation to one subdomain (for example, only psychology).
- Keep subdomains separable but interoperable through explicit router links.
- Keep regulation-sensitive claims tied to first-party sources (ICAO/EASA/FAA where applicable).

## World DoD v1

World is stable when:
- root world map exists and routes to active subdomains;
- each active subdomain has playbook + map + knowledge set + status;
- canonical index points first to the world root, then to subdomains.

