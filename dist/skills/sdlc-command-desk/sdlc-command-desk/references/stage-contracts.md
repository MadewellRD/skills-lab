# SDLC Stage Contracts

Use these contracts when running the suite as an end-to-end workflow. They are concise substitutes for telling the user to manually invoke another skill.

## Stage order

1. product-requirements-desk
2. technical-discovery-desk
3. architecture-design-desk
4. issue-planning-desk
5. implementation-handoff-desk
6. review-quality-desk
7. test-strategy-desk
8. verification-desk
9. docs-traceability-desk
10. security-threat-desk
11. ci-failure-desk
12. release-operations-desk
13. deployment-desk
14. observability-readiness-desk
15. incident-response-desk
16. maintenance-refactor-desk
17. retrospective-desk
18. decommissioning-desk

Not every workflow must run every stage. Run the shortest safe path to the user's target outcome, but never skip a prerequisite that would force the implementation agent to invent facts.

## Contracts

### product-requirements-desk
Inputs: idea, problem, user need, product context, source notes.
Outputs: PRD, requirement IDs, acceptance criteria, non-goals, risks, open questions, workflow packet.
Continue when: requirements are clear enough for technical discovery or design.
Halt when: goals, users, acceptance criteria, or product source facts are unclear.

### technical-discovery-desk
Inputs: requirements, repo/docs context, known constraints.
Outputs: feasibility memo, repo reconnaissance, dependency notes, unknowns, risk register, workflow packet.
Continue when: enough repo and constraint context exists for design.
Halt when: repo access, target stack, dependency facts, or feasibility evidence is missing.

### architecture-design-desk
Inputs: requirements, discovery facts, repo topology, constraints.
Outputs: architecture/design spec, ADRs, interface contracts, migration plan, risk notes, workflow packet.
Continue when: design decisions are sufficient for issue planning.
Halt when: material design choices remain unresolved.

### issue-planning-desk
Inputs: requirements, design, discovery, repo constraints.
Outputs: issue plan, issue drafts, milestone/dependency order, labels, acceptance gates, workflow packet.
Continue when: implementation scope is issue-backed and bounded.
Halt when: scope cannot be split into reviewable/testable units.

### implementation-handoff-desk
Inputs: issue-backed scope, repo facts, target branch/base, allowed files, validation commands, halt conditions.
Outputs: low-token coding-agent prompt, branch/commit plan, PR body, halt-resume prompt, workflow packet.
Continue when: implementation output exists and review/test/security gates are needed.
Halt when: repo state, target branch, allowed scope, or validation commands are missing.

### review-quality-desk
Inputs: PR/diff/implementation summary, requirement IDs, tests/checks.
Outputs: review report, risk findings, missing tests, scope creep notes, change request or approval recommendation, workflow packet.
Continue when: quality risks are known and testing/verification can proceed.
Halt when: diff, PR, tests, or acceptance criteria are unavailable.

### test-strategy-desk
Inputs: requirements, risk areas, implementation summary, existing tests.
Outputs: scenario matrix, regression plan, fixture plan, coverage gap report, workflow packet.
Continue when: test expectations are concrete enough for verification.
Halt when: existing test surface or acceptance behavior is unknown.

### verification-desk
Inputs: requirements, acceptance criteria, test evidence, PR/commit evidence.
Outputs: V&V report, traceability matrix, acceptance gates, blockers, workflow packet.
Continue when: release/security/docs gates can be assessed.
Halt when: proof evidence is missing.

### docs-traceability-desk
Inputs: claims, docs, code facts, test/release evidence.
Outputs: proof map, claim map, doc-code consistency report, audit evidence, workflow packet.
Continue when: docs are aligned enough for release or follow-up issues.
Halt when: claims cannot be tied to sources.

### security-threat-desk
Inputs: architecture, changed surfaces, auth/data boundaries, dependencies.
Outputs: threat model, trust-boundary review, security findings, mitigations, workflow packet.
Continue when: security risks are accepted, mitigated, or converted into issues.
Halt when: auth/data boundaries or dependency facts are unknown.

### ci-failure-desk
Inputs: workflow run, failed job logs, commit/PR, test output.
Outputs: CI diagnostic, flake triage, rerun/fix decision, root cause, workflow packet.
Continue when: release or implementation remediation can proceed.
Halt when: logs or failing run identifiers are missing.

### release-operations-desk
Inputs: merged PRs, version/tag target, CI state, verification evidence, changelog context.
Outputs: release readiness, release notes, version/tag plan, rollback plan, workflow packet.
Continue when: deployment planning can proceed.
Halt when: release target, CI state, or rollback facts are missing.

### deployment-desk
Inputs: release artifact, target environment, rollout method, flags, verification and rollback plan.
Outputs: deployment plan, rollout gates, go/no-go, post-deploy checks, workflow packet.
Continue when: observability or incident readiness can proceed.
Halt when: environment, deploy command, flag, health check, or rollback facts are missing.

### observability-readiness-desk
Inputs: service/component, telemetry, SLO/alert/runbook needs, deployment context.
Outputs: telemetry plan, SLO/alert plan, runbook, readiness checklist, workflow packet.
Continue when: production readiness or incident support is covered.
Halt when: dashboards, metrics, logs, or ownership facts are missing.

### incident-response-desk
Inputs: incident symptoms, timeline, alerts, logs, recent deploys, impact, mitigations.
Outputs: triage, severity, RCA, hotfix handoff, follow-up issues, workflow packet.
Continue when: remediation, verification, or retrospective can proceed.
Halt when: impact, timeline, or source evidence is insufficient.

### maintenance-refactor-desk
Inputs: technical debt, dependency, refactor area, repo evidence, regression constraints.
Outputs: maintenance assessment, refactor plan, migration/dependency sequence, regression controls, workflow packet.
Continue when: implementation handoff or issue planning can proceed.
Halt when: candidate cleanup or regression safety cannot be proven.

### retrospective-desk
Inputs: sprint/release/incident/PR evidence, timeline, outcomes, metrics.
Outputs: retrospective, lessons learned, action plan, process improvement notes, workflow packet.
Continue when: follow-up requirements, issues, or maintenance work can be created.
Halt when: event evidence or outcomes are unavailable.

### decommissioning-desk
Inputs: feature/service/API to retire, consumers, usage, data retention, rollout/rollback context.
Outputs: decommission plan, API sunset, cutover plan, retention plan, communication plan, rollback risk, workflow packet.
Continue when: implementation/release/deployment/docs work is required and bounded.
Halt when: consumer, usage, retention, or rollback facts are missing.
