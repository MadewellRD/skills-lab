---
name: supplier-discovery-desk
description: build a supplier longlist and market view for a sourcing exercise by identifying the legal contracting entity behind each brand reseller or regional subsidiary, assessing supply market structure viability and who can serve at this scale, quantifying incumbent switching cost and switching lead time, running a request for information where the market is unfamiliar, and recording pre-market engagement so contact is equal and documented. use for market scans, supplier longlists and shortlists, rfi design, contracting entity identification, reseller and channel structure questions, incumbent switching assessments, and pre-market supplier engagement.
---

# Supplier Discovery Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, build the longlist and the market view, produce the artifact set, update `procurement_packet`, and continue into `sourcing-event-desk` with the invited list and its contracting entities settled. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the discipline that the company contracts with a legal entity rather than with a brand.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the candidate it affects.

Never invent a supplier's legal entity, registration, ownership, customer base, scale, financial position, capability, reference customer, or reason for declining to bid.

## Role

Own the field: who could actually serve this requirement, who the company would actually be contracting with, and what it would cost to move away from whoever holds the work today. The longlist is the visible product; the durable one is the entity identification behind each name, because a brand, a product, a reseller, a regional subsidiary, and the parent that owns the intellectual property are five different legal persons and only one of them will be on the signature block.

Discovery is also the first act that reaches the market, and that changes the rules. Contacting a supplier starts a sales process the company then has to manage, and in a regulated or public procurement unequal pre-market engagement can disqualify the supplier that helped shape the requirement and can void the process outright. The incumbent deserves separate attention throughout, because the incumbent knows the company's renewal date, its consumption, its internal politics, and how painful a migration would be, and every one of those is a negotiating asset the company handed over by operating normally.

## Use when

- A requirement set exists and the market has to be scanned for suppliers who could plausibly serve it.
- The legal contracting entity behind a brand, a product line, a reseller, or a regional subsidiary has to be established before anyone is invited.
- A longlist has to be reduced to an invited list with the exclusion reason recorded for each candidate.
- Incumbent switching cost and switching lead time have to be quantified before a competitive exercise is justified.
- The market is unfamiliar enough that requirements would otherwise be written blind and a request for information is warranted.
- Pre-market engagement is being planned and has to be equal, authorized, and documented.
- A mandatory requirement appears to have no supplier in the market, and that finding needs establishing.

## Do not use when

- The requirement set and evaluation criteria are not yet fixed: `requirements-specification-desk`.
- The category boundary, supply market strategy, and demand aggregation are still open: `category-strategy-desk`.
- The sourcing document has to be assembled, issued, and run with a question window and addenda: `sourcing-event-desk`.
- Bids exist and have to be scored, normalized, and recommended: `bid-evaluation-desk`.
- The supplier's registration, ownership, sanctions position, insurance, and financial viability need verifying to diligence depth: `supplier-integrity-screening-desk`, which takes this desk's entity identification as its starting point.
- The security posture of a candidate needs assessing: `security-privacy-review-desk` coordinates that, and it runs against a shortlist rather than a longlist.

## Required evidence

- The requirement set with its mandatory items, and the category strategy with its supply market position.
- The incumbent position: what is contracted, what it costs, its term and notice window, and what the incumbent operates today.
- Corporate registry access for candidate entities, and the group structure behind each brand.
- Reseller, distributor, and channel structures, including whether the company would contract with the vendor or with a partner.
- Analyst material, peer input, and industry sources where they exist, each with its date and its independence stated.
- The company's own prior experience with candidates, including terminated relationships and the reason for each.
- The fairness regime governing pre-market contact, and any mandated process where public or regulated procurement rules apply.
- Geographic, regulatory, and data residency constraints on who may be used.
- Supplier scale indicators appropriate to the commitment: the ability to serve at this volume, in these regions, under these obligations.

## Workflow

**Outcome.** A longlist with the legal contracting entity identified per candidate, a market structure view covering concentration, viability, and who can plausibly serve at this scale, an incumbent assessment with switching cost and lead time, a shortlist reached by stated criteria with an exclusion reason per candidate, a request for information where one is warranted, and a pre-market engagement record showing who was contacted, by whom, when, and what was said.

**Grounding.** Registry and group structure evidence establishes the entity; a supplier's website, its logo wall, and its own capability claims are marketing recorded as vendor-claimed. Prior internal experience is evidence about the relationship rather than about the market. Analyst material carries its date and its funding relationship, because a market view purchased from a firm the suppliers also pay is a view with a position.

**Constraints.**

- Identify the contracting entity for every candidate before the invitation, not after the bid. A reseller between the company and the vendor changes who carries the obligations, whose insurance responds, and who the company would have to sue.
- Record why each excluded candidate was excluded. An unrecorded exclusion is the finding a challenge starts from, and it is the field nobody can reconstruct six months later.
- Quantify the incumbent's switching cost as money and elapsed time, including data migration, re-integration, retraining, and parallel running. A switching cost stated as "significant" is the incumbent's negotiating position written in the company's own document.
- Treat pre-market engagement as an act with a record: who was contacted, by whom, on what date, what was asked, and what was said. Where the fairness regime requires equal treatment, the same information reaches every candidate.
- Where no supplier in the market meets a mandatory requirement, that is a requirements finding routed back rather than a market to keep searching. State which requirement, and how many candidates it removed.
- A candidate whose viability or capability could not be established is listed as unassessed. It is not filled in from the supplier's own materials, and it is not quietly dropped either, since a dropped candidate is an exclusion with no reason.

**Parallel surface.** Candidate suppliers are independent and fan out: entity identification, group and channel structure, prior-experience lookup, capability screening, and scale assessment run per candidate at the same time, and within a candidate those lookups draw on different sources and also run at once. Two steps are aggregates and run once after the fan-out returns. The market structure view is a single pass over the whole candidate set, because concentration and the direction of pricing power are properties of the field rather than of any supplier in it. The capability gap finding is the same: a mandatory requirement that removes every candidate is only visible across the set, and it is the finding that sends work back to specification.

**Acceptance bar.** Every candidate carries a legal entity with its jurisdiction and the source that established it, or carries entity-not-established with what was searched. Every exclusion carries its reason and the criterion behind it. The incumbent assessment states switching cost in money and lead time in elapsed weeks, with what each figure includes. The pre-market record names every contact with its date. Any capability gap names the requirement and the candidates it removed.

## Outputs

A complete run delivers the set:

- `supplier-longlist.md`: every candidate with its brand, product, proposed contracting entity, jurisdiction, group position, channel route, and the source that established each.
- `contracting-entity-identification.md`: for each candidate, the entity that would sign, whether a reseller or regional subsidiary sits in between, what that changes about obligations and recourse, and the entities that could not be resolved.
- `market-structure-view.md`: concentration, the realistic field at this scale and in these regions, viability signals with their sources, and the direction of pricing power.
- `incumbent-assessment.md`: what is contracted and what it costs, term and notice position, switching cost with its components, switching lead time, what the incumbent knows about the company's position, and what a competitive exercise realistically achieves against them.
- `shortlist-and-exclusion-record.md`: the shortlist criteria, the invited list, and every excluded candidate with the reason and the criterion applied.
- `request-for-information.md`: the questions, what each is meant to establish, the response format, and how responses will and will not be used, prepared for issue.
- `pre-market-engagement-record.md`: who was contacted, by whom, when, what was asked, what was said, and how equal treatment was maintained.
- `capability-gap-findings.md`: mandatory requirements no candidate meets, the candidates each removed, and the specification question it raises.
- `supplier-discovery-downstream-handoff.md`: the invited list with entities, the incumbent position, and the unresolved candidates the next stages inherit.

Depth standard: an artifact is complete when the sourcing stage can issue to the invited list without further research and a challenge could be answered from the record. "Five suppliers identified" is a count; a longlist entry with the entity that would sign, the jurisdiction, the channel route, the scale evidence, and the exclusion criterion is a candidate assessment. The incumbent assessment is complete when the switching cost has components a finance partner would recognize.

Where the market is well understood and a request for information would add nothing, `request-for-information.md` is returned as not applicable with the basis. Where a registry, the vendor master, or the contract repository cannot be reached, `supplier-discovery-diagnostic.md` names the source and states which entities and which incumbent figures stay unestablished.

Supplier research is conducted almost entirely on material the suppliers themselves produced, which makes this the stage where a marketing claim is most likely to enter the packet as a fact and stay there. The specific pattern is the entity: a plausible legal name is available on every candidate's website footer, and appending a corporate suffix to a brand produces something that looks exactly like a registry result. The same pattern runs through customer counts, deployment scale, regional coverage, and the reference logos that turn into an assertion the supplier serves organizations of this size. A candidate's capability is recorded as vendor-claimed until a document establishes it, an entity that could not be resolved is written as entity-not-established with the registry searched, and a switching cost the company has not estimated is recorded as not quantified rather than described in adjectives that will be quoted back during the negotiation.

## procurement_packet fields to update

- `sourcing_event.bidders` with supplier, contracting entity, invited or excluded state, and the exclusion reason.
- `sourcing_event.event_type` where a request for information precedes the main event, and `sourcing_event.fairness_regime`.
- `sourcing_event.communication_log` with every pre-market contact, its date, and its content.
- `diligence.integrity.legal_entity` and `diligence.integrity.ownership` as the initial identification for the screening stage to verify.
- `relationship.switching_cost`, `switching_lead_time`, `substitutability`, `supply_position` for the incumbent and the realistic field.
- `requirements.business_requirements` flagged where a mandatory item has no supplier behind it.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Approval**: contacting the market. Pre-market engagement starts a sales process and, in a regulated or public procurement, unequal engagement can disqualify the supplier that helped shape the requirement and can void the exercise. Who is contacted, what they are told, and by whom is authorized and documented before it happens rather than reconstructed afterward.
- **Production or destructive**: the next act would send a request for information, share the requirement set, disclose volumes or budget, or signal to the incumbent that the work is being competed. Each of those reaches the market and cannot be recalled, and telling an incumbent that a competitive exercise is coming changes their renewal behavior immediately.
- **Security or privacy**: discovery would share the company's architecture, data flows, user counts, or security posture with candidates under no confidentiality agreement, or would collect personal data about supplier personnel beyond what the assessment needs.
- **Source conflict**: the registry, the vendor master, the supplier's own materials, and the reseller's paperwork name different entities for the same candidate, or the group structure and the registry disagree on ownership. Record every reading and route it; this disagreement usually is the finding.
- **Release integrity**: a market view, a viability position, or a capability claim would be reported to a sponsor or an approver as established when it rests on the supplier's own materials.
- **Connector unreachable**: a corporate registry, the contract repository, or the vendor master exists and cannot be read, so the contracting entity or the incumbent position would be asserted on inference.

An unresponsive candidate, an unavailable analyst report, an unconfirmed regional coverage claim, and a peer contact who has not replied are soft gaps. Record them against the candidate as unassessed, label the assumption, and continue with the field as it stands.

## Downstream handoffs

`sourcing-event-desk` inherits the invited list with contracting entities, the fairness regime, and the pre-market record that establishes what has already been said to whom. `supplier-integrity-screening-desk` inherits the entity identification as the starting point for registry verification and screening, and screens the entity that would sign rather than the brand. `bid-evaluation-desk` inherits the incumbent position and the exclusion record, both of which a debrief will draw on. `pricing-negotiation-desk` inherits the switching cost, the switching lead time, and the realistic alternative, which together are the walk-away position. `requirements-specification-desk` receives any capability gap back, because a mandatory requirement no supplier meets is a specification problem.

## Quality bar

Good discovery produces a field the company can defend and an entity list a lawyer would recognize. Every candidate resolves to a legal person with a jurisdiction, so nobody discovers at signature that the agreement sits with a reseller carrying none of the obligations the specification assumed. Every exclusion has a reason on the record, because the excluded supplier's champion inside the company eventually asks. The incumbent assessment is written by somebody who has priced a migration rather than described one, since a switching cost expressed in adjectives is the number the incumbent will use to explain why the uplift is reasonable. And the record of who was contacted and what was said is complete enough that a challenge, an audit, or a losing bidder's question is answered from the file rather than from anybody's recollection.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
