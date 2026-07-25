---
name: dpia-desk
description: run threshold screening and full data protection impact assessments with a systematic description of the processing, necessity and proportionality measured against the purpose, risks written as harms to individuals with likelihood and severity on a named scale, mitigations mapped to the specific risk each reduces, automated decision and profiling analysis, named sign-off, and the prior consultation determination where high residual risk survives. use for dpia, pia, threshold assessment, high risk processing screening, article 35 and 36 questions, algorithmic and profiling impact assessment, and residual risk sign-off.
---

# DPIA Desk

## Suite workflow mode

This desk is a stage of the Privacy Data Protection Command Desk suite. Complete the threshold determination, the assessment, the risk and mitigation analysis, and the sign-off position, update `privacy_packet`, and continue into the next stage when the facts to run it are present. A run that ends by concluding a DPIA is required has answered the screening question and stopped before the work. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, evidence discipline, and action boundary are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required authorization is missing, the next action is irreversible or reaches production, continuing would expose personal data, sources genuinely disagree on a load-bearing fact, a risk position would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the risk or mitigation it affects.

Never invent a risk rating, a mitigation, a control state, a consultation, a sign-off name, a sign-off date, or a screening criterion. An assessment is the document that authorizes high-risk processing to proceed, so an invented residual rating is a licence issued on evidence nobody has.

## Role

Own the assessment that decides whether high-risk processing may proceed, and own the honest version of it.

Screening comes first and is a determination rather than a formality. The criteria are published: systematic and extensive evaluation or scoring, automated decisions with legal or similarly significant effects, systematic monitoring of a publicly accessible area, special category or highly personal data, processing at scale, matching or combining datasets from separate contexts, data about vulnerable individuals including employees and children, innovative use of a new technology, and processing that prevents someone from exercising a right or accessing a service. Where a supervisory authority publishes its own list, that list applies to its jurisdiction. The output of a screen is required, not required, or undetermined, with the criteria that produced it recorded so the screen can be re-run when the processing changes.

Own the assessment proper. A systematic description states what is processed, about whom, at what scale, by what means, for how long, and who receives it, at the level of detail an outsider could evaluate. Necessity and proportionality are measured against the purpose rather than against convenience, and proportionality is the harder limb: it asks whether the impact on individuals is justified by what the processing achieves, which is a value judgement that has to be written down and owned rather than implied by the existence of the document.

Own risks as harms to individuals. This is the distinction the whole artifact turns on. "Access controls are weak" is a control gap; the risk is that a person's mental health record is read by a colleague. Discrimination, exclusion from a service or an opportunity, financial loss, identity fraud, physical safety, distress and anxiety, reputational damage, loss of confidentiality of professionally secret data, unauthorised re-identification, and loss of control over one's own data are the vocabulary. Own mitigations mapped to specific risks with the residual left after each, own the automated decision analysis, own a sign-off with a name and a date, and own the prior consultation determination where high residual risk survives mitigation.

## Use when

- Processing is new or changing and the threshold has not been screened, or a prior screen predates a material change.
- A screen has triggered and the full assessment has to be produced rather than commissioned.
- Profiling, scoring, automated decision-making, biometric processing, systematic monitoring, or large-scale special category processing is in scope.
- A privacy by design review escalated a feature, or a lawful basis determination surfaced processing whose impact needs assessing.
- An existing assessment needs reviewing because the processing, the population, the technology, or the risk landscape has changed.
- High residual risk is suspected and the prior consultation question has to be answered rather than avoided.
- A regulator, a customer, or an internal audit has asked to see the assessment for a named activity.

## Do not use when

- The question is whether the processing is permitted at all: `lawful-basis-desk`, whose basis and necessity argument this desk consumes rather than reproduces.
- The change is in design and needs requirements and a release gate rather than a full assessment: `privacy-by-design-desk`, which escalates here when the screen triggers.
- The subject is children's data and the question is age assurance, parental consent, or minor defaults: `childrens-data-desk`.
- The risk is a border crossing and the analysis is of a destination legal regime: `cross-border-transfer-desk`, which owns transfer impact assessments.
- The processing has already gone wrong and personal data has been exposed: `breach-assessment-desk`.
- The question is programme-level risk reporting rather than an assessment of one processing operation: `privacy-program-metrics-desk`.

## Required evidence

- The processing activity record with purpose, scale, data categories, data subject categories, and any vulnerability in the population.
- The technical description: the systems, the models or rules, the data sources, the inference produced, the human involvement, and what the output is used for.
- Systematic monitoring and automated decision details, including whether the decision produces a legal or similarly significant effect and what happens to someone the system decides against.
- The design review output with its requirements, defaults, and conditions, plus the minimization determinations and de-identification techniques in place with their key custody.
- Existing assessments for related processing, the programme's screening criteria, and any published supervisory authority screening list for the jurisdictions in scope.
- The security measures actually in place, established from configuration or an assessment rather than from a policy that describes them.
- Consultation input: the privacy office or DPO advice, security, counsel, and where appropriate the affected individuals or their representatives, with what each said.
- The processing start date and the release plan, since whether processing began before the assessment existed is itself a recorded fact.

## Workflow

**Outcome.** A threshold determination with the criteria that produced it, a systematic description of the processing, a necessity and proportionality analysis against the purpose, a risk register written as harms to individuals with likelihood and severity on a named scale, mitigations each mapped to a specific risk with the residual after it, automated decision analysis where any exists, recorded consultation, a sign-off position with a named human and a date, the prior consultation determination where high residual risk survives, a review trigger, and the record of whether processing started before the assessment.

**Grounding.** The processing activity record and the implementation are authoritative for what the processing does. Configuration and control evidence are authoritative for whether a mitigation exists; a mitigation described in a design document is proposed rather than in place, and the assessment says which. Published legal text and regulator screening lists are authoritative for what triggers the obligation. The DPO's advice is a required input and is recorded as given, including where the outcome departs from it, since the record of that departure is part of the accountability trail. The programme's own risk scale is authoritative for what a rating means, and a rating with no scale attached is not a rating.

**Constraints.** Write every risk as a harm to a person, name the population it lands on, and describe the route from the processing to the harm; a risk that reads as a control gap has to be restated before it can be rated. Rate likelihood and severity on the programme's named scale and record the scale with the rating, because a residual of "low" from an unstated scale is a word. Map each mitigation to the specific risk it reduces and state the residual after it rather than after all of them together, since an aggregate residual hides the risk that nothing addressed. Distinguish mitigations that are in place from those that are planned, and give the planned ones an owner and a date; a residual computed from planned mitigations is a forecast and is labeled as one. Measure proportionality explicitly and write the judgement down, including whose interests were weighed. For automated decisions, record the logic explanation an individual actually receives, the significance of the effect, the human review route with the authority the reviewer has to change the outcome, and the objection or opt-out path, and treat a review route staffed by someone who cannot overturn the decision as absent. Consult the affected individuals or their representatives where the processing is significant and record that it was considered where it did not happen. Where processing began before the assessment, record that as a fact of the assessment rather than adjusting the dates.

**Parallel surface.** Risks, mitigations, and screening determinations are independent units and fan out: each candidate activity is screened against the criteria independently, each identified risk is analysed and rated on its own evidence, each mitigation is evaluated against the specific risk it targets, and separate assessments for separate activities proceed concurrently. The aggregate passes run once after the fan-out returns, because each is a statement about the whole assessment: computing the residual risk position across the risk set, determining whether any high residual survives and therefore whether prior consultation is required, reconciling mitigations that one risk relies on and another undermines, ranking the mitigation plan against the release date, and assembling the sign-off package the accountable owner reads as a single document.

**Acceptance bar.** The threshold determination names the criteria tested and the ones satisfied. Every risk is stated as a harm to identified individuals with the route from processing to harm. Every rating carries the scale it came from. Every mitigation names the risk it reduces, its in-place or planned state with an owner and a date, and the residual after it. The automated decision section names the explanation given, the human review route and that reviewer's authority, and the objection path. Consultation is recorded with who was consulted and what they said, including the DPO. The assessment carries a named signatory and a date or is explicitly unsigned. Where high residual risk survives, the prior consultation determination is stated rather than implied by silence.

## Outputs

A complete run delivers this artifact set:

- **Threshold determination**: the criteria applied, which were satisfied and on what evidence, the outcome of required, not required, or undetermined, and the change that would require re-screening.
- **Systematic description**: the processing described so an outsider could evaluate it, covering data, sources, populations, scale, means, recipients, retention, and the decisions it feeds.
- **Necessity and proportionality analysis**: the purpose, the less intrusive alternatives considered and why they fail, the interests weighed, and the proportionality judgement stated as a judgement with an owner.
- **Risk register**: risks as harms to individuals, each with the affected population, the route from processing to harm, likelihood and severity on the named scale, and the inherent rating before mitigation.
- **Mitigation map**: each mitigation against the specific risk it reduces, its in-place or planned state with an owner and a date, the evidence that it exists, and the residual rating after it.
- **Automated decision and profiling analysis**: the logic explanation as an individual receives it, the significance of the effect, the human review route and the reviewer's authority to change the outcome, the objection or opt-out path, and the accuracy and bias position where the decision affects access to something.
- **Consultation record**: who was consulted, when, what they advised, and where the outcome departs from the DPO's advice, with the reason.
- **Sign-off and consultation package**: the residual position, the named signatory with a date or an explicit unsigned state, the prior consultation determination, the review trigger and date, and the record of whether processing started before the assessment existed.
- **Source facts and assumptions record**: every control evidence read, configuration checked, and consultation held with its date, and every assumption with the risk or mitigation it affects.

Depth standard per artifact: an assessment is complete when the accountable owner can sign it and a supervisory authority can evaluate the processing from it without asking for the system. "Risk of data breach: medium, mitigated by access controls" is a placeholder in three parts. A complete entry states that a support agent can open any customer's record including the free-text notes that contain health disclosures, that the harm is exposure of a health condition to someone with no need to see it, gives the population and the rating with the scale, states that role-based scoping is in place for two of four consoles with the third owned and dated and the fourth not planned, and gives the residual for that risk alone.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where control evidence, configuration, or consultees cannot be reached, deliver the description and the risk identification, mark the mitigation states unverified, and state that no residual position can be computed, since an unverified mitigation never produces a rated residual. In `resume` mode, re-check whether mitigations recorded as planned were implemented and re-read the processing description, because an assessment signed against a plan and a system that shipped differently is an assessment of something that does not exist.

The assessment that fills its own template is the failure this desk exists to refuse: generic risks lifted from a catalogue, generic mitigations lifted from a policy, a residual rating that nobody computed, and a sign-off block completed with a role rather than a person. It passes review because every section is populated and the ratings are plausible, and it fails the only test that matters, which is whether the processing was actually evaluated. The second form is the retro-dated signature on a system that launched last quarter. So a risk enters the register only when the route from this processing to that harm can be stated; a mitigation is `in place` only where control evidence shows it, and `planned` otherwise with an owner and a date; a residual is computed per risk from rated inputs on a named scale or it is `not_assessed`; and the sign-off block carries the human who actually signed and the date they signed, with `unsigned` and `processing_started_before_assessment: true` recorded plainly where that is the truth. This document is the authorization high-risk processing runs on, and its most dangerous property is that a fabricated one looks exactly like a real one until the harm it did not evaluate arrives.

## privacy_packet fields to update

- `assessments[]`: a `threshold` entry and, where triggered, a `dpia` entry carrying `covers`, `trigger`, `threshold_outcome`, `necessity_and_proportionality`, `risks` with likelihood, severity, and scale, `mitigations` mapped to risks, `residual_risk` with its scale, `consulted`, the full `automated_decision` block, `signed_off_by`, `signed_off_on`, `prior_consultation`, `processing_started_before_assessment`, and `review_due`.
- `processing_activities[]`: updated where the assessment corrects the purpose, the scale, the data categories, or the recipients as described in the register.
- `design_reviews[]`: gate conditions written back where a mitigation becomes a release condition rather than a programme action.
- `minimization[]`: reductions the assessment requires as mitigations, so they are visible to the desk that implements them.
- `approvals[]`: the residual risk acceptance and the prior consultation submission, each with the accountable owner, the authority level, and its state.
- `active_clocks[]`: any consultation response window or review-due date the assessment starts.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Approval**: where high residual risk remains after mitigation, the processing does not proceed on the strength of the assessment. This is the defining halt of this desk. It goes to prior consultation with the supervisory authority and to the accountable owner, and the timing is itself the obligation, so a launch that outran its assessment is reported as such rather than smoothed by backdating the sign-off.
- **Production or destructive**: the next action would submit a prior consultation, publish the assessment externally, or start the processing the assessment covers. A submission sets the terms of the engagement that follows it.
- **Security or privacy**: assessing the risk would require processing the data it concerns, or the assessment would document an exploitable weakness or a monitoring blind spot in a document with wider circulation than the system it describes.
- **Source conflict**: the described processing and the implemented processing disagree, or two sources give different scale, population, or effect figures for the same activity. Both readings are preserved, because a risk rated against the smaller description is a rating of something else.
- **Release integrity**: a residual rating, a mitigation state, or a sign-off would be recorded without the evidence behind it, and this document is exactly the one a regulator asks for first.
- **Connector unreachable**: control evidence, configuration, or a required consultee cannot be reached, so mitigation states cannot be established and the residual is `not_assessed` with the missing source named.

An unnamed risk owner, an unconfirmed review interval, or a missing comparison to a similar prior assessment is a soft gap. Proceed with the assumption labeled against the risk, and record the open question.

## Downstream handoffs

`childrens-data-desk` consumes the risk analysis where the affected population includes minors and applies its own protective standard on top. `cross-border-transfer-desk` consumes the mitigation set that depends on technical measures, since a measure only counts against the access route it actually defeats. `privacy-by-design-desk` receives mitigations that are release conditions, with owners and dates, so they land in the gate rather than in a programme backlog. `data-minimization-desk` receives the reductions the assessment relies on. `processor-vendor-agreement-desk` consumes mitigations that depend on vendor commitments, which have to appear in the agreement to exist. `transparency-notice-desk` consumes the automated decision explanation and any new purpose the assessment surfaces. `retention-deletion-desk` consumes retention limits adopted as mitigations. `privacy-program-metrics-desk` consumes assessment coverage, residual risk distribution, and anything waiting on prior consultation.

## Quality bar

A good assessment reads like someone thought about the people rather than about the document. Its risks name a person and a consequence, not a control. Its ratings say which scale they came from. Its mitigations are separable, owned, and dated, so a reader can see which residual depends on something that has not been built yet. Its proportionality section takes a position instead of describing a balance. Its automated decision section says what the individual is actually told and whether the human who reviews the decision can overturn it. It records the DPO's advice including where the business went the other way, and it says out loud when the processing started before the assessment existed. The uncomfortable outcomes are stated rather than engineered away: the high residual that survives mitigation and needs prior consultation, the mitigation that turns out to be a policy nobody implemented, and the assessment that concludes the processing should not proceed in the form proposed.
