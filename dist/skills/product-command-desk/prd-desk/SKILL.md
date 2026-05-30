---
name: prd-desk
description: create product requirements documents with problem statement, goals, non-goals, users, requirements, acceptance criteria, risks, open questions, metrics, and downstream handoffs.
---

# PRD Desk

## Role

Create product requirements documents that are ready for technical discovery, design, issue planning, or implementation. Preserve product intent, acceptance criteria, non-goals, risks, metrics, and evidence.

## Use when

- A product idea needs requirements.
- Discovery evidence must be turned into implementable scope.
- An existing requirement needs cleanup, traceability, or acceptance gates.

## Do not use when

- The work is still exploratory and lacks a validated problem or target user.
- The request is already an implementation prompt with accepted requirements.
- The issue is purely technical refactor or incident response.

## Required evidence

- Problem statement, target users, business goal, and success metrics.
- Research, market, analytics, support, sales, or stakeholder evidence.
- Constraints, dependencies, non-goals, edge cases, and release expectations.
- Decision owner and unresolved questions.

## Workflow

- Clarify problem, users, goals, and non-goals.
- Extract requirements and acceptance criteria.
- Map source evidence and risks.
- Identify dependencies and open questions.
- Prepare downstream handoff to SDLC or AI Engineering when ready.

## Outputs

- PRD
- requirement IDs
- acceptance criteria
- non-goals
- risk list
- open question list
- handoff notes

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- requirement_ids
- acceptance_criteria
- success_metrics
- non_goals
- dependencies
- open_questions

## Halt conditions

- Target user, problem, or acceptance criteria are missing.
- Evidence conflicts on scope or value.
- The requirement would commit implementation before discovery or architecture is ready.

## Downstream handoffs

- technical-discovery-desk
- architecture-design-desk
- issue-planning-desk
- AI Engineering Command Desk when AI behavior is in scope
- test-strategy-desk

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
