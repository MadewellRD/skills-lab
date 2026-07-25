---
name: churn-risk-desk
description: build and maintain the account churn risk register with the evidence and date behind each risk, the churn reason category, the arr exposed with its basis, root cause separated from the symptom that surfaced it, the earliest signal available in the record, and closure by observed change rather than by a reassuring call. use for risk review, red account identification, at-risk book reporting, sponsor loss, downgrade and consolidation risk, churn postmortem, and what was knowable and when.
---

# Churn Risk Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the risk artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the risk, the account, or the exposure figure it affects, and record it in `open_questions`. Never invent a risk, the evidence that raised it, the date it was first detected, an ARR exposure, a churn reason, or a competitor's involvement.

## Role

This desk owns the register, and the register is the account's memory. A risk here is written as what the customer will do, not as how the account team feels about it. "Engagement has been light" is a mood; "the operations director who owned the reconciliation workflow was reassigned in the March restructure, her replacement has twice asked what the platform costs per year, and the workflow itself has moved into their new finance system" is a risk with a subject, a verb, and a date. The first is unactionable and unfalsifiable. The second names who, what, and when, and it can be closed by an observation.

Every entry carries the evidence that raised it with its source and its collection date, a category from the churn reason taxonomy so risks aggregate across the book rather than existing only as prose on one account, the ARR exposed with the basis for that number, and severity and confidence stated as two separate fields. Severity and confidence are separated because a certain small risk and an uncertain large one need different responses, and collapsing them into a single heat colour is how the save capacity gets spent on the account that shouts loudest rather than the one that is leaving.

The desk owns the distinction between root cause and symptom, which is most of its value. A decline in weekly active users is a symptom; the cause is a reorganization, a competing tool that arrived with a new CIO, an integration that broke in a release nobody flagged, an administrator who left with the configuration knowledge, or a workflow that never fit the way the team actually works. A save play aimed at a symptom is a training session for a team that has already moved on.

It also owns the archaeology: the earliest point in the available record where this risk was visible and the date that evidence became available. That single field is what a churn postmortem is actually about, and it is the field that makes a health model improvable rather than merely reportable. Closure belongs here too, and closure is an observed change: usage recovered against a stated definition, the sponsor replaced and engaged, the escalation confirmed resolved by the customer, the budget line restored in their own planning cycle. A reassuring conversation is evidence about a conversation.

## Use when

- An account looks wrong and the concern needs to be named, categorized, sized, and given an owner rather than raised in a pipeline meeting.
- A health score has moved, or a score has stayed green while the underlying evidence has not.
- A sponsor has left, changed role, gone dormant, or been replaced by someone with no history with the product.
- A book-level at-risk view is needed for a forum that will allocate save capacity across accounts.
- An account has already churned and the question is which signal was available, when, and why it did not reach anyone.
- Consolidation, acquisition, budget scrutiny, or a competitive evaluation has surfaced and its consequence for the renewal has to be stated.

## Do not use when

- The recovery plan, the concession, and the approvals are the subject. That is `save-play-desk`, which consumes this register.
- The customer has raised something loudly and a committed clock is already running. That is `escalation-management-desk`; an escalation may become a risk here, but the update cadence belongs there.
- The score model, its components, weights, or calibration are the subject. That is `health-scoring-desk`, whose output is an input here.
- The question is what the product is actually being used for. That is `usage-analysis-desk`, and its instrumentation coverage statement bounds every risk claim built on telemetry.
- The renewal timeline, forecast category, and close plan are the subject. That is `renewal-preparation-desk`, which reads the open risks from here.

## Required evidence

- Health score output with its model version, component breakdown, and the age of each input.
- The usage read with its definition of active, its window, and its instrumentation coverage statement.
- The stakeholder map with coverage state, sponsor changes, departures, dormancy, and single-threaded exposure.
- Open and recently closed escalations, plus support ticket volume, themes, reopen rate, and sentiment history.
- The success plan with attainment against each desired outcome, and the commitment register with anything still outstanding.
- Competitive, consolidation, and merger or acquisition signals, with the source and date of each.
- Budget and cost scrutiny signals: procurement engagement out of cycle, invoice disputes, late payment, a request to reduce seats, a request for a usage breakdown.
- Contract facts including term end, notice deadline, termination rights, and co-term relationships that change what is actually exposed.
- The churn reason taxonomy in force and prior losses in this segment with their reasons and their first signals.

## Workflow

**Outcome.** A risk register for the account or the book in which every entry states what the customer will do, carries dated evidence with its source, sits in a taxonomy category, names the ARR exposed with its basis, separates severity from confidence, distinguishes root cause from symptom, records the earliest available signal and its date, has a named owner and a current state, and defines what observation would close it. In postmortem posture, the same register produces the signal timeline and the honest preventability assessment.

**Grounding.** Risks come from evidence, and the evidence carries its source layer. Telemetry outranks a CRM field, and a named customer statement outranks the account team's reading of the room. The most productive place to look is the distance between what the internal narrative says and what the systems show: the account scored green with one active user in six weeks, the strong champion whose last login was two quarters ago, the renewal at commit with no meeting since kickoff, the platform bought for four thousand seats and provisioned for four hundred. Where the sources genuinely disagree, both readings stay on the risk rather than being resolved toward the one that keeps the forecast where it is.

**Constraints.** ARR exposed is the amount actually at stake, computed and shown: a single module at risk is that module's value, not the contract; a co-termed set of subsidiaries is the co-termed total; a multi-year deal with a termination-for-convenience right is exposed at the right the customer holds rather than at the remaining term. First-detected is the date the evidence became available, not the date somebody wrote the risk down, and the gap between those two dates is itself a finding worth recording. A risk with no closure evidence defined is not a register entry; it is a note. Risks are categorized from the taxonomy in force so that nine accounts hitting the same product gap aggregate into one theme rather than nine narratives. Where an account has already churned, nothing in the register is edited backward to look foreseen; the record is what the next postmortem and the next renewal are read against, and a repaired record teaches the team nothing.

**Parallel surface.** Independent items fan out safely: accounts in a book being assessed, individual risks being evidenced and sized, individual signal sources being read for one account, and prior churn records being mined for their first signals. The aggregate is a single pass after the fan-out returns, because the at-risk view, the risk-weighted exposure across the book, the ranking against the save capacity that actually exists, and the pattern across accounts sharing a root cause are statements about the whole set. Within one account, the root cause judgment is also a single pass, since several symptoms frequently resolve to one cause and calling them separate risks doubles the apparent exposure.

**Acceptance bar.** Every risk states a customer action, carries dated evidence with its source, has a taxonomy category, an ARR exposure with the arithmetic behind it, separate severity and confidence, a named owner, and a defined closure observation. Root cause is distinguished from the symptom that surfaced it, or the cause is explicitly recorded as not yet established. Every risk carries the earliest date its evidence was available. No risk is closed on a conversation. A green account with thin evidence appears in the register as exactly that.

## Outputs

A complete run delivers this set:

- `risk-register.md`: every open risk with `risk_id`, the customer action it predicts, evidence with source and date, category, ARR exposed with its basis, severity and confidence stated separately, root cause against symptom, owner, state, and the observation that would close it.
- `root-cause-analysis.md`: per risk, the causal chain from the observable signal back to what changed in the customer's world, with the symptoms that would resolve if the cause were addressed and the ones that would not.
- `exposure-summary.md`: ARR at risk aggregated by category, by severity band, and by renewal date proximity, with the arithmetic shown and the accounts named rather than counted.
- `signal-timeline.md`: for each risk, the earliest point the evidence was available, when it entered the record, who could have seen it, and the lag between availability and detection.
- `risk-closure-log.md`: risks closed in the period, each with the observed change that closed it, kept separate from risks closed as realized so the register does not flatter itself.
- `churn-postmortem.md`, produced when the account is already lost: the customer's stated reason in their words, the taxonomy reason, ARR lost, the first available signal with its date, and the honest preventability assessment naming what would have had to change and who would have had to do it.
- `churn-risk-downstream-handoff.md`: what `save-play-desk` and `renewal-preparation-desk` inherit, with root causes, exposures, and unresolved evidence conflicts carried rather than summarized away.

Depth standard: an artifact is complete when a leader could allocate a person and a budget against it without a follow-up round trip, and a CSM could open the account tomorrow and know what to test. A risk without an exposure figure, a category without a closure observation, or a root cause stated as "low engagement" is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when telemetry, the support history, or the contract cannot be reached, the run delivers `risk-connector-diagnostic.md` naming each unreachable source and stating exactly which risks cannot be sized, which cannot be evidenced, and which categories cannot be assessed at all. Risk positions are not assembled from what an account of this profile usually looks like.

Anti-fabrication guard: the characteristic failure of this desk is the register written after the news. A risk entered on the Monday after the customer gives notice, dated that Monday, categorized confidently and described in perfect detail, is not a risk signal; it is a transcription of an event, and a register full of those produces a health model that appears to work and predicts nothing. So `first_detected` is the date the underlying evidence existed in a readable source, quoted with that source, and where the evidence is real but the detection was late, both dates are written and the lag is stated. The second failure is exposure inflation: writing the full contract value against a risk that touches one module makes the register look serious and makes the risk-weighted forecast meaningless, so every exposure shows its arithmetic and its scope. The third is causal storytelling, which is the easiest text in this suite to produce fluently: a plausible chain from a reorganization to a decline can be written for any account, and it is a hypothesis until a source supports each link. An unestablished cause is recorded as not established, with the specific evidence that would settle it, because a save play aimed at an invented cause consumes the one intervention the account was going to get. Risks that no source supports are not written to fill a thin register, and an account with two verified risks and a stated evidence gap is a better register than one with eight risks assembled from what usually goes wrong.

## success_packet fields to update

- `risks[]` in full: `risk_id`, `category`, `description` stated as customer action, `evidence` with source and date, `severity`, `arr_exposed` with its basis, `first_detected`, `owner`, `mitigation`, `state`, and `closure_evidence`
- `account.lifecycle_stage` moved to `at_risk` where the evidence supports it, or left with the reason it was not moved
- `renewal.open_risks` seeded with the `risk_id` references still open at the renewal, and `renewal.forecast_category` flagged for reassessment where the evidence contradicts the current category rather than changed here
- `renewal.churn_record` in postmortem posture with `reason_primary`, `reason_taxonomy`, `arr_lost`, `preventable`, and `first_signal` with the date it was available
- `assumptions[]` for every inferred cause, with the risk it affects
- `source_facts` with collection dates, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: a risk position or churn forecast would go to a governing forum on evidence that cannot carry it, in either direction. Understating removes the account from the attention that could still save it; overstating consumes the save capacity another account needed. Both are read as facts by the people allocating people and money.
- **Source conflict**: telemetry, the support record, the CRM, and the customer's own statement genuinely disagree on whether something is going wrong or on what is causing it, and adopting the comfortable reading produces a save aimed at a problem nobody has.
- **Security or privacy**: sizing or evidencing a risk would carry customer personal data, a named employee's internal standing, or another customer's confidential situation into an artifact that travels wider than the source did.
- **Missing approval**: changing an account's forecast category of record, raising an account into an executive risk forum, or recording a competitive displacement against a named competitor is a position the company takes, and it belongs to the owner of that record.
- **Production or destructive**: the next action would write risk entries, health overrides, or at-risk flags into the CRM or success platform as the record.
- **Connector unreachable**: telemetry, the support system, or the contract exists and cannot be read, so a risk would be sized against a number nobody observed.

An untested disposition, an unquantified competitive rumour, an unknown budget cycle, and a cause that has not yet been established are soft gaps. Record the gap, label the assumption against the risk it affects, and continue.

## Downstream handoffs

`save-play-desk` is next and needs the root cause rather than the symptom, the ARR exposed with its basis, the stakeholders who can still be reached, and the closure observation that would prove the play worked. `renewal-preparation-desk` needs every risk still open at the renewal with its exposure, because those are what the forecast category has to be defensible against. `health-scoring-desk` needs the false-negative cases, the accounts that were green while the evidence was not, since those are the only real calibration input a scoring model gets. `value-realization-desk` needs risks categorized as value not realized, because an unrealized outcome is a measurement question before it is a relationship question. `voice-of-customer-desk` needs product gap and service delivery causes with the accounts and ARR behind each, so nine instances of one gap arrive at the product function as one theme. `retention-portfolio-reporting-desk` needs the exposure aggregates and the churn records with their first signals.

## Quality bar

Good risk work is specific enough to be wrong. Each entry names a person, a date, and an action the customer is expected to take, so that in six weeks someone can say it happened or it did not. The register is comfortable being short and comfortable being uncomfortable: it contains the risk the account team does not want to write down, and it contains "cause not established, here is what would settle it" rather than a tidy narrative. Exposure figures show their arithmetic and their scope, so a leader reading the aggregate is reading money rather than anxiety. The signal timeline is honest about lag, because the lag is the only thing this desk can actually improve. And closure is earned: a risk moves to closed when the usage came back, the sponsor was replaced and engaged, or the customer confirmed the impact ended, never when the call went well.
