---
name: contact-driver-analysis-desk
description: analyze what is generating support demand by producing a ranked contact driver list with volume, window, and trend against a comparison period, contacts per active account so growth is not read as regression, the underlying cause separated from the reason code that recorded it, miscoding corrected against a read of the underlying threads, the deflectable share stated honestly, and each driver routed to the function that can remove it. use for contact reason taxonomy reviews, demand reduction, ticket deflection strategy, and product feedback loops.
---

# Contact Driver Analysis Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the driver artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the driver it affects, and record it in `open_questions`. Never invent a driver volume, a trend, a cause, a cost per contact, an active account count, a coding rule, or an outcome attributed to a prior routing.

## Role

This desk answers why the contacts exist, which is a different question from how the queue is absorbing them, and it is the only desk in the suite whose output routinely commits another function's quarter.

The central discipline is separating the cause from the code that recorded it. A reason code is what an agent picked from a list, under time pressure, from options that overlap, often at the moment they created the ticket rather than after they understood it. So the coded distribution is a hypothesis about demand, not a measurement of it, and every driver analysis that skips reading the underlying threads produces a ranked list of the taxonomy's shape rather than of the customers' problems. The classic form is a login failure buried inside a billing code because the customer mentioned an invoice, and the quarter it sends to the wrong team.

The second discipline is the rate. Raw contact volume rises when the customer base rises, so an absolute increase says nothing on its own. Contacts per active account, with the account population stated, is the reading that distinguishes a growing company from a degrading product, and it is the number that survives a room full of people who want the answer to be growth.

The third is the routing. A driver stays a report until it names the function that can remove it, states what that function needs in order to decide, and records whether they accepted it. Drivers unchanged across periods are reported as unresolved rather than restated as new findings, because a list that presents the same top three every quarter as fresh insight is how a support organization loses standing with product and engineering.

## Use when

- Demand needs reducing and the question is where it comes from and who can remove it.
- A ranked driver list is needed for a product, engineering, docs, billing, or onboarding forum.
- Contact volume has moved and it is unclear whether that is growth, seasonality, a release, or a regression.
- Reason codes are suspected of being wrong, overlapping, or gamed, and need correcting against the threads.
- A release has shipped and its effect on contact volume needs measuring.
- The deflectable share of demand needs establishing before content or self-service investment is committed.
- Prior driver findings need revisiting to see whether anything actually happened to them.
- The contact reason taxonomy itself needs redesigning so the next quarter's analysis is readable.

## Do not use when

- The subject is queue shape, aging, or breach exposure rather than demand. That is `queue-backlog-health-desk`.
- The question is whether self-service could have answered these contacts and what containment currently is. That is `self-service-deflection-desk`, which consumes this ranked list.
- The article that would answer a driver needs writing. That is `knowledge-base-desk`.
- The picker, field, or taxonomy change needs implementing in the platform. That is `support-tooling-automation-desk`, which owns the blast radius of a taxonomy change.
- One ticket needs a cause. That is `diagnostic-troubleshooting-desk`; a driver is a population-level statement.
- The figures are going to a leadership forum with definitions, populations, and exclusions attached. That is `support-metrics-reporting-desk`, which is the stage after this one.

## Required evidence

- Coded contact reasons with the taxonomy version, the coding rules, when each code was added or changed, and the known weaknesses agents work around.
- Ticket volume by driver over a stated window with the counting rules for merges, duplicates, spam, machine-generated tickets, and incident-generated contacts.
- A readable sample of the underlying threads per driver, drawn by a stated method, rather than the codes alone.
- The active account population over the same window, with the definition of active, so a rate can be computed.
- Handle time or cost per contact per driver where either exists, with the definition and population behind it.
- Product release, configuration, pricing, and policy change history over the same window and the one before it.
- The comparison period with any change in the customer population, product mix, plan mix, or coding rules between them.
- Prior driver findings, what was routed, what was accepted, what shipped, and what happened to the volume afterward.
- The routing paths into product, engineering, documentation, billing, onboarding, and sales, with what each function needs in order to take a driver seriously.

## Workflow

**Outcome.** A ranked driver list with volume, window, and trend against a comparison period with the population held constant, contacts per active account, the underlying cause separated from the code that recorded it, miscoded drivers corrected against the sampled threads with the coding weakness named, the deflectable share stated honestly, each driver routed to the function that can remove it with what that function needs to decide, and prior findings reported as resolved or unresolved rather than restated.

**Grounding.** The ranking starts from the coded distribution and is corrected by reading a sample of the threads behind each driver, because the code is what someone picked and the thread is what the customer said. Volume carries its window and counting rules, and incident-generated contacts are separated so an outage does not appear as a demand trend. Trend is computed against a comparison period with the population, the product mix, and the coding rules held constant, and where any of those changed between periods, that change is stated as part of the comparison rather than left for the reader to discover. Cause is stated at the confidence the evidence carries: a driver whose threads show a consistent mechanism is a cause, and a driver whose threads show three unrelated problems sharing a code is a taxonomy finding.

**Constraints.** No driver is ranked without a stated window, a stated population, and stated counting rules. No trend is reported without naming what changed in the population between the periods. Contacts per active account is reported alongside any absolute volume claim, since absolute movement is uninterpretable without it. A cause is never inferred from a code alone; where the threads behind a driver were not read, the driver is reported as coded but unverified. The deflectable share is stated as an assessment of whether an answer could exist, kept distinct from measured deflection, which belongs to the deflection desk. Individual customers and agents are never named in a driver artifact, because this document travels to functions with no ticket access. Drivers routed in a prior period are reported with what happened, and a driver that was routed and declined is recorded as declined rather than quietly re-raised as new.

**Parallel surface.** Independent items fan out safely: each driver's threads sampled and read, each driver's cause assessed, each driver's routing packet assembled for its owning function, each miscoding candidate checked against its threads, and each prior finding traced to its outcome. Four passes are single after the fan-out returns, because each is a statement about the whole set: the ranking itself, which only exists relative to every other driver; contacts per active account, which is a rate over one population; the trend comparison, which requires both periods held on the same rules at once; and the recoded distribution, since moving contacts out of one code moves them into another and independently recoded drivers do not sum to the population.

**Acceptance bar.** Every driver carries its volume, window, queue scope, and counting rules. Every trend names the comparison period and what changed in the population between them. Contacts per active account appears wherever volume does, with the active definition. Every driver states whether its threads were read and how many. Every corrected miscoding names the coding weakness that produced it. Every driver names the owning function, what that function needs to decide, and its current routed state. Prior findings are reported as resolved, unresolved, or declined, with evidence.

## Outputs

A complete run delivers this set:

- `ranked-driver-list.md`: drivers by volume with the window, queue scope, counting rules, contacts per active account, trend against the comparison period, handle time or cost where it exists, and the rank stated as of a date.
- `driver-cause-analysis.md`: per driver, the cause as the threads establish it, the sample size and selection method behind that reading, the distinction between what the customer contacted about and what actually caused it, and the drivers whose threads showed several unrelated problems.
- `coding-correction-report.md`: the miscoded contacts found, the codes they were moved between, the volume that moves as a result, the specific taxonomy weakness that produced each miscoding, and the recoded distribution alongside the original.
- `deflectability-assessment.md`: per driver, whether an answer could exist and on which surface, what would have to be true for it to work, and the drivers that are not deflectable at all because they need a product change.
- `driver-routing-packets.md`: one packet per routed driver, addressed to the owning function, carrying the volume, the rate, the customer-facing symptom, the cause, the cost where known, and the specific decision being asked for.
- `prior-findings-status.md`: every driver routed in earlier periods with what was accepted, what shipped, what the volume did afterward, and the ones unchanged and still unowned.
- `taxonomy-recommendations.md`: the codes to merge, split, retire, or add, the overlaps agents are resolving arbitrarily, and what each change would break in historical comparison.
- `driver-downstream-handoff.md`: what `support-metrics-reporting-desk` inherits, including the driver figures with their definitions and the movement this analysis explains.

Depth standard: an artifact is complete when a product manager could take a routing packet into their own prioritization without asking support for more data, and when the ranked list could be compared with next quarter's without a reconciliation exercise. A driver named with a volume but no window, or a cause asserted from codes with no threads read, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the reporting layer, the ticket threads, or the active account population cannot be reached, the run delivers `driver-connector-diagnostic.md` naming each unreachable source and which rankings, rates, or causes are unavailable because of it. Where the threads are readable but the volumes are not, a qualitative driver read still ships with the ranking explicitly withheld, since knowing which problems exist is useful and knowing their order is what needs the counts.

Anti-fabrication guard: a driver analysis is the artifact in this suite most likely to be believed without being checked, because it arrives as a tidy ranked list and its audience has no way to test it. The temptation is not to invent a driver; it is to write the causal sentence. A cause narrative for a code nobody read the threads behind, a percentage share that resolves the list neatly, a trend against a comparison period that was never actually pulled, and an attribution of a spike to last month's release all read as analysis and are indistinguishable from it on the page, and each one sends a function to work that will not reduce anything. In these artifacts a cause is written only where a stated number of threads was read by a stated method, and the count appears next to the cause; a driver whose threads were not read is labeled coded but unverified and is ranked with that label attached. Percentages carry the count they were computed from, no share is adjusted to make a distribution sum, and a trend appears only where both periods were pulled on the same counting rules with the population change stated. Where a release is named as the origin of a spike, the release date and the volume series on both sides of it are shown, because attributing demand to a change is exactly the claim the receiving team will check first, and being wrong about it once costs the next three analyses their audience.

## support_packet fields to update

- `drivers[]` with `driver`, `volume` carrying its window and queue, `trend` naming the comparison period and the population held constant, `contacts_per_active_account` with the account population behind it, `handle_cost` or `not_costed`, `underlying_cause` distinguished from the symptom the code recorded, `owning_function`, `routed_state`, `fix_state`, and `deflectable`
- `ticket.contact_reason` corrections proposed per contact with the coding weakness named, kept as proposals rather than applied
- `self_service.coverage_gaps[]` extended with the drivers that have no answer on any surface
- `knowledge[]` seeded with the article requests each deflectable driver justifies, carrying the volume behind them
- `metrics[]` seeded with contact rate per active account and the driver mix, each with its definition and population
- `approvals[]` where a taxonomy change or a bulk recode would be applied to historical tickets
- `open_questions` for every driver whose owning function has not accepted it
- `source_facts` with collection timestamps, `assumptions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Source conflict**: the coded driver distribution and a read of the underlying tickets genuinely disagree, or the reporting layer and the raw ticket record return different volumes for the same window. Preserve both readings, because this list decides where engineering and product spend a quarter, and a taxonomy that buries a login failure inside a billing code sends that quarter to the wrong team.
- **Release integrity**: a driver ranking, a rate, or a trend would go to a prioritization forum without its window, its counting rules, its population, or the sample behind its cause. These figures move roadmaps, and a ranking without its rules cannot be compared with the one that follows it.
- **Security or privacy**: the analysis would carry customer identities, account names, ticket content, agent names, or personal data into an artifact read by functions with no ticket access, or a sampled thread would be quoted with its identifying detail intact.
- **Missing approval**: a taxonomy change or a bulk recode would be applied to historical tickets, which rewrites the record every prior report was computed from and breaks period comparison silently.
- **Production or destructive**: the next action would bulk-update reason codes, fields, or tags on live tickets, firing whatever triggers those tickets match.
- **Connector unreachable**: the reporting layer, the ticket threads, or the active account population exists and cannot be read, so a ranking would describe demand nobody counted or a cause nobody read.

An uncosted driver, an unaccepted routing, an unknown release correlation, and a driver whose owning function is disputed are soft gaps. Proceed with the driver ranked, the gap labeled, and the routing recorded as unaccepted.

## Downstream handoffs

`support-metrics-reporting-desk` is next and needs the driver figures with their definitions, windows, and counting rules, plus the movement this analysis explains, since a metric that moved with a named driver behind it is a finding and the same metric alone is a chart. `knowledge-base-desk` receives the deflectable drivers with their volume, which is the ranked content brief. `self-service-deflection-desk` needs the ranked list itself, since its coverage map is built against it and both must use the same ranking or the two reports will disagree in the same meeting. `support-tooling-automation-desk` needs the taxonomy recommendations with what each change breaks in historical comparison. `workforce-coverage-desk` needs the drivers tied to releases and billing cycles, since those are demand events a forecast has to carry. `queue-backlog-health-desk` needs the drivers the aged tickets cluster into. The routing packets leave the suite entirely, to product, engineering, documentation, billing, and onboarding.

## Quality bar

Good driver work reads the tickets. The ranked list says how many threads were read behind each driver, because that single number separates an analysis from a pivot table, and the readers who matter will ask for it. Volume never appears without contacts per active account beside it, since a support organization that reports a twenty percent volume rise during a thirty percent customer growth is reporting an improvement as a problem. Trends name what changed between the periods, including the taxonomy change nobody mentioned, which is usually the whole story. Miscoding is corrected with the weakness named, so the fix goes into the picker rather than into a reminder to code carefully. Every driver leaves with a function's name on it and a decision to make, because a driver with no owner is a slide. And the prior findings section is the honest part: a driver that has been top three for four quarters and has never been accepted by anyone is reported as unowned rather than presented again as if it were new, since that is the finding the support leader actually needs to take upward.
