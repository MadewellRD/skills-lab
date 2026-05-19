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

- Classify runtime requirements and provider constraints.
- Design request path, retries, timeouts, caching, batching, and fallbacks.
- Define secrets, logging, retention, and data handling.
- Set SLOs and operational runbooks.
- Prepare release and observability handoffs.

## Outputs

- inference ops plan
- runtime topology
- SLO proposal
- fallback policy
- runbook checklist

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

- Production environment, traffic estimate, or reliability target is missing.
- Provider constraints cannot be verified.
- Logging or data retention would violate privacy requirements.

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
- State uncertainty explicitly and halt when required facts are missing.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
