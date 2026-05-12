# Connector Routing

## Required source roles

Use GitHub when the retirement touches code, configs, workflows, issues, PRs, tests, branches, release history, or ownership clues.

Use documentation sources or uploaded files when the retirement depends on product docs, API docs, architecture docs, runbooks, roadmap commitments, migration guides, or retention policy.

Use observability or incident sources when runtime usage, traffic, logs, metrics, traces, alerts, incidents, or operational risk determine safety.

Use issue/project sources when milestones, blockers, customer commitments, ownership, labels, or linked work determine sequencing.

Use communication sources when stakeholder decisions, customer notices, support status, or recent halt reports are not present in docs or issues.

## Target-specific routing

| Target type | Required facts | Preferred sources | Halt if missing |
|---|---|---|---|
| api endpoint or SDK method | consumers, route/version, replacement, docs, usage | github, docs, issues, observability | yes |
| service or job | callers, deployment path, runtime health, rollback | github, observability, runbooks | yes |
| feature flag or UI feature | owners, users, flag config, docs, tests | github, docs, issues, analytics | conditional |
| data store or table | data class, retention, archive/delete path, owners | docs, github, compliance docs | yes |
| dependency or package | import graph, version constraints, alternatives, CI | github, ci, issues | conditional |
| environment or infrastructure | traffic, deploy config, owners, rollback | github, deployment docs, observability | yes |

## Connector diagnostic

When required facts cannot be retrieved, produce a diagnostic with:

- missing fact;
- why it is needed;
- source expected to provide it;
- risk if omitted;
- minimum safe next action.
