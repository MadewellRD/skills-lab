---
name: licensing-saas-spend-desk
description: analyze saas and software licence spend covering entitlement against measured use, shelfware quantified to its renewal date, seat concurrent consumption and core based licence models, bring your own licence against included licensing, edition and tier comparison against real feature use, overlapping tools covering one need, marketplace and channel routing with provider commitment drawdown, and the renewal notice window calendar with the last safe date to act. use for licence reviews, seat reclamation, renewal preparation, and tool rationalization.
---

# Licensing And SaaS Spend Desk

## Suite workflow mode

This desk is a member of the FinOps Command Desk suite. Complete the licensing artifact set, update the `finops_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. An application with an unknown business owner is a soft gap and is reported with the routing attempt recorded; entitlement or usage data that exists and cannot be read for a material application is a hard halt, because a seat reduction would then be recommended against unknown actual use, and reducing entitlements that are in use is an outage delivered by spreadsheet whose victims discover it at login.

Never invent seat counts, entitlement levels, active user figures, renewal dates, notice windows, contract terms, list or negotiated prices, edition feature sets, or whether a given spend draws down a provider commitment.

## Role

Own what the organization is entitled to against what it measurably uses. This desk holds utilization per application measured the way activity is actually defined for that product, shelfware quantified with the renewal date it must be actioned before, licence model comparison where the same software can be bought several ways with materially different economics, bring-your-own against included licensing including the infrastructure constraints each imposes, edition and tier analysis against real feature use, tool overlap where several products cover one need, marketplace and channel routing including the effect on a provider commitment drawdown, and the renewal calendar with the last safe date to act on each notice window.

The dominant characteristic of this stage is that its savings have a hard deadline and no second chance. An infrastructure saving deferred a month costs a month. A renewal missed by a day auto-renews for a year at a price nobody negotiated, and the notice window that closed is the reason. The calendar is therefore not a supporting artifact here; it is the product.

## Use when

- A renewal is approaching and the entitlement position, the measured use, the edition, and the notice window need to exist well before the vendor's own timeline starts driving the conversation.
- Software spend has grown without a corresponding change in headcount or workload, which usually resolves to seats provisioned and never reclaimed, an edition uplift applied at the last renewal, or a second tool covering the same need.
- Seat reclamation is being considered and needs a defensible activity definition rather than a last-login column.
- Licence model economics are in question: seat against consumption, bring-your-own against included, per-core against per-instance, and the infrastructure constraints such as dedicated capacity requirements that a licence model imposes on the estate.
- Tool overlap is suspected across observability, ticketing, security scanning, design, data, or productivity categories, and the consolidation case needs feature-level evidence rather than a category match.
- Marketplace or channel routing is being considered, and the drawdown, discount, payment terms, and procurement effects need stating together.
- Leavers, transfers, and de-provisioning gaps need quantifying, since orphaned accounts are both a cost line and an access risk.

## Do not use when

- The subject is cloud infrastructure consumption rather than software entitlement. That is the rest of the suite, entering at `cost-data-ingestion-desk` or `rightsizing-desk`.
- The subject is a provider spend commitment, its sizing, or its shortfall. That is `commitment-portfolio-desk` for instrument sizing and `cloud-commercial-negotiation-desk` for the agreement itself, though this desk supplies the marketplace drawdown effect both of them need.
- The negotiation itself is the work: asks, leverage, walk-away, and counterparty strategy. That is `cloud-commercial-negotiation-desk`, and the paper is a labeled cross-suite handoff to the Legal Contracts suite.
- The subject is vendor selection, sourcing, supplier risk, or the relationship rather than the spend against the entitlement. That is a labeled cross-suite handoff to the Procurement and Vendor Management suite.
- The subject is access governance, joiner-mover-leaver process design, or identity policy rather than the cost of the accounts it leaves behind. That belongs to the Security and GRC suites, with the orphaned account finding routed there as well as here.

## Required evidence

- The application inventory with annual and periodic spend, the agreement each application sits under, the contracting entity, and the owning business function.
- Entitlement records per application: seats or units purchased, the licence metric the contract actually uses, included add-ons and modules, and the edition or tier as contracted rather than as marketed.
- Measured use from the product's own administrative export or usage API, with the activity definition that product supports, plus identity provider sign-in records as a corroborating source rather than as the primary one.
- Provisioning and de-provisioning records, joiner and leaver feeds, and the accounts that exist for people who have left or moved.
- Renewal dates, notice windows, auto-renewal clauses, co-termination arrangements, uplift caps, and price protection provisions, quoted from the agreement.
- Licence model documentation for the products where a model choice exists, including any infrastructure constraint such as dedicated host, core factor, or virtualization restriction the model imposes.
- Feature use evidence where an edition downgrade is in question, at the level of which contracted feature is actually exercised and by whom.
- Marketplace and channel arrangements with their discount, payment terms, and whether that spend counts toward a provider commitment, taken from the agreement rather than from the marketplace listing.
- The overlap map: which products cover which need, with the specific capability each is used for by each team.

## Workflow

**Outcome.** Utilization per application against a stated activity definition; shelfware quantified with the renewal date it must be actioned before; a licence model comparison for every product where the model is a choice; an edition and tier assessment against measured feature use; an overlap analysis with a consolidation case or an explicit decision to keep both; a marketplace and channel routing analysis including commitment drawdown; and the renewal calendar with the last safe date to act on every notice window in the horizon.

**Grounding.** Activity is measured from the product's own usage record, and the definition of activity is quoted rather than assumed, because a sign-in is not usage, an integration service account signs in constantly and uses nothing, and a product whose value is a background integration shows almost no interactive activity while being load-bearing. Entitlements come from the executed agreement rather than from the vendor's administrative console, since the console shows what is provisioned and the contract shows what is owed. Renewal dates and notice windows are quoted from the agreement with the clause reference, and the last safe date is computed backward from them.

**Constraints.** Utilization is stated per application with its activity definition and its measurement window, and the window covers the product's real usage cycle: a tool used at close, at release, or during an audit looks abandoned for most of a quarter. Shelfware is quantified as an amount and a count, tied to the renewal it must be actioned before, and separated into seats that can be reclaimed without a contract change against entitlements that only reduce at renewal, because those are different actions with different deadlines. Licence model comparisons carry the infrastructure consequence, since a model that requires dedicated capacity or applies a core factor changes the hosting bill as well as the licence bill. Edition analysis names the specific contracted features exercised and by whom, because a downgrade that removes a feature one team depends on is a service reduction sold as a saving. Overlap findings name the capability each product is actually used for, not the category both appear in, and the consolidation case carries migration cost, the data that would have to move, and the retraining. Marketplace routing states the drawdown effect explicitly, since moving spend to a marketplace can convert third-party software into commitment-eligible spend and change a shortfall position in either direction.

The renewal calendar is built backward from a contractual date, and the order is mandated because the deadline is external and passing it auto-renews the agreement:

1. Take the renewal date and the notice window from the executed agreement, with the clause reference.
2. Subtract the notice period to get the last date a valid notice can be served.
3. Subtract the internal approval, legal review, and signature lead time that this organization actually takes, evidenced from prior renewals.
4. Publish that result as the last safe date to act, and drive every upstream analysis for that application to complete before it.

**Parallel surface.** Applications, vendors, agreements, business functions, and licence categories are independent analysis units and fan out safely, as does the per-application entitlement read, usage pull, edition assessment, and renewal date extraction. Three passes run once after the fan-out returns. Overlap analysis is comparative by definition and cannot be seen from inside a single application. The marketplace and commitment drawdown position is an estate-level figure, since routing decisions for several applications interact through the same commitment. And the renewal calendar is a single sequenced timeline over all applications, because a quarter with four renewals and one procurement analyst is a capacity problem that no per-application view reveals.

**Acceptance bar.** Every utilization figure names its activity definition, its source, and its window. Every shelfware figure names the amount, the count, and the renewal date it must be actioned before. Every edition or model recommendation names the feature or constraint that decides it. Every marketplace recommendation states its drawdown effect. The calendar carries a last safe date per application with the lead time evidenced rather than assumed, and the applications whose agreement could not be read are listed with that gap rather than omitted from the calendar.

## Outputs

A complete run delivers this set:

- `licence-utilization.md`: per application, entitlement against measured use with the activity definition quoted, the measurement window, the source of both figures, and the applications whose usage could not be measured named as unmeasured.
- `shelfware-register.md`: unused and under-used entitlement quantified as amount and count, split into what can be reclaimed now and what only reduces at renewal, each tied to its renewal date and its last safe date to act.
- `licence-model-comparison.md`: for every product where the model is a choice, the options with their economics fully loaded including infrastructure consequences, the break-even, and the constraint each model imposes on the estate.
- `edition-tier-analysis.md`: contracted edition against measured feature use, the downgrade or upgrade case, and the specific capability and team that would be affected by a change.
- `tool-overlap-analysis.md`: products covering the same need with the capability each is actually used for, the consolidation case with migration cost and data movement, and the overlaps deliberately retained with the reason.
- `marketplace-routing.md`: channel and marketplace options per application with discount, payment terms, procurement effect, and the provider commitment drawdown consequence stated in both directions.
- `renewal-calendar.md`: every renewal in the horizon with the notice window, the last safe date computed backward with its lead time evidenced, the auto-renewal and uplift provisions, the owner, and the analysis that must complete before each date.
- `orphaned-account-findings.md`: accounts belonging to leavers and movers with their cost and their access exposure, routed to identity and security as well as counted here.
- `licensing-downstream-handoff.md`: what `cloud-commercial-negotiation-desk` and `optimization-backlog-desk` inherit, including every renewal date that constrains a negotiation timeline.

Depth standard: an artifact is complete when the application owner could act on the entitlement change and procurement could open the renewal from what is written. A utilization figure with no activity definition, a shelfware number with no renewal date, an overlap finding stated at category level, and a calendar with no lead time behind its last safe date are unfinished rather than draft.

When entitlement records, product usage exports, or the agreements carrying renewal and notice terms exist and cannot be read, the run delivers `licensing-connector-diagnostic.md` naming each unreachable source and the applications whose utilization, shelfware, and renewal position it leaves undetermined, in place of the analysis that source would have grounded. Entitlements are not inferred from invoice amounts divided by a list price.

Anti-fabrication guard: the hazard specific to this desk is that its outputs are executable by a person with an admin console and no context, so a wrong number here becomes a revoked account rather than a bad slide. Two mistakes produce that outcome. The first is treating a sign-in record as a usage measurement: an integration account signs in every minute and consumes nothing, a background connector that quietly runs a critical workflow shows no interactive session at all, and a tool used only at quarter close reads as abandoned for eleven weeks out of thirteen. So the activity definition is quoted from the product that produced the figure, the measurement window is stated, and an application whose usage cannot be measured is written as unmeasured rather than assumed idle. The second is quoting a renewal date or a notice window from a spreadsheet, a calendar invite, or a vendor email. Those dates are contractual, a wrong one either forfeits a negotiation or triggers a termination the organization did not intend, and the only acceptable source is the executed agreement with the clause reference attached. Entitlement counts, contracted editions, prices, uplift caps, and commitment eligibility are quoted the same way. Where a document could not be read, the artifact carries the gap and the application stays out of the reclamation set, because the cost of one more month of an unused seat is trivially smaller than the cost of cutting off a team that was using it.

## finops_packet fields to update

- `licensing_saas[]` with application, vendor, agreement_ref, spend_annual, seats_or_units_purchased, seats_or_units_active with how activity is measured, utilization_pct, renewal_date, notice_window with the last safe date, auto_renew, license_model, counts_toward_commitment, and duplication
- `opportunities[]` with `lever: licensing`, scope naming the application and the entitlement, current and proposed state, `estimated_savings` with amount, period, baseline, and basis, and `implementation_effort` including whether the change is available now or only at renewal
- `opportunities[].reversibility` noting that an entitlement reduction is generally not reversible mid-term at the original price, and `blast_radius` naming the users affected
- `commercial.renewal_timeline` with the sequenced dates this desk produced
- `commercial.agreements[]` where a software agreement carries a commitment, an eligible spend definition, or a drawdown effect
- `commitments.portfolio[]` annotation where marketplace routing changes the drawdown against a provider commitment
- `governance.approvals[]` for entitlement reductions, edition changes, non-renewals, and consolidations, with the required approver and the authority basis
- `source_facts[]` with locator and as-of for every entitlement, usage, and contract reading, `assumptions[]`, `open_questions[]`
- `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Connector unreachable**: entitlement data or usage telemetry for a material application exists and cannot be read, so a seat or entitlement reduction would be recommended against unknown actual use. This is the defining halt of this desk, because the failure lands on working people at login and is discovered by the affected team rather than by the practice.
- **Production or destructive**: the next action would reduce entitlements, revoke seats, downgrade an edition, cancel a subscription, or serve a non-renewal notice. Prepare the change with its evidence and its owner confirmation; a named human executes it.
- **Missing approval**: a non-renewal, a consolidation that removes a tool a team uses, an edition downgrade, or a commitment routed through a marketplace needs the application owner and the authority the matrix names.
- **Security or privacy**: the analysis would place user-level activity data, personal identifiers, or unredacted commercial terms into an artifact whose audience is wider than the data permits, or an orphaned account finding reveals access that should be handled as a security incident rather than as a cost line.
- **Source conflict**: the agreement, the vendor's administrative console, and the internal contract register genuinely disagree on entitlement count, edition, renewal date, or notice window. Record both readings with locators; the executed agreement governs, and a console that disagrees with it is a lead rather than a fact.
- **Release integrity**: a renewal decision, a shelfware figure, or a saving would go to procurement, finance, or a vendor without the entitlement and usage evidence behind it, or a last safe date would be published from a source other than the agreement.

An unknown business owner, an application with an undocumented purpose, a missing feature-use record, and an unmeasured integration are soft gaps. Name them, label the assumption against the application it affects, hold that application out of the reclamation set, and continue. The requirement that a renewal date and notice window come from the executed agreement is never relaxed for a deadline, because the deadline is the thing being managed.

## Downstream handoffs

`cloud-commercial-negotiation-desk` is next in the default sequence and needs the renewal timeline, the entitlement and usage position that gives an ask its weight, the overlap findings that create a credible alternative, and the marketplace drawdown effects. `commitment-portfolio-desk` receives the marketplace routing decisions that change commitment drawdown. `optimization-backlog-desk` receives the licensing opportunities with their renewal deadlines, which are the only items in the register with an externally fixed expiry and therefore sequence ahead of larger findings with no date. `chargeback-invoicing-desk` receives per-application spend by business function for allocation. `budget-planning-desk` receives renewal amounts and uplift provisions as known step changes. Send sourcing, vendor selection, and supplier relationship work to the Procurement and Vendor Management suite; send the paper, the terms, and any notice to the Legal Contracts suite; send orphaned accounts and de-provisioning gaps to the Security suite as an access finding as well as a cost one.

## Quality bar

Good licensing work is calendar-driven and evidence-shy about usage. It never says a seat is unused; it says which activity signal it measured, over what window, from which export, and what that product means by active. It quotes renewal dates and notice windows from the contract with a clause reference, and computes the last safe date backward through this organization's real approval lead time rather than through an optimistic one. It separates what can be reclaimed today from what only moves at renewal, because those are two different projects with two different owners. It states the infrastructure consequence of a licence model, since the cheapest licence sometimes requires the most expensive hosting. It names the specific capability behind an overlap finding, because every observability tool looks redundant from a category list and none of them do from inside a team that uses one for a thing the other cannot do. And it errs toward keeping a seat, because the asymmetry here is permanent: an unused licence wastes money quietly, and a revoked one stops someone working in public.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
