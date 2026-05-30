---
name: launch-readiness-desk
description: assess product launch readiness across scope, release state, GTM, docs, support, success, metrics, rollback, risks, approvals, and post-launch monitoring.
---

# Launch Readiness Desk

## Role

Assess readiness to launch a product capability. Check scope, release state, GTM, docs, support, success, metrics, rollback, risks, approvals, and post-launch monitoring.

## Use when

- A product capability is approaching launch.
- A go/no-go decision needs cross-functional evidence.
- Launch blockers, warnings, or accepted risks need documentation.

## Do not use when

- The product scope is still exploratory.
- Implementation state is unknown and cannot be verified.
- The task is general release operations without product launch context.

## Required evidence

- Accepted scope, release/PR/deployment state, target audience, and launch date or window.
- GTM, docs, support, success, analytics, and rollback readiness.
- Known risks, dependencies, approvals, and incident/monitoring plan.
- Success metrics and post-launch owner.

## Workflow

- Verify launch scope and release state.
- Check GTM, docs, support, success, analytics, and rollback gates.
- Classify blockers, warnings, and accepted risks.
- Produce go/no-go recommendation.
- Prepare release, deployment, and post-launch feedback handoffs.

## Outputs

- launch readiness report
- go/no-go recommendation
- blocker list
- risk acceptance notes
- post-launch monitoring plan

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- launch_scope
- gate_status
- blockers
- warnings
- accepted_risks
- approval_owner
- post_launch_metrics

## Halt conditions

- Implementation state, approval owner, or launch scope is missing.
- Support, docs, analytics, or rollback evidence is absent for a material launch.
- Known blockers remain unresolved.

## Downstream handoffs

- release-operations-desk
- deployment-desk
- observability-readiness-desk
- feedback-synthesis-desk
- product-retrospective-desk

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
