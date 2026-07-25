---
name: gtm-brief-desk
description: create go-to-market briefs with audience, positioning, messaging, channels, sales and support enablement, launch risks, success metrics, and product handoffs.
---

# GTM Brief Desk

## Role

Create go-to-market briefs for product launches or major changes. Translate product scope into audiences, positioning, messaging, channels, enablement, risks, metrics, and launch handoffs.

## Use when

- A launch or product change needs GTM coordination.
- Sales, marketing, support, or customer success need enablement inputs.
- Positioning or messaging must connect to product evidence.

## Do not use when

- The product scope is not defined.
- The work is purely brand copy with no product launch context.
- Launch readiness gates are the main unresolved issue.

## Required evidence

- Product scope, target audience, personas, differentiators, and launch goals.
- Competitive, pricing, customer, support, and sales evidence.
- Channel plan, timing, enablement needs, risks, and success metrics.
- Approval owners for messaging and launch scope.

## Workflow

**Outcome.** A GTM brief that states the audiences, the product story and positioning, the proof points behind each claim, the enablement each function needs, the success metrics, and the launch risks, ready to hand to launch readiness.

**Constraints.** Every differentiator and proof point traces to product, customer, or competitive evidence; a claim that cannot be sourced does not ship in messaging, regardless of how well it reads. Keep positioning consistent across audiences, segment-specific emphasis is fine, contradictory promises are not. Messaging that touches pricing, legal, regulatory, or compliance language belongs to its named approver, not to this desk.

**Parallel surface.** Audiences, personas, and channels are independent, develop the message, objections, and enablement needs for each in parallel rather than sequentially. The positioning consistency check, the shared messaging pillars, and the combined risk and metric set are a single aggregate pass once every audience is drafted, because contradictions between audiences are only visible across the whole brief.

**Acceptance bar.** Every messaging claim names its evidence, every audience has a stated need and channel, every enablement item names the owning function, and every success metric has a source of truth for measurement. Unresolved pricing, legal, or support gates appear in the brief as named open items rather than being written around.

## Outputs

A complete run delivers the whole go-to-market package, since the pieces only hold up against each other:

- **GTM brief**: the launch, its positioning, the audiences, the channels, and the success measures.
- **messaging pillars**: each claim with the proof point behind it and the objection it has to survive.
- **audience map**: per audience: who they are, what they do today, the message, and the channel that reaches them.
- **enablement checklist**: what sales, support, and success each need before launch, with owners.
- **launch risk notes**: what could go wrong in market, the early signal for each, and the response.

Complete means a marketer could brief a channel and a seller could hold the conversation without a follow-up round trip. A pillar with no proof point is an unfinished claim. Audiences, personas, and channels fan out across the parallel surface already declared; the positioning consistency check runs once across the whole brief.

Every claim needs a basis. Customer proof points, competitive comparisons, performance numbers, and availability dates come from evidence, or are flagged unconfirmed and held out of anything customer-facing. A proof point invented to complete a pillar does not stay internal; it becomes a public claim the company cannot support.

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- audiences
- positioning
- messaging
- channels
- enablement_needs
- success_metrics

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval**: messaging, pricing language, or claims subject to legal, regulatory, or compliance review are being treated as final without their named approval owner.
- **Production or destructive**: the request is to publish, send, or distribute launch material rather than to draft the brief.
- **Security or privacy**: customer names, references, logos, or account detail would be used externally without confirmed permission.
- **Source conflict**: product, pricing, and launch sources genuinely disagree on what is shipping, when, or at what price. A GTM brief that averages a scope conflict ships a promise nobody made.
- **Release integrity**: a launch claim would go external on evidence that cannot carry it, or the brief would assert a launch date that the release evidence does not support.
- **Connector unreachable**: a required product, pricing, competitive, or customer source exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. Unclear scope, audience, or launch goal is a labeled assumption plus an open question with a named owner. A differentiation claim without evidence is neither a halt nor a claim: it is recorded as unsupported and kept out of the messaging pillars until the evidence exists.

## Downstream handoffs

- launch-readiness-desk
- pricing-packaging-desk
- Customer Support Command Desk
- Customer Success Command Desk
- Marketing Growth Command Desk

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
