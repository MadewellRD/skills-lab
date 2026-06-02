# iOS Command Desk

Status: planned suite scaffold.

This folder contains `.md` source stubs for the iOS Command Desk suite. This is a source-only scaffold; no generated `dist/` packages are included yet.

## Coverage

The suite covers both:

- iOS app development
- iOS game development

Use SDLC Command Desk patterns for generic lifecycle controls: requirements, discovery, architecture, issue planning, implementation handoff, review, testing, verification, security, release, deployment, observability, incident response, maintenance, retrospective, and decommissioning.

## Desk inventory

| Order | Desk | Role |
|---:|---|---|
| 000 | `000-ios-command-desk` | iOS app/game workflow orchestrator |
| 001 | `001-ios-product-requirements-desk` | iOS app/game requirements and acceptance gates |
| 002 | `002-ios-technical-discovery-desk` | Repo, toolchain, device, engine, and feasibility discovery |
| 003 | `003-ios-architecture-design-desk` | iOS architecture, modules, services, and ADR decisions |
| 004 | `004-ios-ui-ux-desk` | iOS UI/UX, HIG, accessibility, and inputs |
| 005 | `005-ios-app-engineering-desk` | Native iOS app implementation planning |
| 006 | `006-ios-game-engineering-desk` | iOS game implementation and engine planning |
| 007 | `007-ios-backend-integration-desk` | APIs, auth, sync, IAP, push, multiplayer, and cloud saves |
| 008 | `008-ios-security-privacy-desk` | Security, privacy, entitlements, App Store policy, and abuse controls |
| 009 | `009-ios-performance-optimization-desk` | Launch, memory, battery, crash risk, rendering, and frame pacing |
| 010 | `010-ios-testing-qa-desk` | Unit, UI, simulator/device, TestFlight, gameplay, and release QA |
| 011 | `011-ios-release-app-store-ops-desk` | Signing, provisioning, TestFlight, submission, phased release, and rollback |
| 012 | `012-ios-observability-liveops-desk` | Crash reporting, analytics, remote config, alerts, and live ops |
| 013 | `013-ios-maintenance-growth-desk` | Xcode/SDK updates, policy changes, experiments, monetization, and debt |

## Authoring convention

- Suite folders are human-readable product taxonomy.
- Desk files are ordered kebab-case and end in `.md`.
- Source desks use ChatGPT skill-compatible front matter where possible.
- Packaged ChatGPT skill folders are generated artifacts, not the primary authoring structure.
- Keep `dist/` untouched until packaging is intentionally requested.
