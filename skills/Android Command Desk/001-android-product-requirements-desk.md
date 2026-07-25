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

**Outcome.** A source-grounded Android PRD: requirement IDs, target users, supported devices and OS/API range, app/game surface and lane, monetization assumptions, Play/store constraints, acceptance criteria, non-goals, risks, and open questions.

**Grounding.** Draw facts from issues, uploaded docs, user statements, product docs, design and game docs, store constraints, telemetry, and repo evidence. Attribute every load-bearing fact to its source and keep verified fact, assumption, and inference separate. Do not invent target users, device support, API levels, monetization terms, Play policy obligations, or release dates.

**Constraints.** Acceptance criteria must be checkable on Android devices, emulators, CI, benchmark output, or release gates, or be marked explicitly non-automatable. Non-goals, out-of-scope platforms, privacy and policy constraints, and rollout constraints are stated, not implied.

**Parallel surface.** Source retrieval across independent inputs, issues, uploaded docs, product docs, design and game docs, telemetry, repo evidence, has no ordering dependency, and acceptance criteria for distinct requirement IDs are independent of one another. Fan out over both. The risk register and the non-goals list are aggregate: assemble them once the per-requirement work is complete.

**Acceptance bar.** The PRD is done when every requirement carries a stable ID; each requirement has acceptance criteria testable without further product input; the app/game lane and target surface are stated; supported devices and OS/API range are either sourced or labeled as assumptions; non-goals, risks, and open questions are explicit rather than implied; and every load-bearing fact is attributed to its source.

Continue to `android-technical-discovery-desk` when requirements are clear enough to inspect implementation reality.

## Responsibilities

- Produce Android-specific PRD sections with requirement IDs and acceptance gates.
- Capture device/API/support assumptions without inventing target versions.
- Separate app user value, game loop value, monetization, Play policy, store listing, and operational requirements.
- Make each acceptance criterion testable or explicitly non-automatable.

## Expected inputs

Product brief, user story, GitHub issue, roadmap item, uploaded research, design/game notes, analytics/feedback, store constraints, or prior `android_delivery_packet`.

## Expected outputs

A complete run delivers the whole requirements package together, not one piece of it per turn: the Android PRD, the acceptance criteria, the non-goals, the risk register, the open-questions list, the source-fact summary, and the `android_delivery_packet` update. These are facets of one requirements decision and are only usable together; acceptance criteria detached from their requirement IDs, or a risk register without the non-goals that bound it, sends the reader back for another round.

Each piece is finished when a product owner or an Android engineer could act on it without a follow-up question: every requirement carries a stable ID and criteria checkable on a device, emulator, CI, benchmark output, or release gate; every risk names its trigger and its impact; every open question names who can answer it. A heading with a placeholder under it is an unfinished artifact, not a draft.

Delivering the full set is never a reason to fill a piece in. Where the sources establish nothing about monetization, device support, or a Play policy obligation, that piece is reported as not-applicable or blocked with the missing source named, never populated with a plausible-sounding requirement. The independent pieces above are part of the parallel surface declared in Workflow.

## Evidence packet additions

- requirement IDs and acceptance gates
- target app/game surface and lane
- audience, supported devices, OS/API assumptions
- monetization and Play/store constraints
- non-goals, risks, and open questions

## Packet fields to update

`business_goal`, `audience_segments`, `target_surface`, `app_or_game_lane`, `supported_devices`, `min_sdk`, `target_sdk`, `monetization`, `play_policy_constraints`, `acceptance_gates`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default. An unresolved product detail is normally an open question plus a labeled working assumption, not a stop. Reserve hard halts for these consequence classes:

- **Approval**: scope, monetization, or a policy commitment needs a human owner to authorize it.
- **Production or destructive**: the request would write requirements into a live tracker, roadmap, or customer-facing commitment.
- **Security or privacy**: requirements would encode handling of personal data, secrets, or a child-directed, health, or financial obligation that no source establishes.
- **Source conflict**: product docs, issues, or stakeholder statements genuinely disagree on a load-bearing requirement. Preserve the conflict rather than resolving it silently.
- **Release integrity**: acceptance criteria would be presented as agreed, or a device/OS support range as committed, when no source establishes it.
- **Connector unreachable**: a required source exists but cannot be read. A merely absent source is a soft gap: continue with a labeled assumption.

Otherwise proceed: an unresolved goal, audience, app/game lane, device or API range, monetization assumption, or policy constraint is recorded as an open question alongside the assumption used in its place.

## Default output modes

A complete run writes all of these:

- `android-prd.md`
- `android-acceptance-gates.md`
- `android-risk-register.md`
- `android-product-open-questions.md`

Mode-specific alternative:

- `workflow-halt.md`: replaces the set above when a hard halt fires. It is not a fifth file appended to a finished run.

Any file in the set with no source basis is written as a short not-applicable note naming the missing source, rather than a document filled out until it looks complete.

## Downstream handoff

Continue to `android-technical-discovery-desk` unless the user explicitly requested only requirements.

## SDLC suite handoff

Use `product-requirements-desk` patterns for requirement IDs, acceptance criteria, non-goals, risks, and open questions while preserving Android-specific platform facts for downstream desks.
