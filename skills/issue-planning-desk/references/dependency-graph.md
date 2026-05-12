# Dependency Graph Rules

Use a dependency graph when the work has ordering constraints.

## Classification

- Hard dependency: a later issue cannot start until the earlier issue lands.
- Soft dependency: work can begin, but final validation depends on another issue.
- Parallel work: issues can run independently.
- Blocking unknown: a decision or source fact is missing.

## Output format

```markdown
## Dependency graph

| Issue | Depends on | Blocks | Dependency type | Reason |
|---|---|---|---|---|
| issue-title-a | none | issue-title-b | hard | Contract must exist first |

## Recommended sequence

1. Foundation
2. Implementation
3. Integration
4. Tests and verification
5. Docs and release readiness

## Parallel lanes

- Lane A:
- Lane B:

## Blocking unknowns

- Unknown:
- Needed from:
- Halt or continue:
```

Do not mark work parallel just because it is owned by different people. Parallel work must not require unstable shared contracts, migrations, or generated artifacts from another active issue.
