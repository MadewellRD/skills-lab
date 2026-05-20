# Eval Run Quality Checklist

## Run completeness

- Raw result artifact exists.
- Run ID, timestamp, model version, prompt/config version, dataset slice IDs, grader version, and code commit are known.
- Baseline run is available and comparable.
- Rubric and thresholds are available.

## Analysis quality

- Aggregate scores are broken down by slice.
- Failure examples support each failure cluster.
- Safety, privacy, data leakage, prompt injection, and high-impact failures are separated from ordinary quality failures.
- Grader reliability is assessed or marked as a halt.
- Release status is explicit: pass, warning, blocker, or halt.

## Rerun quality

- Rerun scope names the exact slices and fixtures.
- Rerun trigger is explicit: fix landed, grader changed, dataset changed, baseline refreshed, or manual review completed.
- Downstream owner desk is named for each fix category.
```
