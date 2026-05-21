# Docker Playbook v1

## Purpose
Dedicated playbook for containerized development, testing, and operational reproducibility.

## Scope
- Image and build discipline
- Runtime contracts and environment parity
- Volume/network/process safety
- Security and supply-chain hygiene

## Evidence-Based Working Format
- Fact: define the reproducibility or environment mismatch issue.
- Hypothesis: specify which container change resolves it.
- Check: verify with smallest reproducible container scenario.
- Decision criterion: success/failure thresholds before rollout.
- Confidence mark: explicit certainty level.

## Build Contracts
- Pin base image families and document update cadence.
- Keep images minimal and purpose-specific.
- Separate build and runtime stages where possible.
- Cache dependencies consciously; avoid stale artifact masking.

## Runtime Contracts
- Make ports, volumes, and env vars explicit.
- Keep working directory mapping deterministic.
- Prefer immutable container behavior for CI.
- Ensure graceful startup/shutdown signals for app processes.

## Project-Aware Contracts
- Bind only required host paths into containers.
- Avoid hidden host dependencies.
- Align container entrypoints with repository task contracts.
- Document command parity between local and CI usage.

## Security Contracts
- Avoid running as root unless required and justified.
- Scan image dependencies on update cycles.
- Keep secrets out of images and compose files.
- Restrict capabilities and networking surface area when possible.

## Metrics
- Local vs CI parity failure rate.
- Time to reproduce environment-specific defects.
- Container startup time for core workflows.
- Frequency of image-related regressions.

## Revisit Triggers
- Repeated “works locally but not in CI” incidents.
- Frequent image bloat or slow build regressions.
- Security findings with recurring root causes.
