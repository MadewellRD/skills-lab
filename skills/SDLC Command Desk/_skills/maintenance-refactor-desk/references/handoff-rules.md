# Handoff Rules

## To implementation-handoff-desk

Hand off only after scope is bounded. Include:

- Repo and branch facts.
- Allowed files and forbidden files.
- Exact maintenance objective.
- Non-goals.
- Validation gates.
- Commit structure.
- Halt conditions.

## To test-strategy-desk

Use when regression controls are unknown, coverage is weak, or the refactor is behavioral or structural.

## To verification-desk

Use when maintenance work must prove requirement preservation or release readiness.

## To ci-failure-desk

Use when the maintenance request is triggered by broken CI, build failures, flaky tests, or slow pipelines.

## To security-threat-desk

Use for vulnerable dependencies, auth/authz changes, secrets, crypto, privacy, supply chain, or permission boundaries.

## To release/deployment desks

Use for migrations, package/runtime upgrades, release-sensitive config, rollout, feature flags, or rollback planning.
