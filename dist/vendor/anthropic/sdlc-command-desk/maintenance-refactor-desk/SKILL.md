---
name: maintenance-refactor-desk
description: create connector-grounded maintenance, refactor, dependency-upgrade, dead-code removal, migration, and technical-debt reduction artifacts for software delivery. use when Claude needs to assess refactor scope, plan safe code cleanup, sequence dependency upgrades, evaluate migration risk, define regression controls, prevent scope creep, or prepare downstream handoff notes for implementation-handoff-desk, test-strategy-desk, verification-desk, ci-failure-desk, security-threat-desk, or release-operations-desk workflows.
---

# Maintenance Refactor Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Purpose

Use this skill to turn maintenance intent into bounded, evidence-backed refactor and upgrade plans. The skill produces planning artifacts, not speculative code changes. It is optimized for safe system health work where uncontrolled scope expansion is the main failure mode.

## Operating model

**Outcome.** A bounded, evidence-backed maintenance artifact for the request type: a refactor (structure-preserving internal code change), a dependency upgrade (package, SDK, runtime, framework, or toolchain), a migration (moved API, storage, framework, service, module, or architecture boundary), a dead-code cleanup (unused files, symbols, routes, flags, configs, docs, or tests), or technical-debt reduction (debt register, prioritization, sequencing, or risk controls).

**Grounding.** Use GitHub for repo files, dependency manifests, branches, PRs, issues, tests, CI, ownership, and commit history. Use issue/project connectors for maintenance tickets, acceptance criteria, labels, owners, and blockers. Use document connectors for architecture docs, migration notes, deprecation plans, runbooks, release policy, and prior audits. Use CI connectors or GitHub Actions data for pipeline failures, flaky tests, build matrix, and validation history. Use security or dependency scan evidence when an upgrade has security implications.

**Observation versus recommendation.** Do not present inferred dead code, unused dependencies, or safe migrations as proven unless source evidence supports the claim. Mark uncertain findings as candidates and attach the gate that would confirm them.

**Artifact selection.** Maintenance assessments use `references/maintenance-assessment-template.md`. Refactor plans use `references/refactor-plan-template.md`. Dependency upgrade plans use `references/dependency-upgrade-template.md`. Migration sequences use `references/migration-sequence-template.md`. Dead-code cleanups use `references/dead-code-cleanup-template.md`. Regression controls use `references/regression-control-template.md`.

**Parallel surface.** Assessment fans out: dead-code candidates, dependency entries, modules, and debt items are independent to analyze, and reference-searching each candidate across the repo is independent work. Assess them in parallel. Sequencing is not parallel — upgrade order, migration steps, and cutover ordering are dependency-constrained content and must be emitted as an ordered sequence, not a set.

**Packaging.** When a downloadable artifact is useful, use `scripts/write_maintenance_markdown.py` to wrap the content with a title, use instructions, source facts, and assumptions. If the user needs implementation, continue into the implementation handoff stage after the maintenance scope is bounded.

**Acceptance bar.** The artifact is done when scope and non-goals are stated tightly enough that an implementer cannot reasonably expand them; every dead-code or unused-dependency claim names the search evidence behind it and is labeled proven or candidate; each change carries its risk class from `Risk controls` below; regression coverage and rollback are named per change rather than in general; and the ordered sequence is explicit wherever order matters. Do not invent file paths, symbols, dependency versions, compatibility matrices, test names, CI status, or ownership.

## Required outputs

Every maintenance artifact must include:

- Scope statement and non-goals.
- Source facts used.
- Risk classification.
- Affected files, modules, packages, or services when known.
- Verification commands or evidence requirements.
- Rollback or revert considerations.
- Explicit halt conditions.
- Downstream handoff notes when implementation work is required.

## Risk controls

Default to conservative scope. Prefer small PRs when a change affects runtime behavior, build tooling, dependency resolution, authentication, data migration, persistence, public APIs, or deployment behavior.

Classify changes as:

- Mechanical: formatting, rename with references updated, import cleanup, generated config refresh.
- Behavioral risk: any runtime semantics, API contract, dependency behavior, or data handling change.
- Structural risk: module boundaries, package layout, build system, deployment or CI behavior.
- Release risk: changes requiring rollout, migration, compatibility windows, or rollback planning.

## Halt conditions

Proceed by default. Unknown scope is bounded with a labeled assumption and a narrower plan, not a stop — scope creep, not uncertainty, is this desk's failure mode. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval** — the plan would accept behavioral risk, waive regression coverage, or expand agreed scope, and a human owner must authorize it.
- **Production or destructive** — deletion is proposed on inferential dead-code evidence with no confirming gate available, or the change would cross a release, deployment, or data-migration boundary without the relevant downstream desk.
- **Security or privacy** — an upgrade carries a known vulnerability decision, or the change touches authentication, authorization, secrets, or crypto without security review.
- **Source conflict** — GitHub, docs, and tickets genuinely disagree on the current state or the intended target.
- **Release integrity** — the plan would be presented as safe when required tests or CI gates cannot be identified, or the upgrade target and compatibility matrix are unknown.
- **Connector unreachable** — required repo or dependency evidence exists but cannot be read. Evidence that is merely absent is a soft gap: mark the finding a candidate rather than proven, and continue.

A requested refactor that includes feature changes is a scoping problem: split the feature work out, say that you did, and continue with the structure-preserving portion.

## Composition with other SDLC skills

- Use `technical-discovery-desk` first when the system is not understood.
- Use `architecture-design-desk` first when refactoring changes component boundaries or interfaces.
- Use `security-threat-desk` for dependency vulnerabilities, auth/authz, secrets, crypto, or privacy impact.
- Use `test-strategy-desk` to design regression coverage.
- Use `verification-desk` to prove maintenance work preserved requirements.
- Use `ci-failure-desk` when maintenance is driven by build or test failures.
- Use `release-operations-desk` and `deployment-desk` for release-sensitive migrations.
- Use `implementation-handoff-desk` only after the maintenance scope, guardrails, validation, and halt conditions are clear.

## Bundled references

- `references/connector-routing.md`: source selection and required facts.
- `references/source-hierarchy.md`: truth precedence and conflict behavior.
- `references/maintenance-assessment-template.md`: current-state and debt assessment format.
- `references/refactor-plan-template.md`: bounded refactor plan format.
- `references/dependency-upgrade-template.md`: upgrade sequencing and compatibility format.
- `references/migration-sequence-template.md`: migration and cutover plan format.
- `references/dead-code-cleanup-template.md`: dead-code candidate and proof format.
- `references/regression-control-template.md`: validation and regression guardrails.
- `references/output-contract.md`: artifact wrappers and deliverable expectations.
- `references/handoff-rules.md`: downstream SDLC skill handoff rules.
- `references/halt-conditions.md`: mandatory stop points.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
