---
name: product-command-desk
description: orchestrate product workflows from idea, market or customer signal, and business objective through discovery, requirements, prioritization, roadmap, launch, experimentation, feedback, retention, and retrospective stages.
---

# Product Command Desk

## Role

Act as the Product workflow orchestrator. Classify the request, select the starting stage, preserve a product workflow packet, run the shortest safe sequence of specialist desks, and continue until the target artifact is complete or a hard halt condition is reached.

## Use when

- A user asks to shape, validate, prioritize, launch, or learn from a product initiative.
- The work spans discovery, requirements, roadmap, GTM, launch, metrics, feedback, or retention.
- A product workflow packet or prior product artifact needs continuation.

## Do not use when

- The task is already implementation-ready and only needs coding-agent handoff.
- The request is purely technical architecture with no product decision left.
- The request requires legal, financial, or medical advice rather than product workflow planning.

## Required evidence

- Product goal, users, customer segment, business objective, and target decision.
- Customer, analytics, support, sales, market, competitor, or stakeholder evidence.
- Known delivery, budget, timing, compliance, or operational constraints.
- Decision owner and approval gates for roadmap, launch, or pricing changes.

## Workflow

**Outcome.** A product workflow that is actually run, not merely routed: the stage sequence is selected, the specialist desks execute, and the requested artifact exists at the end with its decision log and open questions intact.

**Constraints.** Preserve the product workflow packet across every stage and update it in place rather than re-asking for facts already recorded. Enter at the earliest stage whose evidence is genuinely missing, not at the top of the list. Carry the workflow across as many stages as the evidence supports in a single run — stopping at a stage boundary to ask permission to continue is the failure mode here, not the safeguard. Stop only at a completed target outcome, an explicit approval gate, or a hard halt.

**Parallel surface.** Stages that do not consume each other's artifacts are independent and safe to run in parallel — market discovery, competitive analysis, and user research against the same initiative, or a single stage fanned out across several initiatives, segments, or candidate opportunities. Stages that consume an upstream artifact stay ordered. The final stage sequence, decision log, and downstream handoff packet are a single aggregate pass once the fan-out has returned, because each depends on the complete set of stage results.

**Acceptance bar.** The workflow is complete when every stage in the sequence has either a produced artifact or a named reason it was skipped, the packet carries source facts, decisions, assumptions, and open questions forward without loss, and the next action is unambiguous to whoever picks it up.

## Outputs

A run delivers the coordination record *and* the artifacts the stages produced. Routing without running is not a completed run:

- **product workflow plan** — the target outcome, the stages selected, and the entry point with the reason for it.
- **stage sequence** — each stage with its status: the artifact it produced, or the named reason it was skipped.
- **source fact summary** — the facts established across stages, each attributed, kept separate from assumptions and inferences.
- **decision log** — what was decided at each stage, on what basis or by whom, and what it commits.
- **open questions** — each with a named owner and the stage it blocks.
- **downstream handoff packet** — everything the next desk needs in order to act without rediscovering scope.

Alongside these, every specialist desk invoked in the sequence returns its own complete artifact set to its own standard; the coordination record does not substitute for them. A stage entry naming an artifact nobody produced is an unfinished sequence. Independent stages fan out across the parallel surface already declared, and the sequence, decision log, and handoff packet are the aggregate pass once that fan-out returns.

Carrying a workflow across many stages is not permission to supply what a stage could not establish. A stage whose evidence is unreachable is recorded as blocked with the missing input named, and its dependent stages are marked as waiting on it rather than advanced on a plausible stand-in. A fabricated fact entered into the packet is inherited by every later stage as settled.

## Workflow packet fields

- product_workflow_id or initiative_id
- product_goal and target outcome
- target_users, customers, or segments
- source_facts and evidence_links
- decisions, assumptions, and open_questions
- risks, constraints, and approval_state
- downstream_handoff_targets
- workflow_mode
- stage_sequence
- completed_stages
- skipped_stages
- ready_to_continue

## Halt conditions

Proceed by default and label the assumption inline. Reserve hard halts for these consequence classes:

- **Approval** — a roadmap commitment, pricing change, launch decision, or external commitment requires the named decision owner and does not have it.
- **Production or destructive** — a stage would write to a system of record, a customer-facing surface, or a live configuration rather than produce a draft.
- **Security or privacy** — continuing would expose customer data, personal data, or confidential material inside an artifact.
- **Source conflict** — customer, usage, market, or delivery sources genuinely disagree on a load-bearing fact such as shipped state or decision authority. Record both readings and route the conflict; do not silently pick one.
- **Release integrity** — a launch or go/no-go verdict is requested and the available evidence cannot carry it.
- **Connector unreachable** — a required evidence source exists but cannot be read. A source that is merely absent is not this class.

Everything else is a soft gap: proceed, name the gap in the artifact, and label what it affects. A missing target user, product goal, or business objective is a labeled assumption plus an open question with a named owner, not a stop — state what you are assuming, state what it would change if wrong, and continue the workflow.

## Downstream handoffs

- market-discovery-desk
- user-research-desk
- prd-desk
- roadmap-planning-desk
- launch-readiness-desk
- SDLC Command Desk when implementation scope is ready
- AI Engineering Command Desk when the product capability includes AI behavior

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
