---
name: deployment-desk
description: create connector-grounded deployment, rollout, feature-flag, change-management, go/no-go, post-deploy verification, and deployment handoff artifacts for software delivery. use when chatgpt needs to plan a deploy, assess rollout readiness, define staged rollout gates, map deployment risks, coordinate release-to-deploy handoff, prepare rollback or monitoring checkpoints, or produce downstream notes for release-operations-desk, observability-readiness-desk, incident-response-desk, ci-failure-desk, verification-desk, or implementation-handoff-desk workflows.
---

# Deployment Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


Use this skill to create deployment-stage artifacts after implementation and release readiness are known, or when a deployment plan must be derived from repo state, release notes, infrastructure configuration, feature flags, verification evidence, and operational constraints.

## Operating model

Deployment planning must be grounded before it is prescriptive. Determine which sources are needed, retrieve them when connectors are available, and separate verified facts from assumptions.

Default source roles:

- GitHub: deployment config, workflow files, release branches, commits, tags, pull requests, checks, deploy scripts, infrastructure-as-code, and prior deployment changes.
- Issue or project trackers: deployment scope, blockers, rollout tasks, owners, and go/no-go criteria.
- Document sources: release runbooks, architecture docs, operational policies, environment maps, feature-flag policy, change-management notes, and customer communication plans.
- Communication sources: current deployment decisions, approval status, stakeholder constraints, incident cautions, and launch timing.
- Observability sources: dashboards, alert rules, SLOs, health checks, recent incidents, and post-deploy monitoring expectations.

If required source facts are unavailable, produce a deployment diagnostic or clearly mark the output as user-fact-grounded only. Do not invent environment names, deploy commands, owners, approvals, feature flags, rollback procedures, health checks, or CI/deployment status.

## Workflow

1. Classify the request.
   - Deployment plan: use `references/deployment-plan-template.md`.
   - Staged rollout or feature flags: use `references/rollout-plan-template.md`.
   - Change-management artifact: use `references/change-management-template.md`.
   - Go/no-go review: use `references/go-no-go-template.md`.
   - Post-deploy verification: use `references/post-deploy-checks.md`.

2. Run connector preflight.
   Use `references/connector-routing.md` to identify required and optional sources. Check for release scope, target environment, deployment mechanism, validation evidence, rollback method, observability coverage, known incidents, and approval requirements.

3. Build the artifact.
   Use the smallest artifact that satisfies the request. Prefer concrete gates, commands, owners, timing, and evidence. Mark unknowns explicitly.

4. Add downstream handoff.
   When deployment depends on a PR, release, CI fix, verification gate, monitoring update, or incident response action, include a handoff note to the appropriate desk skill.

5. Halt when deployment safety is not knowable.
   Use `references/halt-conditions.md` for missing approvals, red checks, unknown rollback path, unclear environment, unresolved blockers, or conflicting source truth.

## Output rules

When creating a deployment artifact, return a downloadable markdown file when the environment supports file output. Use the wrapper and artifact contracts in `references/output-contract.md`. Include source facts and unverified assumptions unless the user explicitly asks for a terse inline answer.

For agent handoffs, write the content so it can be pasted into an execution agent without losing guardrails. Keep halt conditions intact.

## Composition with other desks

- Use `release-operations-desk` before this skill when release scope, versioning, changelog, rollback ownership, or release readiness is not established.
- Use `verification-desk` before this skill when acceptance, test, or evidence gates are unclear.
- Use `ci-failure-desk` before this skill when deployment is blocked by failing checks or unstable pipelines.
- Use `observability-readiness-desk` before or with this skill when monitoring, alerts, SLOs, or post-deploy checks are incomplete.
- Use `incident-response-desk` after this skill when deployment causes or relates to a production incident.
- Use `implementation-handoff-desk` when a deployment plan requires a repository change, rollback PR, config patch, or implementation-agent prompt.

## References

- `references/deployment-plan-template.md`: deployment plan structure.
- `references/rollout-plan-template.md`: staged rollout, feature flag, and blast-radius control structure.
- `references/change-management-template.md`: change-management and stakeholder coordination structure.
- `references/go-no-go-template.md`: go/no-go review format.
- `references/post-deploy-checks.md`: post-deployment validation and monitoring checklist.
- `references/connector-routing.md`: source routing and required facts.
- `references/source-hierarchy.md`: source precedence and conflict rules.
- `references/output-contract.md`: markdown artifact requirements.
- `references/handoff-rules.md`: downstream handoff routing.
- `references/halt-conditions.md`: mandatory stop conditions.
- `scripts/write_deployment_markdown.py`: optional helper for wrapping deployment artifacts in markdown files.
- `references/suite-workflow-contract.md`: shared workflow packet, continuation, and halt contract for SDLC Command Desk suite orchestration.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/codex-conservation-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `CODEX_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
