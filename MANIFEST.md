# Skills-Lab Manifest

This manifest tracks all command desk suites published in this repository.

## Repository identity

- Repository: https://github.com/MadewellRD/skills-lab
- Audience: vibe coders, solo builders, and AI-native engineering teams
- Purpose: reduce workflow ambiguity and help coding agents spend more tokens on code, tests, and validation instead of rediscovering process.

## Suite registry

| Suite | Version | Source | dist/skills | dist/packages | GitHub Release | Status |
|---|---|---|---|---|---|---|
| SDLC Command Desk | v0.2.0-rc.1 | `skills/SDLC Command Desk/` | `dist/skills/sdlc-command-desk/` | `dist/packages/sdlc-command-desk/` | Yes: `v0.2.0-rc.1`; GitHub `Latest` still points to `v0.1.1` | Published release candidate |
| Web Development Command Desk | v0.3.0 | `skills/Web Development Command Desk/` | `dist/skills/web-development-command-desk/` | `dist/packages/web-development-command-desk/` | No | Packaged; GitHub Release pending |
| AI Engineering Command Desk | v0.1.0 | `skills/AI Engineering Command Desk/` | `dist/skills/ai-engineering-command-desk/` | `dist/packages/ai-engineering-command-desk/` | No | Packaged; GitHub Release pending |
| Sales Command Desk | v0.1.0 | `skills/Sales Command Desk/` | `dist/skills/sales-command-desk/` | `dist/packages/sales-command-desk/` | No | Packaged; GitHub Release pending |
| Product Command Desk | v0.1.0 | `skills/Product Command Desk/` | `dist/skills/product-command-desk/` | `dist/packages/product-command-desk/` | No | Packaged; GitHub Release pending |
| Sales Revenue Command Desk | v0.1.0 | `skills/Sales Revenue Command Desk/` | (merged into `sales-command-desk`) | (merged into `sales-command-desk`) | No | Source preserved; superseded by Sales Command Desk |

## Package naming convention

Repository-facing archives use ordered descriptive names:

```text
000-sdlc-command-desk-skill.zip
001-product-requirements-desk-skill.zip
```

Upload-facing archives may be renamed to `skill.zip` when uploading through ChatGPT.

---

## SDLC Command Desk — v0.2.0-rc.1 continuity-kernel

19 desks. Continuity kernel, readiness gates, halt taxonomy, preflight cache, Codex conservation policy applied across all desks.

Checksums: `CHECKSUMS.txt` | Packages: `dist/packages/sdlc-command-desk/`

| Order | Skill | Role | Status |
|---:|---|---|---|
| 000 | `sdlc-command-desk` | Lifecycle orchestrator | packaged |
| 001 | `product-requirements-desk` | PRDs, requirement IDs, acceptance criteria, non-goals, risks | packaged |
| 002 | `technical-discovery-desk` | Repo recon, feasibility, constraints, unknowns, spikes | packaged |
| 003 | `architecture-design-desk` | Architecture specs, ADRs, interface contracts, migrations | packaged |
| 004 | `issue-planning-desk` | GitHub issue plans, milestones, dependency graphs | packaged |
| 005 | `implementation-handoff-desk` | Low-token coding-agent handoffs | packaged |
| 006 | `review-quality-desk` | PR review, diff risk, scope creep, missing-test assessment | packaged |
| 007 | `test-strategy-desk` | QA scenarios, regression plans, fixture plans | packaged |
| 008 | `verification-desk` | V&V reports, RTMs, acceptance gates, evidence maps | packaged |
| 009 | `docs-traceability-desk` | Proof maps, claim maps, doc-code consistency | packaged |
| 010 | `security-threat-desk` | Threat models, trust boundaries, dependency review | packaged |
| 011 | `ci-failure-desk` | CI failure triage, flaky-test classification, root-cause | packaged |
| 012 | `release-operations-desk` | Release readiness, notes, version/tag plan, rollback | packaged |
| 013 | `deployment-desk` | Deployment planning, rollout stages, feature flags | packaged |
| 014 | `observability-readiness-desk` | Telemetry design, logs/metrics/traces, SLOs, alerts | packaged |
| 015 | `incident-response-desk` | Incident triage, severity, RCA, hotfix handoff | packaged |
| 016 | `maintenance-refactor-desk` | Refactors, dependency upgrades, migrations, dead-code | packaged |
| 017 | `retrospective-desk` | Retrospectives, cycle metrics, process improvements | packaged |
| 018 | `decommissioning-desk` | Feature/API/system retirement, cutover, data retention | packaged |

---

## Web Development Command Desk — v0.3.0

14 desks. Covers full web delivery from product intent through launch, operations, maintenance, and growth.

Checksums: `dist/manifests/web-development-command-desk-CHECKSUMS.txt` | Packages: `dist/packages/web-development-command-desk/`

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

---

## AI Engineering Command Desk — v0.1.0

18 desks. Model selection, prompt systems, tool schemas, agent architecture, retrieval/RAG, evals, datasets, fine-tuning, safety, red-team, inference ops, observability, cost/latency, release readiness, and AI incident response.

Checksums: `dist/manifests/ai-engineering-command-desk-CHECKSUMS.txt` | Packages: `dist/packages/ai-engineering-command-desk/`

| Order | Skill | Status |
|---:|---|---|
| 000 | `ai-engineering-command-desk` | packaged |
| 001 | `agent-architecture-desk` | packaged |
| 002 | `agent-observability-desk` | packaged |
| 003 | `ai-incident-response-desk` | packaged |
| 004 | `ai-release-readiness-desk` | packaged |
| 005 | `ai-safety-review-desk` | packaged |
| 006 | `cost-latency-optimization-desk` | packaged |
| 007 | `dataset-curation-desk` | packaged |
| 008 | `eval-design-desk` | packaged |
| 009 | `eval-run-analysis-desk` | packaged |
| 010 | `fine-tuning-desk` | packaged |
| 011 | `inference-ops-desk` | packaged |
| 012 | `model-selection-desk` | packaged |
| 013 | `prompt-systems-desk` | packaged |
| 014 | `red-team-eval-desk` | packaged |
| 015 | `retrieval-rag-design-desk` | packaged |
| 016 | `synthetic-data-desk` | packaged |
| 017 | `tool-schema-design-desk` | packaged |

---

## Sales Command Desk — v0.1.0

13 desks. One orchestrator and twelve specialist sub-desks for the full revenue motion.

Checksums: `CHECKSUMS-sales-command-desk-v0.1.0.txt` | Packages: `dist/packages/sales-command-desk/`

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

---

## Product Command Desk — v0.1.0

16 desks. Covers the full product lifecycle: market discovery through launch, experimentation, feedback, and retrospective.

Checksums: `CHECKSUMS-product-command-desk-v0.1.0.txt` | Packages: `dist/packages/product-command-desk/`

| Order | Skill | Status |
|---:|---|---|
| 000 | `product-command-desk` | packaged |
| 001 | `market-discovery-desk` | packaged |
| 002 | `user-research-desk` | packaged |
| 003 | `persona-segmentation-desk` | packaged |
| 004 | `opportunity-sizing-desk` | packaged |
| 005 | `competitive-analysis-desk` | packaged |
| 006 | `prd-desk` | packaged |
| 007 | `roadmap-planning-desk` | packaged |
| 008 | `feature-prioritization-desk` | packaged |
| 009 | `pricing-packaging-desk` | packaged |
| 010 | `gtm-brief-desk` | packaged |
| 011 | `launch-readiness-desk` | packaged |
| 012 | `experiment-design-desk` | packaged |
| 013 | `feedback-synthesis-desk` | packaged |
| 014 | `churn-retention-analysis-desk` | packaged |
| 015 | `product-retrospective-desk` | packaged |

---

## Operating rules

Every skill in every suite preserves these principles:

1. Keep the user creative and avoid unnecessary process friction.
2. Use connector-grounded facts when available.
3. Treat GitHub as source of truth for repository state.
4. Halt or produce diagnostics instead of inventing missing facts.
5. Produce reusable Markdown artifacts for plans, prompts, reports, checklists, and handoffs.
6. Use `implementation-handoff-desk` only after upstream ambiguity has been reduced.
7. Prefer compact, code-heavy execution handoffs so coding agents spend fewer tokens on planning and more on implementation.

## Planned suites (source scaffold only)

The following suites have `skills/` directories with README stubs. No dist content yet.

Cloud Infrastructure Command Desk, Customer Success Command Desk, Customer Support Command Desk, Data Command Desk, Finance Accounting Command Desk, FinOps Command Desk, GRC Command Desk, Knowledge Ops Command Desk, Legal Contracts Command Desk, Marketing Growth Command Desk, People Talent Command Desk, Platform Engineering Command Desk, Privacy Data Protection Command Desk, Procurement Vendor Management Command Desk, Research Command Desk, Sales Revenue Command Desk (source preserved), Security Command Desk, SRE Reliability Command Desk.
