# Maintenance Refactor Desk

`maintenance-refactor-desk` is an SDLC skill for connector-grounded maintenance planning: refactors, dependency upgrades, dead-code cleanup, migrations, and technical-debt reduction.

## Intended inputs

- Maintenance requests or technical-debt notes.
- GitHub repositories, files, dependency manifests, branches, PRs, and issues.
- Architecture docs, migration plans, release notes, runbooks, and compatibility policies.
- CI history, flaky tests, build failures, test coverage, and regression reports.
- Security/dependency scan findings when relevant.

## Intended outputs

- Maintenance assessment.
- Refactor plan.
- Dependency upgrade plan.
- Migration sequence.
- Dead-code cleanup plan.
- Regression-control checklist.
- Downstream handoff notes for `implementation-handoff-desk`, `test-strategy-desk`, `verification-desk`, `ci-failure-desk`, `security-threat-desk`, and release/deployment skills.

## Required connectors

Use GitHub when repo, file, dependency, PR, issue, branch, or CI facts are needed. Use document connectors for architecture, migration, release, policy, or runbook context. Use issue/project connectors for acceptance criteria and prioritization. Use CI/security evidence when failures, vulnerabilities, or dependency upgrades drive the work.

## Design stance

Maintenance work is high-risk when it expands silently. This skill prioritizes narrow scope, non-goals, proof of necessity, regression controls, and halt conditions.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
