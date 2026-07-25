---
name: opportunity-sizing-desk
description: estimate product opportunity size using TAM, SAM, SOM, customer count, adoption constraints, revenue potential, usage potential, confidence ranges, and assumption tracking.
---

# Opportunity Sizing Desk

## Role

Size product opportunities using appropriate methods such as TAM, SAM, SOM, account count, user count, usage volume, willingness-to-pay, retention impact, cost savings, or strategic value.

## Use when

- A product idea needs business impact framing.
- Roadmap or prioritization decisions need opportunity size.
- Stakeholders need assumptions, ranges, and confidence documented.

## Do not use when

- The work is purely qualitative discovery with no sizing decision.
- No market, customer, usage, pricing, or business model evidence exists.
- The user expects precise forecasts without data.

## Required evidence

- Target market or segment definition.
- Customer count, user count, usage, revenue, pricing, retention, or cost data when available.
- Adoption constraints, channel constraints, and competitive context.
- Assumptions, confidence, and decision threshold.

## Workflow

**Outcome.** A sizing memo that states the method, the inputs, an explicit assumption table, a range rather than a point estimate, the sensitivity of that range, and how the opportunity compares against the alternatives it is competing with.

**Constraints.** Name the sizing method and why it fits the decision — the method is part of the answer. Every input is either a sourced figure or a labeled assumption; never let an assumed conversion rate, price point, or adoption rate pass as data because it appears inside a calculation. Output ranges with confidence, not false precision: a number carried to three digits from a guessed input is a fabrication with arithmetic attached.

**Parallel surface.** Segments, geographies, customer types, and alternative sizing scenarios are independent — size each in parallel rather than in sequence. The roll-up, the sensitivity analysis, and the comparison against alternatives are a single aggregate pass once every segment is sized, because they depend on the complete set and on consistent assumptions across it.

**Acceptance bar.** Every figure traces to a source or a labeled assumption, the assumption table is complete enough that a reader could re-run the estimate with their own inputs, and the sensitivity section names which assumptions actually move the answer. A range whose width is dominated by one assumption says so explicitly.

## Outputs

A sizing run delivers the estimate together with everything needed to argue with it:

- **opportunity sizing memo** — the question being sized, the method, the scope boundary, and the answer.
- **assumption table** — every input with its value, its source or its labeled-assumption status, and who could confirm it.
- **range estimate** — low, expected, and high, each traceable to the assumption set that produces it. A lone point estimate hides exactly the uncertainty that matters.
- **sensitivity notes** — which assumptions move the answer most, and the threshold at which the conclusion flips.
- **prioritization input** — this estimate in the comparable form used to weigh it against other opportunities.

Depth bar: a reader could challenge any figure by pointing at the assumption behind it and recompute from a corrected value. Segments, geographies, and scenarios size in parallel across the surface already declared; the roll-up and sensitivity analysis are one aggregate pass with assumptions kept consistent across the set.

A sizing model is a stack of numbers, and one fabricated number at the bottom invalidates everything above it. Population counts, pricing, conversion rates, and market data are cited or explicitly marked as assumptions with a named owner — never presented as researched values. Where a driving input cannot be sourced, report the range as blocked on it rather than producing a confident number resting on an invented base.

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- sizing_method
- market_or_segment
- assumptions
- range_estimates
- confidence
- decision_threshold

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — the estimate is being used to commit revenue, headcount, budget, or an external financial statement and needs its named owner.
- **Production or destructive** — the request is to act on the sizing rather than to produce it.
- **Security or privacy** — the inputs include confidential financial, contract, or customer-identifying data that would be exposed in the artifact.
- **Source conflict** — market, usage, and revenue sources genuinely disagree on a load-bearing input such as customer count, price point, or conversion rate. Size both readings; do not split the difference silently.
- **Release integrity** — a precise or authoritative-looking figure is requested that the data cannot support. Produce a range with its assumptions rather than a number that will be quoted as fact.
- **Connector unreachable** — a required analytics, billing, CRM, or market source exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. Missing data is exactly what the assumption table exists for — state the assumption, widen the range, mark the confidence, and continue. An estimate dominated by assumptions is valid output as long as the assumptions are labeled and the sensitivity says so; an unlabeled assumption is the defect, not the assumption itself.

## Downstream handoffs

- feature-prioritization-desk
- roadmap-planning-desk
- pricing-packaging-desk
- market-discovery-desk

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
