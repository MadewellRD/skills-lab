# Output Contract

## Default artifacts

Use one of these artifacts depending on the request:

- `pr-review-report.md`: full review decision and findings.
- `diff-risk-assessment.md`: risk-only review for a patch or commit range.
- `missing-test-assessment.md`: test coverage and validation gap review.
- `review-comment-plan.md`: inline/top-level comment plan for a PR.
- `quality-gate-summary.md`: merge readiness and gate status.
- `review-to-pr-command-handoff.md`: follow-up implementation handoff for `implementation-handoff-desk`.

## Required sections for review artifacts

Every review artifact must include:

- Review target.
- Connector/source facts.
- Decision or evidence status.
- Findings with severity/category/evidence/impact/recommendation.
- Missing tests or validation.
- Risk summary.
- Follow-up handoff when needed.

## Downloadable Markdown wrapper

When producing a file for the user, wrap it as:

```markdown
# [artifact title]

## How to use this file

Use this review artifact to decide whether to approve, comment, request changes, or route follow-up work through `implementation-handoff-desk`. Preserve source facts and unresolved evidence gaps.

## Review Artifact

[content]
```
