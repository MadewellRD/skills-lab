---
name: compliance-scoping-desk
description: define the audit boundary and system description for soc 2, iso 27001, hitrust, pci, or an internal assessment, including criteria or annex selection with framework version, in-scope systems, entities, locations and people, subservice organizations with carve-out or inclusive treatment and their complementary user entity controls, exclusions with rationale and who set them, and the observation period as point in time or period of time. use when asked what is in scope, what the system description covers, which trust services criteria or annex a apply, how to treat a cloud provider, or when the observation window should start.
---

# Compliance Scoping Desk

## Suite workflow mode

This desk is a stage of the GRC Command Desk suite. Complete the boundary definition, update `grc_packet`, and continue into the next stage when the facts to run it are present. A run that ends at "the scope should now be reviewed" is a routing note; scoping is the work. Stage sequencing is in `references/stage-contracts.md` and the packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next action would write to the system of record or the audit trail, evidence handling would create a security or privacy exposure, sources genuinely disagree on a load-bearing fact, an assurance statement would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the boundary element it affects.

Never invent a system name, entity, location, criteria identifier, framework version, subservice organization, complementary user entity control, period date, or the name of whoever set an exclusion. A boundary the sources do not establish is a proposal, and it is labeled as one.

## Role

Own the audit boundary and the system description that describes it: which systems, entities, locations, people, and data flows sit inside the assessment, which criteria or annex controls it is assessed against and at which published version, how each subservice organization in the delivery path is treated, what is excluded and on whose authority, and the observation period with its type.

Scope is the single decision that determines what the eventual report opines on. Every downstream stage inherits it. A system left outside the boundary is a control nobody designs, a population nobody extracts, and a question the customer asks after the report is issued. An exclusion is read by customers as a statement about coverage regardless of how carefully the report words it, so this desk treats scope as a governance decision with a named owner rather than as a documentation exercise.

## Use when

- An audit, certification, or attestation is being planned and the boundary, criteria set, or period has not been fixed.
- The organization must decide which trust services criteria categories, which annex controls, or which requirement set applies to this engagement.
- A cloud provider, payment processor, data center, managed service provider, or other subservice organization sits in the delivery path and needs carve-out or inclusive treatment with its complementary user entity controls identified.
- The system description needs drafting or revising, including infrastructure, software, people, procedures, and data components.
- A prior report's boundary is being extended, narrowed, or moved to a new entity, product, region, or period.
- The observation window needs to be set, or the choice between a point-in-time and a period-of-time engagement needs to be made.

## Do not use when

- The question is which requirements apply to the organization at all: `compliance-obligations-desk` sets that, and this desk consumes it.
- The criteria are fixed and the work is mapping controls onto them or finding uncovered criteria: `control-framework-crosswalk-desk`.
- The boundary is settled and the question is whether controls are ready to be tested against it: `audit-readiness-desk`.
- The subservice organization needs tiering, diligence, contract clauses, or attestation review beyond its scope treatment: `third-party-risk-desk`.
- The assessor has been engaged and the work is request tracking, walkthroughs, or draft report review: `audit-engagement-desk`.

## Required evidence

- The obligation register with the frameworks and criteria the engagement must satisfy.
- System and service inventory: production systems, supporting infrastructure, identity and access tooling, code and change pipelines, and the tools that produce control evidence.
- Legal entity list, operating locations, and workforce distribution, including contractors and where they perform in-scope work.
- Data flow and data residency documentation covering what enters the system, where it is processed and stored, and where it leaves.
- Third parties in the delivery path with what each performs and whether it touches in-scope data or controls.
- The published criteria or annex text at the version being adopted, plus any implementation guidance the assessor has issued.
- Prior reports with their boundaries, exclusions, and complementary user entity controls, and any customer commitment about scope made in contracts or sales.
- The assessor's scoping position where one exists, recorded with the assessor named.

## Workflow

**Outcome.** A defined boundary an assessor could accept and a customer could read without ambiguity: system description across infrastructure, software, people, procedures, and data; criteria or annex selection quoted at its published version; in-scope systems, entities, locations, and roles; subservice organizations each with carve-out or inclusive treatment and the complementary user entity controls that treatment pushes back to customers; exclusions with rationale and the person who set each; and the observation period with type and dates.

**Grounding.** The system and service inventory and the data flow records are authoritative for what exists and what touches in-scope data. Executed contracts and the obligation register are authoritative for what the organization committed to cover. Published criteria text is authoritative for what the criteria say, quoted at version. The assessor's scoping position is a source fact with the assessor named, not an inference. Where a system's role in the delivery path is asserted by an architecture diagram but contradicted by configuration or access records, record both readings.

**Constraints.** Draw the boundary from data flow and control dependency rather than from the org chart, because scope follows the data and the systems that protect it. Every in-scope system names why it is in scope: it processes in-scope data, it supports a control, or it grants access to something that does. Every exclusion names what is excluded, why, and who decided, and exclusions whose rationale is convenience rather than irrelevance are recorded plainly as such. Subservice treatment is stated per provider: carve-out shifts reliance to that provider's own report and creates complementary user entity controls this organization must operate, and inclusive treatment pulls the provider's controls into this engagement with the evidence obligation that follows. Complementary user entity controls inherited from a provider's report are quoted from that report and assigned to a named internal owner. Period type is a consequence, not a preference: a point-in-time engagement asserts design at a date, and a period-of-time engagement asserts operation across a window and therefore requires operating history for the whole window.

**Parallel surface.** Boundary elements are independent and fan out: systems, entities, locations, data flows, third parties in the delivery path, and criteria within the selected set are each assessed against their own evidence. Complementary user entity controls are extracted from each provider report in parallel. The aggregate passes run once after the fan-out returns: reconciling the resulting boundary against the full system inventory to find systems that are neither in scope nor excluded, computing criteria coverage of the selected set, resolving overlapping boundaries where several engagements share systems, and setting the observation period against the readiness position for the whole in-scope control set.

**Acceptance bar.** Every system in the inventory is either in scope with a stated reason or excluded with a rationale and a named decider, with no third category. Every criterion in the selected set is quoted at its published version. Every subservice organization has a treatment and, where carved out, its complementary user entity controls named and internally owned. The period has a type and dates, or is stated as unset with what blocks it. A reader could tell from the description alone whether a given customer's data is inside the boundary.

## Outputs

A complete run delivers this artifact set:

- **Scope definition**: in-scope systems, entities, locations, and roles, each with the reason it is included, plus the reconciliation against the full inventory that shows nothing was left unclassified.
- **System description**: the narrative across infrastructure, software, people, procedures, and data, written to the structure the target report expects and specific enough that an assessor could locate every component named.
- **Criteria selection**: the criteria categories or annex controls adopted, quoted at version, with the ones deliberately not adopted listed and the basis for the selection.
- **Subservice organization treatment**: per provider, the service performed, carve-out or inclusive treatment with rationale, the provider's own attestation and period where one exists, and the complementary user entity controls with internal owners.
- **Exclusion register**: each exclusion with what it removes from coverage, the rationale, who set it, and how a customer is likely to read it.
- **Observation period statement**: type, start and end dates, the constraint that set each date, and the consequence for what the report can assert.
- **Source facts and assumptions record**: every boundary fact with its source and collection date, every assumption with the boundary element it affects.

Depth standard per artifact: the system description is complete when an assessor could plan fieldwork from it without asking what a component is. "Cloud infrastructure" is a category. A description names the platform, the accounts or subscriptions, the regions, the workloads they carry, and which of them process in-scope data.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the system inventory, data flow records, or provider attestations cannot be reached, deliver the boundary limited to reachable sources and state precisely which components remain unclassified and which source would classify each. In `resume` mode, re-check the inventory for systems added since the boundary was drawn and re-check provider attestation periods for expiry, because a boundary drifts silently while the engagement is being planned.

Scoping is where plausible text does the most damage, because a system description reads as a management assertion and is signed as one. The failure to refuse here is describing the architecture the organization intends rather than the one it runs: a component named because a diagram shows it, a region listed because the platform offers it, a subservice organization treated as carved out because that is the common treatment rather than because this engagement decided it. A system, entity, location, provider, or complementary user entity control that no inventory, contract, or provider report establishes is listed as unconfirmed with the source that would confirm it, and a boundary that is honestly incomplete is returned as incomplete with the unclassified components named. The boundary is the one thing the report opines on, so every error inside it is inherited by every stage that follows.

## grc_packet fields to update

- `scope.engagement`, `scope.criteria_set[]` with framework versions, `scope.in_scope_systems[]`, `scope.in_scope_entities[]`, `scope.locations[]`.
- `scope.subservice_orgs[]` with `name`, `method` as carve_out or inclusive, and `cuecs[]`.
- `scope.out_of_scope[]` with `item`, `rationale`, and `set_by`.
- `scope.period` with `type`, `start`, and `end`.
- `approvals[]`: boundary approval and each exclusion as an action with its required authority level and state.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: the boundary, an exclusion, a criteria selection, or a subservice treatment would be fixed without the accountable owner. This is the defining halt of this desk. Scope decides what the report covers, and a customer reads an exclusion as a gap in the organization's controls whether or not that is what it means.
- **Production or destructive**: the next action would write the scope into the GRC platform, replace a prior period's system description, or amend a boundary that evidence has already been collected against. Evidence gathered under a superseded boundary does not cover what was added.
- **Security or privacy**: the system description would embed network detail, credential locations, customer identities, or architecture specifics beyond what the report's distribution allows. A system description travels further than its authors expect.
- **Source conflict**: the architecture documentation, the configuration state, and the contract genuinely disagree about whether a system or provider is in the delivery path, or the assessor's scoping position contradicts the internal one. Record both readings and route it.
- **Release integrity**: a scope statement or system description would go to an assessor or a customer while components remain unclassified or a subservice treatment remains undecided.
- **Connector unreachable**: the system inventory, data flow records, entity register, or a provider's attestation cannot be reached, so completeness of the boundary cannot be claimed over a population nobody enumerated.

## Downstream handoffs

`control-framework-crosswalk-desk` consumes the criteria set with versions and the boundary, since a crosswalk that maps controls to criteria outside the scope wastes the control library. `control-design-desk` consumes the in-scope systems and their evidence sources. `audit-readiness-desk` consumes the criteria set and the period, since readiness is measured against in-scope criteria and operating history inside the window. `evidence-collection-desk` consumes the period and the in-scope systems, which set every population boundary. `third-party-risk-desk` consumes the subservice organizations and their complementary user entity controls. `audit-engagement-desk` consumes the system description as the artifact the assessor works from.

## Quality bar

Good scoping is defensible under challenge from two directions at once: an assessor asking why something is out, and a customer asking why something they care about is not covered. The boundary follows the data rather than the reporting lines. Complementary user entity controls are pulled out of provider reports and given internal owners rather than being acknowledged and forgotten, which is where the majority of real inherited gaps live. The period is set from operating history rather than from the date the sales team promised, and where those disagree the disagreement is visible rather than absorbed. Exclusions are few, specific, and owned, and the system description names real components a stranger could go and find.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
