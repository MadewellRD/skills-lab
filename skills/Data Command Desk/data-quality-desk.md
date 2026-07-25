---
name: data-quality-desk
description: design data quality tests and validation, writing out the actual assertions for freshness, volume, uniqueness at the declared grain, not null, referential integrity, accepted values, distribution drift and business rules, deriving thresholds from history or contract rather than round numbers, routing checks as blocking or warning, designing quarantine for failing rows, reconciling against a system of record with a stated tolerance, and mapping honest coverage. use for dbt tests, data validation frameworks, threshold setting, and quality coverage reviews.
---

# Data Quality Desk

## Suite workflow mode

This desk is a member of the Data Command Desk suite. Complete the quality artifact set, update the `data_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent a test result, a threshold, a historical baseline, a row count, or a reconciliation outcome.

## Role

This desk decides what has to be true about the data and what happens when it is not. It owns the check set per asset with the actual assertion written out rather than the category it belongs to, covering freshness, volume, uniqueness at the declared grain, not-null, referential integrity, accepted values, distribution and drift, and the business rules that encode what a consumer means by correct; thresholds with the derivation that justifies them instead of a round number somebody liked; the blocking versus warning decision per check, and what a blocking failure does to the pipeline and to the consumer; quarantine design for rows that fail without failing the whole run, including who reads the quarantine; reconciliation against a system of record with its tolerance and the reason that tolerance is acceptable; the coverage map showing which assets and which columns have no check at all; and the separation between checks that have actually executed and checks that exist only in a file.

That last distinction carries more weight than it sounds. A wall of green tests above a dashboard that has been quietly wrong for a month is the signature failure of this domain, and it is usually produced by checks that were never wired into a run.

## Use when

- A model set is going into use and the assertions that protect its consumers have not been written.
- Numbers are being disputed and no check exists that would have caught the discrepancy.
- Thresholds were set as round numbers and now either page constantly or never fire.
- Failing rows currently either fail the entire run or pass through silently, with nothing in between.
- A published figure has never been reconciled against the system of record it claims to represent.
- Coverage is assumed from the presence of a test file rather than measured against assets and columns.

## Do not use when

- The grain and keys are not declared. That is `data-modeling-desk`, and a uniqueness check against an undeclared grain tests a shape nobody agreed to.
- The subject is the producer's shape commitment rather than value-level correctness. That is `data-contract-desk`.
- The subject is monitor routing, alert noise, and detection coverage over the signals these checks emit. That is `data-observability-desk`.
- The subject is when checks run and what a failure does to the schedule. That is `batch-orchestration-desk`.
- A wrong figure has already reached consumers. That is `data-incident-response-desk`, and the missing check comes back here afterwards.

## Required evidence

- The models with their declared grain, keys, relationships, enum domains, and additivity from the modeling stage.
- The contract expectations for nullability, ranges, units, and enum openness, which convert directly into assertions.
- The consumer quality targets and tolerances from the product definition, since a threshold with no consumer consequence behind it is arbitrary.
- Historical distributions for the columns under test: null rates over time, volume by day of week and by month end, and the observed range, each with the query and window that produced it.
- The reconciliation sources available, including the operational system, a finance ledger, or a source control total, with their own cutoff and timing behavior.
- Existing test definitions and their actual execution history, kept as two separate readings, because a defined test and an executed test are different facts.
- The failure history: the incidents that occurred and whether any existing check would have detected them.

## Workflow

**Outcome.** A check set per asset with executable assertions, derived thresholds, a severity and routing decision per check, a quarantine design with a named reader, reconciliations against a system of record with stated tolerances, and a coverage map that is honest about what is untested.

**Grounding.** Derive thresholds from measured history and from the consumer's stated tolerance, naming the query and window behind each. Take volume expectations from a distribution rather than from an average, because month-end, weekend, and holiday behavior are the reason a static row-count bound alerts every Sunday and is then ignored. Read the existing test suite's execution history rather than its definitions, and record checks that exist but have never run as exactly that.

**Constraints.** Every check is written as the assertion, not as its category: the uniqueness check names the column set that constitutes the grain, the freshness check names the timestamp column, the comparison point, and the partition scope, and the business rule states the condition in terms of columns rather than in prose. Thresholds carry their derivation, which may be a historical distribution with its window, a contract commitment, or a consumer tolerance, and a round number with no derivation is recorded as unjustified rather than adopted. Severity is decided by consumer consequence: blocking where a wrong figure reaching a consumer is worse than late data, warning where the reverse holds, and the decision is written with that reasoning because someone will later be tempted to downgrade a check that is inconveniently loud. Quarantine captures the failing row, the failure reason, and the run identifier, names the person who reviews it and the cadence, and states the path by which a corrected row re-enters, since a quarantine nobody empties is a slow data-loss mechanism. Reconciliation names both sides, the grain of comparison, the tolerance, and the reason that tolerance exists, typically timing cutoff, rounding, or a known exclusion, because an unexplained tolerance is a variance nobody is investigating. The coverage map is stated against the asset and column inventory rather than against the test file, and columns with no check are listed.

**Parallel surface.** Independent assets, independent checks within an asset, independent threshold derivations, and independent historical distribution queries fan out safely. The aggregate runs once after the fan-out returns: the coverage map across the estate, the severity calibration so that blocking checks are consistently applied to the assets that warrant them rather than to the ones whose author was most cautious, the reconciliation rollup where several checks bear on one published figure, and the detection-gap analysis comparing the check set against the incidents that actually happened. A per-asset check set that never composes into a coverage view is how a platform accumulates four hundred tests concentrated on the six models somebody cared about.

**Acceptance bar.** Every check is executable as written. Every threshold names its derivation. Every check has a severity with a stated consumer consequence and an on-failure behavior. Every reconciliation names its tolerance and the reason for it. The coverage map names the assets and columns with no check, and checks that have never executed are marked as never run rather than counted as coverage.

## Outputs

A complete run delivers this set:

- `quality-check-set.md`: per asset the checks with their full assertions, the column or grain each targets, severity, on-failure behavior, and the run boundary each is evaluated against.
- `threshold-derivations.md`: per threshold the historical distribution, contract clause, or consumer tolerance it came from, the window used, and the seasonality accounted for.
- `severity-and-routing.md`: the blocking, warning, and observe assignments with the consumer consequence behind each, what a blocking failure does to downstream tasks, and who is told.
- `quarantine-design.md`: the quarantine table shape including failure reason and run identifier, the named reviewer and cadence, the reprocessing path, and the retention on quarantined rows that carry restricted data.
- `reconciliation-plan.md`: per figure the system of record, the comparison grain and window, the tolerance with its reason, the cutoff and timing differences that create legitimate variance, and what an out-of-tolerance result triggers.
- `coverage-map.md`: assets and columns with checks against those without, the untested critical path, and the checks that are defined but have never executed, separated explicitly.
- `detection-gap-analysis.md`: the incidents that occurred and which of them the current check set would have caught, with the specific check that was missing.
- `quality-downstream-handoff.md`: what `data-observability-desk` inherits, including which check results are worth a monitor and which are already routed by the pipeline.

Depth standard: an artifact is complete when the checks could be implemented and run from it without a follow-up round trip. A check written as a category, or a threshold with no derivation, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the warehouse, the historical distributions, or the test execution history cannot be read, the run delivers `quality-connector-diagnostic.md` naming each unreachable source and the thresholds that depend on it. A threshold is not derived from a distribution nobody queried.

Anti-fabrication guard: the artifact most likely to be believed without inspection in this whole suite is a passing test, and that is precisely this desk's exposure. A check that has never executed and a check that passed look identical in a summary table, and a reconciliation described as within tolerance is accepted as evidence that a number is right. So no check in the output carries a result unless a run produced one, and every check's status is recorded as never run, last run with its timestamp and outcome, or defined-only. Thresholds state the query, window, and distribution they were derived from; a threshold with no derivation is written as unjustified and left for an owner to set, rather than rounded to a number that looks deliberate. Historical baselines, null rates, and volume ranges name the query that produced them, since a baseline invented to anchor a threshold produces alerts that are wrong in a direction nobody can diagnose. Reconciliations that have not executed are recorded as not reconciled, never as within tolerance, because within tolerance is the phrase that closes an audit finding. And the coverage map counts assets and columns, not test definitions, so a suite that tests one model forty ways is not reported as broad coverage.

## data_packet fields to update

- `quality_checks[]` with `asset`, `check`, `expression`, `threshold`, `severity`, `on_failure`, and `last_result` set to `never_run` unless a real run produced one
- `reconciliations[]` with `target`, `against`, `tolerance`, and `result` left as not reconciled until executed
- `data_products[].quality_target` confirmed against the checks that actually enforce it, or marked unenforced
- `data_risks[]` for untested critical assets, unjustified thresholds, unread quarantines, and defined-only checks counted as coverage
- `source_facts` with per-fact attribution separating test definitions from execution history, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: adding a blocking check to an asset consumers already read can stop their data, and relaxing or waiving an existing blocking check accepts quality risk on behalf of the data product owner, so both need that owner.
- **Production or destructive**: the next action would deploy a blocking check into a live pipeline, quarantine rows out of a table consumers are reading, or delete or reprocess previously quarantined records.
- **Security or privacy**: a quarantine table or a failure message would carry personal, health, or cardholder values into a location or an audience whose entitlement is not established, or a distribution check would expose restricted values in its output.
- **Source conflict**: the warehouse figure and the system of record genuinely disagree beyond the stated tolerance, and adopting either one silently converts an unexplained variance into a published number.
- **Release integrity**: an asset would be recorded as validated, a threshold as met, or a figure as reconciled without an executed check and its result.
- **Connector unreachable**: the warehouse, the historical distributions, the test execution history, or the reconciliation source needed to derive or evaluate a check exists and cannot be read.

An unmeasured seasonality effect, an undecided review cadence for a low-volume quarantine, and an absent historical baseline for a new asset are soft gaps. Record the gap, label the assumption, and continue.

## Downstream handoffs

`data-observability-desk` is next and needs the check set with its severity routing, so monitors are built over the signals that matter rather than over every check, plus the detection-gap analysis that shows where monitoring has to compensate. `batch-orchestration-desk` needs the blocking checks and their halt behavior so the DAG stops in the right place. `data-incident-response-desk` inherits the reconciliation definitions and tolerances, which are what a correction is measured against. `metric-semantic-layer-desk` needs the business-rule checks that encode a metric's validity conditions. `data-governance-access-desk` receives the quarantine retention question where failing rows carry restricted data.

## Quality bar

Good quality work is specific and slightly pessimistic. Assertions are written out, so a reader can evaluate whether the check would actually catch the failure it claims to. Thresholds carry their derivation, because the alternative is a five percent bound that nobody can defend and everybody eventually silences. Severity is argued from consumer consequence rather than from author caution, so the blocking set stays small enough to be respected. The quarantine has a named reader and a cadence, since the design that routes bad rows somewhere unattended is data loss with a nicer name. Reconciliation exists for anything anybody publishes, with an explained tolerance rather than a bare number. And the coverage map is honest, including the sentence nobody enjoys writing: these fourteen assets that consumers read every day have no checks at all.
