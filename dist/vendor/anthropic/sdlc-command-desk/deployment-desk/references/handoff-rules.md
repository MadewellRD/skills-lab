# Handoff Rules

Use downstream handoffs when deployment planning reveals work outside this skill.

- Send release scope, versioning, rollback ownership, or release notes gaps to `release-operations-desk`.
- Send failing checks, flaky jobs, or deploy pipeline failures to `ci-failure-desk`.
- Send missing acceptance evidence to `verification-desk`.
- Send monitoring, SLO, alerting, or runbook gaps to `observability-readiness-desk`.
- Send rollback PRs, config patches, or execution prompts to `implementation-handoff-desk`.
- Send production failures or customer-impacting regressions to `incident-response-desk`.

A handoff must include source facts, the blocking question, the current artifact, and the exact next decision needed.
