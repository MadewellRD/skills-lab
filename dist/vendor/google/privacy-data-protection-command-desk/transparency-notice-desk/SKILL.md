---
name: transparency-notice-desk
description: design notice architecture across layers and surfaces, check disclosure coverage element by element against each applicable regime, place notice at collection and just-in-time disclosures where they are needed, maintain versions and effective dates, and decide whether a change is material enough to require telling existing individuals. use for privacy policy drafting and review, notice at collection, layered and just-in-time notices, article 13 and 14 disclosure gaps, source disclosure for indirectly collected data, employee and candidate notices, and notice change materiality.
---

# Transparency Notice Desk

## Suite workflow mode

This desk is a stage of the Privacy Data Protection Command Desk suite. Complete the notice architecture, the disclosure coverage check, the drafts, and the change materiality determination, update `privacy_packet`, and continue into the next stage when the facts to run it are present. A run that ends by recommending the privacy policy be updated has restated the request. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required authorization is missing, the next action is irreversible or reaches production, continuing would expose personal data, sources genuinely disagree on a load-bearing fact, a public statement would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the notice or surface it affects.

Never invent a recipient, a retention period, a transfer mechanism, a legal basis, a right the individual does not have under the applicable regime, a contact route, a source of indirectly collected data, or an effective date. A notice is a public statement the organization is held to by every regulator and every individual who read it, and it becomes the criterion later findings are written against.

## Role

Own what individuals are told, where they are told it, and when.

Notice is architecture rather than a document. A privacy policy is the full layer, and it is not read; the layers that are read are the notice at or before the point of collection sitting next to the form, the just-in-time disclosure appearing at the moment a permission is requested or a sensitive field is entered, the in-product setting text, the script a call centre agent uses, and the paragraph on the paper form. Own all of them, including the surfaces privacy programmes routinely miss: recruitment and candidate notices, employee and contractor notices, CCTV and premises signage, in-product analytics disclosure, notices for data collected from a third party rather than from the individual, and the notice a partner shows on the organization's behalf at a collection point it controls.

Own disclosure coverage as an element-by-element check rather than an overall verdict. Each regime specifies a list, and the lists differ. The demanding elements are the ones drafters generalize: the recipients or at least their categories stated at a level that means something, the retention period or the criteria that determine it, the transfers with the mechanism and how to obtain a copy of the safeguards, the legitimate interests where that basis is relied on, whether providing the data is a statutory or contractual requirement and what happens if the individual declines, meaningful information about the logic of any automated decision with its significance and envisaged consequences, and where data was not collected from the individual, the categories of data and the source including whether it came from a publicly accessible source.

Own versioning and change materiality. A version with an effective date is what lets the organization prove what a person was shown on the day they were shown it, which is what consent validity and most complaints turn on. Materiality is the harder call: a new purpose, a new recipient category, a new transfer destination, a basis change, or an extended retention period reaches existing individuals directly, while a clarification or a restructuring is republished. Getting this wrong in the permissive direction means a purpose was added by quietly editing a page.

## Use when

- A privacy notice is being written, rewritten, or reviewed against what the organization actually does rather than against a template.
- A new collection surface is launching: a form, an app, an SDK-based feature, a call centre flow, an in-store or offline channel, or a partner-hosted collection point.
- A processing change has happened upstream, and the question is whether the notice has to change and whether existing individuals must be told directly.
- Disclosure gaps need identifying individually, for example after a complaint, a questionnaire, or an inquiry that alleges people were not told something.
- Data is being collected from somewhere other than the individual and the source disclosure and its timing need settling.
- Notices are needed in more than one language, at a reading level a general audience can use, or in an accessible format.
- Automated decision-making exists and the explanation an individual receives has to be written.

## Do not use when

- The basis itself is unsettled: `lawful-basis-desk`, because a notice cannot disclose a basis nobody selected.
- The purposes, recipients, transfers, and retention that populate the notice are unknown: `data-inventory-mapping-desk`.
- The surface is a consent request and the question is granularity, wording validity, or withdrawal: `consent-preference-desk`.
- The surface is a cookie banner and the question is which trackers fire and when: `cookie-tracking-governance-desk`.
- The audience includes children and the question is age-appropriate presentation and defaults: `childrens-data-desk`.
- An individual has asked what the organization holds about them: `rights-request-intake-desk`.

## Required evidence

- The processing activity records carrying purposes, bases, recipients, transfers, and retention, since a notice is the individual-facing rendering of the register and inherits its accuracy.
- Every surface where collection happens: web forms, app screens and permission prompts, SDKs, call centre scripts, paper forms, physical premises, and third-party collection points operated on the organization's behalf.
- Current notices with their version identifiers, effective dates, publication locations, and the archived text of superseded versions.
- The sources of indirectly collected data with what arrives from each, including enrichment providers, partners, public sources, and referrals.
- Language, reading level, and accessibility requirements, plus which markets require which languages.
- The rights and complaint routes that actually work: the address or form that reaches the privacy function, the supervisory authority the individual can complain to, and the internal appeal path where a regime provides one.
- Automated decision details where any exist: what the decision is, how significant its effect is, what the individual is told about the logic, and how they obtain human review.

## Workflow

**Outcome.** A notice architecture across layers and surfaces, a disclosure coverage matrix checked element by element against each applicable regime with the missing disclosures named individually, drafted notice text and just-in-time copy for the surfaces in scope, the source disclosure for indirectly collected data with its timing, the version and effective date record, and a change log with a materiality determination per change.

**Grounding.** The processing activity records and the observed system behaviour are authoritative for what the notice has to describe, and where the register and the system disagree the notice cannot be drafted past the disagreement. The published legal text and regulator guidance are authoritative for the required disclosure list per regime. The archived notice at its version is authoritative for what an individual was previously told, which is what a materiality determination is measured against. A notice as a description of practice is authoritative for what someone said and is never evidence of what a system does, so a recipient list that only appears in the notice is unverified until the flow map carries it.

**Constraints.** Draft from the register rather than from a template, and where the register cannot support a sentence, do not write the sentence. State recipients specifically enough to be useful, since "trusted partners" and "service providers" disclose nothing; where a category is genuinely the right granularity, the category is named with examples the individual would recognize. Give a retention period or the criteria that determine it, because "as long as necessary" restates the obligation rather than answering it. Place each disclosure where the decision is made rather than only in the full policy: the permission prompt carries its own purpose, the sensitive field carries its own explanation, and the collection form carries the notice at collection. Write at a reading level a general audience can use, and keep the plain-language version and the legally complete version as the same document rather than as a summary that contradicts its own detail. For indirectly collected data, state the source and give the notice within the required window rather than at first convenient contact. Where the regime provides a right the organization is not offering, that is a finding rather than an editorial choice. Every draft is prepared for publication and stops at the approval gate; publishing, amending, or unpublishing a live notice sits outside this suite's action boundary.

**Parallel surface.** Notices, surfaces, and languages are independent units and fan out: each surface is inventoried, each notice is checked element by element against each applicable regime, each just-in-time placement is drafted against the moment it serves, and translations are prepared per language. The aggregate passes run once after the fan-out returns, because each is a statement about the whole notice estate: reconciling contradictions between the full policy and a just-in-time string that says something narrower, computing disclosure coverage across every surface rather than for the flagship policy alone, deciding materiality for a change that lands on several notices at once, and assembling the single change log and version record that the organization will be asked to produce.

**Acceptance bar.** Every collection surface is inventoried and has a notice or an explicit gap. Every required disclosure element per applicable regime is marked present with the text that carries it or absent by name, with no overall adequacy verdict standing in for the element list. Every statement in a draft traces to a register row, a contract, or a system fact. Every notice carries a version and an effective date, and every change carries a materiality determination with the reason. Automated decision disclosures state the logic in terms an individual can act on and name the route to human review.

## Outputs

A complete run delivers this artifact set:

- **Surface and notice inventory**: every collection point across web, app, offline, telephone, premises, and partner-operated channels, with the notice serving it, its version, its effective date, and its languages.
- **Disclosure coverage matrix**: regime by element by surface, each cell marked present with the sentence that carries it, absent, or not applicable with the reason, so a gap is a named missing disclosure rather than a score.
- **Notice drafts**: the full layer plus the short layer, written from the register, prepared for approval, with any sentence that could not be grounded left out and listed as a blocked disclosure instead.
- **Just-in-time and notice-at-collection copy**: per moment, the trigger, the placement, the text, and the purpose it explains, including permission prompts, sensitive fields, and features that begin a new kind of processing.
- **Source disclosure record**: for indirectly collected data, the source per category, whether it is publicly accessible, the disclosure timing required, and the channel that will deliver it.
- **Change log and materiality determination**: what changed, against which prior version, whether it is material enough to require telling existing individuals, and where it is, the audience, the channel, and the lead time.
- **Gap and remediation list**: every missing or unsupportable disclosure with the desk that has to produce the underlying fact, since most notice gaps are register gaps wearing a drafting label.
- **Source facts and assumptions record**: every register row, contract, and system fact a disclosure rests on with its collection date, and every assumption with the notice it affects.

Depth standard per artifact: a draft is complete when the accountable owner and counsel could approve it without asking what a sentence is based on, and an individual could act on it without reading anything else. "We may share your data with third parties for business purposes" fails both tests. A complete recipient disclosure names the categories with a recognizable example, says what each receives and why, and connects to the transfer statement where the recipient sits abroad.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the register, the archived notice versions, or the collection surfaces cannot be reached, deliver the coverage matrix for what was reachable and state which surfaces are unassessed, because an unassessed surface is never reported as adequately noticed. In `resume` mode, re-read the live notice and its version, since a page edited between readings changes both the coverage answer and the notice version every consent record points at.

Notice drafting is the one privacy artifact with an abundant supply of well-written examples to borrow from, which is precisely why it produces the most confident wrong document in the suite: a notice describing good practice rather than this organization's practice. Borrowed text is fluent, complete-looking, and about somebody else: a rights list including rights the applicable regime does not grant, a retention sentence nobody derived from a schedule, a recipient category chosen for its vagueness, a transfer paragraph mentioning safeguards nobody executed. Every sentence here is a public commitment that will be read back to the organization by a complainant with the system behaviour in front of them. So a disclosure appears in a draft only where the register, a contract, or a system fact supports it, an unsupportable disclosure is listed as blocked with the fact it needs, and a notice that is honestly incomplete is delivered as incomplete with the gaps named individually rather than smoothed into a document that reads finished.

## privacy_packet fields to update

- `notices[]`: per notice, `surface`, `audience`, `version`, `effective_date`, `languages`, `disclosures_covered`, `gaps` named individually, `change_log` with the materiality determination, and `last_reviewed`.
- `processing_activities[]`: recipients, transfers, and retention references corrected where drafting exposed that the register cannot support what the notice needs to say.
- `open_questions[]`: each blocked disclosure with the specific fact and the desk that owns producing it.
- `approvals[]`: publication requests with the accountable owner, the authority level, and the state, since publication sits outside this suite's action boundary.
- `source_facts[]`, `assumptions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: publishing, amending, or withdrawing a notice is an external act with the accountable owner and counsel. This is the defining halt of this desk. A published notice becomes the criterion every later finding and complaint is written against, and it cannot be quietly unpublished once people have relied on it.
- **Release integrity**: a draft would go out asserting recipients, retention, transfers, or a basis that the register and the systems do not support. The notice is consumed as an assertion by people who cannot check the assumption behind it.
- **Source conflict**: the register, the observed system behaviour, and the current notice give different recipient lists, transfer positions, or retention periods. Both readings are preserved and the notice waits, because publishing either one converts a disagreement into a public commitment.
- **Security or privacy**: a draft or a just-in-time string would reveal security detail, an internal identifier, or an individual's data, or a material change would go out to a population assembled from records that were never checked for suppression or restriction flags.
- **Production or destructive**: the next action would push notice text to a live surface, change a consent banner string, or update a version identifier that consent records point back to.
- **Connector unreachable**: the live notice, the archived versions, or the register needed to establish coverage cannot be read, so coverage cannot be stated and the surface is recorded as unassessed.

A missing translation, an unconfirmed reading level, or an unpublished effective date on an old version is a soft gap. Proceed with the assumption labeled against the notice, and record the open question.

## Downstream handoffs

`consent-preference-desk` consumes the notice version and the exact wording in force at each capture surface, since a consent record without the text that was shown cannot prove the informed limb. `cookie-tracking-governance-desk` consumes the tracker disclosure and the banner copy, and returns the scan findings that show whether the disclosed recipient list matches what fires. `childrens-data-desk` consumes the notice architecture where the audience includes minors and replaces the presentation standard. `dpia-desk` consumes the automated decision explanation as an input to the transparency mitigation. `rights-request-intake-desk` consumes the rights and complaint routes the notice publishes, because those are the routes the organization committed to answering on. `processor-vendor-agreement-desk` consumes the recipient categories the notice commits to, since adding a recipient outside them is a notice change rather than a procurement decision. `privacy-program-metrics-desk` consumes disclosure coverage per surface.

## Quality bar

A good notice reads as though the people who run the systems wrote it and the people who read it were considered. It says who receives data specifically enough to be checked, it gives a period or the rule that produces one, it explains an automated decision in terms someone could act on, and its short layer and its full layer say the same thing at different lengths. The surface inventory is where competence shows: the candidate notice, the call recording announcement, the partner-hosted form, and the SDK that collects before anything is shown are all present or all named as gaps. The change log is honest about materiality, including the changes that were material and were previously handled by republishing. And the gap list names disclosures individually, because "the notice needs updating" is a task and "the notice does not state the retention period or the transfer mechanism for two of the four recipients" is a finding.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
