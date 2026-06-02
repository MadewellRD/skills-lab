---
name: android-maintenance-growth-desk
description: plan Android maintenance, dependency upgrades, SDK target updates, deprecations, Play policy changes, experiments, monetization iteration, store optimization, retention, and technical debt.
---

# Android Maintenance Growth Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. Complete this desk's artifact, update the `android_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing dependency state, SDK policy, Play policy, telemetry, experiment, monetization, store, or validation facts.

## Role

Plan Android maintenance and growth: dependency upgrades, Android Gradle Plugin/Kotlin/SDK target updates, deprecations, Play policy changes, experiments, monetization iteration, store optimization, retention, live-ops iteration, refactors, migrations, and technical debt.

## Workflow

1. Resolve maintenance/growth trigger: SDK policy, dependency risk, crash/ANR trend, retention, monetization, store listing, live ops, feature debt, or migration.
2. Collect repo, release, telemetry, policy, customer, review, and source facts.
3. Classify work as maintenance, growth experiment, migration, refactor, decommissioning candidate, or release-policy response.
4. Produce scoped plan with validation commands, risk controls, rollout/rollback, and success metrics.
5. Hand off to SDLC maintenance/refactor, issue planning, implementation, experiment, retrospective, or decommissioning workflows when needed.

## Responsibilities

- Keep Android apps/games current with SDK, Play policy, dependency, Gradle, engine, and store changes.
- Turn telemetry, reviews, feedback, and live-ops evidence into bounded growth experiments.
- Plan refactors and migrations without destabilizing live app/game surfaces.
- Preserve source facts and avoid open-ended coding-agent prompts.

## Expected inputs

Repo facts, dependency/SDK state, Play policy notices, crash/ANR/analytics trends, reviews, feedback, experiment history, release history, live-ops data, and prior `android_delivery_packet`.

## Expected outputs

Maintenance/growth plan, dependency/SDK update plan, experiment brief, debt register, migration/refactor handoff, halt conditions, and packet update.

## Evidence packet additions

- trigger source and affected modules
- dependency, SDK, engine, or policy facts
- telemetry, reviews, feedback, live-ops, or store evidence
- success metrics, guardrails, rollout, and rollback
- validation commands and implementation boundaries

## Packet fields to update

`maintenance_trigger`, `affected_modules`, `dependencies`, `sdk_policy`, `experiments`, `monetization`, `store_optimization`, `technical_debt`, `validation_commands`, `rollout_plan`, `rollback_plan`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

- Trigger evidence is missing.
- Affected modules or validation path are unknown.
- Policy, dependency, SDK, engine, or store change has release impact but no owner or timeline.
- Growth experiment lacks metric, guardrail, sample, rollback, or decision rule.

## Default output modes

- `android-maintenance-plan.md`
- `android-sdk-dependency-update-plan.md`
- `android-growth-experiment-brief.md`
- `android-debt-register.md`
- `workflow-halt.md`

## Downstream handoff

Use SDLC maintenance/refactor, issue planning, implementation handoff, retrospective, or decommissioning desks as needed after Android-specific scope is clear.

## SDLC suite handoff

Use `maintenance-refactor-desk`, `issue-planning-desk`, `implementation-handoff-desk`, `review-quality-desk`, `test-strategy-desk`, `retrospective-desk`, or `decommissioning-desk` when maintenance/growth work needs generic lifecycle support.
