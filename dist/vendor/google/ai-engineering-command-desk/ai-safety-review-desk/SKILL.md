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

This is a safety review chain and the order is mandated. Risks are enumerated before mitigations are claimed, mitigations are evidenced before approval gates are set, and residual risk is recorded last so that nothing is closed out silently.

1. Classify risk surfaces and likely harms.
2. Map mitigations to each risk.
3. Check eval, red-team, and operational controls against those mitigations.
4. Define approval gates and blocked launch criteria.
5. Record residual risks and follow-ups.

Within steps 1 through 3 the risk surfaces are independent: enumerating harms, mapping mitigations, and gathering control evidence for each surface is parallel-safe across surfaces. The risk-tier judgment, the approval gates, and the blocked-launch criteria in steps 4 and 5 are aggregate and are set once against the complete risk set.

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

Default posture is to proceed and label the assumption inline; an unquantified likelihood or an incomplete user-segment breakdown is a soft gap. Halt only when one of the six hard-halt classes applies. In this desk a halt is a normal outcome rather than a failure — surfacing a material risk that has no owner is the point.

- Approval — a material risk has no approval owner, or the capability would ship at a risk tier the owner has not accepted.
- Production or destructive — the capability could take irreversible real-world action and the gate in front of that action is missing or unproven.
- Security or privacy — data exposure, tool authority, or cross-tenant reach is unresolved, or the capability could leak personal, regulated, or credential data.
- Source conflict — capability documentation, eval evidence, and stated intended use disagree on what the system can actually do, or to whom.
- Release integrity — eval or red-team evidence is insufficient to support the release, or a mitigation is claimed without evidence that it works.
- Connector unreachable — eval results, red-team findings, incident history, or policy documentation exist but cannot be read.

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
- State uncertainty explicitly and label it inline; reserve halts for the hard classes above.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
- Passing means every identified risk surface carries a likely harm, a mitigation, the evidence that the mitigation works, and an owner; approval gates and blocked-launch criteria are explicit; and residual risks are recorded rather than resolved by omission.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
