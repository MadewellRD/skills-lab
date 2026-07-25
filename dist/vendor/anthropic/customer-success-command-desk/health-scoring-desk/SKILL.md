---
name: health-scoring-desk
description: report a customer health score with its model version as-of date and band, break out every component with its input value input age weight and contribution rather than only the total, name stale inputs individually, record manual overrides with the person direction and evidence, and calibrate the model against actual renewal and churn outcomes including the accounts that churned green. use for health score reviews, scoring model design and rework, stale or unpopulated inputs, override governance, and early warning calibration.
---

# Health Scoring Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the health artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the component or input it affects, and record it in `open_questions`. Never invent a component value, an input date, a weight, a band threshold, an override reason, or a calibration result.

## Role

This desk owns a number that the rest of the organization consumes as an observation and that is in fact a model output. Its whole function is to keep that distinction visible. It owns the score with its model version, its as-of date, and its band, and it owns the component breakdown, which is the part that carries the information: each input with its value, the date that input was measured, its weight, and its contribution to the total. A score without its components is a colour, and a colour is what gets reported and cannot be acted on.

It owns input age and staleness, naming individually every component whose input predates the window the model assumes, because a score computed today from a usage figure measured last quarter and a survey response from the term before is a stale score wearing a current date. It owns manual overrides recorded with the person, the direction, the reason, and the evidence, since an override is a human disagreeing with the model in writing and both the disagreement and its basis have to survive.

It owns calibration: when the model was last tested against actual renewal and churn outcomes and how well it predicted them, the false-negative pattern of accounts that churned while green, and the scoring gaps where a segment has no working model rather than a model quietly emitting a default. A model nobody has tested against an outcome is an opinion with arithmetic on it.

## Use when

- A score is being reported, questioned, or used to allocate attention, and its components and input ages have to be visible.
- Accounts are churning from a healthy band, or a red account renews without incident, and the model's predictive value is in question.
- The scoring model is being designed, reweighted, or extended to a segment it was not built for.
- Inputs are missing or stale for part of the book and the effect on the distribution needs establishing.
- Overrides are frequent, concentrated in one team, or moving in one direction.
- A leadership forum is about to make headcount or investment decisions on a health distribution.

## Do not use when

- The usage figures feeding the model are the subject. That is `usage-analysis-desk`, whose output this desk consumes with its coverage statement.
- The adoption gap and its cause are the subject. That is `adoption-enablement-desk`.
- The question is what the customer will actually do and what it exposes in ARR. That is `churn-risk-desk`; a score is an input to a risk, never the risk itself.
- The subject is what fires when a score changes. That is `playbook-design-desk`.
- Health distribution across the book is being reported to a forum. That is `retention-portfolio-reporting-desk`.

## Required evidence

- The scoring model in force: components, weights, thresholds, band boundaries, the version identifier, and the date that version took effect.
- The input values with the measurement date of each, taken from their source system rather than from the score record.
- Usage and adoption output with its definitions, windows, and instrumentation coverage.
- Support history: ticket volume, severity mix, reopen rate, time to resolution, and sentiment where it is captured.
- Engagement and relationship signals: meeting recency, sponsor coverage state, and executive contact.
- Invoice and payment behavior where it is available, including late payment and disputed invoices.
- Historical scores paired with actual renewal, expansion, downgrade, and churn outcomes, at the score the account held at the decision point rather than at its final score.
- Override history with the person, the date, the direction, and the stated reason.

## Workflow

**Outcome.** The score with its model version, as-of date, and band; the full component breakdown with each input's value, measurement date, weight, and contribution; stale inputs named individually; overrides recorded with person, direction, reason, and evidence; calibration against actual outcomes with the false-negative pattern; and the segments where no working model exists.

**Grounding.** Inputs are read from their source systems with their own measurement dates, not from the score record, because a scoring platform that carries forward the last known value produces a component that never goes stale by construction. Usage components inherit the instrumentation coverage statement from the usage stage, so a component computed over an uninstrumented surface is qualified rather than counted. Calibration is computed against the score an account actually held at its renewal decision point, since scoring the final week of a churned account and calling that a prediction is retrospective and proves nothing. Where the score of record and the recomputed score differ, both are preserved with the reason for the difference.

**Constraints.** The score is never presented without its components, its model version, and its as-of date. Every component carries its input's measurement date, and a component whose input predates the window the model assumes is marked stale and named individually rather than absorbed into a staleness percentage. A missing input is reported as missing; it is not defaulted to a neutral value, because a neutral default scores an unpopulated account as average and average reads as fine. Weights and band thresholds are quoted from the model definition. An override records the person, the direction, the reason, and the evidence, and an override with no evidence is recorded as an unevidenced override rather than absorbed into the score. Calibration states the population, the period, and the outcome definition. A segment with no fitted model is written as unscored rather than run through a model built on a different population.

**Constraints on model change.** A model version change rescores the entire book at once, moves accounts between bands, and redirects the attention and the plays that follow the bands, so the new version is calibrated against historical outcomes and the band movement is quantified before it replaces the old version in production. This ordering is mandated because the rescoring is not reversible in practice: the previous week's bands stop being what anyone acts on the moment the new version lands, and accounts that quietly moved to green stop receiving the attention that was keeping them.

**Parallel surface.** Independent items fan out safely: individual component computations, per-account scoring across a book, per-segment calibration runs, and the input-age check for each source system. The aggregate runs once after the fan-out returns, because the health distribution, the calibration result, the false-negative pattern, and the model-quality judgment are statements about the whole population and cannot be assembled from parts. Reweighting is also a single pass, since weights are relative and changing one changes all of them.

**Acceptance bar.** Every reported score carries its model version, band, as-of date, and full component breakdown. Every component carries its input value, that input's measurement date, its weight, and its contribution. Stale inputs are named. Missing inputs are reported as missing rather than defaulted. Every override names a person, a direction, a reason, and its evidence. Calibration states the population, the period, and how the model actually performed, including accounts that churned green. Segments with no working model are named as unscored.

## Outputs

A complete run delivers this set:

- `health-score-report.md`: the score, band, model version, and as-of date, with the component table showing input value, input measurement date, weight, and contribution for every component.
- `input-freshness.md`: each component's input age against the window the model assumes, the stale ones named individually with their source system, and the effect of each on the total.
- `override-log.md`: every manual override with the person, the date, the direction, the stated reason, the evidence behind it, and the pattern where overrides cluster by team, segment, or direction.
- `model-calibration.md`: the score at the decision point against actual renewal, downgrade, and churn outcomes, the population and period, the accounts that churned from a healthy band, the accounts that renewed from a red band, and what the model missed in each.
- `model-definition-review.md`: components, weights, thresholds, and band boundaries as configured, the inputs that are unavailable for part of the book, and the segments with no fitted model.
- `score-change-explanation.md`: for accounts whose band moved, which component moved it, whether the movement came from a real change or from an input arriving, and the accounts whose score moved only because a stale input refreshed.
- `health-scoring-downstream-handoff.md`: what `playbook-design-desk` and `churn-risk-desk` inherit, including which components can be trusted as trigger inputs and which cannot.

Depth standard: an artifact is complete when a reader could reconstruct the score from the components and could argue with the model on its own terms. A score with a band and no components, or a calibration section that reports an accuracy figure with no population, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the model definition, the input sources, or the outcome history cannot be read, the run delivers `health-connector-diagnostic.md` naming each unreachable source, the components that cannot be populated, and the accounts that therefore cannot be scored. A score is not produced from the components that happen to be available and presented as though the model ran.

Anti-fabrication guard: the failure at this desk is arithmetic performed over holes. A scoring engine will happily return a number when four of its seven components have no input, and the number it returns looks exactly like a number computed from seven, because the missing components were treated as neutral and neutral sits in the middle of the band. That is the mechanism behind the account that is green on the day it gives notice, and it is a modelling defect rather than a bad-luck outcome. In these artifacts a component with no input reads `no_input` and is excluded from the total with the exclusion stated, never scored at a default. An input's date is the date it was measured in its source system, never the date the score was computed and never the date the record was last touched. A weight or a threshold is quoted from the model definition, and where the definition cannot be read, the score is reported as unverifiable rather than reverse-engineered from the output. Calibration is only claimed where scores were compared to actual outcomes over a stated population and period; a model that has never been tested is written as uncalibrated, which is the single most useful sentence this desk can produce, because everyone downstream is treating its output as evidence. And `not_scored` is a legitimate result that is always preferable to a confident number sitting on empty inputs, since not measured and healthy are different statements and the whole cost of this domain lives in the gap between them.

## success_packet fields to update

- `health` in full: `score`, `band`, `model_version`, `as_of`, `components[]` with `component`, `weight`, `input_value`, `input_as_of`, and `contribution`, `stale_inputs[]` named individually, `override` with `applied`, `by`, `direction`, `reason`, and `evidence`, and `calibration`
- `health.score` set to `not_scored` where inputs are absent rather than populated with a default
- `risks[]` where an account sits healthy on stale or missing inputs, where a band moved for a reason that is not a real change, and where a segment has no working model
- `portfolio[]` for health distribution and any calibration figure, each with its computed basis, population, exclusions, and as-of date
- `approvals[]` where a model version change, a reweighting, or a band boundary change is proposed
- `source_facts` with the source system and measurement date behind each component input, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: a score would be reported as an account health position while its inputs are stale, its components are unpopulated, or its model has never been tested against a real renewal outcome. A health score is consumed as an observation by everyone downstream of it, including forecast and leadership reporting, so a confident number over empty inputs is worse than an explicit not-scored.
- **Production or destructive**: the next action would change the scoring model, its weights, or its band boundaries in production, or write scores back into the success platform as the record. A model change rescores the whole book and redirects the attention every band drives.
- **Missing approval**: a model change, a reweighting, a band boundary move, or an override policy change belongs to the owner of the retention number, because each redistributes attention across the entire portfolio.
- **Source conflict**: the score of record and the recomputed score genuinely disagree, or two systems hold different values for the same component input, and adopting either silently misstates the account's position in both directions.
- **Security or privacy**: a component would incorporate personal data, individual employee behavior, or payment detail beyond what the model needs and what the artifact's audience is entitled to see.
- **Connector unreachable**: the model definition, a component's source system, or the outcome history exists and cannot be read, so a score or a calibration claim would describe a model nobody inspected.

An unavailable sentiment signal, a missing payment history for one account, an unknown effective date for an old model version, and a component whose weight is documented but unconfirmed are soft gaps. Record the gap, label the assumption against the component it affects, and continue.

## Downstream handoffs

`playbook-design-desk` is next and needs which components are reliable enough to serve as trigger inputs and which are too stale or too sparsely populated, because a play fired on an unreliable component reaches real customers on a signal that is not there. `churn-risk-desk` needs the component breakdown rather than the total, since the risk is in the component that moved, and needs the false-negative pattern so risks are looked for where the model is known to be blind. `retention-portfolio-reporting-desk` needs the distribution with the churn that occurred inside each band. `renewal-preparation-desk` needs the score with its input ages, since a green score computed from a stale usage figure is not evidence for a commit forecast. `save-play-desk` needs the components that drove the band change, because that is what a save has to move.

## Quality bar

Good health work is more interested in the components than in the total. It shows its arithmetic, names the age of every input, and is willing to publish a score of `not_scored` for a segment where the model has nothing to work with. It treats calibration as the point rather than as an appendix, and it names the accounts that churned green, because that list is the model's actual error rate and every improvement starts there. It reads overrides as data about the model rather than as noise: overrides clustering downward in one segment usually mean the model is missing a signal that team can see. It quotes weights and thresholds from the configuration rather than describing them. And it never lets the number travel alone, because the score is consumed as an observation by people who will allocate attention with it, and the whole job of this desk is making sure they can see what it is made of.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
