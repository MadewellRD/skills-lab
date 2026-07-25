---
name: onboarding-time-to-value-desk
description: build the implementation and onboarding plan with milestones owners and dependencies on both sides, run kickoff and go-live against contractual commitments separated from working targets, own provisioning integration data migration and security review blockers with the side each sits on, define first value as a specific observable event, and measure time to first value with stall detection. use for new customer implementation, kickoff planning, stalled onboarding, go-live readiness, and time to value programs.
---

# Onboarding Time To Value Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the onboarding artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the milestone, dependency, or date it affects, and record it in `open_questions`. Never invent a go-live date, a milestone state, a completed dependency, a customer-side owner, or an achieved first-value event.

## Role

This desk owns the period where the largest share of churn is decided and almost none of it is visible. It owns the implementation plan: milestones with owners on both sides, dependencies named including the customer-side ones, and the sequence in which provisioning, integration, data migration, security review, and enablement have to land for the first outcome to be reachable.

It owns kickoff and go-live, and it keeps two different kinds of date apart. A contractual milestone is a commitment the order form or SOW made, and missing it is a contract event. A working target is a plan date the team set, and missing it is a schedule event. Presenting the second as the first inflates the alarm; presenting the first as the second is how a contractual commitment quietly lapses.

It owns the definition of first value, stated as a specific observable event that a system can confirm rather than as go-live, because go-live is the vendor's milestone and first value is the customer's. It owns time to first value measured from a named start event, blockers with the side they sit on and the escalation each needs, stall detection with the reason and the elapsed time, and the transition criteria that say onboarding is finished rather than merely elapsed.

## Use when

- A new customer, expansion module, or migrated tenant is being implemented and the plan has to exist before kickoff.
- An onboarding has gone quiet, a milestone has slipped twice, or the customer-side owner has stopped responding.
- Go-live readiness is being assessed, including provisioning, integration, migration, and security review state.
- A contractual onboarding milestone is approaching and its state has to be established honestly.
- Time to first value is being measured across a cohort and the start event, the definition, and the population have to be pinned down.
- An account is being transitioned out of onboarding and the criteria for that transition are the question.

## Do not use when

- The outcomes, baselines, and mutual plan are the subject rather than the implementation. That is `success-planning-desk`, whose first outcome this desk delivers against.
- The entitlement and commitment intake has not happened. That is `post-sale-handoff-desk`.
- The product is live and the question is why a persona is not using a capability. That is `adoption-enablement-desk`.
- The telemetry read itself, with definitions and windows, is the subject. That is `usage-analysis-desk`.
- The customer has raised the delay as a formal escalation with a committed update cadence. That is `escalation-management-desk`.

## Required evidence

- The accepted handoff with entitlements, implementation assumptions, and any contractual onboarding or go-live commitment.
- The success plan with its first outcome and the baseline captured against it.
- Provisioning and entitlement state: what is configured against what was purchased, with the date each was set.
- Integration dependencies with the systems on both sides, the credentials and access required, and who owns each.
- Data migration requirements: volumes, source systems, mapping decisions, cutover approach, and the rollback position.
- Security review, procurement, and legal requirements on the customer side, with their queue times where known.
- Customer-side resource availability with named owners, and their competing internal commitments.
- The standard onboarding path for this product and segment, and prior onboarding cycle times for genuinely comparable accounts.

## Workflow

**Outcome.** An implementation plan with milestones, owners on both sides, and named dependencies; kickoff and go-live dates with contractual commitments separated from working targets; the definition of first value as an observable event; time to first value measured from a named start event; blockers with the side they sit on and the escalation each needs; stall detection with reason and elapsed time; and the transition criteria that end onboarding.

**Grounding.** Milestone state comes from evidence that the work happened, not from the plan's own status field: a provisioning record, a completed integration handshake, an authentication event from the customer's environment, a signed-off migration, a delivered training with attendance. A customer-side milestone marked complete without evidence from the customer's side is recorded as unconfirmed. Time to first value is measured from a start event that is named and applied consistently across the cohort, because contract start, kickoff, and provisioning date produce three different numbers and a cycle-time improvement produced by changing the start event is not an improvement. Where the internal tracker and the customer's own view of progress disagree, both readings are preserved, since the customer's view is the one that determines whether the onboarding feels successful.

**Constraints.** Every dependency names the side it sits on, because the single most useful fact in a stalled onboarding is whether the blocker is ours, theirs, or a third party's, and plans routinely record only the ones the vendor controls. Customer-side owners are named people, not the customer's team name. First value is defined as an event a system can confirm, tied to the first outcome in the success plan; go-live, training completion, and account creation are milestones and are not first value. Contractual dates carry their document reference and are never restated as targets to make the plan look achievable. A stall is declared on elapsed time against a stated threshold rather than on sentiment, with the reason and the owning side. Transition out of onboarding requires the criteria to be met, not the calendar to have passed, and an account transitioned on elapsed time is recorded as such so the adoption stage inherits an honest starting position.

**Mandated order for the go-live cutover.** This order is mandated because a migration and a provisioning change land in the customer's production environment and are theirs to live with, and because the pre-change measurement disappears the moment the cutover completes:

1. Confirm the baseline for the first outcome is captured, since the pre-change state is unrecoverable after cutover.
2. Confirm provisioning, integration, and access state against what was purchased, with the evidence for each.
3. Obtain the customer's explicit go-live authorization from the named owner, including their acceptance of the cutover window and the rollback position.
4. Execute the cutover with the rollback path established and its trigger stated before the window opens.
5. Confirm post-cutover state with the customer, and only then record go-live actual.

This desk prepares the plan, the sequence, the dependencies, and the rollback position, then stops at the gate for anything that executes in the customer's environment.

**Parallel surface.** Independent items fan out safely: individual milestones being evidenced, independent dependency chains such as security review and data mapping that do not block each other, per-integration readiness checks, per-persona enablement preparation, and accounts in an onboarding cohort being assessed at once. The aggregate runs once after the fan-out returns: the critical path, the go-live readiness judgment, the stall determination, and the cohort time-to-first-value figure are statements about the whole plan or the whole cohort. The cutover sequence above is sequential by mandate and is not part of the parallel surface.

**Acceptance bar.** Every milestone has an owner named as a person and a state established by evidence. Every dependency names the side it sits on. First value is a specific observable event tied to the first outcome. Time to first value names its start event. Contractual dates are separated from working targets with the document reference on each. Every blocker names the escalation it needs and who would receive it. Stall state carries elapsed time and reason.

## Outputs

A complete run delivers this set:

- `onboarding-plan.md`: milestones with owners on both sides, dependencies with the side each sits on, the critical path, and the sequence to the first outcome.
- `go-live-readiness.md`: provisioning against entitlement, integration state, migration readiness, security and procurement state, the rollback position, and the readiness judgment with what it rests on.
- `first-value-definition.md`: the observable event that counts as first value, the system that confirms it, the first outcome it serves, and the start event that time to first value is measured from.
- `time-to-value-measurement.md`: elapsed time against the named start event, the comparison cohort with what makes it comparable, and the point at which the current account diverged from it.
- `blocker-register.md`: each blocker with the side it sits on, its owner by name, its age, its effect on the critical path, and the escalation it needs with the recipient.
- `stall-assessment.md`: stalled or not against the stated threshold, since when, the reason, whose side it sits on, and what would restart it.
- `onboarding-transition-record.md`: the criteria for leaving onboarding, their state, and whether the transition is criteria-met or elapsed-time, with the position the adoption stage inherits.
- `onboarding-downstream-handoff.md`: what `usage-analysis-desk` and `adoption-enablement-desk` inherit, including which surfaces went live and when, since that sets the window every usage read is computed over.

Depth standard: an artifact is complete when the customer's project owner and the internal delivery owner could both run their next two weeks from it without a follow-up round trip. A milestone with a state and no evidence, or a blocker with no named owner and no escalation path, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when provisioning records, integration state, or the onboarding tracker cannot be reached, the run delivers `onboarding-connector-diagnostic.md` naming each unreachable source and stating which milestone states, readiness judgments, and time-to-value figures remain unestablished. Go-live readiness is not asserted from a plan document alone.

Anti-fabrication guard: onboarding artifacts fail by optimism, and the mechanism is the status field. A tracker row set to on-track by whoever updated it last, a customer-side task assumed complete because nobody said otherwise, an integration marked configured because the ticket closed, and a go-live date carried forward because moving it requires a conversation: each is a plausible entry that costs nothing to write and produces an account that transitions into adoption with a dependency still open. Milestone state in these artifacts is set from evidence that the work happened, and a milestone with no such evidence reads `unconfirmed` rather than `complete`, especially on the customer's side where the vendor has the least visibility and the most incentive to assume progress. First value is recorded as achieved only when the defined observable event is confirmed in a system; a go-live, a training session, and a positive call are none of them first value, and recording one as such makes the time-to-value metric a measure of vendor activity. Time to first value is computed from the start event already declared for the cohort, and a figure produced by choosing a later start event is reported with that change named, because a cycle time that improved when the definition moved did not improve. Contractual milestone dates are quoted from the document; a working target presented as a contractual date, or the reverse, misstates whether a missed date is a contract event, and both errors are discovered by the customer.

## success_packet fields to update

- `onboarding` in full: `plan_state`, `kickoff_on`, `go_live_target`, `go_live_actual`, `contractual_milestones[]` with their document reference, `milestones[]` with owner, due, state, and dependency, `first_value_definition`, `first_value_achieved_on`, `time_to_first_value_days` with the start event named, and `stall`
- `active_clocks[]` for every contractual onboarding milestone and any date committed to the customer, each with its start event and due date
- `risks[]` for a stalled onboarding, a customer-side dependency with no owner, a contractual milestone at risk, and a transition made on elapsed time rather than criteria
- `commitments[]` updated where an onboarding commitment from the sales cycle is now honored, outstanding, or disputed
- `stakeholders[]` where the implementation owner, administrator, or security reviewer was identified during onboarding
- `approvals[]` for go-live authorization and any change executed in the customer's environment
- `source_facts` with collection dates, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would provision, deprovision, migrate, cut over, or reconfigure in the customer's live environment. This desk prepares the plan, the sequence, the dependencies, and the rollback position, then stops at the gate, because a migration run against the wrong assumption lands in the customer's production system and is theirs to live with.
- **Missing approval**: go-live authorization, a change to a contractual milestone date, or an onboarding scope change beyond what was sold requires the named customer owner and the internal authority the change needs.
- **Security or privacy**: the next step would move customer production data into a test environment, share credentials or access tokens through an artifact, or proceed with a migration before the customer's security review has cleared it.
- **Source conflict**: the internal tracker, the customer's own project plan, and the provisioning record genuinely disagree on what is complete, and adopting the more advanced reading produces a go-live decision on work that has not happened.
- **Release integrity**: go-live readiness or first value would be recorded as achieved without the evidence that establishes it, which propagates into the usage window, the health score, and the renewal narrative unchallenged.
- **Connector unreachable**: the provisioning record, the integration state, or the onboarding tracker exists and cannot be read, so readiness would describe a configuration nobody inspected.

An unknown comparable cycle time, an undocumented customer holiday period, an unconfirmed training date, and a secondary milestone with no owner yet are soft gaps. Record the gap, label the assumption against the milestone it affects, and continue.

## Downstream handoffs

`usage-analysis-desk` is next and needs the go-live actual date and which surfaces went live when, because that sets the earliest window any usage read can legitimately cover and prevents an adoption figure computed across a period the product was not live in. `adoption-enablement-desk` needs the enablement delivered with attendance, the administrator configuration state, and the personas that were never trained. `success-planning-desk` receives the delivered state against the mutual action plan and any milestone that slipped. `health-scoring-desk` needs onboarding state and time to first value where the model uses them. `escalation-management-desk` inherits any blocker the customer has escalated, with its age and owning side. `renewal-preparation-desk` needs the onboarding history, since a first term that started with a three-month stall is a renewal conversation whether or not anyone raised it at the time.

## Quality bar

Good onboarding work is legible to the customer's project owner, because that is who actually runs half of it. Dependencies name whose side they sit on, and the customer-side ones are as specific as the internal ones, with named people rather than a team. First value is a sentence anybody could check: a specific event, in a specific system, tied to the outcome the customer said they bought the product for. The plan distinguishes the dates that are contractual from the dates that are hopeful, and it says which is which next to each one. Stall detection is mechanical rather than sentimental, so an onboarding that has not moved in three weeks is stalled even when the last call was friendly. And the transition record is honest about whether onboarding finished or merely ended, since the account that is handed to the adoption stage as complete, with an integration still unconfigured, spends the next two quarters looking like an adoption problem.
