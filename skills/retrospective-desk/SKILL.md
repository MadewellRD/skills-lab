---
name: retrospective-desk
description: create connector-grounded retrospectives and continuous-improvement artifacts for software delivery. use when chatgpt needs to synthesize sprint, release, incident, pull request, ci, deployment, product, or team evidence into a retrospective report, lessons-learned memo, process-improvement plan, cycle-metrics summary, action-item tracker, or downstream handoff notes for product, architecture, issue planning, implementation-handoff-desk, release, ci, incident, or documentation workflows.
---

# Retrospective Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Overview

Use this skill to turn completed work into evidence-backed retrospectives and process-improvement artifacts. The skill is for software delivery retrospectives across sprints, releases, incidents, migrations, PR trains, CI failures, deployment events, and SDLC skill-suite iterations.

Retrospective outputs must separate facts from interpretation, cite or list source evidence, preserve unresolved questions, and produce concrete improvement actions with owners, priority, and downstream handoff targets.

## Workflow

1. Classify the retrospective scope.
   - Sprint or milestone retrospective.
   - Release or deployment retrospective.
   - Incident or hotfix retrospective.
   - PR train or implementation-cycle retrospective.
   - CI or quality-gate retrospective.
   - Skill/workflow retrospective.

2. Run connector preflight.
   - Use GitHub for PRs, commits, issues, milestones, review discussion, checks, CI status, and release history.
   - Use docs sources for PRDs, plans, release notes, runbooks, decision records, parity docs, and prior retrospectives.
   - Use communication sources for decision-bearing team updates or halt reports when available.
   - Use observability or incident sources when production behavior, telemetry, or customer impact is part of the retrospective.

3. Build an evidence timeline.
   Capture the sequence of events, decisions, commits, PRs, failures, releases, incidents, or handoffs. Mark uncertain timestamps and missing evidence explicitly.

4. Classify outcomes.
   Use the templates in `references/retrospective-template.md`, `references/cycle-metrics-template.md`, and `references/action-plan-template.md`.

5. Produce the artifact.
   Default to a downloadable Markdown report. Include a source-facts section and downstream handoff notes.

## Required outputs

For normal retrospectives, produce:

- Executive summary.
- Scope and timeframe.
- Source facts used.
- Timeline.
- What worked.
- What failed or slowed delivery.
- Root causes and contributing factors.
- Metrics and signals.
- Action items with owner, priority, due window, and evidence.
- Follow-up issues or PR handoff notes.
- Open questions and unresolved risks.

For process-improvement requests, produce:

- Current workflow diagnosis.
- Friction points.
- Proposed changes.
- Expected effect.
- Validation signal.
- Rollout or experiment plan.
- Review date.

## Connector rules

Follow `references/connector-routing.md` and `references/source-hierarchy.md`.

Do not infer source truth from memory when a connector should be used. If required connector evidence is unavailable, produce a limited retrospective marked as user-provided-context only or produce a connector diagnostic instead.

GitHub facts override recollection for repository state. Current user instruction overrides older planning docs for priority. Docs and communication sources provide decision context but do not override live repository state.

## Downstream handoff

Use `references/handoff-rules.md` to route follow-up work:

- Implementation fixes or repo work -> `implementation-handoff-desk`.
- Requirement corrections -> `product-requirements-desk`.
- Design corrections -> `architecture-design-desk`.
- Issue breakdown -> `issue-planning-desk`.
- Test gaps -> `test-strategy-desk`.
- CI or flaky tests -> `ci-failure-desk`.
- Release/deployment changes -> `release-operations-desk` or `deployment-desk`.
- Incident follow-ups -> `incident-response-desk`.
- Documentation drift -> `docs-traceability-desk`.

## Halt behavior

Use `references/halt-conditions.md`. Halt or downgrade confidence when key facts are missing, timelines conflict, source ownership is unclear, metrics cannot be verified, or action items depend on unavailable repo or incident evidence.

Do not invent owners, due dates, metrics, incident impact, PR status, CI state, release state, or decision history.

## Optional helper

Use `scripts/write_retrospective_markdown.py` when a local file artifact is needed from provided text. The helper wraps retrospective content in the standard downloadable Markdown structure.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/codex-conservation-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `CODEX_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
