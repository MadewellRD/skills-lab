# Android Command Desk

Status: planned suite scaffold.

This folder contains `.md` source stubs for the Android Command Desk suite. This is a source-only scaffold; no generated `dist/` packages are included yet.

## Coverage

The suite covers both:

- Android app development
- Android game development

Use SDLC Command Desk patterns for generic lifecycle controls: requirements, discovery, architecture, issue planning, implementation handoff, review, testing, verification, security, release, deployment, observability, incident response, maintenance, retrospective, and decommissioning.

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

## Authoring convention

- Suite folders are human-readable product taxonomy.
- Desk files are ordered kebab-case and end in `.md`.
- Source desks use ChatGPT skill-compatible front matter where possible.
- Packaged ChatGPT skill folders are generated artifacts, not the primary authoring structure.
- Keep `dist/` untouched until packaging is intentionally requested.
