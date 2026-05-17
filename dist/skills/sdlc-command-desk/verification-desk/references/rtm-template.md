# Requirements Traceability Matrix Template

Use this matrix when mapping requirements to implementation and evidence.

| requirement id | requirement summary | source | implementation evidence | test/validation evidence | status | gaps | owner/follow-up |
|---|---|---|---|---|---|---|---|
| REQ-001 | ... | PRD/SRS/issue | PR/commit/files | tests/checks/QA | verified | none | n/a |

## Status taxonomy

- `verified`: direct implementation evidence and validation evidence exist.
- `partially verified`: some evidence exists but coverage is incomplete.
- `unverified`: requirement exists but no adequate evidence exists.
- `blocked`: verification cannot continue due to missing access, failing checks, missing environment, or unresolved dependency.
- `not applicable`: requirement is out of scope for the verified change and the reason is documented.

## Rules

- Do not mark `verified` from implementation evidence alone.
- Do not mark `verified` from test names alone; confirm test execution when possible.
- If requirement IDs are absent, create temporary IDs in report order and state that they are report-local.
- Preserve exact external IDs from PRD, SRS, issues, and milestone docs when they exist.
