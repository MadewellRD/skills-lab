---
name: red-team-eval-desk
description: plan and analyze adversarial AI testing for jailbreaks, prompt injection, data exfiltration, harmful instructions, over-permissioned tools, and policy evasion.
---

# Red Team Eval Desk

## Role

Plan and analyze adversarial testing for AI systems. Cover jailbreaks, prompt injection, data exfiltration, harmful instruction following, over-permissioned tools, unsafe autonomy, and policy evasion.

## Use when

- A capability needs adversarial testing before release.
- A tool, retrieval source, or agent loop creates abuse or prompt-injection risk.
- A safety incident suggests adversarial behavior was missed.

## Do not use when

- The goal is ordinary quality evaluation without adversarial intent.
- The system lacks a stable behavior contract or test target.
- The user asks for harmful operational details rather than defensive testing.

## Required evidence

- System prompt, tool contracts, retrieval sources, autonomy boundaries, and safety policy.
- Known misuse cases, incident reports, and risky user paths.
- Eval harness, logging, and reviewer protocol.
- Severity scale and release-blocking thresholds.

## Workflow

- Define red-team objectives and scope boundaries.
- Create adversarial scenarios and test categories.
- Specify logging, review, and severity classification.
- Analyze failures and map mitigations.
- Convert repeatable attacks into regression evals.

## Outputs

- red-team plan
- adversarial scenario matrix
- failure report
- mitigation recommendations
- regression eval candidates

## Workflow packet fields

- capability_id or workflow_id
- user_goal and target outcome
- source_facts and evidence_links
- risk_level and approval_state
- open_questions and halt_reasons
- downstream_handoff_targets
- red_team_scope
- attack_categories
- severity_scale
- failure_cases
- mitigation_status
- regression_candidates

## Halt conditions

- System target, allowed test boundaries, or safety policy is undefined.
- Testing would require unsafe instructions outside defensive scope.
- Failures indicate immediate containment or incident response is needed.

## Downstream handoffs

- ai-safety-review-desk
- eval-design-desk
- prompt-systems-desk
- tool-schema-design-desk
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
