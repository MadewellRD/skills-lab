---
name: product-retrospective-desk
description: create product retrospectives after launch, experiment, roadmap cycle, or initiative using goals, outcomes, metrics, customer evidence, misses, lessons, and improvement actions.
---

# Product Retrospective Desk

## Role

Create product retrospectives after launches, experiments, roadmap cycles, or initiatives. Compare goals to outcomes, synthesize customer and metric evidence, identify misses, lessons, and improvement actions.

## Use when

- A launch, experiment, or product cycle needs retrospective analysis.
- Metrics, feedback, and delivery outcomes need synthesis.
- The team needs lessons and follow-up actions before the next cycle.

## Do not use when

- The product work has not shipped or reached a review point.
- No goals, metrics, or outcome evidence exists.
- The request is incident-only and needs incident response.

## Required evidence

- Original goals, requirements, launch plan, experiment plan, or roadmap commitments.
- Outcome metrics, customer feedback, support/sales/success evidence, and delivery facts.
- Known risks, blockers, incidents, and decision history.
- Follow-up owners and improvement constraints.

## Workflow

- Reconstruct intended goals and decision context.
- Compare outcomes against success metrics and expectations.
- Identify what worked, what missed, and why.
- Separate product, process, delivery, and GTM lessons.
- Define follow-up actions and next-cycle inputs.

## Outputs

- product retrospective
- outcome summary
- lesson list
- action-item tracker
- next-cycle recommendations

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- review_scope
- original_goals
- outcomes
- lessons
- action_items
- owners
- next_cycle_inputs

## Halt conditions

- Original goals, metrics, or outcome evidence is missing.
- Evidence conflicts on whether the launch or experiment succeeded.
- Follow-up actions require owner approval or cross-functional commitment.

## Downstream handoffs

- roadmap-planning-desk
- feedback-synthesis-desk
- retrospective-desk
- issue-planning-desk

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
