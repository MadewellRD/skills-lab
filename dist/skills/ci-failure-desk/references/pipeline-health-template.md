# Pipeline Health Template

Use this for workflow reliability, required-check design, build time, test split, caching, runner permissions, or release-gate health reviews.

## Required structure

```markdown
# Pipeline Health Review: <repo or workflow>

## How to use this file
Use this review to plan CI improvements, reduce false failures, strengthen gates, or create downstream issues.

## Scope
- Repo:
- Workflows:
- Required checks:
- Time window or commits reviewed:

## Source facts
- Workflow files:
- Check/run history:
- Policy docs:
- Unverified assumptions:

## Health findings
| ID | Finding | Impact | Evidence | Recommendation |
|---|---|---:|---|---|

## Gate quality
| Gate | Purpose | Signal quality | Failure mode | Suggested change |
|---|---|---:|---|---|

## Reliability risks
- Risk:

## Efficiency opportunities
- Opportunity:

## Security and permissions observations
- Observation:

## Downstream issues
| Issue title | Priority | Acceptance gate | Owner if known |
|---|---:|---|---|
```

## Pipeline review discipline

Do not recommend removing gates solely because they are noisy. Prefer isolating flake sources, improving diagnostics, splitting slow jobs, narrowing permissions, and preserving release-relevant signal.
