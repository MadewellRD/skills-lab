---
name: continuous-control-monitoring-desk
description: design and assess continuous control monitoring across the monitoring coverage map, automated check definitions with signal source and evaluation frequency, configuration drift and check failure routed to a named owner, control health metrics computed from actual results, monitoring evidence produced as a byproduct, and checks blocked on a missing signal source. use for control automation, monitoring coverage gaps, alert ownership, control health dashboards, and converting manual controls into continuously evidenced ones.
---

# Continuous Control Monitoring Desk

## Suite workflow mode

This desk is a member of the GRC Command Desk suite. Complete the monitoring artifact set, update the `grc_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance statement asserted on evidence that cannot carry it, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the check or control it affects, and record it in `open_questions`. Never invent check identifiers, signal sources, evaluation frequencies, last-run timestamps, pass rates, coverage percentages, or the owner a failure routes to.

## Role

Own the distance between a control the organization believes is operating and a control something is actually watching. This desk produces the coverage map that says which controls are observed continuously and which are observed once a year by a tester, check definitions that name their signal source and evaluation frequency, drift and failure detection that lands on a named human who can act, control health metrics computed from real result history, the evidence that monitoring produces as a byproduct so the next test does not start from an empty folder, and the explicit list of checks that cannot exist because their signal source is unavailable.

A monitor is a chain: the system has to emit the signal, the collector has to be authorized to read the whole population rather than a slice of it, the check has to run on its schedule, the failure has to reach someone with the authority to fix it, and the result has to be retained long enough to serve as evidence for the observation period. A break anywhere in that chain produces a monitor that reports nothing wrong forever, which is the same output as a control working perfectly.

## Use when

- Control coverage is being claimed, challenged, or reported as a percentage, and the denominator needs to come from an enumeration rather than from the asset register.
- Manual controls are being converted to automated or hybrid, and the check that will carry the evidence needs defining.
- A check is firing constantly, has never fired, or has silently stopped running, and its state needs an honest value.
- Configuration drift away from an approved baseline needs detecting, routing, and dating.
- Control health is being put on a dashboard or into a committee packet and every figure needs a computed basis.
- Monitoring is expected to produce audit evidence rather than only alerts, and the retention and periodicity of check results has to match the observation period.
- Alert ownership is unclear, and failures are landing in a queue nobody works.

## Do not use when

- The subject is a design or operating effectiveness conclusion over a defined period with a population and a sample. That is `control-testing-desk`, which consumes this desk's result history as evidence and does not replace it.
- The subject is the control narrative, owner, operating frequency, or key control designation. That is `control-design-desk`, whose evidence-source designation sets what a check can read here.
- A monitor has already produced a deficiency that needs classification, a corrective action plan, or a compensating control. That is `exception-remediation-desk`.
- Evidence is being pulled against an assessor request list for a closed period. That is `evidence-collection-desk`.
- The subject is detecting adversary behavior rather than control state. That belongs to the Security suite, whose detection coverage this desk maps to criteria rather than re-performs.

## Required evidence

- Control library with the automation designation, operating frequency, and named evidence source per control.
- Read access to the signal systems the checks depend on: identity provider, cloud configuration and posture APIs, device management, ticket and change records, code and pipeline systems, HR joiner and leaver data, and log platforms.
- Existing checks with their definitions, schedules, last run time, and full result history rather than a current-state dashboard.
- The enumeration each collector actually performs and the authorization scope it performs it with, since an integration wired to three of eleven cloud accounts has a denominator of three.
- Alert routing configuration, current on-call or ownership assignment, and the live suppression, snooze, and exclusion state.
- Prior test results and known deviations, so a check can be aimed at the failure mode that actually occurred.
- Retention configuration for the check results themselves, because monitoring output that ages out inside the observation period is not evidence for it.

## Workflow

**Outcome.** A monitoring coverage map keyed by control with the population each check actually observes, check definitions carrying signal source and evaluation frequency, drift and failure detection routed to a named owner with a response expectation, control health metrics computed from actual result history with their window stated, the evidence register of what monitoring produces per period, and a blocked list naming the signal source each blocked check needs.

**Grounding.** The signal system is authoritative for what a check can read; the monitoring platform's own run history is authoritative for whether a check ran and what it returned. The GRC platform's monitoring register is the program's record of itself and is outranked by run history wherever the two disagree, which they do most often for checks that were built, demoed, and then quietly disabled. Coverage is claimed per pair of control and observed population, where the population is the enumeration the collector performed rather than the inventory somebody maintains by hand.

**Constraints.** Every check names its signal source, the query or API call and the scope it runs with, its evaluation frequency, its pass criteria in terms a person could re-perform, the control it evidences, the owner a failure routes to, and how long its results are retained. Check frequency is reconciled against control operating frequency and the mismatch is stated in both directions: a check that runs less often than the control operates leaves periods unobserved, and a check that runs more often than the control operates generates findings against a control that was never meant to be continuous. Silence is not a pass. A check with no result inside its own interval is `failing` or `blocked_on_source`, never `live`, because an unauthorized collector, an expired credential, and a healthy environment all return the same quiet. Suppressions, exclusions, and snoozes carry a reason, an owner, and an expiry, since an indefinite suppression is a control waiver that never went to an approver. Control health metrics carry the window they were computed over and the check population they were computed across. Checks whose signal source does not exist or cannot be read are written as blocked with the source named, never as planned coverage.

**Parallel surface.** Individual checks, individual controls, and individual signal sources fan out and are parallel-safe; each is evaluated against its own system and its own history. The coverage percentage across the control library, the control health rollup, the deduplication of checks reading the same signal for different criteria, the reconciliation of monitored population against the tested population, and the ranking of blocked checks by how many controls each would unblock are single passes over the whole set after the fan-out returns.

**Acceptance bar.** An engineer could implement each check from its definition without asking what to query, and each failure lands on a named person with a stated response expectation. Every coverage figure names the enumeration it was computed from, every check carries a state from the fixed vocabulary with the date of its last real result, and every blocked check names the exact signal source that unblocks it.

## Outputs

A complete run delivers this set:

- `monitoring-coverage-map.md`: per control, whether it is continuously observed, periodically observed, or unobserved, the population each check reaches, and coverage stated as a fraction with its denominator named.
- `check-definitions.md`: per check, the signal source, query and scope, evaluation frequency, pass criteria, the control and criterion it evidences, severity, and result retention.
- `drift-and-failure-routing.md`: what constitutes drift from the approved baseline per check, the named owner each failure routes to, the response expectation, the escalation path, and the current suppression and exclusion register with expiries.
- `control-health-metrics.md`: each metric with its value, the window and check population it was computed over, its as-of timestamp, and the trend where enough history exists to support one.
- `monitoring-evidence-register.md`: what each check produces per period, where the result is stored, how long it is retained, and which control test or criterion it will serve.
- `blocked-checks.md`: checks that cannot run, the missing or unreadable signal source per check, the control left unobserved, and the exposure carried while it stays blocked.
- `monitoring-downstream-handoff.md`: what `exception-remediation-desk` inherits, including current failures with their owners, and what `control-testing-desk` can rely on as evidence versus what it still has to sample by hand.

Depth standard: an artifact is complete when the check could be built from it and its output would be accepted as evidence by someone re-performing the control. A coverage map listing control identifiers with a colored status and no population behind each is a dashboard, not an assessment.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when a signal system or the monitoring platform exists and cannot be read, the run delivers `monitoring-connector-diagnostic.md` naming each unreachable source, the checks whose current state is therefore unknown, and the coverage and health figures that cannot be computed. Coverage is never described from a check catalog alone, because a defined check and a running check are different facts.

Anti-fabrication guard: monitoring programs fabricate in exactly one direction, toward green, and they do it without anyone deciding to. An empty result set reads as compliant, a disabled check reads as quiet, an integration scoped to two of nine accounts reads as full coverage, and every one of those becomes a percentage in a committee packet. So a check state is written from its last real run with that timestamp attached, and `blocked_on_source` and `failing` are used freely because they are the states that get integrations funded. Coverage fractions are computed from the enumeration the collector returned, and where that enumeration is smaller than the known asset population, the gap is named rather than reconciled. No check is credited with observing a population it has no authorization to read, no health metric is quoted without the window and denominator it came from, and no monitor is described as live on the strength of a runbook entry saying it was deployed.

## grc_packet fields to update

- `monitoring[]` with `monitor_id`, `control_id`, `check`, `frequency`, `signal_source`, `state` from `live`, `proposed`, `failing`, or `blocked_on_source`, `last_result` carrying its date, and `coverage` with the basis of its denominator
- `control_library[]` where automation designation, evidence source, or design state changes because a check now carries the control or fails to
- `evidence[]` where monitoring output is the artifact for a control, with `period_covered`, `population_source`, and `completeness_basis` set from the collector's enumeration
- `findings[]` where a persistently failing check, an indefinite suppression, or an unobserved key control is itself a deficiency, with the affected population and an owner
- `approvals[]` where enabling a blocking check, changing alert routing, or accepting a control as unobserved needs the control or risk owner
- `source_facts[]` with `collected` times for every platform read, `assumptions[]` against the check they affect, `open_questions[]`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Connector unreachable**: a signal source or the monitoring platform exists and cannot be read, so any coverage or health figure would describe a population nobody enumerated. Coverage is the one number in this domain that cannot be estimated, because the estimate is always generous and always believed.
- **Security or privacy**: a proposed check would read personal data, credential material, customer content, or regulated records into the monitoring platform, or would replicate it across a residency boundary. Monitoring creates a second durable copy with its own retention and breach exposure.
- **Production or destructive**: the next action would enable, disable, or modify a check in a live platform, change alert routing or on-call assignment, alter a configuration baseline, or write a monitoring result into the system of record.
- **Missing approval**: accepting a key control as unmonitored, granting an indefinite suppression, or extending an exclusion past its expiry moves exposure onto the business and needs the control owner at the authority level the rubric sets.
- **Source conflict**: the monitoring register and the platform's run history genuinely disagree about whether a check is live, so neither reading can be presented as the coverage state. Record both against the field.
- **Release integrity**: a coverage percentage, control health metric, or continuous-monitoring assurance statement would go to an assessor, a customer, or a committee across controls where nothing was confirmed running.

An unknown check owner, an unstated response expectation, or a control whose operating frequency nobody documented is a soft gap: name it, label the assumption inline against that check, and continue with the check recorded as `proposed`. No control is marked observed to complete a map.

## Downstream handoffs

`exception-remediation-desk` is next and needs the current failing checks with their control linkage, the failure's first observed date, and the named owner, so a deficiency is classified against a dated condition rather than a symptom noticed this morning. `control-testing-desk` receives which controls now have monitoring evidence sufficient to reduce manual sampling and which still require it, with the population each monitoring source covers. `evidence-collection-desk` receives the evidence register so monitoring output is requested by locator instead of re-derived. `control-design-desk` receives design gaps where a control cannot be monitored as written. `committee-reporting-desk` receives control health metrics with their computed basis and window intact, since that basis is what makes them reportable.

## Quality bar

Good continuous control monitoring is judged by what happens when something breaks. A drift is detected within a window that matters, it reaches a named person, and the record of the detection survives long enough to be evidence. The coverage map is honest enough to be useful: partial coverage names the population it misses, blocked checks name the signal source, and the blocked list reads as the funding case for the integrations the program actually needs. Health metrics carry their denominators, so a number that moves can be explained by something other than a changed denominator. The most valuable output of a run is frequently a coverage figure lower than the one the program has been quoting, next to a precise account of what it would take to raise it.
