# Connector Routing

## GitHub

Required when the output references repository tests, source files, PR diffs, changed files, issues, commits, CI status, build commands, prior regressions, or named test cases.

Retrieve:

- repo owner/name and default branch
- relevant files and test directories
- PR diff or changed file list when reviewing a change
- linked issues and acceptance criteria
- CI/check status and failing job summaries when available
- test names, assertions, fixtures, commands, and known flaky areas

## Documents and uploaded files

Required when requirements, PRDs, SRS/SDS, QA plans, release notes, architecture specs, audit material, or external specs drive test scope.

Retrieve:

- requirement IDs and acceptance criteria
- non-goals and deferred scope
- architecture and integration boundaries
- compliance, privacy, or release constraints

## Communication sources

Use Slack, Teams, email, or pasted halt reports only for recent decisions, triage notes, stakeholder clarifications, or unresolved dispute context. Do not treat chat as repo truth.

## Public web

Use only for external API, platform, browser, framework, or compliance facts not available from repo or internal docs. Record the source and date sensitivity.
