# Connector Routing

## GitHub

Required when the retrospective references repository work, PRs, commits, branches, issues, milestones, reviews, releases, checks, or CI.

Retrieve:

- PR numbers, titles, state, authors, reviewers, changed files, and timelines.
- Commit SHAs and messages.
- Issue scope, labels, milestone, acceptance criteria, and comments.
- CI status, failed checks, workflow jobs, and rerun history.
- Release tags and related PRs when applicable.

## Documentation sources

Required when the retrospective depends on PRDs, SRS documents, architecture docs, release notes, runbooks, parity documents, audit packs, status docs, or prior retrospectives.

Retrieve canonical docs and note stale or conflicting sections.

## Communication sources

Use Slack, Teams, email, or pasted halt reports for decision history and coordination context. Do not treat chat as code-state truth.

## Observability and incident sources

Use when production impact, alerting, telemetry, customer impact, or incident timeline is part of the retrospective.

## Public web

Use only for external tool behavior or public dependency facts not available in repo or internal docs.
