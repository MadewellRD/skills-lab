---
name: retrospective-desk
description: create connector-grounded retrospectives and continuous-improvement artifacts for software delivery. use when Gemini needs to synthesize sprint, release, incident, pull request, ci, deployment, product, or team evidence into a retrospective report, lessons-learned memo, process-improvement plan, cycle-metrics summary, action-item tracker, or downstream handoff notes for product, architecture, issue planning, implementation-handoff-desk, release, ci, incident, or documentation workflows.
---

# Retrospective Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Overview

Use this skill to turn completed work into evidence-backed retrospectives and process-improvement artifacts. The skill is for software delivery retrospectives across sprints, releases, incidents, migrations, PR trains, CI failures, deployment events, and SDLC skill-suite iterations.

Retrospective outputs must separate facts from interpretation, cite or list source evidence, preserve unresolved questions, and produce concrete improvement actions with owners, priority, and downstream handoff targets.

## Workflow

**Outcome.** An evidence-backed retrospective for the scope in question — sprint or milestone, release or deployment, incident or hotfix, PR train or implementation cycle, CI or quality gate, or skill and workflow — delivered by default as a downloadable Markdown report with a source-facts section and downstream handoff notes.

**Grounding.** Use GitHub for PRs, commits, issues, milestones, review discussion, checks, CI status, and release history. Use docs sources for PRDs, plans, release notes, runbooks, decision records, parity docs, and prior retrospectives. Use communication sources for decision-bearing team updates or halt reports when available. Use observability or incident sources when production behavior, telemetry, or customer impact is part of the retrospective.

**Evidence timeline.** Capture the sequence of events, decisions, commits, PRs, failures, releases, incidents, and handoffs. Mark uncertain timestamps and missing evidence explicitly. The timeline is ordered content — preserve its sequence in the artifact.

**Parallel surface.** Evidence collection fans out cleanly: PRs, issues, CI runs, incidents, and documents in the retrospective window are independent and carry no ordering dependency during retrieval. Gather them in parallel, then assemble the ordered timeline in one pass.

**Classification.** Use the templates in `references/retrospective-template.md`, `references/cycle-metrics-template.md`, and `references/action-plan-template.md`.

**Acceptance bar.** The retrospective is done when observation is visibly separated from interpretation; each finding names the evidence behind it; every action item has an owner, priority, due window, and the evidence that motivated it; unresolved questions and risks are preserved rather than resolved for narrative tidiness; and metrics are either sourced or marked unverified. Do not invent owners, due dates, metrics, incident impact, PR status, CI state, release state, or decision history.

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

Proceed by default. A retrospective with gaps is still useful: downgrade confidence, label the assumption inline, mark unverifiable metrics as unverified, and deliver the report. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval** — an action item would assign work or commit a named owner who has not agreed to it.
- **Production or destructive** — a proposed improvement would change live process, tooling, or configuration rather than recommend the change.
- **Security or privacy** — the timeline would need to reproduce secrets, credentials, or personal data, or the retrospective would attribute fault to a named individual on unsourced evidence.
- **Source conflict** — timelines or accounts of what happened genuinely disagree on a load-bearing event. Preserve both rather than picking the tidier story.
- **Release integrity** — the retrospective would assert that a release or incident was handled correctly when the evidence cannot establish it.
- **Connector unreachable** — a required repo or incident source exists but cannot be read. Absent evidence is a soft gap: produce a retrospective marked as user-provided-context only and continue.

Use `references/halt-conditions.md` for the halt artifact format.

## Optional helper

Use `scripts/write_retrospective_markdown.py` when a local file artifact is needed from provided text. The helper wraps retrospective content in the standard downloadable Markdown structure.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
