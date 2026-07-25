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

**Outcome.** A PRD that a downstream desk can act on without re-interviewing the author: problem, users, goals and non-goals, identified requirements with acceptance criteria, source evidence, risks, dependencies, open questions, and success metrics.

**Constraints.** Non-goals are written explicitly, a PRD that only says what is in scope has not bounded anything. Acceptance criteria are testable statements about observable behavior, not restatements of the requirement. Keep the requirement (what must be true) separate from the design (how it is achieved) so architecture retains its decisions. Never invent a requirement ID, an owner, a date, or a metric target that no source states; an unresolved value is an open question with a named decision owner.

**Parallel surface.** Requirements are independent drafting units, each user need or capability area can be written up with its own acceptance criteria, evidence links, and risks in parallel rather than walking the list top to bottom. Requirement ID assignment, the dependency map, the non-goals section, and the consistency pass across requirements are a single aggregate step, because IDs must not collide and a dependency or contradiction is only visible across the complete set.

**Acceptance bar.** The PRD is done when every requirement has a unique ID and at least one testable acceptance criterion, every requirement traces to evidence or a labeled assumption, every open question names its decision owner, and the non-goals are specific enough to refuse work with. Ambiguity that survives is recorded as an open question rather than resolved silently.

## Outputs

A complete run delivers the whole document, not a section of it. These are parts of one PRD and ship together:

- **PRD**: problem, users, goals, and the requirement set, written so a downstream desk needs no interview.
- **requirement IDs**: unique and stable, assigned across the complete set so nothing collides.
- **acceptance criteria**: at least one per requirement, testable and about observable behavior rather than restating the requirement.
- **non-goals**: specific enough to refuse work with. A PRD that only states scope has bounded nothing.
- **risk list**: each risk with its impact and what would mitigate or detect it.
- **open question list**: each with a named decision owner and what it blocks.
- **handoff notes**: what discovery, architecture, issue planning, or test strategy needs from this document.

Depth bar: no requirement is a heading with an intent underneath it. A requirement a downstream desk would have to come back and ask about is unfinished. Requirements draft in parallel across the surface already declared; ID assignment, the dependency map, and the consistency pass are the single aggregate step.

Filling every section is never a reason to invent one. A requirement ID, an owner, a date, a metric target, or an acceptance threshold that no source states becomes an open question with a named owner, not a plausible value. A fabricated success metric propagates through issue planning into what actually gets built and measured.

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

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval**: the PRD is being accepted as committed scope, or it encodes a pricing, contractual, regulatory, or customer-facing commitment, and needs its named decision owner.
- **Production or destructive**: the request is to act on the requirements, open issues, start implementation, change live configuration, rather than to specify them.
- **Security or privacy**: the requirements involve personal data, credentials, or regulated material and the handling constraints are unresolved rather than merely unwritten.
- **Source conflict**: stakeholder, research, and delivery sources genuinely disagree on scope or value. Record both positions against the affected requirement and name the decision owner; do not resolve a scope conflict by authorial choice.
- **Release integrity**: the PRD would be handed downstream as implementation-ready while resting on discovery or architecture questions that are still open. Mark those requirements provisional instead.
- **Connector unreachable**: a required research, analytics, issue, or repository source exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. A missing target user, problem statement, or acceptance criterion is a labeled assumption plus an open question with a named owner; write the requirement with the assumption visible so it can be corrected in one line rather than blocking the whole document.

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
