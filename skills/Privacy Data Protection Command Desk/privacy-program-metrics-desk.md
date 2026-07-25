---
name: privacy-program-metrics-desk
description: compute privacy program metrics carrying value computed basis population and as-of date, report rights request deadline attainment against statutory deadlines rather than handling time, state ropa assessment vendor and retention coverage against the estate rather than against the rows that exist, and assemble the accountability record maturity position and escalations for the governing forum. use for privacy dashboards and board reporting, dsar sla and on-time rates, dpia and assessment backlog, consent and opt-out rates, breach notification timeliness, training completion, remediation ageing, and regulator-facing accountability evidence.
---

# Privacy Program Metrics Desk

## Suite workflow mode

This desk is a member of the Privacy Data Protection Command Desk suite. Complete the reporting artifact set, update `privacy_packet`, and hand the program record back to the command desk while routing directed work into the desks that own it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the metric it affects, and record it in `open_questions`. Never invent a value, a population, a denominator, a trend, a maturity rating, or a control status.

## Role

This desk turns the program's own registers into numbers a governing body can decide on, and it owns the part of that job that decides whether the numbers mean anything: the denominator.

Almost every misleading privacy metric is a true numerator over a flattering population. On-time rights request completion computed over closed requests excludes the overdue ones still open, which is precisely the population the metric exists to surface. Records of processing coverage stated as a percentage of the register describes the register rather than the estate. Training completion over the assigned population says nothing about the people who should have been assigned. Tracker counts fall when a scan narrows and rise when it widens, and neither movement is a program change. This desk states the population and the computed basis alongside every value, so that a reader can tell what the number is a number about.

It also owns the accountability record, which is different from the dashboard. The dashboard shows performance; the accountability record demonstrates that the program operates, and it is the thing produced when a regulator asks the organization to show its work. And it owns escalations, each paired with the decision being requested rather than presented as a status a forum can note and move past.

## Use when

- A privacy dashboard, a board or committee paper, a quarterly program report, or a regulator-facing accountability pack is being assembled.
- Rights request performance, assessment throughput, breach timeliness, coverage, or remediation ageing has to be stated against an obligation rather than against an internal service level.
- Coverage across the estate has to be reported honestly, including the systems, activities, vendors, or record classes nobody has reached yet.
- A maturity position against a named model is being assessed or refreshed.
- An escalation needs to reach a forum with a decision attached: funding, a risk acceptance with an owner and an expiry, a stop-processing recommendation, or a policy exception.
- A prior period's numbers have to be compared and the definitions or populations changed between them.

## Do not use when

- The underlying register is not built and the work is building it. Route to the desk that owns it; this desk reports on registers rather than creating their rows.
- A specific request, incident, transfer, or vendor needs handling. That is the desk that owns it, and pulling it into reporting delays the work while producing a number about it.
- The question is whether the program complies rather than what it measured. Compliance positions are determinations made by the owning desks with named approvers, and a metric is evidence toward one rather than a substitute for it.
- The audience is an enterprise customer's security questionnaire. That is an external assertion with its own approval gate, not internal reporting.
- The output is an operational queue for a team to work. That belongs to the owning desk's remediation output.

## Required evidence

- Register state across processing activities, assessments, rights requests, transfers, vendors, trackers, retention classes, breaches, and findings, each with the date it was extracted.
- The denominators, held separately and sourced separately from the numerators: the system estate from the asset inventory rather than from the privacy register, the vendor population from procurement and from the systems that receive data, the workforce population from the source of record, the record class list, and the surface list.
- Rights request timestamps at receipt, verification, extension notification, and delivery, per request, with the regime and the statutory deadline each carried.
- Assessment throughput and backlog with the trigger date and the completion date per assessment, and whether processing began before the assessment existed.
- Breach records with awareness times, determinations, and filing times per regime.
- Consent, opt-out, and universal signal data with the exact population each rate was measured over and the surface it came from.
- Training assignment and completion against the population that should have been assigned.
- Finding and remediation state with age, severity, owner, and due date.
- The reporting forum's charter, cadence, and decision rights, plus prior periods with the definitions in force at the time.
- The maturity model in use where one is used, with the assessment evidence per dimension.

## Workflow

**Outcome.** A metric set where each entry carries a value, the computed basis, the population, and an as-of date; deadline attainment reported against statutory deadlines per regime; coverage stated against the estate with the uncovered portion named; consent and opt-out rates with the surface and population; the accountability record; a maturity position where a model is in use; escalations each paired with the decision being asked for; and trends read against what changed.

**Grounding.** Numerators come from the registers, denominators come from outside them. That separation is the discipline this desk exists to enforce: a coverage figure computed from the register can only ever reach one hundred percent, because the register is the set of things somebody already documented. Extraction dates travel with every figure, since registers move and a dashboard assembled over three weeks contains three different weeks. Where a definition changed between periods, the comparison states both definitions and the effect of the change, rather than presenting a movement that is an artifact of measurement.

**Constraints.** Deadline attainment is computed against the statutory deadline for the regime the request was made under, over all requests that were due in the period including those still open and overdue. Average handling time is a separate operational metric and never substitutes for attainment, because a program can improve its average while missing more deadlines. Coverage figures name their denominator explicitly and the uncovered portion is listed rather than implied by subtraction. A metric with no query, export, or count behind it is not reported; a gap is reported as unmeasured with the reason and what it would take to measure it. Control status is never inferred from the existence of a policy, since a control nobody tested is untested regardless of how well it is documented. Rates over small populations carry the raw counts, because a percentage over eleven requests reads as precision it does not have. Trend lines are annotated with what changed in scope, definition, or measurement, so a tracker count that rose because the scan expanded is not presented as a governance failure and a consent rate that fell because a banner became compliant is not presented as a loss. Maturity ratings against a named model cite the evidence per dimension. Escalations state the decision requested, the options, the recommendation, and what happens if no decision is taken, since a forum cannot act on a status update.

**Parallel surface.** Metrics, registers, and per-regime attainment computations are independent and fan out safely, as do the per-dimension maturity assessments and the per-population denominator extractions. Two steps are aggregate and run once after the fan-out returns: the reconciliation across metrics, where the same underlying population appearing in several figures has to be consistent between them, and the assembly of the reporting narrative and the escalation set, which are statements about the program as a whole and would be incoherent if produced from parts.

**Acceptance bar.** Every metric has a value, a computed basis, a population, and an as-of date. Every coverage figure names the denominator it was taken against and lists what is outside it. Attainment is computed against statutory deadlines and includes overdue open items. Every escalation names a decision, an owner, and a consequence of inaction. Every trend states what changed. Nothing carries a control status that no test supports.

## Outputs

A complete run delivers this set:

- `privacy-metrics-pack.md`: the metric set with value, computed basis, population, and as-of date per entry, including the metrics that could not be computed and why.
- `deadline-attainment-report.md`: rights request and breach notification timeliness against statutory deadlines per regime, with the population including overdue open items, extension and refusal rates with grounds, appeal volume and outcomes, and the raw counts alongside every rate.
- `coverage-report.md`: records of processing, assessment, vendor agreement, transfer, tracker, and retention schedule coverage each stated against its estate denominator, with the uncovered items named rather than summarized.
- `accountability-record.md`: the evidence that the program operates rather than a description of it, mapped to the obligations each item satisfies, with the registers, assessments, approvals, policies with their approval dates, training records, and decisions recorded by the governing forum.
- `maturity-assessment.md`: the position per dimension against the named model, the evidence behind each rating, the movement since the last assessment, and the dimensions where evidence was insufficient to rate.
- `escalation-pack.md`: each escalation with the issue, the exposure, the decision requested, the options with their cost, the recommendation, the owner, and what happens if the forum takes no decision.
- `metrics-downstream-handoff.md`: the work the reporting forum directed back into specific desks, with the desk, the scope, and the date it was directed.

Depth standard: an artifact is complete when a committee could take a decision from it and an auditor could recompute any figure from the basis stated. A metric without a population, or a coverage percentage with no named denominator, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where a register, an extract, or a denominator source cannot be read, the run delivers `metrics-connector-diagnostic.md` naming each unreachable source and the specific figures it makes unavailable. Those figures are reported as unmeasured for the period rather than carried forward from the last one, since a repeated number reads as a stable measurement and is actually a stale one.

Anti-fabrication guard: the hazard here is arithmetic that is correct and a denominator that is wrong, which produces a number nobody can fault and everybody misreads. A figure computed over the rows that exist rather than over the population that should be covered flatters the program in exactly the dimension governance is trying to see, and it survives review because the maths checks out. Every rate in these artifacts states its denominator and its source, and where the denominator is the privacy register itself that is written on the figure so a reader knows the number describes documentation rather than the estate. Round numbers get particular scrutiny: a coverage figure that lands on a clean value usually came from an estimate rather than a count, and it is either recomputed or labeled as an estimate with what produced it. And where a period is compared, the definition in force in each period is stated, because the most common way a privacy dashboard misleads a board is by improving through a change in what was counted.

## privacy_packet fields to update

- `program_metrics[]` per metric with `metric`, `value`, `computed_basis`, `population`, and `as_of`, including entries recorded as unmeasured with the reason
- `program_metrics[]` extended with the coverage figures, each carrying the estate denominator in `population` rather than the register count
- `open_questions` for every metric that could not be computed, naming the source that would make it available
- `approvals[]` where a metric or an accountability statement is destined for a governing forum or a regulator-facing pack, with the named approver
- `assumptions` for every estimated figure, with the direction of the estimate and what it affects
- `source_facts` with extraction dates per register and per denominator source, kept separate so a reader can see which week each figure describes
- `next_stage` set to the desks the forum directed work into, with the scope carried rather than summarized
- `artifacts`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: a metric would reach a governing body or a regulator-facing accountability record with no computed basis under it, or a coverage figure would be stated against the register while reading as a statement about the estate. These numbers are read as evidence that the program operates, and a corrected figure after a decision has been taken on it is a governance failure rather than a data quality issue.
- **Missing approval**: publishing the pack externally, asserting a maturity rating, or recording a risk acceptance on behalf of the organization needs a named owner with the authority level the decision requires.
- **Source conflict**: two registers genuinely disagree about the same population, such as the vendor count in procurement against the vendors receiving data. Preserve both readings on the figure rather than reporting the one that produces the better rate.
- **Security or privacy**: a metric or its supporting extract would carry personal data into a reporting artifact with a wider audience than the data had, which a request-level export routinely does.
- **Production or destructive**: the next action would write into the accountability record, amend a prior period's reported figures, or close a finding in the register.
- **Connector unreachable**: a register or a denominator source exists and cannot be read, so a coverage figure would describe a population nobody counted.

An unavailable prior period, a missing owner on one finding, and an unrated maturity dimension are soft gaps. Report the figure with the limitation stated and continue.

## Downstream handoffs

The program record goes back to `privacy-data-protection-command-desk`, and the work the forum directs goes into the desk that owns it with scope attached: coverage gaps to `data-inventory-mapping-desk`, assessment backlog to `dpia-desk`, uncontracted vendors to `processor-vendor-agreement-desk`, uncovered transfers to `cross-border-transfer-desk`, overdue requests to the rights desks, over-retention to `retention-deletion-desk`, and tracker drift to `cookie-tracking-governance-desk`. Each handoff carries the metric that surfaced it and the denominator behind it, so the receiving desk works the actual gap rather than the percentage.

## Quality bar

Good program reporting is recognizable by what it is willing to put a denominator on. A pack that reports ninety-four percent records-of-processing coverage without saying coverage of what is describing its own register, and a reader who notices will discount everything else in it. The attainment section counts the overdue requests that are still open, which is the number an operational dashboard is structured to hide. The coverage section names the systems nobody has reached rather than reporting the complement. The escalations ask for decisions rather than reporting status, because a forum that only notes things is not governing. And the accountability record is assembled as evidence rather than as narrative, since the difference between a program that works and a program that describes itself well is exactly what an authority is looking for when it asks the organization to demonstrate compliance.
