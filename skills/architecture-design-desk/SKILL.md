---
name: architecture-design-desk
description: create connector-grounded architecture and solution design artifacts from product requirements, technical discovery, repository structure, constraints, and stakeholder decisions. use when chatgpt needs to produce software design specs, architecture decision records, component boundaries, interface contracts, migration plans, risk notes, source-fact evidence, or downstream implementation handoff notes for issue planning, verification, security, or implementation-handoff-desk workflows.
---

# Architecture Design Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Purpose

Use this skill to turn requirements and technical discovery into architecture artifacts that can be implemented, reviewed, verified, and traced. The skill must distinguish source-backed facts from design judgment and must not invent repository structure, APIs, ownership, dependencies, constraints, or production behavior.

## Required operating model

Before drafting any design artifact, perform connector preflight.

1. Identify the design mode: new architecture, incremental design, migration design, interface contract, ADR set, or implementation handoff.
2. Gather source facts from the highest-trust available connectors.
3. Separate facts, inferences, decisions, assumptions, and open questions.
4. Produce the requested artifact as Markdown, using the appropriate reference template.
5. Include source facts, unresolved risks, and downstream handoff notes.
6. Halt or produce a connector diagnostic when required facts are missing.

## Connector expectations

GitHub is required for repo-aware design. Use it to verify modules, files, APIs, tests, dependency manifests, prior PRs, and existing architecture patterns. Document connectors are required when the design depends on PRDs, SRS docs, discovery memos, roadmap docs, or architecture records. Issue/project connectors are required when design scope comes from tickets, milestones, labels, or acceptance criteria. Communication connectors are optional but useful for recent stakeholder decisions; treat them as decision context, not code truth.

Apply `references/source-hierarchy.md` when sources conflict. If current user instruction conflicts with existing docs or repo state, preserve the conflict explicitly and ask for resolution or include it as a halt condition.

## Artifact selection

Use these references as needed:

- `references/architecture-template.md` for solution architecture and software design specs.
- `references/adr-template.md` for architecture decision records.
- `references/interface-contract-template.md` for API, event, schema, and module contracts.
- `references/migration-plan-template.md` for phased migrations and compatibility plans.
- `references/output-contract.md` for artifact wrapper, source facts, and handoff rules.
- `references/handoff-rules.md` when design output will feed issue planning, verification, security, or `implementation-handoff-desk`.
- `references/halt-conditions.md` when input or connector facts are insufficient.

## Required output properties

Every design artifact must include:

- design goal and scope;
- source facts and citations or explicit source notes;
- non-goals and constraints;
- current-state architecture when relevant;
- proposed architecture;
- component/module boundaries;
- data, API, or integration contracts when relevant;
- tradeoffs and rejected options;
- risks and mitigations;
- verification and test implications;
- security/privacy considerations;
- migration and rollout notes when relevant;
- downstream handoff notes for issue planning and implementation.

Do not bury unknowns. Open questions and assumptions must be visible and actionable.

## Halt behavior

Halt or produce a connector diagnostic instead of a confident design when any of these apply:

- repo-aware design is requested but GitHub/repo facts are unavailable;
- a required PRD/SRS/discovery source is missing;
- existing architecture cannot be determined from the available sources;
- source facts conflict and the user has not resolved the conflict;
- the design would require unsafe speculation about security, data retention, compliance, or production behavior;
- requested scope is too broad to produce a reviewable architecture artifact.

## Composition with other SDLC skills

Inputs typically come from `product-requirements-desk`, `technical-discovery-desk`, issues, docs, and repo context. Outputs feed `issue-planning-desk`, `security-threat-desk`, `verification-desk`, `docs-traceability-desk`, and `implementation-handoff-desk`. When implementation work is ready, do not write implementation prompts directly unless asked; provide handoff notes suitable for `implementation-handoff-desk`.

## Optional script

Use `scripts/write_design_markdown.py` when a downloadable Markdown artifact is needed and the environment supports file creation. The script wraps supplied content with a title, usage section, and source facts.
