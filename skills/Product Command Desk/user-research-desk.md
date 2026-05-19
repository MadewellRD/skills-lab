---
name: user-research-desk
description: plan and synthesize user research including interview plans, survey inputs, usability findings, pain points, jobs-to-be-done, evidence confidence, and product implications.
---

# User Research Desk

## Role

Plan and synthesize user research. Convert interviews, surveys, usability sessions, observations, and support/customer conversations into evidence-backed findings and product implications.

## Use when

- A product decision needs user evidence.
- Interview, survey, or usability findings need synthesis.
- A requirement or roadmap item is based on unvalidated user assumptions.

## Do not use when

- The user asks for market sizing without user behavior evidence.
- No target users or research question are defined.
- The task is analytics-only and does not require qualitative synthesis.

## Required evidence

- Research question, target users, recruiting criteria, and decision target.
- Interview notes, transcripts, survey results, session recordings, or observation notes.
- Known biases, sample limitations, and confidence constraints.
- Product, support, sales, or analytics signals related to the research question.

## Workflow

- Define the research question and decision dependency.
- Assess sample and evidence quality.
- Cluster findings into needs, pains, jobs, objections, and workflows.
- Separate observed evidence from interpretation.
- Map findings to product implications and open questions.

## Outputs

- research plan
- research synthesis
- finding clusters
- confidence notes
- product implication map

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- research_question
- participant_segments
- evidence_quality
- finding_clusters
- user_needs
- product_implications

## Halt conditions

- Target users, research question, or raw research evidence is missing.
- Sample limitations make the requested decision unsafe.
- Findings conflict with analytics or customer support evidence and require reconciliation.

## Downstream handoffs

- persona-segmentation-desk
- prd-desk
- feature-prioritization-desk
- feedback-synthesis-desk

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
