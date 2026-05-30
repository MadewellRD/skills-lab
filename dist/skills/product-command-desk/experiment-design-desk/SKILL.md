---
name: experiment-design-desk
description: design product experiments with hypotheses, metrics, cohorts, variants, guardrails, duration, analysis rules, ethical constraints, and decision criteria.
---

# Experiment Design Desk

## Role

Design product experiments that answer decision-relevant uncertainty. Define hypotheses, metrics, cohorts, variants, guardrails, duration, analysis rules, risk controls, and decision criteria.

## Use when

- A product decision has uncertainty that can be tested.
- A feature, pricing, onboarding, retention, or messaging change needs experiment design.
- An experiment needs guardrails and decision rules before launch.

## Do not use when

- The decision cannot be ethically or practically tested.
- No measurable outcome or target population exists.
- The user wants to run an experiment without guardrails or approval.

## Required evidence

- Decision question, hypothesis, target population, variants, and constraints.
- Primary, secondary, and guardrail metrics.
- Sample size, duration, segmentation, instrumentation, and analysis needs.
- Risk, ethics, compliance, and user impact constraints.

## Workflow

- Define the decision and hypothesis.
- Select metrics, cohorts, variants, and guardrails.
- Set duration, analysis, and stopping rules.
- Identify instrumentation and risk controls.
- Prepare launch and analysis handoffs.

## Outputs

- experiment plan
- hypothesis and metric tree
- cohort and variant design
- guardrail list
- decision rules

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- hypothesis
- population
- variants
- metrics
- guardrails
- analysis_plan
- decision_rules

## Halt conditions

- Decision question, metric, cohort, or instrumentation is missing.
- Experiment risk requires approval or ethical review.
- Results would be underpowered or misleading for the requested decision.

## Downstream handoffs

- Data Command Desk
- launch-readiness-desk
- feedback-synthesis-desk
- feature-prioritization-desk

## Source hierarchy

- User-provided product goal, target audience, and business constraints define the scope boundary.
- Customer research, usage data, sales/support evidence, experiments, and product analytics are authoritative for product behavior and demand.
- Repository, issue, design, and release evidence are authoritative for shipped implementation state.
- Market reports, public competitor information, and external sources support context but must not override first-party evidence without noting uncertainty.
- Stakeholder notes and conversation summaries are decision context, not proof of customer behavior or shipped state.

## Quality bar

- Trace every recommendation to source evidence or clearly labeled assumptions.
- Separate facts, decisions, hypotheses, and open questions.
- Define measurable acceptance or decision gates whenever possible.
- Avoid converting weak evidence into confident roadmap, pricing, or launch commitments.
