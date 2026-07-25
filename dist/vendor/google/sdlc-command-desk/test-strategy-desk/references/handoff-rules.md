# Handoff Rules

Use these routing rules after producing a test artifact:

- To `verification-desk`: hand off requirement-to-test mapping, scenario matrix, evidence needs, and acceptance gates.
- To `review-quality-desk`: hand off missing tests, changed-file risk, and review-blocking coverage gaps.
- To `ci-failure-desk`: hand off flaky-test classifications, failing commands, suspected failure domains, and minimization targets.
- To `implementation-handoff-desk`: hand off exact test implementation scope, allowed files, validation commands, commit structure, and halt conditions.
- To `release-operations-desk`: hand off release-blocking test gaps, manual validation requirements, rollback-sensitive scenarios, and go/no-go evidence.

Do not convert a test strategy into implementation instructions unless the user requests a handoff prompt or PR scope.
