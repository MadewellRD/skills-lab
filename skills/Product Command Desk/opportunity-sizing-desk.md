---
name: opportunity-sizing-desk
description: estimate product opportunity size using TAM, SAM, SOM, customer count, adoption constraints, revenue potential, usage potential, confidence ranges, and assumption tracking.
---

# Opportunity Sizing Desk

## Role

Size product opportunities using appropriate methods such as TAM, SAM, SOM, account count, user count, usage volume, willingness-to-pay, retention impact, cost savings, or strategic value.

## Use when

- A product idea needs business impact framing.
- Roadmap or prioritization decisions need opportunity size.
- Stakeholders need assumptions, ranges, and confidence documented.

## Do not use when

- The work is purely qualitative discovery with no sizing decision.
- No market, customer, usage, pricing, or business model evidence exists.
- The user expects precise forecasts without data.

## Required evidence

- Target market or segment definition.
- Customer count, user count, usage, revenue, pricing, retention, or cost data when available.
- Adoption constraints, channel constraints, and competitive context.
- Assumptions, confidence, and decision threshold.

## Workflow

- Select the sizing method appropriate to the decision.
- Compute or frame ranges and assumptions.
- Map confidence, sensitivity, and adoption constraints.
- Compare opportunity against alternatives.
- Prepare prioritization or roadmap handoff.

## Outputs

- opportunity sizing memo
- assumption table
- range estimate
- sensitivity notes
- prioritization input

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- sizing_method
- market_or_segment
- assumptions
- range_estimates
- confidence
- decision_threshold

## Halt conditions

- Target segment, sizing method, or business model is unclear.
- Required data is missing and the user needs precise estimates.
- Assumptions dominate the estimate without confidence labeling.

## Downstream handoffs

- feature-prioritization-desk
- roadmap-planning-desk
- pricing-packaging-desk
- market-discovery-desk

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
