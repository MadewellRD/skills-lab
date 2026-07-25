# Child Skill Routing

## Built suite route table

| User asks for | Route to | Supporting desks |
|---|---|---|
| turn idea into requirements | product-requirements-desk | docs-traceability-desk if sources must be mapped |
| assess feasibility or repo fit | technical-discovery-desk | security-threat-desk for risk-heavy areas |
| design solution or architecture | architecture-design-desk | technical-discovery-desk, security-threat-desk |
| break work into issues | issue-planning-desk | product-requirements-desk, architecture-design-desk |
| create coding-agent prompt or branch/PR handoff | implementation-handoff-desk | issue-planning-desk, test-strategy-desk |
| review a PR | review-quality-desk | test-strategy-desk, security-threat-desk |
| plan tests or regression coverage | test-strategy-desk | verification-desk |
| prove acceptance or trace requirements | verification-desk | docs-traceability-desk |
| map docs to source facts | docs-traceability-desk | verification-desk |
| threat model or security review | security-threat-desk | architecture-design-desk |
| diagnose CI or build failure | ci-failure-desk | test-strategy-desk, implementation-handoff-desk |
| prepare release | release-operations-desk | verification-desk, ci-failure-desk |
| deploy or roll out | deployment-desk | release-operations-desk, observability-readiness-desk |
| prepare monitoring or runbooks | observability-readiness-desk | deployment-desk |
| respond to production incident | incident-response-desk | ci-failure-desk, implementation-handoff-desk |
| refactor or upgrade dependencies | maintenance-refactor-desk | test-strategy-desk, implementation-handoff-desk |
| run retrospective | retrospective-desk | docs-traceability-desk |
| retire feature/api/system | decommissioning-desk | deployment-desk, docs-traceability-desk |

## Implementation readiness test

Route to `implementation-handoff-desk` only when at least one is true:

- There is an accepted GitHub issue with acceptance criteria.
- A prior desk artifact explicitly says implementation is ready.
- The user provides complete scope, repo, target branch/base, allowed files, validation commands, and halt conditions.

Otherwise route to the earliest missing upstream desk.


## Continuity rule

This table is an execution map, not a user-facing stopping point. When the next desk can be executed from available context, continue using that desk contract or skill. Do not return only a next-desk recommendation. Stop only with `Workflow Halt` when a required fact, connector, or approval is missing.
