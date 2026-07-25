---
name: issue-planning-desk
description: create connector-grounded issue plans, github issue drafts, dependency graphs, milestone breakdowns, labels, sequencing, acceptance gates, and downstream handoff notes from prds, discovery memos, architecture specs, design docs, repo state, and stakeholder decisions. use when {{AGENT}} needs to turn requirements or design intent into actionable implementation work, sprint scope, issue decomposition, issue bodies, dependency ordering, or implementation-handoff-desk handoff material.
---

# Issue Planning Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Role

Use this skill to convert accepted product and technical intent into implementation-ready issue plans. The skill sits after product requirements, technical discovery, and architecture design, and before `implementation-handoff-desk` implementation prompts.

Create planning artifacts only after grounding the scope in available sources. GitHub is the source of truth for existing issues, labels, milestones, repo files, branches, pull requests, and implementation state. Requirements and design docs are the source of truth for intended behavior. Communication sources are decision context, not repo truth.

## Workflow

**Outcome.** The planning artifact the request calls for: a greenfield issue plan from a PRD or design spec, a milestone or sprint decomposition, GitHub issue body drafts, a dependency graph or sequencing plan, a backlog cleanup or re-triage, or a downstream handoff for `implementation-handoff-desk`.

**Grounding.** Run connector preflight using `references/connector-routing.md`. Use GitHub before naming existing issues, labels, milestones, branches, PRs, files, or tests. Use docs or uploaded files before deriving requirements, acceptance criteria, or non-goals. Use communication sources only for recent decisions, priority, ownership, or policy context.

**Issue model.** Extract the parent objective, requirement IDs, design components, risks, dependencies, and validation needs. Group work into coherent issues with clear boundaries. Identify dependency order, parallelizable work, blocked work, and follow-up work. Separate implementation issues from docs, tests, migration, release, security, and observability issues.

**Templates.** Full planning uses `references/issue-plan-template.md`. GitHub issue drafts use `references/github-issue-template.md`. Dependency sequencing uses `references/dependency-graph.md`. Milestone work uses `references/milestone-planning.md`. Downstream implementation uses `references/handoff-rules.md`.

**Parallel surface.** Once the decomposition is set, drafting the individual issue bodies is independent work, each issue's title, scope, acceptance criteria, and labels stand alone. Draft them in parallel rather than one at a time. Dependency ordering across issues is the one part that must be resolved in a single pass, and the resulting sequence is content: preserve it as ordered output.

**Evidence and uncertainty.** Include source facts and assumptions. Mark unverified facts rather than presenting them as known.

**Acceptance bar.** The plan is done when each issue is independently actionable, a single owner could pick it up, implement it, test it, and close it without asking what was meant, and carries the elements in `Issue quality rules` below. Dependency order must be explicit, and parallelizable issues must be marked as such so downstream work can fan out. Do not invent requirement IDs, issue numbers, labels, milestones, owners, file paths, or acceptance criteria.

## Output rules

A planning run delivers the whole plan, not one layer of it: the issue plan, a drafted body for every issue in it, the dependency order across them, and the downstream handoff for `implementation-handoff-desk`. Milestone or sprint assignment joins that set when the request has a milestone to assign against. A backlog cleanup or re-triage is a different scope; it operates on issues that already exist; and is produced instead of a greenfield plan rather than alongside one.

Default to downloadable Markdown artifacts when creating issue plans, issue batches, milestone plans, or handoff notes. Use `scripts/write_issue_plan_markdown.py` when a local file artifact is needed.

Every issue plan must include:

- source facts used
- planning assumptions
- issue list with titles, bodies, labels, and acceptance gates
- dependency order
- risk and validation notes
- downstream handoff guidance for `implementation-handoff-desk`
- explicit open questions and halt conditions

An issue body is finished when the assignee needs nothing else: the problem, the scope boundary, the files or areas involved where sources establish them, the acceptance criteria, and the validation. Ten issues with one-line bodies is not a decomposition of the work, it is a restatement of it. Drafting bodies is independent work across issues, which is the parallel surface the workflow describes; dependency ordering is the single pass.

Delivering a full plan does not license inventing what it plans against. Requirement IDs, issue numbers, labels, milestones, owners, and file paths come from sources or are marked as proposed. An acceptance criterion nobody stated is a proposal labeled as one, and an issue whose scope has no requirement behind it is raised as an open question rather than written as agreed work.

## Issue quality rules

Each generated issue must be independently actionable. Include:

- title in conventional imperative form
- problem or requirement source
- implementation scope
- acceptance criteria
- validation commands or evidence requirements when known
- dependencies and blockers
- out-of-scope boundaries
- labels or milestone suggestions when grounded

Do not create vague issues such as "improve backend" or "fix UI". Split broad work until each issue can be owned, tested, reviewed, and closed.

## Halt behavior

Proceed by default. A thin requirement is decomposed with the gap named in the issue body and the assumption labeled; that is cheaper to correct than a stalled plan. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval**: the user asks to create, edit, or close live GitHub issues and permission or the target repo is unavailable, or the change needs a human to authorize scope.
- **Production or destructive**: the request would write to or re-triage a live tracker rather than produce draft issue bodies.
- **Security or privacy**: issue bodies would need to embed secrets, credentials, or personal data to be actionable.
- **Source conflict**: requirements are contradictory, or design scope and product scope genuinely disagree. Preserve the conflict rather than picking a reading.
- **Release integrity**: acceptance gates would be presented as agreed when no source establishes them, or acceptance criteria cannot be derived without inventing product behavior.
- **Connector unreachable**: GitHub exists but cannot be read for issues, labels, milestones, or repo files the plan depends on. Absent context is a soft gap: draft against user-provided facts, mark the plan source-limited, and continue.

When decomposition would require architectural decisions not present in sources, route to `architecture-design-desk` rather than halting.

## Composition with other SDLC skills

- Inputs commonly come from `product-requirements-desk`, `technical-discovery-desk`, and `architecture-design-desk`.
- Outputs commonly feed `implementation-handoff-desk`, `test-strategy-desk`, `verification-desk`, and `docs-traceability-desk`.
- When implementation prompts are requested, do not duplicate `implementation-handoff-desk`; prepare issue-backed handoff notes and continue into `implementation-handoff-desk` for the final coding-agent prompt when implementation-readiness facts are present; otherwise emit `Workflow Halt`.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `{{BLOCKER_TAG}}` when implementation handoff facts are insufficient for a coding agent.
