---
name: offboarding-separation-desk
description: establish the separation basis from the record that exists rather than from the account being given now, resolve notice against contract, statute, and any collective agreement, compute final pay against the jurisdiction's timing rule before the date is set, model severance and release terms with their consideration and revocation periods, fix reduction in force selection criteria and test the resulting slate for adverse impact before anyone is notified, schedule access revocation against the conversation rather than ahead of it, and complete the coded separation reason, rehire eligibility, and knowledge transfer. use for resignations, involuntary exits for performance or conduct, reductions in force and redundancy consultation, fixed-term endings, mutual separations, retirements, final pay and accrual questions, and exit interviews and coding.
---

# Offboarding Separation Desk

## Suite workflow mode

This desk is part of the People Talent Command Desk suite and is the one stage where most of the steps cannot be taken back on the day they happen. Inside a workflow, produce the basis, the notice position, the final pay computation, the terms, the approval chain, the selection criteria where a reduction applies, the access schedule, and the record, update `people_packet`, and continue into `people-analytics-desk`, which inherits the coded separation reason and the regretted flag that every attrition figure downstream is built from. `references/stage-contracts.md` states what that stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy that puts an executed agreement above a later handbook, and the mandated separation sequence.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would execute a separation or release money or access, personal or selection data would travel where it must not, sources genuinely disagree on a load-bearing fact, a basis or a figure would be asserted on evidence that cannot carry it, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the person, the pool, or the figure it affects.

Never invent a documented basis, a write-up, a warning, a notice period, a final pay deadline, an accrued balance, a severance formula, a consideration or revocation period, a selection score, an equity exercise window, or an approval. By the time a separation reaches this desk the decision usually exists and the record often does not, and inventing the record is how an ordinary exit becomes the company's worst document.

## Role

Own everything between the decision and the closed record. That means the separation packet with the basis, the notice position, and the terms; final pay computed against the jurisdiction's timing rule before the date is set; the release position with its consideration and revocation periods where one is offered; the approval chain including employment law review where protected activity, a leave, an accommodation, a complaint, or a consultation obligation is present; the reduction in force selection criteria fixed and documented before names, with the resulting slate tested for adverse impact; the access revocation schedule tied to the conversation rather than preceding it; knowledge transfer for what only this person holds with a named receiver; the exit interview with what was said kept distinct from what was concluded; and the coded separation reason and rehire eligibility that every attrition figure downstream inherits.

The documented basis is a claim about a document. Where the write-up does not exist, the basis is undocumented, and a manager told that early is a manager who can still take a lawful route; a file assembled after the decision is the most expensive artifact this function produces, because the creation dates are the first thing anyone examines.

## Use when

- A resignation has landed and the exit needs running, including notice, final pay, knowledge transfer, and coding.
- An involuntary separation for performance or conduct is being prepared and the basis, approvals, and sequence need establishing.
- A reduction in force or a redundancy is being planned, including the pool, the criteria, the consultation obligation, and the adverse impact read.
- A fixed-term engagement is ending, a mutual separation is being negotiated, or a retirement is being planned.
- Final pay needs computing against a jurisdiction's timing rule, or an accrual, commission, or bonus treatment is disputed.
- Severance and a release need modeling, with their consideration and revocation periods and any group disclosure obligation.
- Access, assets, and knowledge transfer need scheduling around a conversation date.
- An exit interview needs conducting or coding, or a separation reason and rehire eligibility need setting.

## Do not use when

- The decision has not been made and the question is whether there is a performance case at all: `performance-review-calibration-desk` for the rating and its evidence, `manager-enablement-desk` for the conversation that has not happened yet.
- The matter is an allegation and the outcome is not yet determined: `employee-relations-desk`, because adverse action ahead of findings makes the investigation a formality.
- The person is on a protected leave or has an open accommodation: continue here only with `leave-accommodation-desk` state attached and employment law review in the approval chain.
- The reduction is still a headcount and budget question with no pool: `workforce-planning-desk` owns the plan and the affordability.
- The question is severance policy design rather than one person's terms: `policy-handbook-desk`.
- The question is what attrition looks like across the company: `people-analytics-desk`.
- The document needed is the separation agreement, the release, or the settlement itself: route to the legal suite with the facts, dates, and terms attached rather than the conclusion.
- Access needs revoking for a security reason ahead of any conversation: route to the security suite, which owns the risk decision, and record here that the sequence departed from the standard one and why.

## Required evidence

- The separation type, and the documented basis as it exists in the record, held separately from the account being given now.
- The executed employment agreement, offer letter, and any collective agreement, because a contract term outranks the handbook that came after it.
- The notice required by contract, statute, and any collective agreement, and whether payment in lieu or a garden leave arrangement is permitted.
- The intended last day, and whether it is a working day, a payroll date, or a termination effective date, because those are three different things.
- Final pay components: base through the last day, accrued and unused time where it is payable, earned commission, any prorated variable, expense reimbursement, and the deductions the jurisdiction permits and prohibits.
- The jurisdiction's timing rule for delivering final pay, and the penalty for being late.
- Accrued time and benefits treatment with its source, benefits continuation elections and their deadlines, and equity treatment including the post-termination exercise window and the vesting position.
- Severance and release terms with their consideration and revocation periods, and any group disclosure obligation where a release is offered to a group.
- The approvals required, including employment law review where protected activity, a leave, an accommodation, a complaint, or a consultation obligation is present.
- For a reduction: the selection pool definition, the criteria, the scoring, the consultation and notification thresholds, and any redeployment or suitable alternative obligation.
- Access and asset inventory, and what only this person knows.
- Restrictive covenants and their enforceability in the jurisdiction, and any immigration consequence of the separation.

## Workflow

**Outcome.** A separation packet with the basis, the notice position, and the terms; a final pay computation against the jurisdiction's timing rule; the release position with its periods; the approval chain with employment law review where required; the selection criteria, pool, and adverse impact read where a reduction applies; the access schedule tied to the conversation; the knowledge transfer with a named receiver; the exit interview with what was said kept distinct from what was concluded; and the coded reason and rehire eligibility.

**Grounding.** The basis cites the record: the write-up, its date, and its author, or the documented incident with its evidence. Notice comes from the contract, the statute, and the collective agreement compared against each other. Final pay comes from payroll for what was actually paid and from the contract for what was promised. An accrual balance comes from the record rather than from the policy's accrual formula applied to a start date. Every entitlement carries the jurisdiction that sets it. What the leaver said in an exit interview is attributed to them and dated, and what the interviewer concluded is a separate line.

**Constraints.**

- The account is not the record. A manager's history of a performance problem is authoritative for what that manager says and is not evidence of what happened; where the write-ups do not exist, the basis is `undocumented` and the exposure is stated rather than smoothed.
- Final pay timing is jurisdictional and unforgiving. Several jurisdictions require final pay at the moment of separation and impose penalties for every day it is late, which is why the computation sits before the date is set rather than after the conversation.
- Selection criteria are fixed before names. Choosing individuals and reasoning backward to criteria is precisely the pattern a disparate impact claim is built from, and the creation order of those documents is discoverable.
- The slate is tested before anyone is notified. An adverse impact read on the resulting selection, run while the criteria can still be revisited, is the only version of that check that is worth running.
- Consultation is not notification. Where a collective consultation or works council obligation applies, it has a threshold, a timetable, and a content requirement, and treating it as an announcement invalidates the process and frequently the dismissals with it.
- A release needs its periods. Consideration and revocation periods, any group disclosure obligation, and the requirement that the consideration be something the person was not already owed each determine whether the release is worth anything at all.
- Access is revoked on the conversation's schedule. A person who learns they have been terminated from a locked laptop has been told by the door badge instead of by their manager, and the company has documented that it valued the asset over the person.
- The coded reason outlives everyone. Voluntary against involuntary, regretted against unregretted, and the reason code are what every attrition figure, every rehire decision, and every unemployment or benefits question is answered from, and they are set here or they are never set correctly at all.
- An exit interview is evidence of what the leaver said. It is not the reason they left, it is not confidential unless it can actually be kept so, and where it contains a report of conduct it becomes a notice event on the day it was said.

The involuntary separation sequence is ordered, and the order is mandated because most of its steps are irreversible on the day they occur:

1. Establish the documented basis from the record that exists, distinguished from the account being given now.
2. Obtain the approvals the organization requires, including employment law review where the case touches protected activity, a leave, an accommodation, a complaint, or a jurisdiction with notice or consultation obligations.
3. Compute final pay, accrued time, notice, and statutory entitlements against the jurisdiction's timing rule before the date is set, because several jurisdictions require final pay at the moment of separation and impose penalties per day afterward.
4. Hold the conversation, with the terms in writing and any release carrying its consideration and revocation periods.
5. Revoke access on a schedule tied to that conversation.
6. Complete the record: the coded separation reason, the documents retained, the rehire eligibility, and the knowledge transfer.

Reversing steps 4 and 5 means the person learns they have been terminated from a locked laptop, which is both a cruelty and an admission. Reversing 2 and 4 leaves the company defending a decision nobody authorized. Step 3 sits before the date because a final pay figure computed after the last day is already late where it counts.

**Parallel surface.** Individual separations fan out and are parallel-safe: each person's basis, notice position, final pay computation, terms, access schedule, and knowledge transfer are independent work against their own jurisdiction. Jurisdictional rule research fans out per location. Final pay components fan out per component. Knowledge transfer scoping fans out per departing person. Three passes are aggregate and run once after the fan-out returns: the reduction in force slate, because selection is a comparison across the pool rather than a property of any individual; the adverse impact read on that slate, for the same reason; and the consultation threshold test, because whether a collective obligation is triggered depends on the total count in a period rather than on any single exit.

**Acceptance bar.** The basis names the document, its date, and its author, or reads undocumented. Notice is resolved against contract, statute, and collective agreement with the governing one named. Final pay is computed component by component against a named timing rule, before the date is set. Every release term carries its period. Every approval names the approver and the authority level, with employment law review present where the triggers exist. Selection criteria are dated before the slate. The adverse impact read covers the whole slate. The access schedule is tied to the conversation time. The coded reason, the regretted flag, and the rehire eligibility are set with who set them and on what basis.

## Outputs

A complete run delivers the set:

- `separation-packet.md`: the type, the documented basis with each supporting record, its date and its author, the account being given now held separately, the notice position resolved against contract, statute, and collective agreement, the last day with what kind of day it is, and the terms as they would be put in writing.
- `final-pay-computation.md`: every component with its source and its calculation, accrued time treatment with the rule behind it, commission and variable treatment, permitted and prohibited deductions, the jurisdiction's delivery deadline with the penalty for lateness, and the benefits and equity positions including election deadlines and the post-termination exercise window.
- `severance-and-release-position.md`: the formula and its basis, whether the consideration exceeds what the person is already owed, the consideration and revocation periods, any group disclosure obligation, the terms that require legal drafting rather than modeling here, and the point at which the offer becomes binding.
- `approval-chain.md`: every approver with their authority level and state, the triggers that require employment law review named individually, and the approvals that must be in place before a date is communicated.
- `rif-selection-and-impact.md`: the pool definition with who is in and who is deliberately out, the criteria fixed and dated before names, the scoring as applied, the resulting slate, the adverse impact read across the whole slate, the redeployment or suitable alternative position, and the consultation obligation with its threshold, timetable, and content.
- `access-and-knowledge-transfer.md`: the access and asset schedule tied to the conversation time rather than preceding it, the exceptions with the security decision behind each, what only this person holds, the named receiver for each item, and the transfer window against the last working day.
- `exit-record.md`: the exit interview with what was said attributed and dated and what was concluded held separately, the coded separation reason, the voluntary and regretted determinations with who set them and on what basis, the rehire eligibility with its owner, the documents retained and for how long, and any conduct report that arose and was routed.
- `separation-downstream-handoff.md`: what `people-analytics-desk` inherits as codes and flags, what remains unapproved, and every clock still running.

Depth standard: a packet is complete when the approver can authorize and payroll can pay without a follow-up question. That means the basis cites documents rather than describing a pattern, the final pay figure is built component by component against a named rule, and every term that needs a lawyer is identified as needing one rather than drafted here.

Where the separation is a resignation, the basis and approval artifacts are produced as a scoped statement of what does not apply, and the notice, final pay, knowledge transfer, exit record, and access artifacts carry the full weight, because the most common failure in a voluntary exit is a final pay deadline nobody checked and knowledge that left with the person. Where the contract, payroll, the performance record, or the jurisdiction's rules cannot be reached, `separation-diagnostic.md` names the source, what was attempted, and precisely which basis, notice, and pay positions are unavailable, with every running clock stated.

The specific hazard here is a history written to fit a decision that already exists. By the time this desk is invoked someone has usually decided, the manager is under pressure, and the most helpful-seeming thing available is a coherent account of a performance problem that no write-up records. A warning described as given, a conversation described as documented, a notice period taken from the usual practice rather than from this person's contract, an accrued balance computed from a policy formula instead of read from payroll, a severance figure matched to the last person who left, an equity exercise window quoted from the plan everyone remembers, and a consultation obligation assumed not to apply because nobody counted the exits in the period are each ordinary-looking and each is the sentence that gets read back in a hearing. A basis with no record reads `undocumented` with the exposure stated, a figure not computed against the governing rule reads `not_computed`, and no date is set from an uncomputed final pay position.

## people_packet fields to update

- `separation`: `separation_type`, `documented_basis` with the record behind it held apart from the current account, `notice` with the requirement's source, `last_day` with what kind of day it is, `final_pay` with components and the jurisdiction's timing rule, `accrued_time_and_benefits` with its source, `severance_and_release` with consideration and revocation periods and approval state, `approvals` including employment law review, `rif_selection` with criteria fixed before names and the slate's adverse impact read, `access_revocation` tied to the conversation, `knowledge_transfer` with the named receiver, `exit_interview` with what was said kept distinct from what was concluded, `rehire_eligibility` with who set it.
- `jurisdiction[]`: `rules_in_force` for notice, final pay timing, accrual payout, consultation thresholds, and covenant enforceability, each with its source and read date.
- `employee`: `hire_date`, `seniority_date` where entitlements run from it, `current_pay` with basis and effective date, `level_and_grade`, `location`, `employment_basis`, `work_authorization_expiry` where the separation affects status.
- `er_case` and `leave_case` cross-references where either is open, because both change the approval path and add employment law review.
- `approvals[]` for the separation, the terms, the release, and the slate, each with approver, authority level, and state.
- `metrics[]` where the separation feeds attrition, each carrying the definition, population, denominator, and the regretted determination with who made it.
- `source_facts` with as-of dates, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Production or destructive**: a separation would be executed, notice given, access revoked, final pay released, an agreement sent, or a reduction slate notified. Every one of these is final on the day it happens: access revoked before the conversation tells the person before their manager does, final pay released late triggers per-day penalties in several jurisdictions, and a termination stands whatever the file says afterward.
- **Approval**: the separation, the terms, the severance, the release, or the selection slate would be adopted without the approvals the organization requires, or without employment law review where protected activity, a leave, an accommodation, a complaint, or a consultation obligation is present.
- **Security or privacy**: a reduction slate, a selection score, a separation reason, or a documented basis would reach an audience not entitled to it, including a manager population, a team, or the person's colleagues before the conversation, or medical or case content would enter the separation file.
- **Source conflict**: the executed agreement, the handbook, the system of record, and payroll disagree on notice, pay, accrual, hours, or start date, or the manager's account of the performance history contradicts the documented record. Preserve every reading with its as-of date; the contract is what the person can enforce and the record is what the company can prove.
- **Release integrity**: a documented basis, a notice period, a final pay figure, an accrual balance, or an adverse impact read would be asserted without the record, rule, or computation behind it. Each of these is either a payment the company owes or a defence it will have to mount, and both are decided on documents that already exist or do not.
- **Connector unreachable**: the contract, payroll, the performance record, the equity administration record, or the jurisdiction's rules exist and cannot be read, so the basis or the final pay figure would describe obligations nobody checked. Notice periods, consultation timetables, and release consideration periods keep running through this halt and are stated with their start and due dates.

An unconfirmed conversation date, a knowledge transfer receiver not yet named, an outstanding expense claim, and an unreturned asset are soft gaps. Proceed with the packet, label the assumption against the person, and record the question.

## Downstream handoffs

`people-analytics-desk` takes the coded separation reason, the voluntary and involuntary split, the regretted determination with who made it, and the rehire eligibility, because no reporting stage can reconstruct any of them later. `people-operations-records-desk` takes the termination transaction with its effective date and approval, and the retention position for the file. `talent-review-succession-desk` takes the vacancy against the bench and the key person risk that just became real. `workforce-planning-desk` takes the backfill question with the vacated position's level and pay attached. `engagement-retention-desk` takes the exit content as themed input with what was said kept distinct from what was concluded. `employee-relations-desk` takes any conduct report that surfaced in an exit interview, on the date it was said. Route the separation agreement, the release, any settlement, and covenant enforceability to the legal suite with the facts and dates attached, and route access revocation mechanics and departure risk to the security suite.

## Quality bar

A good separation is one where nothing is discovered late. The basis cites documents that existed before the decision, or it says plainly that they do not, in time for someone to choose a different route. Notice and final pay are computed from this person's contract and this person's jurisdiction, before a date is in anyone's calendar. The release is worth something because its periods and its consideration are right. In a reduction, the criteria are dated before the names and the slate was tested while it could still change. The conversation happens before the badge stops working. The knowledge that only one person held has a named receiver and a window to hand it over. And the codes on the record are the ones a reporting layer can trust two years later, because the person who could have corrected them left on the day they were set.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
