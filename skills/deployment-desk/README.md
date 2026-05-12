# Deployment Desk

`deployment-desk` creates connector-grounded deployment plans, rollout plans, change-management artifacts, go/no-go reviews, and post-deploy verification checklists.

## Lifecycle coverage

Primary SDLC stages:

- Deployment, rollout, and change management
- Release-to-deploy handoff
- Post-deploy verification
- Feature-flag and staged rollout control

Adjacent stages:

- Release operations
- CI/CD and pipeline health
- Verification and validation
- Observability readiness
- Incident response

## Intended inputs

- Release notes, release runbooks, changelogs, version/tag plans, and release readiness reports
- GitHub PRs, commits, branches, deployment workflows, infrastructure config, and CI/deploy checks
- Feature-flag plans, target environments, rollout cohorts, maintenance windows, and go/no-go constraints
- Verification evidence, test results, QA signoff, security notes, and unresolved blockers
- Monitoring requirements, SLOs, dashboards, alert plans, and post-deploy health checks

## Intended outputs

- Deployment plan
- Staged rollout plan
- Feature-flag plan
- Change-management artifact
- Go/no-go review
- Post-deploy verification checklist
- Rollback and monitoring handoff notes
- Downstream handoff notes for `implementation-handoff-desk`, `release-operations-desk`, `observability-readiness-desk`, `ci-failure-desk`, and `incident-response-desk`

## Required connectors

Use GitHub when deployment depends on repository truth: workflows, deployment scripts, environments, commits, PRs, checks, or infrastructure config. Use docs connectors when deployment depends on release runbooks, policies, architecture, environment maps, or operational procedures. Use issue/project connectors when deployment work is tracked in tickets or milestones. Use communication connectors when approvals, timing, or stakeholder decisions are not in documents.

## Safety rule

Do not invent deployment commands, environment names, rollback procedures, approvals, owners, feature flags, or monitoring checkpoints. If they cannot be verified, mark them as assumptions or produce a deployment diagnostic.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
