---
name: bid-evaluation-desk
description: evaluate submitted bids by scoring each response independently against the published criteria with the evidence in the response cited for every score, reaching consensus only after independent scoring, normalizing total cost onto a common term scope and volume, leaving unanswered criteria unscored, comparing terms exceptions and reference findings, and producing an award recommendation with the record behind it. use for bid evaluation, weighted scorecards, evaluator consensus, tco normalization, reference checks, demonstration assessment, award recommendations, and bidder debriefs.
---

# Bid Evaluation Desk

## Suite workflow mode

This desk is part of the Procurement Vendor Management Command Desk suite. Inside a workflow, evaluate the bid set, produce the artifact set, update `procurement_packet`, and continue into `security-privacy-review-desk` with the recommended supplier and the diligence scope already set by the tier. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet and the discipline that a bid comparison is valid only across a common basis.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act would bind the company or reach a supplier, there is a security or privacy exposure, sources genuinely disagree on a load-bearing fact, a position would leave the company without the evidence behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the bid or criterion it affects.

Never invent a score, a passage in a response, a reference conversation, a demonstration result, a price component, a normalization assumption, an evaluator's view, or a criterion a bid did not answer.

## Role

Own the evaluation and the record it leaves. That means independent scores from each evaluator against the criteria exactly as published, each score citing the passage in the response that produced it, a consensus reached only after those scores exist, a total cost comparison restated onto a common term, scope, and volume with every normalization visible, a terms exception comparison showing what each bidder would actually sign, reference and demonstration findings recorded as observed, and an award recommendation that states the scoring outcome and the commercial position separately so a reader can see which one decided it.

The normalization is the analysis. The headline price rarely survives a restatement onto common volumes, a common term, and a common scope, and the bid that looked cheapest at submission frequently is not the cheapest commitment. The integrity risk is equally specific: the decision gets made first and the scorecard gets filled in to support it, and that failure is detectable precisely because the weights or the scores moved once the bids were open. A losing bidder with a relationship inside the company will ask how the decision was reached, a regulated process gives them a formal route to ask, and the answer is whatever the record shows.

## Use when

- Bids have closed and have to be scored against the published criteria.
- Evaluator scores have to be gathered independently and then reconciled into a consensus with the divergence recorded.
- Prices arrived in different structures and total cost has to be normalized onto a common basis.
- A bid did not address a criterion and the treatment has to be decided and recorded.
- Terms exceptions across bidders have to be compared for what each supplier would actually sign.
- Reference checks and demonstrations have to be planned, run, and recorded as findings.
- An award recommendation and its supporting record have to be produced, along with the debrief position for each unsuccessful bidder.
- A criterion or a weight is being questioned after submissions were opened.

## Do not use when

- Criteria and weights are not yet fixed and dated: `requirements-specification-desk`.
- The event is still running, questions are open, or submissions have not closed: `sourcing-event-desk`.
- The supplier's security, privacy, or integrity evidence is the question: `security-privacy-review-desk` and `supplier-integrity-screening-desk`, which run against the recommended supplier.
- The award is settled and the commercial position has to be built: `pricing-negotiation-desk`.
- The contract request, approval chain, and signature routing are the work: `contract-execution-routing-desk`.
- There is one supplier and no competitive set: `pricing-negotiation-desk`, with the sole source basis recorded by `procurement-policy-desk`.

## Required evidence

- The submitted bids in full, including every attachment and the pricing templates as returned.
- The evaluation criteria, weights, and scoring scale as fixed and dated before issue, plus any addendum that changed them and when.
- The evaluator panel, their roles, and their independence from the outcome.
- The common assumptions bids were told to price against, including volume, term, ramp, and scope.
- The exceptions each bidder declared to the terms, the service levels, and the statement of work.
- Demonstration and proof of concept results as observed, with who observed them.
- Reference contacts, what is to be asked, and who is making the calls.
- The risk tier and any diligence findings already available, since an unremediated finding is a commercial position before signature.
- The incumbent's current pricing and switching cost, where the incumbent is bidding.

## Workflow

**Outcome.** A scored bid set with evidence citations, a consensus record, a normalized total cost comparison, a terms exception comparison, reference and demonstration findings, an award recommendation with the scoring outcome and the commercial position stated separately, a debrief position per unsuccessful bidder, and a permanent record of any change to criteria or weights with its date.

**Grounding.** The response is the evidence. A score cites the passage that produced it, and where the response does not address a criterion, the criterion is unscored rather than estimated. A supplier's claim in a bid is a bid claim; it becomes an obligation only if it enters the agreement, and the evaluation says which of the two it currently is.

**Mandated ordering.** The evaluation runs in this order:

1. Score independently, each evaluator against the published criteria, before evaluators confer.
2. Reach consensus, recording where evaluators diverged, what resolved it, and who was present.
3. Normalize total cost across the whole bid set onto a common term, scope, and volume.
4. Recommend the award against the record the first three steps produced.

The order is mandated because the value of five scores is that five people formed them separately; a panel that scores together produces one confident opinion recorded in five columns, and the independence cannot be recovered afterward. Normalization comes after consensus so the qualitative assessment is not anchored to the price, and the recommendation comes last so it is visibly derived from the record rather than the record being assembled to support it.

**Constraints.**

- Cite evidence for every score. A number with no passage behind it is an impression, and it is the entry a challenge starts from.
- Leave unanswered criteria unscored and report them as unanswered. A middle score assigned to keep the arithmetic tidy converts a bidder's silence into a defensible mark and hides the finding an evaluation panel most needs.
- State every normalization: the common term, the volume assumed, what was added because a bid excluded it, what was removed as out of scope, and the currency and rate basis. A comparison whose assumptions are invisible is a conclusion.
- Include the whole horizon: license, implementation, integration, migration, training, support, internal effort, and exit. The cheapest license is routinely the most expensive commitment.
- Compare terms exceptions as part of the evaluation rather than deferring them. A bidder who declined the liability position, the data protection terms, or the service level remedy has told the company what the negotiation will cost.
- Record reference findings with who was spoken to, at which organization, what was asked, and what they said, and record demonstration findings as what was observed rather than what was presented.
- Any change to criteria or weights is recorded permanently with its date and whether bids were visible at the time, whatever the reason for the change.

**Parallel surface.** Bids are independent under scoring and fan out: each evaluator scores each bid against each criterion at the same time, reference calls run per bid, and demonstration assessments run per supplier. Three steps are aggregates and run once after the fan-out returns. Consensus is a single pass after independent scoring and is never interleaved with it, for the reason stated in the mandated ordering. Normalization is a single pass over the whole bid set, because restating one bid onto a common basis is meaningful only relative to the others and a bid assessed alone is a review rather than a comparison. The award recommendation is a single pass, since it weighs the scoring outcome against the commercial position across the field.

**Acceptance bar.** Every score cites its evidence or is recorded as unanswered. The consensus record names the divergences, what resolved them, and who was in the room. The normalized comparison states every assumption applied to every bid. Terms exceptions are compared clause by clause. Reference findings name the person, the organization, and the question. The recommendation states the scoring outcome and the commercial position separately, and names what would have changed it.

## Outputs

A complete run delivers the set:

- `independent-scores.md`: each evaluator's scores per bid per criterion, with the cited passage behind each and the date recorded before evaluators conferred.
- `consensus-record.md`: the agreed score set, every divergence with the reasoning that resolved it, who was present, and any score that remained contested.
- `unanswered-criteria-register.md`: per bid, the criteria the response did not address, what was asked, and the effect on the comparison, left unscored.
- `normalized-cost-comparison.md`: every bid restated onto the common term, scope, and volume, with each normalization shown, the full horizon components, and the ranking before and after normalization.
- `terms-exception-comparison.md`: what each bidder would actually sign, clause by clause, with the commercial consequence of each exception.
- `reference-findings.md`: who was spoken to, at which organization, what was asked, what was said, and where a reference could not be obtained.
- `demonstration-findings.md`: what was observed, by whom, against which requirements, and what was asserted rather than shown.
- `award-recommendation.md`: the recommendation with the scoring outcome and the commercial position stated separately, the risk position carried in from diligence, and what would change the recommendation.
- `bidder-debrief-positions.md`: what each unsuccessful bidder is to be told, prepared and not sent.
- `criteria-change-log.md`: every change to criteria or weights, its date, its reason, and whether bids were visible at the time.
- `bid-evaluation-downstream-handoff.md`: the recommended supplier, the open exceptions, and the commercial position the negotiation stage inherits.

Depth standard: an artifact is complete when a person who was not in the room could follow the decision from the criteria to the recommendation. "Supplier scored highest" is an outcome; a scorecard where each mark cites the passage that earned it, a normalized comparison showing what was added to each bid and why, and a recommendation that says which of scoring and price decided it is a record. A reference finding is complete when it names the person and the question rather than summarizing an impression.

Where no demonstration or proof of concept was run, `demonstration-findings.md` states that with the reason rather than being dropped, because a recommendation made without observing the product is a different recommendation. Where a bid, a pricing template, or the criteria record cannot be reached, `bid-evaluation-diagnostic.md` names the gap and no score is issued against material that was not read.

A scorecard is the most convincing document in this suite and the easiest to complete without evidence, because every cell wants a number and a blank cell looks like work left undone. The specific failure is the tidy matrix: a score in every position including the criteria a bidder never answered, a reference summary assembled from what the supplier said its references would say, a demonstration finding written from the slides rather than the session, and a normalization assumption adjusted until the preferred bid came out ahead. Each of those survives as the justification for an award that cannot be rescored later. An unanswered criterion stays visibly unscored, a reference that was not reached is recorded as not obtained with who was contacted, and a normalization the evidence does not support is written as an assumption with its effect on the ranking stated in the same place.

## procurement_packet fields to update

- `bids[]` per supplier: `commercial_summary`, `normalized_tco`, `scores` with the evidence for each, `unanswered_criteria`, `exceptions_taken`, `references_checked`, `demonstration_findings`, `risk_flags`.
- `evaluation.independent_scoring_complete`, `consensus_record`, `normalization_basis`, `shortlist`, `award_recommendation`, `award_basis`, `unsuccessful_bidder_position`, `criteria_change_log`.
- `commercial.price_structure`, `quoted_price`, `term_structure` as the bids state them, carried for the negotiation stage.
- `commitment_class` held at `internal_recommendation` until an award is authorized and communicated.
- `approvals` for the award decision, with the amount at stake and the authority basis.
- `source_facts` with locator and as-of date, `assumptions`, `open_questions`, `artifacts`, `current_stage`, `completed_stages`, `next_stage`.

## Halt conditions

- **Release integrity**: an award recommendation would leave the panel without the scoring evidence behind it, or a score or weight would be adjusted after bids became visible. This is the defining integrity failure of the profession, and it is detectable exactly because the numbers moved after the bids were open. A losing bidder will eventually ask how the decision was reached, and the answer is whatever the record shows.
- **Approval**: the award decision itself, and any decision to disqualify a bid, to reopen scoring, to accept a non-conforming submission, or to proceed with an unremediated risk finding. The authority the policy names decides; this desk recommends.
- **Production or destructive**: the next act would communicate an award, a rejection, a price, a ranking, or an intention to any bidder. Telling a supplier they have won ends the negotiation before it starts, and every concession available before that sentence is gone after it.
- **Security or privacy**: bid contents would reach another bidder or the incumbent, or an evaluator has an undeclared relationship with a bidder. A conflict of interest inside the panel is the finding people are least comfortable raising and most likely to leave out.
- **Source conflict**: two evaluators read the same passage as meeting and not meeting a criterion and the divergence is load-bearing, or the pricing template and the narrative in a bid state different prices. Record both readings and route the conflict rather than resolving it toward the preferred bid.
- **Connector unreachable**: a submission, a pricing template, or the criteria record exists and cannot be read, so a score or a comparison would rest on material nobody opened.

An unreturned reference call, a demonstration not yet scheduled, an incomplete diligence workstream, and a clarification a bidder has not answered are soft gaps. Record them against the bid, label the assumption, and continue with the criteria those gaps affect marked as pending rather than scored.

## Downstream handoffs

`security-privacy-review-desk` inherits the recommended supplier, the security content of their response, and the exceptions they declared to the security requirements. `supplier-integrity-screening-desk` inherits the contracting entity from the bid rather than the brand from the proposal. `pricing-negotiation-desk` inherits the normalized comparison, the runner-up position that is the credible alternative, the declared exceptions, and the switching cost, which together define what the company can actually walk away to. `contract-execution-routing-desk` inherits the winning response, since the bid and the specification both become exhibits. The debrief positions stay prepared and unsent until the award is authorized and the agreement is executed.

## Quality bar

A good evaluation is one the panel would be comfortable showing to the bidder who lost. Every score points at a sentence in a response. The normalization is on the page, so the argument is about the assumptions rather than about the conclusion. The unanswered criteria are visible, because three bidders leaving the same criterion blank is a finding about the requirement rather than about the bidders. The recommendation separates what the scoring said from what the price said, since a panel that merges them cannot explain a decision where the two disagreed. And the criteria change log is empty or complete, both of which are answers; the version that is neither is the one a challenge is built on.
