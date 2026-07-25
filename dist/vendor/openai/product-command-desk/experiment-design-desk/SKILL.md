---
name: experiment-design-desk
description: design product experiments with hypotheses, metrics, cohorts, variants, guardrails, duration, analysis rules, ethical constraints, and decision criteria.
---

# Experiment Design Desk

## Role

Design product experiments that answer decision-relevant uncertainty. Define hypotheses, metrics, cohorts, variants, guardrails, duration, analysis rules, risk controls, and decision criteria.

## Use when

- A product decision has uncertainty that can be tested.
- A feature, pricing, onboarding, retention, or messaging change needs experiment design.
- An experiment needs guardrails and decision rules before launch.

## Do not use when

- The decision cannot be ethically or practically tested.
- No measurable outcome or target population exists.
- The user wants to run an experiment without guardrails or approval.

## Required evidence

- Decision question, hypothesis, target population, variants, and constraints.
- Primary, secondary, and guardrail metrics.
- Sample size, duration, segmentation, instrumentation, and analysis needs.
- Risk, ethics, compliance, and user impact constraints.

## Workflow

**Outcome.** An experiment plan that resolves a named decision: hypothesis, population, variants, primary and guardrail metrics, duration, analysis plan, stopping rules, and the decision rule that will be applied to the result.

**Ordered gate (mandated, keep this order).** Guardrail metrics, stopping rules, risk controls, and any required ethics or compliance review are fixed *before* a variant is exposed to a single user, and the analysis and decision rules are fixed *before* results are seen. This ordering is not stylistic: exposure to real users cannot be undone, and rules written after the data is visible are not rules. Do not present a plan as launch-ready with these items deferred.

**Constraints.** The experiment must be able to change the decision, if no outcome would alter what the team does, say so instead of designing it. Keep primary, secondary, and guardrail metrics distinct, and state the instrumentation each depends on. Never restate an assumed conversion rate, baseline, or sample size as if it were measured.

**Parallel surface.** Where several decisions, variants, or candidate metric definitions are in scope, each is an independent design unit and can be worked in parallel. Power, duration, and traffic allocation are an aggregate pass once the full metric and variant set is settled, because they are constrained by the whole design rather than by any one arm.

**Acceptance bar.** The plan passes when the hypothesis is falsifiable, every metric names its instrumentation source, guardrails and stopping rules are explicit, and the decision rule states in advance what result leads to which action. A plan that cannot state what would falsify it is not finished.

## Outputs

A complete run delivers the experiment as a runnable design. These ship together because the design is only valid as a whole:

- **experiment plan**: what is being tested, on whom, for how long, and what happens at the end.
- **hypothesis and metric tree**: the falsifiable hypothesis, the single primary metric, the secondary metrics, and how each is computed.
- **cohort and variant design**: assignment unit, randomization, exposure, exclusions, and sample size with the effect size and power it assumes.
- **guardrail list**: the metrics that must not degrade, their thresholds, and the stop rule if one breaches.
- **decision rules**: written before the experiment runs: what result ships, what result kills, what result is inconclusive, and who decides.

The bar is that an analyst could instrument and run this without a follow-up round trip, and that nobody could reinterpret the outcome after seeing it. Variants and candidate metric definitions fan out across the parallel surface already declared; power, duration, and traffic allocation are the aggregate pass over the settled set.

Every section is delivered and none is fabricated. Baseline conversion rates, traffic volumes, and historical effect sizes come from analytics evidence or are recorded as unavailable. Where the baseline is unknown, the sample size is stated as blocked on it rather than computed from an invented figure; an experiment powered off a made-up baseline returns a confident wrong answer that nobody questions.

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- hypothesis
- population
- variants
- metrics
- guardrails
- analysis_plan
- decision_rules

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval**: the experiment requires ethical, legal, compliance, or launch approval, or exposes users to a pricing, contractual, or safety-relevant variation. Design freely; do not present it as cleared.
- **Production or destructive**: the request is to launch, enroll users, or start exposure rather than to design. Exposure to real users is irreversible and belongs behind the ordered gate above.
- **Security or privacy**: the cohort definition, instrumentation, or analysis would collect or expose personal data beyond what the design justifies.
- **Source conflict**: baseline metrics or population definitions genuinely disagree across sources, so the experiment would be powered against a number nobody agrees on.
- **Release integrity**: a decisive result is requested from a design that is underpowered, confounded, or otherwise cannot answer the question. Say the design cannot carry the decision rather than shipping a plan that will produce a misleading answer.
- **Connector unreachable**: a required analytics or instrumentation source exists but cannot be read, so power and baselines cannot be established at all.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. A missing metric definition, cohort boundary, or instrumentation detail is a labeled assumption in the plan plus an explicit prerequisite in the launch handoff, not a stop.

## Downstream handoffs

- Data Command Desk
- launch-readiness-desk
- feedback-synthesis-desk
- feature-prioritization-desk

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
