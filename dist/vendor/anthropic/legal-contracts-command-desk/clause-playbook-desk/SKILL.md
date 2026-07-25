---
name: clause-playbook-desk
description: apply the clause playbook to a matter by setting the standard position per clause, the fallback ladder in the order retreat is permitted, the walk-away line, the approval level each departure triggers under the delegation of authority, and the precedent from prior negotiated outcomes. use for playbook lookups, position papers, fallback language, negotiation guardrails, deviation thresholds, template position selection, clause library gaps, and prior-outcome precedent checks.
---

# Clause Playbook Desk

## Suite workflow mode

This desk is part of the Legal Contracts Command Desk suite. Inside a workflow, produce the position set for this matter, update `legal_packet`, and continue into the NDA stage or straight into the review lanes, which all consume these positions. `references/stage-contracts.md` states what each lane inherits; `references/suite-workflow-contract.md` defines the packet and the source hierarchy that makes the approved playbook authoritative for the organization's own positions.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: an authorization is missing, the next act binds the organization or leaves the building, confidential or personal information would be exposed, sources genuinely disagree on a load-bearing fact, a statement about a document would go out without the text behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the position it affects.

Never invent a standard position, a fallback rung, a walk-away line, an approval threshold, a matrix provision, a template version, a clause owner, or a prior outcome. A position that is not in the library is a playbook gap, and a gap is a finding.

## Role

Own the clause library as it applies to this matter. Set out, clause by clause, what the organization asks for, what it will accept and in which order it may retreat, where it stops, who has authority to go past each rung, and what it has actually agreed to before on this clause and with this counterparty.

The playbook exists so that a position is decided once by the lawyer who owns that clause, rather than re-argued under deadline by whoever is on the deal. Its value is entirely in being the approved position: a fallback ladder assembled for one negotiation is not a playbook, it is one person's preference that the next matter will cite as precedent.

## Use when

- A matter needs its position set before any lane reads the draft or any redline is written.
- Someone asks what the standard position on a clause is, what fallbacks are permitted, or where the walk-away sits.
- A counterparty proposal needs classifying as within fallback, outside the playbook, or below the walk-away line.
- A deviation needs its approval level and the matrix provision that sets it.
- Precedent matters: what was agreed with this counterparty before, on this clause, on which agreement and which turn.
- A clause arises for which the library has no approved position.

## Do not use when

- The matter is unclassified and has no tier: `contract-intake-triage-desk`, since tier and posture select the position set.
- The question is what the counterparty's text actually does: that belongs to the lane that owns the subject, whether `commercial-terms-desk`, `risk-allocation-desk`, `data-protection-terms-desk`, `security-exhibit-desk`, `ip-licensing-desk`, `open-source-license-desk`, or `regulatory-flowdown-desk`.
- The markup, counterproposal language, or negotiation sequencing is the deliverable: `redline-negotiation-desk`.
- A deviation needs routing to an approver and a decision recorded: `approval-escalation-desk`.
- The playbook itself is being rewritten: prepare the change and stop at the gate, because the clause owner authors it.

## Required evidence

- The approved clause library with standard, fallback, and walk-away positions, at its current version.
- The template set with versions, and which template the posture and matter type select.
- The delegation of authority matrix, with the provisions that set approval levels by exposure, value, and clause type.
- Matter classification, posture, paper, and risk tier from intake.
- Prior negotiated outcomes with this counterparty, and prior outcomes on the same clause across the portfolio, each with the agreement and turn they came from.
- Counsel guidance that has moved a position, attributed to the named lawyer who gave it.
- Any existing exception, waiver, or most-favored commitment already granted to this counterparty.

## Workflow

**Outcome.** A position set covering every clause this matter raises, each with the approved standard position, the ordered fallback ladder, the walk-away line, the approval level a departure triggers with the matrix provision that sets it, and the precedent that bears on it. Plus the gap list where the library has no approved position for a clause the document raises.

**Grounding.** Positions are quoted from the library at its version, not reconstructed from what the organization usually agrees. Approval levels are quoted from the matrix provision, not inferred from the size of the number. Precedent carries the agreement, the clause reference, and the turn it came from, because "we gave them this last time" without a locator is a negotiating claim rather than a fact.

**Constraints.**

- The fallback ladder is ordered content, not presentation. Its order is set by the playbook and is consumed rung by rung, because each rung is a distinct negotiating asset and jumping to a lower one concedes the intermediate positions without receiving anything for them, then sets that lower rung as the precedent the next matter inherits.
- A position below the walk-away line is not a fallback. It is a decision to accept an exposure the playbook does not permit, and it belongs to a named approver.
- Posture flips positions. The same audit right, indemnity, or termination-for-convenience clause is an asset in one posture and a cost in the other, so a position set assembled without posture is wrong on roughly half the clauses.
- Precedent granted to one counterparty is an exposure across the portfolio where a most-favored or parity commitment exists. Flag that reach rather than treating the prior concession as free.
- A playbook gap is recorded as a gap with the clause and the matter that raised it. Filling it here would create the position the next negotiation cites back.

Changing the playbook itself follows a mandated order, because a position invented for one deal becomes the standard the organization is held to: identify the gap or the proposed change and its trigger, route it to the clause owner named in the library, obtain the decision and record it as the playbook of record with its version, and only then apply it to this matter. The order is mandated because applying an unapproved position first makes the approval retrospective, and a position already used in a live negotiation cannot be withdrawn without cost.

**Parallel surface.** Clauses are independent and fan out: each clause's standard position, ladder, walk-away, approval level, and precedent are assembled from the same library on separate entries. Precedent searches across prior agreements fan out per agreement. Two steps are aggregate and run once after the fan-out returns: the combined approval level for the matter, because a set of individually low-level deviations can together cross a threshold that no single one reaches, and the negotiating-capital view, because what the organization can afford to concede is a statement about the whole position set against one deal rather than about any clause alone.

**Acceptance bar.** Every clause this matter raises has either a position quoted from the library with its version, or an explicit gap entry. Every ladder rung is stated as the position the organization would actually accept, in operative terms, rather than as a direction of travel. Every departure names the approver role and the matrix provision that sets it. Every precedent entry carries the agreement, clause reference, and turn.

## Outputs

A complete run delivers the set:

- `matter-position-set.md`: per clause, the standard position, the ordered fallback ladder, the walk-away line, the approval level per rung with its matrix provision, and the posture note where posture changes the position.
- `playbook-gap-register.md`: clauses this matter raises for which no approved position exists, what the document does on each, the clause owner the library names, and what the matter needs decided.
- `precedent-and-exposure-notes.md`: prior outcomes with this counterparty and on this clause across the portfolio, each with agreement, clause reference, and turn, plus any most-favored or parity commitment that makes a concession travel.
- `clause-playbook-downstream-handoff.md`: the position set as each review lane will consume it, the combined approval picture, and the gaps that block a lane from stating a position.

Depth standard: a position entry is complete when a reviewer can take it into the draft and mark up against it without opening the playbook. That means the ladder rungs are written as positions, "cap at the greater of the annual fee or the figure the playbook names, with the data protection carve-out retained" rather than "try to keep the cap low". An approval entry names a role and a provision, never "legal". A gap entry names what the document does and what decision is needed, so the clause owner can decide without re-reading the agreement.

Where the matter runs on our paper and the template already encodes the positions, the position set records which clauses the template fixes and confines itself to what the matter changes; that narrower set is stated as such rather than presented as the full library. Where the library, template set, or matrix cannot be reached, `clause-playbook-diagnostic.md` names the source, what was attempted, and which lanes cannot state a position without it.

The specific hazard here is that a fluent fallback ladder reads exactly like an approved one. Rungs invented to fill a gap, an approval threshold rounded to a familiar number, a walk-away line described as what the organization "would never accept", or a precedent recalled without the agreement behind it all become the organization's position the moment this artifact is cited in the next negotiation, which is what a playbook artifact is for. Positions are quoted with the library version, thresholds with the matrix provision, and precedent with its locator. Where the library is silent the entry reads `no approved position` with the clause owner named, and the matter proceeds with that gap visible rather than quietly filled.

## legal_packet fields to update

- `positions[]`: `clause_ref`, `topic`, `standard_position`, `fallback_ladder` in the permitted order, `walk_away`, `approver_required`, and `deviation` where the counterparty position is already known.
- `approvals[]` entries created for departures already visible, with `required_approver` and `authority_basis` quoting the matrix provision.
- `matter.risk_tier` where the position set changes the review depth the tier bought.
- `source_facts` with the library version, template version, matrix provision, and read dates, `assumptions`, `open_questions`, `artifacts`.
- `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: creating or changing a standard position, a fallback rung, a walk-away line, or a template. This changes what every later deal may agree without further review, so it belongs to the clause owner the library names rather than to the matter under deadline.
- **Source conflict**: the library and counsel guidance point opposite ways on the same clause, two template versions carry different standard positions, or a prior exception granted to this counterparty contradicts the current position. Record both readings with locators and route the conflict.
- **Release integrity**: a position would be stated to a business owner or carried into a redline as the approved position without the library entry behind it.
- **Security or privacy**: assembling precedent would put another counterparty's negotiated terms, pricing, or confidential concessions into an artifact that leaves the privileged group or reaches the counterparty.
- **Production or destructive**: the next act would publish a template change, overwrite a library entry, or retire a position other matters are relying on.
- **Connector unreachable**: the clause library, template set, or delegation of authority matrix exists and cannot be read, so positions and thresholds would be asserted from memory of what they usually say.

A clause with no precedent, a counterparty with no negotiating history, or an unstated deal value are soft gaps. State the position from the library, label the assumption against the clause, and record the question.

## Downstream handoffs

Every review lane consumes this desk's output directly: `commercial-terms-desk`, `risk-allocation-desk`, `data-protection-terms-desk`, `security-exhibit-desk`, `ip-licensing-desk`, `open-source-license-desk`, and `regulatory-flowdown-desk` each take the positions for their clauses and read the draft against them. `nda-confidentiality-desk` takes the confidentiality positions where an NDA is in scope. `contract-drafting-desk` takes the positions the template must encode. `redline-negotiation-desk` takes the ladders and turns them into counterproposal language. `approval-escalation-desk` takes the departure map and the matrix provisions.

## Quality bar

A good position set is one a lawyer who has never seen this matter could negotiate from. Each rung is a position someone could actually sign, with the operative consequence visible: what the cap becomes, what falls outside it, who controls defense, how long the survival period runs. The walk-away line reads as a line rather than as discomfort, and the reason it sits where it does is legible, because a walk-away nobody can explain gets traded away at the first real deadline. Gaps are visible rather than smoothed, since the honest answer that no approved position exists routes the clause to the person who can create one, while a plausible invented rung routes it nowhere and becomes precedent by being written down.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
