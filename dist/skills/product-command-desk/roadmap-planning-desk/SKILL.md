---
name: roadmap-planning-desk
description: create roadmap plans with themes, sequencing, milestones, dependencies, capacity constraints, confidence, risks, decision records, and delivery handoffs.
---

# Roadmap Planning Desk

## Role

Plan product roadmaps by translating strategy, requirements, capacity, dependencies, risks, and evidence into themes, sequence, milestones, and decision records.

## Use when

- A team needs initiative sequencing or roadmap shape.
- Multiple product opportunities must be ordered against constraints.
- Stakeholders need roadmap rationale and dependency visibility.

## Do not use when

- There is only one already-approved implementation task.
- No priorities, constraints, capacity, or decision owner exists.
- The user expects delivery dates without engineering input.

## Required evidence

- Product goals, initiatives, opportunity sizes, customer commitments, and strategic constraints.
- Delivery capacity, dependencies, technical constraints, and risk evidence.
- Priority criteria, timing windows, and decision owner.
- Existing roadmap or milestone state.

## Workflow

**Outcome.** A roadmap with a stated horizon and decision criteria, work grouped into themes and initiatives, a defended sequence, milestones, and an explicit record of the tradeoffs, dependencies, and confidence behind the order.

**Constraints.** State the horizon and the criteria before the sequence, so the order can be argued with rather than merely accepted. Capacity assumptions are written down as assumptions and attributed. Never produce a delivery date that engineering evidence does not support, offer a sequence, a confidence band, or a named dependency instead, and say which it is. A roadmap that conflicts with an accepted commitment surfaces the conflict rather than quietly resequencing around it.

**Parallel surface.** Initiatives are independent for characterization, value, effort, risk, dependency edges, and evidence can be established for each in parallel rather than one initiative at a time. Sequencing, capacity fit, milestone assignment, and cross-initiative dependency resolution are inherently aggregate and run as a single pass once every initiative is characterized, because an ordering is a property of the whole set.

**Acceptance bar.** Every initiative carries its value rationale, dependencies, and confidence; every sequencing decision names the criterion that drove it; and every date or milestone names the delivery evidence or the labeled assumption behind it. Tradeoffs that were rejected are still visible in the record.

## Outputs

A planning run delivers the complete roadmap, not a themed list:

- **roadmap plan**: the initiatives, their order, and the horizon each sits in, with what the plan is optimizing for stated.
- **theme map**: initiatives grouped under the outcome each serves, so the plan reads as strategy rather than as a queue.
- **sequencing rationale**: why this order: the dependency, capacity, risk, or value reason behind each placement, including what was deliberately deferred.
- **milestone proposal**: the checkpoints, what is true at each, and the decision each one enables.
- **risk and dependency list**: cross-initiative dependencies, external dependencies, and the risks that would break the sequence, each with an owner.

Complete means a delivery lead could plan against this and a stakeholder could see what they are not getting. An initiative on a timeline with no value, effort, or dependency behind it has not been planned. Initiatives characterize in parallel across the surface already declared; sequencing, capacity fit, milestone assignment, and dependency resolution are the aggregate pass.

Delivering the full plan is not permission to invent its inputs. Capacity, team availability, effort estimates, delivery dates, and dependency commitments come from evidence or are labeled as assumptions with the owner who can confirm them. A milestone date presented as planned when no team committed to it becomes an external promise made on nobody's authority.

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- roadmap_horizon
- themes
- initiatives
- sequence
- dependencies
- capacity_assumptions
- confidence

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval**: the roadmap is being adopted as a commitment, communicated externally, or used to change accepted scope, and needs its named decision owner.
- **Production or destructive**: the request is to execute the resequencing, cancel, descope, or reassign committed work, rather than to plan it.
- **Security or privacy**: the roadmap would expose customer-specific commitments, contract terms, or confidential partner detail to an audience that should not see them.
- **Source conflict**: the roadmap conflicts with an accepted commitment or a release constraint, or sources genuinely disagree on what is already committed. Surface the conflict and name the owner; do not resequence around a commitment silently.
- **Release integrity**: a delivery date or milestone is requested that engineering evidence cannot support. Produce a sequence, a confidence band, or a named dependency instead, and say which it is. Never emit a date that no source supports.
- **Connector unreachable**: a required issue, release, or capacity source exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. Missing capacity figures, dependency detail, or priority criteria are labeled assumptions attached to the affected initiative plus an open question with a named owner, not a stop.

## Downstream handoffs

- feature-prioritization-desk
- issue-planning-desk
- release-operations-desk
- prd-desk

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

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
