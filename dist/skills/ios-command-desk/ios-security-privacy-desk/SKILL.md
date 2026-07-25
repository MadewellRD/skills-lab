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

**Outcome.** An iOS security and privacy assessment with explicit gates: data collected and shared, permissions and their usage-description strings, third-party SDKs and dependency risk, auth and session risk, Keychain and secure storage, network security, logging, URL scheme and universal-link controls, App Review policy and privacy-label mapping, user consent, abuse, anti-tamper and game-economy risks where relevant, and the release gates that follow.

**Grounding.** Work from manifest and Info.plist files, dependency files, auth and API docs, the data inventory, App Review policy notes, the privacy policy, security findings, app/game design, and the telemetry plan. Ground every privacy and App Review policy claim in source evidence, and map each privacy-label claim to the implementation evidence and the user-facing disclosure that supports it. Do not invent permissions, privacy labels, App Review policy obligations, auth, storage, network, dependency, or release facts.

**Compliance constraints — requirements, not guidance.** Every requested permission must have a named justification, a usage-description string, and a code path that requires it. Every data type in the App Store privacy label must match what the app actually collects, shares, and transmits, and the privacy manifest must declare the app's and each bundled SDK's collected data types, tracking domains, and required-reason API usage. Policy-sensitive surfaces — monetization, ads and tracking, child-directed content, health, financial, location, and game economy — carry their own App Review policy obligations, and those obligations are stated in the artifact whether or not the current implementation satisfies them.

**Parallel surface.** Individual permissions, third-party SDKs, URL schemes, universal links, network security settings, and dependency findings are independent review items: review them in parallel. The privacy-label mapping, the privacy manifest, and the user-facing disclosure are aggregate and must stay internally consistent across every item, so assemble them once, after the per-item review.

**Acceptance bar.** The review is complete when every requested permission is justified against a code path and a usage-description string or flagged as unjustified; every privacy-label and privacy-manifest claim traces to implementation evidence or is marked unverified; third-party SDKs are enumerated with what each collects or marked unknown; each policy-sensitive surface is either cleared against a cited policy or raised as a gate; and each finding carries a severity and an explicit pass, waive-with-rationale, or halt disposition.

Continue to performance, testing, or release when risks are passed, waived, or halted.

## Responsibilities

- Protect users and repo truth over speed.
- Ground privacy and App Review policy claims in source evidence.
- Identify app/game abuse, cheating, economy fraud, payment abuse, insecure local storage, exported component, and network risks.
- Escalate missing production credentials, signing, policy, or privacy-label facts.

## Expected inputs

Manifest files, dependency files, auth/API docs, data inventory, App Review policy notes, privacy policy, security findings, app/game design, telemetry plan, and prior `ios_delivery_packet`.

## Expected outputs

A complete run delivers the assessment whole: the security and privacy review, the threat notes, the privacy-label and privacy-manifest mapping, the permission review, the risk register, the release gates with their dispositions, any halt conditions, and the packet update. A permission review with no privacy-label mapping downstream of it, or release gates with no findings behind them, cannot support an App Review submission decision, so the set is the unit of work.

Depth is measured by whether a reviewer could accept or reject the submission from the artifact alone. Every requested permission appears with its named justification, its usage-description string, and the code path that requires it, or is flagged unjustified; every data type in the privacy label is matched to implementation evidence and the user-facing disclosure behind it; the privacy manifest covers the app's and each bundled SDK's collected data types, tracking domains, and required-reason API usage; every SDK is enumerated with what it collects or marked unknown; every finding carries a severity and an explicit pass, waive-with-rationale, or halt disposition. The compliance constraints in Workflow are requirements, and no artifact reports a gate as passed on their behalf.

This is precisely where completing the set would do the most harm if it meant guessing. A permission justification, a collected data type, an SDK behaviour, a required-reason API, or an App Review obligation that no source establishes is reported as unverified or unassessed with the artifact needed to settle it — never written in so the declaration reads as finished. A privacy label or manifest assembled from plausible content is a false statement to Apple and to users, not a tidy-up. Per-permission, per-SDK, per-scheme, per-link, and per-dependency review are independent items within the parallel surface declared in Workflow.

## Evidence packet additions

- permissions and data collected/shared
- third-party SDKs and dependency risks
- auth/session, storage, network, logging, and exported/deep-link controls
- App Review policy and privacy-label gates
- abuse, anti-tamper, game economy, or fraud risks where relevant

## Packet fields to update

`security_controls`, `privacy_requirements`, `permissions`, `data_safety`, `dependency_risks`, `secrets`, `storage_security`, `network_security`, `abuse_controls`, `release_gates`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default on assessment work: an unreviewed area is recorded as unassessed with its risk named, not turned into a stop. Security and privacy conclusions are different — declaring a surface clear is itself a consequence-bearing act. Reserve hard halts for these consequence classes:

- **Approval** — a risk acceptance, policy waiver, or data-handling decision requires a human owner to authorize it.
- **Production or destructive** — the request would change production security configuration, rotate or publish signing certificates or keys, or alter a live privacy label or privacy manifest.
- **Security or privacy** — the work requires handling secrets, keys, or personal data without safe instructions, or would expose them in an artifact.
- **Source conflict** — Info.plist, the privacy manifest, the data inventory, and the privacy policy genuinely disagree about what is collected or shared. Preserve the conflict: a privacy label cannot be assembled from a guess.
- **Release integrity** — a security, privacy, permissions, or App Review policy gate would be reported as passed while its evidence is missing, or policy-sensitive monetization, ads, child-directed, health, financial, location, or game economy behavior is unresolved for release work.
- **Connector unreachable** — a manifest, dependency file, or policy source exists but cannot be read.

Otherwise proceed: Info.plist, URL scheme, universal-link, or auth risks that cannot be assessed from available evidence are recorded as unassessed with the artifact needed to assess them, and the review continues across the areas that can be assessed.

## Default output modes

The set a complete run writes:

- `ios-security-privacy-review.md`
- `ios-permission-privacy-label-map.md`
- `ios-threat-notes.md`

Mode-specific alternatives — each replaces a clean disposition rather than adding to it:

- `ios-policy-halt.md` — when an App Review policy, privacy-label, or privacy-manifest obligation blocks the release gate and that gate cannot be reported as passed or waived.
- `workflow-halt.md` — when a hard halt fires for any other consequence class.

No file here is completed with claimed permission, data-type, tracking-domain, required-reason API, or App Review content. An entry the evidence does not support is written as unverified or unassessed — a declaration filled in to look finished is a false statement to Apple and to users.

## Downstream handoff

Continue to `ios-performance-optimization-desk` or `ios-testing-qa-desk` after security/privacy gates are explicit.

## SDLC suite handoff

Use `security-threat-desk`, `verification-desk`, `test-strategy-desk`, and release desks when iOS security or privacy work needs generic lifecycle support.

## iOS research grounding

- Use progressive disclosure for relevance, not for volume: route on frontmatter, load the desk that matches the request, and pull a reference when it bears on the decision rather than by default. Context is not the scarce resource; ambiguity is.
- For app work, account for Swift, SwiftUI, SwiftData/Core Data, App Intents, widgets, StoreKit, accessibility, privacy labels, TestFlight, and App Review.
- For game work, account for SpriteKit, SceneKit, Metal, MetalFX, Game Center, StoreKit, controller input, asset delivery, frame budget, thermal behavior, and live ops.
- Default to instruction-only execution unless a reviewed deterministic script creates clear value.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
