---
name: android-security-privacy-desk
description: review Android security, privacy, permissions, secrets, Play policy risk, data safety, secure storage, anti-tamper, networking, dependency risk, and abuse controls.
---

# Android Security Privacy Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. Complete this desk's artifact, update the `android_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing permissions, data safety, Play policy, auth, storage, network, dependency, or release facts.

## Role

Assess Android security and privacy before implementation or release: permissions, secrets, secure storage, network security, auth/session risk, dependency risk, data safety, Play policy, abuse controls, anti-tamper needs, logging, and user consent.

## Workflow

1. Resolve data collected, permissions, SDKs, third parties, auth model, storage, networking, logging, and policy obligations.
2. Review manifest permissions, exported components, deep links, network security config, secrets, logs, and dependency risk where source facts exist.
3. Map privacy/data-safety claims to implementation evidence and user-facing disclosures.
4. Define security acceptance gates, tests, review items, and halt conditions.
5. Continue to performance, testing, or release when risks are passed, waived, or halted.

## Responsibilities

- Protect users and repo truth over speed.
- Ground privacy and Play policy claims in source evidence.
- Identify app/game abuse, cheating, economy fraud, payment abuse, insecure local storage, exported component, and network risks.
- Escalate missing production credentials, signing, policy, or data-safety facts.

## Expected inputs

Manifest files, dependency files, auth/API docs, data inventory, Play policy notes, privacy policy, security findings, app/game design, telemetry plan, and prior `android_delivery_packet`.

## Expected outputs

Security/privacy review, threat notes, data-safety mapping, permission review, risk register, release gates, halt conditions, and packet update.

## Evidence packet additions

- permissions and data collected/shared
- third-party SDKs and dependency risks
- auth/session, storage, network, logging, and exported/deep-link controls
- Play policy and data-safety gates
- abuse, anti-tamper, game economy, or fraud risks where relevant

## Packet fields to update

`security_controls`, `privacy_requirements`, `permissions`, `data_safety`, `dependency_risks`, `secrets`, `storage_security`, `network_security`, `abuse_controls`, `release_gates`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

- Data safety or privacy facts are missing for release work.
- Requested work requires handling secrets without safe instructions.
- Manifest/exported/auth risks cannot be assessed from available evidence.
- Policy-sensitive monetization, ads, child-directed, health, financial, location, or game economy behavior is unresolved.

## Default output modes

- `android-security-privacy-review.md`
- `android-permission-data-safety-map.md`
- `android-threat-notes.md`
- `android-policy-halt.md`
- `workflow-halt.md`

## Downstream handoff

Continue to `android-performance-optimization-desk` or `android-testing-qa-desk` after security/privacy gates are explicit.

## SDLC suite handoff

Use `security-threat-desk`, `verification-desk`, `test-strategy-desk`, and release desks when Android security or privacy work needs generic lifecycle support.
