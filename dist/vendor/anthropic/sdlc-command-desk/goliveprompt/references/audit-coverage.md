# Audit Coverage

Phase 3 requires every suite. "Every suite" means the lists below, not a judgment call made in the moment. Enumerating them is what keeps the gate honest.

## Core SDLC suites

Run all of these on every project:

| Suite | Purpose at this gate |
|---|---|
| product-requirements-desk | requirements exist, are accepted, and match what is built |
| technical-discovery-desk | feasibility, unknowns, dependency and integration risk |
| architecture-design-desk | component boundaries, interface contracts, decision records |
| issue-planning-desk | scope decomposition, sequencing, dependency graph |
| implementation-handoff-desk | whether scoped work is actually ready for a coding agent |
| review-quality-desk | diff risk, scope creep, quality gates |
| test-strategy-desk | coverage gaps, regression scope, fixture plan |
| verification-desk | requirements traceability, acceptance gates, release blockers |
| security-threat-desk | trust boundaries, authn and authz, secrets, dependency exposure |
| ci-failure-desk | pipeline health, flaky tests, red checks |
| release-operations-desk | release readiness, versioning, rollback plan |
| deployment-desk | rollout gates, feature flags, post-deploy verification |
| observability-readiness-desk | logging, metrics, traces, dashboards, alerts, SLOs |
| incident-response-desk | severity model, triage path, runbooks |
| maintenance-refactor-desk | technical debt, dependency upgrades, dead code |
| retrospective-desk | cycle metrics, process gaps, action items |
| decommissioning-desk | anything being retired, sunset, or migrated off |
| docs-traceability-desk | doc to code consistency, unsupported claims, proof map |

## Web suites

Add these when the project has a browser-facing surface. Anything serving HTML, a SPA, a dashboard, an admin UI, a portal, or a docs site qualifies:

| Suite | Purpose at this gate |
|---|---|
| web-development-command-desk | orchestrates the web suites end to end |
| site-product-requirements-desk | page and route scope, journeys, success metrics |
| information-architecture-desk | sitemap, routes, navigation, url taxonomy |
| ux-ui-design-system-desk | component inventory, tokens, interaction states |
| frontend-engineering-desk | rendering strategy, routing, state, data fetching |
| backend-integration-desk | api contracts, auth, sessions, caching, failure modes |
| cms-content-operations-desk | content models, editorial workflow, publishing rules |
| web-security-secops-desk | csp, headers, cors, csrf, cookies, third-party scripts |
| web-performance-desk | core web vitals, budgets, bundle size, caching |
| accessibility-seo-desk | wcag, semantics, keyboard, metadata, structured data |
| web-testing-qa-desk | cross browser, responsive, visual regression, signoff |
| web-observability-desk | rum, synthetic checks, frontend errors, launch monitoring |
| web-release-deployment-desk | preview environments, promotion, cache invalidation |
| web-maintenance-growth-desk | post-launch backlog, experiments, regression follow-up |

## Coverage table

Record the result of every suite in `{SPEC_DIR}/audit-coverage.md`. One row per suite, no gaps:

```markdown
| Suite | Status | Findings | Notes |
|---|---|---|---|
```

`Status` is `run` or `N/A`. An N/A row requires a one line justification in `Notes`. A suite with zero findings is still `run`, not `N/A`; those are different claims and the difference matters when someone audits the audit.

Findings become GL backlog items with the raising suite recorded as the task source. A finding that does not produce a backlog item was summarized away, which the gate forbids.

## Re-running against existing audits

If `{SPEC_DIR}` already holds audit artifacts, do not re-run from zero. Check each suite's recorded findings against the current code, mark suites whose scope has changed since they ran, and run only those fresh. Record the verification date per suite so the next session can do the same.
