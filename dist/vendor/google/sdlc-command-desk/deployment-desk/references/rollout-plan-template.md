# Rollout Plan Template

Use this for staged rollout, canary, dark launch, beta, feature-flag, cohort, regional, or phased deployment planning.

## Rollout strategy

- Rollout type:
- Target population:
- Initial exposure:
- Expansion increments:
- Hold periods:
- Completion criteria:

## Feature flags and controls

For each flag or control:

- Name:
- Owner:
- Default state:
- Target state:
- Exposure rule:
- Kill-switch behavior:
- Audit or logging requirement:

## Stage gates

For each stage:

- Entry criteria:
- Action:
- Observation window:
- Health metrics:
- Error budget or tolerance:
- Expansion decision:
- Rollback decision:

## Blast radius

Describe users, tenants, regions, APIs, jobs, dependencies, data stores, and downstream systems affected at each stage.

## Monitoring

List dashboards, alerts, logs, traces, business metrics, support signals, and owner review cadence.

## Pause and rollback triggers

Define objective triggers. Avoid subjective language such as "looks bad" unless paired with measurable signals.
