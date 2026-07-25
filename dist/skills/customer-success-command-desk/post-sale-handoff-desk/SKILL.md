---
name: post-sale-handoff-desk
description: reconcile the executed order form against what the deal narrative promised at closed-won handoff, covering entitlement and term facts read from the contract, the commitment register of sales-cycle promises with who made them and to whom, the buying group as it stood at signature, implementation assumptions the deal was priced on, and the kickoff acceptance decision. use for handoff intake, sales to customer success transition, new logo readiness, co-term and amendment intake, and reconciling what was sold against what was signed.
---

# Post-Sale Handoff Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the handoff artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the entitlement, commitment, or contact it affects, and record it in `open_questions`. Never invent a term date, a notice period, an entitlement count, a promise, the person who made it, or a contact's role in the buying group.

## Role

This desk owns the moment the account stops being a deal and starts being a relationship, and it owns the gap that opens at that moment. What the customer signed and what the customer was told are two different records, both real, and the company can only deliver the first while the customer will hold it to the second. This desk reads the executed order form, master agreement, service schedules, and any amendment for the facts that bind: term start and end, auto-renewal behavior, the notice period and the deadline computed from it with both inputs shown, entitlements stated as units purchased with the unit named, overage terms, uplift or price protection, and termination rights.

Against that it reads the deal narrative: the business case the customer bought against, the success criteria stated in the evaluation, the demo and proposal content, and the promises made along the way about integrations, timelines, roadmap items, service levels, and what the product would do. Every difference between the two records is named rather than averaged.

It owns the commitment register, which is the artifact that survives longest. A commitment carries the promise in the customer's phrasing, who made it, which named stakeholder heard it, when, where it is recorded, and its state, and it stays outstanding until a source shows it honored. It owns the buying group as it stood at signature, the implementation assumptions the deal was priced on, and the acceptance decision: whether this handoff is complete enough for a kickoff to be scheduled, or what has to arrive first.

## Use when

- A deal has closed and the account is transitioning from the seller to a named customer success owner.
- The order form and the opportunity record disagree on entitlements, product mix, dates, or amount.
- The customer opens the first call by referring to something they were told during the evaluation that nobody on the delivery side has heard.
- An amendment, co-term, expansion order, or renewal-with-changes has been signed and the entitlement and term facts have moved.
- A kickoff is being scheduled and the readiness of the handoff is the question.
- An onboarding is stalling on something that turns out to have been assumed rather than sold.

## Do not use when

- The commercial relationship, tier, and coverage motion are the subject rather than the intake. That is `segmentation-coverage-desk`.
- The buying group has changed since signature and the current map is what is needed. That is `stakeholder-mapping-desk`, which inherits the signature-time group from here.
- The work is turning the customer's business case into measurable outcomes with baselines. That is `success-planning-desk`.
- The implementation plan, its dependencies, and its go-live are the subject. That is `onboarding-time-to-value-desk`.
- A renewal or expansion order form is being prepared commercially. That belongs to the sales suite; this desk consumes the executed result.

## Required evidence

- The executed order form and any master agreement, service schedule, SOW, or amendment, at the signed version rather than the last draft circulated.
- The opportunity record with amount, close date, product lines, and stage history.
- The deal narrative: the business case, the evaluation success criteria, the proposal and pricing rationale, and the competitive context the deal was won against.
- Sales-cycle communications and meeting records carrying promises, including anything committed in a security review, a procurement negotiation, or a late-stage concession.
- Named contacts with their role in the buying group, including the economic buyer, the champion, the technical evaluator, and procurement.
- The provisioning intent and entitlement setup request, plus the implementation assumptions the deal was priced on such as scope, environments, integrations, and customer-side resourcing.

## Workflow

**Outcome.** An intake record reconciling the executed contract against the deal narrative with every difference named; contract facts including the computed notice deadline; a populated commitment register; the customer's stated reason for buying in their own language; the buying group as it stood at signature; the implementation assumptions onboarding inherits; and an acceptance decision that either releases the account to kickoff or states exactly what is missing.

**Grounding.** Contract facts come from the executed document. A term end date taken from a CRM close date, an entitlement count taken from an opportunity line item, and a notice period assumed from the standard paper are three of the most expensive substitutions in this suite, because each is carried forward unchallenged until the renewal that depends on it. Promises come from where they were made, with the maker named; a promise the company has no record of but the customer describes consistently is recorded as `customer_recollection` and stays open rather than being dismissed for lack of a document. Where the contract and the narrative genuinely disagree on scope, entitlement, dates, or capability, both readings are preserved with attribution.

**Constraints.** The notice deadline is computed and shown with both inputs, because auto-renewal fires on it regardless of who read the paper. Units purchased and units provisioned are recorded as separate numbers from the start, since the distance between them is the adoption denominator every later stage divides by. A roadmap item promised during the sales cycle is a commitment, not a delivery date, and is recorded at the confidence the company can actually stand behind. Concessions granted to close the deal, including service commitments and non-standard terms, travel into the register whether or not they appear on the order form. The acceptance decision is a judgment with a stated basis, not a checkbox: an incomplete handoff accepted quietly becomes an onboarding that stalls on a dependency nobody owns.

**Parallel surface.** Independent items fan out safely: individual contract documents and amendments, individual entitlement lines, individual commitments being traced to their source, and individual buying-group contacts being confirmed. The reconciliation itself is a single pass after the fan-out returns, because a difference between contract and narrative is only visible when both records are held together, and so is the acceptance decision, which weighs the whole intake rather than any one line of it.

**Acceptance bar.** A customer success owner could run the kickoff from this record without reopening the deal. Every entitlement line carries its unit, its purchased count, and its provisioned count or an explicit unknown. The notice deadline is computed with both inputs shown. Every commitment has a maker, a recipient, a source, and an owner who carries it now. Every contract-to-narrative difference is stated as a difference rather than resolved. The acceptance decision names its basis.

## Outputs

A complete run delivers this set:

- `handoff-intake-record.md`: the reconciliation, with contract reading and narrative reading side by side per disputed item and the customer's stated reason for buying quoted rather than paraphrased into product language.
- `contract-facts.md`: term dates, auto-renewal behavior, notice period and the computed deadline with its arithmetic shown, entitlements with units purchased against units provisioned, overage terms, uplift, termination rights, and co-term relationships, each with the document and clause it came from.
- `commitment-register.md`: every promise with its wording, maker, recipient, forum, date, recorded source, current state, and the named owner who carries it into delivery.
- `signature-buying-group.md`: the buying group as it stood at signature with role type, what establishes each role, and the contacts the delivery side has never met.
- `implementation-assumptions.md`: what the deal was priced and scoped on, including environments, integrations, data volumes, customer-side resourcing, and any timeline the order form or SOW made contractual.
- `handoff-acceptance-decision.md`: accepted, accepted with conditions, or not accepted, with the basis, the named conditions, their owners, and the kickoff readiness position.
- `post-sale-handoff-downstream-handoff.md`: what `segmentation-coverage-desk` and `onboarding-time-to-value-desk` inherit, with unresolved differences and outstanding commitments carried rather than summarized away.

Depth standard: an artifact is complete when the receiving CSM could run the kickoff and the first business review from it without going back to the seller. An entitlement line with no unit, a commitment with no maker, or a notice period with no computed deadline is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the executed document, the opportunity record, or the sales-cycle communications cannot be reached, the run delivers `handoff-connector-diagnostic.md` naming each unreachable source and the specific contract facts, commitments, and entitlement counts that remain unavailable. Term dates and notice deadlines are not reconstructed from the shape of a standard agreement.

Anti-fabrication guard: the failure mode here is a tidy handoff. This record is written at the one moment when nobody is arguing, so a clean version of it feels like a good result and a version full of open differences feels like a failure of the seller. It is the opposite. A commitment register with no entries almost never means no promises were made; it means nobody read the late-stage email thread where the integration timeline was agreed. An entitlement count that matches the CRM exactly, on an account where the order form was amended twice, means the amendments were not opened. The customer's reason for buying, rewritten into the company's own value language, has lost the phrasing that the first business review has to answer against. Every number in the contract facts artifact is quoted from a document with the clause named, or it is written as unknown. Every commitment is attributed to a named maker or is carried as customer recollection with that label attached, never dropped for lack of a document and never upgraded to a company position because it sounds like something the company would say. Where the contract and the narrative differ, both readings stay on the page under the disputed item, because the difference is the deliverable, and the version of this record that reads smoothest is the one that will be contradicted first, in front of the customer, by the customer.

## success_packet fields to update

- `account` with `account_id`, `name`, `parent_account`, `csm_owner`, `account_team`, and `lifecycle_stage` set to `onboarding`
- `contract` in full: `term_start`, `term_end`, `auto_renewal`, `notice_period_days`, `notice_deadline` with both inputs shown, `renewal_uplift`, `termination_rights`, `co_termed_with`, `arr`, `entitlements[]` with `units_purchased` and `units_provisioned` separate, and `contract_source`
- `commitments[]` with `commitment`, `made_by`, `made_to`, `made_during`, `source`, `state`, and `owner`
- `stakeholders[]` seeded from the signature buying group with `role_type`, `influence`, `disposition`, `last_interaction`, and `coverage_state`
- `active_clocks[]` for the notice deadline and any contractual onboarding milestone, each with its start event and due date
- `source_facts` with collection dates, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Source conflict**: the executed contract and the deal narrative genuinely disagree on scope, entitlements, dates, service commitments, or what the product was said to do. Quietly adopting the contract reading pushes an unrecorded broken promise into the first business review, where the customer states it in front of the economic buyer and the company has no record of it.
- **Missing approval**: honoring, waiving, or renegotiating a sales-cycle commitment would commit the company to work, credit, or scope beyond the order form. That is a commercial decision with an owner and an authority level.
- **Security or privacy**: the handoff would carry personal data, security review findings, or customer confidential material from the deal record into an artifact whose audience is wider than the deal team had.
- **Production or destructive**: the next action would provision, deprovision, or configure entitlements in the customer's environment, or write the intake back into the CRM or success platform as the record.
- **Release integrity**: the handoff would be accepted, and a kickoff scheduled, on entitlement or term facts that no executed document establishes. Every date downstream is computed from these, and a wrong term end propagates into the renewal timeline unchallenged.
- **Connector unreachable**: the executed document, the opportunity record, or the sales-cycle communication history exists and cannot be read, so contract facts would describe a paper nobody opened.

An unnamed technical evaluator, an unrecorded competitive context, an unknown provisioning date, and an implementation assumption nobody wrote down are soft gaps. Record the gap, label the assumption against the item it affects, and continue.

## Downstream handoffs

`segmentation-coverage-desk` is next and needs ARR with its basis, product mix, lifecycle stage, and the account team as assigned at handoff. `stakeholder-mapping-desk` needs the signature buying group as its starting map, with the contacts the delivery side has never met flagged as unverified coverage. `success-planning-desk` needs the customer's stated reason for buying in their own words and the business case they bought against, because those become the desired outcomes. `onboarding-time-to-value-desk` needs the implementation assumptions, the contractual milestones separated from working targets, and the entitlements to be provisioned against. `renewal-preparation-desk` inherits the notice deadline and its arithmetic. `escalation-management-desk` and `qbr-ebr-desk` both read the commitment register, because an unmet sales-cycle promise is a frequent root cause of the first escalation and an unavoidable topic in the first review.

## Quality bar

Good handoff work reads like a record written by someone who expected to be quoted from it a year later. The contract facts section is quoted, with clauses named, and the notice deadline shows its arithmetic rather than asserting a date. The commitment register has entries, including uncomfortable ones, and each names a person. The reconciliation section preserves differences instead of resolving them toward whichever reading is easier to deliver. The customer's reason for buying is in their words, with their metric names, because a business review eighteen months later is judged against that sentence and not against the product's positioning. And the acceptance decision is willing to say not accepted, with conditions and owners, because an onboarding that starts on an incomplete handoff does not fail at kickoff; it fails four weeks later on a dependency nobody knew existed, and by then the delay belongs to customer success.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
