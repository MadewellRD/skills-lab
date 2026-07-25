---
name: inference-ops-desk
description: plan production inference operations including deployment topology, rate limits, quotas, retries, caching, streaming, fallbacks, batching, timeouts, secrets, logging, and SLOs.
---

# Inference Ops Desk

## Role

Plan production inference operations. Define deployment topology, model access, rate limits, quotas, retries, caching, streaming, batching, timeouts, fallbacks, secrets, logging, data handling, and SLOs.

## Use when

- An AI capability is moving toward production.
- Inference reliability, quotas, latency, or cost needs operational design.
- Provider or model behavior requires fallback and monitoring controls.

## Do not use when

- The work is still conceptual and has no traffic or reliability target.
- The main gap is model quality or eval coverage.
- The deployment environment is unknown.

## Required evidence

- Production environment, traffic estimates, latency and availability targets.
- Model/provider limits, quotas, rate-limit behavior, and fallback options.
- Logging, privacy, secrets, retention, and data handling constraints.
- Existing telemetry, runbooks, and incident history.

## Workflow

Produce a runtime plan an operator can stand up: the request path end to end, what happens on every provider failure mode, how secrets and logs are handled, and the SLOs the system is committed to.

Constraints:

- Every provider failure mode: rate limit, timeout, quota exhaustion, degraded quality, hard outage, has a defined behavior. A path without a stated fallback is an incomplete plan.
- Never invent provider quotas, rate limits, pricing, or availability figures. Cite the provider surface or record the limit as unverified and name the measurement that would confirm it.
- Secrets, logging, retention, and data handling are bounded by the privacy requirements of the data class passing through inference.
- SLOs are stated as measurable targets with the telemetry that observes them.
- Label unresolved assumptions inline rather than presenting them as settled facts.

Provider surfaces and endpoints are independent. Gathering and assessing per-provider limits, quotas, failure behavior, and fallback candidates is parallel-safe, as is per-endpoint timeout and retry design. The shared SLO, secrets policy, and logging policy are single decisions across the runtime.

## Outputs

A full run delivers the whole operating design:

- inference ops plan: the serving path end to end, with the capacity, concurrency, and cost assumptions it rests on.
- runtime topology: providers, models, endpoints, regions, and the routing between them, with per-endpoint timeout and retry behavior.
- SLO proposal: latency, availability, and error-rate targets with their measurement window and the consequence of a breach.
- fallback policy: per failure class (rate limit, timeout, provider outage, content filter, degraded quality): what happens, in what order, and what the user sees.
- runbook checklist: the operational actions for each failure class, written for whoever is paged rather than for whoever designed the system.

Complete means operable: an on-call engineer could follow the runbook and an SRE could enforce the SLO without asking a follow-up question. Per-provider and per-endpoint design is parallel-safe; the shared SLO, secrets policy, and logging policy stay single decisions.

Provider facts are the risk point. Rate limits, quotas, context windows, pricing, and regional availability are cited to provider documentation or to observed telemetry, and recorded as unverified when neither is reachable. A fallback policy built on an invented quota fails at precisely the moment it is needed.

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- deployment_target
- traffic_profile
- slo_targets
- provider_limits
- fallback_policy
- logging_policy

## Halt conditions

Default posture is to proceed and label the assumption inline. An unconfirmed traffic estimate or an unverified provider quota is a soft gap: state the assumed figure, mark it, name the measurement that would confirm it, and continue. Halt only when one of the six hard-halt classes applies.

- Approval: the plan would commit spend, quota, or a provider contract beyond what the owner has authorized.
- Production or destructive: a topology, routing, or credential change would disrupt live inference traffic without a reversible path.
- Security or privacy: secrets handling, log content, or retention would expose credentials or personal data, or would violate the data-handling terms of the deployment environment.
- Source conflict: provider documentation, observed runtime behavior, and internal configuration disagree on limits, quotas, or failure semantics.
- Release integrity: the capability would go to production with no fallback for a known provider failure mode, or with SLOs that no telemetry can observe.
- Connector unreachable: runtime configuration, provider documentation, existing telemetry, or runbooks exist but cannot be read.

## Downstream handoffs

- agent-observability-desk
- cost-latency-optimization-desk
- ai-release-readiness-desk
- ai-incident-response-desk

## Source hierarchy

- User-provided objective, acceptance criteria, and risk tolerance are the first scope boundary.
- Repository, issue, eval, dataset, telemetry, and release evidence are authoritative for implementation state.
- Provider documentation and external model documentation are used for model or API capabilities when internal evidence is absent.
- Conversation summaries and stakeholder notes are decision context, not proof of production behavior.

## Quality bar

- Preserve traceability from recommendation to source evidence.
- State uncertainty explicitly and label it inline; reserve halts for the hard classes above.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
- Passing means the request path, every provider failure mode with its fallback, the secrets and logging policy, and the SLO set with its observing telemetry are all stated, each traced to a source fact or a labeled assumption.
