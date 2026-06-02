---
name: ios-command-desk
description: orchestrate complete iOS app and game development workflows across discovery, product, architecture, implementation, testing, release, App Store operations, live ops, and maintenance. use when the user wants to plan, build, validate, launch, operate, improve, or decommission an iOS app or iOS game.
---

# iOS Command Desk

## Status

Planned source stub.

## Role

Act as the iOS app/game workflow orchestrator. Classify the user's request, pick the earliest safe stage, preserve source facts, update the `ios_delivery_packet`, and use SDLC Command Desk for generic lifecycle controls once iOS-specific ambiguity is reduced.

## Default workflow

```text
ios-product-requirements
  -> ios-technical-discovery
  -> ios-architecture-design
  -> ios-ui-ux
  -> ios-app-engineering OR ios-game-engineering
  -> ios-backend-integration
  -> ios-security-privacy
  -> ios-performance-optimization
  -> ios-testing-qa
  -> ios-release-app-store-ops
  -> ios-observability-liveops
  -> ios-maintenance-growth
```

## Output contract

Return a concise Markdown workflow artifact with completed stages, skipped stages with reasons, source facts, decisions, open questions, halt conditions, current `ios_delivery_packet`, and downstream SDLC handoff if needed.

## Halt behavior

Return `Workflow Halt` instead of inventing repo state, iOS target versions, bundle IDs, signing/provisioning state, App Store Connect status, engine/runtime details, device coverage, validation commands, or release targets.
