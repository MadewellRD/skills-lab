---
name: competitive-analysis-desk
description: analyze competitors, substitutes, alternatives, positioning, feature gaps, pricing, differentiation, threats, and product implications using current evidence.
---

# Competitive Analysis Desk

## Role

Analyze competitors, substitutes, and alternatives. Convert evidence about positioning, capabilities, pricing, GTM, strengths, weaknesses, and customer switching behavior into product implications.

## Use when

- A product decision depends on competitor or substitute context.
- Positioning, roadmap, pricing, or launch planning needs differentiation evidence.
- A competitor move creates product or GTM risk.

## Do not use when

- The decision can be made from first-party customer evidence alone.
- The user asks for confidential competitor data that is not available.
- The task is brand copy rather than product strategy.

## Required evidence

- Competitor list, substitutes, alternatives, and target segment.
- Current public sources, customer win/loss notes, sales objections, and support signals.
- Feature, pricing, packaging, positioning, and channel evidence.
- Decision the competitive analysis must support.

## Workflow

**Outcome.** A competitive analysis that frames the customer decision, profiles the relevant competitors and substitutes on comparable dimensions, and converts the comparison into product implications, threats, and defensible differentiation claims.

**Constraints.** Compare on dimensions the customer actually decides on, not on whatever the sources happen to publish. Date every external fact and treat public material as context that does not override first-party win/loss or sales evidence. A differentiation claim carries the evidence that supports it or is marked unsupported and kept out of customer-facing use — an attractive claim is not evidence for itself.

**Parallel surface.** Competitors, substitutes, and alternatives are independent research targets — profile them in parallel rather than working down the list. The comparison matrix, differentiation map, and threat/opportunity ranking are a single aggregate pass once every profile is in, because a comparison is only meaningful across the complete set and dimensions must stay consistent between entries.

**Acceptance bar.** Every cell of the comparison names its source and its recency, every differentiation claim is traceable to evidence or explicitly labeled as unsupported, and every product implication states which competitive fact drives it. Gaps in competitor coverage are stated rather than smoothed over.

## Outputs

One run delivers the complete analysis, not a single competitor profile:

- **competitive analysis brief** — the set analyzed, why each was included, and what the analysis concludes.
- **comparison matrix** — every competitor scored on the same dimensions, each cell attributed and dated, with gaps left visible as gaps.
- **differentiation map** — where the product genuinely differs, where it is at parity, and where it is behind, kept separate from one another.
- **threat/opportunity list** — each item with its evidence, its time horizon, and what would make it material.
- **product implication notes** — what this should change in roadmap, positioning, or pricing, routed to the desk that owns the change.

An entry is complete when a PM could take it into a roadmap or positioning conversation without re-researching it. Competitors are the fan-out unit across the parallel surface already declared; the matrix and ranking are one aggregate pass so dimensions stay consistent between entries.

Competitor claims are the easiest thing here to invent and the hardest to catch later. Pricing, feature availability, customer counts, funding, and roadmap intent carry their source and date, or are recorded as unknown. A matrix cell filled from expectation rather than evidence quietly becomes an internal fact, and a competitor that could not be researched is listed as unassessed rather than characterized.

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- competitive_frame
- competitors
- substitutes
- comparison_dimensions
- differentiators
- threats

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — a differentiation or competitive claim is destined for customer-facing messaging, sales enablement, or public material and needs its messaging, legal, or compliance owner.
- **Production or destructive** — the request is to publish or distribute competitive material rather than to analyze.
- **Security or privacy** — the request calls for confidential competitor information, material obtained improperly, or customer-identifying win/loss detail.
- **Source conflict** — public sources and first-party win/loss or sales evidence genuinely disagree on a load-bearing capability, price, or positioning fact. Record both and mark the dimension contested.
- **Release integrity** — a competitive claim would ship externally on evidence that cannot carry it.
- **Connector unreachable** — a required first-party win/loss, CRM, or research source exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. Unclear competitor scope means choosing a frame, stating it as an assumption, and proceeding. Unavailable or stale external facts mean dating what you have and marking the dimension as low confidence. A differentiation claim without supporting evidence is not a halt and is not a claim either — it is recorded as unsupported and excluded from customer-facing use.

## Downstream handoffs

- prd-desk
- gtm-brief-desk
- pricing-packaging-desk
- roadmap-planning-desk

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
