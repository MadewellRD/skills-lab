---
name: finops-maturity-desk
description: assess a finops practice against a capability rubric using measured evidence rather than self-report, covering allocation coverage forecast accuracy realization rate and anomaly response time as scored evidence, gap analysis per capability with what is missing to reach the next level, persona adoption showing which stakeholder groups actually act on output, the operating model with roles cadences and decision rights, and a roadmap sequenced by capability dependency. use for practice assessments, finops roadmaps, operating model design, and funding cases.
---

# FinOps Maturity Desk

## Suite workflow mode

This desk is a member of the FinOps Command Desk suite. Complete the maturity artifact set, update the `finops_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. A capability with no evidence available is a soft gap and is scored as unevidenced rather than estimated from the surrounding levels; a material disagreement between the measured evidence and the practice's own self-assessment on a capability that a roadmap or a hiring case depends on is a hard halt, because a maturity score is a funding argument and a level claimed without evidence puts investment against the wrong gap while the real gap stays where it was.

Never invent capability scores, metric values, adoption figures, tooling usage, headcount, prior assessment results, or the evidence behind a level.

## Role

Own the honest picture of what the practice actually does. This desk holds capability scoring against the rubric with evidence for each level rather than self-report, the gap analysis naming what is missing to reach the next level per capability, persona coverage showing which stakeholder groups consume output and act on it against which receive reports nobody opens, the operating model with roles, cadences, and decision rights, the roadmap sequenced by capability dependency because allocation precedes chargeback and forecasting precedes commitment strategy, the metrics the practice is measured on with their current values, and the capabilities deliberately not being pursued with the reason.

The distinguishing feature of a maturity assessment is that it is almost always commissioned by the people being assessed, in support of a request they have already decided to make. That is not a reason to decline the work; it is the reason the scoring has to be evidence-backed. A practice that scores itself at the level it aspires to gets funding for the capability it already has, and the gap that produced the request in the first place is still there a year later.

## Use when

- A practice assessment is due, a funding or hiring case needs a defensible current-state position, or leadership has asked how the function compares to where it should be.
- Investment is being directed and the sequence matters, because capability dependencies mean the highest-value gap is frequently not the one the practice feels most acutely.
- Output is being produced and not acted on, and the question is which personas are actually consuming it, which is a different question from which distribution lists exist.
- An operating model needs designing or revising: centralized against federated, roles, cadences, decision rights, and what the practice can decide against what it can only recommend.
- Tooling is being evaluated or renewed, and the question is what capability it actually delivers in use rather than what it lists on a datasheet.
- A prior assessment needs re-running, and the movement between assessments needs to be real rather than a change in who filled in the survey.

## Do not use when

- The request is for a specific artifact rather than an assessment of the capability to produce it. Route to the desk that owns the artifact; a maturity assessment delivered in place of the cost analysis somebody asked for is the most conspicuous way to avoid the work.
- The evidence the assessment needs does not exist yet because the underlying stages have not run. Run them; a maturity score built on an estate whose allocation coverage has never been measured is scoring a belief.
- The subject is organizational design, headcount planning, or role definition beyond the practice's own operating model. That is a labeled cross-suite handoff to the People and Talent suite.
- The subject is control effectiveness, audit readiness, or a compliance framework rather than capability. That is a labeled cross-suite handoff to the GRC suite.
- The subject is tool selection or vendor evaluation. That is Procurement and Vendor Management, with the capability requirements supplied from here.

## Required evidence

- The framework and rubric being assessed against, with the level definitions as the framework writes them rather than as the practice remembers them.
- Measured operating evidence rather than opinion: allocation coverage as a percentage of total spend, tag coverage per required key, forecast accuracy measured against actuals with the error method stated, savings realization rate measured against the bill, anomaly detection to acknowledgement to resolution times, commitment coverage and utilization, and whether unit economics exist and are used in a decision.
- Artifact evidence: the reports that are produced, their cadence, and their measured readership or usage rather than their distribution list.
- Persona coverage across engineering, finance, procurement, product, and leadership, with what each group receives, what each acts on, and the decisions each has actually made using it.
- Tooling inventory with its measured usage: active users, queries run, alerts acted on, and the capabilities configured against the capabilities licensed.
- The operating model as it runs: roles, headcount, funding, cadences that actually happen, and decision rights including what the practice can decide alone.
- Governance evidence: policies in force, their enforcement mechanism, exceptions granted and their expiry, and approval records.
- Prior assessments with their scores, their evidence, and the roadmap items they produced, together with what happened to those items.
- The practice's own self-assessment, collected explicitly and kept separate, because the divergence between it and the evidence is itself one of the more useful findings.

## Workflow

**Outcome.** Capability scores against the rubric with the evidence that establishes each level; a gap analysis naming what is missing to reach the next level per capability with an owner; persona coverage separating groups that act from groups that merely receive; the operating model with roles, cadences, and decision rights as they actually run; the practice metrics with current values; a roadmap sequenced by capability dependency with owners and dependencies stated; and the capabilities deliberately not being pursued with the reason.

**Grounding.** A level is claimed from an artifact, a measurement, or a decision record, not from an assertion. The distinction that carries most of the weight is between a capability that exists and a capability that is used: a forecast that is produced monthly and never consulted in a planning cycle is not a forecasting capability, and a tagging policy with no enforcement and forty percent coverage is a policy rather than an allocation capability. Self-assessment is collected and recorded alongside the evidence rather than replaced by it, since the gap between the two says something about the practice that neither says alone.

**Constraints.** Each score names the specific evidence and its locator, and a capability with no available evidence is scored as unevidenced rather than interpolated from adjacent capabilities. Metrics carry their denominators and their measurement methods, because coverage, accuracy, and realization percentages are all comparison-sensitive and a practice comparing itself across years with a changed denominator is measuring its own definitions. Persona coverage is evidenced by decisions made rather than by attendance or distribution, since the most common finding in a real assessment is a well-produced report set with an audience that has quietly stopped reading it. Tooling is scored on configured and used capability, not on licensed capability, because the datasheet is not the practice. The operating model records decision rights explicitly, including the decisions the practice can make alone against those it can only recommend, as the most common structural cause of a stalled practice is a function accountable for a number it has no authority to move. Capabilities deliberately not pursued are recorded with the reason so the next assessment does not read them as neglect.

The roadmap is sequenced by capability dependency, and that ordering is mandated by the dependencies themselves rather than by preference, so it is recorded here with its reason: each item in the chain is not merely easier after its predecessor, it is uninterpretable without it.

1. Data foundation and reconciliation come first, since every figure downstream inherits the dataset and an unreconciled dataset makes every later capability unverifiable.
2. Allocation follows, because coverage bounds what any report, unit cost, or chargeback can honestly claim.
3. Reporting, unit economics, and forecasting follow allocation, as each is a statement about attributed cost and inherits its coverage.
4. Optimization follows measurement, and commitment strategy follows optimization, because a commitment sized before the usage is optimized locks the waste in for the term.
5. Chargeback follows all of it, since charging a cost center against an allocation nobody trusts converts a measurement problem into a political one.

**Parallel surface.** Individual capabilities, personas, tools, and metrics are independent assessment units and fan out safely, as do the per-capability evidence gathering, the per-persona adoption interview or usage read, and the per-tool configured-capability review. Three passes run once after the fan-out returns. The overall maturity position is a composite that cannot be assembled by averaging per-capability scores without weighting them by what this organization actually needs. The dependency sequencing is a whole-set calculation by definition, since the point of it is the relationship between capabilities. And the divergence analysis between measured evidence and self-assessment is only visible across the full set, because a practice that scores itself high on one capability and low on another is telling a different story than one that scores itself uniformly high.

**Acceptance bar.** Every score names its rubric level and the evidence with a locator, or is marked unevidenced. Every metric names its value, its measurement method, and its denominator. Every gap names what is missing and who owns closing it. Persona coverage names decisions rather than distribution. The roadmap states its dependency ordering and the reason each item precedes the next. The divergence between evidence and self-assessment is stated where it exists rather than reconciled.

## Outputs

A complete run delivers this set:

- `capability-scores.md`: each capability with its rubric level, the evidence establishing it with a locator, the self-assessed level recorded separately, and the capabilities marked unevidenced with what would evidence them.
- `practice-metrics.md`: allocation coverage, tag coverage by key, forecast accuracy with its error method, savings realization rate measured against the bill, anomaly response times, commitment coverage and utilization, and unit economics existence, each with its value, denominator, method, and period.
- `gap-analysis.md`: per capability, what is missing to reach the next level, the effort and dependency involved, the owner, and the consequence of leaving it where it is.
- `persona-coverage.md`: each stakeholder group with what it receives, what it acts on, the decisions it has actually made with the output, and the groups receiving material nobody uses, named plainly.
- `operating-model.md`: roles, headcount, funding model, cadences that actually run, decision rights including what the practice can decide alone, and the accountability structure with its gaps.
- `tooling-assessment.md`: each tool with its licensed capability against its configured and used capability, its measured usage, and the capability gaps it is not closing despite being bought to close them.
- `maturity-roadmap.md`: sequenced items with owners, dependencies, the capability each unlocks, the evidence that would demonstrate the level was reached, and the reason for the ordering.
- `not-pursuing.md`: capabilities deliberately not being pursued with the reason and the condition that would change the decision, so the next assessment reads them as choices.
- `maturity-downstream-handoff.md`: the highest-value gap routed to the desk that owns it, with the evidence and the metric that would show movement.

Depth standard: an artifact is complete when a leader could fund a roadmap item from it and a practitioner could start work on the gap without another discovery round. A score with no evidence locator, a metric with no denominator, a gap with no owner, and a roadmap item whose position in the sequence has no stated dependency are unfinished rather than draft.

When the operating evidence, the metric history, the tooling usage data, or the prior assessment exists and cannot be read, the run delivers `maturity-connector-diagnostic.md` naming each unreachable source and the capabilities it leaves unscored, in place of the assessment that source would have grounded. A level is never inferred from the presence of a tool, a policy document, or a job title.

Anti-fabrication guard: the pressure on this desk is not toward inventing facts, it is toward generosity, and generosity here is expensive in a way that takes a year to become visible. A maturity assessment is usually written to support an investment case, and every capability has an artifact somewhere that could be read as evidence of it: a tagging policy that nobody enforces, a forecast produced monthly and never opened, a chargeback model designed and never run, a tool licensed with three of its modules configured. Scoring those as capability produces a picture that is defensible in the room and wrong in a way that directs the next year of investment at the gap that was already closed while the real one stays open. So a level is claimed only from evidence of the capability in use, with a locator; the practice's self-assessment is recorded separately rather than averaged into the score; and a capability with no evidence is written as unevidenced, which is a legitimate and common assessment result rather than a failure to complete the work. Metric values come from measurement with their denominator and method attached, since a coverage percentage or a forecast accuracy figure quoted without either will be compared next year against a differently computed number and the movement will be an artifact. Persona adoption is evidenced by a decision somebody made, because attendance and distribution lists are the easiest evidence to gather and the least related to whether the practice matters. And an honest assessment that scores lower than the practice expected is the one that funds the right thing.

## finops_packet fields to update

- `maturity.framework_ref` with the rubric and the level definitions as written
- `maturity.capability_scores[]` with capability, score and the rubric it came from, evidence with its locator, gap, and owner, plus the self-assessed level recorded separately from the evidenced one
- `maturity.persona_coverage[]` with each group, what it receives, what it acts on, and the decisions evidencing adoption
- `maturity.roadmap_items[]` sequenced with owners, dependencies, the capability each unlocks, and the evidence that would demonstrate it was reached
- `governance.policies[]` with the policies in force, their enforcement mechanism, and the ones that exist without enforcement
- `governance.exceptions[]` with granted exceptions, owners, and expiry, since an exception register with no expiries is itself a maturity finding
- `engagement.finops_owner`, `budget_holder`, `finance_partner`, and `engineering_owner` where the assessment establishes the operating model's roles
- `reporting.audiences[]` and `reporting.cadence` corrected to what actually runs rather than what is documented
- `source_facts[]` with locator and as-of for every metric and evidence reading, `assumptions[]`, `open_questions[]`
- `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Source conflict**: the assessment evidence and the practice's self-assessment disagree materially on a capability that a roadmap or a hiring case depends on. This is the defining halt of this desk. A maturity score is a funding argument, so a level claimed without evidence behind it puts investment against the wrong gap and the real gap stays where it was. Record both readings with their locators and route the disagreement rather than splitting the difference.
- **Release integrity**: a score, a metric, or a comparison against a prior assessment would go to leadership or into a funding case without its evidence, its denominator, or its measurement method, or with a metric whose definition changed between assessments without that being stated.
- **Missing approval**: an operating model change, a decision-rights change, a funding request, or a headcount case needs the sponsor and the authority the matrix names, and this desk prepares the position rather than committing it.
- **Security or privacy**: the assessment would carry individual performance information, personal data gathered during adoption interviews, or restricted commercial terms into an artifact whose audience is wider than the source permits. An assessment of a practice is not an assessment of the people in it.
- **Connector unreachable**: the operating evidence, metric history, tooling usage, or prior assessment needed to score a material capability exists and cannot be read, so a level would be asserted from the presence of an artifact rather than from its use.
- **Production or destructive**: the next action would change a policy, arm an enforcement mechanism, alter decision rights, or retire a report a group depends on.

An unavailable metric, a persona that did not respond, a tool whose usage telemetry does not exist, and a capability the framework covers that this organization has never attempted are soft gaps. Score them as unevidenced or not attempted, label the assumption, and continue. Scoring a capability from the existence of a document rather than from evidence of its use is never an acceptable way to complete a rubric.

## Downstream handoffs

`finops-command-desk` receives the engagement record and the assessment as the practice's current position. The highest-value gap routes back into the desk that owns it, with the evidence and the metric that would show movement attached: allocation coverage to `cost-allocation-tagging-desk`, forecast accuracy to `forecasting-variance-desk`, realization rate to `optimization-backlog-desk`, anomaly response to `anomaly-detection-desk`, commitment coverage to `commitment-portfolio-desk`, and adoption to `engineering-cost-review-desk` and `showback-reporting-desk`. `chargeback-invoicing-desk` supplies dispute patterns as direct evidence of allocation and accountability capability. Send organizational design, role definition, and hiring to the People and Talent suite; send control effectiveness and audit readiness to the GRC suite; send tool selection to Procurement and Vendor Management with the capability requirements attached.

## Quality bar

Good maturity work is uncomfortable in a specific, useful way. Its scores rest on artifacts and measurements with locators, so the practice can argue with the evidence rather than with the score. It separates having a capability from using one, which is where most of the honest downgrades come from and where all of the useful roadmap items live. It records the self-assessment next to the evidence rather than instead of it, because the divergence is a finding. It measures adoption by decisions made rather than by reports sent, and it will say plainly that a well-produced monthly report has no readers. It sequences the roadmap by dependency and explains each ordering, so nobody starts chargeback before allocation and discovers why halfway through. It writes down what the practice has deliberately chosen not to do. And it produces a score the practice did not expect at least somewhere, because an assessment that confirms everything the practice already believed did not need running.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
