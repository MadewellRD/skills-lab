# Handoff Rules

Route downstream work by type:

- Code hotfix or bounded remediation: `implementation-handoff-desk`.
- CI failure or flaky check: `ci-failure-desk`.
- Rollback, redeploy, staged rollout, or feature flag: `deployment-desk`.
- Release note, tag, rollback plan, or post-release check: `release-operations-desk`.
- Missing metrics, logs, traces, alerts, or runbook: `observability-readiness-desk`.
- Requirement or acceptance proof: `verification-desk`.
- Docs, proof map, runbook, or status page update: `docs-traceability-desk`.
- Security/privacy incident: `security-threat-desk` before implementation handoff.

Handoff notes must include confirmed facts, unresolved unknowns, validation gates, and halt conditions.
