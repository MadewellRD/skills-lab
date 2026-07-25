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

**Outcome.** A retrospective that reconstructs what was intended, compares it against what happened, explains the gap, and converts the explanation into lessons and owned follow-up actions for the next cycle.

**Constraints.** Reconstruct the original goals and decision context from the artifacts of the time, not from hindsight — a goal quietly rewritten to match the outcome makes the retrospective worthless. Keep product, process, delivery, and GTM lessons separate; they have different owners and different fixes. Where the evidence genuinely disagrees about whether something succeeded, record both readings rather than picking the flattering one. Never state an outcome metric that no source reports.

**Parallel surface.** Each original goal, commitment, or success metric is an independent comparison against its own outcome evidence, and the evidence streams (product metrics, customer feedback, delivery facts, support and sales signal) are independently gatherable — work them in parallel rather than in sequence. Lesson synthesis, theme grouping, and the action list with owners are a single aggregate pass, because a lesson is a pattern across comparisons rather than a property of any one of them.

**Acceptance bar.** Every outcome claim cites its metric or evidence source, every lesson names the specific event that produced it, and every action item has an owner and a next-cycle destination. A lesson with no evidence behind it is labeled an opinion of the room, not a finding.

## Outputs

A retrospective run delivers all five, since lessons without owned actions are how the same retrospective gets written again next cycle:

- **product retrospective** — the period, what was committed, what shipped, and the gap between them.
- **outcome summary** — each original goal or success metric against its actual result, with the measurement source and window.
- **lesson list** — each lesson stated as a pattern with the evidence across cases that supports it, distinguished from a single anecdote.
- **action-item tracker** — per action: the owner, the change it makes, the by-when, and the lesson it answers. An action with no owner is a wish.
- **next-cycle recommendations** — what to do differently, routed to the desk or process that owns it.

Depth bar: the team could pick up the tracker and start on Monday. Per-goal comparisons and the separate evidence streams gather in parallel across the surface already declared; lesson synthesis, theme grouping, and the action list are the aggregate pass.

Producing every section never means constructing the record. Metric outcomes, ship dates, incident counts, and customer reactions come from delivery, analytics, and support evidence. A goal with no measured outcome is reported as unmeasured, and a lesson without evidence across cases stays an observation — a retrospective that invents its outcomes teaches the wrong lesson to everyone who reads it.

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

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — a follow-up action commits another team's capacity, changes roadmap scope, or creates an external commitment and needs its named owner. Propose the action with the owner named; do not book the commitment.
- **Production or destructive** — the request is to execute the follow-ups rather than to define them.
- **Security or privacy** — the retrospective would expose personal data, customer-identifying incident detail, or individual performance material. Retrospectives describe systems and decisions, not people.
- **Source conflict** — metrics, customer feedback, and delivery evidence genuinely disagree on whether the launch or experiment succeeded. Record both verdicts with their evidence and mark the outcome contested; a retrospective that resolves this silently teaches the wrong lesson.
- **Release integrity** — a success or failure verdict is requested that the outcome evidence cannot carry.
- **Connector unreachable** — a required analytics, issue, release, or feedback source exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. Missing original goals or outcome metrics mean reconstructing them from the artifacts available, labeling the reconstruction as such, and continuing — a retrospective with a stated evidence gap is more useful than no retrospective.

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
