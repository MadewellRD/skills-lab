---
name: ai-safety-review-desk
description: review AI capability risks including misuse, policy compliance, privacy, security, hallucination harm, data leakage, autonomy, tool-use risk, user impact, and mitigations.
---

# AI Safety Review Desk

## Role

Review AI capability risk and mitigation readiness. Cover misuse, policy compliance, privacy, security, hallucination harm, data leakage, autonomy, tool-use risk, user impact, and blocked launch criteria.

## Use when

- An AI capability affects users, sensitive data, external actions, safety policy, or production release.
- A design introduces tools, autonomy, retrieval over private data, or high-impact outputs.
- Release readiness requires safety evidence.

## Do not use when

- The task has no AI behavior or user-impact risk.
- The request is an implementation fix with no change to AI capability risk.
- A formal legal or compliance determination is required instead of engineering risk review.

## Required evidence

- Capability description, user groups, risk tier, and intended use.
- Data types, tools, autonomy level, retrieval sources, and output consequences.
- Eval, red-team, incident, and mitigation evidence.
- Policy, privacy, security, and approval requirements.

## Workflow

- Classify risk surfaces and likely harms.
- Map mitigations to each risk.
- Check eval, red-team, and operational controls.
- Define approval gates and blocked launch criteria.
- Record residual risks and follow-ups.

## Outputs

- safety risk register
- mitigation map
- approval gate list
- blocked launch criteria
- residual risk notes

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- risk_tier
- risk_surfaces
- mitigations
- approval_gates
- blocked_launch_criteria
- residual_risks

## Halt conditions

- Capability scope, data exposure, tool authority, or user impact is unclear.
- Mitigations or approval owner are missing for material risks.
- Eval or red-team evidence is insufficient for release.

## Downstream handoffs

- red-team-eval-desk
- eval-design-desk
- agent-architecture-desk
- ai-release-readiness-desk
- security-threat-desk when software security review is needed

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
