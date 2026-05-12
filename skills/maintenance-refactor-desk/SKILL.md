---
name: maintenance-refactor-desk
description: create connector-grounded maintenance, refactor, dependency-upgrade, dead-code removal, migration, and technical-debt reduction artifacts for software delivery. use when chatgpt needs to assess refactor scope, plan safe code cleanup, sequence dependency upgrades, evaluate migration risk, define regression controls, prevent scope creep, or prepare downstream handoff notes for implementation-handoff-desk, test-strategy-desk, verification-desk, ci-failure-desk, security-threat-desk, or release-operations-desk workflows.
---

# Maintenance Refactor Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Purpose

Use this skill to turn maintenance intent into bounded, evidence-backed refactor and upgrade plans. The skill produces planning artifacts, not speculative code changes. It is optimized for safe system health work where uncontrolled scope expansion is the main failure mode.

## Operating model

1. Classify the maintenance request.
   - Refactor: structure-preserving internal code change.
   - Dependency upgrade: package, SDK, runtime, framework, or toolchain update.
   - Migration: moved API, storage, framework, service, module, or architecture boundary.
   - Dead-code cleanup: unused files, symbols, routes, flags, configs, docs, or tests.
   - Technical-debt reduction: debt register, prioritization, sequencing, or risk controls.

2. Run connector preflight.
   - Use GitHub for repo files, dependency manifests, branches, PRs, issues, tests, CI, ownership, and commit history.
   - Use issue/project connectors for maintenance tickets, acceptance criteria, labels, owners, and blockers.
   - Use document connectors for architecture docs, migration notes, deprecation plans, runbooks, release policy, and prior audits.
   - Use CI connectors or GitHub Actions data for pipeline failures, flaky tests, build matrix, and validation history.
   - Use security/dependency scan evidence when an upgrade has security implications.

3. Separate observation from recommendation.
   Do not present inferred dead code, unused dependencies, or safe migrations as proven unless source evidence supports the claim. Mark uncertain findings as candidates and require verification gates.

4. Choose the artifact type.
   - Maintenance assessment: use `references/maintenance-assessment-template.md`.
   - Refactor plan: use `references/refactor-plan-template.md`.
   - Dependency upgrade plan: use `references/dependency-upgrade-template.md`.
   - Migration sequence: use `references/migration-sequence-template.md`.
   - Dead-code cleanup: use `references/dead-code-cleanup-template.md`.
   - Regression controls: use `references/regression-control-template.md`.

5. Package output.
   When a downloadable artifact is useful, use `scripts/write_maintenance_markdown.py` to wrap the content with a title, use instructions, source facts, and assumptions. If the user needs implementation, continue into the implementation handoff stage after the maintenance scope is bounded.

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

Halt and report instead of drafting a confident plan when:

- Required repo or dependency evidence is unavailable.
- Source facts conflict across GitHub, docs, and tickets.
- The requested refactor includes feature changes.
- The upgrade target or compatibility matrix is unknown.
- Dead-code evidence is inferential only and no verification path exists.
- Required tests or CI gates cannot be identified.
- The change would cross release/deployment/security boundaries without the relevant downstream desk.

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
