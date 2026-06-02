# Android Command Desk Workflow Reference

## Workflow mode
Use this reference when authoring or reviewing `000-android-command-desk.md` or its packaged `SKILL.md`.

## Stage execution
1. Resolve the requested outcome, workflow mode, target Android surface, and app/game lane.
2. Resolve source facts from GitHub, uploaded files, product/design docs, Android repo files, CI, Gradle, adb/emulator output, benchmark reports, Play/release notes, or live-ops telemetry.
3. Produce the stage output using only grounded facts plus labeled assumptions.
4. Preserve the Android delivery packet.
5. Continue downstream only when evidence is sufficient and approvals are not blocking.

## Required evidence
- target app/game surface, repo, branch, and source scope
- Android build facts: Gradle, modules, SDK/NDK, language/runtime, dependencies, and CI/test commands
- product, design, policy, performance, security, release, and telemetry constraints relevant to the requested outcome
- explicit approval for writes, publishing, external shares, Play Console actions, or production-impacting operations

## Outputs
- Android workflow plan
- stage sequence
- source fact summary
- decision and approval log
- deliverables or drafts
- downstream SDLC or coding-agent handoff packet

## Halt conditions
- target surface, app/game lane, repo, branch, or release target cannot be resolved
- required connector access is missing
- sources conflict on SDK, engine/runtime, module ownership, signing, Play track, validation state, or production telemetry
- a write, publish, external share, release, rollout, rollback, or store operation requires approval

## Downstream handoffs
- android-product-requirements-desk
- android-technical-discovery-desk
- android-architecture-design-desk
- android-ui-ux-desk
- android-app-engineering-desk
- android-game-engineering-desk
- android-backend-integration-desk
- android-security-privacy-desk
- android-performance-optimization-desk
- android-testing-qa-desk
- android-release-store-ops-desk
- android-observability-liveops-desk
- android-maintenance-growth-desk
