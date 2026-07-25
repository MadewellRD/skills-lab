---
name: architecture-design-desk
description: create connector-grounded architecture and solution design artifacts from product requirements, technical discovery, repository structure, constraints, and stakeholder decisions. use when ChatGPT needs to produce software design specs, architecture decision records, component boundaries, interface contracts, migration plans, risk notes, source-fact evidence, or downstream implementation handoff notes for issue planning, verification, security, or implementation-handoff-desk workflows.
---

# Architecture Design Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Purpose

Use this skill to turn requirements and technical discovery into architecture artifacts that can be implemented, reviewed, verified, and traced. The skill must distinguish source-backed facts from design judgment and must not invent repository structure, APIs, ownership, dependencies, constraints, or production behavior.

## Required operating model

Before drafting any design artifact, perform connector preflight.

**Outcome.** A Markdown design artifact in the mode the request calls for, new architecture, incremental design, migration design, interface contract, ADR set, or implementation handoff, built from the appropriate reference template and carrying source facts, unresolved risks, and downstream handoff notes.

**Constraints.** Gather source facts from the highest-trust available connectors. Keep facts, inferences, decisions, assumptions, and open questions visibly separate throughout the artifact; do not merge them into a single confident narrative.

**Parallel surface.** Components, modules, interface contracts, and individual ADRs are independent design units once the boundaries are set. Gather evidence for them and draft them in parallel rather than serially, then reconcile for cross-component consistency in a single pass.

**Acceptance bar.** The design is done when a competent implementer can act on it without re-deriving the decisions: component and module boundaries are named, every interface or data contract the change depends on is specified, tradeoffs and rejected options are stated with the reason, risks carry mitigations, and open questions are visible and actionable rather than buried. Do not invent repository structure, APIs, ownership, dependencies, constraints, or production behavior.

## Connector expectations

GitHub is required for repo-aware design. Use it to verify modules, files, APIs, tests, dependency manifests, prior PRs, and existing architecture patterns. Document connectors are required when the design depends on PRDs, SRS docs, discovery memos, roadmap docs, or architecture records. Issue/project connectors are required when design scope comes from tickets, milestones, labels, or acceptance criteria. Communication connectors are optional but useful for recent stakeholder decisions; treat them as decision context, not code truth.

Apply `references/source-hierarchy.md` when sources conflict. If current user instruction conflicts with existing docs or repo state, preserve the conflict explicitly and ask for resolution or include it as a halt condition.

## Artifact selection

A design run normally draws on several of these at once rather than one: the architecture spec carries the design, the ADRs carry the decisions inside it, and the interface contracts carry what the change depends on. Load a template when the artifact it shapes is genuinely in scope, and mark a shape not applicable when the change does not involve it; a migration plan for a change that moves nothing is padding, not completeness.

- `references/architecture-template.md` for solution architecture and software design specs.
- `references/adr-template.md` for architecture decision records.
- `references/interface-contract-template.md` for API, event, schema, and module contracts.
- `references/migration-plan-template.md` for phased migrations and compatibility plans.
- `references/output-contract.md` for artifact wrapper, source facts, and handoff rules.
- `references/handoff-rules.md` when design output will feed issue planning, verification, security, or `implementation-handoff-desk`.
- `references/halt-conditions.md` when input or connector facts are insufficient.

## Required output properties

A complete design run delivers, together: the design artifact itself, an ADR for every decision it makes that a maintainer would otherwise have to reverse-engineer, the interface or data contracts the change depends on, and the downstream handoff notes for issue planning and implementation. Migration and rollout notes join that set whenever the change moves an existing system rather than adding to it. These are not alternatives to pick between; a design that records no decisions and specifies no contracts has not finished.

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

Each of those carries weight only at implementable depth. A contract states its operations, payloads, error behavior, and compatibility expectations. An ADR states the context, the options weighed, the choice, and what the choice costs. A boundary states what sits on each side of it and what crosses. A section heading with a sentence of intent underneath is not the property being asked for.

Components and ADRs are independent once boundaries are set, which is what the parallel surface above refers to: the artifacts in the set are drafted concurrently, then reconciled in one pass.

Do not bury unknowns. Open questions and assumptions must be visible and actionable.

Producing the whole set is not a reason to produce any part of it from imagination. Where the repository, an existing contract, or an ownership fact could not be established, the artifact says the contract is unspecified and names what would specify it. An invented interface costs more than a missing one, because issue planning and implementation will both build on it.

## Halt behavior

Proceed by default. Design work is inherently underdetermined: where a fact is missing, choose the most defensible option, label it inline as an assumption, and record it as an open question. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval**: the design commits to a decision that a named human owner must authorize, such as a platform, vendor, or data-residency choice.
- **Production or destructive**: the design implies an irreversible migration or data-destructive cutover whose rollback path is not established.
- **Security or privacy**: the design would require speculation about security controls, data retention, or compliance obligations that no source supports.
- **Source conflict**: repo state, PRD/SRS, and stakeholder decisions genuinely disagree on a load-bearing constraint. Preserve the conflict explicitly and halt rather than choosing silently.
- **Release integrity**: the artifact would present an unreviewable design as accepted.
- **Connector unreachable**: a required repo or spec source exists but cannot be read for a repo-aware design. A source that is merely absent is a soft gap: produce a scoped design marked user-fact-only, with the unknown architecture stated as an open question, and continue.

When requested scope is too broad for one reviewable artifact, narrow it and say what was excluded rather than halting.

Use `references/halt-conditions.md` for the halt artifact format.

## Composition with other SDLC skills

Inputs typically come from `product-requirements-desk`, `technical-discovery-desk`, issues, docs, and repo context. Outputs feed `issue-planning-desk`, `security-threat-desk`, `verification-desk`, `docs-traceability-desk`, and `implementation-handoff-desk`. When implementation work is ready, do not write implementation prompts directly unless asked; provide handoff notes suitable for `implementation-handoff-desk`.

## Optional script

Use `scripts/write_design_markdown.py` when a downloadable Markdown artifact is needed and the environment supports file creation. The script wraps supplied content with a title, usage section, and source facts.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
