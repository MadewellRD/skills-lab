---
name: feature-prioritization-desk
description: prioritize product features using impact, effort, confidence, risk, strategic fit, customer evidence, dependencies, and decision records.
---

# Feature Prioritization Desk

## Role

Prioritize features or initiatives with explicit criteria. Compare impact, effort, confidence, risk, strategic fit, customer evidence, dependencies, and opportunity cost.

## Use when

- A backlog, roadmap, or feature set needs ranking.
- Stakeholders need tradeoff rationale.
- Customer, revenue, retention, or strategic signals conflict and need decision structure.

## Do not use when

- There is no decision set to rank.
- The user expects prioritization without criteria or evidence.
- The work is pure task scheduling after priorities are already decided.

## Required evidence

- Candidate features, requirements, opportunities, or backlog items.
- Customer evidence, usage data, opportunity size, risks, dependencies, and effort estimates.
- Prioritization criteria and decision owner.
- Delivery constraints and strategic commitments.

## Workflow

- Define prioritization criteria and decision boundary.
- Score or rank candidates with evidence and confidence.
- Identify dependencies, blockers, and risk-adjusted tradeoffs.
- Record decisions and dissenting evidence.
- Prepare roadmap, PRD, or issue-planning handoff.

## Outputs

- prioritization matrix
- ranked feature list
- decision record
- tradeoff notes
- handoff recommendations

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- candidates
- criteria
- scores
- ranked_order
- dependencies
- decision_record

## Halt conditions

- Candidate list, criteria, effort, or decision owner is missing.
- Ranking would imply commitment without delivery validation.
- Evidence conflicts materially across customer, business, or technical sources.

## Downstream handoffs

- roadmap-planning-desk
- prd-desk
- issue-planning-desk
- experiment-design-desk

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
