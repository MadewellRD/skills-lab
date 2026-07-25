# Connector Preflight

Use this before producing a route, plan, or handoff.

## Required by fact type

| Fact needed | Required source |
|---|---|
| repo, branch, commit, PR, issue, changed files, checks, tests | GitHub |
| product goals, roadmap, spec language, decision records | docs connector or uploaded docs |
| recent team decision, halt report, approval context | communication connector or pasted context |
| CI logs, workflow runs, job output | GitHub Actions via GitHub connector |
| release/deployment status | GitHub releases, deployment config, docs, or available platform connector |
| incidents, telemetry, SLOs | monitoring docs, incident docs, logs/metrics/traces when available |

## Preflight result categories

- `grounded`: required facts are present and current.
- `partially grounded`: some facts are present; missing facts are listed.
- `user-fact only`: only pasted context is available.
- `blocked`: required connector facts are unavailable and the output would be unsafe.

## Missing facts behavior

Do not invent missing facts. Either route upstream, produce a connector diagnostic, or mark the output as user-fact only.
