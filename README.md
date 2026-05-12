# SDLC Command Desk

Token-efficient software delivery skills for vibe coders, solo builders, and AI-native engineering teams.

SDLC Command Desk is a public skills lab for building, packaging, and sharing Agentic SDLC skills. The goal is simple: let builders stay creative while the skills handle lifecycle structure, source grounding, safety gates, and low-token implementation handoffs.

Think freely. Ship safely. Spend coding-agent tokens on code, not chaos.

## Quick links

- [Manifest](MANIFEST.md) — ordered list of every skill in the suite.
- [Install and use guide](docs/INSTALL.md) — how to install and use the skills in ChatGPT.
- [Checksums](CHECKSUMS.txt) — SHA256 hashes for release artifacts.
- [Release notes](releases/v0.1.1.md) — workflow-linked `v0.1.1` suite release notes.
- [Release publishing guide](releases/README.md) — artifact and release policy.

## What this repository contains

This repository contains packaged and source-ready skills for an AI-native software development lifecycle.

The suite is organized around one top-level orchestrator skill:

- `sdlc-command-desk` — orchestrates end-to-end lifecycle flow, enforces connector preflight, prevents premature implementation, and coordinates the SDLC skill suite.

And the lifecycle desks:

- `product-requirements-desk` — product requirements, acceptance criteria, non-goals, risks, and downstream handoff notes.
- `technical-discovery-desk` — repo recon, feasibility, constraints, unknowns, spikes, and risk registers.
- `architecture-design-desk` — architecture specs, ADRs, interface contracts, component boundaries, and migration plans.
- `issue-planning-desk` — GitHub-ready issue plans, milestones, dependency graphs, labels, and acceptance gates.
- `implementation-handoff-desk` — low-token coding-agent handoffs for scoped branch, commit, PR, merge-train, halt-resume, docs/proof, and repo-operation work.
- `review-quality-desk` — PR review, diff risk, scope creep checks, missing-test assessment, and review recommendations.
- `test-strategy-desk` — QA scenarios, regression plans, fixture plans, and coverage-gap reports.
- `verification-desk` — V&V reports, requirements traceability matrices, acceptance gates, evidence maps, and release blockers.
- `docs-traceability-desk` — proof maps, claim maps, doc-code consistency, knowledge indexes, and audit evidence.
- `security-threat-desk` — threat modeling, trust boundaries, dependency/security review, and mitigation mapping.
- `ci-failure-desk` — CI failure triage, flaky-test classification, rerun policy, root-cause analysis, and pipeline health.
- `release-operations-desk` — release readiness, release notes, version/tag planning, rollback planning, and post-release verification.
- `deployment-desk` — deployment plans, rollout stages, feature flags, change management, go/no-go gates, and post-deploy checks.
- `observability-readiness-desk` — telemetry design, logs/metrics/traces, SLO notes, alerts, dashboards, and runbooks.
- `incident-response-desk` — incident triage, severity classification, RCA, hotfix handoff, and follow-up issue planning.
- `maintenance-refactor-desk` — refactor planning, dependency upgrades, migrations, dead-code removal, and regression controls.
- `retrospective-desk` — retrospectives, cycle metrics, process improvements, and follow-up action plans.
- `decommissioning-desk` — feature/API/system retirement, cutover planning, data retention, communications, archive rules, and rollback-safe shutdown.

## Operating model

The suite follows a staged SDLC model:

```text
idea
  -> requirements
  -> technical discovery
  -> architecture and design
  -> issue planning
  -> implementation handoff
  -> review
  -> testing
  -> verification
  -> security
  -> CI/CD
  -> release
  -> deployment
  -> observability
  -> incident response
  -> maintenance
  -> retrospective
  -> decommissioning
```

The intent is not to make builders slower. The intent is to remove repeated process thinking so coding agents can spend more of their token budget on code, tests, and validation.

## Token-efficiency principle

The SDLC skills should reduce ambiguity before work reaches a coding agent.

Upstream desks produce structured source-of-truth artifacts. The implementation handoff desk then compresses those artifacts into concise execution prompts with:

- exact scope
- exact files when known
- exact branch and base facts when available
- exact allowed and forbidden changes
- exact validation commands
- exact halt conditions
- exact PR body requirements

This keeps Codex, Claude Code, and similar tools from wasting tokens rediscovering process, requirements, architecture, tests, or release expectations.

## Connector-grounding principle

Skills should use live connected sources when available.

GitHub is treated as the source of truth for:

- repositories
- branches
- commits
- pull requests
- issues
- changed files
- CI/check status
- workflow logs
- tests and source files

Docs and communication sources are used for:

- roadmap context
- product decisions
- architecture notes
- audit evidence
- stakeholder decisions
- release and operational context

If required source facts are missing or conflicting, the correct behavior is to halt or produce a connector diagnostic. Do not invent repo state, issue IDs, branch names, test names, CI status, or acceptance criteria.

## Install

See [docs/INSTALL.md](docs/INSTALL.md) for the full installation and usage guide.

Recommended install order:

```text
000-sdlc-command-desk-skill.zip
001-product-requirements-desk-skill.zip
002-technical-discovery-desk-skill.zip
003-architecture-design-desk-skill.zip
004-issue-planning-desk-skill.zip
005-implementation-handoff-desk-skill.zip
006-review-quality-desk-skill.zip
007-test-strategy-desk-skill.zip
008-verification-desk-skill.zip
009-docs-traceability-desk-skill.zip
010-security-threat-desk-skill.zip
011-ci-failure-desk-skill.zip
012-release-operations-desk-skill.zip
013-deployment-desk-skill.zip
014-observability-readiness-desk-skill.zip
015-incident-response-desk-skill.zip
016-maintenance-refactor-desk-skill.zip
017-retrospective-desk-skill.zip
018-decommissioning-desk-skill.zip
```

## Packaging rule

Each individual skill should be packaged as a valid uploadable skill archive. When preparing a skill for upload, the final archive should be named `skill.zip`.

For repository organization, archives may use descriptive filenames such as:

```text
005-implementation-handoff-desk-skill.zip
```

The uploaded archive itself should still contain one valid skill directory with a valid `SKILL.md`.

## Release artifacts

The `v0.1.1` workflow-linked release artifact set contains all 19 packaged skill archives plus `CHECKSUMS.txt`.

Use `CHECKSUMS.txt` to verify downloads before installing. PowerShell example:

```powershell
Get-FileHash .\000-sdlc-command-desk-skill.zip -Algorithm SHA256
```

To publish the GitHub Release from a local artifact folder, use the ASCII-safe helper script:

```powershell
powershell -ExecutionPolicy Bypass -File .\publish-v0.1.1.ps1
```

## Repository layout

```text
docs/
  Research notes, lifecycle maps, sprint prompts, operating standards, and install/use docs.

releases/
  Release notes, release policy, and release publishing helpers.

skills/
  Packaged skill archives and/or unpacked skill source directories.
```

## Current status

The workflow-linked SDLC suite source is now published under `skills/`.

Completed repository support:

- Manifest for the workflow-linked suite.
- Workflow-linked suite source imported for all 19 desks under `skills/`.
- Shared `suite-workflow-contract.md` present in every desk.
- `sdlc-command-desk` includes orchestrator contracts and workflow runner script.
- Complete `CHECKSUMS.txt` for the `v0.1.1` release artifact set.
- Install/use instructions for ChatGPT users.
- Release artifact guidance.
- `v0.1.1` release notes.
- ASCII-safe `v0.1.1` publish script.

Remaining work:

- Publish the GitHub Release `v0.1.1` and attach all stable release assets.
