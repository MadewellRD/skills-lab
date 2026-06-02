# iOS Command Desk

Status: source-complete iOS app/game command desk suite. Dist packages are generated intentionally through `tools/generate_ios_command_desk_release.py` when a release candidate is prepared.

This folder contains ChatGPT skill-compatible Markdown source desks for the iOS Command Desk suite. The suite keeps the existing Skills-Lab mobile taxonomy: one iOS orchestrator plus thirteen specialist desks covering product, discovery, architecture, UI/UX, app engineering, game engineering, backend integration, security/privacy, performance, testing, release/store ops, observability/live ops, and maintenance/growth.

## Coverage

The suite covers both:

- iOS app development
- iOS game development

Use SDLC Command Desk patterns for generic lifecycle controls: requirements, discovery, architecture, issue planning, implementation handoff, review, testing, verification, security, release, deployment, observability, incident response, maintenance, retrospective, and decommissioning.

## Research-grounded design rules

- Keep iOS as an umbrella orchestrator with narrow app/game stages; do not collapse everything into one giant iOS prompt.
- Prefer curated, source-grounded desk contracts over self-generated or over-broad skills.
- Use progressive disclosure: short frontmatter descriptions for routing, full desk instructions only on activation, and references loaded only when needed.
- Prefer GitHub, Xcode, xcodebuild, simulators, CI, TestFlight, App Store Connect, Instruments, MetricKit, and source evidence over GUI guessing.
- For app work, default to modern iOS baselines when repo facts support them: Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, Swift Testing/XCTest, previews, accessibility, and privacy-label review.
- For game work, preserve separate SpriteKit/SceneKit/Metal/MetalFX and engine-integration lanes for Unity, Unreal, Godot, custom engines, Game Center, StoreKit, controller input, frame pacing, and device-tier performance.

## Desk inventory

| Order | Desk | Role |
|---:|---|---|
| 000 | `000-ios-command-desk` | iOS app/game workflow orchestrator |
| 001 | `001-ios-product-requirements-desk` | iOS app/game requirements and acceptance gates |
| 002 | `002-ios-technical-discovery-desk` | Repo, toolchain, device, engine, and feasibility discovery |
| 003 | `003-ios-architecture-design-desk` | iOS architecture, modules, services, and ADR decisions |
| 004 | `004-ios-ui-ux-desk` | iOS UI/UX, Human Interface Guidelines, accessibility, and inputs |
| 005 | `005-ios-app-engineering-desk` | Native iOS app implementation planning |
| 006 | `006-ios-game-engineering-desk` | iOS game implementation and engine planning |
| 007 | `007-ios-backend-integration-desk` | APIs, auth, sync, push, payments, multiplayer, and cloud saves |
| 008 | `008-ios-security-privacy-desk` | Security, privacy, permissions, entitlements, App Review policy, and abuse controls |
| 009 | `009-ios-performance-optimization-desk` | Startup, memory, battery, main-thread stalls, rendering, Metal, frame pacing, and thermal behavior |
| 010 | `010-ios-testing-qa-desk` | Swift Testing, XCTest, XCUITest, simulator/device, gameplay, and release QA |
| 011 | `011-ios-release-app-store-ops-desk` | Builds, signing, TestFlight, App Store Connect, phased rollout, and rollback |
| 012 | `012-ios-observability-liveops-desk` | Crash reporting, analytics, remote config, alerts, and live ops |
| 013 | `013-ios-maintenance-growth-desk` | SDK updates, policy changes, experiments, monetization, and debt |

## References

- `references/desk-workflows/ios-command-desk.md`
- `references/desk-workflows/ios-delivery-packet.md`
- `references/platform/ios-app-baseline.md`
- `references/platform/ios-game-baseline.md`
- `references/platform/ios-low-token-policy.md`

## Authoring convention

- Suite folders are human-readable product taxonomy.
- Desk files are ordered kebab-case and end in `.md`.
- Source desks use ChatGPT skill-compatible front matter.
- Packaged ChatGPT skill folders are generated artifacts, not the primary authoring structure.
- Keep `dist/` package artifacts untouched until packaging is intentionally requested.
