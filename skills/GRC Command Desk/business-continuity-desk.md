---
name: business-continuity-desk
description: build and evidence business continuity and disaster recovery across business impact analysis with criticality tiers, committed rto and rpo kept separate from demonstrated recovery, dependency mapping including third parties, plan currency and approval state, exercise plans by type and scope, exercise results including what failed, and corrective actions carried into remediation. use for bia work, recovery objective review, tabletop and failover exercise planning, restore testing, plan approval reviews, and continuity evidence for auditors or customers.
---

# Business Continuity Desk

## Suite workflow mode

This desk is a member of the GRC Command Desk suite. Complete the continuity artifact set, update the `grc_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance statement asserted on evidence that cannot carry it, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the process or plan it affects, and record it in `open_questions`. Never invent recovery times, recovery point values, criticality tiers, exercise dates, exercise results, plan approval dates, or restore success figures.

## Role

Own the difference between what the organization has promised about recovery and what it has demonstrated. This desk runs the business impact analysis that produces criticality tiers from impact over time rather than from opinion, maps dependencies including the third parties inside the chain, records committed recovery objectives against the commitment that created each one, keeps demonstrated recovery from the last exercise in a separate field that is never merged with the commitment, tracks plan currency and approval, scopes exercises by type and records what failed in them, and carries corrective actions into remediation.

Two values look alike in every continuity report and mean completely different things. The committed recovery time objective is a promise, usually written into a contract or a policy by someone who did not run the recovery. The demonstrated recovery time is a measurement from an exercise, and it is the only one an assessor, a regulator, or an outage will accept. Collapsing them is the defining failure of this domain, and it is comfortable to do because the committed value is always the more attractive number.

## Use when

- A business impact analysis is being run or refreshed, or criticality tiers need deriving from impact over time rather than from who argued hardest.
- Recovery objectives need setting, reconciling against contractual and regulatory commitments, or reporting.
- A continuity or disaster recovery plan needs review for currency, approval, and whether it names people who still work here.
- An exercise is being planned, or an exercise has run and its results including failures need recording.
- Backup and restore capability needs evidencing, where the evidence is a completed restore rather than a successful backup job.
- A customer, assessor, or regulator has asked whether recovery commitments are met and the answer needs a demonstrated basis.
- A dependency map needs building or extending into third parties whose own recovery times sit inside the organization's.

## Do not use when

- The subject is engineering the recovery capability itself: replication topology, failover automation, service objectives, or incident command. That belongs to the reliability suite; this desk keeps whether the commitment is evidenced.
- The subject is responding to a live disruption. That is incident command in the reliability suite, and this desk consumes its timeline afterward as exercise-equivalent evidence where the disruption genuinely tested recovery.
- A continuity gap has become a finding needing classification and a corrective action plan. That is `exception-remediation-desk`, which receives the exercise corrective actions from here.
- The subject is a vendor's own continuity posture and contractual exit assistance. That is `third-party-risk-desk`, whose dependency output enters here.
- The subject is a control test conclusion over an observation period. That is `control-testing-desk`; an exercise result is evidence for it, not a substitute.

## Required evidence

- Business process inventory with the products or services each supports and the customers each affects.
- Impact analysis inputs measured over time rather than as a single figure: revenue at risk per interval, contractual penalties, regulatory reporting deadlines that keep running during an outage, customer harm, and reputational exposure.
- Dependency map covering applications, data stores, infrastructure, facilities, people with irreplaceable knowledge, and the third parties in the delivery path with their own recovery commitments.
- Contractual and regulatory recovery commitments quoted from the executed instruments that contain them, since the number in the plan and the number in the contract are frequently different.
- Existing continuity, disaster recovery, and crisis management plans with their version, approval date, and approver.
- Exercise history: date, type, scope, participants, injects, measured outcomes, and the failures observed rather than only the outcome summary.
- Backup configuration and restore test records, distinguishing backup job success from a completed and verified restore.
- Crisis roles, succession, and contact currency.

## Workflow

**Outcome.** A business impact analysis producing criticality tiers with the impact basis behind each, a dependency map extending into third parties, a recovery objective register keeping committed values and their source separate from demonstrated values and their exercise, plan currency and approval state per plan, an exercise plan and exercise results including failures, and corrective actions with owners.

**Grounding.** Contracts, regulatory instruments, and approved policies are authoritative for committed recovery objectives, and the commitment is quoted with the instrument that contains it. Exercise records and real disruption timelines are the only authoritative source for demonstrated recovery. A plan document is authoritative for intent and for who approved it, never for capability. Backup job telemetry is authoritative for whether data was copied and says nothing about whether it can be read back into a working service, which is a separate measurement with a separate date.

**Constraints.** Every critical process carries a criticality tier with the impact basis and the interval at which impact becomes material, because a tier assigned without a time dimension cannot order a recovery sequence. Committed recovery time and recovery point objectives are recorded with the commitment that set each; where the contract and the internal plan differ, both readings are kept and the conflict is surfaced rather than averaged. Demonstrated recovery is recorded from the last exercise with that exercise's date, type, and scope attached, and `never_tested` is used wherever no exercise measured it. Exercise type is stated precisely, since a tabletop, a functional exercise, and a full interruption test produce different classes of evidence and only the last two measure a recovery time. Exercise scope names what was in and what was excluded, because an exercise that excluded the authentication dependency did not test the recovery of anything that needs it. Failures observed during an exercise are recorded as results rather than as lessons, and an exercise where everything went well is examined for whether it exercised anything. Plan currency covers version, approval date, approver, next review, and whether the people and contacts named in it are current. Dependency chains extend through third parties, and a process cannot claim a recovery time shorter than the longest committed recovery time in its own dependency chain.

**Parallel surface.** Individual business processes, individual plan reviews, individual dependency traces, and individual exercise result write-ups fan out and are parallel-safe; each rests on its own process, plan, and exercise record. The criticality tier ranking across the process inventory, the recovery sequence built from interdependency, the aggregate resource contention where several processes claim the same recovery team or the same restore capacity at the same hour, the concentration of processes on one dependency, and the organization-wide gap between committed and demonstrated recovery are single passes over the whole set after the fan-out returns.

**Acceptance bar.** A recovery lead could sequence a recovery from the artifacts without asking what depends on what, and an assessor could distinguish every committed value from every demonstrated value without reading a footnote. Every criticality tier names its impact basis and interval, every recovery objective names its source, and every demonstrated value names the exercise that produced it.

## Outputs

A complete run delivers this set:

- `business-impact-analysis.md`: per process, impact over time with the intervals at which it becomes material, the criticality tier derived from it, the rubric applied, and the participants who provided the impact inputs.
- `dependency-map.md`: per critical process, its applications, data, infrastructure, facilities, key people, and third parties, with each third party's own committed recovery time carried into the chain.
- `recovery-objectives.md`: per process, committed recovery time and recovery point objectives with the instrument that set each, demonstrated values with the exercise that produced each, and the gap between them stated plainly, including `never_tested` where it applies.
- `plan-inventory.md`: per plan, version, owner, approver, approval date, next review, scope, and whether named roles and contacts are current.
- `exercise-plan.md`: exercises by type and scope, what each is designed to measure, the participants and injects, the success criteria set before the exercise runs, and the schedule against tier.
- `exercise-results.md`: per exercise, the date, type, scope with exclusions named, measured recovery times, what failed and at what point, decisions taken under pressure, and the evidence retained.
- `continuity-corrective-actions.md`: findings from exercises and plan review with owners, dates, and the evidence that will close each.
- `continuity-downstream-handoff.md`: what `regulatory-change-desk` and the reporting stages inherit, including recovery commitments that appear in customer contracts and regulatory filings and the evidence position behind each.

Depth standard: an artifact is complete when a recovery could be run from it during an outage by someone who did not write it, and when an assessor could trace every reported recovery figure to either a contract or an exercise. A plan whose recovery steps are titles rather than actions is a table of contents for a capability nobody has demonstrated.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when exercise records, backup and restore telemetry, or the plan repository cannot be reached, the run delivers `continuity-connector-diagnostic.md` naming each unreachable source and the recovery claims that therefore cannot be evidenced. A recovery capability is never described from a plan document alone.

Anti-fabrication guard: continuity documentation invites a specific substitution, the plan standing in for the proof. The plan says four hours, so four hours goes in the report; the backup job succeeded every night, so the data is recoverable; the tabletop went smoothly, so the failover works. Every one of those sentences replaces a measurement with an intention, and the replacement is only discovered during an actual outage, in front of the customers the commitment was made to. So committed and demonstrated recovery live in separate fields that are never merged, `never_tested` is written wherever nothing measured a value, a backup success rate is reported as a backup success rate and never as a restore capability, and an exercise result carries the scope that was excluded from it so a partial test cannot read as a full one. Exercise dates, participants, and measured times are transcribed from the exercise record; where no record exists, the exercise is recorded as undocumented rather than reconstructed from what people remember. A recovery time reported as met without an exercise behind it is the assertion that ends up in a contract, a filing, and eventually a dispute.

## grc_packet fields to update

- `continuity[]` with `process`, `criticality_tier`, `committed_rto` and `committed_rpo` each carrying the commitment that set it, `demonstrated_rto` or `never_tested`, `plan_ref`, `plan_approved_on`, the full `last_exercise` block including `type`, `scope`, and `result` with failures named, and `corrective_actions`
- `risks[]` for unevidenced recovery commitments, single points of failure, dependency concentration, and gaps between committed and demonstrated values, stated as consequences on the named scale
- `findings[]` where an out-of-date plan, an unapproved plan, an untested critical process, or an exercise failure is a deficiency with an owner and a due date
- `remediation[]` for exercise corrective actions with the evidence that will close each
- `third_parties[]` updated where a vendor's own recovery commitment bounds a process recovery time
- `obligations[]` where a contract or regulation creates a recovery commitment the register did not carry
- `evidence[]` for exercise records, restore test results, and plan approvals, with `period_covered` and `collected_on`
- `approvals[]` for plan issuance, tier assignment, accepting an untested critical process, and any exercise that touches production
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: a recovery commitment would be reported as met on the strength of a written plan rather than an exercise result. That statement sits in customer contracts, regulatory filings, and questionnaire answers, and it is relied on by people making continuity decisions of their own. `never_tested` is a legitimate value here; a plausible recovery time is not.
- **Production or destructive**: the next action would run a failover, a restore into a live environment, a full interruption test, or any exercise with production impact. Those are scheduled and authorized, not initiated from an assessment.
- **Missing approval**: issuing or reissuing a plan, assigning a criticality tier that changes recovery investment, changing a committed recovery objective, or accepting a critical process as untested each transfers exposure and needs the accountable executive at the authority level the rubric sets.
- **Source conflict**: the contract, the policy, and the plan genuinely disagree on a committed recovery objective. The contractual value is the one the organization will be held to, and the disagreement is recorded and routed rather than resolved toward the internal number.
- **Security or privacy**: exercise evidence would pull customer data, personal data, or credential material into the artifact, or a restore test would place regulated data in a non-production environment without the controls its classification requires.
- **Connector unreachable**: the exercise record, restore telemetry, or plan repository exists and cannot be read, so a demonstrated recovery figure would describe an exercise nobody confirmed happened.

A missing impact input, an undocumented dependency, or an unnamed crisis role is a soft gap: name it, label the assumption inline against that process, and continue with the tier recorded as provisional.

## Downstream handoffs

`regulatory-change-desk` is next and needs the recovery commitments that come from regulatory instruments, so a change to those instruments lands on the processes it affects. `exception-remediation-desk` receives exercise corrective actions and plan deficiencies as findings with owners and closure evidence. `third-party-risk-desk` receives the dependency positions where a vendor's own recovery commitment bounds an internal one, and where exit assistance obligations matter. `control-testing-desk` receives exercise and restore evidence for controls whose objective is recoverability. `attestation-reporting-desk` receives the evidenced recovery position, since continuity questions are among the most common in customer questionnaires and the answer has to match the exercise record. `committee-reporting-desk` receives the committed-against-demonstrated gap across critical processes, which is the continuity metric a governing body can actually act on.

## Quality bar

Good continuity work reads as measurement rather than as intention. Tiers come from impact over time, so the recovery sequence has a defensible order. Committed and demonstrated values sit side by side, so the gap is a visible piece of work rather than a discovery made during an outage. Exercises name their exclusions, so nobody mistakes a scoped test for a full one, and exercise write-ups record what failed, because an exercise that produced no failures usually tested nothing. Dependency chains run through third parties, so no process claims a recovery time shorter than the vendor it cannot function without. The strongest output of a run is often the list of critical processes marked never tested, ordered by the size of the promise attached to each.
