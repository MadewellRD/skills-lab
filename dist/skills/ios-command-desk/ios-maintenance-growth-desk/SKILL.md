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

1. Resolve maintenance/growth trigger: SDK policy, dependency risk, crash/main-thread stall trend, retention, monetization, store listing, live ops, feature debt, or migration.
2. Collect repo, release, telemetry, policy, customer, review, and source facts.
3. Classify work as maintenance, growth experiment, migration, refactor, decommissioning candidate, or release-policy response.
4. Produce scoped plan with validation commands, risk controls, rollout/rollback, and success metrics.
5. Hand off to SDLC maintenance/refactor, issue planning, implementation, experiment, retrospective, or decommissioning workflows when needed.

## Responsibilities

- Keep iOS apps/games current with SDK, App Review policy, dependency, Xcode, engine, and store changes.
- Turn telemetry, reviews, feedback, and live-ops evidence into bounded growth experiments.
- Plan refactors and migrations without destabilizing live app/game surfaces.
- Preserve source facts and avoid open-ended coding-agent prompts.

## Expected inputs

Repo facts, dependency/SDK state, App Review policy notices, crash/main-thread stall/analytics trends, reviews, feedback, experiment history, release history, live-ops data, and prior `ios_delivery_packet`.

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

- `ios-maintenance-plan.md`
- `ios-sdk-dependency-update-plan.md`
- `ios-growth-experiment-brief.md`
- `ios-debt-register.md`
- `workflow-halt.md`

## Downstream handoff

Use SDLC maintenance/refactor, issue planning, implementation handoff, retrospective, or decommissioning desks as needed after iOS-specific scope is clear.

## SDLC suite handoff

Use `maintenance-refactor-desk`, `issue-planning-desk`, `implementation-handoff-desk`, `review-quality-desk`, `test-strategy-desk`, `retrospective-desk`, or `decommissioning-desk` when maintenance/growth work needs generic lifecycle support.

## iOS research grounding

- Use progressive disclosure: keep routing metadata short, active desk instructions bounded, and references cold until needed.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
