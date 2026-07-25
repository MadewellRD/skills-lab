---
name: ios-maintenance-growth-desk
description: plan iOS maintenance, dependency upgrades, SDK target updates, deprecations, App Review policy changes, experiments, monetization iteration, store optimization, retention, and technical debt.
---

# iOS Maintenance Growth Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. Complete this desk's artifact, update the `ios_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing dependency state, SDK policy, App Review policy, telemetry, experiment, monetization, store, or validation facts.

## Role

Plan iOS maintenance and growth: dependency upgrades, iOS Xcode Plugin/Swift/SDK target updates, deprecations, App Review policy changes, experiments, monetization iteration, store optimization, retention, live-ops iteration, refactors, migrations, and technical debt.

## Workflow

**Outcome.** A bounded iOS maintenance or growth plan: the trigger and its source, affected modules, dependency/SDK/engine/policy facts, the work classification (maintenance, growth experiment, migration, refactor, decommissioning candidate, or release-policy response), success metrics and guardrails, rollout and rollback, validation commands, and implementation boundaries.

**Grounding.** Work from repo facts, dependency and SDK state, App Review policy notices, crash, main-thread-stall and analytics trends, reviews, feedback, experiment history, release history, and live-ops data. Do not invent dependency state, SDK policy, App Review policy, telemetry, experiment, monetization, store, or validation facts.

**Ordered content that stays ordered.** Where the plan responds to an App Review policy deadline, a minimum-SDK or Xcode version requirement for App Store submission, or an on-device data migration, emit the sequence as ordered steps and keep it ordered. The order is externally imposed: Apple sets submission deadlines and after them App Store Connect rejects builds outright, SDK and Xcode minimums gate submission rather than merely warning, and an on-device migration applied out of order against user data cannot be undone by a later release.

**Parallel surface.** Individual dependency upgrades, separate growth experiments, distinct debt items, and per-module impact assessments are independent: assess them in parallel. Sequencing upgrades that share a dependency graph is aggregate and sequential — resolve version conflicts across the whole graph once, after the per-dependency assessments exist, rather than upgrading one at a time and re-resolving each round.

**Acceptance bar.** The plan is sound when the trigger cites its source; affected modules are named from repo evidence; each dependency or SDK change states its breaking-change surface and the validation command that proves it; every experiment has a metric, guardrail, sample basis, rollback, and decision rule; and each item is either scheduled with an owner or explicitly marked owner-unknown.

Hand off to SDLC maintenance/refactor, issue planning, implementation, experiment, retrospective, or decommissioning workflows when needed.

## Responsibilities

- Keep iOS apps/games current with SDK, App Review policy, dependency, Xcode, engine, and store changes.
- Turn telemetry, reviews, feedback, and live-ops evidence into bounded growth experiments.
- Plan refactors and migrations without destabilizing live app/game surfaces.
- Preserve source facts and avoid open-ended coding-agent prompts.

## Expected inputs

Repo facts, dependency/SDK state, App Review policy notices, crash/main-thread stall/analytics trends, reviews, feedback, experiment history, release history, live-ops data, and prior `ios_delivery_packet`.

## Expected outputs

A complete run delivers everything the work classification puts in scope, in full: the maintenance or growth plan, the dependency and SDK update plan, the experiment brief, the debt register, the migration or refactor handoff, any halt conditions, and the packet update. Where the classification genuinely rules one out — a straight toolchain upgrade has no growth experiment — that artifact is reported as not applicable with the reason, which is different from dropping it silently or writing a generic one to fill the slot.

Each artifact is done when someone could pick it up and execute it. The update plan names each dependency with its current and target version, its breaking changes, and the ordering forced by the shared dependency graph; the experiment brief states the hypothesis, the metric, the guardrail, and the stop condition; the debt register names each item, what it costs, and what retiring it unblocks. "Update dependencies" is not a plan.

None of it gets filled in from convention. A version, an App Review policy change, an SDK requirement, a metric baseline, or a debt cost that no source establishes is recorded as unknown with the check that would resolve it — a guessed target version turns a maintenance plan into a broken build. Individual upgrades, experiments, debt items, and per-module impact assessments are independent and part of the parallel surface declared in Workflow.

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
- **Release integrity** — an App Review policy, dependency, SDK, engine, or store change has release impact and would be reported as handled with no owner, timeline, or validation path.
- **Connector unreachable** — repo, release, telemetry, or policy sources exist but cannot be read.

Otherwise proceed: a missing trigger detail, unknown affected module, or unvalidated path becomes a labeled assumption naming the evidence needed to confirm it, and the plan is scoped to what the known facts support.

## Default output modes

A complete run writes each of these that the work classification puts in scope, and marks the rest not applicable with the reason:

- `ios-maintenance-plan.md`
- `ios-sdk-dependency-update-plan.md`
- `ios-growth-experiment-brief.md`
- `ios-debt-register.md`

Mode-specific alternative:

- `workflow-halt.md` — stands in for the set above when a hard halt fires, rather than being added to it.

## Downstream handoff

Use SDLC maintenance/refactor, issue planning, implementation handoff, retrospective, or decommissioning desks as needed after iOS-specific scope is clear.

## SDLC suite handoff

Use `maintenance-refactor-desk`, `issue-planning-desk`, `implementation-handoff-desk`, `review-quality-desk`, `test-strategy-desk`, `retrospective-desk`, or `decommissioning-desk` when maintenance/growth work needs generic lifecycle support.

## iOS research grounding

- Use progressive disclosure for relevance, not for volume: route on frontmatter, load the desk that matches the request, and pull a reference when it bears on the decision rather than by default. Context is not the scarce resource; ambiguity is.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
