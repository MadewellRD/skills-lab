# Hotfix Handoff Template

```markdown
# Hotfix Handoff: [incident or bug]

## How to use this file

Paste the implementation section into `implementation-handoff-desk` or the target coding agent after connector facts are verified.

## Incident context
- Incident ID/link:
- Severity:
- Current state:
- Affected systems:

## Repo facts
- Repository:
- Base branch:
- Candidate files:
- Recent related commits/PRs:
- Required validation:

## Hotfix scope
- Required change:
- Explicitly out of scope:
- Rollback constraint:
- Risk controls:

## Implementation prompt seed

You are operating on [repo]. Your job is to implement a bounded hotfix for [incident/bug].

Do not broaden scope. If the suspected fix requires unrelated refactoring, halt and report.

## Validation gates

## Halt conditions

## PR title and body requirements

## Stop line

Stop at "PR opened, hotfix validation running." Do not merge.
```
