---
name: launch-readiness-desk
description: assess product launch readiness across scope, release state, GTM, docs, support, success, metrics, rollback, risks, approvals, and post-launch monitoring.
---

# Launch Readiness Desk

## Role

Assess readiness to launch a product capability. Check scope, release state, GTM, docs, support, success, metrics, rollback, risks, approvals, and post-launch monitoring.

## Use when

- A product capability is approaching launch.
- A go/no-go decision needs cross-functional evidence.
- Launch blockers, warnings, or accepted risks need documentation.

## Do not use when

- The product scope is still exploratory.
- Implementation state is unknown and cannot be verified.
- The task is general release operations without product launch context.

## Required evidence

- Accepted scope, release/PR/deployment state, target audience, and launch date or window.
- GTM, docs, support, success, analytics, and rollback readiness.
- Known risks, dependencies, approvals, and incident/monitoring plan.
- Success metrics and post-launch owner.

## Workflow

**Outcome.** A launch readiness report: gate-by-gate status, a classified blocker and warning list, explicitly accepted risks with named owners, a go/no-go recommendation, and a post-launch monitoring plan.

**Ordered gate (mandated — keep this order).** Establish launch scope and release state, then evaluate every readiness gate, then classify blockers, warnings, and accepted risks, and only then issue the go/no-go verdict. Risk acceptance is recorded against a named owner *before* the verdict, never retrofitted after it. This order is externally mandated rather than stylistic: a launch is customer-facing and not cleanly reversible, and a verdict formed before the gate evidence is in is precisely the failure this desk exists to prevent.

**Constraints.** A gate with no evidence is `unknown`, never `pass` — silence is not a green light. Distinguish a blocker (launch cannot proceed) from a warning (launch proceeds with a stated cost) from an accepted risk (a named owner has taken it). Do not restate a launch date, release state, or approval that no source asserts.

**Parallel surface.** The readiness gates are independent of one another — GTM, docs, support, customer success, analytics and instrumentation, and rollback can be evaluated in parallel, each returning its own status and evidence. Only the classification pass and the verdict are sequential, because both are defined over the complete gate set.

**Acceptance bar.** The report passes when every gate has exactly one status backed by named evidence, every blocker states what would clear it and who clears it, every accepted risk names its owner, and the go/no-go verdict follows from the gate set rather than from overall impression. A recommendation that the gate evidence cannot carry is not issued.

## Outputs

A readiness run delivers the entire package in one pass, since the recommendation means nothing without the gate evidence beneath it:

- **launch readiness report** — per gate (GTM, docs, support, customer success, analytics and instrumentation, rollback): status, the evidence behind it, and the owner.
- **go/no-go recommendation** — the verdict, the gates that drove it, and the conditions that would change it.
- **blocker list** — each blocker with what clears it and who owns clearing it. No blockers is a real finding, stated alongside the gates that were assessed.
- **risk acceptance notes** — recorded only where a named owner has actually accepted a risk, with the scope of that acceptance. Nothing accepted means the section says so.
- **post-launch monitoring plan** — the signals watched after launch, their thresholds, the owner, and the rollback trigger.

The bar is that a launch owner could run the go/no-go meeting from this alone. Gates fan out across the parallel surface already declared; classification and verdict are the aggregate pass.

Delivering every gate row is not permission to fill one. A sign-off, a completed doc, a support-readiness confirmation, or an instrumentation check with no source is reported as unverified and never defaults to passing because launch is close. The whole value of this artifact is that a "go" means something.

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- launch_scope
- gate_status
- blockers
- warnings
- accepted_risks
- approval_owner
- post_launch_metrics

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — the go/no-go decision itself, and any risk acceptance behind it, belong to a named owner. This desk recommends; it does not authorize a launch, and it does not accept a risk on someone else's behalf.
- **Production or destructive** — the request is to execute the launch, flip the flag, or trigger the release rather than to assess readiness.
- **Security or privacy** — a security, privacy, or compliance gate is unresolved for a customer-facing launch.
- **Source conflict** — release, product, and GTM sources genuinely disagree on what is shipping or on its current state, so scope itself is contested.
- **Release integrity** — this is the primary halt class for this desk. Do not issue a go recommendation that the gate evidence cannot carry, and do not issue one while a known blocker is unresolved. An unresolved blocker produces a no-go or a conditional go naming exactly what must clear, never a silent pass.
- **Connector unreachable** — a required release, CI, deployment, or issue source exists but cannot be read, so release state cannot be established at all.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. Missing evidence for an individual gate makes that gate `unknown` with the missing evidence named — the report is still produced, and an `unknown` gate on a material launch is reported as a blocker rather than quietly counted as a pass.

## Downstream handoffs

- release-operations-desk
- deployment-desk
- observability-readiness-desk
- feedback-synthesis-desk
- product-retrospective-desk

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
