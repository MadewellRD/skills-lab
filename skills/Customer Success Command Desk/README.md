# Customer Success Command Desk

Source Markdown suite for post-sale customer success. One orchestrator routes and runs; nineteen member desks own a real stage of the work.

The subject of this suite is a paying relationship over time: what the customer bought, what they were told it would do for them, whether the people who signed are still there, what the product is actually being used for, what that is worth in their numbers rather than ours, what is quietly going wrong, and whether they will pay again.

The suite covers the function end to end: post-sale handoff intake, segmentation and coverage models, stakeholder mapping, success planning with baselines, onboarding and time to value, usage analysis, adoption and enablement, health scoring, playbook design, escalation management, churn risk, save plays, value realization, QBR and executive business review, expansion whitespace, advocacy and references, renewal preparation, voice of customer, and retention and portfolio reporting.

Commercial negotiation and proposal construction belong to the Sales suite; this suite qualifies the signal and prepares the position. Ticket handling and incident mechanics belong to the Support suite; this suite keeps the relationship consequence and the escalation commitment. Contract interpretation, notice periods, and reference terms belong to the Legal suite. Product defect and roadmap decisions belong to the Product suite, which this suite feeds with themes carrying the accounts and ARR behind them.

## Desks in workflow order

- `customer-success-command-desk.md` (orchestrator)
- `post-sale-handoff-desk.md`
- `segmentation-coverage-desk.md`
- `stakeholder-mapping-desk.md`
- `success-planning-desk.md`
- `onboarding-time-to-value-desk.md`
- `usage-analysis-desk.md`
- `adoption-enablement-desk.md`
- `health-scoring-desk.md`
- `playbook-design-desk.md`
- `escalation-management-desk.md`
- `churn-risk-desk.md`
- `save-play-desk.md`
- `value-realization-desk.md`
- `qbr-ebr-desk.md`
- `expansion-whitespace-desk.md`
- `advocacy-reference-desk.md`
- `renewal-preparation-desk.md`
- `voice-of-customer-desk.md`
- `retention-portfolio-reporting-desk.md`

## How to start

Start at `customer-success-command-desk` and describe the outcome rather than the stage. Name the account or the book, say what decision is waiting on the answer, and say whether a clock is running such as a notice deadline, a review date, or an update you promised a customer. The orchestrator classifies the engagement, enters at the earliest desk whose inputs are satisfied, and runs the stages the outcome needs instead of returning a routing note.

Enter a member desk directly when the stage is already settled: a stakeholder map before a business review, a health score breakdown when the number looks wrong, an onboarding plan for a new logo, a save play for a named risk, or a renewal brief ninety days out.

Examples: "this account renews in March, tell me what the notice deadline actually is and what has to happen before it", "adoption is flat six months in, work out whether that is enablement, configuration, or a product gap", "build the value story for the executive review and tell me which figures the customer has actually validated", "the customer escalated on Friday, set up the plan and the update cadence", "which accounts in this book are green on the score and thin on the evidence", "code last quarter's survey verbatims into themes with the accounts and ARR behind each".

This suite plans, analyzes, scores, and drafts. It does not send customer-facing messages, deliver a business review, offer a discount or credit, sign or amend a contract, publish a logo or case study, provision entitlements, or write to the CRM; it prepares the exact item with the approval it needs and stops at the gate.

## Suite contracts

- `references/suite-workflow-contract.md` defines the `success_packet`, the operating modes, engagement types, the source hierarchy, evidence discipline, the action boundary, the five mandated sequences, and the halt format.
- `references/stage-contracts.md` gives each desk's required inputs, owned outputs, handoff target, and stage-specific hard halt.

Shared halt classes and capability assumptions come from the kernel references, `halt-taxonomy.md` and `capability-baseline.md`.

Most engagements run a subsequence of the chain. A new logo enters at post-sale handoff, an unhappy customer enters at escalation management on a clock the customer started, a renewal enters at renewal preparation and pushes backward into value and risk, and a lost account enters at churn risk in postmortem posture. The chain orders stages that consume each other's packet state; accounts, stakeholders, products, risks, escalations, plays, and open renewals fan out in parallel within a stage, while revenue retention over a cohort, health distribution, capacity math, the risk-weighted forecast, and the business review narrative itself are single passes over the whole set.
