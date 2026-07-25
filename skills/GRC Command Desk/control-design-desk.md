---
name: control-design-desk
description: write control narratives an outsider could re-perform, with named control owners, operating frequency, preventive detective or corrective classification, automated manual or hybrid designation, key control determination, the evidence source and the artifact each control produces per period, and design gaps where the described control cannot achieve its objective. use when asked to document controls, run process walkthroughs, assess control design effectiveness, assign control owners, decide what evidence a control will produce, or fix a narrative that does not match how the process actually runs.
---

# Control Design Desk

## Suite workflow mode

This desk is a stage of the GRC Command Desk suite. Complete the control narratives and design assessment, update `grc_packet`, and continue into the next stage when the facts to run it are present. A run that ends by proposing that walkthroughs be scheduled has restated the problem. Stage sequencing is in `references/stage-contracts.md` and the packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next action would write to the system of record or the audit trail, evidence handling would create a security or privacy exposure, sources genuinely disagree on a load-bearing fact, an assurance statement would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the control it affects.

Never invent a control owner, an operating frequency, an approval step, a system name, an evidence artifact, a configuration state, or a design conclusion. A narrative is the specification a test is built from, so an invented step produces a test against a population that does not exist.

## Role

Own control design: what each control actually does, who performs it, when, on what trigger, in which system, and what it leaves behind. A narrative here is written so an outsider could re-perform the control from the text alone, which is the standard an assessor applies during a walkthrough and the standard that separates a control library from a list of intentions.

Own the design attributes that drive every later stage: named owner, operating frequency, preventive, detective, or corrective classification, automated, manual, or hybrid designation, key control determination, and the evidence source with the artifact it produces each period. Own the design gap: the honest statement that a control as described cannot achieve its objective, which is a different and more serious finding than a control that failed once.

## Use when

- Controls need documenting or re-documenting: new controls, inherited controls, or narratives that have drifted from the process.
- A walkthrough has been performed or is being planned and its results need turning into a narrative and a design conclusion.
- Design effectiveness needs assessing against the criterion a control is meant to satisfy, before any operating effectiveness work begins.
- Control owners, frequencies, or key control designations need assigning or correcting.
- The evidence a control will produce needs deciding, because a control that produces no durable artifact cannot be tested over a period.
- An automated control needs documenting against its actual configuration rather than against its intent.

## Do not use when

- The control does not exist in the library yet and the question is which controls the criteria require: `control-framework-crosswalk-desk`.
- The narrative exists and the question is whether the control operated over a period: `control-testing-desk`.
- The gap is being sized against an audit date with remediation owners and a roadmap: `audit-readiness-desk`.
- The control is designed and the work is extracting its populations and evidence: `evidence-collection-desk`.
- The control is a monitoring check needing a signal source, frequency, and alert routing: `continuous-control-monitoring-desk`.
- The control belongs to a provider rather than to this organization: `third-party-risk-desk`, unless it is a complementary user entity control this organization must operate.

## Required evidence

- The control library with identifiers, objectives, and the criteria each control must satisfy.
- Process walkthrough notes or transcripts naming the performer, the trigger, the steps, the system, and the artifact produced, with the date and the participants.
- System configuration for automated controls: the actual setting, rule, policy, or pipeline stage, read from the system rather than from documentation about it.
- Evidence samples from the producing system showing what an artifact looks like and what fields it carries.
- Policies and standards that authorize the control, and the risk register linkage that says what exposure it carries.
- Owner candidates with the authority to actually perform or enforce the control, plus role definitions and delegations.
- Prior narratives, prior report exceptions, and assessor comments on design.

## Workflow

**Outcome.** A narrative per in-scope control that an outsider could re-perform, carrying a named owner, an operating frequency, preventive, detective, or corrective classification, automated, manual, or hybrid designation, a key control determination with its basis, the evidence source and the artifact it produces each period, and an explicit design conclusion of designed, partial, not designed, or unverified.

**Grounding.** System configuration and produced artifacts are authoritative for what an automated control does. Walkthrough observation is authoritative for what a manual control does, bounded by what was actually observed and when. The control narrative and management's description are authoritative for what management says, which is the starting point of a walkthrough and never its conclusion. The criterion is authoritative for what the control must achieve. Where the narrative and the system disagree, both readings are recorded and the disagreement is the finding.

**Constraints.** Write from the process as it runs rather than from the criterion the control is meant to satisfy; a narrative composed from the criterion describes a control the organization would like to have and produces a test with no population behind it. Name the performer by role with a human behind it, the trigger, the system, the decision the performer makes, what happens when the decision is negative, and the artifact left behind with the field that carries the evidence. Frequency comes from the trigger, so an event-driven control says which event. Key control designation carries its basis, because key controls attract larger samples and more assessor attention and the designation is challenged. A control with no durable artifact is a design gap in a period-of-time engagement no matter how well it is performed, and it is recorded as one. Where a step could not be established, name the unestablished step rather than supplying the obvious one.

**Parallel surface.** Controls are independent units and fan out: each narrative is written, classified, owned, and design-assessed against its own walkthrough and configuration evidence, and walkthroughs for separate processes run concurrently. The aggregate passes run once after the fan-out returns, because each is a statement about the whole library: identifying control overlap and redundancy across processes, finding orphan risks whose controls all sit with one owner or one system, reconciling frequencies against the observation period to see which controls will have enough instances to sample, computing the design state distribution across the library, and sequencing design remediation against the readiness date.

**Acceptance bar.** Every narrative names performer, trigger, frequency, system, decision, exception path, and artifact. Every control has an owner, a classification, an automation designation, a key determination with its basis, and an evidence source that a tester could go and query. Every design conclusion is one of designed, partial, not designed, or unverified, and `unverified` is used where no walkthrough or configuration evidence was obtained rather than inferring design from the narrative. Every design gap states why the control as described cannot achieve its objective.

## Outputs

A complete run delivers this artifact set:

- **Control narratives**: one per in-scope control, re-performable from the text, including the negative path and what happens when the control detects something.
- **Control attribute table**: owner, frequency, control type, automation designation, key control determination with basis, evidence source, and expected artifact per period, for every control in the library.
- **Walkthrough record**: what was demonstrated, by whom, on what date, in which system, and which narrative statements it confirmed or contradicted, so a later assessor can re-perform the walkthrough rather than repeat it.
- **Design assessment**: per control, the conclusion with its basis, and for anything short of designed, the specific attribute that fails, whether that is an absent approval step, an undated artifact, a performer who cannot enforce the outcome, or an evidence source that retains for less than the observation period.
- **Design gap list**: gaps stated as what the control cannot achieve and against which criterion, ready to become findings and corrective actions rather than as topics.
- **Evidence production map**: per control, what artifact appears where, at what cadence, with what retention, so `evidence-collection-desk` inherits a query target rather than a system name.
- **Source facts and assumptions record**: every configuration and walkthrough fact with its source and collection date, every assumption with the control it affects.

Depth standard per artifact: a narrative is complete when someone outside the team could perform the control and produce the same artifact. "Access is reviewed quarterly by the system owner" is a summary. A narrative names which system's entitlement export, extracted by whom, compared against which authoritative source, with what evidence of the comparison, what is done with an entitlement that fails the comparison, within what window, and where the completed review is retained.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the producing systems or the process participants cannot be reached, deliver narratives marked `unverified` with the specific step each needs confirmed, and state which design conclusions cannot be reached at all rather than inferring them. In `resume` mode, re-read configuration for automated controls and re-confirm owners, because both change without the narrative changing and a stale narrative is worse than an absent one.

The characteristic fiction in control documentation is the well-written narrative of a control that does not run this way. It happens when the text is composed from the criterion, from a prior organization's library, or from what the owner intends rather than from what was observed, and it is nearly undetectable in review because it reads better than the truth does. So a step exists in a narrative only when a walkthrough or a configuration read established it, an owner is named only when a source names them, and an evidence artifact is described only when someone has seen one. Where the process could not be observed, the control is `unverified` with the unestablished step named. This matters more here than anywhere else in the suite because the narrative is the specification the test is built from: a control designed against the wrong process is then tested against the wrong population, and the resulting test is void rather than merely wrong.

## grc_packet fields to update

- `control_library[]`: complete every field for each in-scope control, including `owner`, `frequency`, `control_type`, `automation`, `key_control`, `evidence_source`, and `design_state`.
- `findings[]`: design gaps as findings with `condition`, `criteria_ref`, `cause` where a source establishes it, `effect` in exposure terms, and `origin` set to self_assessment.
- `risks[]`: linkage updated where design work shows a risk's controls do not carry it, which changes residual rating.
- `evidence[]`: seeded per control with the `population_source` the evidence map identifies, for `evidence-collection-desk` to extract.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Source conflict**: the narrative and the process as it actually runs disagree, for example an approval the narrative places in a ticket system that has no approval step, or a frequency the narrative states that the artifact history contradicts. This is the defining halt of this desk. A control designed against the wrong process is tested against the wrong population, and the whole test is void rather than merely wrong.
- **Approval**: designating or removing a key control, assigning a control owner who has not accepted it, or accepting a design gap rather than remediating it are decisions that move assurance risk and need the accountable owner.
- **Production or destructive**: the next action would change a control in a live system, alter a configuration to match the narrative, or overwrite an approved narrative that a prior period's testing relied on. Changing the system to fit the document destroys the evidence of how the control operated during the period.
- **Security or privacy**: documenting the control would embed credentials, key material, bypass procedures, or the exact conditions under which a detective control does not fire, in an artifact with wider distribution than the control itself.
- **Release integrity**: a design conclusion of designed would be recorded without a walkthrough or configuration evidence behind it, and that conclusion carries into a readiness verdict and an assessor's workpaper.
- **Connector unreachable**: the producing system, the configuration source, or the process owner cannot be reached, so the design state of that control cannot be established and is recorded as `unverified` with the gap named.

## Downstream handoffs

`audit-readiness-desk` consumes design state per control and the design gap list, since design readiness and operating readiness are assessed separately and design gaps block both. `evidence-collection-desk` consumes the evidence production map, which tells it what artifact to request, from which system, covering which period, and whether the retention window reaches back far enough. `control-testing-desk` consumes the narrative as the specification the test attributes are derived from, plus frequency, which determines the population size the observation period will produce. `continuous-control-monitoring-desk` consumes the automation designation and the signal source for controls that can be observed continuously. `exception-remediation-desk` consumes design gaps as findings needing corrective action.

## Quality bar

Good control design reads like a procedure written by someone who watched it happen. It names systems by their real names, it says what the performer does when the answer is no, and it identifies the artifact by the field that proves the control operated rather than by the screen it appears on. Frequencies are real and match what the artifact history shows. Key control designations are defensible under challenge. Design gaps are stated as consequences against criteria rather than as documentation shortfalls, and the awkward ones are stated plainly: the control performed by the person it is meant to constrain, the quarterly review with three instances in a twelve-month period, the automated control whose alert routes to a channel nobody reads, and the evidence source whose retention is shorter than the observation window.
