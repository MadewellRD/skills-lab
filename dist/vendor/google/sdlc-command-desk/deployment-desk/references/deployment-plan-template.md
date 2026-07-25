# Deployment Plan Template

Use this structure for deployment plans.

## Summary

- Change:
- Release or PR scope:
- Target environment:
- Deployment mechanism:
- Planned window:
- Deployment owner:
- Verification owner:
- Rollback owner:

## Source facts

List verified facts with source names, links, file paths, PRs, commits, issues, or documents.

## Preconditions

- Release readiness:
- CI/deployment checks:
- Verification evidence:
- Security/privacy gates:
- Change approval:
- Observability readiness:
- Rollback readiness:

## Deployment sequence

1. Pre-deploy checks
2. Deploy to target environment
3. Smoke verification
4. Progressive rollout or exposure change
5. Post-deploy monitoring
6. Completion or rollback decision

## Environment and configuration scope

Document environments, regions, services, databases, queues, scheduled jobs, secrets, feature flags, and external integrations affected by the deploy.

## Risk controls

Map each risk to a mitigation, detection signal, owner, and rollback trigger.

## Validation

List exact checks, tests, dashboards, logs, health endpoints, synthetic checks, and manual verification steps.

## Rollback

Define rollback trigger, rollback command or procedure, expected duration, data migration considerations, and verification after rollback.

## Communications

List stakeholders, notification timing, customer-facing impact, internal status channel, and final completion note.

## Open questions

Only include questions that block safe deployment or materially change rollout risk.
