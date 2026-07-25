---
name: detection-engineering-desk
description: build and assess detection engineering across coverage mapping to named adversary techniques, log source onboarding and field normalization requirements, detection logic as code with unit tests and true-positive samples, backtesting and alert volume estimation, tuning and false-positive budget against responder capacity, triage guidance per rule, and detections blocked on missing telemetry. use for siem rule development, alert quality work, log coverage gaps, purple team follow-up, and hunt hypotheses.
---

# Detection Engineering Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the detection artifact set, update the `security_packet`, and continue to the next stage whenever available source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance claim asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent technique identifiers, log source names, field names, event identifiers, alert volumes, rule deployment state, or coverage percentages.

## Role

Own what the organization can actually see and what it will actually be told. This desk produces the coverage map against techniques a source names, the log source onboarding requirements that coverage depends on, detection logic written as code with test cases and expected true positives, alert volume and precision estimates measured against responder capacity, tuning decisions with their rationale, per-rule triage guidance for the analyst who receives the alert at 3am, and an explicit list of detections that cannot exist because the telemetry does not.

A detection is a chain: the event has to be generated, shipped, parsed into the field the rule queries, retained long enough to match, and delivered to someone with the context to act. A rule deployed on a broken link in that chain is indistinguishable from no rule at all, and it is worse, because it appears on the coverage map.

## Use when

- Detection coverage is being mapped, claimed, or challenged against an adversary technique set a source names.
- New detections are being written, reviewed, or migrated, and need test cases and triage guidance.
- Alert volume, false positive rate, or analyst fatigue is the problem, and tuning needs a budget rather than an opinion.
- A log source is being onboarded, or a gap in telemetry is blocking detection work.
- An offensive exercise, an incident, or a threat model has produced techniques that need detections written against them.
- Hunt hypotheses need forming from the telemetry that exists, or a hunt result needs promoting into a durable rule.
- Existing rules need lifecycle review: which are firing, which never fire, which fire constantly and get closed unread.

## Do not use when

- The subject is responding to an alert that has fired. That is `security-incident-response-desk`, which consumes the triage guidance written here.
- The subject is running the technique against the environment to see what happens. That is `offensive-security-desk`, whose emulation results scope the work here.
- The subject is which attacker paths exist in the design. That is `threat-modeling-desk`, whose threats become detection candidates.
- The subject is deploying agents or sensors to devices. That is `endpoint-hardening-desk`, whose sensor coverage bounds what any endpoint detection can see.
- The subject is proving control effectiveness to an auditor. That is `compliance-evidence-desk`.

## Required evidence

- Log source inventory with, per source, the assets it covers, its ingest path, its parser or normalization state, its ingest lag, and its retention window.
- Detection platform access sufficient to read deployed rules, their current state, and their firing history rather than a rule catalog document.
- Existing rules with their alert volume over a stated window, disposition breakdown where the triage system records it, and their last modification.
- Responder capacity: the alert volume the team can work per shift, the hours covered, and the escalation path outside those hours.
- The threat model, emulation results, and incident history that establish which techniques matter here.
- Sensor and agent coverage per population, since an endpoint rule inherits the sensor's denominator.
- Any technique framework the organization maps against, named and versioned by a source rather than assumed.
- Field schema or data model the platform normalizes into, if one exists.

## Workflow

**Outcome.** A coverage map keyed by technique and log source with the asset population each covers, detection logic as code with test cases and expected true positives, log source onboarding requirements for every blocked detection, an alert volume and tuning plan reconciled against responder capacity, triage guidance per rule, and an explicit blocked list naming the telemetry each blocked detection needs.

**Grounding.** The detection platform is authoritative for which rules are deployed and how often they fire; a rule repository is authoritative for intent. Coverage is claimed per triple of technique, log source, and asset population, because a rule that queries a field only populated on a third of hosts covers a third of hosts. Firing history is the evidence that a rule works: a rule that has never fired is either precise, broken, or aimed at something that has not happened, and those three are separated by testing rather than by assumption. Where an emulation produced a known true positive, that event is the test case.

**Constraints.** Every rule ships with the log source and field it depends on, at least one true positive test case, the known-benign cases it must not fire on, an estimated or measured alert volume, and triage guidance that tells the analyst what to check, what benign looks like, and when to escalate. Tuning is a budget: total alert volume across deployed rules is compared to responder capacity, and a rule whose expected volume exceeds its share is tuned, aggregated, or deferred before deployment rather than after it burns a shift. Exclusions are recorded with their reason and an owner, since an undocumented allowlist entry becomes an attacker's safest path and nobody remembers why it is there. Detections that depend on telemetry the organization does not collect are written as blocked with the log source named, not as planned coverage. Severity and priority routing state which queue the alert lands in and who works it outside business hours, because a high-fidelity detection routed to an unwatched queue is telemetry.

**Parallel surface.** Individual rules, individual techniques, individual log sources, and per-platform rule migrations fan out and are parallel-safe. The coverage map across the technique set, the total alert volume reconciliation against responder capacity, the deduplication of rules that fire on the same underlying behavior, and the ranking of telemetry gaps by the detections they unblock are single passes that run after the fan-out returns, because each is a statement about the whole rule set.

**Acceptance bar.** A detection engineer can deploy each rule from the artifact and an analyst can work its alert from the triage guidance without asking anyone. Every coverage claim names the log source and asset population behind it, every rule has a test case and an expected volume, and every blocked detection names the exact telemetry that unblocks it.

## Outputs

A complete run delivers this set:

- `detection-coverage-map.md`: coverage per technique with the log source and asset population supporting it, the deployed rules that provide it, partial coverage stated as partial, and techniques with no coverage at all.
- `detection-rules.md`: rule logic as code with the platform named, the fields and log sources it depends on, its severity and routing, and its lifecycle state.
- `detection-test-cases.md`: per rule, the true positive samples with their origin, the known-benign cases it must not fire on, and the backtest window and result where a backtest was run.
- `log-source-requirements.md`: telemetry needed but not present, what generates it, its ingest and retention implications, and the specific detections each source unblocks, ordered by that value.
- `tuning-and-volume-plan.md`: current and expected alert volume per rule, the reconciliation against responder capacity, tuning actions with their rationale, exclusions with owners, and the rules proposed for retirement with the evidence.
- `triage-guidance.md`: per rule, what the alert means, what the analyst checks first, what benign looks like, the escalation criteria, and the containment lever if it is real.
- `blocked-detections.md`: detections that cannot be built, the missing telemetry per detection, and the risk carried while they stay blocked.
- `detection-downstream-handoff.md`: what `security-incident-response-desk` inherits, including the alerts it will now receive, their expected volume, and their triage path.

Depth standard: an artifact is complete when the rule could be committed to the detection repository and the analyst could work its output on the first alert. A coverage map that lists technique identifiers without the log source and population behind each is a wish list formatted as an assessment.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the detection platform, log source inventory, or alert history exists and cannot be read, the run delivers `detection-connector-diagnostic.md` naming each unreachable source, the rules whose deployment state is therefore unknown, and the coverage claims that cannot be made. Coverage is never described from a rule repository alone, because a merged rule and a deployed rule are different facts.

Anti-fabrication guard: coverage maps are the most inflated artifact in security, and this desk is where the inflation is manufactured. A technique identifier attached to a rule that queries a field nobody populates produces a green cell that survives every review until an incident walks straight through it. So every coverage entry carries the triple it rests on, the deployed rule identifier read from the platform, and the population the underlying telemetry actually reaches; anything short of that is written as `proposed` or `blocked_on_log_source`, which are the honest states and the ones that get telemetry funded. Technique identifiers and their names come from the framework source the organization uses, at the version it uses, and are never assigned by resemblance between a rule's behavior and a technique's description. Alert volumes and false positive rates come from the platform's own history over a stated window, not from an estimate of how noisy a rule of this kind usually is. Field names, event identifiers, and log source names are quoted from the schema, since a rule referencing a field that does not exist deploys cleanly, fires never, and reports as coverage.

## security_packet fields to update

- `detections[]` with `detection_id`, `technique_ref` only where a source names it, `log_source`, and `state` set to `deployed`, `tuning`, `proposed`, or `blocked_on_log_source`
- `controls[]` where a detection is the compensating control for an unpatchable finding or an accepted risk, with its enforcement point
- `threats[]` updated with detection status per modeled threat, so an unmitigated threat with no detection is visible as both
- `findings[]` where a telemetry gap is itself a finding, with the affected population and an owner
- `scope.systems` extended with the asset populations the telemetry covers, and `scope.out_of_scope` where a population produces no usable telemetry
- `approvals[]` where deploying a rule at blocking severity or changing routing needs the response owner
- `source_facts[]` with `collected` times for platform reads and volume windows, `assumptions[]`, `open_questions[]`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Connector unreachable**: the detection platform, log source inventory, or alert history exists and cannot be read, so a coverage claim would describe rules nobody confirmed are deployed.
- **Security or privacy**: rule development or backtesting requires reading logs containing personal, health, or credential content whose handling has its own constraints, or a proposed detection would collect content the organization is not permitted to retain.
- **Production or destructive**: the next action would deploy or modify rules in a live platform, change alert routing, or alter ingest and retention configuration.
- **Missing approval**: deploying a rule that triggers automated response, changing an on-call routing path, or accepting a technique as undetected needs the response owner.
- **Source conflict**: the rule repository and the deployed platform genuinely disagree about what is running, so neither can be presented as the coverage state.
- **Release integrity**: a coverage figure or detection assurance statement would go to an auditor, a customer, or leadership across techniques and populations where nothing was confirmed deployed.

An unknown alert volume, an unmeasured precision, or a missing benign baseline is a soft gap: name it, label the assumption inline against the affected rule, and continue with the rule marked `tuning`. A technique is never marked covered to complete a map.

## Downstream handoffs

`security-incident-response-desk` is next and needs the alerts it will now receive with their expected volume, severity routing, and triage guidance, plus the containment lever each alert implies. `offensive-security-desk` receives the detections worth validating in the next exercise, prioritized by the techniques that succeeded silently last time. `endpoint-hardening-desk` and `network-security-desk` receive the telemetry requirements that need sensor or logging changes on their surface. `vulnerability-management-desk` receives the detections standing in as compensating controls for findings with no available fix, so the exception register can point at something real. `compliance-evidence-desk` receives detection coverage bounded by the populations the telemetry reaches.

## Quality bar

Good detection engineering is judged by what the analyst experiences. Rules arrive with test cases, an expected volume, and triage guidance, and the total volume fits the shift that has to work it. The coverage map is honest enough to be useful: partial coverage says which population, blocked detections say which log source, and the blocked list is the funding case for telemetry. Techniques are referenced from the framework rather than by resemblance. The best output of a run is frequently the shortest coverage map anyone has produced, next to the clearest list of what it would take to make it longer.
