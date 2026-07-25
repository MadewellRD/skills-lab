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

This order is mandated. Scope boundaries and authorization are fixed before any adversarial scenario is executed, and logging, review protocol, and severity classification exist before findings are produced, so that a live finding is never handled ad hoc.

1. Define red-team objectives and scope boundaries, including what is explicitly out of bounds.
2. Create adversarial scenarios and test categories within that scope.
3. Specify logging, review protocol, and severity classification.
4. Analyze failures and map mitigations.
5. Convert repeatable attacks into regression evals.

Within steps 2 and 4 the attack categories are independent: authoring scenarios, executing them, and analyzing results are parallel-safe across jailbreak, prompt-injection, data-exfiltration, harmful-instruction, tool-permission, and policy-evasion categories. Scope definition in step 1 and the severity scale in step 3 are shared and are set once, before that fan-out begins.

## Outputs

A red-team run delivers the plan and the results of running it, together:

- red-team plan — scope, the system boundary under test, the attack categories in and out of scope, the severity scale, and the stop rule.
- adversarial scenario matrix — concrete scenarios per category with the exact input, the target behavior, and what counts as a failure. A category name with no scenarios under it is not coverage.
- failure report — every observed failure with its reproduction input, its severity against the declared scale, and the boundary it crossed.
- mitigation recommendations — per failure: the control and the layer that should enforce it, separating what prompt text can hold from what must move to tools, retrieval, or runtime policy.
- regression eval candidates — the cases that should become permanent slices, shaped for `eval-design-desk` to consume.

Where the run is design-only because the scenarios have not been executed against a real system, the failure report and the mitigations that depend on it are the mode-specific alternative: they are reported as not yet run, the plan and matrix are delivered in full, and execution is named as the next step. They are never populated with failures nobody observed.

Depth bar: another red-teamer could reproduce any listed failure from the record alone. Attack categories fan out in parallel; scope and the severity scale are set once before that fan-out begins.

This is where invention does the most damage. A hypothesized jailbreak written up as an observed one, a severity assigned without a reproduction, or a mitigation described as in place without evidence each corrupt the safety record that later releases lean on. Report the gap instead.

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

Default posture is to proceed and label the assumption inline; an unconfirmed reviewer roster or an undecided sample size is a soft gap. Halt only when one of the six hard-halt classes applies.

- Approval — testing would reach a system, tenant, dataset, or user population that has not been authorized as in scope.
- Production or destructive — an adversarial scenario would execute a real side-effecting action against production systems, real users, or live data.
- Security or privacy — testing would require producing genuinely harmful operational content outside defensive scope, or would expose real personal, regulated, or credential data.
- Source conflict — safety policy, system prompt, and tool contracts disagree about what the system is permitted to do, leaving "failure" undefinable.
- Release integrity — findings would be closed without mitigation evidence, or a release would proceed on red-team coverage that never exercised the material attack surface.
- Connector unreachable — the system prompt, tool contracts, eval harness, or prior incident records exist but cannot be read.

A finding that indicates active exploitation, live data exposure, or ongoing user harm is an immediate escalation to `ai-incident-response-desk`, not a test result to file.

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
- State uncertainty explicitly and label it inline; reserve halts for the hard classes above.
- Prefer measurable gates over qualitative approval language.
- Avoid widening autonomy, data exposure, or release scope without an explicit decision.
- Passing means every in-scope attack category has scenarios and an executed result, every failure carries a severity against the stated scale and a mapped mitigation, and every repeatable attack has been converted into a named regression eval.
