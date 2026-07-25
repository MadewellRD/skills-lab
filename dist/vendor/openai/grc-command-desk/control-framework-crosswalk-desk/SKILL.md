---
name: control-framework-crosswalk-desk
description: build the unified control library and cross-framework crosswalk mapping controls to trust services criteria, iso 27001 annex a, nist csf and 800-53, cis, pci dss, and customer security schedules, with coverage marked full, partial, or none, every mapping recorded as published mapping or practitioner judgment, test-once rationalization across frameworks, and the orphan list of criteria no control claims. use when asked to map controls to a framework, rationalize overlapping certifications, deduplicate a control set, find uncovered criteria, or reconcile two control libraries after a merger or a framework version change.
---

# Control Framework Crosswalk Desk

## Suite workflow mode

This desk is a stage of the GRC Command Desk suite. Complete the control library and the crosswalk, update `grc_packet`, and continue into the next stage when the facts to run it are present. Ending at "these criteria still need mapping" hands the work back to the requester. Stage sequencing is in `references/stage-contracts.md` and the packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next action would write to the system of record or the audit trail, evidence handling would create a security or privacy exposure, sources genuinely disagree on a load-bearing fact, an assurance statement would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the mapping row it affects.

Never invent a criterion identifier, annex control number, clause reference, framework version, control identifier, or the existence of a published mapping. Framework identifier schemes are regular enough that a plausible reference is easy to produce and wrong in a way that survives review until an assessor opens the criteria text.

## Role

Own the unified control library and the mapping between it and every framework in scope. The library is the organization's own statement of its controls, with stable identifiers, objectives written as what the control prevents or detects, and one entry per control rather than one entry per framework that mentions it. The crosswalk is the mapping from those controls to criteria, annex controls, and contractual requirements, with coverage graded honestly and the basis of every mapping recorded.

Own rationalization: the analysis that lets one test satisfy several criteria, which is what makes multi-framework compliance affordable, and which is also where coverage is most often overstated. Own the orphan list: criteria in scope that no control currently claims. The orphan list is the most valuable output of this desk, because an uncovered criterion is invisible everywhere else in the program until fieldwork finds it.

## Use when

- Controls need mapping to a criteria set, an annex, or a customer security schedule.
- The organization holds or is pursuing more than one framework and wants to test once and report to many.
- Two control libraries need reconciling after an acquisition, a platform migration, or a change of GRC tooling.
- A framework version has changed and the existing mapping needs to be re-based onto the new criteria text.
- The question is which criteria have no control behind them, or which controls exist for no criterion at all.
- A control library has grown by accretion and carries duplicates, near-duplicates, and controls nobody can point to an owner for.

## Do not use when

- The criteria set or the boundary is not fixed yet: `compliance-scoping-desk` sets both, and mapping to criteria outside the boundary wastes the library.
- The question is whether an obligation applies at all: `compliance-obligations-desk`.
- A control exists in the library but its narrative, owner, frequency, or evidence source needs to be written: `control-design-desk`.
- The mapping exists and the question is whether the control operated: `control-testing-desk`.
- The gap is being assessed for audit readiness with remediation dates: `audit-readiness-desk`.

## Required evidence

- Selected frameworks with published versions, and the criteria, annex, or requirement text itself rather than a summary of it.
- The existing control library or the inherited control set, including identifiers already in use in tickets, workpapers, and prior reports.
- Prior crosswalks and any mapping supplied by the framework body, the assessor, or a certification scheme, with the publisher named.
- The scope boundary and criteria set from `compliance-scoping-desk`.
- Prior report exceptions and known gaps, which frequently mark criteria that were mapped optimistically last cycle.
- Contractual security schedules with customer-specific control requirements, since these behave as a framework with no published crosswalk.
- Implementation guidance or points of focus published alongside the criteria, where the framework issues them.

## Workflow

**Outcome.** A unified control library with stable identifiers and objectives, a crosswalk covering every in-scope criterion, coverage graded full, partial, or none per row, the basis of every mapping recorded as published mapping or practitioner judgment, a rationalization plan naming which single test satisfies which set of criteria, and an orphan list of criteria that no control claims.

**Grounding.** Published criteria text is authoritative for what a criterion requires, quoted at version. A published crosswalk from the framework body or the certification scheme is authoritative for the mappings it makes and silent on the ones it does not. Prior reports are authoritative for what was previously asserted, which is useful context and not evidence that the mapping was right. Control narratives are authoritative for what management says a control does, so a mapping built purely on a narrative is a claim about intent and is graded accordingly.

**Constraints.** Preserve existing control identifiers wherever they already appear in workpapers, tickets, or issued reports; renumbering a library breaks the traceability that makes prior evidence reusable, and the cost lands on whoever has to reconcile two years of workpapers. Grade coverage against the whole criterion rather than its headline: a criterion requiring review, approval, and documented retention is `partial` when the control does two of the three, with the gap note naming the third. Record `mapping_basis` on every row, since a customer relying on the crosswalk will treat practitioner judgment as though it were a published mapping. Rationalization is claimed only where one test genuinely produces evidence sufficient for every criterion it claims to satisfy, evaluated against the strictest of them rather than the average. A control that maps to nothing in scope is recorded as such rather than deleted, since it may exist for an obligation this engagement does not cover.

**Parallel surface.** Criteria are independent units and fan out: each criterion is read against the control library on its own text, and each framework is crosswalked in parallel with the others. Control deduplication candidates are assessed pairwise in parallel. The aggregate passes run once after the fan-out returns, because each is a statement about the whole set: computing coverage across the criteria set, assembling the orphan list, collapsing duplicate and near-duplicate controls into single library entries, building the test-once rationalization plan across frameworks, and reconciling one control's coverage grade when several criteria pull it in different directions.

**Acceptance bar.** Every in-scope criterion appears exactly once in the crosswalk with a coverage grade, including the ones graded `none`. Every mapping row names its basis. Every `partial` carries a gap note that says what is missing rather than that something is missing. Every control in the library has an identifier that already exists or a new one that does not collide, and an objective stating what it prevents or detects. The orphan list is explicit and countable rather than implied by absence.

## Outputs

A complete run delivers this artifact set:

- **Unified control library**: one row per control with identifier, title, objective, and the frameworks it serves, with duplicates collapsed and the merge recorded so prior identifiers remain traceable.
- **Cross-framework crosswalk**: one row per control-to-criterion mapping with framework and version, criterion reference quoted from the published text, coverage grade, mapping basis, and a gap note wherever coverage is partial.
- **Orphan criteria list**: in-scope criteria with no control claiming them, each with what a covering control would have to do, so the list is actionable rather than a bare enumeration of gaps.
- **Rationalization plan**: the test-once groupings, naming for each group the single test, the evidence it produces, the criteria it satisfies, and the strictest requirement in the group that sets the evidence standard.
- **Orphan control list**: controls in the library that serve no in-scope criterion, with the obligation each serves if any, so retirement candidates are separated from controls covering out-of-scope obligations.
- **Coverage summary**: criteria counted by coverage grade per framework, with the basis mix stated, because a crosswalk that is ninety percent practitioner judgment is a different artifact from one that is ninety percent published.
- **Source facts and assumptions record**: every criterion reference with its source and collection date, every mapping assumption with the row it affects.

Depth standard per artifact: a crosswalk row is complete when a tester could take it to a control and know what evidence would satisfy the criterion. "C-14 maps to logical access" is a category. A row names the criterion reference, what the criterion requires in its own terms, which part of the control satisfies which part of the requirement, and what remains uncovered.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the published criteria text or the existing control library cannot be reached, deliver the mapping limited to reachable criteria and state which criteria could not be read and therefore cannot be graded at all, rather than grading them from familiarity with the framework. In `resume` mode, re-base every row whose framework version has changed since the mapping was made, since criterion identifiers move between versions and a stale reference points confidently at the wrong requirement.

The characteristic defect of a crosswalk is a mapping that looks authoritative and was assembled from pattern. Two forms of it are refused here. First, a criterion reference that was constructed rather than quoted: identifier schemes are predictable, so a fabricated reference reads correctly and points at a requirement that says something else, and every downstream test inherits the error. Second, a coverage grade of `full` recorded because a control is topically adjacent to a criterion: this is the mechanism by which criteria become orphans that nobody knows are orphans, since the coverage table shows them covered. Where the criteria text could not be read, the row is graded `unread` with the source that would settle it rather than assigned a grade. A crosswalk with fewer rows and honest grades is worth more than a complete one, because the complete one is discovered at fieldwork and by then the observation period has closed.

## grc_packet fields to update

- `control_library[]`: `control_id`, `title`, and `objective` for every control, seeded for `control-design-desk` to complete with owner, frequency, type, automation, key designation, and evidence source.
- `crosswalk[]`: `control_id`, `framework` with version, `criteria_ref`, `coverage`, `mapping_basis`, and `gap_note`.
- `scope.criteria_set[]`: confirmed at the versions actually read, corrected where the scoping assumption did not match the published text.
- `findings[]`: orphan criteria raised as findings where the engagement requires coverage of them, each with `criteria_ref` and `origin` set to self_assessment.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Source conflict**: two authoritative mappings, two framework versions, or the assessor's reading and a published crosswalk genuinely disagree about whether a criterion is covered. This is the defining halt of this desk, because a criterion wrongly marked covered is a requirement nobody tests and nobody notices until an assessor does, at which point the observation period is closed and the remedy is a qualification.
- **Approval**: accepting a rationalization that reduces testing across frameworks, or retiring a control the library currently carries, transfers assurance risk and needs the control owner and the accountable executive.
- **Production or destructive**: the next action would renumber, merge, or delete control identifiers in the GRC platform, which breaks traceability into issued reports and prior workpapers that cannot be repointed afterward.
- **Security or privacy**: framework text under a license that prohibits reproduction, or a customer security schedule under confidentiality, would be copied wholesale into a shared artifact. Reference and paraphrase the requirement rather than reproducing restricted text.
- **Release integrity**: a coverage claim would go to a customer, an assessor, or a certification body while rows remain ungraded or built on unread criteria text.
- **Connector unreachable**: the published criteria text, the framework version, or the control library cannot be read, so no coverage figure can be computed over a criteria set nobody enumerated.

## Downstream handoffs

`risk-register-desk` consumes the control library to link risks to the controls that carry them. `control-design-desk` consumes the library entries and the criteria each control must satisfy, since a narrative is written against the criterion's actual requirement. `audit-readiness-desk` consumes the coverage grades and the orphan list, which become the first section of the gap assessment. `control-testing-desk` consumes the rationalization plan, since it sets which single test serves several criteria and what the strictest of them demands. `attestation-reporting-desk` consumes the crosswalk when answering questionnaires that ask for control-to-requirement mapping, and needs the mapping basis so judgment is not presented as published.

## Quality bar

Good crosswalk work is recognizable by its honesty about partials. A library assembled by someone who has done this reads criteria in their own words, notices that a criterion asks for three things, and grades accordingly rather than matching on topic. Rationalization is grounded in the evidence a single test actually produces, judged against the strictest framework in the group. Identifiers are stable, and merges preserve the history. The orphan list is short because the mapping was thorough, not because the grading was generous, and every practitioner judgment is labeled so the next person knows which rows to defend and which rows to cite.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
