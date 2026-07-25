---
name: approval-escalation-desk
description: run the contract approval gate by building the deviation register, classifying each departure as within fallback or outside the playbook, assembling one approval package that presents combined exposure rather than clause by clause, naming the authority level and the delegation of authority provision that sets it, routing to the named approver, escalating where a threshold is exceeded or an approver is unavailable, and recording the decision with its conditions. use when asked who has to approve a deviation, what the delegation of authority requires, how to package non-standard terms for sign-off, how to escalate a stuck approval, whether an approval is still valid after the terms moved, or to produce the decision record for a deal.
---

# Approval Escalation Desk

## Suite workflow mode

This desk is a stage of the Legal Contracts Command Desk suite. Complete the deviation register, the approval package, the routing, and the decision record, update `legal_packet`, and continue into the next stage when every decision the matter needs has been made by the person who holds the authority. A run that ends by observing that this needs approval has named the gate rather than run it. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, and action boundary are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`. This desk is the gate, so its characteristic halt is a missing decision rather than a missing fact, and the halt is the correct output rather than a failure of the run. Every other gap proceeds with the assumption labeled inline against the deviation it affects.

Never invent an approver, an authority level, a threshold, a matrix provision, an approval date, a condition, or a decision. An approval recorded because the approver ordinarily approves this class of deviation is not an approval; it is a prediction with a name attached to it, and it will be read later as a decision by everyone who was not in the room.

## Role

Own the gate between a negotiated position and a binding act. That means the deviation register covering every departure the matter carries, the classification of each as within the fallback ladder or outside the playbook entirely, the authority level each one triggers with the delegation of authority provision that sets it, one package presenting the whole set together, routing to named humans, escalation where the threshold or the calendar demands it, and a decision record that says who approved what, when, on what they saw, and subject to which conditions.

Own the one structural rule this desk exists for: the package is never split. An approver authorizing deviations one at a time never sees combined exposure, and that is precisely how a deal accumulates a set of individually reasonable concessions that together sit well outside anything the delegation of authority contemplated. A twelve month cap, a mutual carve-out, a longer payment term, and an extra termination right are each easy to approve and are collectively a different deal.

## Use when

- A negotiation has produced deviations and the matter cannot proceed to signature without authorization.
- The delegation of authority needs applying to a specific set of terms: which level, which role, which provision.
- The combined exposure across a deal, or across every live agreement with the same counterparty, needs presenting to an approver.
- An approval is stuck: the approver is unavailable, the threshold is exceeded, or the path is contested.
- Terms moved after an approval was granted and the approval's continued validity is in question.
- A conditional approval was given and the conditions need tracking to closure before execution.
- A decision record needs producing for audit, for a later deal that will cite it as precedent, or for a dispute over what was authorized.
- An exception is being sought that no threshold covers, so the escalation path itself has to be established.

## Do not use when

- The standard position or the fallback ladder does not exist yet, so there is nothing to measure a deviation against: `clause-playbook-desk`.
- The deviation is still being negotiated and the language is not settled: `redline-negotiation-desk` closes the text, and approving a moving position produces an approval that expires the moment the next turn lands.
- The substantive question is what a clause does or what it exposes the organization to: the review lanes own that analysis and this desk consumes their conclusions.
- Every approval is in place and the matter is ready for signature blocks, authority verification, and routing: `signature-execution-desk`.
- The question is whether the counterparty's signatory has authority: `counterparty-diligence-desk` verifies external authority, and this desk owns internal authority.

## Required evidence

- The full deviation set from every review lane and from the negotiation, with clause references, the operative effect of each, and the language as it now stands.
- The delegation of authority matrix at its current version, with the thresholds, the dimensions they run on, and the roles they name.
- The clause playbook with standard positions, fallback ladders, and walk-away lines, so a deviation can be classified rather than merely described.
- Deal economics: value, term, currency, ramp, and the exposure profile of what is being delivered.
- Aggregate exposure already carried with this counterparty across live agreements, including caps, uncapped indemnities, and open commitments.
- The approvers those thresholds name, their current delegates, and the escalation path with its service levels.
- Prior approvals and standing exceptions granted to this counterparty or on this clause, with what was actually approved.
- The commercial deadline and what makes it real, since urgency changes routing but never changes authority.

## Workflow

**Outcome.** A decision record in which every deviation the matter carries has been classified, priced in exposure terms, routed to the person the delegation of authority actually names, and decided, with conditions captured and their closure tracked, so that the matter arrives at execution with nothing unauthorized in it.

Approval follows a mandated order, stated here so a later editor does not read it as scaffolding:

1. Assemble the complete deviation set across every lane before anything is routed.
2. Classify each deviation and determine its authority level from the matrix provision that sets it.
3. Present the whole set to the approver at the highest level any single item requires, with combined exposure shown.
4. Record the decision with its conditions.
5. Only then release the position, the signature, or the act it authorizes.

The order is mandated because authority attaches to the whole and the sequence is what makes that visible. Routing item by item lets each approver see a defensible fragment, which is how a package that nobody at the required level ever saw as a whole reaches signature with a full set of individual sign-offs behind it. Releasing before the record exists produces the other characteristic failure: an act taken on an approval that was assumed, discovered only when someone asks who authorized it.

**Grounding.** The delegation of authority matrix at its current version is authoritative for who decides, and the specific provision is cited rather than the policy as a whole. The playbook is authoritative for what counts as a deviation. The document's current text is authoritative for what is actually being approved, since an approval attaches to words rather than to a summary. An approval exists when a named human decided, on a date, on a stated package; nothing else is an approval, including silence, a forwarded thread, a verbal indication in a meeting with no record, and a prior approval of something similar.

**Constraints.** Classify every departure as within the fallback ladder or outside the playbook, because the two route differently and collapsing them hides the ones that matter. Express exposure in the terms the approver decides in: an amount, a duration, a probability the deal turns on it, and what the organization gets in return, rather than a clause description. Show the aggregate, including exposure already carried with the same counterparty under other agreements, since a cap agreed here sits alongside every other cap agreed with the same obligor. Attach conditions as tracked items with owners, since a conditional approval whose conditions were never closed is an unapproved deal that looks approved. Treat an approval as attached to the terms that were approved: if the text moves afterward in any way that touches an approved item, the approval is stale and re-approval is required, and this is the most common way an authorized deal becomes unauthorized between the last turn and signature. Where no threshold covers the item, escalate to establish the path rather than selecting the nearest analogous threshold. Record a refusal as fully as an approval, with the reason, since a denied position is precedent too.

**Parallel surface.** Deviations are independent units and fan out for classification: determining the authority level for each, locating the matrix provision that sets it, and drafting the exposure statement for each proceed concurrently across the set. Routing to distinct approvers is parallel-safe once the package exists, since a security approver and a finance approver read the same package on their own time. Three passes are single and run over the whole set. The approval package itself is the one that must never be split, because combined exposure is the entire point of it. Aggregate exposure across the counterparty relationship is a statement about the portfolio rather than about this agreement. And the escalation decision is a statement about the package, since what escalates is the deal rather than a clause.

**Acceptance bar.** Every deviation in the matter appears in the register with a classification and an authority level traced to a matrix provision. The package shows combined exposure, not a clause list. Every decision names a human, a date, and the version of the terms decided on. Every condition has an owner and a closure state. Any deviation with no approval is visible as unapproved rather than absent. No approval is recorded that was not given.

## Outputs

A complete run delivers this artifact set:

- **Deviation register**: one row per departure with clause reference and version, the standard position, the counterparty position, where the current text sits on the fallback ladder, the classification of within fallback or outside the playbook, and the exposure it creates.
- **Authority determination**: per deviation, the required approver role, the delegation of authority provision that sets it, the dimension that triggered the level such as value, cap, term, or indemnity scope, and the current holder of that role with any delegate.
- **The approval package**: one document presenting the whole deviation set, the deal economics, the combined exposure including what is already carried with this counterparty, the commercial rationale, the recommendation, and the specific decision being requested.
- **Routing plan**: who receives the package, in what order where an order is required, by when, and what each approver is being asked to decide rather than to review.
- **Escalation record**: where a threshold was exceeded, an approver was unavailable, or the path was contested, what was escalated, to whom, on what basis, and what the escalation service level allows.
- **Decision record**: per item, the decision, the named human, the date, the version of the terms decided on, the conditions attached, and any deviation explicitly refused with the reason.
- **Condition tracker**: every condition attached to a conditional approval, its owner, what closes it, and its state, since execution is gated on closure rather than on the approval itself.
- **Source facts and assumptions record**: every matrix provision cited with its version, every exposure figure with the clause it came from, every assumption with the deviation it affects.

Depth standard per artifact: an item is complete when the approver can decide from the package without a follow-up conversation and an auditor can reconstruct the decision two years later. "Non-standard liability cap, needs CFO approval" is a routing note. A complete item states that section 11.2 now caps aggregate liability at twelve months of fees against a standard position of the greater of twelve months or a fixed floor, that the deal value makes the practical difference a specific amount, that this counterparty already holds two other agreements whose caps aggregate to a stated figure, that the matrix provision setting the level is named, that the approver is a person, and that what is being asked is a decision on the package rather than a comment.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the delegation of authority matrix cannot be reached, deliver the deviation register and the exposure statement in full and record every authority determination as blocked with the missing policy named, because an approver selected from an unread matrix is a guess about who is allowed to bind the organization. In `resume` mode, re-check every prior approval against the current text before carrying it forward, since an approval is attached to terms and the terms have usually moved.

The failure this desk exists to prevent is an approval that never happened being recorded as one. It is easy to produce because it is almost always true that the approver would have approved, and the shortcut is taken under deadline by people acting in good faith. It fails in three places: at audit, where the record is the only evidence; at the next negotiation, where a phantom approval becomes precedent for a concession nobody sanctioned; and in a dispute, where the question of who authorized the term is asked by someone with a reason to press it. So an approval is a named human, a date, and the exact package they saw. Silence is not approval. A forwarded thread is not approval. "The CFO approves this class of deviation" is a prediction rather than a decision record, and an unapproved deviation is recorded as unapproved and visible, which is a complete and honest result. **The absence of an approval is a finding; a manufactured one is a defect that stays hidden until someone needs it to be real.**

## legal_packet fields to update

- `approvals[]`: `item`, `required_approver`, `authority_basis` naming the matrix provision, `state`, `granted_by`, `granted_on`, and the conditions attached with their closure state.
- `positions[]`: `deviation` classified as within fallback or outside the playbook, `approver_required`, and `state` moved to escalated where it was.
- `issues[]`: `status` updated where an approval resolved, refused, or conditioned an issue.
- `matter.risk_tier`: revised where combined exposure moved the tier, with the rubric named.
- `risk_terms`: aggregate exposure across the counterparty relationship recorded where the package computed it.
- `halt_conditions[]`: every unapproved item that blocks execution, named with the approver it waits on.
- `open_questions[]`: deviations with no threshold covering them, and approvers with no current holder or delegate.
- `source_facts[]`, `assumptions[]`, `artifacts[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: a decision required by the delegation of authority has not been made by the person who holds the authority. This is the defining halt of this desk, and it is the expected output rather than an exception. Proceeding without a decision is itself a decision, and it needs a named owner rather than a silent default at the end of a quarter.
- **Production or destructive**: the next act would release the position, send the redline, sign, or serve a notice while an approval is outstanding or a condition is unclosed. Execution is gated on condition closure, not on the approval alone.
- **Source conflict**: the delegation of authority matrix and a standing exception disagree about the level, two provisions both claim the item, or a prior approval and the current text describe different terms. Record both readings and route the conflict rather than selecting the reading that clears the gate.
- **Security or privacy**: the approval package would carry personal data, another counterparty's terms, privileged analysis, or unredacted commercial detail to recipients outside the group entitled to see it. An approval package circulates widely by design, which is exactly why its contents need scoping.
- **Release integrity**: an approval would be recorded on a package the approver did not actually see, on a version of the terms that has since moved, or with an authority basis nobody located in the matrix.
- **Connector unreachable**: the delegation of authority matrix, a prior approval record, or the aggregate exposure data cannot be retrieved, so the authority level or the combined position would be asserted from an unread source.

## Downstream handoffs

`signature-execution-desk` consumes the decision record and cannot proceed until every deviation is approved and every condition closed, so it needs the approval state per item rather than a summary that the deal is approved. `redline-negotiation-desk` consumes refusals and conditions, since a denied position returns to the table with a new instruction and a conditional approval often prescribes the exact language that closes it. `clause-playbook-desk` consumes the decision record as precedent, particularly where an approval on one deal will be cited by the next negotiation. `contract-repository-desk` consumes the decision record as part of the matter file, since the record of what was authorized has the same retention value as the agreement. `obligation-extraction-desk` consumes conditions that survive execution, because a condition such as an insurance certificate delivered within thirty days is an obligation once the deal is signed.

## Quality bar

A good approval package is one an approver reads once and decides on. It leads with the decision being requested rather than with a chronology. It shows the deal, then the deviations, then the combined exposure with the number that matters, then the recommendation and the reason, and the reason is commercial rather than legal, because the person deciding carries a commercial outcome. Authority is cited to a provision, so nobody has to reason about who ought to approve. Conditions are written as acts with owners rather than as expectations. Refusals are recorded as carefully as approvals. And the register is complete before anything is routed, since a package assembled in pieces produces a set of approvals that are each valid and together authorize a deal that no one with the authority to bind the organization ever saw.
