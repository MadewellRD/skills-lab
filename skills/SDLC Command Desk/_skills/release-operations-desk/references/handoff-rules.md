# Handoff Rules

Use downstream skills as follows:

- `implementation-handoff-desk`: final PR, branch, tag-prep, merge-train, or halt-resume prompts.
- `deployment-desk`: rollout, deployment sequencing, feature flag, and go/no-go deployment plans.
- `verification-desk`: missing V&V evidence, RTM, acceptance gate proof, release blockers.
- `ci-failure-desk`: red checks, flaky tests, failed release workflows, rerun decisions.
- `docs-traceability-desk`: changelog, proof maps, release evidence packets, doc-code consistency.
- `security-threat-desk`: unresolved security/privacy risk before release.
- `incident-response-desk`: active production incident, hotfix release, rollback-triggered response.

Do not convert a release decision into execution instructions unless the user requests an execution handoff.
