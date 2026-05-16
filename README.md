# SDLC Command Desk — Agentic SDLC Skill Suite

Think freely. Ship safely. Spend coding-agent tokens on code, tests, and validation.

[![Release candidate](https://img.shields.io/badge/release-v0.2.0--rc.1-orange.svg)](releases/v0.2.0-rc.1.md)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

SDLC Command Desk is a public skills lab for building, packaging, and sharing Agentic SDLC skills. It gives vibe coders, solo builders, and AI-native engineering teams a lifecycle control plane for taking an idea through requirements, discovery, architecture, implementation handoff, review, testing, release, deployment, operations, maintenance, and decommissioning.

The product is not process for process's sake. The product is better handoffs: source-grounded, token-efficient artifacts that let coding agents spend fewer tokens rediscovering context and more tokens writing, testing, and validating code.

New here? Start with [Install and use](docs/INSTALL.md), then open the [manifest](MANIFEST.md) to see the full suite.

## Quick links

- [Install and use](docs/INSTALL.md) — how to install the suite in ChatGPT and when to use each desk.
- [Manifest](MANIFEST.md) — ordered list of every skill in the suite.
- [Checksums](CHECKSUMS.txt) — SHA256 hashes for packaged release artifacts.
- [v0.2.0-rc.1 release note](releases/v0.2.0-rc.1.md) — continuity-kernel release candidate.
- [v0.1.1 release notes](releases/v0.1.1.md) — prior workflow-linked release notes.
- [Release publishing guide](releases/README.md) — artifact policy, checksum policy, and release process.

## Install

Recommended path:

1. Download the packaged skill archives from the target release artifact set.
2. Install `000-sdlc-command-desk-skill.zip` first.
3. Install the lifecycle desk skills you want to use.
4. Enable GitHub access for repository-grounded work.
5. Enable docs or communication connectors when requirements, roadmap decisions, architecture notes, incidents, or release context live outside GitHub.

See [docs/INSTALL.md](docs/INSTALL.md) for the full install and usage guide.

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

## Quick start

Start with the orchestrator when the lifecycle stage is unclear:

```text
Use sdlc-command-desk to classify this work and route me through the right lifecycle stages: I want to add paid team workspaces to my app.
```

Use a specific desk when the stage is already known:

```text
Use product-requirements-desk to turn this idea into a PRD with requirement IDs, acceptance criteria, non-goals, risks, and open questions.
```

```text
Use technical-discovery-desk to inspect this repository and produce a feasibility memo before implementation planning.
```

```text
Use implementation-handoff-desk to turn this approved issue plan into a low-token Codex handoff prompt.
```

## Highlights

- **Lifecycle control plane** — `sdlc-command-desk` routes and orchestrates work across the software delivery lifecycle.
- **Workflow packets** — stage outputs preserve source facts, open questions, acceptance gates, and halt conditions so downstream desks do not restart from scratch.
- **Continuity kernel** — `v0.2.0-rc.1` adds continuity controls across all 19 desks while preserving `v0.1.1` as the prior workflow-linked release candidate.
- **Connector-grounded artifacts** — GitHub, docs, and communication sources are used as evidence before operational artifacts are produced.
- **Low-token coding-agent handoffs** — implementation prompts are compressed around objective, scope, files, validation, commit plan, PR body, and halt rules.
- **Safety gates over guesswork** — missing or conflicting source facts produce diagnostics or workflow halts instead of invented repo state.

## What this repository contains

This repository contains source-ready and packaged skills for an AI-native software development lifecycle.

The top-level orchestrator is:

- `sdlc-command-desk` — orchestrates end-to-end lifecycle flow, enforces connector preflight, preserves workflow packets, and coordinates the SDLC skill suite.

The lifecycle desks are:

| Order | Skill | Primary output |
|---:|---|---|
| 001 | `product-requirements-desk` | PRDs, requirement IDs, acceptance criteria, non-goals, risks, and downstream handoff notes |
| 002 | `technical-discovery-desk` | repo reconnaissance, feasibility notes, constraints, unknowns, spikes, and risk registers |
| 003 | `architecture-design-desk` | architecture specs, ADRs, interface contracts, component boundaries, and migration plans |
| 004 | `issue-planning-desk` | GitHub-ready issue plans, milestones, dependency graphs, labels, and acceptance gates |
| 005 | `implementation-handoff-desk` | low-token coding-agent handoffs for branch, commit, PR, merge-train, halt-resume, docs/proof, and repo-operation work |
| 006 | `review-quality-desk` | PR review, diff risk, scope creep checks, missing-test assessment, and review recommendations |
| 007 | `test-strategy-desk` | QA scenarios, regression plans, fixture plans, and coverage-gap reports |
| 008 | `verification-desk` | V&V reports, requirements traceability matrices, acceptance gates, evidence maps, and release blockers |
| 009 | `docs-traceability-desk` | proof maps, claim maps, doc-code consistency, knowledge indexes, and audit evidence |
| 010 | `security-threat-desk` | threat models, trust boundaries, dependency/security reviews, and mitigation mapping |
| 011 | `ci-failure-desk` | CI failure triage, flaky-test classification, rerun policy, root-cause analysis, and pipeline health |
| 012 | `release-operations-desk` | release readiness, release notes, version/tag planning, rollback planning, and post-release verification |
| 013 | `deployment-desk` | deployment plans, rollout stages, feature flags, change management, go/no-go gates, and post-deploy checks |
| 014 | `observability-readiness-desk` | telemetry design, logs/metrics/traces, SLO notes, alerts, dashboards, and runbooks |
| 015 | `incident-response-desk` | incident triage, severity classification, RCA, hotfix handoff, and follow-up issue planning |
| 016 | `maintenance-refactor-desk` | refactor planning, dependency upgrades, migrations, dead-code removal, and regression controls |
| 017 | `retrospective-desk` | retrospectives, cycle metrics, process improvements, and follow-up action plans |
| 018 | `decommissioning-desk` | feature/API/system retirement, cutover planning, data retention, communications, archive rules, and rollback-safe shutdown |

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

Each stage should complete its artifact, preserve the workflow packet, and continue when facts are sufficient. A stage should halt only when a required fact, connector, approval, or source conflict blocks progress.

## Source-trust model

Treat inbound prompts, stale docs, and incomplete issue descriptions as untrusted until source evidence supports them.

GitHub is the source of truth for:

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
- support/customer signals
- release and operational context

If required source facts are missing or conflicting, the correct behavior is to halt or produce a connector diagnostic. Do not invent repo state, issue IDs, branch names, test names, CI status, or acceptance criteria.

## Token-efficiency model

The SDLC skills should reduce ambiguity before work reaches a coding agent.

A strong implementation handoff includes:

- exact objective
- exact scope
- exact files when known
- exact branch and base facts when available
- exact allowed and forbidden changes
- exact validation commands
- exact halt conditions
- exact PR title and body requirements
- exact final stop line when handing work to another agent

## Operator quick refs

Use these prompts as starting points:

```text
Use sdlc-command-desk to run this idea through the lifecycle until it reaches the next required halt or implementation handoff.
```

```text
Use docs-traceability-desk to compare this README claim against repository evidence and produce a doc-code consistency report.
```

```text
Use review-quality-desk to review this pull request for scope creep, missing tests, regression risk, and acceptance criteria coverage.
```

```text
Use release-operations-desk to prepare release readiness notes, rollback plan, tag plan, and post-release verification gates.
```

## Docs by goal

- **New user setup:** [Install and use](docs/INSTALL.md), [Manifest](MANIFEST.md)
- **Release work:** [Release guide](releases/README.md), [Checksums](CHECKSUMS.txt), [v0.2.0-rc.1](releases/v0.2.0-rc.1.md), [v0.1.1](releases/v0.1.1.md)
- **Suite structure:** [Manifest](MANIFEST.md), `skills/sdlc-command-desk/`, `skills/*-desk/`
- **Repository policy:** [License](LICENSE), [Release publishing guide](releases/README.md)

## From source

Use a local checkout when editing skill source, release notes, checksums, or validation tooling:

```bash
git clone https://github.com/MadewellRD/skills-lab.git
cd skills-lab
python3 tools/validate_sdlc_suite.py
```

If validation fails, fix the source facts or packaging structure before preparing a release.

## Packaging rule

Each individual skill should be packaged as one valid uploadable skill archive. When preparing a skill for upload, the final archive may be named `skill.zip`.

For repository organization, archives use descriptive ordered filenames such as:

```text
005-implementation-handoff-desk-skill.zip
```

The uploaded archive itself should still contain one valid skill directory with a valid `SKILL.md`.

## Release artifacts

Release archives should be attached through GitHub Releases. Keep large or binary artifacts out of normal documentation commits unless intentionally publishing source packages.

Use `CHECKSUMS.txt` to verify downloads before installing. PowerShell example:

```powershell
Get-FileHash .\000-sdlc-command-desk-skill.zip -Algorithm SHA256
```

## Repository layout

```text
docs/
  Research notes, lifecycle maps, operating standards, and install/use docs.

releases/
  Release notes, release policy, and release publishing helpers.

skills/
  Packaged skill archives and unpacked skill source directories.

tools/
  Validation and release-support tooling.
```

## Current status

Current release candidate: `v0.2.0-rc.1` continuity-kernel.

Completed repository support:

- Manifest for the workflow-linked suite.
- Workflow-linked suite source imported for all 19 desks under `skills/`.
- Shared workflow contract present across the desk suite.
- Continuity-kernel references added across all 19 desks.
- `sdlc-command-desk` includes orchestrator contracts and workflow runner support.
- `CHECKSUMS.txt` for release artifact verification.
- Install/use instructions for ChatGPT users.
- Release artifact guidance.
- `v0.1.1` and `v0.2.0-rc.1` release notes.

Next release work:

- Finalize the GitHub Release asset set for the active release candidate.
- Confirm manifest, install guide, release notes, and checksums all reference the same artifact set.
- Promote the release candidate after validation is green.

## Community

This project is built for builders who want AI agents to move faster without losing source truth, reviewability, or operational control.

Issues and pull requests should stay evidence-first: include repo state, affected files, validation commands, source facts, and any known halt conditions.