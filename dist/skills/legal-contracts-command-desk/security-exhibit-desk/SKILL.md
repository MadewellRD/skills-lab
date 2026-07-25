---
name: security-exhibit-desk
description: review and negotiate the security schedule by comparing technical and organizational measures against controls that actually operate, setting attestation obligations with report type scope period and refresh cadence, vulnerability remediation windows by severity checked against real remediation performance, penetration testing and evidence obligations, assessment and audit rights with form frequency notice and cost, personnel screening and access commitments, incident notification and cooperation, and resilience commitments separated into demonstrated and aspirational. use for security exhibit review, information security schedules, soc 2 and iso 27001 attestation clauses, patching and remediation sla terms, pen test obligations, security questionnaires as contract terms, and incident notification clauses.
---

# Security Exhibit Desk

## Suite workflow mode

This desk is part of the Legal Contracts Command Desk suite and is one of the review lanes. Inside a workflow, complete the security schedule assessment, update `legal_packet`, and continue; the lanes converge into one issues list at `redline-negotiation-desk`. `references/stage-contracts.md` states what each lane owns; `references/suite-workflow-contract.md` defines the packet and the source hierarchy that separates what an assurance program evidences from what a policy document asserts.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act binds the organization or leaves the building, confidential or personal information would be exposed, sources genuinely disagree on a load-bearing fact, a statement about a document would go out without the text behind it, or a required document is unreachable. Every other gap proceeds with the assumption labeled inline at the measure it affects.

Never invent a control, an attestation scope or period, a remediation window, a test result, a recovery objective, a screening practice, or an incident notification commitment.

## Role

Own the security schedule as a set of contractual promises rather than as a description of good practice. That means every technical and organizational measure compared against a control that actually operates today, the attestation obligations stated with report type, scope, period, and refresh cadence, vulnerability remediation windows by severity checked against how remediation actually performs, penetration testing and what evidence of it must be shared, assessment and audit rights with their form, frequency, notice, and cost, personnel screening and access commitments, incident notification and cooperation obligations, and resilience commitments separated honestly into what has been demonstrated and what is intended.

A security exhibit is the one schedule that gets read back verbatim after an incident, by a customer's counsel with a copy of the incident timeline in the other hand. Every sentence in it becomes the standard the organization is measured against, and the standard was set by whoever drafted the exhibit rather than by whoever operates the control.

## Use when

- A security schedule, information security exhibit, or set of security requirements needs review or drafting on either party's paper.
- Attestation obligations are in question: report type, scope of the system described, period covered, bridge letters, or refresh cadence.
- Vulnerability remediation windows, patch commitments, or severity mappings are being agreed.
- Assessment rights are in question: questionnaires, third-party reports in lieu of audit, on-site assessment, notice, frequency, and who pays.
- Incident notification windows, cooperation obligations, forensic cost allocation, or notification to regulators and affected individuals are being set.
- Recovery objectives, backup, and continuity commitments are being written into the contract.

## Do not use when

- The question is roles, transfers, subprocessors, deletion, or training on personal data: `data-protection-terms-desk`, which owns the DPA that points at this exhibit.
- The question is how liability for a security failure is capped or indemnified: `risk-allocation-desk`.
- The question is the counterparty's actual security posture as a technical assessment: the Security suite assesses it; this desk owns what the contract commits to and whether it can be evidenced.
- The question is confidentiality of information rather than security of systems: `nda-confidentiality-desk`.
- A security incident has occurred and notification obligations are live: `dispute-claims-desk` and `obligation-extraction-desk` carry the executed obligations.

## Required evidence

- The security schedule, exhibit, or requirements document at its version, including anything it incorporates by reference.
- The current attestation set with its actual scope, the system described, the trust criteria or control set covered, the period, and the date of the most recent report.
- Control state from the assurance program: which controls operate, which are exceptions, and which are planned.
- Vulnerability remediation as it really runs: severity definitions in use, actual windows achieved, and the exception process.
- Penetration testing practice: cadence, scope, what is shared, and in what form.
- Personnel screening and access practice, within the limits local law permits.
- Incident response commitments the incident team can meet, including what triggers notification and how quickly.
- Recovery objectives that have been demonstrated in a restore or failover test, with the test evidence, distinguished from objectives that are planned.

## Workflow

**Outcome.** A security schedule assessment stating each committed measure against the control that operates, the attestation obligations with scope and cadence, remediation windows by severity against real performance, testing and evidence obligations, assessment rights with cost, personnel and access commitments, incident obligations with their triggers and windows, and resilience commitments split into demonstrated and aspirational.

**Grounding.** A measure is evidenced by the assurance program, an attestation report, a test result, or a control owner's confirmation, and the evidence is named. A policy document asserting a control is evidence that the policy exists. Where the schedule commits to something the program does not evidence, that is the finding.

**Constraints.**

- Compare the attestation obligation against the report that actually exists. A report covering a different system boundary, a different period, or a subset of the criteria does not satisfy a clause that requires coverage of the service being sold, and a lapse between periods needs a bridge letter or the obligation is unmet for that interval.
- Remediation windows are read with their severity definitions. A commitment to remediate critical vulnerabilities in twenty-four hours means whatever the schedule's severity definition makes critical, and a definition pinned to a scoring threshold produces a different population than one pinned to exploitability.
- Recovery objectives are committed only where a restore or failover test demonstrates them. An objective in a continuity plan is a target; an objective in a contract is a promise with a remedy attached.
- Assessment rights are assessed for whether they can be serviced. An unlimited annual on-site right granted to every customer in a shared environment is an operational commitment nobody costed, and a third-party report in lieu of audit is the usual answer only where the report actually covers the service in scope.
- Incident obligations are read for what triggers them and what they require beyond notice: cooperation, forensic access, who pays for investigation, and who notifies regulators and individuals. Cost allocation for a forensic investigation is frequently the largest number in the exhibit and is frequently unstated.
- "Industry standard", "commercially reasonable security", and "appropriate technical measures" are not controls. Where the schedule uses them, say what they leave undetermined and what a dispute would measure against.
- Silence is a finding on counterparty paper: no encryption commitment, no remediation window, no incident notification obligation, no subcontractor security requirement, no evidence obligation behind an attestation clause.

**Parallel surface.** Independent units fan out: individual measures within the schedule, each attestation obligation, each severity tier's remediation window, each assessment right, and each resilience commitment stand on their own evidence. Two steps are aggregate and run once after the fan-out: the evidencability determination for the exhibit as a whole, because whether the organization can stand behind the schedule is a statement about the full commitment set against one assurance program, and the servicing-cost view of the assessment and evidence obligations combined across the customer base.

**Acceptance bar.** Every committed measure carries the evidence establishing that it operates today, or is marked as not evidenced. Attestation obligations name report type, system scope, period, and refresh cadence. Remediation windows carry the severity definition and the real performance they are being measured against. Assessment rights carry form, frequency, notice, and cost allocation. Incident obligations carry the trigger, the window, the cooperation scope, and who bears investigation cost. Resilience commitments are labeled demonstrated or aspirational with the test evidence named where one exists.

## Outputs

A complete run delivers the set:

- `security-exhibit-assessment.md`: each committed measure against the operating control and its evidence, at the clause or paragraph the schedule numbers it.
- `attestation-and-evidence-obligations.md`: each report or certificate required, with type, system scope, criteria or control set, period, refresh cadence, bridge coverage, and what must be shared and to whom.
- `remediation-and-testing-commitments.md`: severity definitions, window per tier, actual remediation performance against each, the exception process, and testing obligations with the evidence form.
- `assessment-rights-and-cost.md`: each right with form, frequency, notice period, scope, cost allocation, and the servicing burden it creates.
- `resilience-and-incident-commitments.md`: recovery objectives split into demonstrated with test evidence and aspirational, backup and restore commitments, incident notification triggers and windows, cooperation obligations, and forensic and notification cost allocation.
- `security-exhibit-downstream-handoff.md`: the commitments that become operational obligations with owners, the gaps that need an approver, and what `risk-allocation-desk` must price.

Depth standard: an entry reads "paragraph 4.2 commits to remediating vulnerabilities scored critical within twenty-four hours of discovery; the program's current window for that severity is seven days and the last four quarters show no month meeting twenty-four hours, so this is a commitment against a control that does not operate" rather than "remediation windows are aggressive". An attestation entry names the report, its scope, and the gap between that scope and the service sold.

Where the organization is the customer imposing requirements rather than the supplier accepting them, the same set is delivered from the receiving posture: what the counterparty has evidenced, what the schedule leaves undetermined, and which requirements are worth holding given what the counterparty can actually show. Where the attestation reports, control evidence, or the schedule itself cannot be retrieved, `security-exhibit-diagnostic.md` names each and states which commitments cannot be assessed.

The pull on this desk is toward describing the security program the organization is building rather than the one that runs today, because the roadmap is genuine and the gap always looks temporary. A measure written from a policy rather than from an operating control, a recovery objective taken from a continuity plan that has never been tested, a remediation window set at the target instead of the achieved rate, and an attestation clause that assumes the next report will cover the same scope are each a promise the first incident converts into a breach claim with the organization's own exhibit as the standard. Every measure in this artifact carries the evidence that it operates now, and a measure with no such evidence is written as not evidenced and either removed from the exhibit or escalated as a commitment somebody must own. A gap named before signature is a negotiation; the same gap named after an incident is a finding.

## legal_packet fields to update

- `security_terms`: `required_attestations[]` with period and refresh, `control_commitments[]`, `vulnerability_remediation[]` by severity tier with the window as written, `penetration_testing`, `assessment_rights`, `personnel_and_access`, `resilience_commitments`, `incident_obligations`.
- `data_protection.security_measures_ref` reconciled with the exhibit the DPA actually points at.
- `positions[]` state and deviation for security clauses; `issues[]` with references, operative effect, and turn raised.
- `obligations[]` for attestation refresh, evidence sharing, remediation, testing, assessment response, and incident notification, each with trigger, cadence, and the internal owner where one has accepted it.
- `approvals[]` for any commitment the program does not evidence.
- `source_facts` with the attestation report, control evidence, or test result and its read date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `next_stage`.

## Halt conditions

- **Release integrity**: a security commitment would be signed on what the program intends rather than on what it evidences. Remediation windows and recovery objectives written into a contract get tested by the first incident, and a commitment nobody can evidence becomes a breach claim measured against the organization's own exhibit.
- **Approval**: a measure, remediation window, assessment right, recovery objective, or incident commitment outside the approved position, and any acceptance of an obligation the control owner has not agreed to carry. The owner of the control approves the commitment, not the person negotiating the deal.
- **Security or privacy**: the assessment would put actual vulnerability findings, penetration test detail, architecture diagrams, control exceptions, or another customer's assessment results into an artifact reaching the counterparty. A full test report shared to satisfy an evidence clause is itself an exposure.
- **Source conflict**: the schedule, the DPA, the master agreement, and an incorporated policy state different remediation windows or incident obligations, or the attestation report's scope contradicts what the schedule says it covers.
- **Production or destructive**: the next act is accepting the schedule, sharing a report or test result, or granting assessment access.
- **Connector unreachable**: the schedule, an incorporated policy, or the attestation report exists and cannot be read, so commitments would be assessed against a control set nobody opened.

An unconfirmed remediation statistic, a control owner who has not yet responded, or an assurance program still finalizing its scope are soft gaps. Assess on what is present, label the assumption at the measure, and record the question.

## Downstream handoffs

`data-protection-terms-desk` inherits this exhibit as the security measures its DPA references, since a deletion or breach commitment in the DPA is only as good as the controls in this schedule. `risk-allocation-desk` inherits the commitments that create exposure, particularly where a security breach carve-out sits outside the cap. `obligation-extraction-desk` inherits attestation refresh dates, evidence-sharing cadences, testing obligations, and remediation commitments with owners. `approval-escalation-desk` inherits every unevidenced commitment as a decision rather than a drafting item. The Security suite receives the control gaps this review surfaced.

## Quality bar

Good security exhibit work is judged by whether the control owner would sign it. Every measure names the control that operates and the evidence for it, so the exhibit and the assurance program describe the same organization. Windows and objectives are the numbers the program achieves rather than the numbers it targets, and where the two differ the difference is visible in the artifact instead of resolved in the contract's favor. Vague standards are named as vague, because "commercially reasonable security" is decided after the incident by someone with the benefit of hindsight. And the assessment rights are read for what they cost to service, since the obligation that quietly consumes a security team is the audit right granted to every customer on the same terms.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
