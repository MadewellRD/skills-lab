# Fixture Plan Template

A fixture plan defines the test data and state required to execute the strategy.

```markdown
# Fixture Plan: <feature or risk area>

## Fixture inventory
| fixture | purpose | scope | source | generated or real | reset behavior | privacy notes |
|---|---|---|---|---|---|---|

## Data requirements
List users, roles, permissions, records, files, API payloads, database state, and external service responses.

## Generation strategy
State whether fixtures should be hand-authored, generated deterministically, captured from corpus data, mocked, or imported from sanitized production-like examples.

## Isolation and cleanup
Define how tests avoid cross-test contamination and how data resets.

## Golden files and snapshots
Use golden outputs only when stable and reviewable. Do not snapshot large volatile output without a narrow assertion purpose.

## Privacy and compliance
Do not use real sensitive user data unless the user explicitly states it is approved and sanitized.
```
