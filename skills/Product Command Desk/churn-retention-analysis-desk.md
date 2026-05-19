---
name: churn-retention-analysis-desk
description: analyze churn and retention drivers using cohorts, usage patterns, feedback, lifecycle stages, activation, engagement, expansion, and intervention opportunities.
---

# Churn Retention Analysis Desk

## Role

Analyze churn and retention signals. Identify cohorts, usage patterns, lifecycle gaps, activation failures, engagement drop-offs, expansion blockers, feedback themes, and intervention opportunities.

## Use when

- A product needs churn, retention, activation, or engagement diagnosis.
- Feedback and analytics suggest users are not adopting or staying.
- Retention initiatives need product implications and experiment ideas.

## Do not use when

- There is no churn, retention, cohort, usage, or feedback evidence.
- The task is purely financial revenue recognition.
- The issue is a known production incident requiring incident response.

## Required evidence

- Cohort, retention, churn, activation, usage, and engagement data where available.
- Customer interviews, cancellation reasons, support tickets, sales/customer success notes, and feedback.
- Segment, plan, lifecycle stage, and product area context.
- Business impact and intervention constraints.

## Workflow

- Frame the retention question and affected segments.
- Map funnel, lifecycle, cohort, and usage evidence.
- Cluster churn drivers and retention opportunities.
- Identify product, support, success, or pricing interventions.
- Define experiments or roadmap inputs.

## Outputs

- retention analysis
- churn driver taxonomy
- cohort insight summary
- intervention map
- experiment recommendations

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- retention_question
- cohorts
- churn_drivers
- usage_patterns
- interventions
- expected_impact

## Halt conditions

- Required cohort, usage, or feedback data is missing.
- Churn cause cannot be separated from incident or support failure.
- Recommended intervention needs pricing, legal, or customer success approval.

## Downstream handoffs

- experiment-design-desk
- feature-prioritization-desk
- pricing-packaging-desk
- Customer Success Command Desk
- Data Command Desk

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
