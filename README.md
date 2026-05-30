# Skills-Lab

![Skills-Lab hero](assets/skills-lab-hero.svg)
[![SDLC Command Desk](https://img.shields.io/badge/SDLC%20Command%20Desk-v0.2.0-green.svg)](releases/v0.2.0-rc.1.md)
[![Web Development Command Desk](https://img.shields.io/badge/Web%20Dev%20Command%20Desk-v0.3.0-green.svg)](releases/v0.3.0-web-development-command-desk.md)
[![AI Engineering Command Desk](https://img.shields.io/badge/AI%20Engineering%20Command%20Desk-v0.1.0-blue.svg)](dist/manifests/ai-engineering-command-desk-manifest.json)
[![Sales Revenue Command Desk](https://img.shields.io/badge/Sales%20Revenue%20Command%20Desk-v0.1.0-blue.svg)](releases/sales-command-desk-v0.1.0.md)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
Think in chat. Execute in the CLI. Ship like you already know the process.


Skills-Lab is a public lab for building and sharing **Desk Suites** — ChatGPT skill systems that let vibe coders, non-developers, solo builders, and AI-native teams walk professional workflows without needing to already know the process.

The goal is direct: give builders a guided path through any domain — software delivery, web development, AI engineering, sales — while producing the kind of output expected from an experienced team. Chat does the reasoning. The CLI does the execution. Coding agents receive constrained, source-grounded work instead of open-ended intent.

## Quick links

- [Install and use](docs/INSTALL.md) — how to install a Desk Suite in ChatGPT.
- [Manifest](MANIFEST.md) — all published suites with versions and status.
- [Checksums](CHECKSUMS.txt) — SHA256 hashes for SDLC Command Desk release artifacts.
- [Release guide](releases/README.md) — artifact policy, checksum policy, and release process.

---

## Published Desk Suites

### SDLC Command Desk — v0.2.0

End-to-end software delivery. One orchestrator, 18 lifecycle desks covering requirements through decommissioning.

- **Source:** `skills/SDLC Command Desk/`
- **Packaged:** `dist/skills/sdlc-command-desk/`
- **Release:** [v0.2.0-rc.1](releases/v0.2.0-rc.1.md) — 19 skill archives + `CHECKSUMS.txt` on GitHub Releases
- **Checksums:** `CHECKSUMS.txt`

| # | Skill | Role |
|--:|---|---|
| 000 | `sdlc-command-desk` | Orchestrator — routes lifecycle stages, enforces connector preflight, preserves workflow packets |
| 001 | `product-requirements-desk` | PRDs, requirement IDs, acceptance criteria, non-goals, risks |
| 002 | `technical-discovery-desk` | Repo recon, feasibility, constraints, unknowns, spikes, risk registers |
| 003 | `architecture-design-desk` | Architecture specs, ADRs, interface contracts, migrations |
| 004 | `issue-planning-desk` | GitHub issue plans, milestones, dependency graphs, acceptance gates |
| 005 | `implementation-handoff-desk` | Low-token coding-agent handoffs for branch, commit, PR, halt-resume, merge-train work |
| 006 | `review-quality-desk` | PR review, diff risk, scope creep, missing-test assessment |
| 007 | `test-strategy-desk` | QA scenarios, regression plans, fixture plans, coverage gaps |
| 008 | `verification-desk` | V&V reports, RTMs, acceptance gates, evidence maps, release blockers |
| 009 | `docs-traceability-desk` | Proof maps, claim maps, doc-code consistency, knowledge indexes |
| 010 | `security-threat-desk` | Threat models, trust boundaries, dependency/security reviews |
| 011 | `ci-failure-desk` | CI failure triage, flaky-test classification, rerun policy, root-cause analysis |
| 012 | `release-operations-desk` | Release readiness, notes, version/tag plan, rollback plan |
| 013 | `deployment-desk` | Deployment planning, rollout stages, feature flags, go/no-go gates |
| 014 | `observability-readiness-desk` | Telemetry design, logs/metrics/traces, SLOs, alerts, runbooks |
| 015 | `incident-response-desk` | Incident triage, severity, RCA, hotfix handoff, follow-up issues |
| 016 | `maintenance-refactor-desk` | Refactors, dependency upgrades, migrations, dead-code cleanup |
| 017 | `retrospective-desk` | Retrospectives, cycle metrics, process improvements, action plans |
| 018 | `decommissioning-desk` | Feature/API/system retirement, cutover, data retention, rollback-safe shutdown |

---

### Web Development Command Desk — v0.3.0

Full web delivery. One orchestrator, 13 specialist desks from product intent through launch, operations, and growth.

- **Source:** `skills/Web Development Command Desk/`
- **Packaged:** `dist/skills/web-development-command-desk/`
- **Archives:** `dist/packages/web-development-command-desk/`
- **Manifest:** `dist/manifests/web-development-command-desk-MANIFEST.md`
- **Checksums:** `dist/manifests/web-development-command-desk-CHECKSUMS.txt`

| # | Skill | Role |
|--:|---|---|
| 000 | `web-development-command-desk` | Orchestrator — full web workflow routing |
| 001 | `site-product-requirements-desk` | Web product requirements, user journeys, acceptance criteria |
| 002 | `information-architecture-desk` | Sitemap, navigation, routes, content structure |
| 003 | `ux-ui-design-system-desk` | Components, states, tokens, responsive patterns |
| 004 | `frontend-engineering-desk` | Rendering strategy, routing, state, data fetching, implementation handoff |
| 005 | `backend-integration-desk` | API, auth, data, BFF, caching, failure modes |
| 006 | `cms-content-operations-desk` | CMS, editorial workflow, localization, governance |
| 007 | `web-security-secops-desk` | Auth, CSP, headers, CORS, CSRF, dependency risk, abuse prevention |
| 008 | `web-performance-desk` | Core Web Vitals, budgets, caching, optimization |
| 009 | `accessibility-seo-desk` | WCAG, semantic HTML, metadata, crawlability, SEO |
| 010 | `web-testing-qa-desk` | Browser/device/responsive testing, integration, release sign-off |
| 011 | `web-observability-desk` | RUM, synthetic checks, dashboards, alerts, incident hooks |
| 012 | `web-release-deployment-desk` | CI/CD, preview, deployment, rollback, launch validation |
| 013 | `web-maintenance-growth-desk` | Post-launch iteration, experiments, content refresh, lifecycle health |

---

### AI Engineering Command Desk — v0.1.0

AI system design and operations. One orchestrator, 17 specialist desks covering the full AI engineering lifecycle.

- **Source:** `skills/AI Engineering Command Desk/`
- **Packaged:** `dist/skills/ai-engineering-command-desk/`
- **Manifest:** `dist/manifests/ai-engineering-command-desk-manifest.json`
- **Checksums:** `dist/manifests/ai-engineering-command-desk-CHECKSUMS.txt`
- **Note:** Source-only packaging pass. Zip archives and GitHub Release pending.

| # | Skill | Role |
|--:|---|---|
| 000 | `ai-engineering-command-desk` | Orchestrator — AI engineering stage routing |
| 001 | `model-selection-desk` | Model choice, routing, fallback, tradeoff evidence |
| 002 | `prompt-systems-desk` | Prompt architecture, instruction hierarchy, context assembly, test fixtures |
| 003 | `tool-schema-design-desk` | Tool/resource contracts, argument validation, permission boundaries |
| 004 | `agent-architecture-desk` | Agent loop, planning boundary, state strategy, approval gates |
| 005 | `retrieval-rag-design-desk` | Indexing, chunking, retrieval, citation, freshness, permission-filtered grounding |
| 006 | `eval-design-desk` | Eval objectives, datasets, rubrics, thresholds, slices, review protocol |
| 007 | `eval-run-analysis-desk` | Completed eval analysis, failure taxonomy, regression deltas, release implications |
| 008 | `dataset-curation-desk` | Dataset sourcing, labeling, splits, privacy, provenance, consent, retention |
| 009 | `synthetic-data-desk` | Synthetic data generation, diversity controls, contamination prevention |
| 010 | `fine-tuning-desk` | Fine-tuning justification, training data readiness, eval gates, rollout, rollback |
| 011 | `inference-ops-desk` | Production inference topology, quotas, retries, caching, secrets, SLOs |
| 012 | `agent-observability-desk` | Agent telemetry, tracing, latency, token usage, failure signals |
| 013 | `cost-latency-optimization-desk` | Cost modeling, latency profiling, batching, caching, routing optimization |
| 014 | `ai-release-readiness-desk` | AI system release gates, eval evidence, safety sign-off, rollout plan |
| 015 | `ai-incident-response-desk` | AI incident triage, severity, RCA, hotfix, monitoring, post-incident review |
| 016 | `ai-safety-review-desk` | Safety risk assessment, red-team evidence, guardrail review, harm taxonomy |
| 017 | `red-team-eval-desk` | Adversarial testing, attack surface mapping, failure injection, eval reporting |

---

### Sales Revenue Command Desk — v0.1.0

End-to-end revenue motion. One orchestrator, 12 specialist desks covering the full sales cycle.

- **Source:** `skills/Sales Revenue Command Desk/`
- **Packaged:** `dist/skills/sales-command-desk/`
- **Archives:** `dist/packages/sales-command-desk/`
- **Manifest:** `dist/manifests/sales-command-desk-v0.1.0.json`
- **Checksums:** `CHECKSUMS-sales-command-desk-v0.1.0.txt`

| # | Skill | Role |
|--:|---|---|
| 000 | `sales-command-desk` | Orchestrator — revenue workflow routing |
| 001 | `lead-research-desk` | ICP matching, prospect research, enrichment, ranking |
| 002 | `account-discovery-desk` | Account briefs, stakeholder maps, whitespace hypotheses, meeting prep |
| 003 | `outbound-sequence-desk` | Email and follow-up sequences, persona targeting, compliance controls |
| 004 | `sales-call-prep-desk` | Agendas, discovery questions, attendee context, objection watchlists |
| 005 | `qualification-desk` | MEDDICC/BANT scoring, evidence-backed gap analysis, next actions |
| 006 | `objection-handling-desk` | Grounded responses to pricing, timing, security, competitive objections |
| 007 | `proposal-desk` | Customer-facing proposals, scope documents, brand and pricing controls |
| 008 | `deal-review-desk` | Internal deal reviews, risk assessment, commercial impact, approvals |
| 009 | `crm-update-desk` | Safe CRM note, task, field, and stage updates with dry-run diffs |
| 010 | `pipeline-forecast-desk` | Forecast narratives, commit/best-case views, risk-adjusted models |
| 011 | `renewal-expansion-desk` | Renewal, upsell, cross-sell motions, churn risk, expansion hypotheses |
| 012 | `customer-handoff-desk` | Post-sale handoff packages for onboarding, CS, support, implementation |

---

## Planned Desk Suites

The following suites have source directories in `skills/` and are in active or planned authoring:

| Suite | Slug | Status |
|---|---|---|
| Cloud Infrastructure Command Desk | `cloud-infrastructure-command-desk` | Planned |
| Customer Success Command Desk | `customer-success-command-desk` | Planned |
| Customer Support Command Desk | `customer-support-command-desk` | Planned |
| Data Command Desk | `data-command-desk` | Planned |
| FinOps Command Desk | `finops-command-desk` | Planned |
| Finance & Accounting Command Desk | `finance-accounting-command-desk` | Planned |
| GRC Command Desk | `grc-command-desk` | Planned |
| Knowledge Ops Command Desk | `knowledge-ops-command-desk` | Planned |
| Legal Contracts Command Desk | `legal-contracts-command-desk` | Planned |
| Marketing & Growth Command Desk | `marketing-growth-command-desk` | Planned |
| People & Talent Command Desk | `people-talent-command-desk` | Planned |
| Platform Engineering Command Desk | `platform-engineering-command-desk` | Planned |
| Privacy & Data Protection Command Desk | `privacy-data-protection-command-desk` | Planned |
| Procurement & Vendor Management Command Desk | `procurement-vendor-management-command-desk` | Planned |
| Product Command Desk | `product-command-desk` | Planned |
| Research Command Desk | `research-command-desk` | Planned |
| Sales Command Desk | `sales-command-desk` | Planned |
| Security Command Desk | `security-command-desk` | Planned |
| SRE & Reliability Command Desk | `sre-reliability-command-desk` | Planned |

---

## How Desk Suites work

Each Desk Suite follows the same model:

```text
ChatGPT Desk Suite
  → reason through the workflow domain
  → produce source-grounded artifacts, plans, and code-ready files
  → hand off constrained work to Codex / Claude Code / CLI agent
  → CLI executes with minimal reasoning
  → results return to chat for validation and next-step planning
```

**Chat does the reasoning.** Desk Suites run planning, analysis, decomposition, source review, and quality-gate reasoning in the chat interface.

**CLI does the execution.** Coding agents receive small, explicit tasks and files — not broad product intent. The goal is constrained execution, not open-ended rediscovery.

**Halt instead of hallucinate.** Missing facts, conflicting sources, absent tests, or unverified requirements produce a halt or diagnostic — not invented certainty.

---

## Quick start

Start with a suite orchestrator when you don't know which stage applies:

```text
Use sdlc-command-desk to classify this work and walk me through the lifecycle:
I want to build a paid team workspace feature.
```

Use a specific desk when the stage is known:

```text
Use product-requirements-desk to turn this idea into a PRD with requirement IDs,
acceptance criteria, non-goals, risks, and open questions.
```

```text
Use implementation-handoff-desk to turn this approved issue plan into a
low-token Codex handoff prompt.
```

```text
Use ai-engineering-command-desk to design an evaluation strategy for this
new model deployment.
```

```text
Use sales-command-desk to prep me for my call with Acme Corp and draft
a follow-up sequence for the champion.
```

---

## Design principles

- **Zero-knowledge domain guidance** — users should not need to know what a PRD, ADR, RTM, MEDDICC score, inference SLO, or release gate is before starting.
- **Source grounding** — repo state, issues, PRs, CI, docs, CRM, and connector evidence are cited when they drive an artifact.
- **Token conservation** — every desk reduces rework and repeated reasoning for coding agents and downstream automation.
- **Nearly complete output** — each suite should provide as much implementation-ready content as possible before any CLI or external handoff.
- **Workflow continuity** — desks preserve workflow packets so sessions can pause, resume, and hand off without losing state.

---

## Repository layout

```text
assets/                         Visual assets for README and release materials.

docs/                           Research notes, lifecycle maps, install/use guides, and standards docs.

releases/                       Versioned release notes, publish scripts, and release support files.

skills/                         Human-authored source Markdown for all Desk Suite specs.
  SDLC Command Desk/            19 desk source files + references/
  Web Development Command Desk/ 14 desk source files + references/
  AI Engineering Command Desk/  18 desk source files + references/
  Sales Revenue Command Desk/   13 desk source files + references/
  ...                           23 additional planned suite directories

dist/
  skills/                       Packaged ChatGPT-compatible skill directories by suite slug.
    sdlc-command-desk/          19 skill directories (SKILL.md, agents/openai.yaml, references/)
    web-development-command-desk/ 14 skill directories
    ai-engineering-command-desk/  18 skill directories
    sales-command-desk/           13 skill directories

  packages/                     ZIP archives for GitHub Releases and direct upload.
    web-development-command-desk/ 14 zip archives
    sales-command-desk/           13 zip archives + build artifacts

  manifests/                    Generated manifests and checksums per suite.

tools/                          Validation and packaging tooling.

CHECKSUMS.txt                   SHA256 checksums for SDLC Command Desk release artifacts.
CHECKSUMS-sales-command-desk-v0.1.0.txt   SHA256 checksums for Sales Revenue Command Desk.
MANIFEST.md                     All suite versions, desk inventory, and package status.
.gitattributes                  LF line-ending enforcement for all text files.
```

---

## Releases

| Release | Suite | Status | Assets |
|---|---|---|---|
| [v0.2.0-rc.1](releases/v0.2.0-rc.1.md) | SDLC Command Desk | Released (latest) | 19 skill zips + CHECKSUMS.txt |
| [v0.3.0-web-development-command-desk](releases/v0.3.0-web-development-command-desk.md) | Web Development Command Desk | Packaged; GitHub Release pending | 14 skill zips |
| [sales-command-desk-v0.1.0](releases/sales-command-desk-v0.1.0.md) | Sales Revenue Command Desk | Packaged; GitHub Release pending | 12 skill zips |
| AI Engineering Command Desk v0.1.0 | AI Engineering Command Desk | Source-only; zips and GitHub Release pending | — |

Verify downloads before installing:

```powershell
Get-FileHash .\000-sdlc-command-desk-skill.zip -Algorithm SHA256
```

---

## From source

```bash
git clone https://github.com/MadewellRD/skills-lab.git
cd skills-lab
python3 tools/validate_sdlc_suite.py
```

---

## Community

Skills-Lab is built for builders who want AI agents to move faster without losing source truth, reviewability, or operational control.

Issues and pull requests should stay evidence-first: include repo state, affected files, validation commands, source facts, and known halt conditions.

See [MANIFEST.md](MANIFEST.md) for the full suite registry and [docs/INSTALL.md](docs/INSTALL.md) for setup instructions.
