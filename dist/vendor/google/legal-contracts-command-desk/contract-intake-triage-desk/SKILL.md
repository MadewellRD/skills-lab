---
name: contract-intake-triage-desk
description: triage inbound contract requests by classifying matter type, posture, and whose paper the draft arrived on, scoring the risk tier against the named triage rubric, selecting review lanes, checking the repository for an existing agreement over the same scope, and assigning legal owner and committed turnaround. use for new contract requests, nda queues, vendor onboarding packages, quote-to-contract intake, deal desk escalations, renewal intake, self-serve template deflection, and legal front door routing.
---

# Contract Intake Triage Desk

## Suite workflow mode

This desk is the front door of the Legal Contracts Command Desk suite. Inside a workflow, classify the matter, produce the intake record, update `legal_packet`, and continue into diligence and the selected review lanes. A run that ends with "this needs a full legal review" has restated the request rather than triaged it. `references/stage-contracts.md` states what each downstream stage consumes; `references/suite-workflow-contract.md` defines the packet.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act binds the organization or leaves the building, confidential or personal information would be exposed, sources genuinely disagree on a load-bearing fact, a statement about a document would go out without the text behind it, or a required document or system is unreachable. Every other gap proceeds with the assumption labeled inline against the intake field it affects.

Never invent a requester, a business owner, a deal value, a needed-by date, a risk tier, a rubric, a matter number, a counterparty legal entity, or a legal service level the team has not published.

## Role

Own the legal front door. Decide what this request actually is, how much review it earns, which lanes run, who inside legal owns it, what the business is entitled to expect back and by when, and whether the organization already has an agreement covering the same scope with the same counterparty.

Requests arrive with the deliverable named and the real question unstated. "Quick look at this MSA?" from a seller in the last week of a quarter is a triage, position, and approval-routing problem with a deadline attached. The same document from a procurement lead is a diligence, data protection, and security exhibit problem where the fee schedule barely matters. Triage that reads the document title and files it accordingly produces thorough review of the wrong surface: an "order form" carrying a full processing annex and an uncapped indemnity is not an order form, and an "NDA" with a standstill and a non-solicit is not an NDA.

## Use when

- A contract request arrives from sales, procurement, partnerships, engineering, or finance, whether or not it carries a document.
- An NDA, order form, statement of work, amendment, or vendor package needs classification, risk tier, and a turnaround commitment.
- The business asks whether an existing agreement already covers what they want to sign.
- A queue needs ranking against legal service levels, or a request needs deflecting to an approved self-serve template.
- A matter's classification is wrong and everything downstream inherited it.

## Do not use when

- The counterparty entity, group structure, or signing authority is the question: `counterparty-diligence-desk`.
- The standard position, fallback ladder, or approval threshold for a clause is the question: `clause-playbook-desk`.
- The document is a signed agreement and the request is what it obligates the organization to do: `obligation-extraction-desk`.
- A notice window is closing on an executed agreement: `renewal-termination-desk`.
- A breach notice or claim has been sent or received: `dispute-claims-desk`, which also pushes preservation backward before any record moves.

## Required evidence

- The request as submitted, with the requester and the named business owner who carries the commercial outcome.
- The draft, executed instrument, or vendor package where one exists, at its actual version and turn.
- Counterparty name as given, plus the brand or trading name the requester used where it differs.
- Deal value, term length, and the order form, quote, or budget line the figure came from.
- The needed-by date and the urgency basis that makes it real: quarter end, an expiring NDA, a go-live, a regulatory date, a board meeting.
- The triage rubric with its tier definitions, and the published legal service levels per tier.
- Repository or CLM search results for existing agreements with this counterparty and its affiliates.
- The approved self-serve template set and the conditions under which the business may use it without legal.

## Workflow

**Outcome.** A classified matter with type, posture, and paper settled, a risk tier scored against the named rubric with the scoring inputs shown, the review lanes this matter actually needs, a prior-agreement determination, and an intake record naming the legal owner and the committed turnaround.

**Grounding.** Classification comes from what the document does, not from what it is called and not from how the requester framed it. Posture and paper are read off the draft: whose template, whose defined terms, which side the indemnities run toward. The tier comes from the rubric the organization published, cited by name, with each scoring input attributed. Turnaround comes from the service level for that tier, never from the requester's deadline.

**Constraints.**

- Deal value alone does not set the tier. A low-value subscription that ingests customer personal data, or a free pilot that grants a perpetual license, outranks a large renewal on unchanged paper.
- The counterparty's classification of its own paper is a claim. A document sent as "our standard mutual NDA" is checked for whether it is mutual in operative effect.
- Deflection is a real outcome. Where an approved self-serve template covers the request within its stated conditions, say so, name the template and version, and record the conditions the business must meet; that is triage working, not triage refusing.
- Lane selection is a judgment about the document, not a checklist. Silence on counterparty paper selects a lane as reliably as a bad clause does: no limitation of liability selects risk allocation, no deletion obligation selects data protection.
- Privilege status is set at intake, because material collected without it cannot be retrofitted into it later.

**Parallel surface.** Items in an intake queue are independent and fan out: each request is classified, tiered, and lane-selected on its own inputs. Within one matter, the prior-agreement search, the entity name resolution, and the rubric scoring draw on separate sources and run at once. Queue ranking is the aggregate step and runs once after the fan-out returns, because ranking is a statement about the whole queue against finite legal capacity, and a request scored in isolation is always urgent.

**Acceptance bar.** The matter type, posture, and paper are each stated with the evidence that settled them. The tier names the rubric and shows its inputs. Every selected lane names what in the document selected it, and every deselected lane names why the document does not raise it. The prior-agreement check names what was searched and what it returned. The turnaround is the published service level for the tier, with the requester's date recorded separately alongside its urgency basis.

## Outputs

A complete run delivers the set:

- `contract-intake-record.md`: matter type, posture, paper, requester, business owner, legal owner, counterparty as given and as resolved, deal value with its source, needed-by date with its urgency basis, committed turnaround, privilege determination.
- `contract-triage-assessment.md`: the tier with the rubric named, each scoring input attributed to its source, the lanes selected and deselected with the reason for each, and the review depth the tier buys.
- `prior-agreement-check.md`: what was searched, which systems, under which entity names and aliases, what was found, and whether an existing instrument already covers this scope.
- `contract-intake-downstream-handoff.md`: what `counterparty-diligence-desk` and each selected lane inherit, the open questions blocking them, and the deadline arithmetic they are working against.

Depth standard: an intake record is complete when the assigned lawyer can open the matter and start reading without asking the requester anything the intake could have settled. A lane selection reads "data protection: the order form incorporates a processing annex at clause 8 and the service ingests end-customer contact records" rather than "data protection: yes". A tier reads "Tier 2 under the commercial contracting triage rubric, scored on data category and contract value" rather than a bare number.

Where an approved template covers the request, the deflection note carries the template name and version, the conditions attached, and what would pull the matter back into full review. Where the request cannot be classified from what was supplied, `contract-intake-diagnostic.md` records what was reachable, what was not, and which downstream lanes each gap leaves unselectable.

Intake is where a fact enters the packet and is never questioned again, because every later stage treats classification as settled and reads the document instead of re-deriving the matter. A business owner inferred from an email thread, a deal value read off a slide, a tier assigned without naming the rubric, or a counterparty entity taken from the brand becomes the spine that diligence, drafting, and approval routing all hang on. Each intake field carries either a source or the value `unknown` with the question that would settle it. An unknown field slows one stage; an invented one silently misroutes the entire matter.

## legal_packet fields to update

- `mode`, `matter_type`, `posture`, `paper`, `current_stage`, `completed_stages`, `next_stage`, `skipped_stages` with the reason each lane was not selected.
- `matter`: `request_id`, `requester`, `business_owner`, `legal_owner`, `needed_by`, `urgency_basis`, `deal_value` with `amount`, `currency`, `term_length`, and `basis`, `risk_tier` carrying the rubric it was scored against, `privileged`.
- `parties.counterparty.legal_name` as given, with the brand or trading name recorded separately where they differ.
- `instrument`: `title`, `version_label`, `parent_agreement`, `family` as known at intake.
- `source_facts`, `assumptions`, `open_questions`, `artifacts`, `ready_to_continue`.

## Halt conditions

- **Source conflict**: the request describes a new master agreement while the repository shows a live agreement with the same counterparty over the same scope. Two masters over one relationship makes the governing terms a dispute rather than a fact, and the second one is usually discovered by whichever party benefits from it.
- **Approval**: the request asks legal to commit a turnaround, waive a review lane, or accept a self-serve route outside the published service levels. Skipping a lane is a risk-acceptance decision with a named owner, not a scheduling adjustment.
- **Security or privacy**: the intake package contains another counterparty's confidential terms, unredacted personal data, or privileged analysis that would be circulated to the requester's distribution list.
- **Production or destructive**: intake would close, merge, or supersede an existing matter or repository record.
- **Release integrity**: the intake record would state that an existing agreement covers the requested scope without the operative text having been read, which is the answer most likely to be relied on and least likely to be checked.
- **Connector unreachable**: the repository, CLM, or the draft itself cannot be opened, so the prior-agreement check and the classification would describe a document nobody read.

A missing business owner, an unstated deal value, a needed-by date with no urgency basis, or a counterparty whose registered name is not yet resolved are soft gaps. Classify on what is present, label the assumption against the field, and record the question.

## Downstream handoffs

`counterparty-diligence-desk` inherits the counterparty as given with any alias, the posture, and the tier that sets how much diligence is proportionate. `clause-playbook-desk` inherits matter type, posture, paper, and tier, which together select the position set. Each selected review lane inherits the lane rationale and the deadline arithmetic. `nda-confidentiality-desk` inherits the prior-agreement result where an NDA already exists with this counterparty. The command desk inherits the queue ranking.

## Quality bar

Good triage is recognizable when the assigned lawyer never re-does it. The matter type survives contact with the document, the tier survives the first reading of the liability clause, and the lane set does not grow on turn two because nobody noticed the processing annex at intake. The prior-agreement check answers with an instrument and a clause rather than "nothing found in CLM", because CLM silence is a search result and not a fact about the relationship. Turnaround is stated as what the service level supports, with the requester's date visible next to it, so the gap between them becomes a decision someone makes rather than a pressure that quietly compresses the review.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
