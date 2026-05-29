# Eval Quality Checklist

Use this checklist before advancing from Eval Design Desk.

## Coverage

- Representative success cases are included.
- Edge cases and negative cases are included.
- Known failures and regressions are included.
- Safety or high-impact slices are included when risk is material.
- Dataset rights, privacy, provenance, and split policy are explicit for release-bound evals.

## Scoring

- Rubric fields are objective enough for repeatable review.
- Grader type is specified.
- Human review policy is specified when model grading is insufficient.
- Thresholds include pass, warn, block, rerun, and review states where relevant.

## Release interpretation

- Eval output maps to a release gate or explicit non-release exploratory status.
- Rerun cadence is defined.
- Reporting fields are defined.
- Rollback implications are named when release-bound.

## Halt triggers

Return `Workflow Halt` if behavior contract, representative examples, scoring criteria, safety threshold, dataset rights, or release decision policy is missing.
