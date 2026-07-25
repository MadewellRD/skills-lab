---
name: engineering-cost-review-desk
description: run team-facing cloud cost reviews presenting spend in the vocabulary of the services a team actually owns, decomposing movement into consumption rate and allocation change, converting findings into an action set with named owners and dates, placing cost signals where engineering decisions already happen, and proposing guardrails split into what should block provisioning and what should only inform. use for team cost reviews, engineering scorecards, cost accountability models, and guardrail design.
---

# Engineering Cost Review Desk

## Suite workflow mode

This desk is a member of the FinOps Command Desk suite. Complete the review artifact set, update the `finops_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. A partial allocation is a soft gap and is presented to the team as a coverage figure rather than hidden inside a total; a blocking guardrail is a hard halt, because a control that can refuse a provisioning request during an incident is an availability decision wearing a cost label.

Never invent a team's service ownership, spend figures, movement causes, action owners, dates, prior review outcomes, or the guardrail thresholds already in force.

## Role

Own the conversation between the practice and the engineers who can change the number. This desk holds the team-facing cost picture expressed in the vocabulary of the services the team actually owns, movement explained as a consumption change, a rate change, or an allocation change so the discussion is about engineering rather than about the report, the action set with owners and dates rather than a list of observations, cost signals placed where engineering decisions are already being made, guardrail proposals separated into what should block and what should only inform, the accountability model naming who owns a number and what happens when it moves, and the findings that belong to the platform rather than to the team, routed away instead of presented as their problem.

The failure mode this stage exists to prevent is a review that produces agreement and no change. That happens when the cost view is organized by billing constructs the team does not recognize, when the movement is presented as a number rather than as a cause, when the actions have no owner, or when the largest line on the team's report turns out to be a share of a platform they do not operate. Engineers respond to a number they can move; they disengage from one they cannot.

## Use when

- A recurring team cost review, scorecard, or engineering cost forum needs its content, and the content has to be actionable rather than informational.
- A team's spend moved and the cause needs decomposing before anyone asks them to explain it, since a material share of movements turn out to be rate or allocation effects the team did not cause.
- Optimization findings need converting into work a team will actually schedule, with the ask in the vocabulary of the services they own.
- Guardrails are being designed or revised, including provisioning quotas, instance family restrictions, budget alerting, and cost signals in design review or change review.
- Cost accountability needs defining: who owns which number, what a movement obliges them to do, and what happens when nothing happens.
- A cost target has been given to a team and it needs converting into service-level actions with owners rather than staying a percentage on a slide.
- A prior review's actions need closing out, since the review that never checks its own action set becomes a monthly meeting about a chart.

## Do not use when

- The allocation underneath the team view is not established or its coverage is unmeasured. That is `cost-allocation-tagging-desk` and `shared-cost-allocation-desk`; presenting a team a figure built on an allocation nobody trusts loses the room permanently and costs a quarter to recover.
- The opportunities have not been consolidated and netted. That is `optimization-backlog-desk`; taking un-netted lane findings into a team review means asking for work that has already been counted somewhere else.
- The subject is charging the team's cost center rather than informing the team's engineers. That is `chargeback-invoicing-desk`, which has a different audience, a different cadence, and a ledger to balance.
- The subject is a unit cost or a margin figure for a product rather than a service cost picture for a team. That is `unit-economics-desk` and `software-cogs-margin-desk`.
- The finding belongs to the platform: shared cluster idle, observability pipeline volume, network overhead, or a platform default. Route it to `shared-cost-allocation-desk` and the platform's own owner rather than presenting it as the team's problem.

## Required evidence

- Allocated cost for the team with its coverage caveats: which portion is directly attributed, which arrives through a shared split with the method that produced it, and which is unallocated.
- The team's actual service ownership, taken from the service catalog, the on-call rotation, or the code ownership records rather than from the tag that happens to be on the resource.
- The movement decomposition inputs: consumption quantity by service and period, effective rate by service and period, and any allocation or split method change with its effective date.
- Unit economics for the team's services where they exist, so growth is not presented as a regression.
- The opportunity register filtered to this team, netted, with effort, risk, reversibility, and the ask already stated in engineering terms.
- Prior review actions with their owners, dates, and outcomes, including the ones that did not happen and why.
- The guardrails and policies currently in force with their thresholds, their enforcement point, and their exemption path.
- The team's roadmap and current commitments, since the review competes with everything else in their plan and a review that ignores that produces polite agreement.
- The forum and cadence the review runs in, and who attends, because the artifact for a fifteen-minute engineering standup and the artifact for a quarterly leadership forum are different documents.

## Workflow

**Outcome.** A team cost picture organized by the services the team owns; movement decomposed into consumption, rate, and allocation change with the driver named for each material move; an action set with owners, dates, and expected effect; cost signals placed at the decision points the team already uses; guardrail proposals split into blocking and informing with the failure behavior of each stated; an accountability model naming who owns which number; and the findings routed away because they belong to the platform.

**Grounding.** Cost is presented at the level the team can act on, which means service and workload names they use in their own documentation, never billing SKUs or blended account totals. Movement is decomposed before it is discussed, because the same increase looks like negligence, like success, and like a reporting artifact depending on which of the three causes produced it. Coverage is stated with the figure, since a team view built on seventy percent allocation is useful and a team view that silently presents seventy percent as the whole is a trap that springs the first time an engineer checks a service they know the cost of.

**Constraints.** Movement is attributed to a change the team can recognize: a deployment, a traffic increase, a retention setting, a new environment, a commitment expiry, a discount change, or a split method revision. A movement whose cause is a rate or allocation change is labeled as such prominently, because sending a team to investigate an increase that came from an amortization change consumes a sprint and teaches them to ignore the next report. Growth is normalized where a unit metric exists, since a team whose traffic doubled and whose cost rose by sixty percent improved and should not be presented as having regressed. Blended figures are never handed to a team, as there is nothing an engineer can do about a rate that is an artifact of consolidated billing. Actions carry an owner, a date, and the expected effect on a named service, and an action nobody accepted in the room is recorded as unassigned rather than written down as agreed. Platform-owned findings are separated out explicitly and routed, because presenting a team with cluster idle they do not control is the fastest way to end the review's usefulness. Cost signals are placed where decisions already happen rather than in a new process: an estimate in the infrastructure change review, an annotation on the change that provisions capacity, a cost section in the design template. Guardrails state their threshold, their enforcement point, what happens when they trigger, who is notified, and the exemption path.

Introducing a blocking guardrail follows a mandated order, and the reason is recorded here so a later editor does not read it as scaffolding: a control that can refuse a provisioning request is capable of preventing a scale-up during an incident, and that failure has to be impossible before the control is armed.

1. Publish the threshold and its rationale to the teams it will apply to, with the exemption path named.
2. Run the control in an informing mode long enough to see what it would have blocked, and review the false positives with the affected teams.
3. Confirm the break-glass path works and name who can invoke it at any hour.
4. Arm the blocking behavior, with the owner of the availability consequence agreeing in writing.

**Parallel surface.** Teams, services, and individual findings are independent units and fan out safely, as do the per-team cost picture assembly, the per-service movement decomposition, the per-finding ownership routing, and the prior action closeout. Two things run once after the fan-out returns. The movement decomposition has an estate-level component, since a rate change from a commitment expiry or a discount revision hits many teams at once and diagnosing it per team produces the same investigation repeated by every team that received it. And the guardrail set is designed once across teams, because a quota that is right for one team and wrong for its neighbor becomes an exemption process rather than a control.

**Acceptance bar.** Every figure the team sees is in their vocabulary and carries its allocation coverage. Every material movement names a cause classified as consumption, rate, or allocation. Every action has an owner, a date, and an expected effect. Every guardrail states its threshold, its enforcement point, its failure behavior, and its exemption path, and is explicitly marked blocking or informing. Platform-owned findings are absent from the team's action set and present in the routing record.

## Outputs

A complete run delivers this set:

- `team-cost-picture.md`: spend organized by the services the team owns, with the allocation coverage stated, the shared splits identified with their method, and the unallocated share shown rather than folded in.
- `movement-analysis.md`: every material move decomposed into consumption, rate, or allocation change, with the specific driver named and the moves that were not the team's doing labeled clearly at the top rather than in a footnote.
- `action-set.md`: actions with owner, date, the service affected, the expected effect, the effort agreed, and the actions nobody accepted recorded as unassigned with the routing attempt.
- `cost-signal-placement.md`: where cost information enters the team's existing decision points, what it says at each point, what it costs to maintain, and the signals deliberately not added because they would be noise.
- `guardrail-proposals.md`: each proposed control with its threshold, enforcement point, blocking or informing designation, trigger behavior, notification, exemption path, and the failure mode it creates during an incident.
- `accountability-model.md`: who owns which number, what a movement obliges them to do, the cadence, and what happens when an action does not land.
- `platform-routing.md`: findings that belong to the platform rather than the team, with the figure, the platform owner, and why the team cannot act on it.
- `prior-action-closeout.md`: the previous cycle's actions with their outcome, including the ones that did not happen and the reason, since that reason is usually the most useful input to this cycle's realism.
- `review-downstream-handoff.md`: what `chargeback-invoicing-desk` and `optimization-backlog-desk` inherit, including accepted actions with owners and dates.

Depth standard: an artifact is complete when an engineer could leave the review knowing exactly what they own and what they are doing about it, and a platform owner could pick up the routed findings without translation. A cost picture in billing vocabulary, a movement with no classified cause, an action with no owner, and a guardrail with no exemption path are unfinished rather than draft.

When the allocated dataset, the service ownership record, or the prior action history exists and cannot be read, the run delivers `review-connector-diagnostic.md` naming each unreachable source and the parts of the team picture it leaves ungrounded, in place of the view that source would have grounded. A team's services are never inferred from resource names.

Anti-fabrication guard: the specific damage available on this desk is attribution, and it is paid for in engineering trust rather than in dollars. Telling a team that their spend rose thirty percent when a commitment expired, a discount step changed, or a shared split method was revised sends competent people to hunt for a regression that does not exist, and they find nothing, and the next report gets less attention than this one. So every movement is classified into consumption, rate, or allocation before it is presented, and where the decomposition could not be completed the movement is labeled as undecomposed rather than assigned to the most likely engineering cause. Service ownership comes from the catalog, the rotation, or the code owners, never from a tag value or a resource naming convention, because attributing a service to the wrong team wastes their time and leaves the real owner uninformed. Actions are recorded with the owner who accepted them in the room, and an action with no acceptance is written as unassigned rather than as agreed, since a plan the implementing engineer has never seen is a plan that does not exist. And the allocation coverage travels with every team figure, because the fastest way to lose an engineering audience permanently is to show them a total for a service whose real cost they already know.

## finops_packet fields to update

- `reporting.audiences[]` with the engineering audience, the forum, the cadence, and what this audience can actually act on
- `reporting.views[]` with the team view and the decision it supports, and `reporting.known_distortions[]` for the rate and allocation effects present in the period
- `allocation.allocation_coverage_pct` and `allocation.unallocated` as presented to the team, with the largest contributors named
- `opportunities[].owner` and `state` updated to accepted, scheduled, or rejected with `rejection_reason` for every item the team declined, preserved so it is not re-presented next cycle
- `opportunities[].implementation_effort` revised to the estimate the implementing team gave
- `governance.policies[]` with proposed and existing guardrails, each carrying its enforcement point, its blocking or informing designation, and its exemption path
- `governance.approvals[]` for any blocking guardrail or hard budget stop, with the availability owner named and the authority basis
- `governance.exceptions[]` with granted exemptions, their owner, rationale, and expiry
- `unit_economics[].owner` where the review establishes who can move a metric
- `source_facts[]` with locator and as-of for every cost, movement, and ownership reading, `assumptions[]`, `open_questions[]`
- `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: a guardrail that blocks provisioning, a hard budget stop, or a policy that can fail a deployment is an availability control wearing a cost label. It belongs to platform and engineering leadership, because the failure mode is a team unable to scale during an incident. This is the defining halt of this desk.
- **Production or destructive**: the next action would arm a control in a live environment, apply a quota, revoke a provisioning permission, or change a running configuration on a team's behalf.
- **Release integrity**: a team-facing figure would be presented without its allocation coverage, on a blended rate, or with a movement attributed to the team when the decomposition shows a rate or allocation cause. A wrong attribution costs the practice its audience, and the audience is the mechanism.
- **Source conflict**: the service catalog, the tag inventory, and the ledger cost center mapping genuinely disagree about which team owns a material service, or two datasets give different totals for the same team and period. Record both readings with locators and route the conflict; presenting one of them and hoping is how a review ends.
- **Security or privacy**: the team view would expose another team's cost detail, customer identifiers, or a workload whose existence is restricted from this audience.
- **Connector unreachable**: the allocated dataset, the movement decomposition inputs, or the service ownership record exists and cannot be read, so a team would be shown a cost picture whose composition nobody can explain when they ask.

An unassigned action, an unestimated effort, a service with no documented owner, and an incomplete prior-cycle outcome are soft gaps. Name them, label the assumption in the artifact, and continue. Presenting a movement as a consumption change because the decomposition was not finished is never an acceptable way to fill a review agenda.

## Downstream handoffs

`chargeback-invoicing-desk` is next in the default sequence and inherits the team-level position, the disputes this review surfaced about a split method, and the coverage caveats that will reappear as questions on a statement. `optimization-backlog-desk` receives the acceptance and rejection states with owners, dates, and revised effort estimates, and the rejection reasons that keep the item from being rediscovered. `shared-cost-allocation-desk` receives the split-method challenges the review produced, which is where most of them originate. `unit-economics-desk` receives the metrics the team agreed they can move. `finops-maturity-desk` receives the persona adoption evidence: which teams act on the review, which receive it, and which have stopped attending. Send accepted implementation work to the owning teams through the SDLC suite, packaged for Jules with the service, the change, the expected effect, and the rollback; send guardrail implementation to the Platform Engineering suite, and send any availability trade-off to the SRE Reliability suite.

## Quality bar

Good engineering cost review is a working session rather than a report-out. Its numbers are labeled with names the team uses, so nobody spends the first ten minutes decoding a service identifier. It says up front which part of the movement was theirs and which was the practice's own doing, which is the single behavior that earns an engineering audience. It normalizes for growth, because punishing a team for serving more traffic teaches them to hide it. It leaves with owners and dates, not with agreement. It routes platform findings away rather than making them somebody else's homework. Its guardrails are mostly informing, because a control that blocks is a control that eventually blocks the wrong thing at three in the morning, and the ones that do block have a break-glass path somebody has actually used. And it opens by closing out last cycle's actions, since a review that never checks whether anything happened is a meeting rather than a mechanism.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
