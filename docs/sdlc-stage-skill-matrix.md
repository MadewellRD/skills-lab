# SDLC Stage and Skill Matrix

Status: planning artifact
Decision: do not create any new skills until this matrix is reviewed and accepted.

## Purpose

This document defines the full software development lifecycle coverage map for the Skills Lab project. The goal is to identify every lifecycle stage, assign one or more candidate skills to each stage, and establish the order in which those skills should later be built. `pr-command-desk` is the completed anchor skill and will later be used to wrap the implementation into one large Sprint.

## Evidence base

Initial seed sources:

- `MadewellRD/skills-lab/docs/sdlc-skills-research-map.md` — local project research map and operating principles.
- `Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC` — public repo explicitly containing prompts, skills, hooks, agents, and docs for an SDLC workflow.
- `kcenon/claude_code_agent` — AD-SDLC source describing greenfield, enhancement, and GitHub issue import pipelines, plus 35 specialized agents across the lifecycle.
- `VoltAgent/awesome-agent-skills` — curated index of public agent skills from official teams and community sources.
- Additional public GitHub searches for PRD, code-review, threat-modeling, security, CI/CD, validation, and lifecycle-specific skills.

## Naming convention

Use `*-desk` for control-plane skills. A desk is responsible for intake, connector grounding, source hierarchy, artifact production, halt conditions, and handoff packaging.

Use `*-advisor`, `*-auditor`, or `*-generator` only when the skill is narrow and should not own a full lifecycle stage.

## Global rules for every SDLC skill

Every skill in this suite must:

1. Use connector preflight before producing operational output.
2. Treat GitHub as source of truth for repo files, commits, branches, PRs, issues, and checks.
3. Treat docs/connectors as source of truth for product, policy, roadmap, audit, and decision context.
4. Include a source hierarchy and conflict-resolution rule.
5. Emit downloadable Markdown artifacts for prompts, runbooks, reports, plans, and checklists.
6. Include evidence blocks or a companion provenance file.
7. Halt instead of inventing repo state, issue IDs, test names, CI status, branch names, or source facts.
8. Separate analysis artifacts from execution handoff artifacts.
9. Prefer small, auditable handoffs over vague broad instructions.
10. Preserve `pr-command-desk` as the implementation and PR handoff layer.

## Complete lifecycle stage map

### 0. Strategy, portfolio, and initiative intake

Purpose: decide whether a workstream should exist and where it fits.

Candidate skills:

- `portfolio-intake-desk`
- `initiative-ranking-desk`
- `business-case-desk`

Outputs:

- Initiative brief
- Strategic fit memo
- Prioritization matrix
- Funding/resource assumptions
- Kill/defer/proceed recommendation

Connector grounding:

- Roadmap docs
- Strategy docs
- GitHub milestones/projects
- Customer/request sources when available

### 1. Opportunity discovery and problem framing

Purpose: define the problem before defining the solution.

Candidate skills:

- `opportunity-discovery-desk`
- `problem-framing-desk`
- `customer-signal-desk`

Outputs:

- Problem statement
- User/customer segment summary
- Current pain points
- Opportunity hypothesis
- Research questions

Connector grounding:

- Customer notes
- Issues and support tickets
- Product docs
- Analytics summaries

### 2. Stakeholder, user, and market research

Purpose: gather evidence and identify who the system serves.

Candidate skills:

- `research-synthesis-desk`
- `stakeholder-map-desk`
- `competitive-research-desk`

Outputs:

- Stakeholder map
- Persona summary
- Jobs-to-be-done notes
- Competitive scan
- Evidence-backed insight report

Connector grounding:

- Docs, interviews, customer notes, public research, GitHub issues when product-facing

### 3. Product requirements

Purpose: convert intent and evidence into product requirements.

Candidate skills:

- `product-requirements-desk`
- `acceptance-criteria-desk`
- `prd-review-desk`

Outputs:

- PRD
- Requirement IDs
- Acceptance criteria
- Non-goals
- Open questions
- Release/defer boundaries

Connector grounding:

- Product docs
- Roadmap docs
- Issues
- Stakeholder decisions

### 4. System and software requirements

Purpose: convert product requirements into explicit system requirements.

Candidate skills:

- `software-requirements-desk`
- `requirements-normalization-desk`
- `requirements-traceability-desk`

Outputs:

- SRS
- Functional requirements
- Non-functional requirements
- Constraints
- Requirement-to-source traceability seeds

Connector grounding:

- PRD
- Repo docs
- Architecture docs
- Existing specs

### 5. Technical discovery and feasibility

Purpose: establish what is unknown, risky, or technically constrained.

Candidate skills:

- `technical-discovery-desk`
- `spike-planning-desk`
- `repo-recon-desk`
- `dependency-research-desk`

Outputs:

- Technical discovery memo
- Feasibility assessment
- Spike plan
- Risk register
- Unknowns and assumptions

Connector grounding:

- GitHub code search
- README/docs
- Dependency manifests
- Public API docs
- Prior PRs/issues

### 6. Architecture and solution design

Purpose: define the system design before implementation.

Candidate skills:

- `architecture-design-desk`
- `adr-desk`
- `interface-contract-desk`
- `migration-design-desk`

Outputs:

- SDS / design spec
- ADRs
- Component boundaries
- API contracts
- Data-flow diagrams
- Migration plan

Connector grounding:

- Repo topology
- Existing architecture docs
- PRD/SRS
- Code ownership and module boundaries

### 7. UX, UI, interaction, and content design

Purpose: design user-facing behavior and content before build.

Candidate skills:

- `ux-design-desk`
- `ui-spec-desk`
- `design-system-desk`
- `content-design-desk`

Outputs:

- UX brief
- User flows
- Screen specs
- Design-system mapping
- Copy/content requirements
- Accessibility notes

Connector grounding:

- Design docs
- Figma links when available
- Existing UI code
- Brand/design-system docs

### 8. Data, API, and integration contract design

Purpose: make data and integration contracts explicit.

Candidate skills:

- `api-contract-desk`
- `data-modeling-desk`
- `integration-design-desk`
- `schema-change-desk`

Outputs:

- API spec
- Schema spec
- Backward compatibility notes
- Migration notes
- Integration test plan

Connector grounding:

- API docs
- Database schemas
- OpenAPI/GraphQL/protobuf files
- Existing integration tests

### 9. Security, privacy, and threat modeling

Purpose: identify and mitigate abuse, privacy, and security risks before code lands.

Candidate skills:

- `security-threat-desk`
- `privacy-risk-desk`
- `secrets-boundary-desk`
- `dependency-security-desk`

Outputs:

- Threat model
- STRIDE/DREAD-style risk matrix where applicable
- Trust boundaries
- Security requirements
- Privacy/data handling notes
- Dependency and secrets review checklist

Connector grounding:

- Architecture spec
- Auth/authz code
- Dependency manifests
- Secret scanning results
- Compliance docs

### 10. Planning, decomposition, and issue generation

Purpose: turn design into sequenced work.

Candidate skills:

- `issue-planning-desk`
- `milestone-planning-desk`
- `dependency-graph-desk`
- `sprint-scope-desk`

Outputs:

- GitHub issues
- Milestone plan
- Dependency graph
- Labels/components
- Sprint sequence
- Acceptance gates per issue

Connector grounding:

- GitHub issues/projects/milestones
- PRD/SRS/SDS
- Roadmap docs
- Existing issue labels

### 11. Repository setup, environment, and scaffolding

Purpose: ensure build substrate exists before implementation.

Candidate skills:

- `repo-setup-desk`
- `environment-bootstrap-desk`
- `scaffold-desk`
- `devcontainer-desk`

Outputs:

- Repo setup plan
- Environment checklist
- Bootstrap commands
- Branching/worktree policy
- Local verification commands

Connector grounding:

- GitHub repo settings
- Build files
- README/dev docs
- CI config

### 12. Implementation handoff, branch, and PR operations

Purpose: convert scoped work into executable coding-agent instructions.

Candidate skills:

- `pr-command-desk` — completed anchor
- `branch-hygiene-desk`
- `merge-train-desk`
- `halt-resume-desk` if later split out; otherwise keep inside `pr-command-desk`

Outputs:

- Grounded PR prompt
- Halt resume prompt
- Merge-train runbook
- Repo cleanup prompt
- Connector diagnostic
- PR body/title instructions

Connector grounding:

- GitHub commits, branches, PRs, issues, files, checks
- Docs and decision sources

### 13. Code review and change quality

Purpose: evaluate changes before merge.

Candidate skills:

- `review-quality-desk`
- `diff-risk-desk`
- `maintainer-review-desk`
- `review-comment-desk`

Outputs:

- Review decision: approve/comment/request changes
- Risk-tagged findings
- Inline comment plan
- Missing-test assessment
- Scope creep detection

Connector grounding:

- PR diff
- Changed files
- Tests/checks
- CODEOWNERS or ownership docs
- Prior review comments

### 14. Test planning and QA strategy

Purpose: define what must be tested and how.

Candidate skills:

- `test-strategy-desk`
- `qa-scenario-desk`
- `regression-planning-desk`
- `fixture-design-desk`

Outputs:

- Test strategy
- Scenario matrix
- Regression plan
- Fixture plan
- Coverage-gap report

Connector grounding:

- Requirements
- Existing test tree
- CI results
- Bug reports
- Prior regressions

### 15. Verification, validation, and traceability

Purpose: prove implemented work satisfies requirements.

Candidate skills:

- `verification-desk`
- `validation-desk`
- `rtm-desk`
- `acceptance-gate-desk`

Outputs:

- V&V report
- Requirements traceability matrix
- Acceptance-gate checklist
- Evidence map
- Release-blocker list

Connector grounding:

- PRD/SRS/SDS
- Test results
- GitHub PRs/commits
- CI artifacts
- Manual QA evidence

### 16. CI/CD, build, and pipeline health

Purpose: keep automation trustworthy and fast.

Candidate skills:

- `ci-failure-desk`
- `pipeline-health-desk`
- `build-system-desk`
- `flake-triage-desk`

Outputs:

- CI failure diagnosis
- Flake classification
- Minimal repro or rerun decision
- Pipeline improvement plan
- Build gate checklist

Connector grounding:

- GitHub Actions runs/jobs/logs
- Commit status checks
- Build scripts
- Test output

### 17. Release planning and release operations

Purpose: safely ship a verified change.

Candidate skills:

- `release-operations-desk`
- `release-notes-desk`
- `rollback-plan-desk`
- `versioning-desk`

Outputs:

- Release runbook
- Release notes
- Rollback plan
- Version/tag plan
- Pre/post-release checks

Connector grounding:

- Merged PRs
- Changelog
- CI artifacts
- Deployment config
- Release history

### 18. Deployment, rollout, and change management

Purpose: deploy safely and control blast radius.

Candidate skills:

- `deployment-desk`
- `rollout-control-desk`
- `feature-flag-desk`
- `change-management-desk`

Outputs:

- Deployment plan
- Rollout stages
- Feature-flag plan
- Monitoring checkpoints
- Go/no-go criteria

Connector grounding:

- Deployment configs
- Infrastructure docs
- Feature flag config
- Release runbooks
- Observability dashboards if available

### 19. Observability, telemetry, and operational readiness

Purpose: ensure the system can be monitored and diagnosed.

Candidate skills:

- `observability-readiness-desk`
- `telemetry-design-desk`
- `runbook-desk`
- `slo-desk`

Outputs:

- Observability plan
- Metrics/logs/traces checklist
- Runbook
- SLO/SLA notes
- Alerting recommendations

Connector grounding:

- Monitoring docs
- Logging/tracing code
- Incident docs
- Deployment topology

### 20. Incident response, bug triage, and production support

Purpose: handle production failures and regressions.

Candidate skills:

- `incident-response-desk`
- `bug-triage-desk`
- `root-cause-analysis-desk`
- `hotfix-command-desk`

Outputs:

- Incident summary
- RCA
- Severity classification
- Hotfix PR prompt
- Follow-up issue plan

Connector grounding:

- Incident reports
- GitHub issues/PRs
- Logs/metrics/traces
- Recent deploys

### 21. Maintenance, refactoring, and dependency management

Purpose: improve system health without uncontrolled scope expansion.

Candidate skills:

- `maintenance-refactor-desk`
- `dependency-upgrade-desk`
- `dead-code-desk`
- `migration-command-desk`

Outputs:

- Refactor plan
- Dependency upgrade plan
- Migration sequence
- Risk controls
- Regression checklist

Connector grounding:

- Dependency files
- Static analysis output
- Test coverage
- Code ownership
- Prior PRs/issues

### 22. Documentation, knowledge management, and proof maps

Purpose: make project truth durable and inspectable.

Candidate skills:

- `docs-traceability-desk`
- `proof-map-desk`
- `knowledge-index-desk`
- `doc-code-consistency-desk`

Outputs:

- Docs update prompt
- Proof map
- Claim map
- Knowledge index
- Doc-code drift report

Connector grounding:

- Docs tree
- GitHub source files
- Test names
- Status docs
- Design/roadmap docs

### 23. Compliance, audit, and governance evidence

Purpose: show that process, policy, and controls were followed.

Candidate skills:

- `compliance-evidence-desk`
- `audit-readiness-desk`
- `control-mapping-desk`
- `risk-register-desk`

Outputs:

- Audit evidence packet
- Control mapping
- Risk register updates
- Policy exception log
- Compliance checklist

Connector grounding:

- Compliance docs
- PR history
- Review records
- Test/CI evidence
- Release approvals

### 24. Retrospective and continuous improvement

Purpose: learn from completed work and improve future cycles.

Candidate skills:

- `retrospective-desk`
- `process-improvement-desk`
- `cycle-metrics-desk`

Outputs:

- Retro report
- What worked / what failed
- Process changes
- Future skill improvements
- Metrics summary

Connector grounding:

- PR timeline
- Issues
- CI history
- Incident data
- Team notes

### 25. Decommissioning and end-of-life

Purpose: safely retire systems, features, APIs, or dependencies.

Candidate skills:

- `decommissioning-desk`
- `api-sunset-desk`
- `data-retention-desk`
- `migration-cutover-desk`

Outputs:

- Decommission plan
- Migration/cutover plan
- Data retention checklist
- Customer/internal communication plan
- Rollback and archive rules

Connector grounding:

- Usage data
- API consumers
- Docs
- Deployment config
- Compliance/data-retention policy

## Recommended build order

Do not build all skills simultaneously. Build in dependency order.

### Sprint A — Lifecycle foundation

1. `product-requirements-desk`
2. `technical-discovery-desk`
3. `architecture-design-desk`
4. `issue-planning-desk`

### Sprint B — Existing implementation lane

5. `review-quality-desk`
6. `test-strategy-desk`
7. `verification-desk`
8. `docs-traceability-desk`

### Sprint C — Security and delivery lane

9. `security-threat-desk`
10. `ci-failure-desk`
11. `release-operations-desk`
12. `deployment-desk`

### Sprint D — Operations and lifecycle hardening

13. `observability-readiness-desk`
14. `incident-response-desk`
15. `maintenance-refactor-desk`
16. `retrospective-desk`
17. `decommissioning-desk`

## Minimum viable suite

The minimum viable SDLC suite after `pr-command-desk` is:

1. `product-requirements-desk`
2. `technical-discovery-desk`
3. `architecture-design-desk`
4. `issue-planning-desk`
5. `review-quality-desk`
6. `verification-desk`
7. `release-operations-desk`
8. `docs-traceability-desk`
9. `security-threat-desk`
10. `ci-failure-desk`

## Later consolidation question

After the full stage map is accepted, use `pr-command-desk` to generate one large Sprint prompt that creates the initial suite skeletons, shared connector-policy references, shared output templates, validation scripts, and documentation index.

No individual skill should be created before that Sprint plan is generated and reviewed.
