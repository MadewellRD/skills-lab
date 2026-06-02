---
name: android-product-requirements-desk
description: define Android app and game product requirements, audience, platform targets, acceptance criteria, non-goals, risks, Play constraints, monetization assumptions, and open questions.
---

# Android Product Requirements Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. Complete this desk's artifact, update the `android_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing product, platform, device, monetization, policy, or release facts.

## Role

Turn Android app/game intent into source-grounded requirements with requirement IDs, target users, supported devices, OS/API range, app/game surface, monetization assumptions, Play/store constraints, acceptance criteria, non-goals, risks, and open questions.

## Workflow

1. Resolve goal, user/audience, target Android surface, app/game lane, business constraints, and requested outcome.
2. Capture source facts from issues, uploaded docs, user statements, product docs, design/game docs, store constraints, telemetry, and repo evidence.
3. Convert needs into requirement IDs and acceptance criteria that can be verified on Android devices, emulators, CI, benchmark output, or release gates.
4. Mark non-goals, out-of-scope platforms, privacy/policy constraints, monetization assumptions, rollout constraints, risks, and open questions.
5. Continue to `android-technical-discovery-desk` when requirements are clear enough to inspect implementation reality.

## Responsibilities

- Produce Android-specific PRD sections with requirement IDs and acceptance gates.
- Capture device/API/support assumptions without inventing target versions.
- Separate app user value, game loop value, monetization, Play policy, store listing, and operational requirements.
- Make each acceptance criterion testable or explicitly non-automatable.

## Expected inputs

Product brief, user story, GitHub issue, roadmap item, uploaded research, design/game notes, analytics/feedback, store constraints, or prior `android_delivery_packet`.

## Expected outputs

Android PRD, acceptance criteria, non-goals, risk register, open questions, source-fact summary, and packet update.

## Evidence packet additions

- requirement IDs and acceptance gates
- target app/game surface and lane
- audience, supported devices, OS/API assumptions
- monetization and Play/store constraints
- non-goals, risks, and open questions

## Packet fields to update

`business_goal`, `audience_segments`, `target_surface`, `app_or_game_lane`, `supported_devices`, `min_sdk`, `target_sdk`, `monetization`, `play_policy_constraints`, `acceptance_gates`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

- Product goal, target user, app/game lane, or target surface is unresolved.
- Supported devices or OS/API range affects scope but is unknown.
- Monetization, privacy, policy, store, or compliance constraint is launch-critical but missing.
- Acceptance criteria cannot be made testable from available facts.

## Default output modes

- `android-prd.md`
- `android-acceptance-gates.md`
- `android-risk-register.md`
- `android-product-open-questions.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `android-technical-discovery-desk` unless the user explicitly requested only requirements.

## SDLC suite handoff

Use `product-requirements-desk` patterns for requirement IDs, acceptance criteria, non-goals, risks, and open questions while preserving Android-specific platform facts for downstream desks.
