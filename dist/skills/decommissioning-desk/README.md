# Decommissioning Desk

`decommissioning-desk` is an SDLC skill for retiring software assets safely. It creates connector-grounded decommissioning plans, API sunset plans, cutover plans, data retention/archive plans, communication plans, and downstream handoff notes.

## Lifecycle coverage

This skill covers SDLC stage 25: decommissioning and end-of-life. It also touches release operations, deployment, observability, incident response, verification, and documentation traceability when retirement work needs staged rollout, monitoring, support readiness, or proof updates.

## Intended inputs

- Feature, API, service, repository, job, dependency, flag, environment, integration, data store, or documentation surface to retire.
- GitHub repository context, code references, owners, issues, PRs, tests, and release history.
- Usage data, logs, metrics, dashboards, or incident context when available.
- Product docs, API docs, runbooks, support commitments, retention policies, and roadmap decisions.
- User-provided constraints such as target sunset date, customer impact, compliance requirements, or rollback window.

## Intended outputs

- Decommission plan.
- API sunset plan.
- Migration/cutover plan.
- Data retention/archive plan.
- Stakeholder communication plan.
- Risk and rollback checklist.
- Verification gates and downstream handoff notes.

## Required connectors

- GitHub for code, issues, PRs, branches, release history, deployment config, tests, and ownership clues.
- Documentation sources or uploaded docs for API promises, runbooks, policy, roadmap, migration instructions, and retention rules.
- Observability/incident sources when usage, health, traffic, logs, or production risk matter.
- Issue/project sources when milestones, customer commitments, labels, blockers, or owners affect sequencing.

## Composition

Use `implementation-handoff-desk` after this skill when the plan must become an implementation PR prompt. Use `deployment-desk` for rollout/cutover gates, `release-operations-desk` for release and rollback packaging, `verification-desk` for proof of retirement, and `docs-traceability-desk` for docs and proof-map cleanup.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
