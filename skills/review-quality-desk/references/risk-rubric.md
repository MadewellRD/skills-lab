# Risk Rubric

## Severity

- `blocking`: likely incorrect, unsafe, data-losing, security-sensitive, or merge-blocking.
- `major`: material risk that should be fixed before merge unless explicitly accepted.
- `minor`: localized issue, readability concern, small test gap, or non-blocking edge case.
- `note`: informational observation or follow-up suggestion.

## Risk dimensions

Assess risk across:

- Correctness and edge cases.
- Regression and blast radius.
- Test adequacy.
- Security, privacy, and secrets.
- Data/schema/API compatibility.
- Reliability and performance.
- Maintainability and convention alignment.
- Documentation/release readiness.

## Decision guidance

- Any unresolved blocking finding -> request changes.
- Multiple major findings with unclear ownership -> request changes.
- Missing required tests for changed critical behavior -> request changes or insufficient evidence.
- Green checks alone are not enough for approval.
- Style-only preferences should not block merge.
