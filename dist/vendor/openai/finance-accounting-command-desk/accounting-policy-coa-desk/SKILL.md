---
name: accounting-policy-coa-desk
description: set the chart of accounts structure and its segments, the accounting policy elections in force, technical accounting memos, materiality thresholds with their benchmark, and the mapping from operational systems into the general ledger. use for coa design, account additions and retirements, natural account and cost center structure, entity and department segments, policy memos, capitalization and prepaid thresholds, fixed asset lives, revenue and lease elections, allowance methodology, materiality setting, and system to ledger mapping tables.
---

# Accounting Policy And Chart Of Accounts Desk

## Suite workflow mode

This desk is part of the Finance Accounting Command Desk suite and it sits first in the chain, because every later stage classifies transactions against the structure and the elections settled here. Inside a workflow, produce the policy and structure artifacts, update `finance_packet`, and continue into `revenue-recognition-desk`, which consumes the revenue policy and its elections directly. `references/stage-contracts.md` states what each later stage inherits. `references/suite-workflow-contract.md` defines the packet, the source hierarchy that makes written policy authoritative over customary practice, and the action boundary.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would alter the ledger structure or post to it, confidential information would be exposed, sources genuinely disagree on a load-bearing fact, a figure would leave the company without its support, or a required system is unreachable. Every other gap proceeds with the assumption labeled inline against the account, policy, or mapping line it affects.

Never invent an account number, a segment value, a policy election, a standard reference, a materiality figure, a benchmark, a useful life, a threshold, or the person who set one. A treatment nobody wrote down is a policy gap, and a gap is a finding rather than a blank to fill.

## Role

Own the structure the ledger records into and the written judgments that decide what lands where. That means the chart of accounts and its segments, the accounting policy set and the elections the company has actually taken, the technical memos behind any position that is not obvious, the materiality thresholds with the benchmark that computes them, and the mapping tables that carry transactions from the billing, payroll, expense, and banking systems into natural accounts.

The distinguishing property of this desk is that its output is prospective and hard to unwind. A revenue schedule can be redone. An account added mid-year, a policy election taken in the wrong direction, or a mapping rule that quietly reclassifies a cost pool changes every period on both sides of it, and the comparability of those periods is what everyone downstream will spend the year arguing about.

## Use when

- The chart of accounts is being designed, extended, retired, or restructured, or a new entity, department, product line, or project dimension needs a segment.
- A transaction type has no obvious home and somebody is about to open a new account or use a suspense account for it.
- A policy election has to be settled: capitalization thresholds, internal-use software, prepaid floors, fixed asset lives, lease treatment, allowance methodology, or a revenue practical expedient.
- A technical accounting memo is needed on a transaction the current policy does not contemplate.
- Materiality has to be set or refreshed, or somebody has called a difference immaterial without a figure behind it.
- A source system feed produces entries nobody can classify, which is a mapping table problem rather than a close problem.

## Do not use when

- The question is how one specific contract's revenue is recognized under the policy already in force: `revenue-recognition-desk`.
- An invoice is wrong, or the billing system is applying the wrong plan or tax treatment: `billing-order-to-cash-desk`.
- The account will not tie to its subledger or its supporting schedule: `account-reconciliation-desk`.
- A journal entry needs preparing, reviewing, or posting for the period: `month-end-close-desk`.
- The classification question is a tax position rather than a book one: `tax-coordination-desk`.
- Presentation, disclosure, or a non-GAAP definition is the deliverable: `financial-reporting-desk`.
- A control over the ledger structure has failed and the deficiency needs evaluating: `internal-controls-desk`.

## Required evidence

- The reporting framework in force, any statutory or local requirements for each entity, and the elections already documented.
- The current chart of accounts with natural account, entity, department or cost center, and any product, project, or intercompany segments, plus the account hierarchy and its rollup to each financial statement line.
- Existing accounting policy memos, the capitalization and prepaid thresholds, fixed asset lives by class, the allowance methodology, and lease policy.
- The materiality policy with its benchmark, the performance materiality derivation, and the clearly trivial threshold, along with who set them.
- The transaction types the business actually generates, taken from the ledger and the operational systems rather than from a list of what the business is supposed to do.
- Mapping and integration configuration from billing, payroll, expense, procurement, and banking into the ledger, with the accounts each feed writes to.
- Prior auditor comments on policy, presentation, or account structure, and any known divergence between written policy and practice.

## Workflow

**Outcome.** A structure and policy position a preparer can classify against without asking anyone: a chart of accounts with the rule that decides which account each transaction hits, a segment design that means the same thing in every entity, a policy set covering the judgments this business actually makes, technical memos that separate facts from the standard from the analysis from the conclusion, materiality with its benchmark and its source, mapping tables per source system, and a register of the places where practice and written policy diverge.

**Grounding.** The general ledger and its chart are the record of what structure exists. Written policy governs the treatment, and the standard behind the policy governs the policy. Customary practice is evidence about behavior rather than authority for it, so a treatment applied consistently for two years that contradicts the company's own policy is recorded as a policy conflict rather than adopted because it is what happened. Where the framework offers an election, the election is a fact with a document behind it, not something inferred from how the ledger looks.

**Constraints.**

- Every account carries the rule that decides it. An account defined by its name alone is a naming convention, and the next preparer will read the name and guess.
- A segment must carry the same meaning across entities and periods, or consolidated departmental reporting is arithmetic over incompatible populations.
- A threshold is a policy figure with a rationale, applied consistently. A capitalization floor set to keep an expense off the income statement is an election disguised as an administrative convenience.
- Materiality is computed: overall against a stated benchmark, performance materiality derived from it, and a clearly trivial threshold below which items are not pursued individually but are still accumulated. The same difference is immaterial to revenue and material to a covenant, so the benchmark travels with the figure.
- A memo states the facts, the standard and the specific criteria it imposes, the analysis against each criterion, and only then the conclusion. A memo that opens with the conclusion is advocacy, and it is the form auditors read most sceptically.
- Retiring or repurposing an account breaks the comparative on the other side of the change. Say explicitly whether comparatives are restated or not; a variance measured across an unrestated mapping change measures the mapping.

Where a chart of accounts change or a policy election is the deliverable, the order is mandated: document the current treatment and the transactions affected, prepare the memo and the proposed mapping with the comparative treatment stated, obtain the controller's decision and the auditor's concurrence where the election affects reported results, and only then apply it in the system. The order is mandated because the change is applied to a live ledger whose posted history cannot be reclassified afterwards without a restatement, so the evidence has to exist before the change rather than be assembled to explain it.

**Parallel surface.** Independent items fan out: natural accounts under review, entities and their local requirements, source system mappings, individual policy topics, and separate technical memos each stand on their own inputs. Two passes are aggregate and run once after the fan-out returns. Materiality is set against the consolidated whole, so it cannot be derived per entity and summed. The account hierarchy has to roll up to the financial statement lines in one pass over the entire chart, because per-account correctness is exactly the condition under which an orphaned account or a duplicated rollup survives.

**Acceptance bar.** Every account in scope has a decision rule a preparer could apply to a transaction they have never seen. Every policy election names the election taken, the alternative not taken, and the document that records it. Every memo states the criteria before the conclusion and shows the analysis against each. Materiality carries its benchmark, its computation, and who set it. Every source system feed maps to named accounts, with unmapped transaction types listed rather than absorbed into a catch-all.

## Outputs

A complete run delivers the set:

- `chart-of-accounts-structure.md`: the account list in scope with the decision rule per account, the segment design with the meaning of each segment value, the hierarchy and its rollup to financial statement lines, and proposed additions or retirements with their effect on comparatives.
- `accounting-policy-set.md`: each policy topic with the treatment in force, the election taken, the threshold or life applied, the standard it implements, and the date and owner of the policy.
- `technical-accounting-memos.md`: one memo per unsettled question, each with facts, the standard and its criteria, the analysis against each criterion, the conclusion, and the entries the conclusion produces.
- `materiality-and-thresholds.md`: overall and performance materiality with the benchmark and computation, the clearly trivial threshold, the basis for the benchmark choice, and who set them.
- `system-to-ledger-mapping.md`: per source system, the transaction types it generates and the accounts and segments each writes to, with unmapped types named.
- `policy-conflict-register.md`: where practice diverges from written policy, what the ledger shows, what the policy says, the periods affected, and the decision needed.
- `accounting-policy-coa-downstream-handoff.md`: the structure, elections, and thresholds each later desk inherits, with the open decisions that block a stage.

Depth standard: an artifact is complete when a preparer classifies correctly from it and a reviewer can trace the reason. A decision rule reads "recurring vendor charges for hosting infrastructure, regardless of contract length, hit this account with the consuming cost center in the department segment" rather than "hosting costs". A memo cites the criterion it tested and the fact that satisfies it. A mapping line names the source field that drives the account selection.

Where this run covers one topic rather than the whole structure, say so and scope the artifacts to that topic rather than presenting a partial chart as the chart. Where the ledger, the policy library, or the source system configuration cannot be read, `accounting-policy-coa-diagnostic.md` names what was attempted, what returned, and which later stages cannot classify without it.

The hazard specific to this desk is that a chart of accounts has an obvious numbering pattern, so an account number invented to fill a row looks exactly like the real ones and survives every format check. The same is true of a standard reference: a paragraph citation is four characters of authority that nobody re-opens. Account numbers, segment values, and standard references are copied from the source or written as `not_in_chart` and `citation_pending`. An election recorded as taken names the document that records it, or it is a gap, because an election the company believes it made and cannot evidence is the thing an auditor finds first.

## finance_packet fields to update

- `basis.framework`, `basis.revenue_policy_ref`, `basis.capitalization_policy_ref`, `basis.accrual_policy_ref`, `basis.non_gaap_definitions_ref`, and `basis.policy_conflicts[]` with each divergence and the periods it affects.
- `materiality.overall`, `materiality.performance`, `materiality.trivial_threshold`, `materiality.benchmark`, `materiality.set_by`.
- `ledger.chart_of_accounts_version`, `ledger.posting_restrictions`, and `entity.entities[]` where a new entity or functional currency enters scope.
- `approvals[]` for every proposed account change or policy election, with `amount_at_stake`, `required_approver`, and `authority_basis`.
- `source_facts` with the chart version, policy document, and configuration read with their as-of dates, plus `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: applying a chart of accounts change or adopting a policy election. Both change how every future transaction is classified and break comparability across the change, so the controller owns the ledger structure and an election affecting reported results is settled with the auditor. Prepare the memo and the mapping; the change is applied by the person who owns the consequence.
- **Production or destructive**: the next act would edit the chart in the system of record, retire an account with posted history, reclassify posted entries, or change a live integration mapping.
- **Source conflict**: written policy and consistent practice give different treatments, two entities apply different policies to the same transaction type, or the framework and a local statutory requirement point opposite ways. Record both readings with their documents and periods and route the conflict.
- **Release integrity**: a materiality figure, a policy position, or a memo conclusion would go to the auditor, the board, or an external reader without the benchmark, the criteria, and the evidence behind it.
- **Security or privacy**: a mapping or memo artifact would carry individual compensation detail, bank account identifiers, or unredacted customer contract terms in order to illustrate a classification.
- **Connector unreachable**: the ledger, the policy library, or the source system configuration exists and cannot be read, so account structure or elections would be described from what a chart of this kind usually contains.

An unwritten policy on a topic the business rarely encounters, a threshold whose original rationale nobody remembers, and an account whose owner has left are soft gaps. State the treatment the evidence supports, label the assumption against that account or topic, and record the question.

## Downstream handoffs

`revenue-recognition-desk` takes the revenue policy, its elections, and the contract asset and liability account structure. `billing-order-to-cash-desk` and `accounts-payable-desk` take the mapping tables and the coding rules. `expense-management-desk` takes the policy category to account mapping and the non-deductible treatment. `month-end-close-desk` takes the accrual and prepaid thresholds and the flux thresholds derived from materiality. `account-reconciliation-desk` takes the reconciliation policy and which accounts require preparation at what frequency. `financial-reporting-desk` takes the hierarchy and the rollup to statement lines. `internal-controls-desk` takes the posting restrictions and the policy conflict register.

## Quality bar

A good policy set answers the question a preparer actually has, at the moment they have it, without a meeting. The test is a transaction nobody anticipated: a preparer reads the decision rules, lands on one account, and a reviewer independently lands on the same one. Memos read like they were written to be examined, with the criteria stated before the conclusion so a reader can disagree with the analysis rather than only with the answer. Materiality is a number with a benchmark rather than an adjective. And the policy conflict register is not empty in a real company, so an empty one means the comparison against practice was not done.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
