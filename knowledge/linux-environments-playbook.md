# Linux Environments Playbook v1

## Purpose
Project-independent playbook for reliable engineering and troubleshooting on Linux hosts.

## Scope
- Linux process/service runtime behavior
- Permissions and ownership model
- Resource limits and isolation boundaries
- Operational diagnostics baseline

## Evidence-Based Working Format
- Fact: capture concrete host symptom (service crash loop, permission issue, limit exhaustion).
- Hypothesis: define smallest plausible Linux-level cause.
- Check: run minimal reproducible verification command set.
- Decision criterion: predefine close/escalate threshold.
- Confidence mark: explicit certainty and residual risk.

## Core Linux Contracts
- Service model and lifecycle semantics must be explicit.
- Ownership/mode/capability assumptions must be validated.
- Resource limits and cgroup boundaries must be visible.
- Locale/timezone/encoding assumptions must be explicit.

## Runtime and Service Contracts
- systemd unit contracts (dependencies, restart, environment) must be deterministic.
- Startup arguments and runtime env must be explicit.
- Signal handling and graceful shutdown behavior must be validated.
- Worker/daemon ownership of subprocesses must be clear.

## Permissions and Filesystem Contracts
- Validate uid/gid ownership and mode bits on critical paths.
- Keep mount and symlink boundaries explicit.
- Avoid implicit root assumptions.
- Confirm write boundaries before mutating operations.

## Resource and Isolation Contracts
- Check `ulimit` and file descriptor ceilings for IO-heavy services.
- Validate memory/cpu/pid constraints in cgroups/containers.
- Distinguish host saturation from app-level faults.
- Keep capacity symptoms separated from logic bugs.

## Diagnostics Baseline
- journal logs + structured application logs.
- Process tree, open-file/socket state, and limit visibility.
- Resource pressure timeline (cpu/memory/io) before deep app debugging.
- One concise root-cause and prevention delta per incident.

## Metrics
- Mean time to identify Linux host root cause.
- Frequency of limit/ownership-related incidents.
- Recovery time for service restarts.
- Reopen rate for Linux environment incidents.

## Revisit Triggers
- Repeated “works only on one distro/host profile” failures.
- Frequent permission/ownership regressions.
- Recurring incidents from invisible resource constraints.
