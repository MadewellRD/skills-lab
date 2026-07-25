# GRC Stage Contracts

One entry per desk in the GRC Command Desk suite. Use these when running the suite as a continuous program of work, so a desk can carry work into the next stage instead of telling the user to invoke another skill.

## Stage order

```text
compliance-obligations-desk
  -> compliance-scoping-desk
  -> control-framework-crosswalk-desk
  -> risk-register-desk
  -> policy-lifecycle-desk
  -> control-design-desk
  -> audit-readiness-desk
  -> evidence-collection-desk
  -> control-testing-desk
  -> continuous-control-monitoring-desk
  -> exception-remediation-desk
  -> third-party-risk-desk
  -> business-continuity-desk
  -> regulatory-change-desk
  -> internal-audit-desk
  -> audit-engagement-desk
  -> attestation-reporting-desk
  -> committee-reporting-desk
```

The order is a dependency chain, not a mandatory itinerary. Most engagements run a subsequence and enter partway: an auditor request list enters at `evidence-collection-desk`, a customer questionnaire enters at `attestation-reporting-desk`, a new regulation enters at `regulatory-change-desk` and pushes backward into obligations, policies, and controls. Never run a stage ahead of the packet state it consumes, and never skip a stage the source facts show is load-bearing for the requested outcome.

Each entry states the hard halt that is specific to that stage. The default posture everywhere else is to proceed with the assumption labeled inline against the control, risk, or finding it affects, per `references/halt-taxonomy.md`.

## Contracts

### compliance-obligations-desk
Requires: business description, jurisdictions and entities, data types handled, customer and industry commitments, executed contracts and their security schedules, certifications customers or regulators are asking for, existing obligation inventory.
Owns: obligation register with each entry carrying its citation, applicability determination and who made it, accountable owner, effective and reporting dates, the compliance calendar built from those dates, and framework selection driven by what is actually required rather than what is fashionable.
Hands to: `compliance-scoping-desk`.
Hard halt: approval. A determination that an obligation does not apply is a legal position the organization will be held to by a regulator or a customer, and it belongs to counsel or the accountable executive rather than to an analyst reading the text.

### compliance-scoping-desk
Requires: obligation register, system and service inventory, entity and location list, data flows and data residency, third parties in the delivery path, the criteria set or annex for the target engagement, prior report boundaries.
Owns: boundary definition and system description, criteria or annex selection with version, in-scope systems, entities, locations and people, subservice organizations with carve-out or inclusive treatment and their complementary user entity controls, exclusions with rationale and the person who set each, and the observation period with its type.
Hands to: `control-framework-crosswalk-desk`.
Hard halt: approval. Scope determines what the eventual report opines on, and customers read an exclusion as a statement about coverage whether or not the report words it that way. The accountable owner sets the boundary.

### control-framework-crosswalk-desk
Requires: selected frameworks with versions, criteria and annex text, existing control library or inherited control set, prior mappings, published crosswalks where they exist, scope boundary.
Owns: unified control library with stable identifiers and control objectives, cross-framework mapping with coverage marked full, partial, or none, the basis of every mapping recorded as published or practitioner judgment, rationalization that lets one test satisfy several criteria, and the orphan list of criteria no control currently claims.
Hands to: `risk-register-desk`.
Hard halt: source conflict. Two authoritative mappings or framework versions disagree about whether a criterion is covered, and a criterion wrongly marked covered is a requirement that nobody tests and nobody notices until an assessor does.

### risk-register-desk
Requires: asset and process inventory, threat and loss scenarios, incident and finding history, the org rating scales and risk appetite statement, control library, business context for impact, existing register.
Owns: risk register with each entry stated as a consequence rather than a topic, inherent and residual ratings on the org scale with the scale named, treatment decision per risk, linkage from risk to the controls that carry it, formal acceptances with approver, authority level, and expiry, risk owners, and the review cadence with overdue entries surfaced.
Hands to: `policy-lifecycle-desk`.
Hard halt: approval. Accepting a risk moves exposure onto the business, and the rubric sets which authority level can accept which magnitude. An acceptance recorded without a named approver is an unowned risk wearing the label of a decided one.

### policy-lifecycle-desk
Requires: policy hierarchy and current policy set with versions, approval authorities, obligation register, control library, review cadence, acknowledgment records, exception history.
Owns: policy inventory with status, version, approver, approval date, and next review date, drafting and revision against the obligations the policy carries, mapping from policy clause to control, workforce acknowledgment coverage reported over its population, policy exception handling, and retirement with its superseding document named.
Hands to: `control-design-desk`.
Hard halt: approval. A published policy binds the workforce and becomes the criteria that later findings are written against, so the authority named in the policy hierarchy issues it. Acknowledgments collected against an unapproved draft have to be collected again.

### control-design-desk
Requires: control library, process walkthroughs, system configuration for automated controls, owner candidates, criteria the control is meant to satisfy, risk linkage, evidence-producing systems.
Owns: control narratives written so an outsider could re-perform the control, named owner per control, operating frequency, preventive, detective, or corrective classification, automated, manual, or hybrid designation, key control determination, the evidence source and what it will produce each period, and design gaps where the described control cannot achieve its objective.
Hands to: `audit-readiness-desk`.
Hard halt: source conflict. The narrative and the process as it actually runs disagree, for example an approval the narrative places in a ticket system that has no approval step. A control designed against the wrong process is then tested against the wrong population, and the whole test is void rather than merely wrong.

### audit-readiness-desk
Requires: scope boundary and criteria set, control library with design state, evidence sources, operating history per control, prior report exceptions, target audit or certification date, remediation capacity.
Owns: gap assessment against every in-scope criterion, design versus operating readiness separated, remediation roadmap with owners and dates, the earliest defensible observation window given how much operating history each control has, point-in-time versus period-of-time implications, and the readiness verdict with the criteria that hold it back named individually.
Hands to: `evidence-collection-desk`.
Hard halt: release integrity. A readiness verdict books an audit and gets repeated to customers as a date. Declaring readiness on controls with no operating history commits the organization to a period it cannot evidence, and the correction arrives as a qualified report.

### evidence-collection-desk
Requires: control library with evidence sources, observation period, request list from the assessor or the internal test plan, access to the evidence-producing systems, retention and confidentiality constraints, prior period evidence for comparison.
Owns: request list with status per item, population extraction with the query or export that produced it, the completeness and accuracy basis for every population, evidence items carrying collection date and the period they cover, freshness and staleness flags against the observation period, storage locators, and rejected evidence with the assessor's stated reason.
Hands to: `control-testing-desk`.
Hard halt: security or privacy. Fulfilling the request as written would pull personal data, credentials, customer records, or regulated content into a shared artifact or send it outside the authorized recipient set. Over-collection is the common failure here, and a copy in a new location carries its own retention and breach exposure.

### control-testing-desk
Requires: control library, evidence with established populations, testing methodology including sampling approach and sizes, the criteria each control maps to, prior period results and known deviations, tester independence expectations.
Owns: test plan per control with objective and method, population and sample recorded with the basis for the size, attribute testing results, deviations with their nature and extent rather than a count alone, conclusion per control from the fixed vocabulary, and the tested-by and tested-on record that makes the workpaper reusable.
Hands to: `continuous-control-monitoring-desk`.
Hard halt: release integrity. A conclusion of effective would rest on a population nobody established or a sample nobody drew, and that conclusion travels into a report an external party relies on. Re-performance is the first thing an assessor does, and a hollow conclusion fails there rather than quietly.

### continuous-control-monitoring-desk
Requires: control library with automation state, telemetry and configuration sources, existing automated checks and their history, alert routing and ownership, the manual controls that are candidates for automation.
Owns: monitoring coverage map showing which controls are observed continuously and which are not, check definitions with their signal source and frequency, failure and drift detection with routing to a named owner, control health metrics computed from actual results, evidence produced as a byproduct of monitoring, and checks that are blocked on a missing signal source stated as blocked.
Hands to: `exception-remediation-desk`.
Hard halt: connector unreachable. The signal source cannot be read, and silence from a monitor nobody confirmed is running is indistinguishable from a control that is working. Coverage is the one figure in this domain that cannot be estimated.

### exception-remediation-desk
Requires: finding and deficiency population from every origin, severity rubric, control and risk linkage, remediation owners and their capacity, exception policy with authority levels, compensating control options, closure evidence.
Owns: deficiency classification against the rubric, corrective action plans with owners, dates, and the evidence that will demonstrate closure, compensating controls carrying exposure in the meantime, exceptions with approver, grant date, and expiry, aging and escalation of overdue items, and closure validation that confirms the control now operates rather than that the ticket was resolved.
Hands to: `third-party-risk-desk`.
Hard halt: production or destructive. Writing a closure or status change into the system of record alters the audit trail an assessor will read, and a closure entered before validation cannot be removed, only annotated. Prepare the entry, its evidence, and its validation basis, and stop at the gate.

### third-party-risk-desk
Requires: vendor inventory with what each holds or accesses, data classification, contracts and security schedules, attestations and questionnaire responses, the criticality tier rubric, incident and performance history, subservice organizations from the scope boundary.
Owns: tiering with the rubric named, due diligence depth matched to tier, attestation review recording scope, period, exceptions carried forward, and whether a bridge letter covers the gap to today, complementary user entity controls pushed back from vendor reports and assigned internally, required contractual clauses including audit rights, breach notification, and flow-down, ongoing monitoring cadence, concentration risk, and offboarding requirements.
Hands to: `business-continuity-desk`.
Hard halt: approval. Onboarding or continuing a vendor that holds regulated or personal data needs the data owner, plus legal or privacy review where the jurisdiction requires it. An attestation that covers a different service or an expired period is not coverage, and treating it as coverage is a decision someone has to own.

### business-continuity-desk
Requires: business process inventory, dependency map including third parties, impact analysis inputs, contractual and regulatory recovery commitments, existing continuity and recovery plans with approval dates, exercise history and results, crisis roles.
Owns: business impact analysis with criticality tiers, recovery objectives stated as committed values with their source, demonstrated recovery from the last exercise separated from the committed target, plan currency and approval state, exercise plan with type and scope, exercise results including what failed, and corrective actions carried into remediation.
Hands to: `regulatory-change-desk`.
Hard halt: release integrity. A recovery commitment reported as met on the strength of a written plan rather than an exercise result is an assertion that sits in customer contracts and regulatory filings. Never-tested is a legitimate value here and a plausible recovery time is not.

### regulatory-change-desk
Requires: obligation register, horizon sources for the relevant jurisdictions and sectors, published text of the change with its effective and enforcement dates, current control, policy, and contract state, interpretation from counsel where one exists.
Owns: change log of what was published, applicability determination for this organization, impact analysis onto named controls, policies, contracts, and vendor terms, the implementation plan sequenced against the effective date, notification to the owners whose artifacts change, and the update pushed back into the obligation register.
Hands to: `internal-audit-desk`, and back into `compliance-obligations-desk` and `policy-lifecycle-desk` where the change lands on them.
Hard halt: source conflict. The published text and the internal interpretation disagree on scope or effective date. An implementation plan built on the wrong date misses a statutory deadline, and statutory deadlines do not move because the plan was reasonable.

### internal-audit-desk
Requires: audit universe and risk assessment, the annual audit plan and its approval, engagement scope, process and control documentation, evidence access, prior findings and their closure state, independence constraints.
Owns: risk-based audit plan and engagement scoping, fieldwork with workpapers that support every assertion, findings written as condition, criteria, cause, effect, and recommendation, agreed management responses with owners and dates, rating against the org rubric, follow-up testing that validates closure independently of the owner who closed it, and the state of the audit universe coverage.
Hands to: `audit-engagement-desk`.
Hard halt: approval. Auditing work this program performed is an independence impairment, and the audit committee decides whether the engagement proceeds and how the impairment is disclosed. Independence cannot be granted retroactively once a report is issued.

### audit-engagement-desk
Requires: assessor and engagement details, agreed scope and period, request list, evidence packages, control narratives, walkthrough participants, prior report and its exceptions, management representation requirements.
Owns: request tracking with submitted, accepted, and rejected states and the assessor's stated reason for each rejection, walkthrough preparation and the record of what was demonstrated, responses to assessor questions grounded in evidence, exception and deviation handling with management response drafted for signature, draft report review against the packet, and the representation letter prepared with every assertion traced to its basis.
Hands to: `attestation-reporting-desk`.
Hard halt: release integrity. An answer to the assessor, a walkthrough statement, or a management representation would go on the record without evidence behind it. Correcting a statement already relied on is a restatement, not an edit, and it changes the assessor's view of everything else the organization said.

### attestation-reporting-desk
Requires: issued report or certificate with its scope statement and validity, the period covered, exceptions in the report, distribution constraints, customer questionnaire and trust-package requests, bridge letter requirements, surveillance and recertification dates.
Owns: attestation inventory with scope, validity, and distribution constraint, bridge or gap letters covering the interval since the last period, surveillance and recertification calendar, the customer trust package with what it may and may not include, questionnaire responses answered from the packet rather than from memory, and the record of who received what under which agreement.
Hands to: `committee-reporting-desk`.
Hard halt: security or privacy. Distributing a report, certificate detail, or trust package outside its authorized recipient set discloses control weaknesses and system architecture to parties with no confidentiality obligation. Disclosure is not retractable, and the exception list inside a report is a map for anyone who wants one.

### committee-reporting-desk
Requires: register state across risks, controls, findings, exceptions, and vendors, monitoring and test results for the period, program milestones, incident and audit outcomes, the forum's charter and reporting cadence, decisions that need committee authority.
Owns: reporting packet for the named forum, metrics with the value, its computed basis, and its as-of date, risk and control health presented against appetite rather than in isolation, escalations with what is being asked of the committee, decisions requested with the authority level each needs, and a minutes-ready record of what the committee was told.
Hands to: `grc-command-desk` for the program record, and back into `risk-register-desk` and `exception-remediation-desk` where the committee directs action.
Hard halt: release integrity. A metric or program status would go to a governing body without a computed basis. The body's decisions and its minutes then rest on it, and a corrected number after a decision is a governance failure rather than a data-quality issue.

## Packet rule

Every stage updates `grc_packet` as defined in `references/suite-workflow-contract.md` before handing off. Obligations, controls, risks, findings, exceptions, and evidence accumulate across stages and are never dropped to keep an artifact short. A row removed from a register is removed with a reason and a date, because registers are read as a history as well as a current state.
