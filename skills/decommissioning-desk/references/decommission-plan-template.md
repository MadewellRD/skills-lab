# Decommission Plan Template

Use this structure for retiring a feature, service, job, environment, repository, flag, dependency, or integration.

## Executive summary

- Target:
- Retirement type:
- Proposed sunset date or window:
- Current status:
- Decision needed:

## Source facts

- Confirmed code references:
- Confirmed owners:
- Confirmed docs/runbooks:
- Confirmed issues/PRs:
- Confirmed usage or traffic evidence:
- Confirmed retention/compliance constraints:

## Scope

### In scope

- Components to retire.
- Config, flags, workflows, jobs, or docs to change.
- Tests and verification gates.

### Out of scope

- Adjacent systems not affected.
- Deferred cleanup.
- Follow-up migrations not required for this retirement.

## Dependency and consumer analysis

| Consumer or dependency | Evidence | Impact | Required action | Owner | Status |
|---|---|---|---|---|---|

## Retirement sequence

1. Pre-sunset readiness.
2. Consumer migration or traffic drain.
3. Disable or freeze.
4. Monitor for residual usage.
5. Remove code/config/docs.
6. Archive retained data/artifacts.
7. Post-retirement verification.

## Risks and mitigations

| Risk | Likelihood | Impact | Mitigation | Halt trigger |
|---|---|---|---|---|

## Verification gates

- No active traffic or dependent consumers remain.
- Tests and CI pass.
- Alerts/logs show no unexpected calls or failures.
- Docs/runbooks are updated or removed.
- Support/customer communications are complete.
- Rollback path remains available until the defined cutoff.

## Downstream handoff

- PR work needed:
- Release/deployment work needed:
- Verification work needed:
- Docs/proof-map work needed:
