# Blocker Rubric

## Release blocker
Use when shipping would create a known unacceptable risk or violate a required gate.

Examples:
- A must-have requirement lacks implementation evidence.
- Required tests or CI checks are failing.
- Security/privacy approval is required but absent.
- Migration or rollback path is missing for a risky change.
- Acceptance criteria are contradicted by observed behavior.

## Evidence blocker
Use when the work might be correct but cannot be verified.

Examples:
- CI logs are inaccessible.
- Manual QA evidence is referenced but not attached.
- Test names are mentioned but no run status is available.
- Requirement source documents are missing.

## Non-blocking risk
Use when the risk should be documented but does not prevent proceeding under the stated policy.

Examples:
- Nice-to-have scenario lacks coverage.
- Documentation can be updated in a follow-up and is not release-critical.
- Hosted CI is unavailable but local verification is accepted by project policy.
