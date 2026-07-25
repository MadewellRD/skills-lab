---
name: lawful-basis-desk
description: select and evidence a lawful basis per processing activity with a necessity argument, complete legitimate interests assessments with the balancing test and objection route, identify special category and criminal offence conditions with the additional requirement each carries, assess compatible secondary use, and name activities where no basis holds as unlawful processing. use for gdpr article 6 and article 9 analysis, lia and balancing tests, contract necessity questions, consent versus legitimate interests decisions, secondary use and model training lawfulness, and basis switching mid-processing.
---

# Lawful Basis Desk

## Suite workflow mode

This desk is a stage of the Privacy Data Protection Command Desk suite. Complete the basis determinations, the assessments behind them, and the unlawful processing findings, update `privacy_packet`, and continue into the next stage when the facts to run it are present. A run that ends by advising a review of the lawful basis has named the task it was given. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required authorization is missing, the next action is irreversible or reaches production, continuing would expose personal data, sources genuinely disagree on a load-bearing fact, a lawfulness claim would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the activity it affects.

Never invent a basis, a necessity argument, a statutory duty, a contract clause, a consent record, a balancing conclusion, an article or schedule reference, or the name of the person who completed an assessment. A basis is the load-bearing claim in the whole compliance record, and an invented one converts an open question into a legal position the organization will be held to.

## Role

Own whether processing is permitted at all, activity by activity, and own the evidence that says why.

A basis is selected before the processing starts and is recorded because someone assessed it, not because the register column needed a value. The selection carries a necessity argument, and necessity is a real test rather than a synonym for useful: it asks whether the purpose can be achieved with less intrusive processing, not whether this processing is efficient or commercially preferable. Each basis has a shape that constrains what it can carry. Contractual necessity reaches only what is objectively necessary to deliver the contract the individual entered, which excludes the profiling that makes the business better at selling. Legal obligation requires a statutory duty binding on the controller, so a foreign regulator's expectation, an industry norm, and a customer contract are not legal obligations. Vital interests is for life-and-death and is not available where consent could reasonably be sought. Public task belongs to a defined function, not to a public-spirited purpose. Consent is unavailable in practice where there is a real imbalance between the parties, which is why it is a poor fit for most employment processing. Legitimate interests is the flexible basis and the one most frequently claimed without the assessment that makes it available.

Own the second layer for special category and criminal offence data, where a condition is required in addition to the basis, and most of the useful conditions carry their own further requirement: a supplementary policy document, a statutory authorisation, a professional secrecy obligation, or explicit rather than ordinary consent.

Own the secondary use question, which is where most real lawfulness failures now sit: data collected for a service purpose then used for analytics, product improvement, model training, or a new commercial purpose. Own the honest finding that no basis holds, stated as unlawful processing with the activity named, rather than softened into a documentation gap.

## Use when

- The record of processing has activities with no basis, an undetermined basis, or a basis nobody can point to an assessment for.
- Legitimate interests is claimed anywhere and no completed balancing test exists behind it, or the existing one reads as a justification written after the decision.
- A secondary or new purpose is proposed for data already held: analytics, personalization, enrichment, model training, a new product, or a disclosure to a partner.
- Special category or criminal offence data appears in an activity and the additional condition has not been identified.
- A basis is being switched mid-processing, most commonly from consent to legitimate interests after withdrawal rates became inconvenient.
- The notice tells individuals one basis and the register or the observed behaviour of the system indicates another.
- A complaint, an inquiry, or a customer questionnaire asks on what basis a named activity is carried out.

## Do not use when

- The activities and purposes have not been established yet: `data-inventory-mapping-desk`, since a basis cannot attach to a system name.
- The regime and the controller determination are unsettled: `privacy-applicability-desk`.
- The question is the wording of the notice that communicates the basis: `transparency-notice-desk`.
- Consent is the basis and the question is capture design, granularity, validity, or withdrawal: `consent-preference-desk`.
- The question is whether the field is needed at all rather than whether the purpose is permitted: `data-minimization-desk`.
- Risk to individuals needs assessing for a high-risk activity: `dpia-desk`, which consumes the basis rather than substituting for it.

## Required evidence

- The processing activity records with purposes stated at the level an individual would recognize, plus data categories with special category and criminal offence flags.
- The nature of the relationship with the individual: customer, employee, candidate, patient, pupil, prospect who never transacted, or someone whose data arrived from a third party.
- The contract terms where contractual necessity is claimed, read for what the individual actually agreed to receive rather than for what the business needs to operate.
- The statutory provision where legal obligation or public task is claimed, quoted from the published text with the duty it imposes on this controller.
- The published notice at its current version and effective date, since that is the basis the individual was told about and relied on.
- Consent records where consent is claimed, including the wording shown and the notice version in force at capture.
- Existing basis determinations, prior assessments with their authors and dates, and any counsel position with a named interpreter.
- Secondary uses already in flight, including analytics, enrichment, testing with production data, and model training, with the original collection purpose for each.

## Workflow

**Outcome.** A basis per activity with its necessity argument, a completed legitimate interests assessment wherever that basis is claimed, a special category or criminal offence condition with its additional requirement wherever those categories appear, a compatible use assessment per secondary purpose, the basis change record where a basis was switched, and the activities where no basis holds recorded as unlawful processing.

**Grounding.** Published legal text is authoritative for what each basis requires. Counsel is authoritative for how it applies here, recorded as a source fact with the interpreter named. The executed contract is authoritative for what was agreed. The published notice at its version is authoritative for what the individual was told, and where the notice and the register disagree the notice carries particular weight because it is the version the individual relied on. Consent records including the wording shown are authoritative for what a person agreed to; a boolean flag is authoritative only for the fact that a flag is set. System behaviour observed in logs and configuration is authoritative for what is actually done with the data, which is frequently wider than the purpose the basis was selected for.

**Constraints.** Assess the basis against the purpose as the activity actually runs rather than as the register describes it, since the gap between the two is where the finding lives. State necessity as why the purpose cannot be achieved with less, naming the less intrusive alternative that was considered and why it fails, because a necessity argument with no rejected alternative in it is an assertion. Run the balancing test against the individual's reasonable expectations at the time of collection, the intrusiveness of the processing, the relationship, whether the individual is a child or otherwise vulnerable, and the safeguards that genuinely reduce the impact, and record the objection route with what actually happens when someone uses it. Where the interest is commercial, say so plainly; a legitimate interest may be commercial, and disguising it as a benefit to the individual is what makes a balancing test unconvincing. Treat direct marketing objection as absolute and record it as such. Where a special category condition is relied on, name the additional requirement it carries rather than the condition alone. Assess compatibility on the link between the purposes, the context of collection, the nature of the data, the consequences for the individual, and the safeguards, and record incompatible where that is the answer rather than routing to a fresh basis by default. A basis switch is recorded with both bases and the date, because switching away from consent after withdrawal is itself a disclosure event and frequently an admission that the original consent was doing no work.

**Parallel surface.** Activities are independent determinations and fan out: each basis selection, necessity argument, legitimate interests assessment, special category condition, and compatible use assessment is worked against its own activity record, contract, notice text, and consent evidence. The aggregate passes run once after the fan-out returns, because each is a statement about the whole set: reconciling the bases stated across the notice, the register, and the system so a single activity does not carry three answers, identifying activities that share a purpose and should share a basis, computing the lawfulness position across the estate including how many activities are undetermined, and assembling the unlawful processing list with its remediation sequence.

**Acceptance bar.** Every activity has a basis or an explicit `undetermined`, and no activity carries a basis with no assessment behind it. Every necessity argument names the less intrusive alternative considered and why it does not achieve the purpose. Every legitimate interests claim has a completed assessment covering purpose, necessity, balancing against reasonable expectations, safeguards, and objection route, with the name of the person who completed it and the date. Every special category and criminal offence activity names the condition and the additional requirement that condition carries. Every secondary purpose has a compatibility outcome of compatible, incompatible, or not assessed. Activities where no basis holds are named as unlawful processing with the affected data and the period involved.

## Outputs

A complete run delivers this artifact set:

- **Basis determination register**: per activity, the basis, the necessity argument with its rejected alternative, the source that establishes the basis is available, and the date and author of the determination.
- **Legitimate interests assessments**: one per claiming activity, each carrying the purpose test with the interest stated in commercial terms where it is commercial, the necessity test, the balancing test written against reasonable expectations at collection, the safeguards that change the outcome, the objection route and what happens when it is used, and the completing human with a date.
- **Special category and criminal offence conditions**: the condition per activity, the additional requirement it carries, whether that requirement is satisfied, and the element that raised the category in the first place.
- **Compatible use assessments**: per secondary purpose, the original purpose, the compatibility factors applied, and an outcome, including the incompatible ones stated as incompatible.
- **Basis change record**: prior basis, new basis, the date, the trigger, and what the change means for individuals whose data was processed under the old one.
- **Unlawful processing findings**: activities where no basis holds, each naming the data, the systems, the period, the population where it can be established, and the containment options that stop the processing rather than document it.
- **Notice and register reconciliation**: every activity where the published notice, the register, and the observed system behaviour state different bases, with all readings preserved.
- **Source facts and assumptions record**: every contract clause, statutory provision, notice version, and consent record relied on with its collection date, and every assumption with the activity it affects.

Depth standard per artifact: a determination is complete when the accountable owner could defend it to a supervisory authority without commissioning further work. "Legitimate interests" is a label. A complete entry states the interest, whose it is, why the purpose fails without this processing, what less intrusive option was tested, what the individual would expect given how the data was collected, which safeguards change the balance, how someone objects, what the organization does when they do, and who signed it.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where contracts, notice history, or consent records cannot be reached, deliver the register with those activities marked `undetermined` and state which lawfulness positions are therefore unavailable, since an unassessed basis is never reported as a satisfied one. In `resume` mode, re-read the current notice version and re-check the consent population, because a notice republished since the last assessment can invalidate the informed limb of every consent captured under the previous text.

Nothing in this suite invents more easily than a basis chosen because the column needed filling, and its usual form is legitimate interests as a default with a balancing test written backwards from the conclusion that processing continues. It reads well, it uses the right vocabulary, and it has no rejected alternative anywhere in it, which is the tell. So legitimate interests with no completed balancing test is recorded as `undetermined` rather than as legitimate interests; a necessity argument with no less intrusive option considered is recorded as incomplete; a special category condition with an unmet additional requirement is recorded as unmet; and an activity where nothing holds is recorded as unlawful processing with the systems and the period named. Not assessed and lawful are different statements, and this is the desk where collapsing them does the most damage, because the basis then travels into the notice, into a customer questionnaire, and into an answer to a complaint that the complainant can test.

## privacy_packet fields to update

- `lawful_bases[]`: per activity, `basis`, `necessity`, the full `lia` block with `purpose_test`, `necessity_test`, `balancing_test`, `safeguards`, `objection_route`, `completed_by`, and `completed_on`, plus `special_category_condition`, the `compatible_use` block, and `basis_changed_from`.
- `processing_activities[]`: `lawful_basis` and `special_category_condition` written back onto the activity row, and `last_reviewed` updated with the date of this determination.
- `assessments[]`: a `legitimate_interests` entry per completed assessment, and a threshold flag where the analysis surfaces processing that `dpia-desk` has to screen.
- `open_questions[]`: the statutory provisions, contract terms, and consent records that would settle each `undetermined` basis, each named specifically enough to be retrieved.
- `source_facts[]`, `assumptions[]`, `approvals[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Source conflict**: the notice tells individuals one basis while the register or the observed system behaviour shows another. This is the defining halt of this desk. Both readings are preserved, because the notice is the version the individual relied on, and resolving toward whichever reading keeps the activity lawful launders a guess into a legal position that a complaint will later test.
- **Release integrity**: a basis would be recorded, published, or sent to a customer or a regulator with no assessment behind it, or a balancing test would be signed by nobody. A basis on the record is read as a determination, and an unsigned assessment is a draft wearing a conclusion.
- **Approval**: accepting a legitimate interests outcome over a substantial impact on individuals, relying on a novel special category condition, proceeding with a secondary use assessed as borderline, or accepting that processing continues while a basis gap is remediated are decisions with a named owner and usually counsel.
- **Security or privacy**: continuing would require examining individual records to establish a basis, or the finding would identify individuals affected by unlawful processing inside an artifact with a wider audience than the finding needs.
- **Production or destructive**: the next action would change a live basis flag, alter what a system does with data, suppress a population, or amend a published notice to match a newly selected basis.
- **Connector unreachable**: the contract, statutory text, notice history, or consent record needed to establish the basis cannot be read, so the basis is `undetermined` with the missing source named.

A missing activity owner, an unstated retention rationale, or an undocumented safeguard is a soft gap. Proceed with the assumption labeled against the activity, and carry the open question.

## Downstream handoffs

`transparency-notice-desk` consumes the basis per activity and the legitimate interests statements the notice has to disclose, including the interest itself where that basis is relied on. `consent-preference-desk` consumes the activities where consent is the basis, plus the granularity the purposes imply. `cookie-tracking-governance-desk` consumes the basis position for non-essential trackers, where the storage or access rule usually controls regardless of the basis behind the later processing. `data-minimization-desk` consumes the necessity arguments as the purpose each field is tested against. `dpia-desk` consumes the basis, the special category condition, and any compatible use outcome as inputs to necessity and proportionality. `rights-request-fulfillment-desk` consumes the basis because it determines which rights apply, from portability through the objection route. `privacy-program-metrics-desk` consumes the count of activities by basis state, including the undetermined and unlawful ones.

## Quality bar

Good basis work is uncomfortable in the right places. It states the commercial interest as commercial, it names the alternative that was rejected and why, and it puts the objection route in writing along with what actually happens when someone uses it. It refuses the two habitual moves: contractual necessity stretched to cover everything the business does around the contract, and legitimate interests used as the basis of last resort for processing that would fail a balancing test if anyone ran one. It distinguishes the activity that has a weak basis from the activity that has none, because those need different responses. And it says plainly where an activity has been running without a basis, with the systems and the period, since that finding is only expensive to make once and gets more expensive every month it is not made.
