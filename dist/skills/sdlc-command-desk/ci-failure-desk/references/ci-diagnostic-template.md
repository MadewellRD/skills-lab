# CI Diagnostic Template

Use this for failed checks, workflow runs, build failures, test failures, lint failures, coverage failures, deployment gates, or implementation-agent halt reports.

## Required structure

```markdown
# CI Failure Diagnostic: <subject>

## How to use this file
Use this diagnostic to decide whether to rerun, fix, narrow, escalate, or prepare a PR/halt-resume handoff. Preserve source facts, missing evidence, and halt conditions.

## Triage decision
Decision: rerun | fix required | halt for missing evidence | external incident | release blocker | needs human adjudication
Confidence: high | medium | low

## Scope reviewed
- Repo:
- PR/branch/commit:
- Workflow/check/job:
- Run/log/artifact references:

## Source facts
- GitHub facts:
- Log/error facts:
- Changed-file facts:
- Policy/test/release facts:
- Unverified assumptions:

## Failure signature
- Failing command or step:
- Error excerpt:
- First failing test or check:
- Repeated or one-off:

## Classification
| Category | Applies | Evidence | Notes |
|---|---|---|---|
| code regression |  |  |  |
| test regression |  |  |  |
| flaky test |  |  |  |
| environment failure |  |  |  |
| dependency or registry issue |  |  |  |
| workflow/config failure |  |  |  |
| permission/secret failure |  |  |  |
| quota/billing/external outage |  |  |  |

## Root cause hypothesis
| Hypothesis | Evidence | Confidence | How to verify |
|---|---|---:|---|

## Recommended action
- Immediate action:
- Owner or downstream desk:
- Validation command or check:
- Stop condition:

## Downstream handoff
- For review-quality-desk:
- For verification-desk:
- For release-operations-desk:
- For implementation-handoff-desk:
```

## Diagnostic discipline

Do not call a failure flaky without evidence. Do not call a failure a code regression without connecting the failed check to changed files, commits, or reproducible behavior.
