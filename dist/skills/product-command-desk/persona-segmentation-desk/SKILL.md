---
name: persona-segmentation-desk
description: define personas, customer segments, ICPs, jobs-to-be-done, journey stages, use cases, and segment-specific product needs from research and market evidence.
---

# Persona Segmentation Desk

## Role

Define personas, segments, ICPs, use cases, jobs-to-be-done, and journey stages. Keep segmentation tied to evidence and product decisions rather than decorative persona documents.

## Use when

- A product workflow needs target user clarity.
- Discovery or roadmap decisions depend on segment differences.
- Messaging, requirements, or launch planning needs segment-specific needs.

## Do not use when

- The audience is already fixed and no segment-level decision is needed.
- There is no customer, research, usage, or market evidence.
- The task is demographic labeling without product implications.

## Required evidence

- User research, customer data, sales/support signals, or market evidence.
- Business model, buyer/user distinction, and deployment context.
- Use cases, workflows, pains, jobs, and adoption constraints.
- Decision that segmentation must support.

## Workflow

- Identify segmentation purpose and decision dependency.
- Cluster users by behavior, needs, context, and value potential.
- Define personas or segments with evidence and confidence.
- Map segment needs to product and GTM implications.
- Flag gaps requiring research or analytics.

## Outputs

- persona or segment map
- ICP hypothesis
- jobs-to-be-done summary
- journey notes
- segment implication matrix

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- segments
- personas
- jobs_to_be_done
- journey_stages
- segment_needs
- confidence_notes

## Halt conditions

- No evidence supports segmentation.
- Buyer, user, and admin roles are conflated without clarification.
- Segment decision affects roadmap or pricing without owner approval.

## Downstream handoffs

- prd-desk
- gtm-brief-desk
- pricing-packaging-desk
- user-research-desk

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
