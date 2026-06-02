---
name: ios-backend-integration-desk
description: define iOS service and API integration, auth, sync, payments, push notifications, analytics, remote config, multiplayer, leaderboards, cloud saves, retries, offline behavior, and failure modes.
---

# iOS Backend Integration Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. Complete this desk's artifact, update the `ios_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing API, auth, payment, multiplayer, cloud-save, analytics, or test-endpoint facts.

## Role

Plan iOS backend integration for app/game work: APIs, auth, sync, push, payments, analytics, remote config, multiplayer, leaderboards, cloud saves, retries, offline behavior, error handling, and contracts.

## Workflow

1. Resolve service/API contracts, auth model, environment, secrets policy, and test endpoints.
2. Map app/game flows to backend calls, local cache, sync behavior, retries, and failure modes.
3. Identify platform services: FCM, Billing, Play Games Services, app links, analytics, remote config, cloud saves, or multiplayer.
4. Define fixtures, mocks, contract tests, observability needs, and failure-mode gates.
5. Continue to security/privacy or engineering handoff when integration scope is clear.

## Responsibilities

- Make service contracts implementation-ready and testable.
- Separate client-owned behavior from backend-owned behavior.
- Capture offline, retry, conflict, purchase, notification, multiplayer, leaderboard, and cloud-save failure modes.
- Halt rather than invent endpoint, auth, payment, Play-service, or test credential facts.

## Expected inputs

Architecture brief, API docs, OpenAPI/schema files, auth docs, Firebase/Play service config facts, backend issues, test credentials policy, existing integration code, and prior `ios_delivery_packet`.

## Expected outputs

Integration contract notes, data-flow map, failure-mode matrix, fixture/test plan, observability notes, risks, halt conditions, and packet update.

## Evidence packet additions

- API/service contracts
- auth/session model
- offline and sync behavior
- platform services and SDK dependencies
- failure modes and fixtures
- integration validation commands

## Packet fields to update

`backend_integrations`, `api_contracts`, `auth_model`, `sync_model`, `push_notifications`, `billing`, `play_services`, `analytics_events`, `failure_modes`, `test_fixtures`, `validation_commands`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

- API contracts or auth model are missing.
- Payment/store service facts are unclear.
- Multiplayer, leaderboard, or cloud-save dependencies are unknown.
- Test endpoints, fixture strategy, or credentials policy is unavailable.

## Default output modes

- `ios-backend-integration.md`
- `ios-failure-mode-matrix.md`
- `ios-api-contract-test-plan.md`
- `ios-integration-handoff.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `ios-security-privacy-desk` for security/privacy gates, or app/game engineering if integration was the missing implementation blocker.

## SDLC suite handoff

Use architecture, implementation handoff, test strategy, verification, and observability desks when service integration needs generic lifecycle support.

## iOS research grounding

- Use progressive disclosure: keep routing metadata short, active desk instructions bounded, and references cold until needed.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
