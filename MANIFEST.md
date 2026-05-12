# SDLC Command Desk Manifest

This manifest tracks the workflow-linked SDLC Command Desk skill suite.

## Suite identity

- Suite name: SDLC Command Desk
- Suite version: v0.1.1 workflow-linked
- Repository: https://github.com/MadewellRD/skills-lab
- Audience: vibe coders, solo builders, and AI-native engineering teams
- Purpose: reduce SDLC ambiguity and help coding agents spend more tokens on code, tests, and validation instead of rediscovering process.

## Package naming convention

Repository-facing archives use ordered descriptive names:

```text
000-sdlc-command-desk-skill.zip
001-product-requirements-desk-skill.zip
```

Upload-facing archives should still contain one valid skill and may be renamed to `skill.zip` when uploading through ChatGPT.

## Core suite

| Order | Skill | Role | Lifecycle position | Status |
|---:|---|---|---|---|
| 000 | `sdlc-command-desk` | top-level SDLC router/orchestrator | lifecycle control plane | created |
| 001 | `product-requirements-desk` | PRDs, requirement IDs, acceptance criteria, non-goals, risks | requirements | created |
| 002 | `technical-discovery-desk` | repo recon, feasibility, constraints, unknowns, spikes, risk registers | discovery | created |
| 003 | `architecture-design-desk` | architecture specs, ADRs, interface contracts, migrations | design | created |
| 004 | `issue-planning-desk` | GitHub issue plans, milestones, dependency graphs, acceptance gates | planning | created |
| 005 | `implementation-handoff-desk` | low-token coding-agent handoffs for implementation, branch, commit, PR, halt-resume, and merge-train work | implementation handoff | created |
| 006 | `review-quality-desk` | PR review, diff risk, scope creep, missing-test assessment | review | created |
| 007 | `test-strategy-desk` | QA scenarios, regression plans, fixture plans, coverage gaps | testing | created |
| 008 | `verification-desk` | V&V reports, RTMs, acceptance gates, evidence maps, blockers | verification | created |
| 009 | `docs-traceability-desk` | proof maps, claim maps, doc-code consistency, knowledge index | documentation and traceability | created |
| 010 | `security-threat-desk` | threat modeling, trust boundaries, dependency/security review | security | created |
| 011 | `ci-failure-desk` | CI failure triage, flaky-test classification, rerun policy, root-cause analysis | CI/CD | created |
| 012 | `release-operations-desk` | release readiness, notes, version/tag plan, rollback plan | release | created |
| 013 | `deployment-desk` | deployment planning, rollout stages, feature flags, go/no-go gates | deployment | created |
| 014 | `observability-readiness-desk` | telemetry design, logs/metrics/traces, SLOs, alerts, runbooks | observability | created |
| 015 | `incident-response-desk` | incident triage, severity, RCA, hotfix handoff, follow-up issues | incident response | created |
| 016 | `maintenance-refactor-desk` | refactors, dependency upgrades, migrations, dead-code cleanup | maintenance | created |
| 017 | `retrospective-desk` | retrospectives, cycle metrics, process improvements, action plans | continuous improvement | created |
| 018 | `decommissioning-desk` | feature/API/system retirement, cutover, data retention, communications, rollback-safe shutdown | decommissioning | created |

Source publication status: all 19 workflow-linked skill source directories are published under `skills/`.

## Operating rules

Every skill in the suite should preserve these principles:

1. Keep the user creative and avoid unnecessary process friction.
2. Use connector-grounded facts when available.
3. Treat GitHub as source of truth for repository state.
4. Halt or produce diagnostics instead of inventing missing facts.
5. Produce reusable Markdown artifacts for plans, prompts, reports, checklists, and handoffs.
6. Use `implementation-handoff-desk` only after upstream ambiguity has been reduced.
7. Prefer compact, code-heavy execution handoffs so coding agents spend fewer tokens on planning and more on implementation.

## Release artifact status

Release archives should be attached through GitHub Releases. Keep large or binary artifacts out of normal documentation commits unless intentionally publishing source packages.

Future release support files:

- `releases/README.md`
- `releases/v0.1.1.md`
- `CHECKSUMS.txt`
- `docs/INSTALL.md`
