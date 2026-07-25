# Connector Routing

## Required by request type

| Request | Required sources | Facts to retrieve |
|---|---|---|
| Release readiness | GitHub, release docs when present | target branch, commits, PRs, checks, issues, changelog, blockers |
| Release notes | GitHub, docs | merged PRs, issue titles, user-visible changes, known limitations |
| Version/tag plan | GitHub | current tags, target commit, branch, version files, changelog |
| Rollback plan | GitHub, deployment docs | release delta, deploy surface, migrations, rollback docs, affected services |
| Post-release verification | GitHub, deployment/observability docs when available | deployed version, checks, smoke tests, monitoring plan |
| Handoff | GitHub plus relevant downstream docs | executor scope, validation commands, halt conditions |

## Missing sources

If GitHub is unavailable for repo-specific releases, do not produce a confident release decision. Produce a source-limited draft or connector diagnostic.

If docs are unavailable for changelog, release policy, or deployment runbooks, mark those gates as unknown and require follow-up.
