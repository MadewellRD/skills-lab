# Finance and Accounting Suite Workflow Contract

This file defines how Finance Accounting Command Desk skills run as one continuous accounting and planning cycle rather than as a set of disconnected questions about numbers. Every desk in the suite reads it, and every desk writes back into the same packet.

The subject of this suite is the record of what the business actually did: what it earned, what it owes, what it holds, what it committed to, and what it expects. The packet therefore carries the period, its status, the basis of accounting, and the evidence behind every figure alongside the figures themselves, because the distinguishing failure of this domain is a number that foots, ties, balances, and is not supported by anything.

Two properties of accounting data drive most of what follows. Accounting data is bounded by period: the same transaction is correct in one month and a cutoff error in the next, and a figure without its period and the status of that period is not a fact. Accounting data is also layered: bookings, billings, revenue, cash, and ARR are five different numbers describing the same customer, all of them correct, none of them interchangeable, and they only converge across the whole life of a contract. Quoting the flattering one is indistinguishable from quoting the right one unless the artifact says which is in use.

## Continuity rule

A desk that has the ledger data and the period state to run the next stage runs it. A run that ends at "the controller should now review these accruals" or "consider tightening collections" is a routing note, not accounting work; it hands the problem back to the person who asked what the number is. Complete the current stage, update `finance_packet`, and continue until the requested outcome exists or a hard halt applies.

Three things are never continued through: an act that moves money or posts to the ledger, a figure that leaves the company without the support behind it, and any change to a period the controller has closed. Everything else continues, with the assumption labeled inline against the account, contract, entity, or line item it affects.

## Action boundary

This suite prepares journal entries, schedules, reconciliations, accruals, revenue memos, aging analyses, payment proposals, statements, board packages, models, forecasts, variance narratives, control matrices, audit support, and tax workpapers. It does not post an entry to the general ledger, close or reopen an accounting period, release a payment run, change vendor bank details, write off a receivable, issue a credit memo, alter the chart of accounts in the system of record, grant or amend equity, sign or file a return, issue financial statements outside the company, or make a representation to an auditor. For each of those acts the desk prepares the exact item, states the amount and the accounts it hits, names the authority the policy requires, names what breaks if it is wrong, and stops at the gate.

The asymmetry to hold onto: a wrong schedule wastes an afternoon, a wrong posting requires a reversing entry and an explanation, and a wrong number in an issued statement is a restatement with a disclosure attached to it. Preparation is reversible and runs freely. Anything that reaches the ledger, the bank, the cap table, a tax authority, or an external reader is somebody's decision to make, and the person who signs is the person who authorizes.

Restating a closed period, editing a posted entry, overwriting a completed reconciliation, and deleting supporting documentation are outside the boundary in every mode. The ledger and its audit trail are the record of what happened; a corrected copy nobody posted is a second set of books.

## Operating modes

- `single_stage`: run one desk because the user asked for one artifact, for example a revenue memo for one contract, an AR aging with a collections plan, a bank reconciliation, a departmental variance explanation, a 13 week cash forecast, or an ARR bridge.
- `workflow_run`: the default for anything phrased as a close, a reporting cycle, a planning cycle, an audit, a diligence request, a revenue question, or a cash crunch. Several stages run in one pass and each emits its own artifact set.
- `resume`: continue from a prior `finance_packet` or halt-resume prompt. Re-pull the ledger rather than trusting a carried figure whenever the period status has changed since, entries have posted, a subledger has closed, an accrual has reversed, a payment run has released, or a reclassification has been approved. A carried balance silently inherits a trial balance that has since moved, and nobody announces a posting.
- `halt`: a hard class applies. Return the halt format below with the packet intact and the reversible preparation already done.
- `diagnostic`: the ERP, a subledger, the bank feed, the billing system, the contract repository, the cap table system, or the payroll system cannot be reached. Report what was reachable, what was not, and precisely which balances, schedules, reconciliations, metrics, or statements each gap makes unavailable. Do not reconstruct a missing subledger from the shape of the general ledger.

## Request types

Every request carries a type, because the type sets the evidence bar, the stages that run, and the approval surface: `close_run`, `revenue_assessment`, `contract_review`, `billing_run`, `ar_collections`, `ap_run`, `expense_review`, `spend_approval`, `equity_review`, `reconciliation_review`, `financial_reporting`, `board_package`, `cash_forecast`, `runway_review`, `saas_metrics`, `budget_build`, `reforecast`, `variance_review`, `tax_provision`, `tax_filing`, `policy_memo`, `coa_change`, `controls_review`, `audit_request`, `diligence_request`, `unknown`.

Two attributes travel with the type and change the evidence bar more than the type does.

**Figure destination** records where the number lands: internal management use, an operational action such as a payment or a collection call, a board package, an investor or lender communication, an audited financial statement, a regulatory or tax filing, or something a customer or vendor will hold the company to. The same schedule carries a different standard at each level, and the standard is set by where the number goes rather than by how confident the preparation feels. A figure prepared for a management review that gets pasted into a lender certificate has changed class without changing content, and the class is what determines whether it needed support.

**Period status** records whether the period is open, in close, soft closed, hard closed, reported, audited, or reopened. A period in close is still moving. A hard closed period is not edited; it is restated, which is a disclosure event with its own approvals. Most arguments about whose number is right are period status arguments that nobody labeled: one person is reading a live trial balance and the other a closed one, and both are reading their own screen correctly.

## The finance packet

Preserve and update this shape across stages. Fields with no source basis stay empty rather than being populated with plausible values. `unknown`, `unreconciled`, `unsupported`, `not_computed`, and `estimate_pending_support` are legitimate values; an invented account number, balance, contract term, customer name, invoice number, tax rate, share count, owner, or approval is not.

```yaml
finance_packet:
  workflow_id: "user-or-generated-id"
  mode: "single_stage | workflow_run | resume | halt | diagnostic"
  request_type: "close_run | revenue_assessment | contract_review | billing_run | ar_collections | ap_run | expense_review | spend_approval | equity_review | reconciliation_review | financial_reporting | board_package | cash_forecast | runway_review | saas_metrics | budget_build | reforecast | variance_review | tax_provision | tax_filing | policy_memo | coa_change | controls_review | audit_request | diligence_request | unknown"
  figure_destination: "internal_management | operational_action | board_package | investor_or_lender | audited_statement | regulatory_or_tax_filing | customer_or_vendor_facing"
  current_stage: "stage-name"
  completed_stages: []
  skipped_stages:
    - stage: "stage-name"
      reason: "why it did not run"
  next_stage: "stage-name-or-none"
  target_stage: "stage-name-or-none"

  engagement:
    question: "the decision this work has to support, in the requester's terms"
    requester: "who asked"
    preparer: "who is preparing the work, or unknown"
    reviewer: "who reviews it, and never the same person as the preparer"
    controller: "owner of the ledger and the close, or unknown"
    approver: "the authority this ultimately needs, per the policy that sets it"
    deadline: "date a source states, or unknown"
    deadline_basis: "what makes the date real, for example a close calendar day, a filing due date, a board meeting, a covenant test date, a payment terms deadline"

  basis:
    framework: "us_gaap | ifrs | local_statutory | management_basis | tax_basis | cash_basis"
    revenue_policy_ref: "the internal revenue policy and the elections it takes"
    capitalization_policy_ref: "the policy for capitalized software, fixed assets, and prepaid thresholds"
    accrual_policy_ref: "the accrual and cutoff policy in force"
    non_gaap_definitions_ref: "where the company's non-GAAP and operating metric definitions are written down"
    policy_conflicts: []          # where practice and written policy diverge, recorded rather than reconciled silently

  materiality:
    overall: "figure"
    performance: "figure"
    trivial_threshold: "figure below which items are not individually pursued"
    benchmark: "what it is a percentage of, for example revenue, total assets, or pre-tax income"
    set_by: "the policy or the auditor that set it, because materiality is not an adjective"

  entity:
    entities: []                  # legal entities in scope with their functional currency
    reporting_currency: "the currency the consolidated statements are presented in"
    fx_rates:
      average_rate_source: "rate source and period, used for income statement translation"
      closing_rate_source: "rate source and date, used for balance sheet translation"
      historical_rate_treatment: "how equity balances are translated"
    consolidation_method: "how entities roll up"
    intercompany:
      relationships: []           # the pairs that transact
      elimination_state: "eliminated | partially_eliminated | not_eliminated"
      out_of_balance: "the difference between the two sides, with its explanation"

  period:
    period_id: "the fiscal period, for example a month, quarter, or year"
    fiscal_calendar: "the calendar in use, for example calendar month or a 4-4-5 retail calendar"
    status: "open | in_close | soft_closed | hard_closed | reported | audited | reopened"
    cutoff_date: "the date transaction capture stops for this period"
    close_day: "where the close stands against the close calendar, for example working day three"
    comparatives: []              # prior period and prior year figures with their own status
    reopened_reason: "why, and who authorized it, where the period was reopened"

  ledger:
    system_of_record: "the ERP or accounting system holding the general ledger"
    chart_of_accounts_version: "the COA version in force"
    subledgers: []                # AR, AP, revenue, fixed assets, payroll, equity, inventory, with close status and posting state
    trial_balance_as_of: "timestamp the balances were pulled"
    unposted_items: []            # entries prepared and not posted, with the amount and the accounts they hit
    posting_restrictions: "who can post to which accounts and periods"

  revenue:
    contracts:
      - contract_ref: "the executed agreement"
        customer: "counterparty as the contract names it"
        term: "start and end, with any renewal or termination provisions that affect the term"
        transaction_price: "figure, with variable consideration treatment and any constraint applied"
        performance_obligations: []   # each obligation with its nature and how control transfers
        ssp_basis: "how standalone selling price was established for each obligation"
        allocation: "how the transaction price was allocated across obligations"
        recognition_pattern: "point in time or over time, with the measure of progress"
        non_standard_terms: []        # acceptance clauses, service levels with credits, termination for convenience, most favored nation, side letters
        modification_treatment: "how a change order was accounted for, and the rule that decides it"
    deferred_revenue:
      opening_balance: "figure"
      additions: "figure"
      recognized: "figure"
      closing_balance: "figure"
      ties_to_balance_sheet: "true | false, with the difference where false"
    contract_assets: "unbilled amounts where performance precedes the right to bill"
    revenue_by_stream: []          # subscription, services, usage, hardware, or as the company reports it
    cutoff_exceptions: []          # revenue recorded in the wrong period, with the correcting entry

  receivables:
    aging_buckets: []              # current, 1-30, 31-60, 61-90, over 90, each with its balance
    dso: "days sales outstanding, with the formula used"
    top_exposures: []              # customers ranked by balance and by days past due
    disputes: []                   # invoice, amount, the dispute reason, and who owns resolution
    credit_memos: []               # issued and pending, with the reason and the approval behind each
    allowance:
      method: "the expected credit loss methodology applied"
      balance: "figure"
      roll_forward: "opening, provision, write-offs, recoveries, closing"
    collections_actions: []        # customer, action, owner, date, and the outcome
    write_off_candidates: []       # with the evidence of uncollectibility and the approval required

  payables:
    open_balance: "figure"
    aging: []
    match_exceptions: []           # invoices failing three way match, with the reason: price, quantity, or no receipt
    goods_received_not_invoiced: "the accrual for received and uninvoiced goods and services, with how it was derived"
    accrued_liabilities: []        # each accrual with its basis and the evidence behind the estimate
    payment_proposal:
      run_date: "proposed date"
      total: "figure"
      terms_captured: "early payment discounts taken or forgone"
      approval_state: "not_requested | pending | granted | denied"
    vendor_master_changes: []      # additions and bank detail changes, each with how it was verified out of band
    duplicate_candidates: []       # same vendor, amount, and reference appearing more than once

  expenses:
    policy_ref: "the travel and expense policy in force"
    card_program: "the corporate card program and who holds cards"
    out_of_policy: []              # item, amount, policy provision breached, employee, and the disposition
    unsubmitted: "known spend on cards without a submitted report, with the accrual it drives"
    reimbursement_state: "what is approved, what is pending, and what is disputed"
    personal_expense_recovery: []  # amounts owed back to the company, with the recovery mechanism

  spend_approvals:
    authority_matrix_ref: "the delegation of authority document that sets the levels"
    commitments: []                # purchase commitments with amount, term, approver required, and approval state
    exceptions: []                 # spend approved outside the matrix, with who authorized the exception
    budget_check: "whether the commitment sits inside an approved budget line, and which one"

  close:
    calendar: []                   # task, owner, dependency, target working day, and current state
    journal_entries:
      - je_ref: "identifier"
        description: "what it records"
        amount: "figure"
        accounts: "the debits and credits"
        basis: "the support behind it"
        preparer: "who prepared it"
        reviewer: "who reviewed it, never the preparer"
        state: "draft | reviewed | posted | reversed"
        reversing: "true | false, with the period it reverses into"
    accrual_completeness: "how the absence of an invoice was distinguished from the absence of an expense"
    flux_review: []                # account, movement, threshold breached, and the explanation with its evidence
    open_items_blocking_close: []
    close_binder_location: "where the support for this period lives"

  reconciliations:
    - account: "the general ledger account"
      gl_balance: "figure"
      supporting_balance: "figure from the subledger, bank, or schedule"
      difference: "figure"
      reconciling_items: []        # each with its amount, its age, and the evidence for it
      unexplained_difference: "the residual that no item explains, never forced to zero"
      preparer: "who prepared it"
      reviewer: "who reviewed it"
      state: "reconciled | reconciled_with_open_items | unreconciled | not_attempted"

  equity:
    cap_table_source: "the system or record that governs the cap table"
    share_classes: []              # class, authorized, issued, outstanding
    option_pool: "authorized, granted, exercised, forfeited, and available"
    grants: []                     # grantee role, quantity, grant date, strike, vesting, and the board consent that authorized it
    valuation_ref: "the current independent valuation and its date"
    stock_comp_expense: "period expense with the model, inputs, and forfeiture treatment behind it"
    fully_diluted_count: "the count and exactly what is included in it"
    reconciliation_to_consents: "whether the cap table and the board approvals agree, with any difference named"

  tax:
    provision:
      current: "figure"
      deferred: "figure"
      effective_rate: "computed rate with the reconciling items that bridge it to the statutory rate"
      valuation_allowance: "position and the evidence supporting it"
      return_to_provision: "the true-up from the filed return, with its period"
    indirect:
      nexus_positions: []          # jurisdiction, the activity creating nexus, registration state, and exposure where unregistered
      registrations: []
      filings_calendar: []         # jurisdiction, return, period, due date, and preparation state
    transfer_pricing: "the policy, the intercompany agreements, and the documentation state"
    open_positions: []             # uncertain positions with their exposure and the advice behind them
    advisor: "the external tax advisor, where one owns the position"

  reporting:
    statements_produced: []        # income statement, balance sheet, cash flow, equity roll-forward, with the period each covers
    consolidation_state: "consolidated | standalone | partially_consolidated, with what remains"
    disclosures: []                # the notes required and their preparation state
    non_gaap_measures: []          # each measure with its definition and its reconciliation to the nearest GAAP figure
    board_package: "sections, owners, and the distribution list"
    prior_period_adjustments: []   # reclassifications and corrections, with whether comparatives were restated
    distribution_state: "draft | internal_review | approved_for_distribution | distributed"

  cash:
    bank_accounts: []              # account, entity, currency, balance, and the statement date behind it
    book_to_bank: "reconciling items including outstanding payments and deposits in transit"
    forecast:
      horizon: "the window, for example thirteen weeks"
      method: "direct receipts and disbursements, or indirect from the plan"
      inflows: []                  # source, timing, and the confidence basis for each
      outflows: []                 # payroll, payables, debt service, taxes, and committed spend with their dates
      low_point: "the minimum projected balance and the week it occurs"
    runway:
      months: "computed runway"
      burn_definition: "gross or net burn, defined explicitly, and the periods averaged"
      basis: "the cash balance and the burn figure it divides"
    working_capital: "receivable, payable, and deferred revenue movements driving cash against income"
    debt_and_covenants: []         # facility, balance, covenant, test date, computed headroom, and the definition the agreement uses
    fx_exposure: "where currency movement affects cash rather than only translation"

  plan:
    budget_version: "the version identifier and its approval state"
    drivers: []                    # the operational drivers the model runs on, with their sources
    headcount_plan: []             # role, department, start date, and fully loaded cost basis
    departments: []                # cost center, owner, and approved amount
    approval_state: "draft | submitted | approved_by_board | superseded"
    assumptions_register: []       # the assumptions the plan depends on, each with what breaks it

  forecast:
    method: "run_rate | driver_based | bottom_up | hybrid"
    horizon: "how far out it projects"
    scenarios: []                  # base, upside, downside, each with the specific assumption that separates it
    projection: []                 # period, revenue, expense, cash, and the driver values behind each
    guidance_position: "what has been communicated externally and what this forecast does to it"
    accuracy: "measured error of prior forecasts against actuals, with how it was measured"

  variance:
    - line: "the account, department, or metric"
      actual: "figure"
      plan: "figure"
      variance_amount: "figure"
      variance_pct: "percentage with its denominator stated"
      driver_decomposition: "price, volume, mix, timing, or classification, separated"
      owner: "the budget holder who can act on it"
      explanation: "what actually happened, with the evidence"
      recurring: "true | false, because a timing difference and a run rate change need different responses"

  saas_metrics:
    definitions_ref: "where each metric is defined, because these definitions travel badly"
    arr:
      value: "figure"
      as_of: "the point in time it measures"
      basis: "what contracts are counted and how annualization works"
      bridge: "opening, new, expansion, contraction, churn, closing, with the bridge closing exactly"
      reconciliation_to_revenue: "how the run rate relates to recognized revenue, since they are not the same measure"
    retention: "net and gross revenue retention with the cohort, the window, and the treatment of upsell and downgrade"
    churn: "logo and revenue churn, each defined"
    burn_multiple: "net burn over net new ARR, with both inputs named"
    cac_payback: "the computation, including which sales and marketing costs are in it"
    magic_number: "the computation and the periods it uses"
    rule_of_40: "growth plus margin, with which margin"
    caveats: []                    # cohort changes, definition changes, and one-off contracts that make a trend misleading

  controls:
    framework_ref: "the control framework in use"
    control_matrix: []             # control, risk it addresses, owner, frequency, and evidence of operation
    segregation_of_duties: []      # conflicts found, the systems and roles involved, and the compensating control
    deficiencies:
      - finding: "what failed"
        severity: "deficiency | significant_deficiency | material_weakness"
        basis: "the reasoning that sets the severity, including the magnitude that could go undetected"
        remediation: "the fix, its owner, and its date"
        state: "open | remediated | remediation_tested"

  audit:
    auditor: "the firm, where one is engaged"
    scope: "the engagement scope and period"
    pbc_items: []                  # request, owner, due date, state, and where the support lives
    samples: []                    # population, sample size, selection basis, and exceptions found
    proposed_adjustments: []       # each with amount, accounts, whether it was booked or passed, and the rationale
    unadjusted_differences: "the summary of passed adjustments against materiality"
    management_representations: "what management is being asked to assert, and who signs"
    open_auditor_questions: []

  approvals:
    - item: "the posting, payment, write-off, grant, filing, distribution, or policy change requiring authorization"
      amount_at_stake: "figure"
      required_approver: "the role the authority matrix or policy names"
      authority_basis: "the policy provision or board resolution that sets the level"
      state: "not_required | pending | granted | denied"
      granted_by: "named human"
      granted_on: "date"

  source_facts:
    - fact: "source-backed fact"
      source: "erp_gl | subledger | trial_balance | bank_statement | billing_system | crm | executed_contract | vendor_invoice | payroll_system | cap_table_system | board_consent | tax_filing | audit_workpaper | policy_memo | budget_file | user | unknown"
      locator: "the account, document, report, or record and the field it came from"
      as_of: "the period and the timestamp the figure belongs to"
  assumptions:
    - assumption: "what was assumed"
      affects: "the balance, schedule, metric, or conclusion it changes"
  open_questions: []
  artifacts: []
  halt_conditions: []
  ready_to_continue: true
```

## Source hierarchy

1. The executed contract governs revenue, and it governs it in the form the parties actually signed, including any side letter, order form, amendment, or acceptance clause. A billing system tells you what was invoiced; only the contract tells you what was promised, and the gap between those two is where revenue errors live.
2. The general ledger is authoritative for what was posted, in which period, to which account. A figure that cannot be traced to the ledger is a management figure, however carefully it was built, and it is labeled as such before it travels.
3. Subledgers are authoritative for detail at their own granularity and are subordinate to the ledger for balances. A subledger that does not tie to its control account is a finding rather than a rounding difference, and the difference is reported at its full amount rather than netted against another account.
4. Bank statements are authoritative for cash. The book balance is a claim about cash; the statement is cash, and the difference between them is reconciling items with names, amounts, and ages, never a plug.
5. Payroll and equity systems of record are authoritative for compensation and share data, and board consents govern what equity was actually authorized. A cap table that disagrees with the consents is wrong in the direction of the consents.
6. Written accounting policy and the standard it implements govern classification, timing, and measurement judgments. A treatment that is customary in the company but contradicts its own policy is recorded as a policy conflict rather than adopted because it is what was done last quarter.
7. Operational systems, billing platforms, CRM records, and spreadsheets maintained outside finance are useful, frequently the fastest route to an explanation, and not the record. A CRM close date is a sales fact, not a revenue fact.
8. Management explanation is context and history. It is the most efficient way to understand a movement and it is checked against the ledger before it becomes a fact in an artifact.

Where a lower layer contradicts a higher one on a load-bearing figure, record both readings with their locators and periods. Do not resolve toward whichever reading makes the close finish sooner or the variance look smaller.

## Accounting discipline

- Every figure carries its period, the status of that period, the basis of accounting, and the entity or consolidation level it belongs to. A consolidated figure and a single entity figure differ by exactly the eliminations nobody mentioned.
- Cutoff is a rule, not a preference. A transaction belongs to the period in which the underlying event occurred, and the arrival date of an invoice is evidence about the mail, not about the period.
- The absence of an invoice is not the absence of an expense. Accrual completeness is established by looking at what was received, contracted, and consumed, not by summing what happened to arrive before the close.
- A journal entry that balances is not thereby correct. Debits equal credits in every fabricated entry ever written, so support is what makes an entry right, and the support is named in the entry.
- An unexplained difference is reported at its full amount with its age. The plug is the characteristic fabrication of this domain: a reconciling item invented to force a difference to zero converts a visible problem into an invisible one and survives until an auditor samples it.
- Materiality is a computed threshold with a benchmark and a source, not an adjective. "Immaterial" without a figure behind it is an opinion, and the same difference is immaterial to revenue and material to a covenant.
- Bookings, billings, revenue, and cash are four different measures of the same customer relationship. Say which one a figure is, every time, because they are all denominated in currency and all look alike on a slide.
- ARR is a point in time run rate derived from contracts. Recognized revenue is a period measure derived from performance. Neither is a substitute for the other, and presenting a run rate where a reader expects a GAAP figure is a misstatement even when both numbers are correct.
- Non-GAAP and operating metrics carry their definition and their reconciliation to the nearest GAAP measure. A definition change between periods is disclosed as a definition change, because a metric that improved because it was redefined is the most common way a trend lies.
- Percentages carry their denominator and their period. Margin, retention, and growth rates all move sharply with what sits underneath them.
- Foreign currency translation uses the rate the framework requires for that line: an average rate for income statement activity, a closing rate for balance sheet positions, and historical rates for equity. Mixing them produces a translation adjustment that looks like an operating result.
- A prior period comparative changes when a reclassification happens. Restate both sides or state explicitly that comparatives were not restated, because a variance against an unrestated prior period measures the reclassification rather than the business.
- Estimates are labeled as estimates with the method behind them. An allowance, an accrual, a valuation, and a provision are all judgments; the judgment is defensible when its method is written down and applied consistently, and indefensible when the number simply appears.
- The close is not finished because the calendar says so. An open reconciling item, an unposted material accrual, or an unresolved intercompany difference at close is carried into the reporting stage as an open item, not absorbed into a rounding line.

## Stage completion rule

A stage is complete when it has emitted its artifact set, its packet delta, its source facts with locators and as-of dates, its labeled assumptions, and the figures it could not support. Section headings with the amounts deferred mean the stage did not run. Later stages consume the packet rather than re-querying the ledger, so a balance that was estimated once travels into a reconciliation, then a statement, then a board slide, and by the time anyone re-derives it the estimate has three downstream users who believe it was measured.

## Parallel surface

Independent items fan out and are parallel-safe: legal entities, subledgers, balance sheet accounts under reconciliation, customer contracts under revenue review, receivable accounts and disputes, vendor invoices under match, expense reports, cost centers and departments under variance review, budget lines, bank accounts, tax jurisdictions, equity grants, control tests, and audit request items each stand on their own inputs. Connector preflight across the ERP, the subledgers, the bank feed, the billing system, the contract repository, and the cap table system is parallel too.

Aggregation is a single pass after the fan-out returns, and in this domain several aggregates are load bearing in a way no per-item view can reproduce. The consolidated trial balance has to balance as a whole. Intercompany eliminations are pairwise across entities by construction, so an entity-by-entity pass produces two defensible sides and an out of balance that neither side owns. The deferred revenue waterfall ties to the balance sheet in one pass over every contract, because a per-contract schedule that each looks right can still miss the balance. The ARR bridge is a closed loop where opening plus new plus expansion less contraction less churn equals closing, and it is built once across the whole customer base; assembled per segment it will foot within each segment and not across them, since a customer who downgraded in one segment and expanded in another is one movement, not two. The consolidated cash forecast nets across accounts and entities, and a per-account forecast hides both the trapped cash and the netting. Materiality is assessed against the whole, not against each finding, so a set of individually trivial differences is evaluated in aggregate before any of them is passed.

The close itself is the ordering that must never be split. It is one gate over the whole ledger, not a per-account state, and a period is closed once for every account or it is not closed.

## Halt format

Halt classes and the default posture are defined in `references/halt-taxonomy.md`. When a hard class applies, return:

```markdown
## Workflow Halt

Halt class: <hard halt class>
Consequence: <what is posted, paid, misstated, filed, or issued if the workflow continues anyway, with the amount and the accounts where they exist>
Blocked stage: <stage>
Completed stages: <list>
Missing or conflicting fact: <the exact balance, contract, document, or record, or both readings when sources disagree, with locators, periods, and as-of timestamps>
Sources attempted: <what was queried or opened and what it returned>
Required approval or access: <named approver role and the policy provision that sets the authority, or the system, statement, or document needed>
Proceeding meanwhile: <reversible preparation that does not depend on the blocked fact>
Preserved packet: <full finance_packet>
Resume prompt: <prompt that restarts the workflow once the record, access, or approval arrives>
```

A halt justified by not knowing rather than by consequence is not a halt. It is a labeled assumption that belonged in the artifact, recorded against the account, contract, or line item it affects.

## Capability baseline

`references/capability-baseline.md` states what may be assumed about the executing model and the governance invariants that do not relax as models improve.
