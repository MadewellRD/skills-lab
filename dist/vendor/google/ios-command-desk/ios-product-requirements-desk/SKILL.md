---
name: ios-product-requirements-desk
description: define iOS app and game product requirements, audience, platform targets, acceptance criteria, non-goals, risks, Play constraints, monetization assumptions, and open questions.
---

# iOS Product Requirements Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. Complete this desk's artifact, update the `ios_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing product, platform, device, monetization, policy, or release facts.

## Role

Turn iOS app/game intent into source-grounded requirements with requirement IDs, target users, supported devices, OS/API range, app/game surface, monetization assumptions, App Store constraints, acceptance criteria, non-goals, risks, and open questions.

## Workflow

**Outcome.** A source-grounded iOS PRD: requirement IDs, target users, supported devices and OS/API range, app/game surface and lane, monetization assumptions, App Store constraints, acceptance criteria, non-goals, risks, and open questions.

**Grounding.** Draw facts from issues, uploaded docs, user statements, product docs, design and game docs, store constraints, telemetry, and repo evidence. Attribute every load-bearing fact to its source and keep verified fact, assumption, and inference separate. Do not invent target users, device support, OS versions, monetization terms, App Review policy obligations, or release dates.

**Constraints.** Acceptance criteria must be checkable on iOS devices, simulators, CI, benchmark output, or release gates, or be marked explicitly non-automatable. Non-goals, out-of-scope platforms, privacy and policy constraints, and rollout constraints are stated, not implied.

**Parallel surface.** Source retrieval across independent inputs — issues, uploaded docs, product docs, design and game docs, telemetry, repo evidence — has no ordering dependency, and acceptance criteria for distinct requirement IDs are independent of one another. Fan out over both. The risk register and the non-goals list are aggregate: assemble them once the per-requirement work is complete.

**Acceptance bar.** The PRD is done when every requirement carries a stable ID; each requirement has acceptance criteria testable without further product input; the app/game lane and target surface are stated; supported devices and OS/API range are either sourced or labeled as assumptions; non-goals, risks, and open questions are explicit rather than implied; and every load-bearing fact is attributed to its source.

Continue to `ios-technical-discovery-desk` when requirements are clear enough to inspect implementation reality.

## Responsibilities

- Produce iOS-specific PRD sections with requirement IDs and acceptance gates.
- Capture device/API/support assumptions without inventing target versions.
- Separate app user value, game loop value, monetization, App Review policy, store listing, and operational requirements.
- Make each acceptance criterion testable or explicitly non-automatable.

## Expected inputs

Product brief, user story, GitHub issue, roadmap item, uploaded research, design/game notes, analytics/feedback, store constraints, or prior `ios_delivery_packet`.

## Expected outputs

iOS PRD, acceptance criteria, non-goals, risk register, open questions, source-fact summary, and packet update.

## Evidence packet additions

- requirement IDs and acceptance gates
- target app/game surface and lane
- audience, supported devices, OS/API assumptions
- monetization and App Store constraints
- non-goals, risks, and open questions

## Packet fields to update

`business_goal`, `audience_segments`, `target_surface`, `app_or_game_lane`, `supported_devices`, `min_sdk`, `target_sdk`, `monetization`, `play_policy_constraints`, `acceptance_gates`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default. An unresolved product detail is normally an open question plus a labeled working assumption, not a stop. Reserve hard halts for these consequence classes:

- **Approval** — scope, monetization, or a policy commitment needs a human owner to authorize it.
- **Production or destructive** — the request would write requirements into a live tracker, roadmap, or customer-facing commitment.
- **Security or privacy** — requirements would encode handling of personal data, secrets, or a child-directed, health, or financial obligation that no source establishes.
- **Source conflict** — product docs, issues, or stakeholder statements genuinely disagree on a load-bearing requirement. Preserve the conflict rather than resolving it silently.
- **Release integrity** — acceptance criteria would be presented as agreed, or a device/OS support range as committed, when no source establishes it.
- **Connector unreachable** — a required source exists but cannot be read. A merely absent source is a soft gap: continue with a labeled assumption.

Otherwise proceed: an unresolved goal, audience, app/game lane, device or OS range, monetization assumption, or policy constraint is recorded as an open question alongside the assumption used in its place.

## Default output modes

- `ios-prd.md`
- `ios-acceptance-gates.md`
- `ios-risk-register.md`
- `ios-product-open-questions.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `ios-technical-discovery-desk` unless the user explicitly requested only requirements.

## SDLC suite handoff

Use `product-requirements-desk` patterns for requirement IDs, acceptance criteria, non-goals, risks, and open questions while preserving iOS-specific platform facts for downstream desks.

## iOS research grounding

- Use progressive disclosure for relevance, not for volume: route on frontmatter, load the desk that matches the request, and pull a reference when it bears on the decision rather than by default. Context is not the scarce resource; ambiguity is.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
