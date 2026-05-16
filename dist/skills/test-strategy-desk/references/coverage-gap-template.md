# Coverage Gap Template

Use this when comparing requirements or risks against existing tests.

```markdown
# Coverage Gap Report: <scope>

## Summary
State total requirements or risk areas reviewed and the coverage posture.

## Coverage table
| id | requirement or risk | current coverage | evidence | gap | recommended coverage | priority |
|---|---|---|---|---|---|---|
| REQ-001 | requirement text | covered, partial, missing, deferred, unknown | file/test/CI/source fact | what is absent | proposed test or check | p0/p1/p2 |

## High-priority missing coverage
List gaps that block implementation, review, release, or verification.

## Deferred coverage
List intentionally deferred areas and rationale.

## Unknowns
List items that cannot be assessed because connector evidence is missing.
```

Never infer coverage from filenames alone when the exact test behavior matters. Inspect test names, assertions, or user-provided evidence when possible.
