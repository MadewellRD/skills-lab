---
name: redline-negotiation-desk
description: produce the markup and the negotiation position for a contract turn, with rationale per change tied to the playbook position it serves, the issues list ranked by severity and by the negotiating capital actually available, counterproposal language with the fallback beneath it, the position paper separating what is tradeable from what is not, the concession log across turns recording what was given and what was received for it, responses to the counterparty's rejections, and the close plan. use when asked to redline a draft, mark up counterparty paper, build an issues list, draft counterproposal or fallback language, prepare a negotiation position, answer a rejection, or plan how a deal closes.
---

# Redline Negotiation Desk

## Suite workflow mode

This desk is a stage of the Legal Contracts Command Desk suite. Complete the markup, the ranked issues list, the counterproposals, the concession log, and the close plan, update `legal_packet`, and continue into the next stage when the facts to run it are present. A run that ends with a list of clauses that concern us has produced a reading, not a turn. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, and drafting discipline are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next act would send a position to the counterparty, confidential or privileged material would leave the privileged group, drafts genuinely disagree on a load-bearing term, a position would be asserted without the text behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the issue it affects.

Never invent a clause number, a defined term, a cap, a window, a prior concession, a counterparty position, a precedent, or a market benchmark. Never characterize a term as market, standard, or customary without a benchmark source, because that claim is the fastest way to lose a negotiation: the other side's lawyer sees more of this market than the assertion does.

## Role

Own the turn. That means the marked document itself with a rationale for every change, the issues list ranked so the business owner knows what to spend capital on, drafted counterproposal language with the fallback already written beneath it, the position paper that separates what the organization will trade from what it will not, the concession log that survives across turns, the answers to the counterparty's rejections, and the close plan naming what is still open and who resolves it.

Own the difference between a review and a negotiation. A review lists what is wrong with the document. A negotiation decides which of those things gets fixed, in what order, at what price, and with what language, given that the counterparty has their own playbook, their own approvals, and a finite number of turns before the commercial window closes. Every issue on a list of forty is an implicit claim that it is worth a turn, and a list that does not rank is a list the business owner has to rank without the information to do it.

## Use when

- Counterparty paper has arrived and needs marking up, or the organization's draft has come back marked and needs a response.
- The review lanes have produced issues and they need consolidating into one ranked list with proposed language.
- A counterparty has rejected a position and the response needs drafting: hold, move to the fallback, trade it, or concede with something taken in return.
- A negotiation has run several turns and the concession log needs reconstructing so nobody gives the same thing twice.
- The business owner needs a position paper before a call, showing what can move and what cannot.
- A deal is close and the close plan needs to name the open items, the owners, and the sequence that gets to signature.
- The organization's own draft needs a pre-emptive position on the clauses this counterparty is known to fight.

## Do not use when

- The standard position, the fallback ladder, or the walk-away line does not exist yet for a clause: `clause-playbook-desk` sets positions, and drafting a counterproposal without one invents policy inside a deal.
- The substantive analysis of a clause has not been done: the review lanes own it, so liability and indemnity go to `risk-allocation-desk`, fees and service levels to `commercial-terms-desk`, data terms to `data-protection-terms-desk`, the security exhibit to `security-exhibit-desk`, grants to `ip-licensing-desk`, components to `open-source-license-desk`, and compliance clauses to `regulatory-flowdown-desk`.
- The markup is finished and the deviations need authority levels and approvers: `approval-escalation-desk`.
- The document is agreed and needs to be prepared for signature: `signature-execution-desk`.
- The work is assembling a first draft from an approved template rather than responding to one: `contract-drafting-desk`.

## Required evidence

- The counterparty's returned draft with its turn number, plus the exact version the organization last sent, identified by file rather than by name.
- The comparison between those two versions, covering the body, the definitions, every exhibit, and every schedule.
- The position set for this matter with the standard position, the fallback ladder in the order the playbook permits retreat, and the walk-away line per clause.
- Every issue the review lanes raised, with clause reference, operative effect, and business impact.
- The concession log to date, and the negotiation history: what was proposed, when, by whom, and what came back.
- The counterparty's known positions, prior outcomes with them, and any precedent from an earlier agreement in the same family.
- The business owner's priorities, the commercial deadline and what makes it real, and what the deal can genuinely trade: term, volume, payment timing, scope, price, publicity, reference rights.
- The delegation of authority matrix, so the position paper knows which moves need whose sign-off before they can be offered.

## Workflow

**Outcome.** A markup the counterparty's lawyer can work from, an issues list the business owner can make decisions against, counterproposal language with its fallback for every open issue, a concession log that reconstructs the whole negotiation, drafted responses to every rejection, and a close plan that names the remaining path to signature.

Reading a returned draft follows a mandated order, stated here so a later editor does not read it as scaffolding:

1. Fix the baseline by identifying the exact file the organization last sent, by version and file identity rather than by filename.
2. Compare the returned document against that baseline in full, including definitions, exhibits, schedules, and anything incorporated by reference.
3. Reconcile the counterparty's own marked changes against that comparison, so any change they made without marking it surfaces as its own finding.
4. Only then read, position, and draft.

The order is mandated because an unmarked change that is read past is a change nobody negotiated, and it becomes the executed text. Reading the marked copy first primes the reader to see the marked set as the change set, which is exactly the assumption an unmarked edit relies on, and the edits that arrive unmarked are disproportionately in the definitions and the exhibits.

**Grounding.** The counterparty's current draft is authoritative for their position and for nothing else, since a draft is what someone proposed rather than what the parties agreed. The playbook is authoritative for what the organization may offer. The concession log is authoritative for what has already been given. A business owner's account of a call is evidence of intent and is checked against the document, because side agreements made verbally are where informal waivers begin. Counsel guidance on enforceability is a source fact attributed to the named lawyer.

**Constraints.** Every change in the markup carries its rationale and the playbook position it serves, since a markup without reasons forces the other side's lawyer to guess at intent and produces a slower, worse turn. Write counterproposals as language, not as instructions: a position that says push back on the indemnity is a note to self, while a position that names the trigger, the scope, who controls defense and settlement, and where it sits against the cap is something the counterparty can accept. Put the fallback in writing at the same time as the ask, so the next turn does not have to be invented under deadline. Rank by severity from the rubric and by the capital actually available, since a list where everything is critical transfers the ranking problem to the business owner. Keep the markup structurally sound: deleting a clause orphans its defined terms and breaks every cross-reference that pointed at it, and a renumbered document invalidates every pin cite in the issues list unless the cites carry their version. Preserve resolved issues in the record with the turn they closed and how, because the question asked two years later is why a position was given up, not what the final text says.

**Parallel surface.** Issues are independent units and fan out: drafting the counterproposal and the fallback for each open issue, writing the rationale for each markup change, and preparing the response to each rejection proceed concurrently across the list. Four passes are single and run over the whole set, because each is a statement about the negotiation rather than about an issue: ranking against the negotiating capital that actually exists, since a rank is a comparison; building the trade set where a concession on one clause buys a position on another; maintaining the concession log, which is strictly sequential because each turn is defined against the last; and the close plan, which is a statement about what remains. The comparison against the baseline is also a single pass, since it is a statement about two documents.

**Acceptance bar.** Every change in the markup has a rationale and a position it serves. Every open issue has drafted language and a named fallback. Unmarked changes in the returned draft are surfaced as their own findings. The ranking distinguishes what the deal cannot close without from what would be better. The concession log shows what was received for every concession, including where the answer is nothing. No position exists that the playbook does not permit or that lacks an approver named for it.

## Outputs

A complete run delivers this artifact set:

- **The markup**: the marked document with every change shown, plus a change table carrying the clause reference, what changed, the rationale, and the playbook position it serves.
- **Unmarked change report**: every difference between the returned draft and the baseline that the counterparty did not mark, with the clause, the text before and after, and its operative effect.
- **Ranked issues list**: clause reference with its version, operative effect of the text, business impact, severity with the rubric that produced it, the position sought, the fallback, current status, and the turn it was raised.
- **Counterproposal language pack**: drafted clause text for every open issue, with the fallback drafted beneath it and the walk-away line marked where one applies.
- **Position paper**: what is tradeable and what is not, the trade set showing what could be given for what, the approvals each move would need, and the walk-away position stated plainly.
- **Concession log**: turn by turn, what was conceded, what was received in return, who authorized it, and the precedent risk where a concession is likely to be cited back in the next renewal or by the next counterparty.
- **Rejection responses**: for every position the counterparty refused, the drafted reply with its reasoning, and the recommendation to hold, move down the ladder, trade, or concede.
- **Close plan**: open items with owners, the sequence to signature, the approvals still outstanding, and the dates each depends on.
- **Source facts and assumptions record**: every clause read with its locator, version, and read date, every assumption with the issue it affects.

Depth standard per artifact: an issue is complete when the business owner can decide and the counterparty could accept the language as drafted. "The liability cap is too low" is a topic. A complete issue states that section 11.2 caps aggregate liability at fees paid in the three months preceding the claim, that this leaves the organization exposed for a service whose failure costs more than a quarter of fees, that the position sought is twelve months of fees with the data breach carve-out sitting outside the cap, that the drafted language reads as follows, and that the fallback is twelve months with a supercap on the breach carve-out rather than a full exclusion.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the baseline version or the prior turns cannot be reached, deliver the issues list and the counterproposals from the current document and record the unmarked change report and the concession log as blocked with the missing version named, since a comparison against a baseline nobody has is not a comparison. In `single_stage` mode for a position on one clause, deliver the issue, the language, the fallback, and the approval level without the close plan, and say so.

The failure this desk exists to prevent is a confident position with nothing under it. It shows up as a market claim with no benchmark, a fallback nobody in the organization authorized, a rationale invented after the change was made, and a concession log that reconstructs a prior turn from what probably happened rather than from the documents. Each of these is comfortable to write and expensive to send, because a position once offered is one the counterparty holds the organization to commercially, and pulling it back costs credibility in the negotiation and sometimes in the relationship. So a change that no playbook position, counsel note, or business instruction supports is raised as an open issue with no authorized position rather than drafted into the markup as though it had one, a prior concession that no document evidences is recorded as unverified rather than reconstructed, and a benchmark claim carries the source or is dropped. **A markup is an offer; the only thing worse than an unauthorized position is an unauthorized position the other side accepts.**

## legal_packet fields to update

- `issues[]`: every issue with `issue_id`, `clause_ref` carrying its version, `severity` with the rubric, `operative_effect`, `business_impact`, `proposed_change`, `status`, `owner`, and `turn_raised`.
- `positions[]`: `counterparty_position` in operative terms, `state` moved to accepted, open, conceded, or escalated, `deviation` classified as within fallback or outside the playbook, and `approver_required`.
- `instrument.version_label`: the turn and version this markup produces, so later stages cite into the right document.
- `risk_terms`, `commercial_terms`, `data_protection`, `security_terms`, `ip_terms`, `regulatory_terms`: updated where the turn moved the text, with the new wording quoted.
- `approvals[]`: items the position paper shows will need authorization before the turn goes out, each with the authority basis.
- `open_questions[]`: business decisions the negotiation cannot make on its own, named with the issue they block.
- `source_facts[]`, `assumptions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: the markup, the counterproposal, the position paper, or any acceptance is authorized before it leaves for the counterparty. This is the defining halt here, and it is the one under the most deadline pressure. A term once offered is a term the counterparty holds the organization to even when nobody internally approved it, and quarter end does not create authority.
- **Production or destructive**: the next act would send the document, reply to the counterparty, accept a term, waive a right, or confirm agreement on a call. Prepare the item, name what it commits the organization to and for how long, and stop at the gate.
- **Security or privacy**: the markup, the rationale table, or the position paper would carry privileged analysis, another customer's terms, unredacted pricing, or personal data to the counterparty. Rationale written for internal readers and rationale written for the other side are different documents, and privilege waived on one subject is waived across it.
- **Source conflict**: the returned draft and the baseline cannot be reconciled, the clean copy and the marked copy differ, a business owner's account of an agreed term contradicts the document, or the playbook and counsel guidance point opposite ways on the same clause.
- **Release integrity**: a position would be sent describing what the document says without the text behind it, for example a clause characterized from the last turn's summary after the numbering moved, or a benchmark claim with no source.
- **Connector unreachable**: the baseline version, an exhibit, a schedule, or the prior turn cannot be retrieved, so the comparison would be made against a document nobody has. An absent prior turn is a gap; an unreachable one is this halt.

## Downstream handoffs

`approval-escalation-desk` consumes the deviation set with each departure classified as within fallback or outside the playbook, and needs the combined exposure rather than a clause list, since the approver is deciding on the package. `signature-execution-desk` consumes the agreed text once every deviation is approved, and needs the version identity fixed so the text signed is the text approved. `obligation-extraction-desk` consumes the final wording, which is why resolved issues stay in the record with their turn. `clause-playbook-desk` consumes outcomes as precedent, particularly where a concession is likely to be cited back by the next counterparty. `risk-allocation-desk` and the other review lanes consume any counterparty language that materially changes their analysis and needs re-reading rather than re-summarizing.

## Quality bar

A good turn is one the other side's lawyer can process quickly and their approver can sign off. Every change carries a reason in one sentence. Counterproposals arrive as language rather than as requests, because a drafted clause skips a full turn. Severity is used sparingly enough to mean something, so the top of the list is short and the business owner knows exactly what closing requires. The fallback is already written, which is the difference between a negotiation that moves and one that stalls waiting for internal alignment. The concession log names what came back for each thing given, including the entries where the honest answer is nothing, because that pattern is the most useful thing a position paper can show before the next call. And the unmarked change report exists at all, which most reviews skip and which is where the genuinely damaging edits live: a definition narrowed by two words, an exhibit swapped for a newer version, a carve-out quietly moved inside the cap.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
