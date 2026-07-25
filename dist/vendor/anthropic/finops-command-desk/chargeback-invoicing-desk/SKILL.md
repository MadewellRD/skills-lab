---
name: chargeback-invoicing-desk
description: design and operate internal cloud chargeback and showback covering the model and its rationale, the internal rate card with the basis for any markup or subsidy, a chargeback ledger that balances to the provider invoice with the residual shown rather than absorbed, cost center postings with the allocation rule behind each figure, statements detailed enough for a recipient to check rather than only to pay, and dispute intake and resolution that either corrects the allocation rule for everyone or defends it. use for chargeback design, internal billing runs, cost center statements, rate card setting, and allocation disputes.
---

# Chargeback And Invoicing Desk

## Suite workflow mode

This desk is a member of the FinOps Command Desk suite. Complete the chargeback artifact set, update the `finops_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. A residual that no defensible rule allocates is a soft gap and appears in the ledger as a residual with its cause; a ledger that does not tie to the invoice is a hard halt before anything posts, because a posted period is audit-visible and unwinding one is a finance exercise that costs more than the allocation was worth.

Never invent cost center codes, ledger accounts, posting amounts, rate card figures, allocation rules, dispute outcomes, approval states, or the period a posting belongs to.

## Role

Own the internal bill. This desk holds the chargeback or showback model with the rationale that suits the organization's structure, the internal rate card with the basis for any markup or subsidy, the chargeback ledger that balances to the provider invoice with any residual shown rather than absorbed, postings per cost center with the allocation rule that produced each figure, the statement each cost center receives with enough detail to check the number rather than only to pay it, dispute intake naming the specific allocation rule under challenge, resolution that either corrects the allocation for everyone or explains why the rule holds, the model change proposal where disputes reveal a structural problem, and the reconciliation between what was charged internally and what was billed externally.

Two properties separate this stage from showback reporting. The output is a financial transaction rather than an analysis, so it goes into a ledger, sits inside a close, and is read by an auditor. And it changes behavior whether or not anyone intended it: a rate card that charges for storage but not for egress produces an estate with a lot of egress, and the model teaches an organization what to optimize as surely as any policy does.

## Use when

- A chargeback or showback model is being designed, revised, or moved from showback to chargeback, and the method needs choosing along with what it will fail to allocate.
- A periodic internal billing run is due and the ledger has to balance to the invoice before anything posts.
- Cost center statements need producing at a level of detail that lets the recipient check the figure rather than only accept it.
- An internal rate card is being set or revised, including any markup for platform services or subsidy for shared capability, and the over-recovery or under-recovery position needs stating.
- A cost center disputes a charge, and the dispute needs resolving against the specific allocation rule rather than against the amount.
- Disputes have revealed a structural problem in the model and a change proposal is needed, with its effective period and its before-and-after shown together.
- The internal ledger and the provider invoice have diverged and the tie-out needs establishing before the period closes.

## Do not use when

- The allocation itself is incomplete, the coverage is unmeasured, or shared pools have no agreed split method. That is `cost-allocation-tagging-desk` and `shared-cost-allocation-desk`; posting a chargeback over an unresolved allocation produces a charge a team can prove is wrong, and that costs the practice more credibility than any delay does.
- The audience is engineers who need to act rather than cost center owners who need to be charged. That is `engineering-cost-review-desk`, a different artifact with a different cadence and no ledger behind it.
- The subject is external revenue, cost of revenue classification, capitalization, or gross margin. That is `software-cogs-margin-desk`, and the financial close belongs to the Finance and Accounting suite.
- The subject is a budget rather than a charge. That is `budget-planning-desk`.
- The subject is a provider invoice dispute with the vendor rather than an internal dispute between cost centers. That is a labeled cross-suite handoff to Procurement and Vendor Management, with the evidence supplied here.

## Required evidence

- The fully allocated dataset including direct attribution, shared pool splits with their methods, container allocation, and the residual, with the allocation coverage figure that came with it.
- The provider invoice for the period, which is what the ledger has to balance to, plus any credits, refunds, adjustments, and corrections applied outside the export.
- The cost center structure and the ledger accounts the postings land in, taken from the finance system rather than from a tagging inventory.
- The chargeback model and its approval state, including who signed off on each split method and from which effective period.
- The internal rate card where one exists, with the basis for each rate, any markup or subsidy, and the volume assumption the rate was set against.
- The finance posting calendar with the close dates, the period state, and the controller who owns the close.
- Dispute history with the rule challenged, the outcome, and any allocation change it forced.
- Prior period postings and their reconciliation state, since a recurring variance is a model problem rather than a period problem.

## Workflow

**Outcome.** A chargeback ledger that balances to the invoice with any residual shown; postings per cost center with the allocation rule behind each figure and its approval state; the internal rate card with the basis for every rate, markup, and subsidy and the recovery position it produces; a statement per cost center detailed enough to check; a dispute register with each dispute tied to a specific rule and resolved by correcting the rule or defending it; and a model change proposal where the dispute pattern shows a structural problem.

**Grounding.** The provider invoice is the anchor and every internal total ties to it or carries a stated and explained variance. Postings carry the rule that produced them, since a cost center owner who cannot see why they were charged cannot check the charge and will either accept everything or dispute everything, and both are failures of the model. Rate card figures carry the volume assumption they were set against, because a rate set on forecast volume produces over-recovery or under-recovery the moment volume differs, and that variance has to land somewhere visible.

**Constraints.** The ledger balances to the invoice, and the residual is a line in the ledger rather than an adjustment spread across cost centers to make the arithmetic close. Split methods carry their approval state and their effective period, because a method change moves what teams are charged without any team changing behavior and the first person to notice is the one whose number went up. A rate card states its markup or subsidy explicitly, along with the recovery position, since a platform rate that quietly under-recovers is a subsidy nobody approved. Statements are built for checking: the services, the volumes, the rate applied, the shared allocations with their driver, and the movement against the prior period with its cause. Disputes are logged against the rule rather than the amount, and a dispute that is upheld corrects the rule for every cost center it affected rather than issuing a credit to the one that complained, because a model that is only correct for the teams that argue is not a model. Retroactive changes to a posted period do not happen here; a correction applies from a stated effective period with the before and after shown together, unless the controller who owns the close decides otherwise.

The posting sequence is mandated, and the reason is recorded here so a later editor does not read it as scaffolding: a posted period is audit-visible and reversing one requires finance to unwind it across every affected cost center.

1. Confirm the period state with the controller, and confirm that the allocation and any split method changes carry their approvals with an effective period.
2. Tie the allocated total to the provider invoice, and either explain the variance or record it with its size as unexplained.
3. Show the residual as a residual, and produce the postings and statements from the approved rules.
4. Obtain the controller's authorization for the posting, then post inside the finance calendar for that period.

**Parallel surface.** Cost centers, statements, and individual disputes are independent units and fan out safely, as do the per-cost-center posting composition, the per-statement detail assembly, and the per-dispute rule lookup. The ledger itself is not part of that surface. It has to balance to one invoice, so it is built once over the full allocated set after the fan-out returns, and the tie-out, the residual determination, the rate card recovery position, and the model-level dispute pattern are all whole-set calculations. A ledger assembled from per-cost-center views that each look complete is exactly how a plug ends up in the largest cost center, and it will balance, which is why nobody catches it.

**Acceptance bar.** The ledger balances to the invoice or carries an explained variance with its size. Every posting names its allocation rule and that rule's approval state. The residual is visible with its cause. Every rate names its basis, its markup or subsidy, and its recovery position. Every statement contains enough to let a recipient check the largest line without asking. Every dispute names the rule it challenges and its resolution names what changed for everyone. Nothing has been posted without the named authorization.

## Outputs

A complete run delivers this set:

- `chargeback-model.md`: the model with its rationale against the organization's structure, the allocation rules in force with their approval state and effective period, the behavior the model will incentivize, and what it deliberately does not allocate.
- `rate-card.md`: each internal rate with its basis, its volume assumption, any markup or subsidy stated explicitly with who approved it, and the over-recovery or under-recovery position the current period produces.
- `chargeback-ledger.md`: the full ledger balancing to the provider invoice, with the residual as a line, credits and adjustments handled explicitly, and the tie-out variance stated with its explanation or recorded as unexplained with its size.
- `cost-center-postings.md`: postings per cost center with the amount, the period, the allocation rule that produced each figure, the ledger account, and the posting state as draft, approved, or posted.
- `cost-center-statements.md`: the statement each recipient receives, with services and volumes, the rate applied, shared allocations with their driver and method, movement against the prior period with its cause, and the contact and route for raising a dispute.
- `dispute-register.md`: each dispute with the cost center, the amount, the specific rule challenged, its state, and the resolution including whether the rule was corrected for everyone or defended with the reasoning.
- `model-change-proposal.md`: where the dispute pattern shows a structural problem, the proposed change with its effective period, the before-and-after impact by cost center shown together, and the approval it requires.
- `invoice-tie-out.md`: the reconciliation between what was charged internally and what was billed externally, by period, with recurring variances identified as model issues rather than period issues.
- `chargeback-downstream-handoff.md`: what `finops-maturity-desk` inherits, including the disputes that revealed allocation gaps and the coverage that limits the model.

Depth standard: an artifact is complete when the controller could approve the posting from it and a cost center owner could check their largest line without contacting anyone. A ledger that balances without showing its residual, a posting with no rule behind it, a rate with no basis, and a dispute resolved against an amount rather than a rule are unfinished rather than draft.

When the allocated dataset, the provider invoice, the cost center structure, or the ledger extract exists and cannot be read, the run delivers `chargeback-connector-diagnostic.md` naming each unreachable source and the postings, tie-out, and statements it makes impossible, in place of the ledger that source would have grounded. Postings are never produced against a cost center structure taken from a tagging inventory.

Anti-fabrication guard: the tell on this desk is a ledger that balances perfectly, because balancing is the one property everyone checks and the easiest to manufacture. The residual in an internal bill is real: shared capacity nobody consumed on purpose, cluster idle, an untagged account, a credit that arrived after the split was computed, a rounding difference across thousands of postings. Every one of those has a defensible treatment and none of them is a quiet addition to the largest cost center, which is what happens when the arithmetic is closed before the cause is understood. So the residual appears as its own line with its cause, a variance against the invoice is stated with its size even when it cannot be explained, and a period where the tie-out failed is reported as not reconciled rather than posted. Cost center codes, ledger accounts, and posting amounts come from the finance system and the allocated dataset, never from a tag value that looks like a cost center, because a posting to the wrong account is a correcting journal entry somebody else has to write. Rate card figures carry the volume assumption and the recovery position, since a rate quoted without either is a number that will be wrong next month in a direction nobody is watching. And a dispute is never settled by adjusting one cost center's charge, because a model that bends for whoever complains loudest is a model the quiet teams are subsidizing.

## finops_packet fields to update

- `chargeback.model` and `chargeback.model_rationale` with the structure the model suits and what it deliberately leaves unallocated
- `chargeback.ledger_ties_to_invoice` and `chargeback.tie_out_variance` with the difference and its explanation where one exists
- `chargeback.postings[]` with cost_center, amount, period, the allocation basis that produced it, and state as draft, approved, or posted
- `chargeback.disputes[]` with dispute_id, cost_center, amount, the rule challenged as the basis, state, and resolution including any allocation rule change it forced
- `allocation.shared_cost_pools[].approved_by` and `rationale` updated where a dispute changed a split method, with the effective period recorded
- `allocation.unallocated` reflecting the residual as carried into the ledger, with its cause breakdown
- `reconciliation.invoice_total`, `dataset_total`, `variance_amount`, `variance_pct`, `variance_explanation`, and `state`
- `governance.approvals[]` with the posting, the rate card, and any model change as items, each with the amount at stake, the required approver, and the authority basis
- `cogs.period_state` and `cogs.controller_owner` where the posting interacts with the close
- `source_facts[]` with locator and as-of for every invoice, ledger, and allocation reading, `assumptions[]`, `open_questions[]`
- `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: posting a chargeback moves money between cost centers in the ledger, and reversing a posted period requires finance to unwind it. A posting into a closed period, a retroactive model change applied to periods already posted, and a ledger that does not tie to the invoice each stop at the gate with the controller. This is the defining halt of this desk.
- **Missing approval**: a model change, a new or revised split method, a rate card, a markup or subsidy, or the posting itself needs the owner of the allocation model, the controller, or the authority the matrix names, and has not been granted.
- **Release integrity**: statements would go to cost centers with a total that does not tie to the invoice, with the residual absorbed rather than shown, or with an allocation rule whose approval state is unknown. An internal invoice is quoted in budget conversations for the rest of the year.
- **Source conflict**: the allocated dataset, the provider invoice, and the ledger extract genuinely disagree on the total for a period, or the tag inventory and the finance system name different cost centers for the same spend. Record both readings with locators and as-of dates and route the conflict; the ledger governs for financial reporting.
- **Security or privacy**: a statement would expose another cost center's detail, customer identifiers, unredacted commercial terms, or the existence of a restricted workload to a recipient who should not see it.
- **Connector unreachable**: the allocated dataset, the invoice, the cost center structure, or the ledger extract exists and cannot be read, so a posting would be produced against a structure or a total nobody can confirm.

An unresolved residual cause, an unowned cost center, a dispute awaiting information from the challenger, and a rate whose volume assumption has drifted are soft gaps. Name them, label the assumption in the ledger and the affected statement, and continue with the draft postings prepared and unposted. Closing a tie-out variance by adjusting a cost center's charge is never an acceptable way to meet a posting deadline.

## Downstream handoffs

`finops-maturity-desk` is next in the default sequence and receives the model, its dispute pattern, and the coverage that bounds it as direct evidence of allocation and accountability capability. `cost-allocation-tagging-desk` and `shared-cost-allocation-desk` receive every dispute that resolved into an allocation rule change, since that is where the fix belongs. `engineering-cost-review-desk` receives the postings that will generate questions, so the team conversation and the statement do not contradict each other. `budget-planning-desk` receives the recovery position and any rate change as an input to the next cycle. `optimization-backlog-desk` receives realized savings reflected in cost center statements, because a reduction that never reaches a team's statement is one they have no reason to repeat. Send the financial close, the journal entries, revenue recognition, and statutory reporting to the Finance and Accounting suite; send any provider invoice dispute to Procurement and Vendor Management with the evidence attached.

## Quality bar

Good chargeback is defensible line by line and boring by design. Its ledger ties to the invoice, and where it does not, the variance is stated with its size rather than smoothed. Its residual has a name and a cause and sits in plain view, because the residual is the honest part of an internal bill and hiding it is the moment a model starts lying. Its statements are built for a recipient who intends to check, with the rule, the driver, and the movement all present, which produces fewer disputes rather than more. Its rates carry their basis and their recovery position, so a subsidy is a decision somebody made rather than a drift nobody noticed. Its disputes are argued about rules, and a rule that loses gets corrected for every cost center it touched, not just for the one that complained. It changes methods prospectively with the before and after shown together. And it never posts into a period it has not confirmed with the controller, because the cost of being early to a close is measured in other people's correcting entries.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
