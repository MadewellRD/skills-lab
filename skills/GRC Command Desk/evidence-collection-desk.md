---
name: evidence-collection-desk
description: run the evidence and pbc request list against an observation period, extract populations with the query or export that produced them, establish the completeness and accuracy basis for every population, collect evidence carrying its collection date and the period it actually covers, flag stale and out-of-period artifacts, track custody and storage locators, and record assessor-rejected items with the stated reason. use when asked to fulfil an auditor request list, pull evidence for a control, build an evidence package, extract a user access or change population, or check whether existing evidence still covers the period.
---

# Evidence Collection Desk

## Suite workflow mode

This desk is a stage of the GRC Command Desk suite. Complete the evidence package, update `grc_packet`, and continue into the next stage when the facts to run it are present. A run that ends by listing the evidence someone should now gather has produced a request list twice. Stage sequencing is in `references/stage-contracts.md` and the packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next action would write to the system of record or the audit trail, evidence handling would create a security or privacy exposure, sources genuinely disagree on a load-bearing fact, an assurance statement would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the evidence item it affects.

Never invent an artifact, a collection date, a period covered, a population size, a query, a completeness basis, a storage locator, a custodian, or an assessor's stated reason for rejecting something. Evidence is the layer of this suite where fabrication is cheapest to produce and fastest to detect, because the assessor opens the artifact.

## Role

Own everything between a request and a testable artifact: the request list with a state per item, the population extraction with the exact query or export that produced it, the completeness and accuracy basis for every population, the evidence items themselves with collection dates and the periods they actually cover, freshness against the observation window, custody and storage, and the rejected set with the assessor's stated reason.

The two things this desk is judged on are populations and dates. A population nobody established turns every downstream sample into a number with no denominator, and it is the first thing an assessor re-performs. A date that does not cover the observation period turns a perfectly good artifact into no evidence at all. Everything else is logistics.

## Use when

- An assessor, certification body, customer, or internal audit team has issued a request list and it needs fulfilling against a period.
- A population needs extracting: user access, changes, deployments, incidents, terminations, onboarding, vendor payments, backup runs, or any other set a sample will be drawn from.
- Evidence needs gathering for a control test, a readiness assessment, or a customer assurance request.
- Existing evidence needs checking for freshness, period coverage, or completeness before it is submitted.
- Evidence has been rejected and the reason needs recording, understanding, and re-collecting against.
- An evidence repository needs organizing so a package can be handed over cold.

## Do not use when

- The observation period or the boundary is not fixed: `compliance-scoping-desk` sets both and every population inherits them.
- The control has no defined evidence source: `control-design-desk` decides what a control produces before anyone can request it.
- The evidence exists and the question is drawing a sample, testing attributes, and concluding: `control-testing-desk`.
- The evidence is produced automatically by a monitoring check with a signal source and a cadence: `continuous-control-monitoring-desk`.
- The work is coordinating with the assessor on the record: responses, walkthroughs, and question handling belong to `audit-engagement-desk`.
- The request came from a customer wanting a report or a questionnaire answer: `attestation-reporting-desk`.

## Required evidence

- The control library with the evidence source and expected artifact per control, from `control-design-desk`.
- The observation period with its type and dates, and the in-scope systems and entities from the boundary.
- The request list itself, in the requester's own wording, since a paraphrased request produces evidence that answers a different question.
- Access to the producing systems: identity provider, ticketing and change management, HR system, cloud configuration, code and deployment pipeline, log platform, backup and monitoring tooling.
- Retention configuration per producing system, because retention shorter than the observation period is a hard constraint rather than an inconvenience.
- Confidentiality, residency, and data classification constraints governing what may leave which system and enter which repository.
- Prior period evidence and prior rejections with the reasons given, which are the cheapest available guide to what this assessor will accept.

## Workflow

**Outcome.** A request list with a state per item, populations extracted with the query or export recorded and a completeness and accuracy basis stated, evidence items carrying collection date, period covered, custodian, and storage locator, freshness flags against the observation window, and the rejected set with each assessor reason recorded verbatim.

**Grounding.** System-generated records are authoritative for whether a control operated, bounded by the population they actually cover and the moment they were extracted. A screenshot is authoritative for a moment; it is not authoritative for a period, and an undated one is authoritative for nothing. Management assertions and control narratives are authoritative for what management says and are not evidence that a control operated. The requester's wording is authoritative for what was asked. Where an extract and the system disagree because time passed between them, the extract's timestamp is the fact and the drift is recorded.

**Constraints.** Record the query, filter, or export path with every population, including the time bounds and the exclusions applied, because the population is the first thing re-performed and an unreproducible extract fails at that step. State the completeness and accuracy basis explicitly: reconciliation to an independent count, a system-generated total, a record count against a control total, or unknown. Unknown is a legitimate value and a tidy-looking export is not a basis. Evidence carries the period it actually covers rather than the period it was requested for; a control operating monthly needs an artifact per month, and a single artifact is one instance regardless of what the request asked for. Requested and collected are different states and never collapse. Sensitive content stays where it lives: reference by locator, extract the attribute the test needs, and never pull personal data, credentials, or customer records into the artifact.

Evidence capture around remediation follows a mandated order, stated here so a later editor does not read it as scaffolding:

1. Capture and date the evidence of the control in its current failing state.
2. Remediate.
3. Capture and date the evidence of the corrected control operating.

The order is mandated because a period-of-time report covers the whole period rather than its final state, and remediation destroys the record of how the control operated during the period being reported on. Once the failing-state evidence is gone it cannot be reconstructed, and the organization is left unable to describe its own deficiency accurately to the assessor who will ask about it.

**Parallel surface.** Evidence requests are independent units and fan out: each item is extracted, dated, and filed against its own system on its own terms, and populations from separate systems are pulled concurrently. Freshness checks against the window run per item in parallel. The aggregate passes run once after the fan-out returns, because each is a statement about the whole package: reconciling combined populations where one sample will be drawn across several systems, deduplicating evidence serving several controls or criteria so it is submitted once, computing package completeness against the request list, sequencing collection against retention windows so the artifacts nearest to expiry are pulled first, and assembling the index a recipient reads cold.

**Acceptance bar.** Every population names its source system, its query or export path with time bounds, its size, and its completeness and accuracy basis, including where that basis is unknown. Every evidence item names what it shows, its collection date, the period it covers, its custodian, and its locator. Every request list item has a state that reflects reality. No artifact enters the package without a date. No sensitive content sits in the package that could have been referenced instead.

## Outputs

A complete run delivers this artifact set:

- **Request list tracker**: every item with the requester's original wording, the control and criterion it serves, its state as open, submitted, accepted, or rejected, the owner, and the due date.
- **Population register**: per population, the source system, the exact query or export path with time bounds and exclusions, the extraction timestamp, the record count, and the completeness and accuracy basis.
- **Evidence index**: every artifact with what it demonstrates, its control and criterion, its collection date, the period it covers, its custodian, its storage locator, and its state.
- **Freshness and coverage report**: items whose period does not reach the window, controls whose instance count falls short of what their frequency should have produced, and gaps where a producing system's retention cannot reach the window's start.
- **Rejection log**: rejected items with the assessor's stated reason recorded verbatim, what will be re-collected, and by when, since a paraphrased rejection reason produces a second rejection.
- **Custody and handling record**: what was pulled, by whom, from where, into which repository, under what classification, and what was deliberately referenced rather than copied.
- **Source facts and assumptions record**: every extraction fact with its source and timestamp, every assumption with the evidence item it affects.

Depth standard per artifact: an evidence index entry is complete when a stranger could open the artifact and see what it proves without asking. "Access review evidence, Q2" is a filename. An entry names the system, the entitlement scope, the review date, the reviewer, the number of entitlements reviewed, the number revoked, the artifact showing the revocation, and the period it covers.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where producing systems cannot be reached, deliver the request list with those items in a reachable-source state and name precisely which populations cannot be enumerated and which control conclusions each gap makes unavailable, rather than describing the evidence the system would have produced. In `resume` mode, re-pull any population whose extraction predates the current period boundary and re-check freshness on every carried item, because evidence collected for a prior window silently ages into the wrong period.

Evidence is where an overstated state costs the most, because an assessor tests it directly and immediately. Requested and collected are different states, and an item nobody has actually opened stays requested no matter how confident the requester is that it exists. A population whose completeness and accuracy nobody established is recorded with that basis unknown rather than assumed from the export looking clean, since a tidy CSV from a system with a filter applied upstream is exactly what an incomplete population looks like. A screenshot with no date is filed as undated rather than assigned the date it was requested for. The reason this discipline matters more here than the tidiness it resembles: an index that overstates its own state fails at the first item the assessor opens, and after that the assessor stops trusting the index and re-performs everything, which converts a two-week fieldwork into a two-month one and turns every other honest item into a suspect one.

## grc_packet fields to update

- `evidence[]`: `evidence_id`, `control_id`, `description`, `artifact_ref` as a locator, `period_covered`, `collected_by`, `collected_on`, `population_source` with the query, `completeness_basis`, and `state`.
- `audit_engagement.request_list`: `open`, `submitted`, `accepted`, and `rejected` with the assessor's stated reason on each rejection.
- `findings[]`: where a population cannot be established or a control produced no evidence for the period, raised against the criterion it fails.
- `control_library[]`: `evidence_source` corrected where the expected artifact does not exist or the retention does not reach the window.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Security or privacy**: fulfilling the request as written would pull personal data, credentials, customer records, health or payment data, or regulated content into a shared artifact, cross a residency boundary, or send it beyond the authorized recipient set. This is the defining halt of this desk. Over-collection is the routine failure here, and a copy in a new repository carries its own retention obligation and its own breach exposure, permanently.
- **Production or destructive**: the next action would overwrite collected evidence, replace a prior period's artifact, alter an extract, or change a control in a live system before the failing-state evidence has been captured and dated. A repaired evidence trail is worth less than a documented gap in one.
- **Approval**: releasing evidence to an external assessor, a customer, or a new repository needs the data owner, and evidence containing regulated content needs privacy or legal review where the jurisdiction requires it.
- **Source conflict**: two extracts of the same population disagree on record count or membership on load-bearing grounds, or the system record and the ticket record disagree about whether an event occurred. Record both readings against the population and route it.
- **Release integrity**: a package would be submitted with items marked collected that nobody pulled, or populations whose completeness basis is unknown presented as established.
- **Connector unreachable**: a producing system cannot be read, so the population cannot be enumerated. Evidence that is merely absent is a soft gap recorded as a gap with the control named; evidence that is unreachable is this halt, because coverage cannot be estimated from a system nobody could query.

## Downstream handoffs

`control-testing-desk` consumes populations with their completeness basis and evidence with its period coverage, and cannot draw a sample from a population whose basis is unknown without the conclusion inheriting that weakness. `audit-engagement-desk` consumes the request list states and the rejection log to manage the assessor relationship, and needs each rejection reason verbatim. `continuous-control-monitoring-desk` consumes the collection patterns that recur, since a request fulfilled manually every quarter is a monitoring check waiting to be built. `exception-remediation-desk` consumes the controls that produced no evidence for the period, which are findings whether or not the control operated. `attestation-reporting-desk` consumes the custody and classification record when deciding what may appear in a customer trust package.

## Quality bar

Good evidence work is recognizable from the population register alone. Queries are recorded well enough to re-run, with time bounds and exclusions visible. Completeness bases are specific: reconciled against a headcount extract on a stated date, against a system-generated control total, or honestly unknown. Dates are everywhere and periods are stated rather than assumed. Sensitive content is referenced rather than copied, and the record shows the deliberate decision to reference it. The rejection log is treated as the most valuable artifact in the set, because an assessor who rejects an item has just told the organization exactly what its evidence standard is, and a program that reads it carefully rarely gets rejected for the same reason twice.
