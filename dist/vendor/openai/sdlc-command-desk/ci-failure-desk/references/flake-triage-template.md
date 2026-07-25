# Flaky-Test Triage Template

Use this when a test, workflow, or deployment gate appears intermittent.

## Required structure

```markdown
# Flaky-Test Triage: <test or check>

## How to use this file
Use this triage to decide whether a rerun is justified, whether a quarantine or fix issue is required, and what evidence must be retained.

## Flake decision
Decision: likely flaky | not flaky | insufficient evidence | infrastructure transient | deterministic failure
Confidence: high | medium | low

## Evidence reviewed
- Current failing run:
- Prior runs:
- Same commit behavior:
- Same test behavior across branches:
- Relevant logs:

## Test/check identity
- Test/check name:
- File or workflow:
- Runtime environment:
- Dependencies or services:

## Failure pattern
| Observation | Evidence | Interpretation |
|---|---|---|
| fails and passes on same commit |  |  |
| timeout or race pattern |  |  |
| external service dependency |  |  |
| order-dependent behavior |  |  |
| resource contention |  |  |
| data/time dependency |  |  |

## Recommended action
- Rerun policy:
- Quarantine policy:
- Fix issue needed:
- Release impact:
- Verification follow-up:

## Required follow-up
- Action:
```

## Flake discipline

A single failed run is not enough to prove flakiness. Prefer same-commit pass/fail evidence, repeated intermittent signatures, infrastructure signals, or known historical failure records.
