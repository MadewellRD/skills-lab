---
name: deployment-desk
description: create connector-grounded deployment, rollout, feature-flag, change-management, go/no-go, post-deploy verification, and deployment handoff artifacts for software delivery. use when Gemini needs to plan a deploy, assess rollout readiness, define staged rollout gates, map deployment risks, coordinate release-to-deploy handoff, prepare rollback or monitoring checkpoints, or produce downstream notes for release-operations-desk, observability-readiness-desk, incident-response-desk, ci-failure-desk, verification-desk, or implementation-handoff-desk workflows.
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

**Outcome.** The smallest deployment artifact that satisfies the request, with concrete gates, commands, owners, timing, and evidence, and unknowns marked explicitly.

**Artifact selection.** Deployment plans use `references/deployment-plan-template.md`. Staged rollout or feature-flag work uses `references/rollout-plan-template.md`. Change-management artifacts use `references/change-management-template.md`. Go/no-go reviews use `references/go-no-go-template.md`. Post-deploy verification uses `references/post-deploy-checks.md`.

**Grounding.** Run connector preflight per `references/connector-routing.md` to identify required and optional sources. Establish release scope, target environment, deployment mechanism, validation evidence, rollback method, observability coverage, known incidents, and approval requirements.

**Ordered content is not scaffolding.** The gate sequences this desk produces, pre-deploy checks, approval, cutover, post-deploy verification, rollback, are externally mandated order. Emit them as ordered, numbered steps in the artifact and never reorder, merge, or collapse them for brevity.

**Parallel surface.** Reading the evidence is parallel-safe even though executing the deploy is not. Retrieve deployment config, CI check state, release notes, feature-flag state, observability coverage, and approval status concurrently; assess independent services, regions, or environments in parallel when the rollout treats them as independent. The rollout gate sequence itself remains strictly ordered.

**Downstream handoff.** When deployment depends on a PR, release, CI fix, verification gate, monitoring update, or incident response action, include a handoff note to the appropriate desk skill.

**Acceptance bar.** The artifact is done when the target environment and deployment mechanism are named from sources; every gate has an owner and a pass condition that can be evaluated without further interpretation; a rollback path is stated and marked as verified or unverified; post-deploy checks name the specific signals to watch and the threshold that triggers rollback; and approval status is recorded rather than assumed. Do not invent environment names, deploy commands, owners, approvals, feature flags, rollback procedures, health checks, or CI/deployment status.

## Output rules

A deployment run delivers the whole plan, not the piece the request named: the deployment plan with its gate sequence, the go/no-go review with every gate classified, the rollback path, and the post-deploy verification checklist. A staged rollout or feature-flag plan joins that set whenever the deploy is staged or flag-gated, and is legitimately absent for a single-shot deploy. A change-management record is the genuinely conditional one; produced when the organization's process requires it, skipped when no source establishes such a process.

The bar is execution under pressure by someone who did not plan it. Every gate names its owner and a pass condition that needs no interpretation. Every command is exact. Post-deploy checks name the signal, the threshold, the observation window, and the action when the threshold trips. Rollback states the path and whether it has been verified. A checklist whose steps read "verify deployment succeeded" has not reached that bar.

Evidence retrieval across environments, services, and regions is parallel-safe as the workflow describes, so the artifacts in the set are built concurrently. The gate sequence inside them stays ordered.

Completeness of the set is bounded by the evidence under it. Environment names, deploy commands, owners, approvals, flags, rollback procedures, health checks, and CI status are sourced or explicitly missing. A gate whose status could not be established is `unknown` and blocking, never `pass`, and a rollback path nobody has confirmed is marked unverified rather than written as though it were.

When creating a deployment artifact, return a downloadable markdown file when the environment supports file output. Use the wrapper and artifact contracts in `references/output-contract.md`. Include source facts and unverified assumptions unless the user explicitly asks for a terse inline answer.

For agent handoffs, write the content so it can be pasted into an execution agent without losing guardrails. Keep halt conditions intact.

## Halt policy

Proceed by default when producing planning artifacts: an unknown that can be marked and worked around is a labeled assumption, not a stop. Deployment carries more hard-halt surface than most desks, so reserve halts for these consequence classes from `references/halt-taxonomy.md` and do not soften them:

- **Approval**: a required approval is missing, unrecorded, or the approver is unidentified.
- **Production or destructive**: the request asks to execute a deploy, cutover, flag flip, or data migration rather than plan one, or the rollback path is unknown or unprovable.
- **Security or privacy**: the deploy would move secrets, credentials, or personal data across a trust boundary that sources do not establish as intended.
- **Source conflict**: repo state, release docs, and deployment configuration genuinely disagree on what ships or where it ships to.
- **Release integrity**: a go decision would be issued while required checks are red, stale, or unverifiable.
- **Connector unreachable**: a required deployment, CI, or approval source exists but cannot be read. A source that is merely absent is a soft gap: mark the artifact source-limited and continue.

Use `references/halt-conditions.md` for the halt artifact format.

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

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
