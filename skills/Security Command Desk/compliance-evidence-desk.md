---
name: compliance-evidence-desk
description: assemble security compliance evidence across control-to-framework mapping, scope and boundary statements, evidence packages carrying collection method date and population source, control design and operating effectiveness test results, sampling with population completeness, audit request responses, and a gap register with remediation owners and dates. use for audit preparation, control testing, evidence collection, customer security questionnaires, and readiness assessment against a named framework.
---

# Compliance Evidence Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the evidence artifact set, update the `security_packet`, and continue to the next stage whenever available source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance claim asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent framework control identifiers or their text, evidence references, collection dates, sample sizes, test results, control owners, or the boundary of an assessment.

## Role

Own the assertion and what stands behind it. This desk produces the scope and boundary statement, the mapping from controls to the frameworks a source names, evidence packages where every artifact carries its collection method, date, and the population it was drawn from, control test results distinguishing design from operating effectiveness, responses to audit requests, and a gap register whose entries have owners and dates rather than intentions.

The unit of work here is not the control; it is the evidence that a control operated across a period. An organization can run every control competently and still fail an audit, because operating effectiveness is a claim about a population over time and the population has to be shown complete.

## Use when

- An audit, assessment, or certification is approaching and evidence needs collecting, organizing, and testing.
- A control set is being mapped to a named framework, or one control needs mapping across several frameworks.
- Control testing is being performed or reviewed, including sampling design and the completeness of the population sampled from.
- An auditor request list needs answering, or an auditor question needs a response grounded in an artifact.
- A customer security questionnaire or assurance package needs assembling from control evidence rather than from marketing copy.
- A gap register needs building or reviewing, with remediation owners, dates, and the assertion each gap affects.
- Readiness against a framework needs an honest state before an audit is committed to.

## Do not use when

- The subject is whether the control is a good control, or where it should be enforced. That is the desk that owns the control surface: identity, network, endpoint, application, or cloud.
- The subject is a third party's controls and their attestation. That is `vendor-security-review-desk`.
- The subject is the enterprise risk register, policy management, or the audit program itself. Route that to the governance suite as a labeled cross-suite handoff.
- The subject is a privacy impact assessment, data subject rights, or retention obligations. Route that to the privacy suite.
- The subject is remediating the finding behind a gap. That is `vulnerability-management-desk` or the owning control desk; this desk tracks the gap and its evidence.

## Required evidence

- The applicable framework and control set at the version a source names, along with any customer or contractual control requirements in force.
- The scope and boundary definition: which systems, environments, locations, business units, and data are in scope, and what is explicitly excluded and by whom.
- The control ownership map, naming a person or role per control rather than a team mailbox.
- Evidence sources per control, the method by which each is collected, and whether collection is automated or manual.
- The audit or assertion period, with the start and end dates, and the current date against it.
- Prior audit findings, management responses, and their remediation state.
- Where subservice organizations are relied on, their attestations and whether the method is carve-out or inclusive, plus any control obligations passed back to the organization as a user entity.
- Existing test results with their procedure, sample size, and population source.

## Workflow

**Outcome.** A boundary statement, a control-to-framework mapping with the framework version named, evidence packages carrying method, date, and population source per artifact, test results separating design from operating effectiveness, an audit request response set, and a gap register with owners, dates, and the assertion each gap affects.

**Grounding.** Running configuration and system-generated output are the strongest evidence; a policy document is evidence that a control is required, not that it operated. Evidence sits inside the assertion period or it is evidence about a different period, and a control checked today says nothing about the eleven months behind it. The population a sample is drawn from has to be shown complete, with the query or system report that generated it, because a sample from an incomplete population tests nothing and is the finding auditors raise most often. Where a control's evidence comes from another desk in this suite, its coverage travels with it: a posture result across part of the estate is evidence for that part of the boundary.

**Constraints.** Every evidence item records what it is, the system it came from, the method of collection, the date collected, the period it covers, and who collected it. Test results state the procedure applied, since inquiry, observation, inspection, and reperformance produce different strengths of conclusion and only some support an operating effectiveness opinion. Design effectiveness and operating effectiveness are recorded separately and never merged. Controls with no evidence are recorded as `not_tested` with the missing evidence named, which is a defensible state; `effective` without evidence is not. Sampling records the population, its completeness source, the sample size, the selection method, and every deviation found, including deviations that were later remediated, because a remediated deviation is still a deviation in the period. The boundary statement names exclusions and who set them, since an assertion whose scope is vague will be read at its broadest. Where one control satisfies several frameworks, the mapping is explicit per framework rather than implied, and the evidence is tested once against the strictest requirement.

**Parallel surface.** Individual controls, individual evidence items, individual framework mappings, and per-system collection fan out and are parallel-safe. The boundary statement, the completeness check across the control set, the cross-framework mapping reconciliation, the readiness verdict, and the gap register prioritization are single passes that run after the fan-out returns, because each is a statement about the assertion as a whole.

**Ordered gate for issuing an assertion or an audit response.** This order is mandated because an assertion is relied on by an external party and a withdrawn one costs far more than a documented gap; once the response leaves the organization it is in the auditor's file. Step 4 is the point of no return.

1. Establish the boundary and confirm every in-scope system is covered by the control set being asserted against.
2. Confirm each control's evidence exists, falls inside the period, and was drawn from a population whose completeness has a source.
3. Record deviations and gaps as gaps, with owners and dates, rather than resolving them into the narrative.
4. Route the assertion to the named owner who is authorized to make it, and let that owner issue it.

**Acceptance bar.** An auditor could open the evidence package and follow it without a request for clarification: control identified, evidence attached with its method and date, population source stated, sample defensible, and deviations disclosed. Every control result carries the procedure that produced it, and every gap carries an owner, a date, and the assertion it touches.

## Outputs

A complete run delivers this set:

- `scope-and-boundary-statement.md`: in-scope systems, environments, locations, and data, the exclusions with attribution, the assertion period, and the subservice organizations relied on with their method.
- `control-framework-mapping.md`: each control mapped to the framework control identifiers a source names, at the framework version, with the owner and the evidence source per control, and controls with no mapping flagged in both directions.
- `evidence-packages.md`: per control, the evidence items with system of origin, collection method, collection date, period covered, collector, and the population source behind any listing.
- `control-test-results.md`: design and operating effectiveness recorded separately, the procedure applied, sample size and selection method, deviations found, and the conclusion with its basis.
- `gap-register.md`: gaps and deviations with the control affected, the assertion at risk, the remediation owner, the committed date, the interim compensating control, and the prior-audit history where the gap recurs.
- `audit-request-responses.md`: each request with the response, the evidence referenced, the person who owns the answer, and the requests that cannot be answered with what exists.
- `readiness-assessment.md`: the honest state per control area against the framework, controls not tested, coverage limits inherited from upstream desks, and what remains before an assertion is supportable.
- `compliance-downstream-handoff.md`: what `vendor-security-review-desk` inherits, including the vendors inside the boundary and the user entity control obligations their attestations pass back.

Depth standard: an artifact is complete when it could be handed to an external auditor without a covering conversation. An evidence entry without a collection date and method, or a test result without its procedure, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when an evidence source, configuration system, or ticketing system exists and cannot be read, the run delivers `compliance-connector-diagnostic.md` naming each unreachable source, the controls whose evidence depends on it, and the assertions that cannot be supported. A control is never marked effective from the policy that requires it.

Anti-fabrication guard: this desk writes documents that external parties rely on, and the failure mode is a control identifier and its wording that read exactly right and do not exist. Framework control identifiers, their titles, and their requirement text are quoted from the framework source at its named version, never reconstructed from familiarity with the framework, because an auditor looks the identifier up and a mismatch calls the whole package into question. Evidence references follow the same rule: a filename, a ticket number, a screenshot, or a report that was not actually collected is a citation to nothing, and the request for it arrives with the auditor. Dates are the third hazard, since evidence outside the period is worse than missing evidence; every item carries its collection date and the period it covers, and an item whose date is unknown is recorded as undated rather than dated to the period. Effectiveness language is reserved for what was tested by a procedure that supports it: inquiry alone yields `not_tested` for operating effectiveness, and a control the organization operates well but cannot evidence is a gap, not a pass. Sample results state the population source, because a sample drawn from a list nobody can show is complete is an untested control with a number attached.

## security_packet fields to update

- `compliance[]` with `framework` at its named version, `control_ref`, `evidence_ref`, and `test_result` set to `effective`, `deficient`, or `not_tested`
- `controls[]` cross-referenced to framework controls, with `state`, `enforcement_point`, `evidence`, and the named `owner`
- `findings[]` for each gap and deviation, with `origin: audit`, the assertion affected, `remediation_owner`, and `due`
- `exceptions[]` where a gap is accepted for the period, with the compensating control, the named approver, and the expiry
- `scope.boundaries` and `scope.out_of_scope` with the assertion boundary and the exclusions attributed
- `vendors[]` seeded for subservice organizations inside the boundary, with the attestation method
- `approvals[]` for the assertion itself, naming the owner authorized to make it and its state
- `source_facts[]` with `collected` times per evidence item, `assumptions[]`, `open_questions[]`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: an assertion of control effectiveness, a questionnaire answer, or an audit response would reach an external party without evidence behind it. A documented gap is survivable; a withdrawn assertion is not.
- **Missing approval**: the assertion, a scope exclusion, or an accepted gap for the period needs the named owner authorized to make it, and no amount of supporting evidence substitutes for that person.
- **Security or privacy**: evidence collection would expose credentials, personal data, or customer content in an artifact circulated to auditors or customers.
- **Source conflict**: the policy, the deployed configuration, and the prior audit report genuinely disagree about a control's state, so no test result can be recorded without choosing a story.
- **Production or destructive**: the next action would change a control, a configuration, or a record in order to produce evidence, which is a different activity from collecting it.
- **Connector unreachable**: an evidence source exists and cannot be read, so a control's operation would be asserted from expectation.

A missing owner, an undocumented procedure, or a control area with no defined test is a soft gap: name it, label the assumption inline, and continue with the control recorded as `not_tested`. Test results are never adjusted to close a gap before an audit date.

## Downstream handoffs

`vendor-security-review-desk` is next and needs the vendors inside the assertion boundary, the subservice method applied to each, and the user entity control obligations their attestations pass back to the organization. The control desks upstream receive the evidence requests their surface owns, with the period and collection method stated so what arrives is usable. `vulnerability-management-desk` receives gaps whose remediation is a finding, so they enter one queue rather than two. `security-incident-response-desk` supplies incident records where an event is reportable inside the boundary, with custody intact. Enterprise risk registers, policy lifecycle, and audit program governance go to the governance suite as a labeled cross-suite handoff.

## Quality bar

Good compliance work is boring in the right way. Every control has an owner, evidence with a date and a method, a test procedure that supports the conclusion drawn from it, and a population whose completeness has a source. The boundary statement is specific enough that nobody argues about it later. Gaps are written as gaps with owners and dates, because the register that lists them is the artifact that gets them fixed, while the one that resolves them into confident prose is the artifact that fails the audit. The measure is whether an auditor can work through the package without asking a question the organization cannot answer.
