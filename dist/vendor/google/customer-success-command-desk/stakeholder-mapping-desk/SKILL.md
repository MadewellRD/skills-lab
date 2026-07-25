---
name: stakeholder-mapping-desk
description: map the buying and using centers on an account with economic buyer champion executive sponsor administrator power users detractors procurement and security reviewers each identified or named unidentified, with influence on the renewal decision, disposition and its evidence, last interaction recency, coverage state across engaged dormant departed and unknown, multi-threading counts, single-threaded exposure, and succession gaps. use for relationship mapping, sponsor change and champion departure, coverage checks before a renewal or qbr, and multi-threading plans.
---

# Stakeholder Mapping Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the stakeholder artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the person or role it affects, and record it in `open_questions`. Never invent a stakeholder name, a title, a reporting line, a disposition, a departure, or an interaction that did not occur.

## Role

This desk owns the answer to the only question every later stage resolves onto: which named person decides, and are they still there. It maps the buying center, meaning the people who will decide whether to renew, expand, or leave, and the using center, meaning the people whose behavior produces the usage the decision will be justified with. Both are mapped, because they are frequently disjoint and the account where the users love the product and the buyer has never seen it is the standard shape of a surprise churn.

For each person it owns role type across economic buyer, champion, executive sponsor, administrator, power user, end user, detractor, procurement, security reviewer, finance, and partner; influence on the renewal decision with what establishes it rather than with an assigned number; disposition with the evidence and the date behind it; last interaction with the date and the surface; and coverage state, which distinguishes engaged from dormant from unreachable from departed from unknown, because those are five different situations and collapsing them into covered is how an account arrives at its renewal with nobody on the other side.

Above the individuals it owns the account-level facts: multi-threading stated as a count with the window it was measured over, buying-center coverage naming which decision roles are covered and which are not, single-threaded exposure stated as the specific person the renewal depends on rather than as a flag, and succession gaps where a role has no second contact.

## Use when

- A renewal, save, expansion, advocacy request, or business review is being prepared and it has to resolve onto named people.
- A champion, sponsor, or administrator has left, changed role, or gone quiet, and the coverage consequence needs establishing.
- The account is being handed to a new owner and the relationship inventory is what transfers.
- Health is green and nobody internally can name who would sign the renewal.
- The customer has reorganized, been acquired, or consolidated a function the product sits inside.
- Engagement is concentrated in one person and a multi-threading plan is needed before the renewal window.

## Do not use when

- The buying group at signature is the subject rather than the current map. That is `post-sale-handoff-desk`, whose signature-time group seeds this one.
- The subject is which accounts sit in which segment and who owns them internally. That is `segmentation-coverage-desk`.
- The work is what these people want the product to achieve, with metrics and baselines. That is `success-planning-desk`.
- The subject is whether a named person will act as a reference and what approvals that needs. That is `advocacy-reference-desk`.
- The relationship risk is being sized in ARR terms with a mitigation owner. That is `churn-risk-desk`, which consumes coverage state from here.

## Required evidence

- Contact records with role, title, and last interaction date, plus the record's own last-updated date, since a contact record and the person it describes drift apart quietly.
- Meeting and email history with attendance rather than invitation, because an invitee list is not a relationship.
- Product administrator and permission records, and authentication activity for named administrators and power users, which is frequently the only evidence that survives a title change.
- The buying group as it stood at signature, carried from handoff.
- Support and escalation contacts, including whoever actually files the tickets.
- Organizational announcements, departure signals, out-of-office and bounce evidence, and public role changes.
- The customer's own reporting structure where they have stated it, and their statements about who decides.
- Prior relationship history, including anyone previously covered by a former owner and anyone who was a detractor in an earlier cycle.

## Workflow

**Outcome.** A map of the buying and using centers with every decision role either named or explicitly recorded as unidentified; influence, disposition, last interaction, and coverage state per person, each with what establishes it; multi-threading with its count and window; buying-center coverage stating which roles are uncovered; single-threaded exposure named as a person; and succession gaps with the roles that have no second contact.

**Grounding.** A role is established by evidence of the person acting in it: the person who signed, the person who approves the invoice, the person whose approval unblocked the security review, the person who administers the tenant. A title is a weak signal and is labeled as inference where it is all there is. Disposition comes from something the person said or did, quoted and dated, rather than from the account team's impression of the relationship; where only an impression exists, it is recorded as internal narrative with the person who holds it. Departure is established by evidence, and an absence of evidence produces `unknown` rather than `engaged`. Where the CRM records a relationship the interaction history does not support, both readings are preserved against the contact.

**Constraints.** Every entry carries a last-interaction date or `never`, because recency is the field that turns a map into a coverage judgment and its absence is the defect this desk exists to remove. A contact nobody has spoken with inside the period the coverage motion promises is unverified coverage rather than coverage, and is written that way. Unidentified roles are named as unidentified, since a missing economic buyer is a finding and an empty row is not. Influence is stated with what establishes it rather than as a score, so that a later reader can disagree with the basis. Multi-threading is a count of people with a real interaction inside a stated window, not a count of contacts in the CRM. Single-threaded exposure is written as the person's name and the specific decisions that route through them. Personal information stays limited to what the coverage judgment needs; personal circumstances, health, performance, and internal political detail about the customer's employees do not belong in an artifact that will travel.

**Parallel surface.** Independent items fan out safely: individual stakeholders being researched and dated, individual role confirmations, individual administrator and permission checks, and accounts in a book being mapped at once. The aggregate runs once after the fan-out returns, because buying-center coverage, the multi-threading count, single-threaded exposure, and the succession judgment are statements about the whole map and change meaning as each person's coverage state resolves. The multi-threading plan is also a single pass, since it allocates a fixed amount of relationship capacity across the gaps.

**Acceptance bar.** Every decision role is filled with a named person or explicitly recorded as unidentified. Every person carries a last-interaction date or `never`, a coverage state, and the evidence behind their disposition. Multi-threading states its window. Single-threaded exposure names the person and the decisions that depend on them. Every succession gap names the role and what is missing. No coverage state is `engaged` on the strength of a CRM field alone.

## Outputs

A complete run delivers this set:

- `stakeholder-map.md`: buying center and using center, each person with role type, what establishes the role, influence with its basis, disposition with quoted and dated evidence, last interaction with its surface, coverage state, and succession.
- `coverage-assessment.md`: which decision roles are covered, which are uncovered, which are covered only by an unverified contact, and the multi-threading count with the window it was measured over.
- `single-threaded-exposure.md`: the specific person the renewal depends on, the decisions and information that route through them, what happens on the day they leave, and the ARR that sits behind that dependency.
- `relationship-change-log.md`: departures, role changes, new arrivals, and dormancy since the last map, each with the evidence and the date it became known, plus what each change removed from the coverage position.
- `multi-threading-plan.md`: the roles to reach, the route to each including who can introduce them, the reason the customer would take the meeting, and the owner and date on each, sequenced so the highest exposure is closed first.
- `stakeholder-mapping-downstream-handoff.md`: what `success-planning-desk`, `renewal-preparation-desk`, and `save-play-desk` inherit, including who can agree a plan and who can sign.

Depth standard: an artifact is complete when a new owner could take over the relationship from it and know who to call first, who has not been spoken with, and who is missing entirely. A contact entry without a date, or a role marked covered without evidence of the person acting in it, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when contact records, interaction history, or administrator records cannot be reached, the run delivers `stakeholder-connector-diagnostic.md` naming each unreachable source and stating which roles, recency judgments, and coverage states remain unestablished. Coverage is not asserted from an account's size or industry.

Anti-fabrication guard: the specific danger at this desk is org-chart plausibility. Every enterprise account has an economic buyer, a champion, and an administrator somewhere, so writing those three rows produces a map that looks correct and is entirely unverified. A named person is only written where a source names them, and a role is only assigned where evidence shows that person acting in it; a title that merely sounds like the role, a name appearing on a distribution list, and an attendee who was invited but did not attend are each labeled as inference or left as unidentified. A last-interaction date comes from a real interaction record and is never rounded forward or inherited from an adjacent meeting on the same account. Disposition is quoted from what the person said, with the date, because "supportive" written from the account team's impression is how a detractor stays invisible until they run the evaluation. A departure is recorded only on evidence, and a person nobody can reach becomes `unreachable` or `unknown` rather than either departed or engaged. An unidentified economic buyer is the single most valuable line this desk can produce, and filling that row to make the map look complete removes the only warning the account gets before the renewal arrives with nobody on the other side.

## success_packet fields to update

- `stakeholders[]` with `name_or_role`, `role_type`, `influence` with what establishes it, `disposition` with its evidence and date, `last_interaction`, `coverage_state`, and `succession`
- `stakeholders.multi_threading` with `engaged_contacts` including the window it was measured over, `single_threaded`, and `buying_center_coverage` naming the uncovered roles
- `risks[]` for single-threaded exposure, a departed or dormant sponsor, and any uncovered decision role, each with `arr_exposed`, `first_detected`, and an owner
- `account.account_team` where the internal side of the relationship has changed
- `source_facts` with collection dates and the record each reading came from, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: a renewal, save, expansion, or advocacy position would be built on a sponsor map that no interaction in the current period supports. Every downstream decision in this suite resolves onto who will decide, and a champion who left two quarters ago is not a champion; carrying them as one is the most common way an account reaches its renewal with nobody on the other side.
- **Security or privacy**: the map would carry personal data beyond what the coverage judgment needs, record a customer employee's personal circumstances or internal standing, or move one customer's org detail into another account's artifact.
- **Source conflict**: the CRM, the interaction history, the administrator records, and the customer's own statement genuinely disagree about who holds a role or whether a person is still there, and resolving it silently would point the renewal at the wrong person.
- **Missing approval**: reaching a new executive, escalating above a current contact, or approaching a stakeholder the champion has asked to be routed through is a relationship act with consequences, and it belongs to the account owner rather than to the analysis.
- **Production or destructive**: the next action would write contact changes, mark a contact inactive, or trigger outreach from the CRM or engagement platform.
- **Connector unreachable**: contact records, interaction history, or administrator records exist and cannot be read, so recency and coverage state would be asserted about people nobody looked up.

An unknown reporting line, an unconfirmed succession candidate, an untested disposition, and a partner contact whose role is unclear are soft gaps. Record the gap, label the assumption against the person it concerns, and continue.

## Downstream handoffs

`success-planning-desk` is next and needs the named customer stakeholder who can agree a plan and the outcome owners on the customer side, because a plan agreed with nobody is an internal document. `renewal-preparation-desk` needs who signs, who influences, and the procurement contact, plus the single-threaded exposure. `save-play-desk` needs who can still be reached, who decides, and which relationships survive the current dissatisfaction. `escalation-management-desk` needs the executive relationship on both sides and the person who raised the issue. `advocacy-reference-desk` needs candidate disposition with quoted willingness evidence and the customer-side approver. `expansion-whitespace-desk` needs the map extended into business units nobody has met. `churn-risk-desk` consumes coverage state directly, since sponsor loss is a risk category rather than a relationship inconvenience.

## Quality bar

Good stakeholder work is dated. Every row carries when, and the map reads as a set of relationships with an age rather than a list of names with titles. It is willing to be short: four verified people and three roles marked unidentified is a better artifact than eleven rows assembled from an org chart, because the three unidentified roles are the work. It distinguishes the using center from the buying center and says out loud when the two do not overlap, which is the shape that produces a renewal decision made by someone who has never seen the product. It names the person the account depends on, in a sentence, with the decisions that route through them, so a leader reading one line knows the exposure. And it treats the customer's people with the discretion the relationship requires, carrying what the coverage judgment needs and leaving out what belongs to them.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
