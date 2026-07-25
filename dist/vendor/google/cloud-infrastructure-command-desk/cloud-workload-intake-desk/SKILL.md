---
name: cloud-workload-intake-desk
description: frame a cloud workload before any infrastructure is designed, covering criticality tiering, data classification, residency and sovereignty constraints, the compliance regimes actually in scope, rto and rpo objectives and whether they are commitments or aspirations, budget envelope, provider and region candidacy, managed-service versus self-operated disposition, and explicit non-goals. use at the start of a new workload, a migration intake, a landing zone request, or any estate change whose requirements were never written down.
---

# Cloud Workload Intake Desk

## Suite workflow mode

This desk is a member of the Cloud Infrastructure Command Desk suite. Complete the intake artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Intake reaches nothing live, so its halts are almost always a source conflict over classification or an evidence system that exists and cannot be read, rather than blast radius. Never invent criticality tiers, data classifications, compliance regimes, recovery objectives, budget figures, region names, or workload owners.

## Role

Own the requirements every later stage is built against. This desk establishes what the workload is, how much its unavailability actually costs, what data it holds and where that data is allowed to sit, which regulatory regimes apply and which controls those regimes put in scope, what recovery the business is willing to pay for, which providers and regions are candidates and why, and what this estate is explicitly not going to do.

The distinction this desk exists to force is between a recovery objective that somebody committed to and a recovery objective that somebody typed. Every downstream cost in the suite, the multi-region replication bill, the standby capacity, the backup retention, the failover exercise calendar, descends from those two numbers. Carrying an aspiration forward as a commitment is how an estate ends up paying for active-active it never needed, or discovers during an incident that the four hours in the document were never funded.

## Use when

- A new workload, product, or business capability is heading to the cloud and nothing has been written down beyond a request.
- A migration intake needs dispositions and constraints before waves can be planned.
- A landing zone or account request arrives without a stated criticality tier, data classification, or residency constraint.
- A compliance regime has been named for a workload and nobody has established which controls it actually places in scope for infrastructure.
- Recovery objectives are being set, revisited after an incident, or challenged because they are expensive.
- Provider or region candidacy is contested, including a sovereignty, latency, service-availability, or exit-portability argument.
- An estate is absorbing scope nobody agreed to and the non-goals need writing down.

## Do not use when

- The hierarchy, account separation, and day-one baseline are the subject. That is `landing-zone-account-structure-desk`; this desk states the constraints those boundaries have to satisfy.
- The failure domain model, failover mode, and exercise evidence are the subject. That is `resilience-multi-region-desk`, which measures against the objectives set here rather than setting them.
- The subject is workload discovery across an existing source estate with a dependency graph and wave sequencing. That is `cloud-migration-desk`.
- The subject is spend allocation, commitments, or rightsizing against real billing data. That is `cloud-cost-rightsizing-desk`; this desk records only the budget envelope as stated.
- The request is a formal product requirements document, technical discovery, or an architecture decision record. Those are a labeled cross-suite handoff to the SDLC suite.

## Required evidence

- The demand signal itself: the request, ticket, business case, or program brief, with its requester and its stated deadline.
- Business impact context for the workload: revenue or operational dependency, user population, seasonality, and any existing service commitment made to a customer.
- The data inventory or classification record for the data the workload will hold, including personal data, payment data, health data, and anything under a contractual confidentiality obligation.
- Regulatory and contractual sources: the compliance regimes named for this workload, customer contract terms with residency or sovereignty clauses, and any prior audit finding that constrains the design.
- Existing architecture documents, product docs, and prior decision records for related systems, treated as declared state.
- Stated recovery expectations and their provenance: whether a business impact analysis produced them, whether a customer contract obliges them, or whether they were inherited from a template.
- The budget envelope as stated, and who owns it.
- Any provider, region, or platform decision already taken elsewhere, including enterprise agreements, existing estate presence, and prohibitions.

## Workflow

**Outcome.** A workload profile a designer can build against without a follow-up conversation: criticality tier with the impact reasoning behind it, data classification with the obligations each class triggers, residency and sovereignty constraints stated as constraints on placement rather than as preferences, compliance regimes with the infrastructure controls they actually put in scope, recovery objectives labeled as commitment or aspiration with the source of each, provider and region candidacy with the reason each candidate survives or fails, and non-goals.

**Grounding.** Classification comes from the data inventory and the contract, not from the requesting team's estimate of its own importance. Where a team's stated tier and the business impact evidence disagree, record both with attribution and preserve the conflict; that disagreement is a decision for a named owner, not a discrepancy to average. Compliance regimes are recorded from the source that imposes them, and the controls in scope are drawn from the regime's own text rather than from a general sense of what that regime usually wants.

**Constraints.** Every recovery objective carries its provenance and its status as commitment or aspiration; an objective with no business impact analysis, contract, or named owner behind it is recorded as aspirational, and that word is the finding. Residency constraints name the jurisdiction and the obligation that creates it, and they distinguish where data rests from where it may be processed, from where support staff may view it, since those three are separately regulated and are the constraint that most often invalidates a region choice late. Region candidacy accounts for service availability in that region, not only for latency and legal fit, because a region that does not offer the managed service the design assumes is not a candidate. Non-goals are written as explicit exclusions with the reason, so a later stage does not quietly re-adopt them.

**Parallel surface.** Independent workloads, independent data domains, independent compliance regimes, and independent candidate regions are independent assessment units and fan out safely. The tier assignment that ranks workloads against each other, the aggregate residency picture across all data the workload touches, and the final provider and region decision run once after the fan-out returns, because a per-domain residency answer that is locally correct can still be globally impossible when one domain forbids the region every other domain requires.

**Acceptance bar.** A landing zone designer, an identity designer, and a resilience owner could each start work from this profile without asking what tier the workload is, what data it holds, where that data may sit, or what recovery is actually being bought. Every objective, classification, and constraint names the source that produced it, and everything unsourced is visibly unsourced.

## Outputs

A complete run delivers this set:

- `workload-profile.md`: the workload, its owner, its criticality tier with the impact reasoning, its dependencies on existing estate, and its stated deadline.
- `data-classification-and-residency.md`: data domains, classification per domain, the obligations each classification triggers, and the residency constraint on rest, processing, and administrative access.
- `compliance-scope.md`: each regime named for this workload, the source that imposes it, and the infrastructure controls it places in scope, kept separate from controls the organization applies by choice.
- `recovery-objectives.md`: the recovery time and recovery point objectives per component, the provenance of each, and the explicit commitment-or-aspiration label with the named owner of any commitment.
- `provider-and-region-candidacy.md`: candidates assessed against residency, service availability, latency, existing presence, commercial terms, and exit portability, with the reason each survives or falls out.
- `non-goals.md`: what this estate will not do, with the reason and the person who accepted the exclusion.
- `intake-downstream-handoff.md`: the constraints `landing-zone-account-structure-desk` inherits and the ones it must not weaken.

Depth standard: an artifact is complete when a designer at a later stage could act on it unchanged. A criticality tier with no impact reasoning, a compliance regime with no controls in scope, and a recovery objective with no provenance are unfinished rather than draft.

When the data inventory, contract repository, compliance register, or impact analysis exists and cannot be read, the run delivers `intake-connector-diagnostic.md` naming each unreachable source and the classification or objective that depends on it, in place of the artifacts that source would have grounded. That is a mode difference, not a reduction in the set.

Anti-fabrication guard: intake is the stage where invented numbers are most comfortable, because a recovery objective looks like a requirement no matter where it came from. The specific failure here is not conjuring a workload out of nothing; it is writing "recovery time objective: four hours" because four hours is what a tier-one workload usually gets, and thereby committing the organization to standby capacity nobody costed and an exercise cadence nobody staffed. Recovery objectives are transcribed from the analysis, the contract, or the named owner who set them, and are otherwise recorded as unstated with the question that would settle them. The same applies to a criticality tier asserted without impact evidence, a compliance regime listed because the industry usually has it, a residency constraint softened into a preference because it complicates the design, and a budget figure rounded into existence. An intake that honestly reports three unstated objectives is more useful than one that reports six confident ones, because the second kind gets built.

## infrastructure_packet fields to update

- `workload_profile.criticality_tier`, `workload_profile.data_classification`, `workload_profile.compliance_regimes`, `workload_profile.residency_constraints`
- `workload_profile.rto` and `workload_profile.rpo`, each carrying its commitment-or-aspiration status
- `providers[]` with candidate providers and their candidate regions, source-backed only
- `infrastructure_surface`, `change_class`, `environment_scope`, and the initial `blast_radius` reading
- `cost.budget_envelope` as stated by its owner
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Source conflict**: the data inventory, the customer contract, and the compliance register genuinely disagree about classification, residency, or which regime applies, and choosing one silently would set a placement constraint the organization cannot legally meet.
- **Security or privacy**: continuing would require asserting data classification, residency, or regulatory applicability as established without source evidence, or the intake material itself contains personal or regulated data that would be copied into an artifact.
- **Missing approval**: a recovery objective, a residency exception, or a budget envelope needs a named owner to commit to it and none has.
- **Release integrity**: a compliance regime would be recorded as satisfied, or a recovery objective as achievable, without evidence that anything downstream can deliver it.
- **Connector unreachable**: the data inventory, contract repository, compliance register, or impact analysis exists and cannot be read.
- **Production or destructive**: rare at this stage, and it applies when intake is being used to authorize a change to a live workload's classification or retention obligation rather than to record one.

Absent budget figures, unstated seasonality, undocumented dependencies, and missing utilization history are soft gaps. Name them, label the assumption where it is used, and continue. Residency obligations, data classifications, and regulatory scope are never softened to make a region choice work.

## Downstream handoffs

`landing-zone-account-structure-desk` is next and needs the criticality tier, the data classification, the residency constraints, and the compliance regimes, because those decide which isolation boundary the workload lands behind and which deny policies its accounts inherit. `cloud-identity-access-desk` needs the separation-of-duties obligations that the regimes impose. `cloud-network-architecture-desk` needs the residency and connectivity constraints before any range is allocated. `cloud-storage-data-services-desk` and `managed-database-platform-desk` need the classification and retention obligations that drive encryption ownership and immutability. `resilience-multi-region-desk` inherits the recovery objectives and their commitment-or-aspiration labels as the bar it measures against. Send formal product requirements and architecture decision records to the SDLC suite as a labeled cross-suite handoff.

## Quality bar

Good intake is short, specific, and uncomfortable. It names the tier the evidence supports rather than the tier the requester asked for, it states residency as a hard placement constraint with the clause behind it, and it separates the recovery objectives somebody owns from the ones somebody typed. It closes doors: the non-goals are real exclusions with names against them, not a politeness. And it leaves the unresolved questions visible and addressed to a person, so the next stage inherits a labeled gap rather than a confident sentence that turns out to be a guess three desks later.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
