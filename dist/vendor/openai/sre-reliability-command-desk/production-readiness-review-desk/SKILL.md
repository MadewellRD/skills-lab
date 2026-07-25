---
name: production-readiness-review-desk
description: run a production readiness review or support acceptance review with a gate set scored pass, waived, failed, or not assessed against named evidence, a launch or acceptance decision with conditions, waivers carrying a named owner and an expiry date, hand-back criteria, and the reliability debt the service enters production carrying.
---

# Production Readiness Review Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the readiness artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent gate evidence, waiver owners, approval decisions, launch dates, measured results, or the tier a service claims.

## Role

Own the moment where reliability work becomes a decision. This desk converts the accumulated packet state into gates with defensible states, then into a launch or support-acceptance verdict that a service owner and an accepting rotation can both live with.

The review has one specific enemy, and it is not an unready service. It is the checkbox. A readiness review that reads a document and marks a gate green produces a signed form and no information, and the organization discovers what was actually true during the first incident. So the unit of work here is not the gate; it is the evidence behind the gate. A recovery gate passes on a dated exercise with a measured time, not on a DR plan. An alerting gate passes on a rule that has fired or been driven by a test, not on a rule that exists. An SLI gate passes on a query that returns data, not on an objective in a slide.

The second thing this desk owns is honesty about what is being accepted anyway. Almost every real launch carries reliability debt, and the useful review does not pretend otherwise; it names the debt, attaches an owner and a date, and makes the exception visible instead of silent.

## Use when

- A service is approaching launch, general availability, or first exposure to real users, and someone must decide whether it goes.
- A rotation is being asked to accept support for a service it did not build.
- A service is changing tier, taking a critical journey it did not previously carry, or moving from a team-owned model to a shared on-call model.
- An existing production service needs a readiness assessment after an incident showed the original review missed something.
- Waivers granted at a previous review are approaching expiry and the exception needs re-adjudication.
- A launch decision needs conditions: what must be true before ramp proceeds past the first cohort.

## Do not use when

- The upstream evidence a gate needs does not exist yet. Route to the desk that produces it: `sli-specification-desk` for measurement, `capacity-planning-desk` for headroom, `disaster-recovery-desk` and `backup-restore-desk` for recovery proof, `alerting-quality-desk` and `runbook-engineering-desk` for detection and response, `oncall-escalation-desk` for staffing.
- The question is how the change reaches users rather than whether the service is ready: that is `change-safety-desk`, which owns rollout stages and rollback.
- The review is a periodic health check on a service already in production and accepted: that is `reliability-review-desk`.
- The service is degraded right now: that is `incident-command-desk`.
- The gate is a security control, privacy assessment, or regulatory approval: cross-suite handoff to the Security suite, the Privacy suite, or the GRC suite. Record the dependency and its state; do not adjudicate it here.

## Required evidence

- The packet state from every upstream stage that ran, with measurement state intact.
- The launch or support-acceptance request: what is going live, to whom, at what volume, and on what date.
- The tier the service claims and the critical user journeys it carries, with their owners and rotation.
- The standard the review is conducted against, whether an internal readiness checklist, a support acceptance policy, or the suite gate set.
- Prior review records for the same service, including waivers with their expiry and whether they were closed.
- Dated results rather than plans: exercise results, restore times, load test outcomes, chaos results, canary and rollback history.
- The named people with authority to accept a waiver, approve the launch, and accept support.

## Workflow

**Outcome.** A scored gate set with evidence per gate, a launch or acceptance decision with any conditions attached, waivers each carrying a named owner and an expiry date, a reliability debt register the service enters production with, and hand-back criteria if a rotation is accepting support.

**Grounding.** Gate states come from measured evidence and dated results. Documents establish intent and are recorded as intent. Where a plan and a measurement disagree, the measurement sets the gate state and both are recorded per `references/suite-workflow-contract.md`. `not_assessed` is a first-class state and is used whenever nothing was read; it is the honest alternative to a pass, and a review with no `not_assessed` rows in an organization that has never measured its recovery time is a review that guessed.

**Constraints.** Four states exist and each has a meaning that does not blur. `pass` requires named evidence. `failed` means evidence exists and does not meet the bar. `waived` means the gap is real, accepted deliberately, and carries an owner and an expiry date. `not_assessed` means it was not evaluated, and it is never rendered as a pass because the review ran out of time.

A waiver without a named owner and a dated expiry is not a waiver; it is an exception that becomes permanent by default, and this is the mechanism by which reliability debt becomes invisible. The same applies to conditions on a launch decision: a condition with no owner and no checkpoint is a wish.

The acceptance sequence is mandated because the alternative transfers responsibility to people who never agreed to it, and because a launch approved before the gates are scored cannot be un-launched:

1. Score every gate against evidence, marking `not_assessed` where nothing was read.
2. Adjudicate each failed gate as a blocker or as a waiver with a named owner and an expiry date.
3. Obtain the launch approval from the accountable owner, with the open waivers visible in the same decision.
4. Obtain support acceptance from the rotation that will carry the pager, with the page load impact and hand-back criteria stated.
5. Record the decision, the debt, and the waiver expiries where the next review will find them.

**Parallel surface.** Gates, services, and critical journeys are independent units and are parallel-safe: per-gate evidence gathering, per-journey coverage checks, prior-waiver status lookups, and connector preflight across metrics, paging, incident tracker, catalog, and backup system all fan out.

The aggregate work is not parallel and runs once after the fan-out returns: the overall readiness verdict, ranking the debt by journey impact, judging whether accumulated waivers cross a threshold that individually none of them reach, and the approval steps above. A service can pass every gate individually and still be unready when three waived gates compound, and only the aggregate view sees it.

**Acceptance bar.** Every gate carries a state and the evidence that produced it, with the source named. Every waiver names an owner and an expiry date. The decision states go, go with conditions, or no go, with each condition owned and dated. The debt register is what the service actually carries, not the residue that was easy to write down. If a rotation is accepting support, the hand-back criteria are explicit.

## Outputs

A complete run delivers this artifact set:

- `production-readiness-gate-scorecard.md`: every gate with its state, the evidence and its source, the measurement date where one exists, and the assessor's reasoning where a state is contested.
- `production-readiness-decision.md`: the verdict, its scope and effective date, the conditions attached with owners and checkpoints, the approvers, and what changes if a condition is not met.
- `production-readiness-waivers.md`: each waiver with the gap, the risk accepted, the journeys exposed, the named owner, the expiry date, and the review that will re-adjudicate it.
- `production-readiness-debt-register.md`: the reliability debt entering production, ranked by journey impact, each entry naming the stage that would close it.
- `production-readiness-support-agreement.md`: for support acceptance, the services and journeys accepted, the expected page load, the response expectations, the access the rotation needs, and the hand-back criteria that return the service to its owning team.
- `production-readiness-downstream-handoff.md`: what `change-safety-desk` and `reliability-review-desk` inherit, including the waivers whose expiry falls inside the next review period.

Depth standard per artifact: a gate row is complete when a reader can tell what was read to produce the state. "Monitoring: pass" is a checkbox. "Monitoring: pass, four burn-rate rules on the checkout availability SLI, each with a runbook, two observed firing in the last quarter, two unproven" is a gate score. A waiver is complete when someone who was not in the review can tell what risk was accepted and who owns it.

In `diagnostic` mode, when the evidence systems exist and cannot be read, the run delivers `production-readiness-connector-diagnostic.md` naming what was reachable, what was attempted, and the exact access required. Gates are scored `not_assessed` in that mode, and no readiness decision is issued, because a readiness verdict is precisely the claim that evidence was seen.

This desk fails by scoring green. A readiness scorecard is the most quotable artifact in the suite: it gets pasted into launch mail, attached to approvals, and cited a year later as proof the service was ready, long after everyone has forgotten which rows were read and which were assumed. So no gate here moves to `pass` without a named source, a date where the evidence is a result, and the query, report, or record it came from. `not_assessed` is used freely and without embarrassment; it is a true statement about the review and it tells the next reader exactly what to go and check. A scorecard of honest unknowns is a working document; a scorecard of confident passes that nobody can trace is how a service arrives in production carrying risk that was recorded as absent.

## reliability_packet fields to update

- `readiness_gates[]` in full: `gate`, `state`, `evidence`, `owner`, and `expiry` for waived gates.
- `services[].lifecycle` and `services[].support_model` as the decision changes them.
- `services[].tier` where the review confirms or corrects the claimed tier.
- `reliability_risks[]` with each accepted risk, the journeys affected, its current control, and its owner.
- `oncall.rotations` and `oncall.page_load` where support acceptance changes what a rotation carries.
- `decisions` with the verdict and its conditions, and `assumptions` where a gate state rests on one.
- `source_facts` with attribution, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: the launch approver, the waiver owner, or the accepting rotation has not agreed, and continuing would record a decision on their behalf.
- Production or destructive: the next action would enable the launch, ramp traffic, route production load to the service, or change its support routing rather than assess readiness.
- Security or privacy: a gate depends on a security, privacy, or residency control whose state cannot be established from evidence, or the review would restate personal or sensitive data from an incident record as gate evidence.
- Source conflict: the DR plan and the last exercise disagree on recovery time, the catalog and the rotation disagree on ownership, or the capacity model and the load test disagree on headroom. Scoring one silently converts a contradiction into an approval.
- Release integrity: a gate would be recorded as passed without evidence, a waiver recorded without an owner or an expiry, or a service declared production-ready while its critical journey has no measured SLI.
- Connector unreachable: a system holding the evidence for a gate the decision depends on exists and cannot be read.

An unmeasured demand forecast, an absent prior review, and an untested secondary degradation path are soft gaps. Proceed with each recorded as `not_assessed` or as a labeled assumption. A gate is never upgraded to keep a launch date, a waiver never issued without an owner to answer for it, and the review is never narrowed to the gates that happen to have evidence.

## Downstream handoffs

`change-safety-desk` needs the decision, its conditions, and the open waivers, since a conditional launch usually converts directly into rollout stages and promotion criteria. `oncall-escalation-desk` needs the accepted support scope and expected load. `reliability-review-desk` needs the debt register and the waiver expiry dates for the next period's adjudication. `incident-command-desk` inherits the known accepted risks, which shorten diagnosis when one of them lands. Any gate resolving into engineering work hands to the SDLC suite as a labeled cross-suite handoff rather than being tracked as a reliability artifact.

## Quality bar

A scorecard where a reader can trace every state to something someone actually read, a decision that says go or no go rather than describing the situation, waivers that expire on a date with a person attached, and a debt register the service owner recognizes as an accurate account of what they are shipping with.
