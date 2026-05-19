---
name: market-discovery-desk
description: create market discovery artifacts covering category context, customers, alternatives, trends, constraints, demand signals, and opportunity framing for product decisions.
---

# Market Discovery Desk

## Role

Map the market context around a product opportunity. Identify category dynamics, target customers, alternatives, trends, constraints, demand signals, adoption blockers, and unresolved market assumptions.

## Use when

- A product idea needs market context before requirements or roadmap decisions.
- A team is entering or repositioning within a market/category.
- Stakeholders need opportunity framing grounded in evidence.

## Do not use when

- The request already has accepted market research and needs implementation planning.
- The work is purely internal tooling with no market/customer decision.
- The user needs a legal, investment, or regulatory opinion.

## Required evidence

- Target category, users, buyers, customer problem, and business objective.
- First-party customer or sales signals when available.
- Public market, competitor, substitute, and trend sources.
- Constraints such as geography, segment, budget, regulation, and channel.

## Workflow

- Define the market question and decision target.
- Map category, customers, buyers, alternatives, and substitutes.
- Identify demand signals and adoption constraints.
- List assumptions, confidence, and research gaps.
- Prepare handoff to user research, opportunity sizing, or competitive analysis.

## Outputs

- market discovery brief
- category map
- customer and buyer hypothesis
- demand signal summary
- research gap list

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- market_question
- category
- customer_hypotheses
- demand_signals
- market_constraints
- research_gaps

## Halt conditions

- Market category, target customer, or decision target is unclear.
- Evidence is too weak to distinguish fact from hypothesis.
- Recent market facts are required but unavailable.

## Downstream handoffs

- user-research-desk
- opportunity-sizing-desk
- competitive-analysis-desk
- persona-segmentation-desk

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
