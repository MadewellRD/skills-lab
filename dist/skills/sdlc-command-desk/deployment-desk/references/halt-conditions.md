# Halt Conditions

Halt or produce a deployment diagnostic when any of these apply:

- Target environment is unknown.
- Deployment mechanism is unknown.
- Release scope is not confirmed.
- CI, verification, or required checks are red or unavailable without an accepted exception.
- Rollback path is missing, untested, or contradictory.
- Required approval is missing.
- Feature-flag or rollout control cannot be verified.
- Monitoring or post-deploy verification is absent for a risky change.
- Source facts conflict on what is being deployed.
- The request asks for execution of a deployment when only a planning artifact can be safely produced.
- The artifact would require inventing owners, commands, environment names, or health checks.

When halting, state the blocker, the missing source, why it matters, and the smallest next step to unblock.
