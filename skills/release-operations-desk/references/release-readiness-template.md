# Release Readiness Template

Use this structure when the user asks whether a release is ready.

```markdown
# Release Readiness Report: <release name or version>

## Decision

Status: pass | fail | blocked | unknown

## Scope

- Target version/tag:
- Target branch or commit range:
- Included PRs/issues:
- Excluded/deferred work:

## Gate summary

| Gate | Status | Evidence | Notes |
|---|---|---|---|
| Scope confirmed |  |  |  |
| CI/checks green |  |  |  |
| Verification complete |  |  |  |
| Security/privacy reviewed |  |  |  |
| Docs/changelog ready |  |  |  |
| Rollback path defined |  |  |  |
| Deployment plan ready |  |  |  |
| Stakeholder approval captured |  |  |  |

## Release risks

| Risk | Severity | Evidence | Mitigation | Owner |
|---|---|---|---|---|

## Required actions before release

1. ...

## Source facts

- ...

## Downstream handoff

- `deployment-desk`: ...
- `implementation-handoff-desk`: ...
- `verification-desk`: ...
```
