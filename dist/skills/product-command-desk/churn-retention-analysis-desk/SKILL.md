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

**Outcome.** A retention analysis that names the churn and retention drivers, ties each to cohort, usage, or feedback evidence, and converts them into candidate interventions with experiment or roadmap inputs.

**Constraints.** Keep the retention question and the affected segments explicit — an analysis that does not say who churned is not an answer. Hold the line between an observed drop-off and an explanation of it: a correlation inside a cohort is evidence, never a cause on its own. Interventions that touch pricing, contracts, or customer commitments are proposals for a named owner, not decisions this desk makes.

**Parallel surface.** Cohorts, lifecycle stages, customer segments, and plan tiers are independent units of analysis — profile them in parallel rather than walking the funnel one cohort at a time. The churn-driver taxonomy, cross-cohort ranking, and expected-impact estimate are a single aggregate pass once every cohort has been profiled, because each depends on the complete set.

**Acceptance bar.** Every named driver cites the cohort, metric, or feedback source it rests on and carries a confidence label. Every intervention names the driver it addresses and the metric that would show it worked. A driver with no evidence behind it appears as a labeled hypothesis, not as a finding.

## Outputs

A complete run delivers all five together — a driver taxonomy with no intervention map leaves the reader exactly where they started:

- **retention analysis** — retention and churn by cohort and segment over a stated window, with the churn definition used and the population each figure covers.
- **churn driver taxonomy** — named drivers with the evidence behind each, its strength, and whether the relationship is observed correlation or inferred cause, labeled as such.
- **cohort insight summary** — what actually differs between the cohorts that retain and those that do not.
- **intervention map** — per driver: the candidate intervention, the mechanism it acts on, the owning team, and the expected effect with its basis.
- **experiment recommendations** — the interventions worth testing first, each with the metric that would confirm it, shaped for `experiment-design-desk` to pick up.

Depth bar: a retention owner could choose an intervention and brief a team from this without a follow-up round trip. Cohorts fan out across the parallel surface already declared; the taxonomy and cross-cohort ranking are the aggregate pass once every cohort is profiled.

Completing the set is never a reason to produce a number. Retention rates, cohort sizes, churn reasons, and revenue impact come from the analytics, billing, or research evidence actually available. Where a cut cannot be computed, it is reported as unavailable and the driver that depended on it stays a hypothesis — a plausible churn rate is indistinguishable from a real one on the page, and will be acted on as real.

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

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — an intervention that changes pricing, contract terms, entitlements, or customer commitments requires its named owner in pricing, legal, or customer success before it is presented as decided.
- **Production or destructive** — the request moves from analysis to acting on customers directly: outreach, save offers, plan changes, or account modifications.
- **Security or privacy** — the cohort, usage, or cancellation evidence carries personal data that would be exposed in the artifact. Aggregate or strip it; do not reproduce it to make a point.
- **Source conflict** — analytics, support, and customer-success evidence genuinely disagree about why a cohort left. Preserve both attributions rather than resolving to the convenient one.
- **Release integrity** — a retention commitment, forecast, or save-rate target is requested and the cohort evidence cannot support it.
- **Connector unreachable** — a required analytics, CRM, or support source exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. Missing cohort, usage, or feedback data means the analysis proceeds on what exists with the coverage limitation stated and the affected drivers marked low confidence. Churn that cannot yet be separated from an incident or support failure is recorded as a competing explanation carried forward, not a reason to stop.

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

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
