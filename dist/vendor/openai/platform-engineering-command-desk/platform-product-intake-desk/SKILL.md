---
name: platform-product-intake-desk
description: triage internal developer platform demand and frame the platform as a product, covering demand intake and request triage, developer personas and jobs-to-be-done, build versus buy versus adopt disposition, capability scope and published non-goals, funding and ownership constraints, and the success measure plus counter-metric a capability is judged on. use for new platform capability requests, roadmap conflicts, duplicate or shadow tooling, vendor evaluations, platform funding cases, and paved-road scope decisions.
---

# Platform Product Intake Desk

## Suite workflow mode

This desk is a member of the Platform Engineering Command Desk suite. Complete the intake artifact set, update the `platform_packet`, and continue to the next stage whenever available source facts support it. A bare next-desk recommendation is not a finished stage. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; the input and output boundary this desk is held to lives in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent requesting teams, ticket volumes, headcount, budget figures, vendor pricing, adoption counts, roadmap commitments, or approval decisions.

## Role

Own the platform's front door. This desk decides whether a request is a platform problem at all, who the platform is building for, whether the capability is built, bought, or adopted from a team that already has it, what the capability explicitly will not do, and the single measure that will later be used to say the capability worked.

Platform teams fail more often from unbounded scope than from weak engineering. The published non-goal is the load-bearing artifact here, because a platform that absorbs every bespoke request becomes a shared services queue with a paved-road logo on it.

## Use when

- A team asks the platform to own a capability, take over a tool they built, or fund a shared version of something they run privately.
- Two or more teams have independently built the same capability and the duplication needs a disposition.
- A vendor evaluation is on the table and the build-versus-buy-versus-adopt question has not been settled against total cost of ownership and exit cost.
- A request arrives as an executive ask and needs to be tested against actual developer demand before it displaces roadmap commitments.
- The platform surface is creeping and the team needs published non-goals to point at.
- A capability is about to be funded and nobody has written down the number it will be judged on.

## Do not use when

- The question is how painful the current developer experience actually is, or what the delivery baselines are. That is `developer-experience-research-desk`, which owns the friction map and the measured-versus-unmeasured split.
- The question is which stacks get a paved road and what the opinionated defaults are. That is `golden-path-design-desk`.
- The capability is already agreed and the open question is which teams are on it and in what wave. That is `platform-adoption-migration-desk`.
- The question is who has authority to decide, what the RFC path is, or how a standard becomes mandatory. That is `platform-governance-desk`.
- A capability is being retired rather than started. That is `platform-deprecation-sunset-desk`.
- The work needed is a formal product requirements document, technical discovery, or an architecture decision record. Those are cross-suite handoffs to the SDLC suite; label them as such rather than producing them here.

## Required evidence

- The demand signal in its original form: the ticket, RFC, survey free-text response, escalation thread, or incident action item, with requester and date intact.
- The current capability inventory and the developer portal's published surface, so an existing capability is not rebuilt under a new name.
- Prior RFCs and architecture decision records covering the same surface, including ones that were rejected and why.
- The platform roadmap with existing commitments, and the funding or ownership model that says who pays for platform work.
- Support queue volume and request classes for the workaround the capability would replace.
- For a buy disposition: vendor documentation, data-handling and residency posture, contract and renewal terms, integration surface, and the documented exit path.
- For an adopt disposition: the owning team, their stated support commitment, their current consumers, and whether they want to keep owning it.

## Workflow

**Outcome.** A triaged demand item carrying a disposition, the personas and jobs-to-be-done it serves, a scope statement with published non-goals, and a success measure paired with the counter-metric that catches the measure being gamed.

**Grounding.** Read demand from the sources that record it happening, meaning the ticket queue, survey free text, and incident action items, and read intent from the roadmap, RFCs, and portal. When an executive ask and the ticket queue disagree about how broad the demand is, that gap is the finding; record both with attribution rather than resolving one into the other.

**Constraints.** Personas are synthesized from observed requests and recorded roles, not from an idealized developer. Jobs-to-be-done are written as the job the developer is trying to finish, not as the feature the platform wants to ship. Every disposition carries total cost of ownership across build, run, support, and exit, because the exit cost is what makes a cheap buy expensive three years later. Non-goals are written as commitments a reader can hold the platform to, not as hedges. The success measure is a single number with a named source, and it comes with a counter-metric: time to first deploy falling while escape-hatch usage climbs is a failed capability, not a successful one.

**Parallel surface.** Independent demand items, independent vendor candidates, and independent adopt candidates are separate evaluation units and fan out safely. The ranked intake backlog, the portfolio-level duplication judgment, and the roadmap displacement decision run once, after the fan-out returns, because each depends on seeing every item at the same time.

**Acceptance bar.** A platform lead could take the disposition to a funding conversation without a follow-up round trip: every persona traces to observed requests, the disposition names its decisive criterion rather than listing all of them, the non-goals are specific enough to decline a real request, and the success measure names the query or export that will produce the number.

## Outputs

A complete run delivers this set:

- `platform-intake-brief.md`: the demand item, its origin and requester, the triage result, the affected population with its evidence, and the recommended disposition with the criterion that decided it.
- `developer-personas-jtbd.md`: personas with the request evidence behind each, and jobs-to-be-done written as outcomes the developer is chasing.
- `capability-scope-and-non-goals.md`: what the capability covers, the explicit non-goals, the boundary with adjacent internal teams, and the requests this capability will decline.
- `build-buy-adopt-analysis.md`: candidates scored on differentiation, total cost of ownership, staffing load, integration surface, data posture, and exit cost, with the runner-up and why it lost.
- `success-measure-definition.md`: the measure, its baseline state, the counter-metric, the data source for each, and the review point at which the capability is judged.
- `platform-intake-downstream-handoff.md`: what `developer-experience-research-desk` inherits, including which friction claims still need a baseline.

Depth standard: an artifact is complete when a platform lead and a finance or governance partner could both act on it unchanged. A persona with no request behind it, a disposition with no exit cost, or a success measure with no data source is an unfinished artifact rather than a first draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the ticket queue, survey export, or roadmap source exists and cannot be read, the run delivers `platform-intake-connector-diagnostic.md` naming each unreachable source, what it would have established, and who can grant access. Disposition recommendations are not drafted on top of an unread demand record.

Anti-fabrication guard: demand is the single easiest thing to manufacture at this desk, because a plausible sentence about what developers want reads exactly like a finding. Demand laundering is the specific failure: one director's escalation is written up as broad developer demand, and by the time it reaches the roadmap nobody can trace it back to a single thread. If the evidence is one escalation from one requester, the brief says one escalation from one requester and names them. Affected-population counts name the ticket query or survey export that produced them or are written as uncounted. A persona with no observed request behind it is listed as hypothesized and flagged for the research stage, and a vendor's pricing, terms, or data posture is quoted from the vendor's own documentation or recorded as not established.

## platform_packet fields to update

- `platform_surface` and `platform_maturity`
- `developer_personas` and `jobs_to_be_done`
- `consumers[].tenant` for teams named in the demand evidence
- `governance.funding_or_ownership_model`, `governance.decision_forum`, `governance.approval_gates`
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: the disposition commits funding, headcount, a vendor contract, or displaces an existing roadmap commitment, and no named owner has authorized it.
- **Production or destructive**: intake would absorb or retire another team's running capability, which is a tenant-affecting removal and runs under the ordered gates in `references/suite-workflow-contract.md` rather than as an intake recommendation.
- **Security or privacy**: a buy or adopt option would move source code, secrets, tenant data, or personal data to a new processor, and the data-handling or residency posture is not established from vendor documentation.
- **Source conflict**: the roadmap, the funding model, and the request record genuinely disagree about who owns the capability, and choosing one silently would launder a guess into a platform commitment.
- **Release integrity**: the capability is already published in the portal as available and no template, module, or pipeline evidence supports that claim.
- **Connector unreachable**: the ticket queue, survey export, roadmap, or capability inventory exists and cannot be read.

Missing effort estimates, unpriced vendor options, and unmeasured baselines are soft gaps. Proceed with the gap named and the assumption labeled.

## Downstream handoffs

`developer-experience-research-desk` is next and needs the personas, the jobs-to-be-done, the affected population with its evidence, and the success measure, so it baselines the journey the capability actually claims to improve rather than a generic one. `golden-path-design-desk` inherits the scope and non-goals as the boundary of what a paved road may cover. `platform-governance-desk` inherits the funding and ownership model and any approval gate this stage opened. Send formal requirements and technical discovery to the SDLC suite, labeled as a cross-suite handoff.

## Quality bar

Good intake reads like a product decision, not a request log. The disposition is defensible to the team whose capability was declined. The non-goals are specific enough that a real incoming request can be pointed at them and closed. Personas are recognizable to the developers they describe, including the ones the platform serves badly. The success measure is one number rather than a dashboard, its counter-metric would actually fire if the capability were gamed, and both name where the number comes from. The strongest signal of a good intake artifact is that it can say no, in writing, to a named request.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
