# Android Command Desk

Status: source-complete Android app/game command desk suite. Dist packages are generated intentionally through `tools/generate_android_command_desk_release.py` when a release candidate is prepared.

This folder contains ChatGPT skill-compatible Markdown source desks for the Android Command Desk suite. The suite keeps the existing Skills-Lab mobile taxonomy: one Android orchestrator plus thirteen specialist desks covering product, discovery, architecture, UI/UX, app engineering, game engineering, backend integration, security/privacy, performance, testing, release/store ops, observability/live ops, and maintenance/growth.

## Coverage

The suite covers both:

- Android app development
- Android game development

Use SDLC Command Desk patterns for generic lifecycle controls: requirements, discovery, architecture, issue planning, implementation handoff, review, testing, verification, security, release, deployment, observability, incident response, maintenance, retrospective, and decommissioning.

## Research-grounded design rules

- Keep Android as an umbrella orchestrator with narrow app/game stages; do not collapse everything into one giant Android prompt.
- Prefer curated, source-grounded desk contracts over self-generated or over-broad skills.
- Use progressive disclosure: short frontmatter descriptions for routing, full desk instructions only on activation, and references loaded only when needed.
- Prefer GitHub, Gradle, adb, emulator, CI, benchmark, and Play workflow evidence over GUI guessing.
- For app work, default to modern Android baselines when repo facts support them: Kotlin, Jetpack Compose, modularization, DI, screenshot/UI testing, Macrobenchmark, and Baseline Profiles.
- For game work, preserve separate native/AGDK/NDK and engine-integration lanes for Unity, Unreal, Godot, custom engines, Play Asset Delivery, Android GPU Inspector, frame pacing, and device-tier performance.

## Desk inventory

| Order | Desk | Role |
|---:|---|---|
| 000 | `000-android-command-desk` | Android app/game workflow orchestrator |
| 001 | `001-android-product-requirements-desk` | Android app/game requirements and acceptance gates |
| 002 | `002-android-technical-discovery-desk` | Repo, toolchain, device, engine, and feasibility discovery |
| 003 | `003-android-architecture-design-desk` | Android architecture, modules, services, and ADR decisions |
| 004 | `004-android-ui-ux-desk` | Android UI/UX, Material design, accessibility, and inputs |
| 005 | `005-android-app-engineering-desk` | Native Android app implementation planning |
| 006 | `006-android-game-engineering-desk` | Android game implementation and engine planning |
| 007 | `007-android-backend-integration-desk` | APIs, auth, sync, push, payments, multiplayer, and cloud saves |
| 008 | `008-android-security-privacy-desk` | Security, privacy, permissions, Play policy, and abuse controls |
| 009 | `009-android-performance-optimization-desk` | Startup, memory, battery, ANR, rendering, and frame pacing |
| 010 | `010-android-testing-qa-desk` | Unit, instrumented, UI, device, gameplay, and release QA |
| 011 | `011-android-release-store-ops-desk` | Builds, signing, Play tracks, staged rollout, and rollback |
| 012 | `012-android-observability-liveops-desk` | Crash reporting, analytics, remote config, alerts, and live ops |
| 013 | `013-android-maintenance-growth-desk` | SDK updates, policy changes, experiments, monetization, and debt |

## References

- `references/desk-workflows/android-command-desk.md`
- `references/desk-workflows/android-delivery-packet.md`
- `references/platform/android-app-baseline.md`
- `references/platform/android-game-baseline.md`
- `references/platform/android-low-token-policy.md`

## Authoring convention

- Suite folders are human-readable product taxonomy.
- Desk files are ordered kebab-case and end in `.md`.
- Source desks use ChatGPT skill-compatible front matter.
- Packaged ChatGPT skill folders are generated artifacts, not the primary authoring structure.
- Keep `dist/` package artifacts untouched until packaging is intentionally requested.
