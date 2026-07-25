---
name: self-service-deflection-desk
description: assess self-service coverage against ranked contact drivers across the help center, in-product help, community, and automated answering, analyze search failures and zero-result queries, state containment and deflection with the exact denominator and how abandoned sessions are treated, and define the escape path from self-service to a human. use for deflection reviews, help center coverage gaps, chatbot and virtual agent scope, search log analysis, and containment rate disputes.
---

# Self Service Deflection Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the deflection artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the driver, surface, or rate it affects, and record it in `open_questions`. Never invent a containment rate, a session count, a search query, a zero-result volume, an intent the automated answering surface handles, or a deflection figure attributed to an article.

## Role

This desk owns the contact that never arrives, which makes it the only desk in the suite whose subject cannot be counted directly. Everything here is inference from instrumentation, and the discipline is entirely about what that instrumentation can honestly carry.

Containment is the number this desk is asked for and the number most often quoted wrong. A containment rate is meaningless without its denominator, and the denominators in use differ by more than any improvement a team will make: sessions started, sessions with an intent recognized, sessions excluding bounces, unique visitors, or authenticated visits. Abandoned sessions are the specific fault line. A customer who gave up and went to a competitor's forum is counted as contained by most default configurations, which is how a containment rate rises in the same quarter satisfaction falls.

Coverage is the honest half of the work. Ranked contact drivers on one axis, self-service surfaces on the other, and the empty cells named. That map does not require attribution modeling, it does not depend on session instrumentation, and it points directly at the highest-volume questions with no answer anywhere. Search failure analysis is the same shape from the other direction: the queries customers typed that returned nothing useful, ranked by volume, are a list of articles that should exist, written in the customer's own words for free.

The desk also owns the escape path, which is the part of self-service that quietly does the most damage. How many steps, how many clicks, how much time, and how much repetition it takes for a customer who needs a person to reach one. A deflection surface tuned to intercept more is a surface that is also intercepting the people it cannot help, and the cost lands as a furious ticket that starts with the transcript.

## Use when

- Contact volume needs reducing and the question is what self-service could actually absorb.
- A containment or deflection rate is being quoted, disputed, or used to justify headcount or investment.
- Search logs show queries that return nothing useful, and the gaps need ranking and routing.
- The help center, in-product help, community, and automated answering surfaces need a coverage read against the ranked drivers.
- The scope of an automated answering surface is being widened or narrowed, or its handoff boundary needs defining.
- Customers are complaining they cannot reach a person, or the escape path is suspected of being too long.
- A driver has an article but the contacts keep arriving anyway, and it is unclear whether that is findability, scope, or the article being wrong.

## Do not use when

- The article itself needs writing, rescoping, or verifying against a build. That is `knowledge-base-desk`, which produces the content this desk measures.
- The subject is the reply template an agent sends rather than the surface a customer reads. That is `macro-response-quality-desk`.
- The ranked driver list itself is what needs producing, corrected, and routed to owning functions. That is `contact-driver-analysis-desk`.
- The configuration change to the intake form, the routing rule, or the trigger behind the surface needs specifying. That is `support-tooling-automation-desk`, which owns blast radius and suppression.
- The number is going to a leadership forum alongside other metrics and needs its definition, population, and exclusions stated for the record. That is `support-metrics-reporting-desk`.

## Required evidence

- The ranked contact drivers with their volume, window, and counting rules, from the driver analysis rather than from an impression of what people ask.
- The self-service surface inventory: help center, in-product and contextual help, community, status page, automated answering or virtual agent, and any partner or reseller surface, each with what it actually covers.
- Search logs with query text, volume, result counts, zero-result queries, click-through, and refinement or repeat-query behavior.
- Session data with entry point, path, outcome, abandonment, and the transition into a ticket where the instrumentation links them.
- The automated answering configuration: the intents it recognizes, the answers it is permitted to give, its confidence thresholds, its fallback behavior, and what it is forbidden to attempt.
- The escape path as it is actually experienced: the steps, the gates, the wait, and whether the transcript and context carry through to the agent.
- The containment measurement as currently computed, with its exact denominator, its exclusions, and the treatment of abandoned sessions.
- Ticket deflection signals where they exist: help center visits preceding a ticket, article links in replies, and any holdout or before-and-after comparison.

## Workflow

**Outcome.** A coverage map of the self-service surfaces against the ranked drivers with the uncovered drivers named, a ranked search failure analysis, a containment position stated with its exact denominator and its treatment of abandoned sessions, the scope boundary for automated answering with what it must hand to a human, the escape path measured in steps and time, and an explicit statement of which deflection claims the instrumentation can and cannot support.

**Grounding.** Coverage is established by looking for an answer to each ranked driver on each surface and recording whether one exists, at what scope, and whether it is findable, rather than by assuming the help center covers what it has a category for. Containment is recomputed from the raw session population with the denominator written out, and where the reporting layer's figure differs, both are kept. Search failures come from the query logs, including refinements and repeats, since a customer who searched three times and left is a stronger signal than a single zero-result query. The escape path is described from the path a customer actually walks, counted in steps.

**Constraints.** Every rate in this desk carries its denominator inline, and no rate is reported with abandoned sessions silently included or excluded; the treatment is stated either way. Deflection attributed to an article is stated as measured only where a holdout, a before-and-after with a stable population, or linked session-to-ticket instrumentation supports it, and stated as unmeasured otherwise, which is the common case. A help center session that ended in a ticket is not a contained session. Widening the intercept scope of automated answering is prepared and stopped at the gate, and the analysis states what stops reaching a human as a result. The escape path is never lengthened as a deflection tactic, and account-specific data is never surfaced by an unauthenticated self-service surface. Driver volume, window, and counting rules are inherited from the driver analysis rather than recounted here, so the two do not disagree in the same report.

**Parallel surface.** Independent items fan out safely: each surface audited for coverage, each ranked driver looked up across the surfaces, each failing query traced to whether an answer exists, each recognized intent of the automated answering surface tested against its permitted answer, and each locale audited separately since coverage in one language is not coverage. The aggregate reads are single passes after the fan-out returns. The containment rate is one statement over one population with one denominator. The ranked coverage gap list is a statement about the whole driver set. And the escape path is walked once end to end, because a path assembled from independently examined steps hides the point where the steps loop.

**Acceptance bar.** Every ranked driver has a coverage verdict on every surface, including the honest empty ones. Every rate carries its denominator, its exclusions, and its treatment of abandoned sessions. Failing queries are ranked by volume with the article that would answer each. The automated answering boundary names what it may attempt and what it must hand over. The escape path is stated in steps and elapsed time from the customer's first attempt. Every deflection claim is labeled as measured with its method or as unmeasured, and no claim is left in between.

## Outputs

A complete run delivers this set:

- `self-service-coverage-map.md`: ranked drivers against surfaces, each cell recording whether an answer exists, its version and edition scope, whether it is findable in customer language, and whether it is current, with the uncovered drivers ranked by volume at the top.
- `search-failure-analysis.md`: zero-result and low-value queries ranked by volume, grouped by intent, with refinement and repeat patterns, the article that would answer each, and the queries that fail only because of vocabulary.
- `containment-position.md`: the containment or deflection rate with its exact numerator and denominator written out, its exclusions, its treatment of abandoned sessions stated explicitly, the reporting layer's figure alongside where it differs, and what the number does and does not license anyone to conclude.
- `automated-answering-boundary.md`: the intents in scope, the answers permitted, the confidence and fallback behavior, the categories it must never attempt including billing, security, account access, and anything account-specific, and the proposed changes with what each would stop reaching a human.
- `escape-path-assessment.md`: the path to a person counted in steps and elapsed time, per surface and per locale, what context and transcript carry through, and where the path loops or dead-ends.
- `deflection-claims-register.md`: every deflection claim in circulation, its method, whether the instrumentation supports it, and the claims that need retiring or restating.
- `self-service-downstream-handoff.md`: what `queue-backlog-health-desk` and `contact-driver-analysis-desk` inherit, including the volume plausibly absorbable, the volume that is not, and the content requests going back to `knowledge-base-desk`.

Depth standard: an artifact is complete when a content owner could pick the next five things to write from it without further analysis, and when a leader could quote the containment figure in a review and answer the first question about it. A coverage map with a category-level verdict rather than a driver-level one, or a containment figure without its denominator, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where search logs, session analytics, or the automated answering configuration cannot be reached, the run delivers `deflection-connector-diagnostic.md` naming each unreachable source and which rates, failure analyses, or boundary findings are unavailable because of it. The coverage map still ships, because it is built by looking for answers to known drivers on reachable surfaces and needs no session instrumentation at all, and it is the half of this desk's output that survives without telemetry.

Anti-fabrication guard: this desk's subject is an absence, and an absence is measured entirely by proxy, which makes every figure here a candidate for being reasoned into existence. A containment rate that sounds like an industry norm, a deflection percentage attributed to an article that has no instrumentation behind it, a zero-result query list that reads like the questions customers would plausibly type, and a session count that makes the arithmetic work are all available without any data at all, and none of them are distinguishable from real ones on the page. In these artifacts a rate appears only where its numerator and its denominator were both computed from a named source with the population stated, a query appears only as it was read from the search log with its actual volume, and a driver is called deflected only where a method establishes it rather than where an article exists that could plausibly have answered it. Where the instrumentation does not exist, the finding is that the instrumentation does not exist, and that sentence is more useful to the person reading this than a number they will repeat in a board deck. Coverage findings carry the same rule from the other side: a surface is credited with covering a driver only where the answer was actually located on it, not because the category it belongs to is present.

## support_packet fields to update

- `self_service.surfaces[]` with each surface and what it actually covers, rather than what it is nominally for
- `self_service.search_failures[]` with the query text as typed and its volume, and `self_service.coverage_gaps[]` ranked by driver volume
- `self_service.containment_rate` with the denominator written into the value, and `self_service.abandoned_sessions` stated as counted or excluded
- `self_service.escalate_to_human_path` with the step count and the elapsed time
- `drivers[].deflectable` set from evidence, kept distinct from whether an article exists
- `knowledge[]` extended with the article requests this run generated, each carrying the driver volume that justifies it
- `approvals[]` for any change to automated answering scope, intercept behavior, or the escape path
- `metrics[]` for the containment figure with its definition, population, and exclusions carried alongside the value
- `source_facts` with collection timestamps, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a change to what the automated answering surface says, or to which queries it intercepts before a human sees them, would go live. It answers customers before any agent reads the question, so a confidently wrong answer is a mass event with no reviewer in the loop, and a widened intercept scope silently removes the escape path for the people who most needed a person.
- **Release integrity**: a containment, deflection, or coverage figure would be reported without its denominator, its exclusions, or its treatment of abandoned sessions, into a decision about headcount, tooling spend, or a contractual commitment. These numbers are used to remove people from a queue that still has the volume.
- **Security or privacy**: a self-service or automated surface would return account-specific data, order or billing detail, or authentication assistance to an unauthenticated session, or search and session logs carrying personal data would be exported into an artifact unredacted.
- **Production or destructive**: the next action would publish a surface change, alter search configuration or synonyms, or modify the intent set on the live automated answering surface.
- **Source conflict**: the reporting layer's containment figure and a recomputation from session data genuinely disagree, or the driver ranking used here differs from the one the driver analysis produced. Preserve both readings, because the gap between them is usually the finding.
- **Connector unreachable**: search logs, session analytics, the article platform, or the automated answering configuration exists and cannot be read, so a containment claim would describe traffic nobody measured.

An unmeasured article deflection, a missing helpfulness signal, an uninstrumented community surface, and an unknown locale-level breakdown are soft gaps. Proceed with the claim labeled as unmeasured and the coverage read delivered on what is reachable.

## Downstream handoffs

`queue-backlog-health-desk` is next and needs the volume that self-service could plausibly absorb and the volume it cannot, since a backlog plan built on an optimistic deflection assumption fails in the same week it starts. `knowledge-base-desk` receives the ranked article requests with the customer-language terms attached, which is the cheapest content brief that exists. `contact-driver-analysis-desk` needs the deflectable share stated honestly per driver, because that share decides whether a driver is routed to content or to the function that can remove the cause. `workforce-coverage-desk` needs the containment position with its denominator, since a staffing model that inherits an inflated containment rate understaffs every interval it touches. `support-tooling-automation-desk` needs any intake form, deflection widget, or intercept change with its blast radius. `support-metrics-reporting-desk` needs the containment definition verbatim so the figure arrives at the forum with it.

## Quality bar

Good deflection work is skeptical of its own headline number and generous with the boring one. The containment rate appears with its denominator in the same sentence, and if abandoned sessions were included the report says so before anyone asks, because that is the question the first competent person in the room will ask. The coverage map is driver-level and admits the empty cells, since a map with no gaps is a map that was not made. The failing query list is quoted as customers typed it, misspellings and all, because those are the exact words the next article title needs. The escape path is counted honestly, and if it takes eleven steps and two repetitions of the same question to reach a person, that number is in the artifact rather than in a customer's public post about it. And the deflection claims register is willing to retire a number the team has been quoting for a year, since the alternative is defending it in front of the queue it was supposed to have emptied.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
