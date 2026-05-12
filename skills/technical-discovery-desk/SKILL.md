---
name: technical-discovery-desk
description: create connector-grounded technical discovery memos, repo reconnaissance reports, feasibility assessments, spike plans, risk registers, unknowns lists, and downstream handoff notes before architecture or implementation work. use when the user asks to investigate technical feasibility, inspect a repo before planning, research dependencies or integrations, compare implementation options, identify unknowns, map risks, plan a spike, or prepare technical input for architecture-design-desk, issue-planning-desk, or implementation-handoff-desk.
---

# Technical Discovery Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Role

Use this skill to turn early product or engineering intent into a grounded technical discovery package. The skill is pre-architecture and pre-implementation: it investigates what exists, what is feasible, what is risky, what remains unknown, and what must be decided before design or PR work begins.

Do not write implementation prompts with this skill. When the user is ready for branch/PR execution, continue into the implementation handoff stage with a clear discovery summary and source facts when implementation-readiness facts are present.

## Workflow

1. Classify the discovery request.
   - Repo reconnaissance: inspect code structure, build system, tests, dependencies, ownership, and recent change history.
   - Feasibility assessment: evaluate whether a product requirement can be implemented under current constraints.
   - Integration discovery: inspect external APIs, SDKs, service boundaries, auth, rate limits, and failure modes.
   - Spike planning: define a bounded investigation with questions, commands, expected artifacts, and stop conditions.
   - Risk and unknowns analysis: separate proven facts from assumptions, blockers, and decisions needed.

2. Run connector preflight.
   - Use GitHub for repo facts, files, commits, PRs, issues, CI checks, dependency manifests, tests, and build scripts.
   - Use docs connectors or uploaded docs for PRDs, roadmaps, architecture docs, design notes, audit packs, and decisions.
   - Use issue/project connectors for ticket scope, acceptance criteria, priority, labels, owners, and blockers.
   - Use communication connectors only for recent decision context or agent halt reports.
   - Use public web only for external APIs, SDKs, standards, vendor docs, or current tool behavior not present in repo/docs.

3. Apply the source hierarchy.
   Prefer current user instruction, then live GitHub state, then live issue/project state, then canonical docs, then decision-bearing communications, then public web for external facts, then explicit assumptions. If sources conflict, preserve the conflict and either ask for resolution or produce a diagnostic rather than smoothing it over.

4. Produce the right artifact.
   - Technical discovery memo: default for broad investigation.
   - Repo reconnaissance report: default for unfamiliar codebases.
   - Feasibility assessment: default for “can we build this?” questions.
   - Spike plan: default when implementation is premature.
   - Connector diagnostic: default when required sources are missing.

5. Make downstream handoff explicit.
   End with one of these decisions:
   - Ready for `architecture-design-desk`.
   - Ready for `issue-planning-desk`.
   - Ready for `implementation-handoff-desk`.
   - Needs product clarification.
   - Needs spike.
   - Blocked by missing connector facts.

## Output rules

When producing a discovery artifact, create a downloadable Markdown file when tools allow it. Use the wrapper in `references/output-contract.md`. Include source facts, unverified assumptions, risks, open questions, and explicit next-step routing.

Do not cite or claim code facts that were not retrieved from connectors or supplied by the user. Do not invent file paths, dependency versions, test names, architecture decisions, CI status, owners, or issue IDs.

## Reference loading

Load these references when relevant:

- `references/discovery-template.md` for the default technical discovery memo structure.
- `references/repo-recon-template.md` for codebase inspection and repo topology work.
- `references/connector-routing.md` for required source selection.
- `references/source-hierarchy.md` for truth precedence and conflict handling.
- `references/risk-register.md` for risk scoring and unknowns classification.
- `references/output-contract.md` for downloadable Markdown artifact rules.
- `references/handoff-rules.md` for routing to later SDLC skills.
- `references/halt-conditions.md` when connector facts are missing or scope is unsafe.

## Halt conditions

Halt or produce a connector diagnostic when:

- The request depends on live repo facts and GitHub is unavailable or the repo is not selected.
- The request depends on product/spec truth and no PRD, roadmap, issue, or user-provided source is available.
- The repo state conflicts with pasted facts and the user has not resolved the conflict.
- The user asks for implementation before discovery questions, risks, and constraints are sufficiently bounded.
- External API or SDK behavior is current-sensitive and cannot be verified.
- The request would require security, legal, privacy, or production-risk assumptions that are not supported by sources.

## Composition with other SDLC skills

- Use `product-requirements-desk` outputs as upstream product truth when available.
- Hand architectural decisions and viable options to `architecture-design-desk`.
- Hand decomposed work themes and constraints to `issue-planning-desk`.
- Hand bounded implementation-ready facts to `implementation-handoff-desk` only after discovery is complete.
