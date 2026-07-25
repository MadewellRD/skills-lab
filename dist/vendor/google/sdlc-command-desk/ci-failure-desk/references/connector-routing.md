# Connector Routing

## GitHub required

Use GitHub for any claim about:

- workflow files, GitHub Actions runs, jobs, logs, artifacts, check suites, commit statuses, branches, PRs, issues, changed files, test names, failing commands, and commit history.

Retrieve when available:

- PR metadata, base/head refs, and changed files
- failing check names and status
- workflow run IDs, job IDs, job steps, logs, artifacts, and rerun state
- commit SHA and combined status
- relevant workflow YAML files
- recent related failures for flake or regression classification

## Docs required

Use docs, uploaded files, Notion, Drive, or SharePoint for:

- release policy, required checks, deployment gates, test strategy, flake policy, incident policy, and team-specific CI conventions.

## Communication connectors optional

Use Slack, Teams, email, or pasted halt reports for recent decisions, agent failure reports, incident context, or manual reproduction notes. Do not let chat override GitHub check state.

## Public web allowed

Use public web only for current external service incidents, vendor documentation, CI platform behavior, package registry status, or action/tool documentation when internal sources do not contain the needed external fact.

## Missing connector behavior

If required GitHub or log facts are unavailable, produce a connector diagnostic or mark the output as user-fact-only. Do not invent workflow names, check statuses, job IDs, log lines, test names, or failure history.
