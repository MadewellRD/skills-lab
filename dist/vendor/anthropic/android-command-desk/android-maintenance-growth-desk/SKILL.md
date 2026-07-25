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

**Outcome.** A bounded Android maintenance or growth plan: the trigger and its source, affected modules, dependency/SDK/engine/policy facts, the work classification (maintenance, growth experiment, migration, refactor, decommissioning candidate, or release-policy response), success metrics and guardrails, rollout and rollback, validation commands, and implementation boundaries.

**Grounding.** Work from repo facts, dependency and SDK state, Play policy notices, crash/ANR and analytics trends, reviews, feedback, experiment history, release history, and live-ops data. Do not invent dependency state, SDK policy, Play policy, telemetry, experiment, monetization, store, or validation facts.

**Ordered content that stays ordered.** Where the plan responds to a Play policy deadline, a target-SDK level bump, or an on-device data migration, emit the sequence as ordered steps and keep it ordered. The order is externally imposed: Play policy deadlines are set by Google and missing one removes the app from distribution, target-SDK bumps gate on Play's published enforcement dates, and an on-device migration applied out of order against user data cannot be undone by a later release.

**Parallel surface.** Individual dependency upgrades, separate growth experiments, distinct debt items, and per-module impact assessments are independent: assess them in parallel. Sequencing upgrades that share a build graph is aggregate and sequential — resolve version conflicts across the whole graph once, after the per-dependency assessments exist, rather than upgrading one at a time and re-resolving each round.

**Acceptance bar.** The plan is sound when the trigger cites its source; affected modules are named from repo evidence; each dependency or SDK change states its breaking-change surface and the validation command that proves it; every experiment has a metric, guardrail, sample basis, rollback, and decision rule; and each item is either scheduled with an owner or explicitly marked owner-unknown.

Hand off to SDLC maintenance/refactor, issue planning, implementation, experiment, retrospective, or decommissioning workflows when needed.

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

Proceed by default. An incomplete trigger or unclear scope is normally a labeled assumption plus an open question, not a stop. Reserve hard halts for these consequence classes:

- **Approval** — an upgrade, migration, experiment launch, monetization change, or decommissioning decision requires a human owner to authorize it.
- **Production or destructive** — the plan would act on live users, live economy state, or production data: launching an experiment, removing a feature or surface, or migrating on-device user data.
- **Security or privacy** — a dependency, SDK, or policy change alters how personal data or credentials are handled, or the upgrade is a security fix whose details cannot be handled safely here.
- **Source conflict** — repo state, release history, and telemetry genuinely disagree on current version, dependency state, or observed trend. Preserve the conflict.
- **Release integrity** — a Play policy, dependency, SDK, engine, or store change has release impact and would be reported as handled with no owner, timeline, or validation path.
- **Connector unreachable** — repo, release, telemetry, or policy sources exist but cannot be read.

Otherwise proceed: a missing trigger detail, unknown affected module, or unvalidated path becomes a labeled assumption naming the evidence needed to confirm it, and the plan is scoped to what the known facts support.

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

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
