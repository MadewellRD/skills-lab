# Connector Routing

## GitHub

Required when deployment depends on repository state, including workflow files, deploy scripts, infrastructure code, release branches, tags, commits, PRs, checks, environments, or rollback code.

Retrieve:

- repo and default branch
- relevant PRs, commits, branches, or tags
- deployment workflows and scripts
- CI/check status
- changed files affecting deployment
- infrastructure and configuration files

## Issue/project tracker

Required when deployment scope, blockers, owners, or rollout tasks are tracked in issues, milestones, or project boards.

Retrieve:

- issue IDs and titles
- acceptance or rollout tasks
- blockers and owners
- priority and target milestone
- linked PRs

## Document sources

Required when deployment depends on runbooks, release policy, architecture, environment maps, operational procedures, or change-management standards.

Retrieve:

- release and deployment runbooks
- environment documentation
- rollback procedures
- monitoring requirements
- customer communication plans

## Communication sources

Required when approvals, launch timing, incident cautions, or stakeholder decisions are only present in messages.

Retrieve only decision-bearing messages. Treat messages as decision context, not repo truth.

## Observability sources

Use when dashboards, SLOs, alerts, metrics, logs, or incident signals affect go/no-go or post-deploy verification.

If observability data is unavailable, say which monitoring checks are assumed or missing.
