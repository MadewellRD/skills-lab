---
name: regulatory-change-desk
description: track and operationalize regulatory and framework change across horizon scanning of official sources, applicability determination for a published change, impact analysis onto named controls policies contracts and vendor terms, an implementation plan sequenced against the effective and enforcement dates, notification to the owners whose artifacts change, and the update pushed back into the obligation register. use for new regulations, amended rules, framework version upgrades, supervisory guidance, contractual regime changes, and compliance deadline planning.
---

# Regulatory Change Desk

## Suite workflow mode

This desk is a member of the GRC Command Desk suite. Complete the regulatory change artifact set, update the `grc_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance statement asserted on evidence that cannot carry it, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the obligation or control it affects, and record it in `open_questions`. Never invent article, section, or clause numbers, effective or enforcement dates, transition periods, applicability thresholds, framework version numbers, or an interpretation attributed to counsel.

## Role

Own what changed outside the organization and what has to change inside it as a result. This desk scans the horizon sources that matter for the jurisdictions and sectors the organization operates in, determines whether a published change applies here and on what basis, analyses its impact onto named controls, policies, contracts, vendor terms, notices and records, sequences an implementation plan against the dates the instrument itself sets, notifies the owners whose artifacts change, and pushes the result back into the obligation register so the change becomes part of the program's standing record rather than a memo.

Regulatory instruments carry several dates and they are not interchangeable. Publication, entry into force, the effective or application date, the end of a transition or grandfathering period, and the date a supervisor begins enforcing are distinct, and a plan built against the wrong one misses a statutory deadline. Statutory deadlines do not move because the plan was reasonable, and the remedy for missing one is not a corrective action plan.

## Use when

- A new or amended regulation, statute, supervisory guidance, code of practice, or framework version has been published and needs an applicability determination.
- Horizon scanning is being established or refreshed for the jurisdictions, sectors, data types, and customer segments the organization touches.
- A framework the organization certifies against has released a new version, and the delta needs mapping onto the existing control library and crosswalk.
- A contractual regime change, such as a customer's new security schedule or a regulator-driven flow-down obligation, needs treating as a change to obligations rather than as a one-off negotiation.
- An implementation plan is needed against a fixed compliance date with dependencies on policy approval, control build, contract repapering, and vendor amendments.
- The obligation register has drifted from what is currently in force and needs reconciling against the published text.

## Do not use when

- The subject is the standing obligation inventory and its ownership rather than a specific published change. That is `compliance-obligations-desk`, which this desk writes back into.
- The subject is mapping controls across frameworks once the applicable set is settled. That is `control-framework-crosswalk-desk`, which receives the new criteria from here.
- The subject is drafting or reapproving the policy text the change requires. That is `policy-lifecycle-desk`, which receives the required policy delta from here.
- The subject is a privacy impact assessment, lawful basis, data subject rights, or retention determination. That belongs to the privacy suite; this desk keeps the obligation and its deadline.
- The subject is negotiating or drafting the contract language. That belongs to the legal suite; this desk states the obligation the language has to create and by when.
- The change has already been implemented and the question is whether the resulting control operates. That is `control-testing-desk`.

## Required evidence

- The published text of the change from its official source, with its citation structure intact: the article, section, or clause numbers, and the version or amendment identifier.
- The instrument's own date set: publication, entry into force, application or effective date, transition or grandfathering provisions, and any phased obligations with their separate dates.
- Applicability criteria as the instrument states them: entity scope, material scope, territorial scope, thresholds by headcount, revenue, volume, or sector, and any exemptions or derogations.
- Delegated or implementing measures, technical standards, and supervisory guidance that fill in the operative detail, distinguished from the binding text itself.
- The current obligation register, control library, crosswalk, policy set, contract inventory, and vendor terms, so impact lands on named artifacts rather than on themes.
- Counsel or the assessor's interpretation where one exists, recorded as a source fact with the interpreter named and dated.
- The organization's own footprint: entities, jurisdictions, data types, customer segments, and services, since applicability is determined against facts about this organization.
- Horizon source list with the official publication channels for each relevant jurisdiction and sector.

## Workflow

**Outcome.** A change log of what was published with its citation and dates, an applicability determination with its basis and its determiner, an impact analysis naming every control, policy, contract, vendor term, notice, and record the change touches, an implementation plan sequenced against the instrument's own dates, owner notifications, and the obligation register update.

**Grounding.** The official publication of the instrument is authoritative for what it says, and its text is quoted rather than summarized from secondary coverage. Trade press, vendor marketing, conference material, and consultancy summaries are useful for detecting that something happened and are never the basis of a citation, a date, a threshold, or a scope statement. Counsel or the assessor is authoritative for how a requirement applies to this organization, and that interpretation is recorded as a source fact with the interpreter and the date, never as an inference the desk performed. A consultation draft, a proposed rule, and a final instrument are different documents; the first two are tracked and never planned against as though the text were settled.

**Constraints.** Every logged change carries its official citation, its version or amendment identifier, and each of its distinct dates recorded separately with the provision that sets each. The applicability determination states entity, material, and territorial scope against this organization's actual footprint, names any threshold and where the organization sits relative to it, and records who determined applicability, because a determination that a requirement does not apply is a legal position the organization will be held to. Impact analysis names artifacts: control identifiers, policy identifiers, contract references, vendor names, and record types, with the specific delta for each rather than a statement that the area is affected. The implementation plan is sequenced backward from the earliest binding date with its dependencies explicit, and where an internal step has its own lead time, such as policy approval cycles, contract repapering windows, or vendor amendment negotiation, that lead time is stated so the plan shows whether the date is reachable rather than assuming it is. Where the plan cannot reach the date, that is stated as an exposure with the shortfall named rather than compressed into an optimistic schedule. Framework version changes carry the criterion-level delta: criteria added, removed, renumbered, or reworded, with the crosswalk rows each affects. Every owner whose artifact changes is named and notified with the specific change and the date it lands on them.

**Parallel surface.** Individual published changes, individual applicability determinations, individual impacted controls, individual policies, and individual contract or vendor term reviews fan out and are parallel-safe; each rests on its own text and its own artifact. The consolidated implementation plan across changes, the reconciliation of competing deadlines against one delivery capacity, the deduplication of a single control change demanded by several instruments, the obligation register update as a whole, and the ranking of exposures by deadline proximity are single passes over the whole set after the fan-out returns.

**Acceptance bar.** An owner could start work from the impact entry that names their artifact, and counsel could review the applicability determination against the quoted text without reconstructing it. Every date in the plan traces to a provision, every impacted artifact is named by its identifier, and every requirement whose applicability is undetermined is recorded as `under_analysis` rather than resolved by the desk.

## Outputs

A complete run delivers this set:

- `regulatory-change-log.md`: per change, the instrument, official citation, version or amendment identifier, publication source, status from consultation to final, and every date it sets recorded separately with the provision behind each.
- `applicability-determination.md`: per change, entity, material and territorial scope against this organization, thresholds with the organization's position relative to them, exemptions and derogations considered, the determination, its basis, and who made it.
- `impact-analysis.md`: per change, the named controls, policies, contracts, vendor terms, notices, records, and systems affected, with the specific delta required for each and the owner of each.
- `implementation-plan.md`: work sequenced backward from the earliest binding date, with dependencies, internal lead times for approval and repapering cycles, milestones, owners, and an explicit statement where the date is not reachable.
- `owner-notifications.md`: per affected owner, what changes in their artifact, the date it binds, what they need to decide, and what this desk needs back.
- `obligation-register-update.md`: the additions, amendments, and retirements to push into the register, each with its citation, applicability, owner, and effective date.
- `crosswalk-delta.md`: for framework version changes, criteria added, removed, renumbered, or reworded, and the control library and crosswalk rows each affects.
- `regulatory-change-downstream-handoff.md`: what `internal-audit-desk`, `compliance-obligations-desk`, and `policy-lifecycle-desk` inherit, including the obligations now in scope for testing and the policies that need reissue.

Depth standard: an artifact is complete when the named owner could begin work without reading the instrument themselves, and when a reviewer could check the determination against the quoted provision. An impact analysis that says access management is affected has identified a topic; naming the control identifiers, the policy clause, and the contract schedule that change identifies the work.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the official publication, the obligation register, or the contract repository cannot be reached, the run delivers `regulatory-change-connector-diagnostic.md` naming each unreachable source, the changes whose text could not be read, and the applicability determinations that therefore cannot be made. A change is never analysed from a secondary summary standing in for the instrument.

Anti-fabrication guard: regulatory text has a shape that is very easy to imitate and impossible to guess. Article numbers, paragraph structure, transition provisions, and threshold figures all read as plausible when invented, and the invention survives every internal review because nobody in the room has the instrument open. It fails later, in front of a supervisor, and it fails as a compliance failure rather than as a documentation error. So every citation, date, threshold, and scope statement in these artifacts is quoted from the official publication that was actually read, with that source recorded; where the text was not obtained, the change is logged as `text_not_obtained` and no determination is made from its description. An interpretation is attributed only where a named person gave it on a stated date, never assembled from what a reasonable reading would suggest. A consultation draft stays labelled as a draft with its status, and an effective date is left as `unknown` rather than filled with the publication date plus the interval such instruments usually allow. `under_analysis` is the correct value for an applicability question that belongs to counsel, and it is a better answer than a determination the organization would have to defend.

## grc_packet fields to update

- `obligations[]` with `obligation_id`, `source_type`, the exact `citation`, `applies_to`, `effective_date`, `owner`, `applicability` set to `applicable`, `not_applicable`, or `under_analysis`, and `basis` naming who determined it
- `scope.criteria_set` where a framework version change alters the criteria in scope
- `crosswalk[]` for criteria added, renumbered, or reworded, with `coverage` and `mapping_basis` restated rather than carried
- `control_library[]` where a control must change to carry a new requirement, with the design state moved to `unverified` until the change is made
- `policies[]` where a policy needs revision or reissue, with `next_review_due` and `status` reflecting the change rather than the calendar
- `third_parties[]` where vendor terms need amendment or flow-down, with the clause named
- `findings[]` where the organization is already out of compliance with an instrument in force
- `risks[]` for deadlines the plan cannot reach, stated as consequences with the shortfall named
- `approvals[]` for every applicability determination, since it is a legal position, and for any plan that accepts arriving late
- `source_facts[]` with the publication read and its `collected` date, `assumptions[]`, `open_questions[]`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Source conflict**: the published text and the internal or advisory interpretation genuinely disagree on scope, threshold, or effective date. An implementation plan built on the wrong date misses a statutory deadline, and both readings are recorded and routed to counsel rather than resolved toward whichever gives more time.
- **Missing approval**: a determination that a requirement does not apply, an interpretation of an ambiguous provision, or a decision to accept arriving after a binding date is a legal position belonging to counsel or the accountable executive. An analyst reading the text is not the authority the organization will cite when asked.
- **Release integrity**: a compliance position, readiness statement, or attestation about a new requirement would go to a regulator, a customer, or a committee without the text behind it or with implementation status asserted rather than evidenced.
- **Connector unreachable**: the official publication or the register the change must be reconciled against exists and cannot be read, so the analysis would rest on a description of the instrument rather than the instrument.
- **Security or privacy**: the change analysis would require pulling personal data, customer records, or regulated content to establish applicability thresholds, where a count or a data map answers the question without the underlying records.
- **Production or destructive**: the next action would write the obligation register update, retire an obligation, or amend a policy record in the system of record. Prepare the entry and stop at the gate, because a retired obligation leaves no trace of what it required.

A missing horizon source, an unclear internal owner for an affected artifact, or an unquantified lead time is a soft gap: name it, label the assumption inline against that change, and continue with the plan drafted and the gap in `open_questions`.

## Downstream handoffs

`internal-audit-desk` is next and needs the newly applicable obligations and their dates so the audit plan covers what is now in force. `compliance-obligations-desk` receives the register additions, amendments, and retirements with citations and owners, and is the desk that owns the register afterward. `policy-lifecycle-desk` receives the policy deltas with the approval authority and the date each must be published by. `control-framework-crosswalk-desk` receives the criteria delta for version changes, including renumbered criteria whose old references will otherwise persist in every mapping. `control-design-desk` receives the control changes a new requirement demands. `third-party-risk-desk` receives vendor term amendments and flow-down obligations with their deadlines. `committee-reporting-desk` receives deadlines the plan cannot reach, with the shortfall and the decision the committee is being asked for.

## Quality bar

Good regulatory change work is dated and cited, and it is judged by whether the right person hears about it early enough to act. Each change carries the citation and every one of its dates separately, so nobody plans against publication when application is what binds. Applicability is determined against this organization's actual footprint and thresholds, with the determiner named, so the position is defensible when a supervisor asks who decided. Impact lands on named controls, policies, contracts, and vendors rather than on themes, so owners have work rather than awareness. Plans are built backward from binding dates with real lead times, so an unreachable deadline is visible while there is still time to escalate it rather than after it passes. And a change whose text was not obtained stays logged and undetermined, because the alternative is a plausible article number that nobody discovers is wrong until it matters most.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
