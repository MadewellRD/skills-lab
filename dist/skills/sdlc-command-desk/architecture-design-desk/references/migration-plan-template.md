# Migration Plan Template

Use this when architecture work changes existing systems, data, APIs, storage, dependencies, or runtime behavior.

```markdown
# [Migration Name] Plan

## Goal

[What changes and why.]

## Current state

[Verified current architecture and constraints.]

## Target state

[Verified or proposed target architecture.]

## Compatibility requirements

- [Consumer compatibility]
- [Data compatibility]
- [API compatibility]
- [Operational compatibility]

## Phases

| Phase | Change | Validation | Rollback |
|---|---|---|---|
| 0 | [Preparation] | [Check] | [Rollback] |
| 1 | [Change] | [Check] | [Rollback] |
| 2 | [Cleanup] | [Check] | [Rollback] |

## Data and state handling

[Migration, backfill, cache, retention, and consistency details.]

## Feature flags and rollout controls

[Flags, staged rollout, kill switch, monitoring.]

## Risks and mitigations

| Risk | Mitigation | Detection |
|---|---|---|
| [Risk] | [Mitigation] | [Signal] |

## Required implementation handoffs

- [Issue or PR scope]
- [Verification scope]
- [Docs scope]
```
