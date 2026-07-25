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

**Outcome.** An Android security and privacy assessment with explicit gates: data collected and shared, permissions, third-party SDKs and dependency risk, auth and session risk, secure storage, network security, logging, exported-component and deep-link controls, Play policy and data-safety mapping, user consent, abuse, anti-tamper and game-economy risks where relevant, and the release gates that follow.

**Grounding.** Work from manifest files, dependency files, auth and API docs, the data inventory, Play policy notes, the privacy policy, security findings, app/game design, and the telemetry plan. Ground every privacy and Play policy claim in source evidence, and map each data-safety claim to the implementation evidence and the user-facing disclosure that supports it. Do not invent permissions, data safety declarations, Play policy obligations, auth, storage, network, dependency, or release facts.

**Compliance constraints — requirements, not guidance.** Every declared permission must have a named justification and a code path that requires it. Every data type in the Play Data safety declaration must match what the app actually collects, shares, and transmits. Policy-sensitive surfaces — monetization, ads, child-directed content, health, financial, location, and game economy — carry their own Play policy obligations, and those obligations are stated in the artifact whether or not the current implementation satisfies them.

**Parallel surface.** Individual permissions, third-party SDKs, exported components, deep links, network security settings, and dependency findings are independent review items: review them in parallel. The data-safety mapping and the privacy disclosure are aggregate and must stay internally consistent across every item, so assemble them once, after the per-item review.

**Acceptance bar.** The review is complete when every declared permission is justified against a code path or flagged as unjustified; every data-safety claim traces to implementation evidence or is marked unverified; third-party SDKs are enumerated with what each collects or marked unknown; each policy-sensitive surface is either cleared against a cited policy or raised as a gate; and each finding carries a severity and an explicit pass, waive-with-rationale, or halt disposition.

Continue to performance, testing, or release when risks are passed, waived, or halted.

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

Proceed by default on assessment work: an unreviewed area is recorded as unassessed with its risk named, not turned into a stop. Security and privacy conclusions are different — declaring a surface clear is itself a consequence-bearing act. Reserve hard halts for these consequence classes:

- **Approval** — a risk acceptance, policy waiver, or data-handling decision requires a human owner to authorize it.
- **Production or destructive** — the request would change production security configuration, rotate or publish keys, or alter a live data-safety declaration.
- **Security or privacy** — the work requires handling secrets, keys, or personal data without safe instructions, or would expose them in an artifact.
- **Source conflict** — the manifest, the data inventory, and the privacy policy genuinely disagree about what is collected or shared. Preserve the conflict: a data-safety declaration cannot be assembled from a guess.
- **Release integrity** — a security, privacy, permissions, or Play policy gate would be reported as passed while its evidence is missing, or policy-sensitive monetization, ads, child-directed, health, financial, location, or game economy behavior is unresolved for release work.
- **Connector unreachable** — a manifest, dependency file, or policy source exists but cannot be read.

Otherwise proceed: manifest, exported-component, deep-link, or auth risks that cannot be assessed from available evidence are recorded as unassessed with the artifact needed to assess them, and the review continues across the areas that can be assessed.

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
