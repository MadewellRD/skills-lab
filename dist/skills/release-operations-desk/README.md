# Release Operations Desk

`release-operations-desk` prepares release readiness, release notes, version/tag planning, rollback planning, go/no-go, and post-release verification artifacts.

## Lifecycle coverage

Primary SDLC stage: release planning and release operations.

Adjacent stages:

- verification and validation
- CI/CD and pipeline health
- deployment and rollout
- documentation and changelog updates
- incident response and production support

## Intended inputs

- merged pull requests
- commit ranges and release branches
- issues, milestones, and labels
- CI/check evidence
- changelog or release-history docs
- deployment configuration and runbooks
- security, compliance, and verification reports
- stakeholder release decisions when available

## Intended outputs

- release readiness report
- release notes
- version and tag plan
- rollback plan
- go/no-go checklist
- post-release verification plan
- downstream handoff notes

## Required connectors

- GitHub for PRs, commits, tags, issues, releases, branches, changed files, and checks
- document sources for changelog, release policy, roadmap, compliance, and runbooks when relevant

## Optional connectors

- Slack, Teams, or email for release coordination decisions
- deployment or observability sources when available through connected tools

## Composition

Use this skill after `verification-desk` has produced enough validation evidence. Hand off to `deployment-desk` for rollout execution planning, `implementation-handoff-desk` for any final PR or tag-prep work, `ci-failure-desk` for failing checks, and `incident-response-desk` if release risk is tied to an active incident.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
