---
name: market-discovery-desk
description: create market discovery artifacts covering category context, customers, alternatives, trends, constraints, demand signals, and opportunity framing for product decisions.
---

# Market Discovery Desk

## Role

Map the market context around a product opportunity. Identify category dynamics, target customers, alternatives, trends, constraints, demand signals, adoption blockers, and unresolved market assumptions.

## Use when

- A product idea needs market context before requirements or roadmap decisions.
- A team is entering or repositioning within a market/category.
- Stakeholders need opportunity framing grounded in evidence.

## Do not use when

- The request already has accepted market research and needs implementation planning.
- The work is purely internal tooling with no market/customer decision.
- The user needs a legal, investment, or regulatory opinion.

## Required evidence

- Target category, users, buyers, customer problem, and business objective.
- First-party customer or sales signals when available.
- Public market, competitor, substitute, and trend sources.
- Constraints such as geography, segment, budget, regulation, and channel.

## Workflow

**Outcome.** A market discovery brief that answers a named market question: category map, customer and buyer hypotheses, alternatives and substitutes, demand signals, adoption constraints, and the research gaps that remain.

**Constraints.** Keep the market question and the decision it serves visible throughout, market context with no decision attached is trivia. Date external facts and label their freshness; public market material informs but does not outrank first-party customer or sales signal. Keep the buyer distinct from the user and from the payer where the business model separates them. A hypothesis stays labeled as a hypothesis no matter how many sources repeat it.

**Parallel surface.** Category segments, customer types, buyer roles, alternatives, substitutes, and individual trend sources are independent research targets, investigate them in parallel rather than one at a time. The opportunity framing, demand-signal synthesis, and research-gap list are a single aggregate pass once the fan-out returns, because each is defined against the whole picture.

**Acceptance bar.** Every claim is marked as observed evidence, inference, or hypothesis, and carries a source with a date where freshness matters. Every research gap names what would close it. The brief is complete when a reader can tell which parts of the market picture are known and which are assumed without asking.

## Outputs

One run delivers the full discovery picture:

- **market discovery brief**: the market as currently understood, what is established, and what remains hypothesis.
- **category map**: segments, adjacent categories, alternatives and substitutes, and where the product sits among them.
- **customer and buyer hypothesis**: who has the problem, who buys, who blocks, and the evidence for each, with hypotheses labeled as hypotheses.
- **demand signal summary**: the signals found, their source and date, and how strongly each supports demand.
- **research gap list**: what is not known, why it matters to the decision, and the research that would close it.

Complete means a PM could decide whether to pursue this market, or knows precisely what to learn first. A category map that lists names without placing the product among them has answered nothing. Segments, buyer roles, alternatives, and trend sources fan out across the parallel surface already declared; the framing, synthesis, and gap list are the aggregate pass.

Market numbers are unusually easy to state and hard to source. Market size, growth rate, adoption figures, and competitor traction carry their source and date or are recorded as unknown, because a plausible TAM figure with no citation gets quoted in a funding conversation. Where the evidence is thin, report the demand signal as weak rather than describing a market nobody measured.

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- market_question
- category
- customer_hypotheses
- demand_signals
- market_constraints
- research_gaps

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval**: the brief is being used to commit to entering, exiting, or repositioning in a market and needs its named decision owner.
- **Production or destructive**: the request is to act on the discovery externally rather than to produce it.
- **Security or privacy**: the research would use confidential, improperly obtained, or customer-identifying material.
- **Source conflict**: first-party signal and external market sources genuinely disagree on demand, category boundaries, or buyer behavior. Record both; a market picture built by dropping the inconvenient source is not discovery.
- **Release integrity**: a market conclusion is about to be presented as established fact when the evidence supports only a hypothesis.
- **Connector unreachable**: a required first-party customer, sales, or research source exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. An unclear category, customer, or decision target means choosing a frame, stating it as an assumption, and proceeding. Unavailable or dated market facts mean labeling freshness and marking those claims low confidence; weak evidence is a reason to label carefully, not a reason to stop.

## Downstream handoffs

- user-research-desk
- opportunity-sizing-desk
- competitive-analysis-desk
- persona-segmentation-desk

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
