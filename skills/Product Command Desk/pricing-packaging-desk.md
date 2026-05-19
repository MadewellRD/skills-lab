---
name: pricing-packaging-desk
description: develop pricing and packaging hypotheses, entitlements, plan boundaries, monetization risks, willingness-to-pay signals, experiments, and rollout handoffs.
---

# Pricing Packaging Desk

## Role

Frame pricing and packaging decisions. Define packages, entitlements, monetization hypotheses, willingness-to-pay signals, plan boundaries, risks, experiments, and rollout considerations.

## Use when

- A product change affects monetization, plan packaging, limits, or entitlements.
- A launch needs pricing or packaging assumptions.
- Customer, sales, or market evidence suggests pricing friction or opportunity.

## Do not use when

- The user needs accounting, tax, or legal pricing advice.
- No business model or target segment is known.
- The feature has no monetization or packaging impact.

## Required evidence

- Target segment, buyer, value metric, product usage, and business goal.
- Willingness-to-pay signals, sales objections, churn/retention data, competitor pricing, and support impact.
- Current plans, entitlements, billing constraints, and operational limits.
- Approval owner and experiment tolerance.

## Workflow

- Define pricing decision and constraints.
- Map value metric, package boundaries, and entitlement options.
- Assess customer, revenue, retention, and operational risk.
- Design experiments or rollout plan when uncertain.
- Prepare GTM, launch, and implementation handoffs.

## Outputs

- pricing hypothesis
- packaging proposal
- entitlement map
- risk assessment
- experiment or rollout plan

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- pricing_decision
- segments
- value_metric
- packages
- entitlements
- risks
- approval_owner

## Halt conditions

- Business model, buyer, approval owner, or pricing constraints are missing.
- Decision would affect revenue without evidence or approval.
- Legal, tax, or compliance review is required.

## Downstream handoffs

- gtm-brief-desk
- launch-readiness-desk
- experiment-design-desk
- SDLC Command Desk for entitlement implementation

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
