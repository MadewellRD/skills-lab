---
name: roadmap-planning-desk
description: create roadmap plans with themes, sequencing, milestones, dependencies, capacity constraints, confidence, risks, decision records, and delivery handoffs.
---

# Roadmap Planning Desk

## Role

Plan product roadmaps by translating strategy, requirements, capacity, dependencies, risks, and evidence into themes, sequence, milestones, and decision records.

## Use when

- A team needs initiative sequencing or roadmap shape.
- Multiple product opportunities must be ordered against constraints.
- Stakeholders need roadmap rationale and dependency visibility.

## Do not use when

- There is only one already-approved implementation task.
- No priorities, constraints, capacity, or decision owner exists.
- The user expects delivery dates without engineering input.

## Required evidence

- Product goals, initiatives, opportunity sizes, customer commitments, and strategic constraints.
- Delivery capacity, dependencies, technical constraints, and risk evidence.
- Priority criteria, timing windows, and decision owner.
- Existing roadmap or milestone state.

## Workflow

- Define roadmap horizon and decision criteria.
- Group work into themes and initiatives.
- Sequence by value, risk, dependency, and capacity.
- Record tradeoffs and confidence.
- Prepare downstream issue planning or release handoff.

## Outputs

- roadmap plan
- theme map
- sequencing rationale
- milestone proposal
- risk and dependency list

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- roadmap_horizon
- themes
- initiatives
- sequence
- dependencies
- capacity_assumptions
- confidence

## Halt conditions

- Capacity, dependencies, priority criteria, or decision owner is missing.
- Dates are requested without delivery evidence.
- Roadmap conflicts with accepted commitments or release constraints.

## Downstream handoffs

- feature-prioritization-desk
- issue-planning-desk
- release-operations-desk
- prd-desk

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
