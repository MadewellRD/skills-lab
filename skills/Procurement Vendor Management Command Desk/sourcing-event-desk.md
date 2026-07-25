---
name: sourcing-event-desk
description: construct and run a competitive sourcing event covering the rfp rfq or reverse auction document, the pricing template that forces bids into a comparable structure, a single communication channel with questions answered to all bidders together, addenda and deadline extensions where a clarification changes the requirement, late and non-conforming submission handling stated in advance, terms exceptions declared during the bid, and confidentiality controls that keep bid contents from other bidders and from the incumbent. use for rfp and rfq construction, sourcing document assembly, pricing templates, bidder q and a, addenda, auction design, bid confidentiality, and sourcing process integrity questions.
---

# Sourcing Event Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, assemble the sourcing package, run the event, produce the artifact set, update `procurement_packet`, and continue into `bid-evaluation-desk` with submissions closed and the process record intact. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet, the action boundary, and the halt format.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the document section or bidder it affects.

Never invent a bidder's question, an answer that was distributed, an addendum, a submission time, a declared exception, a decline reason, or a communication that took place.

## Role

Own the event: the document that goes to the market, the pricing template that makes what comes back comparable, the single channel every communication runs through, the addenda that keep every bidder working from the same requirement, the rules for late and non-conforming submissions written before anyone is late, and the confidentiality controls that keep one bidder's content away from the others and away from the incumbent.

The pricing template is the piece practitioners underrate and evaluators live with. Bids that arrive in each supplier's preferred shape have to be normalized afterward, and normalization performed after the prices are visible is analysis nobody can distinguish from advocacy. A template that forces unit, volume, term, ramp, implementation, and exclusions into fixed cells converts that whole argument into arithmetic. The other thing this desk protects is equality of information. Every answer, every clarification, and every extension reaches all bidders together, because an answer given to one bidder is an advantage the record shows, and in a regulated procurement it is a ground for challenge that survives the award.

## Use when

- A sourcing document has to be assembled from an approved requirement set, statement of work, criteria, and timeline.
- A pricing template has to be designed so bids arrive comparable rather than being reconciled afterward.
- A question and answer window has to be run, with answers distributed to every bidder together.
- A clarification changes the requirement and an addendum with a deadline extension has to be issued.
- A submission arrives late, incomplete, or in the wrong format and the rule has to be applied as it was published.
- A reverse auction needs its lot structure, bid decrements, visibility rules, and reserve handling designed.
- Confidentiality controls are needed for bid contents, particularly where the incumbent is bidding.
- A process deviation has occurred and has to be recorded with what it affects.

## Do not use when

- The requirement set, statement of work, or evaluation criteria are not yet fixed and dated: `requirements-specification-desk`.
- The invited list and the contracting entities are not settled: `supplier-discovery-desk`.
- Submissions have closed and scoring, normalization, and the award recommendation are the work: `bid-evaluation-desk`.
- The exercise is a direct award or a renewal negotiation with a single supplier: `pricing-negotiation-desk`, with the sole source basis recorded by `procurement-policy-desk`.
- The question is which sourcing method the policy requires at this value and tier: `procurement-policy-desk`.
- The supplier's security evidence has to be requested and assessed: `security-privacy-review-desk`, which runs against the shortlist rather than through the bid channel.

## Required evidence

- The requirement set and statement of work as approved, with mandatory and desirable marked.
- The evaluation criteria, weights, and scoring scale as fixed, with the date they were fixed.
- The invited bidder list with contracting entities and named contacts.
- The timeline: issue date, question deadline, addendum cut-off, submission deadline, evaluation window, and target award date.
- The fairness regime and any mandated process, including publication obligations where public procurement rules apply.
- The contract template and the terms bidders are being asked to accept, plus the mandatory positions the policy requires.
- The response format and the pricing structure that makes bids comparable.
- The confidentiality regime, including any non-disclosure agreement that has to be in place before the document is issued.
- The named single point of contact through whom all communication runs.

## Workflow

**Outcome.** A coherent sourcing package issued as one document set, a pricing template that produces comparable bids, a running communication record with every question and its distributed answer, addenda where a clarification changed the requirement, submissions received and closed under published rules, exceptions to terms declared during the bid, and a process record complete enough to answer a challenge.

**Grounding.** The approved requirement set, the fixed criteria, and the policy's mandatory terms are what goes to market. Nothing is added to the document that a stakeholder has not owned, and nothing already communicated to any bidder is left out of the record.

**Mandated ordering.** For any competitive exercise, fix and date the criteria and weights, communicate them in the sourcing document, close the submission window, and open submissions only after it closes. The order is mandated because a criterion or a weight adjusted once bids are visible is indistinguishable from choosing the winner and back-solving the arithmetic, and no explanation offered later removes that ambiguity; in a regulated or public procurement it is a ground for challenge that can void the award and restart the exercise. This ordering is recorded so a future editor reads it as a fairness constraint rather than as procedure.

**Constraints.**

- Issue the requirements, statement of work, response format, criteria and weights, timeline, and terms as one package. A requirements list bidders answer in their own shape produces responses that cannot be compared and an evaluation that becomes a reading exercise.
- Force pricing into fixed cells: unit, volume assumption, term, ramp, implementation, support, and what is excluded. Free-form pricing shifts the normalization from before the bids to after them.
- Run every communication through the single named channel and distribute every answer to every bidder together, attributed to the question rather than to the asker. A supplier's question frequently reveals their approach, and the asker is not named.
- Where a clarification changes the requirement rather than explaining it, issue an addendum and extend the submission deadline where the change is material. A material change absorbed without an extension advantages whoever already knew.
- Publish the late and non-conforming rules before submissions open, and apply them as published. A rule relaxed for one bidder is a rule that no longer exists.
- Require bidders to declare exceptions to the terms and the service levels during the bid. Exceptions discovered during the negotiation are leverage transferred to the supplier at exactly the moment the company has committed.
- Record who declined and why. A market that declines is telling the company something about its requirements, its terms, or its timeline, and that signal is lost if only submissions are recorded.
- Record process deviations as deviations, with what each one affects, rather than smoothing them out of the file.

**Parallel surface.** Document construction fans out: the requirement sections, the statement of work, the response format, the pricing template, the terms package, and the timeline are drafted against their own sources at the same time, and invitations and confidentiality agreements are prepared per bidder in parallel. Two things are explicitly not parallel per bidder. The question and answer cycle is a single distribution to the whole invited list, because answering bidders individually is unequal treatment however even-handed the content is. Addenda are the same: one issue, to everyone, with one deadline. The package review before issue is also a single pass, since the criteria, the pricing template, and the requirement set have to be consistent with each other and each is only checkable against the rest.

**Acceptance bar.** The package is internally consistent: every criterion maps to something the response format asks for, and every pricing cell has a stated volume and term assumption. The communication record shows every question, its answer, the distribution date, and the recipients. Every addendum states what changed, why, and what happened to the deadline. Submissions are recorded with their arrival time against the published deadline. Every declared exception and every decline reason is captured verbatim.

## Outputs

A complete run delivers the set:

- `sourcing-document.md`: requirements, statement of work, response format, criteria and weights with the date fixed, timeline, terms, and instructions to bidders, assembled as one package.
- `pricing-template.md`: the fixed cell structure with unit, volume, term, ramp, implementation, support, and exclusions, plus the assumptions every bidder prices against and the currency and rounding rules.
- `bidder-communication-log.md`: every contact, its date, its channel, the question as asked, the answer as distributed, and the recipients.
- `addenda-record.md`: each addendum with what changed, whether it was a clarification or a requirement change, the deadline consequence, and the date issued.
- `submission-receipt-record.md`: what arrived from whom, when against the deadline, in what form, what was missing, and how the published rule was applied.
- `terms-exception-register.md`: every exception each bidder declared, to which clause, and the position they proposed.
- `confidentiality-controls-record.md`: who has access to bid contents, how the incumbent's access is separated, the agreements in place, and the handling rules for the evaluation period.
- `participation-and-decline-record.md`: who was invited, who declined, and the reason each gave, recorded as given.
- `process-deviation-record.md`: every departure from the published process, what it affects, and who was informed.
- `sourcing-event-downstream-handoff.md`: the closed bid set, the criteria as issued, the assumption set, and the open exceptions the evaluation stage inherits.

Depth standard: an artifact is complete when a bidder could respond without a clarification and a reviewer could reconstruct the whole exercise from the file. A pricing template is complete when two bidders filling it honestly produce numbers that can be added to each other. A communication log is complete when the question, the answer, and the distribution date are all present for every entry.

Where the event is a reverse auction, `pricing-template.md` carries the lot structure, decrement rules, visibility rules, and reserve handling in place of a static price schedule, and the same document states what happens if the auction closes below a threshold nobody can honor. Where the bidder list, the criteria, or the approved requirement set cannot be reached, `sourcing-event-diagnostic.md` names the gap; the document is not assembled from a draft specification, because what is issued is what the contract will inherit.

The record is the artifact here, and a process record is the one thing in this suite that cannot be reconstructed after the fact without becoming fiction. Filling in a communication log from memory, dating an addendum to the day it should have gone out, recording an answer as distributed to all bidders when it was given on a call to one, and writing a decline reason a supplier never stated are each a repair to a process rather than a record of it, and they are indistinguishable from the real thing until somebody asks for the sent items. A communication with no evidence behind it is logged as unverified with what is known, a deviation is written as a deviation, and a gap in the record is left visible, because an incomplete record is defensible and a tidy invented one is not.

## procurement_packet fields to update

- `sourcing_event.event_type`, `competitive_basis`, `fairness_regime`, `bidders`, `evaluation_criteria` with the date fixed, `timeline`, `questions_and_addenda`, `communication_log`, `confidentiality_controls`.
- `sourcing_event.sole_source_justification` where the event is a direct award and the condition and approver are recorded.
- `bids[].supplier` and `bids[].submitted` with what arrived, plus `bids[].exceptions_taken` from the declarations.
- `requirements.assumptions_given_to_bidders` as actually issued, including anything an addendum changed.
- `commitment_class` moved to `supplier_communication` at issue, since the document is an act against the market.
- `approvals` for issue, for any addendum that changes the requirement, and for any deviation from the published process.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Production or destructive**: issuing the document, answering a bidder question, sending an addendum, extending a deadline, or opening an auction. Each is an act against the market that cannot be recalled. An answer given to one bidder and not the others taints the process, a requirement corrected after submissions arrive either restarts the exercise or advantages whoever already knew, and in a regulated procurement either is a ground for challenge that survives the award. Prepare the document, the answer, and the addendum; the authorized owner releases them.
- **Approval**: accepting a late or non-conforming submission, waiving a published rule, shortening the response window, cancelling the event, or issuing a change that alters the evaluation basis. Each of these changes the outcome for every bidder and belongs to whoever owns the process.
- **Security or privacy**: bid contents, another bidder's pricing, or the company's own architecture and data flows would be exposed, or the incumbent would receive access to material from the bidders competing against them. Where the incumbent is bidding, separation is designed before issue rather than managed afterward.
- **Source conflict**: the issued document, the addenda, and the criteria as fixed no longer agree, or two bidders received different answers to the same question. Record both readings, because the discrepancy decides whether the exercise can proceed at all.
- **Release integrity**: the exercise would proceed with the criteria unfixed or undated, with a weight changed after submissions were visible, or with the process record incomplete enough that the award could not be explained.
- **Connector unreachable**: the criteria record, the approved requirement set, the bidder list, or the submission system exists and cannot be read, so what was issued or what arrived would be asserted rather than established.

A bidder who has not confirmed receipt, an unanswered question inside the window, an unreturned confidentiality agreement, and a contact whose details are unconfirmed are soft gaps. Record them against the bidder, label the assumption, and continue preparing.

## Downstream handoffs

`bid-evaluation-desk` inherits the closed bid set, the criteria exactly as issued and dated, the assumption set every bid priced against, the pricing templates as returned, and the terms exception register, and it scores against the published criteria rather than a refined version of them. `security-privacy-review-desk` inherits the shortlisted suppliers and the security requirements as issued, so evidence is requested against what bidders were told. `pricing-negotiation-desk` inherits the exception register and the pricing structure, since a bidder's declared exception is a negotiation position they have already committed to in writing. `contract-execution-routing-desk` inherits the issued terms and the addenda, because the agreement carries them.

## Quality bar

A well-run event is boring in the right places. Every bidder had the same information at the same time, every question has an answer with a distribution date beside it, and the pricing came back in a shape that adds up without an analyst rebuilding it. The rules for lateness were published before anybody was late and applied when somebody was. The incumbent bid without seeing anything the others sent. The declines are on the record with what the suppliers said, because three declines citing the same term is the most useful market feedback the company will get for free. And the whole file reads as something a challenge could be answered from: what was issued, when, to whom, what changed, and why.
