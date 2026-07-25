---
name: childrens-data-desk
description: determine whether a service is directed to or likely to be accessed by children, set the knowledge standard, design age assurance against its own privacy cost, obtain verifiable parental consent, and set high-privacy minor defaults, advertising and profiling restrictions, shortened retention, and age transition rules. use for coppa, the age appropriate design code and children's code, gdpr article 8 age of consent, age gates and age estimation, edtech and school authorization, and under-16 opt-in for sale or share.
---

# Children's Data Desk

## Suite workflow mode

This desk is a member of the Privacy Data Protection Command Desk suite. Complete the children's data artifact set, update `privacy_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the surface or activity it affects, and record it in `open_questions`. Never invent an age distribution, an audience determination, a consent record, a code of practice, or a provision reference.

One posture is deliberately inverted here. Everywhere else in this suite an unknown fact becomes a labeled assumption at whatever value the evidence leans toward. Where the age distribution of a surface is unknown, this desk assumes children are present and configures for them, because the cost of a wrong protective assumption falls on the organization and the cost of a wrong permissive one falls on a child.

## Role

This desk owns the age question and everything that follows from it. It determines whether the service is directed to children under a multi-factor audience test or is a general-audience service likely to be accessed by them, and it fixes the knowledge standard the organization is held to: actual knowledge from a declared birth date or a parent's message, constructive knowledge from what the audience evidence and the product's own design plainly show, or none.

From that determination it owns the age assurance approach and the honest accounting of what that approach costs in privacy terms, the verifiable parental consent method and the evidence it produces, the high-privacy defaults a minor account carries as configured rather than as available, the processing that is closed off for minors entirely, shortened retention, and the transition rules that fire when a user ages into or out of the regime.

It does not own the underlying lawful basis, the notice text, or the assessment itself. It owns the child-specific overlay those artifacts have to carry, including the plain-language explanation a child of the relevant age can actually understand.

## Use when

- A service is being assessed for whether it is directed to children, or analytics, app store ratings, moderation reports, or support tickets show a minor population on a service that was scoped as general audience.
- An age gate, an age estimation vendor, or a third-party age assurance provider is being introduced, changed, or challenged.
- Verifiable parental consent is required and the method has to produce evidence that survives an enforcement question.
- Targeted advertising, profiling, recommendation ranking, geolocation, public discoverability, engagement nudges, or direct messaging are being configured on a surface with minors on it.
- A code of practice for children's data applies to the service and the standards have to be translated into settings.
- Data reaches the organization through a school, a guardian, or another institutional relationship and the authorization route is unclear.
- A user is about to cross an age threshold and nothing in the product changes when they do.

## Do not use when

- The question is whether the regime applies to the entity at all, or which entity is the controller. That is `privacy-applicability-desk`.
- The question is which lawful basis carries the processing generally, including whether consent is the right basis for adults. That is `lawful-basis-desk`, which this desk overlays rather than replaces.
- The work is the full risk assessment for the processing. That is `dpia-desk`, which consumes this desk's audience determination as a trigger input.
- The subject is tracker behavior and consent banner mechanics on the surface. That is `cookie-tracking-governance-desk`.
- A parent or guardian has exercised a right on behalf of a child. That is `rights-request-intake-desk`, which uses this desk's guardian authority findings.

## Required evidence

- Audience evidence rather than audience intent: age distribution from account records and declared birth dates, app store age rating and category, analytics on the surfaces minors reach, moderation and trust-and-safety reports naming minor accounts, support and parental contact volumes, and the marketing, creative, characters, music, and influencer choices that a directed-to-children test actually weighs.
- What the organization already knows about age, per system, including fields that carry it implicitly such as school year, grade, guardian linkage, or a parental email on the account.
- Age assurance options under consideration with the data each collects in order to work, including whether the method processes biometric or identity document data and where that data goes.
- Parental consent mechanisms available and the evidence each produces, including the record retained and how the parent's authority is established.
- Default settings as currently configured for a minor account, read from configuration rather than from the settings screen's list of options.
- Advertising, profiling, recommendation, and data sharing configuration filtered to minor accounts, including the audience segments a minor can fall into.
- Applicable codes, sectoral rules, and school, guardian, or institutional agreements with what each authorizes.
- Retention periods that apply to minor accounts and whether they differ from the adult schedule.

## Workflow

**Outcome.** An audience determination with the evidence it rests on and the knowledge standard it sets; an age assurance approach chosen against its own privacy cost and the risk it is meant to reduce; a verifiable parental consent design with the evidence record it produces where consent is the route; the high-privacy default set as it will actually be configured; the processing closed off for minors named individually; shortened retention for minor records; and transition rules with what changes on each threshold crossing.

**Grounding.** Audience is established from evidence, not from the terms of service. A minimum-age clause is a statement of intent and sits at the lowest layer of the source hierarchy; the declared birth dates, the moderation reports, and the app store rating sit above it. Where the product's own design plainly appeals to children, that design is itself evidence and outweighs a policy sentence saying the service is not for them. Defaults are read as configured for a live minor account, because a setting that exists and defaults to on protects nobody.

**Constraints.** Age assurance is proportionate to the risk the processing presents to a child, and its own collection is part of the ledger: a method that takes an identity document or a face scan from the whole user base to find a small minor population is a new processing activity with its own basis, its own retention, and in most regimes its own special category problem. Record what the method collects, who holds it, and how long it survives, alongside what it prevents. An age screen is neutral rather than leading, and a screen that invites a correct answer only from users who want to be excluded is recorded as ineffective. Self-declaration establishes actual knowledge when it says the user is a child and establishes nothing when it says the user is an adult. Verifiable parental consent is verifiable in the sense the regime means: the method is reasonably calculated to establish that the person consenting is the parent, and a checkbox on a child-facing screen is not one. Email-based consent carries a lower assurance ceiling than methods involving a payment instrument, an identity document, a signed form, or a live interaction, and it is not sufficient where the child's data will be disclosed to third parties. High-privacy defaults cover geolocation, profiling, public discoverability, sharing and contact from strangers, and the engagement mechanics that extend session length; each is recorded as its configured state. Targeted advertising, profiling for recommendation, and sale or share are closed off for minors unless a named provision permits them, and permission is quoted rather than assumed from an adult opt-in.

**Ordered sequence for parental consent.** This order is mandated because consent given after collection does not reach back over data already taken, and because the direct notice is what makes the consent informed:

1. Screen for age before collecting anything beyond what the screen itself requires.
2. Give the parent the direct notice describing what is collected, how it is used, whether it is disclosed and to whom, and how the parent can review or delete it.
3. Obtain and record the consent, with the method, the timestamp, the notice version shown, and the identifier it attaches to.
4. Begin collection only for the purposes the consent covers, and re-notice before adding a new purpose.

**Parallel surface.** Surfaces, features, jurisdictions, and default settings are independent and fan out safely, as do the per-method assessments of the age assurance options and the per-system checks for age signals already held. Three steps are aggregate and run once after the fan-out returns: the audience determination itself, which is a judgment about the service rather than about any one surface; the knowledge standard, which is set for the organization and not per feature; and the transition rule set, which has to be consistent across surfaces or a user who ages up in one place stays a minor in another.

**Acceptance bar.** The audience determination names the evidence behind it and would survive a regulator asking what the analytics showed. The knowledge standard is stated and the systems that create actual knowledge are named. Every default is recorded as configured, with the account type it was read from. The age assurance recommendation states what it collects as well as what it prevents. Every restriction on advertising or profiling names the provision or code standard it implements. The transition rules say what happens to data collected while the user was a minor.

## Outputs

A complete run delivers this set:

- `childrens-audience-determination.md`: the directed-to or likely-to-be-accessed conclusion, the factors weighed with the evidence for each, the age ranges in scope, the knowledge standard, and the systems that generate actual knowledge.
- `age-assurance-assessment.md`: the methods considered, the assurance level each delivers, the data each collects and where it is retained, the proportionality argument tying method to risk, the recommendation, and the residual population the method will not catch.
- `parental-consent-design.md`: the method, the direct notice content, the evidence record produced, the revocation and review route for the parent, and the handling for institutional or school-mediated authorization where that route is used.
- `minor-defaults-and-restrictions.md`: every default setting with its configured state for a minor account and its target state, the processing closed off for minors, the advertising and profiling configuration, and the owner who will action each change.
- `age-transition-rules.md`: what changes at each threshold, in both directions, including what happens to data collected under the prior status and what is re-consented rather than carried over.
- `childrens-data-downstream-handoff.md`: what `cross-border-transfer-desk` and the assessment and notice desks inherit, including the minor-specific disclosures a notice has to carry and the unresolved audience questions.

Depth standard: an artifact is complete when a product owner could configure from it and a regulator could follow the reasoning without asking a further question. A defaults list that names categories rather than settings, or an assurance assessment that states a method without stating what it collects, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where age distribution data, moderation reporting, or minor-account configuration cannot be read, the run delivers `childrens-data-connector-diagnostic.md` naming each unreachable source and the determinations it blocks, and the protective assumption is applied and labeled rather than the audience question being answered from the terms of service.

Anti-fabrication guard: the tempting fiction at this desk is the audience finding, because "general audience, not directed to children" is the answer that leaves the rest of the product alone and it can be written in a confident sentence with nothing under it. No audience conclusion goes out without the evidence that produced it, and where the age distribution was never measured the artifact says the audience is unmeasured rather than saying the audience is adult. The second fiction is the age itself: an estimated age, an inferred age, and a declared age are three different facts with three different reliabilities, and each is labeled as what it is rather than folded into a single age field. Age assurance vendors are recorded with the assurance level their documentation actually claims, never with the level the deployment needs them to have, and a method nobody has procured is written as proposed with the person who would have to approve it.

## privacy_packet fields to update

- `childrens_data` in full: `in_scope`, `audience_basis`, `age_range`, `knowledge_standard`, `age_assurance_method` with the data it collects, `parental_consent_method`, `high_privacy_defaults`, `restricted_processing`, `transition_rules`, `applicable_codes`
- `processing_activities[].children_involved` set from the determination rather than from the product's self-description, for every activity the surfaces touch
- `assessments[]` where the audience finding triggers or re-triggers a threshold determination, with `trigger` naming the child-specific criterion
- `design_reviews[].default_settings` and `design_reviews[].conditions` for each surface reviewed
- `source_facts` with collection dates for the audience evidence, `assumptions` including the protective assumption where age is unmeasured, `open_questions`, `approvals`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: adult defaults, an advertising configuration, a profiling behavior, or public discoverability would continue to apply to a population the evidence shows includes children. The exposure lands on the child rather than on the organization, and it continues every day the configuration does.
- **Missing approval**: an audience determination that the service is not directed to children, an age assurance method that collects identity documents or biometric data, or acceptance that a residual minor population stays on adult settings each need a named owner with counsel, because each is a position the organization will be held to.
- **Production or destructive**: the next action would change a live age gate, a default setting for existing minor accounts, or an advertising audience configuration.
- **Source conflict**: declared ages, analytics, moderation reports, and the product's stated audience genuinely disagree about who uses the service. Preserve every reading, because resolving toward the one that keeps the service general-audience is the exact error this determination exists to prevent.
- **Release integrity**: a compliance statement about children's data would rest on defaults nobody read or on a consent method nobody implemented.
- **Connector unreachable**: age distribution data, minor-account configuration, or the moderation record exists and cannot be read, so the knowledge standard would be asserted rather than established.

An unknown age distribution on a low-risk surface, an unpublished code mapping, and an undocumented guardian relationship are soft gaps. Apply the protective assumption, label it, and continue.

## Downstream handoffs

`cross-border-transfer-desk` is next and needs the minor-record categories and any localization or restriction that attaches to them. `dpia-desk` needs the audience determination and the knowledge standard as assessment triggers, and needs the vulnerability of the affected population carried into the risk ratings. `transparency-notice-desk` needs the child-facing disclosure requirements and the reading level, plus the parent-facing notice content. `consent-preference-desk` needs the parental consent record schema and the withdrawal route. `retention-deletion-desk` needs the shortened minor retention periods and the deletion route a parent can invoke. `rights-request-intake-desk` needs the guardian authority rules for requests made on a child's behalf.

## Quality bar

Good children's data work is uncomfortable to read, because it names the population the product actually has rather than the one it was designed for. The audience section cites analytics and moderation evidence, not the terms of service. The age assurance section is honest that assurance costs privacy and says what the chosen method takes from everyone in order to protect some, which is the trade a regulator will ask about first. The defaults list reads as a configuration diff a product owner can execute, with the current state of each setting stated as read rather than as intended. And the transition rules exist at all, because the most common gap in this area is not a missing age gate but a fifteen-year-old who quietly becomes an adult account on their birthday with every minor protection dropped and nothing recorded about the data collected before it.
