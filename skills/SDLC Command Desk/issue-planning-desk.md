---
name: issue-planning-desk
description: create connector-grounded issue plans, github issue drafts, dependency graphs, milestone breakdowns, labels, sequencing, acceptance gates, and downstream handoff notes from prds, discovery memos, architecture specs, design docs, repo state, and stakeholder decisions. use when chatgpt needs to turn requirements or design intent into actionable implementation work, sprint scope, issue decomposition, issue bodies, dependency ordering, or implementation-handoff-desk handoff material.
---

# Issue Planning Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Role

Use this skill to convert accepted product and technical intent into implementation-ready issue plans. The skill sits after product requirements, technical discovery, and architecture design, and before `implementation-handoff-desk` implementation prompts.

Create planning artifacts only after grounding the scope in available sources. GitHub is the source of truth for existing issues, labels, milestones, repo files, branches, pull requests, and implementation state. Requirements and design docs are the source of truth for intended behavior. Communication sources are decision context, not repo truth.

## Workflow

1. Classify the planning request:
   - greenfield issue plan from PRD or design spec
   - milestone or sprint decomposition
   - GitHub issue body drafting
   - dependency graph or sequencing plan
   - backlog cleanup or re-triage
   - downstream handoff for `implementation-handoff-desk`

2. Run connector preflight using `references/connector-routing.md`.
   - Use GitHub before naming existing issues, labels, milestones, branches, PRs, files, or tests.
   - Use docs or uploaded files before deriving requirements, acceptance criteria, or non-goals.
   - Use communication sources only for recent decisions, priority, ownership, or policy context.

3. Build the issue model.
   - Extract parent objective, requirement IDs, design components, risks, dependencies, and validation needs.
   - Group work into coherent issues with clear boundaries.
   - Identify dependency order, parallelizable work, blocked work, and follow-up work.
   - Separate implementation issues from docs, tests, migration, release, security, and observability issues.

4. Produce the requested artifact.
   - For full planning, use `references/issue-plan-template.md`.
   - For GitHub issue drafts, use `references/github-issue-template.md`.
   - For dependency sequencing, use `references/dependency-graph.md`.
   - For milestone work, use `references/milestone-planning.md`.
   - For downstream implementation, use `references/pr-command-handoff.md`.

5. Preserve evidence and uncertainty.
   - Include source facts and assumptions.
   - Mark unverified facts rather than presenting them as known.
   - If required facts are unavailable, produce a connector diagnostic instead of an implementation-ready plan.

## Output rules

Default to downloadable Markdown artifacts when creating issue plans, issue batches, milestone plans, or handoff notes. Use `scripts/write_issue_plan_markdown.py` when a local file artifact is needed.

Every issue plan must include:

- source facts used
- planning assumptions
- issue list with titles, bodies, labels, and acceptance gates
- dependency order
- risk and validation notes
- downstream handoff guidance for `implementation-handoff-desk`
- explicit open questions and halt conditions

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

Halt or produce a connector diagnostic when:

- requirements are missing or contradictory
- design scope and product scope disagree
- GitHub state cannot verify existing issues, labels, milestones, or repo files that the plan depends on
- issue decomposition would require architectural decisions not present in sources
- acceptance criteria cannot be derived without inventing product behavior
- the user asks to create live GitHub issues but permissions or target repo are unavailable

## Composition with other SDLC skills

- Inputs commonly come from `product-requirements-desk`, `technical-discovery-desk`, and `architecture-design-desk`.
- Outputs commonly feed `implementation-handoff-desk`, `test-strategy-desk`, `verification-desk`, and `docs-traceability-desk`.
- When implementation prompts are requested, do not duplicate `implementation-handoff-desk`; prepare issue-backed handoff notes and continue into `implementation-handoff-desk` for the final coding-agent prompt when implementation-readiness facts are present; otherwise emit `Workflow Halt`.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/codex-conservation-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `CODEX_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
