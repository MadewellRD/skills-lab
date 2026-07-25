---
name: feature-prioritization-desk
description: prioritize product features using impact, effort, confidence, risk, strategic fit, customer evidence, dependencies, and decision records.
---

# Feature Prioritization Desk

## Role

Prioritize features or initiatives with explicit criteria. Compare impact, effort, confidence, risk, strategic fit, customer evidence, dependencies, and opportunity cost.

## Use when

- A backlog, roadmap, or feature set needs ranking.
- Stakeholders need tradeoff rationale.
- Customer, revenue, retention, or strategic signals conflict and need decision structure.

## Do not use when

- There is no decision set to rank.
- The user expects prioritization without criteria or evidence.
- The work is pure task scheduling after priorities are already decided.

## Required evidence

- Candidate features, requirements, opportunities, or backlog items.
- Customer evidence, usage data, opportunity size, risks, dependencies, and effort estimates.
- Prioritization criteria and decision owner.
- Delivery constraints and strategic commitments.

## Workflow

**Outcome.** A ranked candidate set with explicit criteria, per-candidate evidence and confidence, the dependencies and tradeoffs that shaped the order, and a decision record that survives the meeting.

**Constraints.** State the criteria and the decision boundary before any ranking is asserted, and keep them stable across candidates — a score is only comparable if the scale was the same. Preserve dissenting evidence in the record rather than resolving it into the ranking. A ranking is an ordering of intent, not a delivery commitment; do not let it imply dates, staffing, or scope that has not been validated with delivery.

**Parallel surface.** Candidates are independent for scoring — evaluate impact, effort, confidence, risk, and strategic fit for each candidate in parallel rather than walking the backlog in order. The ranking itself, dependency resolution, and opportunity-cost tradeoffs are a single aggregate pass once every candidate is scored, because ordering and dependency detection are cross-candidate operations.

**Acceptance bar.** Every candidate has a score or rank on every stated criterion, every score names the evidence and confidence behind it, and every dependency or blocker names the candidates it links. An estimate carried in without a source is labeled an assumption, not treated as data.

## Outputs

- prioritization matrix
- ranked feature list
- decision record
- tradeoff notes
- handoff recommendations

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- candidates
- criteria
- scores
- ranked_order
- dependencies
- decision_record

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — the ranking is being converted into a commitment, a roadmap change, or a customer-facing promise and needs its named decision owner.
- **Production or destructive** — the request is to act on the ranking by closing, cancelling, or descoping committed work rather than to produce the ranking.
- **Security or privacy** — candidate evidence carries customer-identifying or confidential material that would be exposed in the matrix.
- **Source conflict** — customer, business, and technical evidence materially disagree on a candidate's impact or feasibility. Preserve the disagreement in the record and mark the candidate contested rather than averaging it away.
- **Release integrity** — the ranking would be published as a delivery commitment without delivery validation behind it.
- **Connector unreachable** — a required evidence source for a candidate exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. A missing effort estimate, criterion weight, or decision owner is a labeled assumption plus an open question against that candidate — score it with the assumption visible and let the owner correct one cell rather than restarting the exercise.

## Downstream handoffs

- roadmap-planning-desk
- prd-desk
- issue-planning-desk
- experiment-design-desk

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
