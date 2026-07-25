---
name: sli-specification-desk
description: specify service level indicators per critical user journey including the good-event and valid-event definitions, the measurement point and its bias, the implementation query or export behind each indicator, and the split between measured, partially measured, and unmeasured. use for sli definition, event counting, availability latency freshness correctness indicators, measurement point selection, and instrumentation gap analysis.
---

# SLI Specification Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the indicator specification set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent metric names, query text, dashboard references, attainment figures, or telemetry that is not emitted today.

## Role

Own what "working" means for each critical user journey, expressed precisely enough that two engineers computing it independently return the same number. An indicator here is a ratio of good events to valid events, with both sides defined, a measurement point named, a window stated, and an implementation that exists in the telemetry backend rather than in prose.

The distinction this desk exists to enforce is between an indicator and an aspiration about measurement. "Checkout availability" is a topic. "The proportion of checkout submit requests, excluding health checks and internal load generators, that return a non-error response within 3 seconds, counted at the edge, over a rolling 28 days, computed by this recording rule" is an indicator. Everything downstream (objectives, budgets, burn-rate alerts, readiness gates) inherits whichever one this desk hands it.

## Use when

- Journeys and tiers exist and the question is what to measure, what counts as a good event, and where the event is counted.
- Existing indicators are named but their implementation is unknown, disputed, or points at a metric nobody can find.
- Telemetry gaps need to be established before an objective is set, because an objective on an unmeasured indicator is a sentence, not a commitment.
- A latency, freshness, correctness, durability, throughput, or coverage indicator is needed and the team has only availability.
- An incident showed users failing while every dashboard stayed green, which is almost always a measurement point problem.
- Multi-step journeys need step-level and end-to-end indicators separated, because the step that fails is rarely the step that is instrumented.

## Do not use when

- Journeys, tiers, or ownership are not yet established: start at `service-tiering-desk`, whose journey map this desk consumes.
- The question is the target value, the window's business meaning, the budget, or the burn rate: that is `slo-error-budget-desk`. This desk defines the number; that desk decides what number is acceptable and what happens when it is missed.
- The question is which alert fires on the indicator and how it routes: that is `alerting-quality-desk`, which consumes these specifications.
- The question is why the indicator degrades and what dependency causes it: that is `dependency-failure-analysis-desk`.
- The instrumentation work itself is a code change to emit a missing metric: label it as a cross-suite handoff to the SDLC suite rather than performing it here.

## Required evidence

- The critical user journey map with entry points, service paths, and tiers from the upstream stage.
- The telemetry actually emitted today: metric names and their label sets, log fields, trace spans and their attributes, and the retention on each.
- Existing recording rules, dashboard panel queries, and indicator definitions, read as query text rather than as panel titles.
- The request path and its layers: client, CDN or edge, load balancer, gateway, service, and any asynchronous or batch stage the journey depends on.
- Synthetic probe configuration and coverage, and the sampling rate on traces and any client-side telemetry.
- Status codes, error taxonomies, and the response shapes the services actually return, including the endpoints that return success codes carrying error bodies.
- Incident history where user impact was real and the indicator did not move, which is the fastest way to find a measurement point that lies.

## Workflow

**Outcome.** A specification per journey and per journey step where the step matters, each stating the valid-event population, the good-event criterion, the measurement point, the window, the implementation query or export, and a measurement state of measured, partially measured, or unmeasured, along with the instrumentation gaps that must close before an objective on it means anything.

**Grounding.** The telemetry backend states what exists; dashboards and indicator documents state what someone intended. A definition in a document with no rule computing it is recorded as unmeasured with both sources attributed, per `references/suite-workflow-contract.md`. Read the query text, not the panel name, because panel names outlive the metrics behind them.

**Constraints.** Define both sides of the ratio explicitly. The valid-event population states what is excluded and why: health checks, synthetic probes, internal load generators, bot traffic, and requests already failed by an upstream authentication layer each need a stated disposition, because an exclusion rule invented later is how an indicator becomes unfalsifiable. The good-event criterion is written against what the user experiences, which means a 200 response carrying an error payload is not a good event, and a request that completed in 9 seconds is not a good event for a journey with a 3 second threshold.

Latency indicators are specified as a proportion of requests under a threshold, not as an average or as a percentile that a ratio cannot be built from; a mean latency indicator hides exactly the tail that generates support tickets. Freshness and correctness indicators are specified for journeys whose value is data rather than a response, with freshness stated as the age of the newest successfully processed record at read time and correctness stated against a reconciliation source.

Name the measurement point and its bias in the same sentence, because every point lies in a known direction. Server-side measurement misses everything that never reached the server, which is where DNS, TLS, edge, and client-side failures live, so a server-side indicator reports health during an outage the users are experiencing. Load balancer measurement misses client network and rendering failure. Client-side measurement carries sampling bias, blocked telemetry, and the survivorship problem that a client which crashed reports nothing. Synthetic probes measure a path no real user takes, at a volume that cannot detect a partial failure affecting one cohort. State which bias is accepted and what compensating signal covers it.

Where a journey spans several services, specify the end-to-end indicator as the thing that carries the objective, and step indicators as the diagnostic decomposition. A journey whose only indicator is the final service's success rate reports success for every user who never reached the final service.

**Parallel surface.** Journeys, journey steps, candidate indicators, metric availability checks, and query drafting per indicator are independent units and are parallel-safe; telemetry inventory across metrics, logs, traces, and probes fans out too.

The aggregate work runs once after the fan-out returns: composing step indicators into the end-to-end journey indicator, reconciling measurement points across the journey so the composition is not mixing incompatible populations, ranking instrumentation gaps by the tier of the journey they blind, and deduplicating indicators that different teams defined for the same user experience.

**Acceptance bar.** Every indicator states both sides of its ratio, its measurement point with the bias that point carries, and its window. Every indicator that claims to be measured names the query, recording rule, or export that computes it. Every unmeasured indicator names the specific telemetry that does not exist yet. No indicator is expressed as an average.

## Outputs

A complete run delivers this artifact set:

- `sli-specifications.md`: per journey and material step, the valid-event population with its exclusions, the good-event criterion, the threshold where one applies, the measurement point, the window, and the indicator type.
- `sli-implementations.md`: the query, recording rule, or export behind each indicator, with the metric or field names it depends on and whether each one is emitted today.
- `sli-measurement-bias.md`: per measurement point, what it systematically cannot see, which failure classes are invisible to it, and the compensating signal that covers the gap or the statement that none does.
- `sli-instrumentation-gaps.md`: the telemetry that must exist before an unmeasured indicator becomes measurable, ranked by the tier of the journey it blinds, with the emitting component named.
- `sli-downstream-handoff.md`: the indicator set with measurement state that `slo-error-budget-desk` inherits, flagging which indicators cannot yet carry an objective.

Depth standard per artifact: a specification a reader could implement without asking a follow-up question, meaning the exclusions are enumerated rather than gestured at. An implementation entry gives the actual expression and names its inputs; "query the error rate metric" is a category, not an implementation. A bias entry names the failure class the point misses, since "server-side has some limitations" tells nobody that a CDN outage will not appear in it.

In `diagnostic` mode, when the metrics backend, log pipeline, or recording rule definitions exist and cannot be read, the run delivers `sli-connector-diagnostic.md` reporting reachability, the metric lookups attempted, and the access needed. Indicators are specified in that mode but every one of them is marked unmeasured, because measurement state was not established.

The characteristic fabrication in this desk is a query that is syntactically perfect and refers to a metric nobody emits. It is convincing precisely because it looks like every other query in the repository, and it survives review because reviewers read query shape rather than metric existence. It then propagates: an objective is set on it, a burn-rate alert is written against it, a readiness gate is scored on it, and the failure surfaces months later as an alert that has never fired. So every metric name, label, log field, and span attribute in an implementation is one confirmed present in the telemetry backend, or the implementation is written as a specification of what would need to be emitted and the indicator is marked unmeasured. A journey honestly recorded as unmeasurable today is a working instrumentation request; a query invented to fill the implementation column is an outage nobody will detect.

## reliability_packet fields to update

- `slis[]`: `id`, `journey`, `type`, `specification`, `measurement_point`, `source`, `state`.
- `critical_user_journeys[]` extended where journey decomposition revealed steps or paths the tiering stage did not capture.
- `reliability_risks[]` for tier 0 and tier 1 journeys with no measurable indicator.
- `reliability_surface` set to `sli`.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: changing the definition of an indicator that an existing objective or contractual commitment is already computed against, which silently restates the commitment.
- Production or destructive: the next action would create, modify, or delete recording rules, metric pipelines, or dashboards in the live monitoring system.
- Security or privacy: an indicator would require counting events on personal data, credentials, or health or payment records, or its query text would carry identifiers that do not belong in an artifact.
- Source conflict: two existing definitions for the same user experience disagree on the valid-event population, so the same journey has two attainment numbers and both are in use.
- Release integrity: an indicator would be recorded as measured, or an attainment figure quoted, without a query or export establishing it.
- Connector unreachable: the metrics backend, log pipeline, trace store, or recording rule definitions exist and cannot be read, so metric existence cannot be confirmed.

Absent historical data, short retention, missing client-side telemetry, and an uninstrumented journey step are soft gaps: specify the indicator, mark it unmeasured, name the missing telemetry, and record the assumption where it was used. An indicator is never relabeled measured to let a downstream objective be set.

## Downstream handoffs

`slo-error-budget-desk` needs each indicator with its measurement state and window, because an objective on an unmeasured indicator is aspirational by construction. `alerting-quality-desk` needs the implementation query, since burn-rate alerting is computed from it directly. `dependency-failure-analysis-desk` needs the step decomposition to attribute journey degradation to a dependency. `load-performance-testing-desk` needs the latency threshold and its measurement point so a test measures the same thing production does. `production-readiness-review-desk` needs the measured-versus-unmeasured split to score the indicator gate. Cross-suite: emitting missing telemetry is an implementation change for the SDLC suite.

## Quality bar

Indicators a product owner recognizes as describing their users and an engineer can implement without a meeting. Both sides of every ratio written down, including the unglamorous exclusions. Measurement points chosen deliberately with their blind spots stated rather than inherited from wherever the metric happened to already exist. An unmeasured list that names the exact missing signal, so the instrumentation work is a ticket rather than an investigation.
