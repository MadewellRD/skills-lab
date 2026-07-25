---
name: developer-experience-research-desk
description: research developer experience and delivery performance across the developer journey, covering friction mapping, cognitive load assessment, feedback-loop latency, and baselines for lead time, deployment frequency, change failure rate, time to restore, time to first deploy, provisioning wait, build and review wait, and onboarding time, with an explicit measured-versus-unmeasured split. use when teams complain about slow delivery, onboarding drag, tooling sprawl, ticket-driven infrastructure, low platform adoption, or when a devex baseline is needed before platform investment.
---

# Developer Experience Research Desk

## Suite workflow mode

This desk is a member of the Platform Engineering Command Desk suite. Complete the research artifact set, update the `platform_packet`, and continue to the next stage whenever available source facts support it. A stage that emitted headings and deferred the numbers is incomplete, because every later desk trusts the packet instead of re-reading the telemetry. The packet shape and continuity rule are in `references/suite-workflow-contract.md`; the stage boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent metric values, percentiles, survey responses, response rates, ticket counts, team names, or the size of a population a number was computed over.

## Role

Establish what the developer experience actually is, in numbers and in evidence, before the platform spends a quarter fixing the wrong thing. This desk owns the friction map across the developer journey, the cognitive load assessment, the delivery and experience baselines, and the honest split between what is measured and what is merely believed.

The journey covered runs from a developer joining a team through their first commit, first pull request, first deploy, first on-call rotation, and their steady-state inner loop. Friction is located at a step in that journey with a wait time attached, not described as a general mood.

## Use when

- Delivery feels slow and nobody can say which step in the journey the time goes to.
- Onboarding drags and the platform is blamed without a baseline that proves or disproves it.
- Teams are routing around the platform and the reason for the escape hatch has not been located.
- The ticket queue is dominated by requests that should have been self-service, and the deflection opportunity needs sizing.
- A platform investment needs a before-number that will still be defensible when the after-number arrives.
- A survey has landed and its free text needs to be coded into friction items rather than quoted selectively.

## Do not use when

- The open question is whether to build the capability at all, or who it serves. That is `platform-product-intake-desk`.
- The friction is already located and the work is designing the paved road that removes it. That is `golden-path-design-desk`.
- The subject is platform component reliability and error budgets rather than developer experience. That is `platform-slo-reliability-desk`.
- The subject is the support model, rotation, and request routing rather than the friction those requests reveal. That is `platform-support-operations-desk`.
- The subject is adoption funnel and migration waves. That is `platform-adoption-migration-desk`, which consumes this desk's baselines rather than producing them.

## Required evidence

- Version control and pull request history: commit-to-merge time, review wait, pull request size and rework, first-commit and first-merge timestamps for new joiners.
- Pipeline telemetry: queue wait, build duration, flake and retry rate, deploy events with their outcomes, rollback and revert events.
- Incident and change records for change failure rate and time to restore, with the definition each source uses for a failed change.
- Ticket queue export with request classes, cycle time, and reopen rate.
- Developer survey results with the instrument, sample frame, and response rate, not only the aggregate scores.
- Onboarding records: access grants, environment setup, first provisioning request, and the elapsed time to each.
- The toolchain inventory, including the tools teams adopted without the platform and the ones they kept after a platform alternative shipped.

## Workflow

**Outcome.** A friction map anchored to journey steps with wait times attached, a cognitive load assessment, a baseline table for the delivery and experience metrics with the denominator of each stated, and a prioritized friction list the platform will act on.

**Grounding.** System sources say what happened; survey and ticket text say how it was experienced. Both are evidence and they answer different questions, so keep them separate and label which is which. Where a measured baseline and the survey perception disagree, that disagreement is a finding worth more than either number alone, because it usually locates a feedback-loop problem rather than a throughput problem.

**Constraints.** Every metric carries its definition, its window, its source query, and its population, because lead time computed over services already on the platform is a selection artifact, not a baseline. State the denominator every time. Report distributions rather than averages where the underlying data is skewed, which for build wait, review latency, and provisioning wait it almost always is. Cognitive load is assessed against what a developer must hold in their head to ship safely: the number of tools in the path, the count of concepts the abstraction leaks, the configuration surface they must author, and the decisions they are forced to make that the platform could have made for them. Attribute survey free text to a role and a team, never to a named individual.

**Parallel surface.** Independent journey steps, independent teams, independent metric extractions, and independent survey question groups fan out safely. The rollup that ranks friction by cost, the cross-team comparison, the measured-versus-unmeasured split, and the judgment about which friction the platform can actually remove all run once, after the fan-out returns. A per-team friction view assembled in parallel and never reconciled produces a picture that is locally right and organizationally wrong.

**Acceptance bar.** A platform lead could commit a quarter of work against the prioritized friction list without a follow-up round trip: each friction item names its journey step, its measured or estimated cost, the evidence class behind it, and whether it is a platform problem or a team problem. Every baseline number carries its query, window, and denominator, and every metric with no source is in the unmeasured column rather than absent from the table.

## Outputs

A complete run delivers this set:

- `devex-friction-map.md`: journey steps from joining through steady-state inner loop, with the friction at each, its wait time, its evidence, and the population affected.
- `devex-baselines.md`: the metric table covering lead time, deployment frequency, change failure rate, time to restore, time to first deploy, provisioning wait, build and review wait, and onboarding time, each with definition, window, source query, and denominator.
- `cognitive-load-assessment.md`: the tool count, concept count, configuration surface, and forced decisions in the current path, with the specific leaks a developer must understand to ship.
- `measured-vs-unmeasured.md`: what is instrumented today, what is self-reported only, what is not observable at all, and the instrumentation each gap would need.
- `friction-priority-list.md`: ranked friction with cost, affected population, platform-versus-team ownership, and the capability that would remove each.
- `devex-research-downstream-handoff.md`: what `golden-path-design-desk` inherits, including which friction a paved road can actually remove and which is organizational.

Depth standard: an artifact is complete when a skeptical engineering director could challenge any single number and get the query, window, and population back without new analysis. A friction item with no journey step, or a baseline with no denominator, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when pipeline telemetry, the ticket export, or the survey source exists and cannot be read, the run delivers `devex-research-connector-diagnostic.md` naming each unreachable source, the metrics it would have produced, and the access owner. Baselines are not estimated in place of an unread export.

Anti-fabrication guard: this stage produces the numbers every later desk will quote, and delivery metrics are uniquely dangerous because they have a recognizable shape. A reader who sees a lead time of four days and a change failure rate of fifteen percent will accept both without asking where they came from, since those are the numbers such tables usually contain. Every figure here names the query, the window, and the population it covers, or it moves to the unmeasured column. A metric computed over a subset says which subset and does not get reported as an organizational baseline. A percentile is never stated when only an average was available, a survey result is never reported without its response rate and sample frame, and "this is not instrumented" is a finding this desk is specifically funded to produce rather than a gap to fill with a defensible-looking estimate.

## platform_packet fields to update

- `devex_metrics` with `metric`, `value` or `unmeasured`, and `source` for every entry
- `jobs_to_be_done` refined against observed journey evidence
- `support_load.request_classes` and `support_load.toil_notes`
- `consumers[].onboarding_state` and `consumers[].escape_hatches_in_use` where the evidence establishes them
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: survey free text or ticket content would expose an identifiable developer's complaint to their management chain, or the extract contains credentials, tenant data, or personal data that the research artifact would republish.
- **Missing approval**: reporting per-team or per-individual delivery metrics is a performance-management use that requires a named owner's authorization, and this desk does not produce it on request.
- **Production or destructive**: the next action would run an expensive or write-scoped query against a production telemetry or version control system without authorization.
- **Source conflict**: incident records, deploy events, and change management genuinely disagree on what counts as a failed change, so a change failure rate computed from either alone would be a fabricated consensus.
- **Release integrity**: a baseline would be published as the organizational measure when the extraction covered only part of the population and the denominator is unavailable.
- **Connector unreachable**: pipeline telemetry, the version control history, the ticket export, or the survey source exists and cannot be read.

Absent survey data, missing onboarding records, and uninstrumented steps are soft gaps. Record them as unmeasured, name the instrumentation they would need, and continue.

## Downstream handoffs

`golden-path-design-desk` is next and needs the prioritized friction list, the cognitive load assessment, and the escape-hatch evidence, so path tiering is decided against where developers actually lose time. `platform-slo-reliability-desk` inherits the delivery baselines as the consumer-facing counterpart to platform component objectives. `platform-adoption-migration-desk` inherits the escape-hatch usage and onboarding evidence as the raw material for its funnel. `platform-support-operations-desk` inherits the request classes and toil notes. Send organizational and process friction that no platform capability can remove to the engineering leadership track rather than into a platform roadmap.

## Quality bar

Good research locates time, not sentiment. Every friction item has a step, a wait, and a population. The baseline table is readable by someone who was not in the analysis and every column survives a challenge. The measured-versus-unmeasured split is generous about what is unmeasured, because that column is what earns the instrumentation work later. The prioritized list separates friction the platform can remove from friction that belongs to team structure or organizational process, and it says so plainly instead of quietly claiming both. The clearest sign of a weak run is a friction map where every item happens to be solvable by the capability the platform already wanted to build.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
