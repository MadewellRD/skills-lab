# Skills-Lab Manifest

This manifest tracks all command desk suites published in this repository.

## Repository identity

- Repository: https://github.com/MadewellRD/skills-lab
- Audience: vibe coders, solo builders, and AI-native engineering teams
- Purpose: reduce workflow ambiguity and help coding agents spend more tokens on code, tests, and validation instead of rediscovering process.

## Suite registry

| Suite | Version | Source | Packaged | Release status |
|---|---|---|---|---|
| SDLC Command Desk | v0.2.0-rc.1 | `skills/SDLC Command Desk/` | `dist/skills/sdlc-command-desk/` | Released (prerelease promotion pending) |
| Web Development Command Desk | v0.3.0 | `skills/Web Development Command Desk/` | `dist/skills/web-development-command-desk/` | Packaged; GitHub Release pending |
| AI Engineering Command Desk | v0.1.0-source-only | `skills/AI Engineering Command Desk/` | `dist/skills/ai-engineering-command-desk/` | Source-only; zip packaging and GitHub Release pending |
| Sales Revenue Command Desk | v0.1.0 | `skills/Sales Revenue Command Desk/` | `dist/skills/sales-command-desk/` | Packaged; GitHub Release pending |

## Package naming convention

Repository-facing archives use ordered descriptive names:

```text
000-sdlc-command-desk-skill.zip
001-product-requirements-desk-skill.zip
```

Upload-facing archives should still contain one valid skill and may be renamed to `skill.zip` when uploading through ChatGPT.

## SDLC Command Desk — v0.2.0-rc.1 continuity-kernel

19 desks. Continuity kernel, readiness gates, halt taxonomy, preflight cache, Codex conservation policy applied across all desks.

| Order | Skill | Role | Lifecycle position | Status |
|---:|---|---|---|---|
| 000 | `sdlc-command-desk` | top-level SDLC router/orchestrator | lifecycle control plane | packaged |
| 001 | `product-requirements-desk` | PRDs, requirement IDs, acceptance criteria, non-goals, risks | requirements | packaged |
| 002 | `technical-discovery-desk` | repo recon, feasibility, constraints, unknowns, spikes, risk registers | discovery | packaged |
| 003 | `architecture-design-desk` | architecture specs, ADRs, interface contracts, migrations | design | packaged |
| 004 | `issue-planning-desk` | GitHub issue plans, milestones, dependency graphs, acceptance gates | planning | packaged |
| 005 | `implementation-handoff-desk` | low-token coding-agent handoffs for implementation, branch, commit, PR, halt-resume, and merge-train work | implementation handoff | packaged |
| 006 | `review-quality-desk` | PR review, diff risk, scope creep, missing-test assessment | review | packaged |
| 007 | `test-strategy-desk` | QA scenarios, regression plans, fixture plans, coverage gaps | testing | packaged |
| 008 | `verification-desk` | V&V reports, RTMs, acceptance gates, evidence maps, blockers | verification | packaged |
| 009 | `docs-traceability-desk` | proof maps, claim maps, doc-code consistency, knowledge index | documentation and traceability | packaged |
| 010 | `security-threat-desk` | threat modeling, trust boundaries, dependency/security review | security | packaged |
| 011 | `ci-failure-desk` | CI failure triage, flaky-test classification, rerun policy, root-cause analysis | CI/CD | packaged |
| 012 | `release-operations-desk` | release readiness, notes, version/tag plan, rollback plan | release | packaged |
| 013 | `deployment-desk` | deployment planning, rollout stages, feature flags, go/no-go gates | deployment | packaged |
| 014 | `observability-readiness-desk` | telemetry design, logs/metrics/traces, SLOs, alerts, runbooks | observability | packaged |
| 015 | `incident-response-desk` | incident triage, severity, RCA, hotfix handoff, follow-up issues | incident response | packaged |
| 016 | `maintenance-refactor-desk` | refactors, dependency upgrades, migrations, dead-code cleanup | maintenance | packaged |
| 017 | `retrospective-desk` | retrospectives, cycle metrics, process improvements, action plans | continuous improvement | packaged |
| 018 | `decommissioning-desk` | feature/API/system retirement, cutover, data retention, communications, rollback-safe shutdown | decommissioning | packaged |

Checksums: `CHECKSUMS.txt`

## Web Development Command Desk — v0.3.0

14 desks. Covers full web delivery from product intent through launch, operations, maintenance, and growth.

- Source: `skills/Web Development Command Desk/`
- Packaged skills: `dist/skills/web-development-command-desk/`
- Packages: `dist/packages/web-development-command-desk/`
- Manifest: `dist/manifests/web-development-command-desk-MANIFEST.md`
- Checksums: `dist/manifests/web-development-command-desk-CHECKSUMS.txt`

| Order | Skill | Status |
|---:|---|---|
| 000 | `web-development-command-desk` | packaged |
| 001 | `site-product-requirements-desk` | packaged |
| 002 | `information-architecture-desk` | packaged |
| 003 | `ux-ui-design-system-desk` | packaged |
| 004 | `frontend-engineering-desk` | packaged |
| 005 | `backend-integration-desk` | packaged |
| 006 | `cms-content-operations-desk` | packaged |
| 007 | `web-security-secops-desk` | packaged |
| 008 | `web-performance-desk` | packaged |
| 009 | `accessibility-seo-desk` | packaged |
| 010 | `web-testing-qa-desk` | packaged |
| 011 | `web-observability-desk` | packaged |
| 012 | `web-release-deployment-desk` | packaged |
| 013 | `web-maintenance-growth-desk` | packaged |

## AI Engineering Command Desk — v0.1.0-source-only

18 desks. Covers model selection, prompt systems, tool schemas, agent architecture, retrieval/RAG, evals, datasets, fine-tuning, safety, red-team, inference ops, observability, cost/latency, release readiness, and AI incident response.

- Source: `skills/AI Engineering Command Desk/`
- Packaged skills: `dist/skills/ai-engineering-command-desk/`
- Manifest: `dist/manifests/ai-engineering-command-desk-manifest.json`
- Checksums: `dist/manifests/ai-engineering-command-desk-CHECKSUMS.txt`
- Note: Source-only packaging pass. Zip archives and GitHub Release pending.

| Order | Skill | Status |
|---:|---|---|
| 000 | `ai-engineering-command-desk` | packaged (source only) |
| 001 | `model-selection-desk` | packaged (source only) |
| 002 | `prompt-systems-desk` | packaged (source only) |
| 003 | `tool-schema-design-desk` | packaged (source only) |
| 004 | `agent-architecture-desk` | packaged (source only) |
| 005 | `retrieval-rag-design-desk` | packaged (source only) |
| 006 | `eval-design-desk` | packaged (source only) |
| 007 | `eval-run-analysis-desk` | packaged (source only) |
| 008 | `dataset-curation-desk` | packaged (source only) |
| 009 | `synthetic-data-desk` | packaged (source only) |
| 010 | `fine-tuning-desk` | packaged (source only) |
| 011 | `inference-ops-desk` | packaged (source only) |
| 012 | `agent-observability-desk` | packaged (source only) |
| 013 | `cost-latency-optimization-desk` | packaged (source only) |
| 014 | `ai-release-readiness-desk` | packaged (source only) |
| 015 | `ai-incident-response-desk` | packaged (source only) |
| 016 | `ai-safety-review-desk` | packaged (source only) |
| 017 | `red-team-eval-desk` | packaged (source only) |

## Sales Revenue Command Desk — v0.1.0

13 desks. One orchestrator and twelve specialist sub-desks for the full revenue motion.

- Source: `skills/Sales Revenue Command Desk/`
- Packaged skills: `dist/skills/sales-command-desk/`
- Packages: `dist/packages/sales-command-desk/`
- Manifest: `dist/manifests/sales-command-desk-v0.1.0.json`
- Checksums: `CHECKSUMS-sales-command-desk-v0.1.0.txt`

| Order | Skill | Status |
|---:|---|---|
| 000 | `sales-command-desk` | packaged |
| 001 | `lead-research-desk` | packaged |
| 002 | `account-discovery-desk` | packaged |
| 003 | `outbound-sequence-desk` | packaged |
| 004 | `sales-call-prep-desk` | packaged |
| 005 | `qualification-desk` | packaged |
| 006 | `objection-handling-desk` | packaged |
| 007 | `proposal-desk` | packaged |
| 008 | `deal-review-desk` | packaged |
| 009 | `crm-update-desk` | packaged |
| 010 | `pipeline-forecast-desk` | packaged |
| 011 | `renewal-expansion-desk` | packaged |
| 012 | `customer-handoff-desk` | packaged |

## Operating rules

Every skill in every suite preserves these principles:

1. Keep the user creative and avoid unnecessary process friction.
2. Use connector-grounded facts when available.
3. Treat GitHub as source of truth for repository state.
4. Halt or produce diagnostics instead of inventing missing facts.
5. Produce reusable Markdown artifacts for plans, prompts, reports, checklists, and handoffs.
6. Use `implementation-handoff-desk` only after upstream ambiguity has been reduced.
7. Prefer compact, code-heavy execution handoffs so coding agents spend fewer tokens on planning and more on implementation.
