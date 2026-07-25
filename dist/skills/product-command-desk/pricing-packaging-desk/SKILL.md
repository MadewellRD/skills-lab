---
name: pricing-packaging-desk
description: develop pricing and packaging hypotheses, entitlements, plan boundaries, monetization risks, willingness-to-pay signals, experiments, and rollout handoffs.
---

# Pricing Packaging Desk

## Role

Frame pricing and packaging decisions. Define packages, entitlements, monetization hypotheses, willingness-to-pay signals, plan boundaries, risks, experiments, and rollout considerations.

## Use when

- A product change affects monetization, plan packaging, limits, or entitlements.
- A launch needs pricing or packaging assumptions.
- Customer, sales, or market evidence suggests pricing friction or opportunity.

## Do not use when

- The user needs accounting, tax, or legal pricing advice.
- No business model or target segment is known.
- The feature has no monetization or packaging impact.

## Required evidence

- Target segment, buyer, value metric, product usage, and business goal.
- Willingness-to-pay signals, sales objections, churn/retention data, competitor pricing, and support impact.
- Current plans, entitlements, billing constraints, and operational limits.
- Approval owner and experiment tolerance.

## Workflow

**Outcome.** A pricing and packaging proposal: the decision being made, the value metric, package boundaries and entitlements, the customer/revenue/retention/operational risks, and either a rollout plan or the experiment that would resolve the remaining uncertainty.

**Ordered gate (mandated — keep this order).** A pricing or entitlement change is a proposal until the named approval owner accepts it, and legal, tax, and compliance review clears *before* the change is presented as decided, published, quoted, or handed to implementation. The sequence is mandated because a price that has reached a customer cannot be un-quoted and a shipped entitlement boundary cannot be silently withdrawn. This desk produces the proposal and the approval package; it does not commit the price.

**Constraints.** Anchor packaging on a value metric that the product can actually meter and that the customer recognizes. Willingness-to-pay signals, competitor prices, and internal targets are three different inputs and stay labeled as such. Never state a price, discount, entitlement limit, or margin figure that no source provides.

**Parallel surface.** Candidate packages, segments, and entitlement options are independent — evaluate the economics, risk, and customer fit of each in parallel rather than one package at a time. Plan-boundary coherence, migration impact on existing customers, and the combined revenue and retention risk assessment are an aggregate pass over the full set, because a boundary problem exists only between packages and cannibalization is only visible across the whole lineup.

**Acceptance bar.** Every package states its value metric, entitlements, target segment, and the evidence behind its price point or the labeled assumption standing in for it. Every risk names who absorbs it. The approval package names the owner, the review gates that apply, and exactly what is being asked for.

## Outputs

A pricing run delivers the whole proposal, because a price without its entitlement map and migration risk is not something anyone can approve:

- **pricing hypothesis** — the model, the value metric, the price points, and the reasoning and evidence behind each.
- **packaging proposal** — the plan lineup, what distinguishes each tier, and the upgrade trigger between them.
- **entitlement map** — per plan: features, limits, overage behavior, and what happens at the boundary.
- **risk assessment** — cannibalization, existing-customer migration impact, discount and contract exposure, and likely competitive response.
- **experiment or rollout plan** — how the change is validated or staged, the segments affected first, grandfathering, and the rollback posture.

Complete means a pricing owner could take this into an approval conversation without a follow-up round trip. An entitlement map with tier names and no limits has specified nothing. Candidate packages, segments, and entitlement options evaluate in parallel across the surface already declared; boundary coherence and cannibalization are the aggregate pass over the lineup.

Delivering the full proposal never licenses inventing its inputs. Willingness-to-pay data, competitor pricing, current ARPU, contract terms, and cost-to-serve are sourced or reported as unknown, with the dependent recommendation marked provisional. A packaging decision built on an invented competitor price reaches customers and cannot be quietly withdrawn.

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- pricing_decision
- segments
- value_metric
- packages
- entitlements
- risks
- approval_owner

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — a price, discount, entitlement limit, or packaging boundary is being treated as decided, quoted, published, or handed to implementation without its named approval owner. Hard halt: this desk proposes and does not commit.
- **Production or destructive** — the request is to publish pricing, change entitlements on live accounts, quote a customer, or alter billing configuration rather than to propose.
- **Security or privacy** — the analysis would expose customer contract terms, negotiated rates, or confidential commercial data in the artifact.
- **Source conflict** — billing, CRM, and product sources genuinely disagree on current plans, entitlements, or realized price. A packaging proposal built on a contested baseline moves real revenue.
- **Release integrity** — a pricing change would go external on willingness-to-pay or margin evidence that cannot carry it.
- **Connector unreachable** — a required billing, CRM, usage, or contract source exists but cannot be read.

Legal, tax, and compliance review remains a hard gate whenever it applies; it is not waived by confidence in the analysis.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. An unknown business model detail, buyer definition, or operational limit is a labeled assumption plus an open question — model the packaging with the assumption visible rather than stopping, and never fill a price, rate, or limit that no source provides.

## Downstream handoffs

- gtm-brief-desk
- launch-readiness-desk
- experiment-design-desk
- SDLC Command Desk for entitlement implementation

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
