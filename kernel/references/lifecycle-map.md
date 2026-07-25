# Lifecycle Map

Use this map to locate the current stage before choosing a child desk.

| Stage | Lifecycle area | Primary desk | Typical artifacts |
|---:|---|---|---|
| 0 | Strategy, portfolio, initiative intake | portfolio-intake-desk | initiative brief, prioritization, proceed/defer recommendation |
| 1 | Opportunity discovery and problem framing | opportunity-discovery-desk | problem statement, opportunity hypothesis, research questions |
| 2 | Stakeholder, user, and market research | research-synthesis-desk | stakeholder map, personas, insights, competitive scan |
| 3 | Product requirements | product-requirements-desk | PRD, requirement IDs, acceptance criteria, non-goals |
| 4 | System and software requirements | software-requirements-desk | SRS, functional/non-functional requirements, constraints |
| 5 | Technical discovery and feasibility | technical-discovery-desk | technical discovery memo, risk register, spike plan |
| 6 | Architecture and solution design | architecture-design-desk | SDS, ADRs, component boundaries, migration plan |
| 7 | UX, UI, interaction, and content design | ux-design-desk | user flows, screen specs, accessibility notes |
| 8 | Data, API, and integration contracts | api-contract-desk | API spec, schema spec, integration plan |
| 9 | Security, privacy, and threat modeling | security-threat-desk | threat model, trust boundaries, mitigation plan |
| 10 | Planning, decomposition, issue generation | issue-planning-desk | issue plan, dependency graph, milestones, labels |
| 11 | Repository setup and environment | repo-setup-desk | bootstrap commands, environment checklist, repo setup plan |
| 12 | Implementation handoff, branch, and PR operations | implementation-handoff-desk | coding-agent prompt, branch plan, PR body, halt-resume prompt |
| 13 | Code review and change quality | review-quality-desk | review report, risk findings, change request comments |
| 14 | Test planning and QA strategy | test-strategy-desk | QA scenarios, regression plan, coverage gap report |
| 15 | Verification, validation, and traceability | verification-desk | V&V report, RTM, acceptance-gate evidence |
| 16 | CI/CD, build, and pipeline health | ci-failure-desk | CI diagnosis, flake classification, rerun/fix policy |
| 17 | Release planning and release operations | release-operations-desk | release runbook, notes, rollback plan |
| 18 | Deployment, rollout, and change management | deployment-desk | rollout plan, feature-flag plan, go/no-go checklist |
| 19 | Observability and operational readiness | observability-readiness-desk | telemetry plan, SLO notes, runbook, alert checks |
| 20 | Incident response and production support | incident-response-desk | incident triage, RCA, hotfix handoff, follow-up issues |
| 21 | Maintenance, refactoring, dependency management | maintenance-refactor-desk | refactor plan, upgrade plan, migration sequence |
| 22 | Documentation and proof maps | docs-traceability-desk | proof map, claim map, doc-code drift report |
| 23 | Compliance, audit, governance evidence | compliance-evidence-desk | audit packet, control mapping, risk log |
| 24 | Retrospective and continuous improvement | retrospective-desk | retro report, cycle metrics, improvement plan |
| 25 | Decommissioning and end-of-life | decommissioning-desk | decommission plan, cutover plan, retention plan |

The current built suite includes the core desks from product requirements through decommissioning plus the renamed `implementation-handoff-desk`. If a listed early-stage or narrow sub-desk is not installed, route to the closest available parent desk and state the substitution.
