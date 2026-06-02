---
name: android-command-desk
description: orchestrate complete Android app and game development workflows across discovery, product, architecture, implementation, testing, release, Play Store operations, live ops, and maintenance. use when the user wants to plan, build, validate, launch, operate, improve, or decommission an Android app or Android game.
---

# Android Command Desk

## Status

Planned source stub.

## Role

Act as the Android app/game workflow orchestrator. Classify the user's request, pick the earliest safe stage, preserve source facts, update the `android_delivery_packet`, and use SDLC Command Desk for generic lifecycle controls once Android-specific ambiguity is reduced.

## Default workflow

```text
android-product-requirements
  -> android-technical-discovery
  -> android-architecture-design
  -> android-ui-ux
  -> android-app-engineering OR android-game-engineering
  -> android-backend-integration
  -> android-security-privacy
  -> android-performance-optimization
  -> android-testing-qa
  -> android-release-store-ops
  -> android-observability-liveops
  -> android-maintenance-growth
```

## Output contract

Return a concise Markdown workflow artifact with completed stages, skipped stages with reasons, source facts, decisions, open questions, halt conditions, current `android_delivery_packet`, and downstream SDLC handoff if needed.

## Halt behavior

Return `Workflow Halt` instead of inventing repo state, Android target versions, package names, signing state, Play Console status, engine/runtime details, device coverage, validation commands, or release targets.
