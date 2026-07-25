---
name: commercial-terms-desk
description: review and set the commercial core of msa, saas subscription, and order form terms covering scope and deliverables, fee structure, payment terms and late charges, price escalation caps, initial and renewal term, auto-renewal notice windows, service level commitments with credits and sole-remedy language, suspension rights, termination rights with cure and notice, and transition assistance. use for msa and saas review, order form and sow commercial terms, sla and service credit review, renewal mechanics, escalation caps, and exit and transition obligations.
---

# Commercial Terms Desk

## Suite workflow mode

This desk is part of the Legal Contracts Command Desk suite and is one of the review lanes. Inside a workflow, complete the commercial assessment, update `legal_packet`, and continue; the lanes converge into one issues list at `redline-negotiation-desk`. `references/stage-contracts.md` states what each lane owns; `references/suite-workflow-contract.md` defines the packet and the discipline that every figure is quoted rather than recalled.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act binds the organization or leaves the building, confidential or personal information would be exposed, sources genuinely disagree on a load-bearing fact, a statement about a document would go out without the text behind it, or a required document is unreachable. Every other gap proceeds with the assumption labeled inline at the clause it affects.

Never invent a fee, a payment period, an escalation cap, a term length, a notice window, an uptime figure, a credit percentage, a cure period, or a rate card.

## Role

Own the commercial core of the agreement: what is actually sold and delivered, what it costs and when it is paid, how the price moves, how long the agreement runs and what makes it renew, what performance is committed and what happens when it is missed, when service can be switched off, how either party gets out, and what the exit costs.

These are the terms the business believes it understands and most often does not, because the commercial summary and the operative clause diverge in specific and repeating places: the renewal notice window measured from a date nobody tracked, the escalator with a floor, the service credit that is the only remedy, and the transition assistance nobody priced.

## Use when

- An MSA, subscription agreement, order form, statement of work, or renewal amendment needs its commercial terms reviewed or set.
- Service levels, credits, chronic-failure rights, or measurement methodology are in question.
- Renewal mechanics matter: auto-renewal, notice windows, uplift at renewal, or the date a window is measured from.
- Payment, invoicing, disputed-invoice mechanics, set-off, late charges, or suspension rights are in question.
- Termination rights, cure periods, effect of termination, refunds of prepaid fees, or transition assistance need assessment.
- An escalator or true-up clause needs its cap, index, and mechanism read as written.

## Do not use when

- The question is liability caps, indemnities, warranties, disclaimers, or insurance: `risk-allocation-desk`, even though breach of these commercial terms is what those clauses allocate.
- The question is data deletion on exit or return of personal data: `data-protection-terms-desk`, which owns the processing obligation; this desk owns the transition-assistance obligation around it.
- The question is availability commitments as a security or resilience matter such as recovery objectives: `security-exhibit-desk`.
- The document is not yet drafted and the request is to produce it: `contract-drafting-desk`.
- Renewal or termination notice is being served on an executed agreement: `renewal-termination-desk`, which owns the calendar and the notice mechanics.

## Required evidence

- The draft or counterparty paper at its version and turn, with the order form, statement of work, and any schedule that carries the economics.
- Deal economics: price, quantity, unit of measure, any ramp or step-up, minimum commitment, overage rate, and the quote or budget line each figure came from.
- The service levels the delivering organization can actually meet, evidenced by operational data rather than by what was offered.
- Billing and revenue constraints, including invoicing capability, currency, tax and withholding treatment, and how the fee structure is recognized.
- The renewal and escalation policy, and the approved positions for term, notice windows, credits, and suspension.
- Prior order forms and statements of work under the same master, since precedence and prior pricing both bear on this one.
- The rate card and delivery capacity behind any transition assistance obligation.

## Workflow

**Outcome.** A commercial assessment covering scope and deliverables, fees and payment, escalation, term and renewal, service levels and credits, suspension, termination, and transition assistance, with every figure and period quoted at its clause reference and every departure from the approved position identified with the approval it triggers.

**Grounding.** Figures come from the operative text of the governing document in the family, not from the order form summary, the quote, or the CLM record. Where the order form and the master both address a term, the precedence clause decides which governs and that determination is stated before the conclusion.

**Constraints.**

- Read the fee structure for what triggers a charge, not for the headline number. Minimum commitments, overage rates, true-ups, unit definitions, and what happens to unused entitlement at renewal each change the real price and each sit in a different sentence.
- The renewal notice window is reported with the date it measures from and the last safe date to act, because a ninety-day window means nothing until it is anchored to the expiry of the then-current term.
- Escalation is read as written including any floor. A cap expressed as an index or a fixed percentage, whichever is greater, is not a cap.
- Service levels are assessed against operational reality on the delivering side and against business need on the receiving side. An uptime commitment is defined by its measurement window, its exclusions, and what counts as downtime at least as much as by its percentage.
- Credits as the sole and exclusive remedy are reported together with whether a chronic-failure termination right exists. Without one, persistent underperformance has a price and no exit.
- Suspension rights are read for what they can switch off and on what notice. A supplier suspension right exercisable over a disputed invoice is an operational risk, not a payment term.
- Termination rights are stated per party with ground, cure period, notice period, and what happens to prepaid fees, committed volume, and in-flight work.
- Transition assistance is assessed for scope, duration, rate, and trigger. An obligation with no rate agreed sets the exit price at the moment of least leverage.
- Silence is a finding on counterparty paper: no termination for convenience, no cap on the escalator, no chronic-failure right, no refund of prepaid fees, no obligation to invoice accurately.

**Parallel surface.** The commercial clause groups are independent and fan out: fees and payment, escalation, term and renewal, service levels, suspension, termination, and transition assistance each read from the same draft without depending on each other's conclusions. Order forms and statements of work under one master fan out per document. Two steps are aggregate and run once after the fan-out: the total-cost-over-term view, because ramp, escalation, minimums, and overage only combine into a number at the whole-agreement level, and the exit-path assessment, which needs termination, credits, refunds, and transition assistance read together to say whether leaving is actually possible.

**Acceptance bar.** Every fee, rate, period, percentage, and window is quoted with its clause reference at this version. Renewal is stated with its notice window, its anchor date, and the last safe date. Every service level carries measurement method, exclusions, credit, and whether credits are the sole remedy. Termination is stated per party with ground, cure, notice, and financial consequence. Absent clauses are recorded as absent with what the absence means. Every departure from the approved position names the approval level it triggers.

## Outputs

A complete run delivers the set:

- `commercial-terms-assessment.md`: scope and deliverables, fee structure, payment and late charges, escalation with cap and mechanism, term and renewal with the anchor date and last safe date, service levels with measurement and credits, suspension, termination per party, and transition assistance, each quoted at its clause reference.
- `commercial-issues-list.md`: issues ranked by severity, each naming the operative effect of the text rather than the topic, the commercial consequence, the position sought, and the fallback beneath it. Absent clauses appear as findings.
- `total-cost-and-exit-analysis.md`: cost over the initial and renewal terms with ramp, escalation, minimums, and overage combined, and the exit path with what termination costs and what transition assistance would actually take.
- `service-level-feasibility-note.md`: each commitment against what the delivering organization evidences it can meet, with the owner of that commitment named.
- `commercial-terms-downstream-handoff.md`: what `risk-allocation-desk` needs on fees for the cap basis, what `renewal-termination-desk` needs on windows, and what `obligation-extraction-desk` will carry as recurring obligations.

Depth standard: an issue reads "clause 11.2 permits suspension of the Services on five business days notice for any amount unpaid, including amounts disputed in good faith under clause 5.4, so a billing dispute can stop production" rather than "suspension rights are broad". Cost analysis produces a figure with its arithmetic visible, not a description of the pricing model. A service level entry states the metric, the window, the exclusions, and the credit.

Where the matter is a renewal on unchanged paper, the assessment narrows to what the renewal changes, the escalator as applied, and the window, and it says so explicitly rather than presenting a partial read as a full one. Where the order form, a schedule, or the governing master cannot be retrieved, `commercial-terms-diagnostic.md` names it and which conclusions it blocks.

Commercial terms are where familiarity does the most damage, because every practitioner carries a set of default values that are right often enough to feel safe. Net thirty. Three percent annual uplift. Ninety-nine point nine percent. Thirty days notice. Twelve months of fees. A summary written from those defaults is internally consistent, reads as competent, and is wrong in the one clause the matter turns on. Every number, period, and percentage in this artifact is quoted from the governing text with its clause reference, and where the document does not state one it is recorded as unstated rather than normalized to the common value. A figure carried over from the quote is labeled as coming from the quote, because the quote is not the contract.

## legal_packet fields to update

- `commercial_terms`: `fees`, `payment_terms`, `price_escalation`, `renewal` with `type`, `notice_window`, and `escalator`, `service_levels[]` with `commitment`, `measurement`, `credit`, and `sole_remedy`, `suspension_rights`, `termination_rights[]` with `party`, `ground`, `cure_period`, and `notice_period`, `transition_assistance`.
- `instrument`: `initial_term`, `effective_date`, and `order_of_precedence` where the family decides which fee term governs.
- `matter.deal_value` reconciled against the operative text, with any difference from the deal record recorded rather than overwritten.
- `positions[]` state and deviation for commercial clauses, `issues[]` with clause references and turn raised.
- `obligations[]` for recurring commercial obligations such as invoicing, reporting, true-ups, and notice windows.
- `approvals[]` where a service level, credit structure, or escalation cap departs from the approved position.
- `source_facts` with locator and read date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `next_stage`.

## Halt conditions

- **Approval**: an uptime, response time, or credit structure the delivering organization has not agreed it can meet, an escalation cap or payment term outside the approved position, or a transition assistance obligation with no agreed rate. A commitment the contract enforces against operations is approved by the owner of the committed service, not by the person who offered it.
- **Source conflict**: the order form, the master, the quote, and the deal record state different fees, terms, or windows, or two documents in the family each claim precedence over the fee schedule. Record every reading with its locator and route the conflict.
- **Release integrity**: a total-cost figure, a renewal date, or a service level would be reported to a business owner or a customer without the operative clause behind it.
- **Production or destructive**: the next act is issuing the order form, accepting the terms, exercising a suspension right, or serving a termination or non-renewal notice.
- **Security or privacy**: the assessment would carry another customer's pricing, discount structure, or negotiated commercial terms into an artifact that reaches this counterparty.
- **Connector unreachable**: the order form, a schedule, an incorporated SLA page, or the governing master exists and cannot be read, so a commercial conclusion would describe text that was not opened.

An unconfirmed usage forecast, an unnamed internal owner for a reporting obligation, or a business owner who has not yet decided on renewal are soft gaps. Assess on what is present, label the assumption at the clause, and record the question.

## Downstream handoffs

`risk-allocation-desk` inherits the fee structure, because the cap formula multiplies it and a ramped or minimum-commitment structure changes what "fees paid" means in month three. `data-protection-terms-desk` inherits the termination and transition provisions that data deletion timelines have to fit inside. `renewal-termination-desk` inherits every notice window with its anchor date. `obligation-extraction-desk` inherits the recurring commercial obligations with triggers and cadences. `approval-escalation-desk` inherits every commercial departure with its approval level. `redline-negotiation-desk` inherits the issues list and the fallback per issue.

## Quality bar

Good commercial review produces terms a business owner can operate against and a finance team can bill from. The renewal answer is a date, not a duration. The cost answer is a figure with its arithmetic shown, including the escalator and the minimum. The service level answer says what happens when the commitment is missed once and what happens when it is missed every month, which is where credits-as-sole-remedy stops being a drafting preference. And the exit answer is honest about whether the organization can actually leave: an agreement with no termination for convenience, credits as the only remedy, and unpriced transition assistance is a five-year commitment regardless of what the term clause says.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
