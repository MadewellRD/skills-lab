---
name: ios-security-privacy-desk
description: review iOS security, privacy, permissions, secrets, App Review policy risk, privacy labels, secure storage, anti-tamper, networking, dependency risk, and abuse controls.
---

# iOS Security Privacy Desk

## Suite workflow mode

This desk is part of the iOS Command Desk workflow suite. Complete this desk's artifact, update the `ios_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing permissions, privacy labels, App Review policy, auth, storage, network, dependency, or release facts.

## Role

Assess iOS security and privacy before implementation or release: permissions, secrets, secure storage, network security, auth/session risk, dependency risk, privacy labels, App Review policy, abuse controls, anti-tamper needs, logging, and user consent.

## Workflow

1. Resolve data collected, permissions, SDKs, third parties, auth model, storage, networking, logging, and policy obligations.
2. Review manifest permissions, exported components, deep links, network security config, secrets, logs, and dependency risk where source facts exist.
3. Map privacy/privacy-label claims to implementation evidence and user-facing disclosures.
4. Define security acceptance gates, tests, review items, and halt conditions.
5. Continue to performance, testing, or release when risks are passed, waived, or halted.

## Responsibilities

- Protect users and repo truth over speed.
- Ground privacy and App Review policy claims in source evidence.
- Identify app/game abuse, cheating, economy fraud, payment abuse, insecure local storage, exported component, and network risks.
- Escalate missing production credentials, signing, policy, or privacy-label facts.

## Expected inputs

Manifest files, dependency files, auth/API docs, data inventory, App Review policy notes, privacy policy, security findings, app/game design, telemetry plan, and prior `ios_delivery_packet`.

## Expected outputs

Security/privacy review, threat notes, privacy-label mapping, permission review, risk register, release gates, halt conditions, and packet update.

## Evidence packet additions

- permissions and data collected/shared
- third-party SDKs and dependency risks
- auth/session, storage, network, logging, and exported/deep-link controls
- App Review policy and privacy-label gates
- abuse, anti-tamper, game economy, or fraud risks where relevant

## Packet fields to update

`security_controls`, `privacy_requirements`, `permissions`, `data_safety`, `dependency_risks`, `secrets`, `storage_security`, `network_security`, `abuse_controls`, `release_gates`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

- Data safety or privacy facts are missing for release work.
- Requested work requires handling secrets without safe instructions.
- Manifest/exported/auth risks cannot be assessed from available evidence.
- Policy-sensitive monetization, ads, child-directed, health, financial, location, or game economy behavior is unresolved.

## Default output modes

- `ios-security-privacy-review.md`
- `ios-permission-privacy-label-map.md`
- `ios-threat-notes.md`
- `ios-policy-halt.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `ios-performance-optimization-desk` or `ios-testing-qa-desk` after security/privacy gates are explicit.

## SDLC suite handoff

Use `security-threat-desk`, `verification-desk`, `test-strategy-desk`, and release desks when iOS security or privacy work needs generic lifecycle support.

## iOS research grounding

- Use progressive disclosure: keep routing metadata short, active desk instructions bounded, and references cold until needed.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.
