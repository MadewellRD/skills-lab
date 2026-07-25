---
name: control-testing-desk
description: build test plans and execute design and operating effectiveness testing using inquiry, observation, inspection, and reperformance, with sampling method and size recorded against the methodology that set them, attribute testing per sampled item, deviations described by nature and extent rather than counted alone, and a per-control conclusion from the fixed vocabulary of effective, deficient, not tested, or unable to test, recorded in a reusable workpaper. use when asked to test a control, draw a sample, assess operating effectiveness, evaluate deviations, or produce workpapers for an audit or internal assessment.
---

# Control Testing Desk

## Suite workflow mode

This desk is a stage of the GRC Command Desk suite. Complete the test plans, the testing, and the conclusions, update `grc_packet`, and continue into the next stage when the facts to run it are present. A run that ends by proposing which controls should be tested has produced a plan and called it a result. Stage sequencing is in `references/stage-contracts.md` and the packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next action would write to the system of record or the audit trail, evidence handling would create a security or privacy exposure, sources genuinely disagree on a load-bearing fact, an assurance statement would rest on evidence that cannot carry it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the test it affects.

Never invent a population size, a sample size, a sampling method, a confidence level, a deviation threshold, a tested item, a deviation, a tester, a test date, or a conclusion. A test conclusion is the assurance layer's atomic unit: it travels into a report, an assertion, and a customer's purchasing decision, and it is re-performed by the first person who doubts it.

## Role

Own testing: the test plan per control with its objective and method, the sample drawn from an established population with the basis for its size, attribute testing against the control's actual specification, deviations described by nature and extent, the conclusion drawn from the fixed vocabulary, and the workpaper that lets someone else re-perform the whole thing without asking a question.

Own the distinction between design and operating effectiveness, and keep it visible in every conclusion. Design asks whether the control, as it exists, could achieve its objective. Operating effectiveness asks whether it did, across a period, on a population. They fail for different reasons, they are remediated differently, and a report that conflates them misstates what the organization knows about itself.

## Use when

- A control needs a design or operating effectiveness conclusion for an audit, a readiness assessment, an internal audit, or a customer commitment.
- A sample needs drawing from an established population with a defensible basis for the size and the method.
- Attribute testing needs designing from a control narrative, so the attributes match what the control actually does.
- Deviations have been found and need characterizing by nature and extent, and their effect on the conclusion decided.
- Workpapers need producing to a standard that survives assessor re-performance or internal audit review.
- Prior period test results need re-performing, extending, or reconciling against this period's evidence.

## Do not use when

- The population has not been extracted or its completeness basis is not established: `evidence-collection-desk` produces both, and a sample drawn without them yields no conclusion.
- The control narrative does not describe what actually happens: `control-design-desk` fixes the specification before a test is built from it.
- The question is whether the organization is ready to be tested at all, or what window it can evidence: `audit-readiness-desk`.
- A deviation has become a finding needing classification, corrective action, and closure validation: `exception-remediation-desk`.
- The control is evaluated by an automated check on a cadence rather than by a sample: `continuous-control-monitoring-desk`.
- The testing is being performed by an external assessor and the work is responding to them: `audit-engagement-desk`.

## Required evidence

- The control library with narratives, owners, frequencies, control types, automation designations, and key control determinations.
- Populations with their source system, extraction query, record counts, and completeness and accuracy basis.
- Evidence items with their collection dates and the periods they cover.
- The testing methodology in force: sampling approach, size tables or the basis for sizes, confidence expectations, deviation thresholds, and the source that set them.
- The criteria each control maps to, since the criterion sets what the test must demonstrate and the strictest mapped criterion sets the evidence standard.
- Prior period results, known deviations, and prior assessor conclusions on the same controls.
- Tester independence expectations, and who performed the control, since the performer cannot be the tester of record.

## Workflow

**Outcome.** A test plan and an executed test per in-scope control, each carrying objective, method, population with its source, sample with its size basis, attributes tested per item, deviations described by nature and extent, a conclusion from the fixed vocabulary, and a tested-by and tested-on record complete enough that the workpaper can be re-performed by someone who was not there.

**Grounding.** System-generated records are authoritative for whether an instance of the control occurred, bounded by the population they cover. The control narrative is authoritative for what the control is supposed to do, which is where attributes come from and not where conclusions come from. The methodology is authoritative for sample size and method. Inquiry is the weakest method and never stands alone for an operating effectiveness conclusion; corroborate it with inspection, observation, or reperformance, and record which was performed. Prior period conclusions are context and are not evidence about this period.

**Constraints.** Derive attributes from the narrative's actual steps so a test measures the control rather than its topic: who performed it, whether the trigger was met, whether the decision was made, whether the negative path was followed, and whether the artifact carries the date and the approver. Take sample size and method from the stated methodology; where no methodology exists, record the size actually drawn and name the basis as unsourced rather than quoting a size that appears standard. Describe deviations by nature and extent, since three deviations from one root cause in one week is a different control state from three spread across three quarters by three performers, and a count alone cannot distinguish them. Conclude only from the fixed vocabulary: `effective`, `deficient`, `not_tested`, `unable_to_test`. Missing evidence yields `not_tested`, never `effective`. A control whose population could not be established yields `unable_to_test` with the reason recorded.

Operating effectiveness testing follows a mandated order, stated here so a later editor does not read it as scaffolding:

1. Establish the population from its source system and record the query or export that produced it.
2. Show the population complete and accurate, and record on what basis.
3. Draw the sample using the stated method and size, and record both.
4. Test the sampled items against the attributes and record deviations by nature and extent.
5. Conclude, carrying the population, the sample, and the deviation record with the conclusion.

The order is mandated because an assessor re-performs the population before anything else. A sample drawn from a population that was never established does not produce a weak conclusion; it produces no conclusion, and the defect cannot be repaired after the observation period closes because the underlying data has moved on. Reversing steps one and three is the single most common way a program discovers, during fieldwork, that a quarter of its testing has to be redone.

**Parallel surface.** Controls are independent units and fan out: each test is planned, sampled, executed, and concluded on its own population and its own evidence, and testing across separate controls runs concurrently. Attribute evaluation across sampled items within one test is parallel-safe. The aggregate passes run once after the fan-out returns, because each is a statement about the whole set: drawing a single sample across a combined population where one test serves several controls, deduplicating one deviation that fails several criteria into one finding, evaluating whether individually tolerable deviations aggregate into a pervasive condition, computing coverage across the control set with the untested remainder named, and rolling conclusions up into the position `audit-readiness-desk` and `audit-engagement-desk` will report.

**Acceptance bar.** Every test names its objective, its method, its population with source and size, its sample with the size basis, and its attributes. Every deviation is described rather than counted. Every conclusion comes from the fixed vocabulary and carries the evidence it rests on. Every workpaper names the tester and the test date and could be re-performed from the text alone. No conclusion of `effective` exists where the population basis is unknown or the sample was not drawn.

## Outputs

A complete run delivers this artifact set:

- **Test plans**: per control, the objective as design or operating effectiveness, the method, the attributes derived from the narrative, the population definition, the sample size with its basis, and what would constitute a deviation.
- **Workpapers**: per control, the sampled items with their identifiers, the attribute results per item, the exceptions with what specifically failed, the evidence locators, the tester, and the test date, at a depth that survives re-performance.
- **Deviation analysis**: each deviation characterized by nature, extent, root cause where a source establishes it, whether it is isolated or systemic, and its effect on the conclusion, with the reasoning shown rather than asserted.
- **Conclusions register**: one row per control with its conclusion from the fixed vocabulary, its evidence basis, its population and sample, and the criteria it serves.
- **Coverage statement**: controls tested, controls not tested with the reason each, and controls concluded `unable_to_test` with the missing population or evidence named, expressed as coverage of the in-scope control set rather than as a share of the ones that were convenient.
- **Findings for handoff**: deficiencies written as condition, criteria reference, cause where established, and effect in exposure terms, ready for classification rather than as raw test failures.
- **Source facts and assumptions record**: every population and evidence fact with its source and date, every assumption with the test it affects.

Depth standard per artifact: a workpaper is complete when an assessor could re-perform it without a conversation. "Sampled 25 changes, no exceptions" is a summary. A workpaper names the population and its query, the sampling method, the 25 change identifiers, the attributes evaluated per change, where each piece of evidence sits, and what the tester did when an attribute could not be evaluated.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where evidence or producing systems cannot be reached, deliver the test plans in full and record the affected controls as `unable_to_test` with the missing source named, since a plan is genuinely useful and a conclusion without a sample is not. In `resume` mode, re-test rather than carry any conclusion whose evidence predates the current observation period, because a conclusion silently inherits a date it no longer has and prior period results say nothing about this period.

The defining failure in testing is a conclusion written from the control narrative instead of from the sampled items. It is easy to produce because the narrative describes a control that works, it reads exactly like a real conclusion, and it survives internal review; it fails at re-performance, which is where it matters. So a conclusion is written only from the items actually examined, a deviation is recorded only when an attribute actually failed, and sample size, method, and deviation threshold come from a stated methodology or are marked unsourced. Where no sample was drawn the control is `not_tested`, and that is a complete and honest result. **Not tested and no exceptions noted are different statements and never collapse into each other**, and the distance between them is where the organization's real control position lives.

## grc_packet fields to update

- `tests[]`: `test_id`, `control_id`, `objective`, `method`, `population_size`, `sample_size`, `sampling_basis`, `deviations`, `conclusion`, `tested_by`, and `tested_on`.
- `findings[]`: deficiencies with `condition`, `criteria_ref`, `cause`, `effect`, `severity` with the rubric named, `classification`, `owner`, and `due`.
- `control_library[]`: `design_state` corrected where design testing established it.
- `evidence[]`: state updated where testing consumed, exhausted, or rejected an item.
- `risks[]`: residual ratings flagged for re-rating where a linked control concluded `deficient`, since a residual rating rests on controls that operate.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Release integrity**: a conclusion of `effective` would rest on a population nobody established, a sample nobody drew, or inquiry alone. This is the defining halt of this desk. The conclusion travels into a report an external party relies on, and re-performance is the first thing an assessor does, so a hollow conclusion fails loudly rather than quietly and takes the credibility of the surrounding workpapers with it.
- **Approval**: waiving a deviation, treating a deficiency as isolated when the population suggests otherwise, or reducing a sample size below the methodology are judgments that change what the organization asserts, and they belong to the engagement owner rather than the tester.
- **Production or destructive**: the next action would overwrite a workpaper, edit a prior period's conclusion, alter collected evidence, or change a control in a live system mid-test. A test performed across a control that changed during the test measures neither state.
- **Security or privacy**: testing would pull personal data, credentials, customer records, or regulated content into a workpaper. Test the attribute, record the identifier, reference the artifact by locator, and keep the content where it lives.
- **Source conflict**: the evidence and the system record disagree about whether an instance occurred, or the control owner disputes a deviation on load-bearing grounds. Record both readings against the test and route it rather than resolving toward the reading that closes the test.
- **Connector unreachable**: the evidence source or the producing system cannot be read, so the control is concluded `unable_to_test` with the unreachable source named rather than assessed from what it would have shown.

## Downstream handoffs

`continuous-control-monitoring-desk` consumes the controls whose testing is repetitive and evidence-rich, since those are the candidates for automated checks, and needs the attributes the test evaluated. `exception-remediation-desk` consumes deficiencies as findings needing classification, corrective action, compensating controls, and closure validation, and needs the deviation nature rather than the count to size the fix. `audit-readiness-desk` consumes conclusions and coverage to update the readiness position. `audit-engagement-desk` consumes workpapers as the artifacts an assessor will re-perform, and needs them complete enough to hand over without narration. `risk-register-desk` consumes `deficient` conclusions, which invalidate any residual rating that assumed the control operates. `committee-reporting-desk` consumes coverage and conclusion counts with their computed basis.

## Quality bar

Good testing is boring in the right places and specific everywhere else. Populations are reproducible. Sample sizes come from a methodology someone can point to. Attributes match the narrative rather than the criterion's headline, so the test measures the control that exists. Deviations are described in a sentence a control owner would recognize as an account of what went wrong, with the root cause separated from the symptom and the systemic ones distinguished from the one-off. Conclusions use four words and no others. The workpaper is written for a stranger, because the stranger is the assessor, and the difference between a program that passes fieldwork calmly and one that does not is almost entirely visible in the workpapers before fieldwork starts.
