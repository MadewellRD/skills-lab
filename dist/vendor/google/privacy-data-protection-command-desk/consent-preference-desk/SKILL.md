---
name: consent-preference-desk
description: design consent per purpose with real granularity, apply the freely given specific informed and unambiguous test to the wording a person actually saw, define the consent record schema and the withdrawal path, handle universal opt-out and preference signals at the layer where behaviour changes, and identify the invalid-consent population with the defect named per record. use for consent banner and preference centre design, marketing permission audits, double opt-in and re-consent programmes, global privacy control handling, opt-out of sale or share, and consent validity disputes.
---

# Consent Preference Desk

## Suite workflow mode

This desk is a stage of the Privacy Data Protection Command Desk suite. Complete the consent design, the validity assessment, the record schema, and the invalid-consent population, update `privacy_packet`, and continue into the next stage when the facts to run it are present. A run that ends by proposing a consent review has renamed the request. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required authorization is missing, the next action is irreversible or reaches production, continuing would expose personal data, sources genuinely disagree on a load-bearing fact, a lawfulness claim would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the consent surface or population it affects.

Never invent consent wording, a capture timestamp, a notice version, a granularity setting, a withdrawal route, an opt-in rate, or the size of a valid or invalid population. Consent is the one basis whose entire weight rests on a record, so a reconstructed record is a fabricated legal position rather than a documentation improvement.

## Role

Own consent as a mechanism rather than as a checkbox: what a person was asked, how they answered, what the answer was attached to, what proves it, and how they take it back.

Consent has to be freely given, specific, informed, and unambiguous, and each limb fails in a characteristic way. Freely given fails where the choice is bundled into a term of service, where declining costs the individual the service or a materially worse version of it with no equivalent alternative, or where the parties are unequal enough that refusal is not realistic, which is why consent is usually the wrong basis for employment processing. Specific fails where one control covers analytics, advertising, and partner sharing at once, since a single answer cannot mean three things. Informed fails where the identity of the recipients, the purposes, and the right to withdraw were not in front of the person, and it fails retrospectively when the text they saw was overwritten and never archived. Unambiguous fails on pre-ticked boxes, on continued browsing treated as agreement, on scrolling, and on silence.

Own the record schema, which is where most programmes are quietly broken. A consent record is the timestamp, the notice or wording version, the exact text shown, the granularity, the capture surface, and the identifier the consent attaches to. A boolean column proves that a flag is set at some point by something.

Own withdrawal, which must be as easy as giving was: a one-click grant answered by an email to a support address is a defect, not a workflow. Own preference signals, including universal opt-out signals and opt-out of sale or share, recorded at the layer where the signal actually changes behaviour rather than at the layer that receives it. Own the invalid-consent population with the defect named per record, and the disposition for processing already carried out under it.

## Use when

- Consent is the claimed basis anywhere and its validity has not been tested against the wording that was actually shown.
- A consent banner, preference centre, marketing permission flow, or double opt-in journey is being designed, rebuilt, or challenged.
- Withdrawal is suspected of being harder than the original grant, or a withdrawal does not propagate to every system and vendor holding the permission.
- Universal opt-out signals, opt-out of sale or share, or limits on sensitive data use need handling, or their current handling needs testing at the enforcement layer.
- A notice version or a purpose has changed and the question is which existing consents survive it.
- A marketing list, an acquired database, or an inherited audience needs a validity assessment before it is used.
- A complaint, an inquiry, or an internal audit asks the organization to produce what a named individual agreed to and when.

## Do not use when

- Consent is not actually the right basis for the activity: `lawful-basis-desk`, which decides whether consent is available before this desk designs it.
- The question is the notice text surrounding the request rather than the request itself: `transparency-notice-desk`.
- The question is which trackers fire, in what order, and whether they precede the answer: `cookie-tracking-governance-desk`, which measures the surface this desk designs.
- The individual is a child and the question is verifiable parental consent or an age assurance method: `childrens-data-desk`.
- Someone has asked to withdraw, opt out, or be deleted as an exercised right with a deadline: `rights-request-intake-desk`.
- Explicit consent is being relied on as a transfer derogation: `cross-border-transfer-desk`.

## Required evidence

- The activities relying on consent, with the purposes stated at the granularity the individual is being asked about.
- Every capture surface with the wording as currently shown: banner, form, checkout, in-app prompt, preference centre, paper form, and call script, captured as text rather than described.
- The consent record schema and a sample of what it actually stores, including whether the wording and the notice version travel with the record.
- The withdrawal path per purpose as implemented, plus what happens downstream when it is used: suppression, propagation to vendors, and the lag before it takes effect.
- Notice versions with effective dates, so a capture timestamp can be resolved to the text that was in force.
- Marketing and communication channel configuration, list membership and its provenance, and any imported or acquired audience with its source.
- Universal opt-out and preference signal handling: what receives the signal, what stores it, and the layer at which behaviour changes.
- Consent management or preference platform configuration, plus its export of consent states with the fields it retains.

## Workflow

**Outcome.** A consent design per purpose with its granularity, a validity assessment applying each limb of the test to the wording actually shown, a record schema that can reproduce what a person saw, a withdrawal path as easy as the grant with its propagation mapped, preference and universal signal handling recorded at the enforcement layer, the invalid-consent population with the defect named per record, and a disposition for processing already carried out under invalid consent.

**Grounding.** The captured wording and the consent records are authoritative for what a person was asked and how they answered, bounded by what the record retains. The live surface is authoritative for what is shown now, and the archived notice version is authoritative for what was shown then; where the wording was never archived, the informed limb is unprovable rather than presumed satisfied. Platform configuration is authoritative for intent and the observed behaviour of the surface is authoritative for what happened, so a preference centre that lists a purpose is evidence of a control existing, not of the control working. Downstream system state is authoritative for whether a withdrawal reached anything, because a suppression flag set in one platform while a vendor keeps mailing is a withdrawal in one system only.

**Constraints.** Test the limbs against the text a person saw rather than against the policy that describes the intent, since a compliant policy sitting behind a bundled toggle is a compliant policy and an invalid consent. Set granularity from the purposes rather than from the vendor categories, because a category-shaped control lets one answer cover purposes an individual would separate. Reject symmetry is part of the design: an accept control and a decline control that differ in prominence, in the number of steps, or in wording pressure make the choice less than free, and confirmshaming counts. Withdrawal is designed with the same number of steps as the grant and with its propagation named system by system, including the vendors that hold their own copy of the permission. Record the enforcement layer for every preference signal, because a signal received at the edge and never applied at the profile store is an unhonoured signal that reports as honoured. Where a purpose or the wording changes materially, the existing consents are assessed rather than assumed to carry over, and re-consent is scoped as a population with a route. Personal data stays out of the artifact: the invalid population is described by count, surface, capture window, and defect, referenced by identifier class rather than by identifier.

**Parallel surface.** Capture surfaces, purposes, and consent populations are independent units and fan out: each surface has its wording captured and each limb applied, each purpose has its granularity and withdrawal path assessed, each channel's propagation is traced, and each population segment is tested against the notice version in force when it was captured. The aggregate passes run once after the fan-out returns, because each is a statement about the whole set: sizing the invalid population across surfaces and windows, deduplicating an individual whose consent state differs between platforms, computing valid and withdrawn rates against the population they were measured over, resolving a preference signal that conflicts with an explicit in-product choice, and assembling the re-consent plan with its sequence and its suppression list.

**Acceptance bar.** Every consent purpose has a granularity, a capture surface, and the wording that was shown attached to it. Every record in the schema can answer what a person was shown, when, under which notice version, and what identifier it attaches to, or the schema is recorded as unable to. Every withdrawal path is stated with its step count against the grant and its propagation per system and vendor. Every preference signal names the layer where behaviour changes. Every consent state is `valid`, `stale`, `invalid`, `withdrawn`, or `never_captured`, and `invalid` carries the specific defect rather than a general concern. Processing carried out under invalid consent has a disposition rather than a note.

## Outputs

A complete run delivers this artifact set:

- **Consent design specification**: per purpose, the granularity, the surface, the proposed wording, the default state, the reject path with its symmetry, and the interaction with any other basis relied on for the same activity.
- **Validity assessment**: per surface and per population, each limb applied to the wording actually shown, with the failing limb named and quoted rather than summarized.
- **Consent record schema**: the fields required to reproduce a grant, the fields the current schema stores, the difference between them, and what that difference makes unprovable.
- **Withdrawal and propagation map**: the route per purpose, its step count against the grant, every system and vendor the withdrawal must reach, the confirmation each returns, and the lag before it takes effect.
- **Preference and universal signal handling**: per signal, where it is received, where it is stored, the layer where behaviour changes, and the surfaces where it is currently not applied.
- **Invalid-consent population**: segmented by surface, capture window, and defect, with counts and the basis for each count, and the derived data produced from the affected processing.
- **Remediation and re-consent plan**: what stops now, what is suppressed, what is re-consented, in what order, over which channel, and what happens to individuals who do not respond.
- **Source facts and assumptions record**: every wording capture, configuration read, and record export with its collection date, and every assumption with the surface or population it affects.

Depth standard per artifact: an assessment is complete when the accountable owner can act on it without a further round of investigation. "Consent may not be valid for the newsletter list" is a concern. A complete finding names the surface, quotes the text shown, states which limb fails and why, gives the capture window and the record count with what produced the count, says which processing that population feeds, and states whether the failure is curable by re-consent or requires the processing to stop.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where consent records, archived wording, or platform exports cannot be reached, deliver the design and the schema assessment and state which populations cannot have their validity determined at all, since undetermined validity is never reported as valid. In `resume` mode, re-capture the live wording and re-read the notice version, because a banner rebuilt between readings changes what every subsequent record means and can invalidate an assessment that was accurate when it was written.

Watch for the reconstructed grant, which is this desk's own way of inventing evidence: describing what a person "would have seen" from the banner that is live today, when the text they actually saw was replaced and never archived. It is tempting because the current wording is available, plausible, and probably similar, and it is exactly the claim a complainant can disprove with a single screenshot. So wording enters an artifact only as a capture with a date, a consent state is `invalid` where the record cannot reproduce the grant rather than being rated on how likely the grant was, an imported or acquired list with no provenance is `never_captured` rather than inherited, and a population whose notice version cannot be resolved is reported as unprovable with its size. Consent is the only basis that lives entirely inside its own record, so an optimistic consent state does not merely overstate compliance; it removes the organization's ability to discover that a whole population needs re-consenting until someone external asks first.

## privacy_packet fields to update

- `consent[]`: per consent purpose, `purpose`, `surface`, `granularity`, `capture_record` describing what the schema actually retains, `withdrawal_path`, `state`, `invalid_reason` where applicable, and `refresh_due`.
- `preference_signals{}`: `global_privacy_control`, `opt_out_of_sale_or_share`, `sensitive_data_limitation`, and `enforced_at` naming the layer where behaviour changes rather than where the signal arrives.
- `lawful_bases[]`: updated where a validity finding removes consent as an available basis for an activity, which sends that activity back to `lawful-basis-desk` rather than to a different consent design.
- `processing_activities[]`: flagged where processing has been running under invalid consent, with the period and the systems.
- `approvals[]`: suppression, re-consent campaigns, and any change to a live banner or preference centre, each with the accountable owner and the authority level.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Release integrity**: a lawfulness claim would rest on consent records that cannot reproduce what the person was shown when they agreed. This is the defining halt of this desk. That claim travels into the register, into the notice, and eventually into a regulator response, and once the original wording is unrecoverable the only remedy is re-consent across the whole population.
- **Approval**: changing a live banner or preference centre, launching a re-consent campaign, suppressing a population, or accepting continued processing while consent is remediated are decisions with a named owner and a stated authority level.
- **Production or destructive**: the next action would write consent states, set suppression flags, purge a list, or reconfigure the consent platform. Consent state is itself an accountability record, and overwriting it destroys the evidence of the defect being remediated.
- **Security or privacy**: the invalid population would be assembled into an artifact carrying identifiers, or a re-consent message would be sent to individuals who have already objected or withdrawn, which turns a remediation into a fresh contact against an existing preference.
- **Source conflict**: the platform export and the operational system disagree on a person's consent state, or the banner text and the archived notice version disagree about what was in force. Both readings are preserved, because adopting the state that keeps the processing lawful is the failure this halt prevents.
- **Connector unreachable**: consent records, archived wording, or the platform export cannot be read, so validity cannot be determined and the population is recorded as undetermined with the missing source named.

A missing opt-in rate, an unconfirmed refresh interval, or an undocumented surface owner is a soft gap. Proceed with the assumption labeled against the surface, and record the open question.

## Downstream handoffs

`cookie-tracking-governance-desk` consumes the consent design, the granularity, and the signal handling, and returns the measurement of what actually fired before the answer was given, which is the test of whether the design works. `transparency-notice-desk` consumes the wording requirements and the version pinning that lets a consent record resolve to a text. `lawful-basis-desk` consumes any activity where consent has been found unavailable or invalid, since that activity now needs a different basis or needs to stop. `rights-request-fulfillment-desk` consumes withdrawal propagation, because a withdrawal that did not reach a vendor becomes an objection complaint later. `processor-vendor-agreement-desk` consumes the list of vendors that hold their own copy of a permission and therefore need an instruction when it changes. `retention-deletion-desk` consumes the derived data produced under invalid consent. `privacy-program-metrics-desk` consumes consent and opt-out rates with the population and surface each was measured over.

## Quality bar

Good consent work quotes. It puts the exact string a person saw next to the limb it fails, names the surface and the date it was captured, and resists the urge to describe wording in the abstract. It treats granularity as a purpose question rather than a vendor question, and it counts the steps in the withdrawal path against the steps in the grant instead of asserting parity. It follows a withdrawal all the way to the vendor that still holds the audience. It states the enforcement layer for every signal, because that is where the difference between honouring a signal and receiving one is visible. And it sizes the invalid population honestly, including the awkward ones: the pre-ticked box that ran for two years, the list acquired with the company nobody bought consent records for, the purpose added by editing the notice, and the preference centre that offers a toggle no downstream system reads.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
