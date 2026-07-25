---
name: android-backend-integration-desk
description: define Android service and API integration, auth, sync, payments, push notifications, analytics, remote config, multiplayer, leaderboards, cloud saves, retries, offline behavior, and failure modes.
---

# Android Backend Integration Desk

## Suite workflow mode

This desk is part of the Android Command Desk workflow suite. Complete this desk's artifact, update the `android_delivery_packet`, and continue when enough source facts are available. Return `Workflow Halt` instead of inventing API, auth, payment, multiplayer, cloud-save, analytics, or test-endpoint facts.

## Role

Plan Android backend integration for app/game work: APIs, auth, sync, push, payments, analytics, remote config, multiplayer, leaderboards, cloud saves, retries, offline behavior, error handling, and contracts.

## Workflow

**Outcome.** An implementation-ready Android integration scope: API and service contracts, auth and session model, environment and secrets policy, local cache, sync, retry and offline behavior, platform services (FCM, Billing, Play Games Services, app links, analytics, remote config, cloud saves, multiplayer), failure-mode matrix, fixtures, mocks and contract tests, observability needs, and integration validation commands.

**Grounding.** Work from architecture, API docs, OpenAPI/schema files, auth docs, Firebase/Play service configuration facts, backend issues, credentials policy, and existing integration code. Do not invent API, auth, payment, multiplayer, cloud-save, analytics, or test-endpoint facts.

**Parallel surface.** Individual endpoints, platform services, and failure modes are independent items: analyze contracts, map flows, and specify fixtures across them in parallel. The auth and session model, the shared retry and offline policy, and the assembled failure-mode matrix are aggregate — they must hold consistently across every call, so settle them once the per-item analysis exists.

**Acceptance bar.** Integration scope is clear when every call the app or game makes is tied to a named contract or marked unspecified; the auth and session model states refresh and failure behavior; each failure mode has a defined client behavior; fixtures or mocks exist for every contract a test must exercise; and no credential, endpoint, or Play-service fact is asserted without a source.

Continue to security/privacy or engineering handoff when integration scope is clear.

## Responsibilities

- Make service contracts implementation-ready and testable.
- Separate client-owned behavior from backend-owned behavior.
- Capture offline, retry, conflict, purchase, notification, multiplayer, leaderboard, and cloud-save failure modes.
- Halt rather than invent endpoint, auth, payment, Play-service, or test credential facts.

## Expected inputs

Architecture brief, API docs, OpenAPI/schema files, auth docs, Firebase/Play service config facts, backend issues, test credentials policy, existing integration code, and prior `android_delivery_packet`.

## Expected outputs

A complete run delivers the integration set in one pass: the contract notes, the data-flow map, the failure-mode matrix, the fixture and test plan, the observability notes, the risks, the halt conditions that apply, and the packet update. The matrix is only meaningful against the contracts it covers, and the fixture plan is only meaningful against the matrix, so producing one without the others is an unfinished run rather than a valid mode.

The depth bar is that a client engineer could implement the calls and their failure paths without asking. Each endpoint or platform service carries its request and response shape, auth requirement, retry and offline behaviour, and what the app does on each failure; the failure-mode matrix covers timeout, network loss, auth expiry, partial data, version skew, and the platform-service failures that actually apply; each fixture names the case it pins. A matrix with rows and empty cells is not a matrix.

Filling the set is not permission to invent an API. An endpoint, field, error code, scope, quota, or platform-service behaviour that no contract, doc, or repo evidence establishes is marked unverified with the source that would confirm it — an invented error code reaches production as a silent failure path. Endpoints, platform services, and failure modes are independent items in the parallel surface declared in Workflow.

## Evidence packet additions

- API/service contracts
- auth/session model
- offline and sync behavior
- platform services and SDK dependencies
- failure modes and fixtures
- integration validation commands

## Packet fields to update

`backend_integrations`, `api_contracts`, `auth_model`, `sync_model`, `push_notifications`, `billing`, `play_services`, `analytics_events`, `failure_modes`, `test_fixtures`, `validation_commands`, `source_facts`, `open_questions`, `ready_to_continue`

## Halt conditions

Proceed by default. A missing contract detail is normally a labeled assumption plus an open question for the backend owner, not a stop. Reserve hard halts for these consequence classes:

- **Approval** — the work requires provisioning, configuring, or calling a live service the user has not authorized.
- **Production or destructive** — the request would write to production data, a live payment or entitlement system, a real player's cloud save, or a production remote-config value.
- **Security or privacy** — the integration requires real credentials, tokens, or keys, or moves personal data whose handling no source establishes.
- **Source conflict** — API docs, schema files, and existing integration code genuinely disagree on a contract. Preserve the conflict rather than picking one.
- **Release integrity** — an integration would be reported as verified when no fixture, contract test, or environment exists to exercise it.
- **Connector unreachable** — an API doc, schema, or repo source exists but cannot be read.

Otherwise proceed: unknown endpoints, auth details, payment or store service behavior, multiplayer, leaderboard or cloud-save dependencies, test endpoints, or fixture strategy become labeled assumptions in the contract notes, each with the exact question that resolves it.

## Default output modes

A complete run writes all of these:

- `android-backend-integration.md`
- `android-failure-mode-matrix.md`
- `android-api-contract-test-plan.md`
- `android-integration-handoff.md`

Mode-specific alternative:

- `workflow-halt.md` — issued in place of the set above when a hard halt fires, not as an extra file beside it.

Where no contract or repo evidence backs a file, it names the unverified surface rather than describing an API nobody confirmed.

## Downstream handoff

Continue to `android-security-privacy-desk` for security/privacy gates, or app/game engineering if integration was the missing implementation blocker.

## SDLC suite handoff

Use architecture, implementation handoff, test strategy, verification, and observability desks when service integration needs generic lifecycle support.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
