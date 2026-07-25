---
name: persona-segmentation-desk
description: define personas, customer segments, ICPs, jobs-to-be-done, journey stages, use cases, and segment-specific product needs from research and market evidence.
---

# Persona Segmentation Desk

## Role

Define personas, segments, ICPs, use cases, jobs-to-be-done, and journey stages. Keep segmentation tied to evidence and product decisions rather than decorative persona documents.

## Use when

- A product workflow needs target user clarity.
- Discovery or roadmap decisions depend on segment differences.
- Messaging, requirements, or launch planning needs segment-specific needs.

## Do not use when

- The audience is already fixed and no segment-level decision is needed.
- There is no customer, research, usage, or market evidence.
- The task is demographic labeling without product implications.

## Required evidence

- User research, customer data, sales/support signals, or market evidence.
- Business model, buyer/user distinction, and deployment context.
- Use cases, workflows, pains, jobs, and adoption constraints.
- Decision that segmentation must support.

## Workflow

**Outcome.** A segmentation that serves a named decision: segments or personas defined by behavior and need, each with its evidence and confidence, mapped to concrete product and GTM implications, plus the gaps that need research.

**Constraints.** State the decision the segmentation must support, a persona set that changes no decision is decoration. Keep buyer, user, admin, and payer roles distinct wherever the business model separates them; conflating them is the most common way this artifact goes wrong. Segments are clustered on behavior, need, and context rather than on demographics that carry no product implication. A persona built from inference rather than observation is labeled as a hypothesis, and stays labeled when it is handed downstream.

**Parallel surface.** Segments and personas are independent once the clustering axes are set, develop the evidence, needs, jobs, journey stages, and implications for each in parallel rather than one persona at a time. Choosing the clustering axes, selecting the ICP, and de-duplicating overlapping segments are aggregate steps over the full set, because overlap and priority are only visible across all segments at once.

**Acceptance bar.** Every segment names the evidence that distinguishes it from its neighbors, every persona carries a confidence label, and every stated need maps to a product or GTM implication. Two segments that cannot be told apart by a decision are merged or the distinction is explained.

## Outputs

A complete run delivers the full segmentation, not one persona at a time:

- **persona or segment map**: the clustering axes and why they were chosen, each segment with its defining attributes, its size or share where evidence supports one, and the boundary between it and its neighbors.
- **ICP hypothesis**: which segment is the target, on what basis, and what would disconfirm the choice.
- **jobs-to-be-done summary**: per segment: the job, the current alternative, and the trigger, in the customer's framing rather than the product's.
- **journey notes**: where each segment enters, what they hit, and where they drop.
- **segment implication matrix**: what each segment implies for product, messaging, and pricing.

Complete means a PM or marketer could act on any single segment without a follow-up round trip. A persona with demographics and no job is decoration. Segments develop in parallel once the axes are fixed, across the surface already declared; axis choice, ICP selection, and de-duplication are aggregate over the full set.

Delivering a persona for every segment is not license to write one. Personas are built from research, usage, sales, and support evidence. A segment with no evidence is listed as an unvalidated hypothesis with the research that would validate it, and it gets no quotes, no behaviors, and no size; an invented persona becomes a fiction the whole company then builds against.

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- segments
- personas
- jobs_to_be_done
- journey_stages
- segment_needs
- confidence_notes

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval**: the segmentation is being used to change roadmap scope, pricing, packaging, or targeting and needs its named decision owner.
- **Production or destructive**: the request is to apply the segmentation to live systems, campaigns, or account records rather than to define it.
- **Security or privacy**: the segmentation would be built from or would expose personal data, or would encode an attribute whose use is legally or ethically restricted.
- **Source conflict**: research, usage, and sales evidence genuinely disagree on who the customer is or on which role decides. Carry both segmentations rather than merging them into a persona nobody recognizes.
- **Release integrity**: a hypothesis persona is about to be handed downstream as a validated segment.
- **Connector unreachable**: a required research, analytics, or CRM source exists but cannot be read.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. Thin evidence produces explicitly labeled hypothesis personas plus the research that would confirm them; that is this desk's output, not a reason to stop. Conflated buyer, user, and admin roles are separated on a stated assumption and the assumption is flagged for confirmation.

## Downstream handoffs

- prd-desk
- gtm-brief-desk
- pricing-packaging-desk
- user-research-desk

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
