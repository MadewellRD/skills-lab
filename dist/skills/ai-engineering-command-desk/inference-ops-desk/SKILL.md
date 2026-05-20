---
name: inference-ops-desk
description: plan production inference operations including deployment topology, rate limits, quotas, retries, caching, streaming, fallbacks, batching, timeouts, secrets, logging, and SLOs.
---

# Inference Ops Desk

## Packaged skill operating model

Use this skill when ChatGPT needs to design, review, diagnose, or harden production inference operations for AI capabilities. Prefer connector-grounded evidence over generic LLMOps advice. Use SignalDesk for local repo state and report files when available, GitHub for remote source truth, and current provider or standards documentation only after repo facts and user-scoped requirements are captured.

When asked to produce implementation work, do not emit broad instructions. Emit a compact inference-ops packet or implementation handoff with exact runtime targets, provider constraints, fallback policy, logging and retention rules, SLOs, validation gates, allowed and forbidden changes, halt conditions, and downstream desk targets.

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
- workflow_mode
- current_stage
- user_goal and target outcome
- source_facts and evidence_links
- risk_tier and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- deployment_target
- traffic_profile
- slo_targets
- provider_limits
- rate_limits
- quota_policy
- retry_policy
- timeout_policy
- batching_policy
- caching_policy
- streaming_policy
- fallback_policy
- secrets_policy
- logging_policy
- retention_policy
- rollback_policy

## Validation gates

- Production environment, traffic profile, latency target, and availability target are explicit.
- Provider limits, rate limits, quotas, timeout behavior, and fallback options are verified or listed as blockers.
- Logging, privacy, secret handling, data retention, and redaction requirements are explicit.
- Retry, batching, caching, and fallback policies include failure modes and rollback expectations.
- SLOs, runbooks, alerts, and downstream observability handoff targets are explicit.

## Halt conditions

- Production environment, traffic estimate, or reliability target is missing.
- Provider constraints cannot be verified.
- Logging or data retention would violate privacy requirements.
- Secrets, credentials, data residency, or provider tenancy rules are unclear.
- A release or production handoff is requested without eval, safety, rollback, or observability gates.

## Downstream handoffs

- agent-observability-desk
- cost-latency-optimization-desk
- ai-release-readiness-desk
- ai-incident-response-desk
- SDLC Command Desk for implementation

## Source hierarchy

- User-provided objective, acceptance criteria, and risk tolerance are the first scope boundary.
- Repository, issue, eval, dataset, telemetry, deployment, incident, and release evidence are authoritative for implementation state.
- Provider documentation and official platform docs are used for model/API/runtime capabilities when internal evidence is absent.
- Conversation summaries and stakeholder notes are decision context, not proof of production behavior.

## Quality bar

- Preserve traceability from recommendation to source evidence.
- State uncertainty explicitly and halt when required facts are missing.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
- Do not hide operational uncertainty behind generic best-practice language.

## Low-token execution policy

- Produce compact inference-ops packets with exact deployment target, provider limits, SLOs, retries, timeouts, caching, batching, fallbacks, logging, retention, and rollback expectations.
- Do not ask Codex or Claude Code to infer runtime topology, provider constraints, secrets policy, SLOs, or validation commands.
- When implementation is required, hand off exact files, config keys, environment variables, validation commands, allowed files, forbidden files, PR title/body, and stop line.
- Collapse long operational research into source facts, decisions, assumptions, hard halts, soft gaps, and downstream handoff targets before implementation handoff.

## References

- `references/suite-workflow-contract.md`: AI Engineering workflow packet, stage advancement, continuation, and halt contract.
- `references/standards-source-map.md`: standards and industry patterns used for AI Engineering desk hardening.
- `references/desk-hardening-matrix.md`: desk-by-desk hardening expectations and downstream handoff map.
- `references/inference-ops-packet-template.md`: packet structure for production inference operations handoffs.
- `references/inference-ops-quality-checklist.md`: operational readiness checklist.

## Continuity Kernel Adoption

Preserve and update the workflow packet instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable downstream work.

Set `ready_to_continue: true` only when runtime target, provider constraints, SLOs, fallback policy, logging/retention rules, validation gates, and downstream handoff target are explicit enough for the next desk to act without rediscovering scope. Otherwise return `Workflow Halt` with exact resume requirements.
