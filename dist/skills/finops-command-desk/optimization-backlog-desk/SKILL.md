---
name: optimization-backlog-desk
description: consolidate cloud cost optimization opportunities into one deduplicated register netted for overlap, prioritized on savings against engineering effort risk reversibility and blast radius rather than on savings alone, assigned to the team that must act with the ask in engineering terms, tracked through accepted scheduled implemented and verified states with rejection reasons preserved, and with savings realization measured against the invoice rather than against the estimate. use for optimization programs, savings target tracking, and consolidating findings from rightsizing waste architecture licensing and commitment lanes.
---

# Optimization Backlog Desk

## Suite workflow mode

This desk is a member of the FinOps Command Desk suite. Complete the backlog artifact set, update the `finops_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. An opportunity with no owner yet is a soft gap and sits in the register as unowned with its routing attempt recorded; a savings total that sums overlapping opportunities is a hard halt before it leaves the practice, because that total is the number a budget gets cut against.

Never invent savings amounts, realized figures, effort estimates, owners, implementation dates, opportunity states, or the billing evidence that a saving actually landed.

## Role

Own the register and the truth of the savings number. This desk holds every opportunity from every lane in one deduplicated set with overlaps netted rather than summed, prioritization on savings against effort, risk, reversibility, and blast radius rather than on savings alone, the sequencing constraint that optimization precedes commitment, ownership assigned to the team that must act with the ask stated in engineering terms, acceptance and rejection states with the rejection reason preserved, savings realization tracked against the bill rather than against the estimate, and the estimate-to-actual gap fed back into how future opportunities are sized.

The problem this stage solves is arithmetic that nobody else in the chain is positioned to catch. Each lane sizes its own findings correctly against its own baseline. Rightsizing sizes an instance change, commitment sizes a rate change on the same instance, scheduling sizes the hours removed from it, and architecture sizes the traffic it stops generating. Every one of those numbers is defensible in isolation, and adding them produces a saving larger than the resource costs. A register that has never been netted grows past the bill, and the first person to notice is the person whose budget was reduced on the strength of it.

## Use when

- Two or more optimization lanes have produced findings and the consolidated position needs to exist before anybody quotes a total.
- A savings target has been set and the register needs to show what is actually available, netted, with what it costs in engineering time to get.
- Optimization work needs sequencing against engineering capacity, change freezes, and the constraint that commitments are sized after the usage changes land.
- Savings claimed in a prior cycle need checking against the invoice, and the realization rate needs measuring rather than assuming.
- The same findings keep resurfacing each quarter and the record of why they were rejected needs to become durable enough to stop the rediscovery.
- An estimate-to-actual gap has appeared and future sizing needs correcting, since a lane that consistently over-estimates by a third is fixable once it is measured.

## Do not use when

- The lane analysis has not been done and there is nothing to consolidate. Run `rightsizing-desk`, `waste-elimination-desk`, `cost-aware-architecture-desk`, `licensing-saas-spend-desk`, and `commitment-portfolio-desk` first; a register assembled ahead of them is a task list.
- The question is how to size or evidence a specific opportunity. That belongs to the lane that owns it, and a re-sizing done here loses the utilization or access evidence behind the original.
- The subject is presenting cost to a team, explaining movement, or setting guardrails. That is `engineering-cost-review-desk`, which consumes this register filtered to each team.
- The subject is whether a commitment should be purchased. That is `commitment-portfolio-desk`; this desk supplies the netted usage changes that its baseline depends on.
- The subject is a cost anomaly needing a root cause rather than an opportunity needing an owner. That is `anomaly-detection-desk`.

## Required evidence

- Every opportunity from every lane with its scope at resource, workload, dataset, or application granularity, its current and proposed state, its sizing with the baseline the sizing was measured against, and the evidence behind it.
- The commitment recommendations with the usage baseline they were sized against, since they are the one item in the register whose sequencing constraint is contractual rather than practical.
- The cost basis and period for every figure, because opportunities arriving from different lanes routinely arrive on different bases and summing an amortized saving with a billed one is a silent error.
- The engineering capacity, roadmap, and change process the work competes with, including change freezes, release calendars, and the lead time a change of each type actually takes in this organization.
- Prior accepted and rejected opportunities with their reasons, and the period each was resolved in.
- The savings realization record: what was implemented, when, and the billing lines before and after, normalized for any volume change over the same period.
- The materiality threshold, so the register tracks what is worth tracking and says what it is excluding.
- Ownership structure mapping a resource, workload, or application to the team that can actually change it, which is frequently not the team the cost is allocated to.

## Workflow

**Outcome.** One deduplicated register with overlaps netted and the netting shown; prioritization on savings against effort, risk, reversibility, and blast radius; an owner and an engineering-terms ask per item; acceptance and rejection states with reasons preserved; a sequenced plan that respects capacity, change windows, and the optimize-before-commit constraint; realization tracked against the invoice with the estimate-to-actual gap measured; and a savings position that separates realized reduction from cost avoidance and from estimate.

**Grounding.** Every opportunity keeps the sizing and the evidence its originating lane produced, and is not re-derived here. Netting is performed against scope rather than against category, because two opportunities overlap when they touch the same resource or the same spend, not when they share a lever name. Realization is measured from the billing line the change was supposed to move, over a period after the change landed, normalized for volume, and it is the only figure permitted to carry the word realized.

**Constraints.** Overlap is resolved by stating which opportunity is applied first and what remains for the second, with both figures shown, since the resolution is a decision rather than an arithmetic identity: rightsizing an instance and then committing to the smaller one is a different total than committing first, and the order matters. Opportunities are ranked on the return per unit of engineering effort with risk, reversibility, and blast radius carried alongside, because the largest saving in a register is frequently the one nobody will schedule and the register's credibility depends on its top items actually getting done. Effort is stated in the units the implementing team plans in, with the change process and its real lead time included rather than the hands-on time alone. The ask is written in engineering terms naming the resource, the change, and the expected behavior, because an item phrased as a cost objective gets read as a request to explain the number rather than to act. Items with an externally fixed deadline, principally licence renewals and commitment expiries, sequence ahead of larger items with no date, since their availability expires. Rejections are recorded with the reason and the period, and a rejected item stays in the register rather than being deleted, because the same idle cluster is rediscovered every quarter and the useful record is why it was left alone the last three times. Realized savings and cost avoidance are reported as separate totals in every artifact, never combined into a headline.

The realization measurement follows a mandated order, recorded here with its reason so a later editor does not read it as scaffolding: a pre-change baseline cannot be reconstructed after the change, so it has to be captured before.

1. Record the specific billing line, its cost basis, and its value for a complete period before the change, together with the volume driver that will be used to normalize it.
2. Implement the change, with its date recorded.
3. Read the same billing line for a complete period after the change, once the period has closed and any corrections have landed.
4. Report the difference normalized for volume, as realized, and feed the gap against the estimate back into the originating lane's sizing.

**Parallel surface.** Individual opportunities, teams, and lanes are independent for the per-item work: enrichment with owner and effort, risk and reversibility assessment, scheduling against a team's calendar, and per-item realization measurement all fan out safely. The netting is explicitly not part of that surface and cannot be, because an overlap is invisible from inside either of the opportunities that share it. Deduplication, overlap netting, the ranked sequence, the capacity fit across teams, and every published total are single passes over the whole register after the fan-out returns. A per-team backlog that was never netted centrally reproduces the original defect at smaller scale and hides it better.

**Acceptance bar.** Every item carries scope, sizing with its baseline, savings type, effort, risk, reversibility, blast radius, owner, and state. Every overlap is named with both opportunity identifiers, the resolution order, and the net figure. Every published total states what it is net of, which portion is realized against which is estimated, and which portion is avoidance. Every rejected item carries a reason and a period. Realization figures cite the billing line and the closed period they came from.

## Outputs

A complete run delivers this set:

- `opportunity-register.md`: the deduplicated set with scope, lever, current and proposed state, sizing with its baseline and cost basis, savings type, effort, risk, reversibility, blast radius, owner, and state per item.
- `overlap-netting.md`: every overlapping pair or group with the opportunity identifiers, the shared scope, the resolution order, the gross figures, and the net that survives, so the reduction from gross to net is auditable rather than asserted.
- `prioritization.md`: the ranking with the return per unit of effort, the risk and reversibility carried alongside, the items whose deadline is externally fixed, and the reason the top of the list is the top of the list.
- `ownership-and-asks.md`: per item, the team that must act, the ask in engineering terms naming the resource and the change, the acceptance state, and the routing record for items whose owner could not be established.
- `sequencing-plan.md`: the schedule against engineering capacity, change windows and freezes, dependency between items, and the optimize-before-commit constraint with the commitment decisions that wait on specific usage changes.
- `rejection-register.md`: items rejected or deferred with the reason, the period, and the condition that would reopen them, kept so the next cycle inherits the decision rather than the discovery.
- `realization-tracking.md`: implemented items with the billing line, the pre-change baseline, the post-change measurement, the closed period each came from, the volume normalization applied, and the realized figure.
- `estimate-to-actual.md`: the gap between estimated and realized savings by lane and by lever, with the sizing correction it implies for the next cycle.
- `savings-position.md`: the current totals separated into realized, in flight, accepted but not started, and identified, with cost avoidance reported separately and the netting basis stated on every figure.
- `backlog-downstream-handoff.md`: what `engineering-cost-review-desk` and `chargeback-invoicing-desk` inherit, filtered to team and cost center.

Depth standard: an artifact is complete when an engineering manager could take an item into sprint planning without asking what it means, and a finance partner could rely on the savings position without asking what is in it. An item with no owner and no routing record, an overlap noted but not netted, a total with no netting basis, and a realized figure with no billing line are unfinished rather than draft.

When the billing lines needed for realization, the lane evidence behind an opportunity, or the ownership mapping exists and cannot be read, the run delivers `backlog-connector-diagnostic.md` naming each unreachable source and the items it leaves unsizable or unverifiable, in place of the tracking that source would have grounded. A realized figure is never carried forward from the estimate that preceded it.

Anti-fabrication guard: the defect this desk exists to catch is a register that has grown larger than the bill it is optimizing. It happens without anyone inventing anything: each lane sizes honestly, the totals are added, and a service costing a hundred thousand a month acquires a hundred and forty thousand of annualized savings across four lanes that all touch the same instances. The second version of the same defect is a realized column populated from the estimate column, which is what happens when a change ships and nobody goes back to the invoice, and it is worse because it is indistinguishable from success until a finance partner reconciles it. So no total is published from this desk without stating what it is net of, no figure enters the realized column without the billing line and the closed period that shows it, and cost avoidance is reported on its own line with its own label rather than blended into a headline that sounds larger. Owners, effort estimates, and implementation dates are taken from the teams that gave them and are recorded as unassigned where no team has agreed, because a backlog that assigns work by inference produces a plan the implementing teams have never seen. An honest register that is smaller than the target is a finding the organization can act on; a register that reaches the target by summing the same instance four times destroys the practice's mandate the first time someone checks, and takes every real opportunity on the list down with it.

## finops_packet fields to update

- `opportunities[]` consolidated across every lane, each with opportunity_id, lever, scope, current_state, proposed_state, estimated_savings with amount, period, baseline and confidence basis, and savings_type
- `opportunities[].overlaps_with` naming the specific opportunity identifiers that share scope, and `net_of_overlap` with the figure that survives the resolution order
- `opportunities[].implementation_effort` with who does it, `performance_risk` with the evidence behind the judgment, `blast_radius`, and `reversibility`
- `opportunities[].owner` and `state` moved through identified, accepted, scheduled, implemented, verified, rejected, or superseded, with `rejection_reason` preserved for every item not proceeding
- `opportunities[].realized_amount` and `realization_evidence` naming the billing line and the closed period that demonstrates it
- `commitments.purchase_recommendations[].assumed_baseline_usage` annotated with the netted usage changes this register expects to land and their scheduled dates
- `governance.approvals[]` where an accepted item requires an authority the matrix names
- `forecast.known_step_changes[]` where a scheduled optimization materially changes the run rate
- `source_facts[]` with locator and as-of for every sizing and realization figure, `assumptions[]`, `open_questions[]`
- `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: a savings total would be reported that sums overlapping opportunities, mixes cost avoidance into realized savings, or counts an estimate as a result. This is the defining halt of this desk. A backlog that claims more savings than the bill can lose is the fastest way for a practice to lose its mandate, because the first person to check is the person whose budget was cut on the strength of it.
- **Missing approval**: an item would be scheduled into a team's plan without that team accepting it, a savings target would be committed on behalf of an owner who has not agreed, or an item requiring a named authority would proceed without it.
- **Production or destructive**: the next action would implement a change rather than schedule it, including any deletion, resize, schedule change, entitlement reduction, or commitment purchase carried in the register. This desk sequences and tracks; the owning team and the named approver act.
- **Source conflict**: two lanes genuinely disagree on the sizing or the current state of the same scope, or the realization measurement and the originating estimate disagree by a margin that suggests one of them is measuring something else. Record both readings with locators and route the conflict rather than resolving toward the larger figure.
- **Connector unreachable**: the billing lines needed to measure realization, or the evidence behind a material opportunity, exists and cannot be read, so a realized figure would be asserted from an estimate.
- **Security or privacy**: an item's evidence carries customer identifiers, personal data, or restricted commercial terms, or the register would expose a workload's existence to an audience that should not see it.

An unassigned owner, an unestimated effort, an unscheduled item, and a lane that has not yet reported are soft gaps. Name them, label the assumption against the item, and continue with the item held in an explicit state rather than dropped. Netting overlaps before publishing a total is never deferred to meet a reporting deadline, and an item is never moved to realized to make a cycle look complete.

## Downstream handoffs

`engineering-cost-review-desk` is next in the default sequence and receives the register filtered to each team, with the ask already in engineering terms and the items that belong to the platform rather than to the team separated out. `commitment-portfolio-desk` receives the netted usage changes with their scheduled dates, since its baseline depends on which of these items will actually land inside the term it is sizing. `forecasting-variance-desk` receives accepted items as known step changes. `chargeback-invoicing-desk` receives realized savings by cost center, since a reduction that never reaches a team's statement is a reduction that team has no reason to repeat. `budget-planning-desk` receives the savings position as an input to the next cycle rather than as a commitment. Send implementation to the owning teams through the SDLC suite, packaged for the coding agent with the scope, the evidence, the expected saving, the reversibility, and the rollback attached; send estate changes to the Cloud Infrastructure suite and any reliability trade-off to the SRE Reliability suite.

## Quality bar

Good backlog work is trusted precisely because its number is smaller than the sum of its inputs, and it shows the subtraction. It nets overlaps in the open with both gross figures visible, so a reader can see the register being honest rather than being told it is. It ranks on what will actually get done, since a top item nobody schedules is worth less than a smaller one that ships this month. It writes the ask the way the implementing engineer would write it. It keeps its rejections, which is the difference between a backlog and a rediscovery loop. It measures realization against a closed billing period and reports the gap against the estimate without flinching, because a lane that over-estimates by a third is only fixable once somebody says so. And it never lets cost avoidance and realized savings share a line, because those two numbers get combined exactly once before a finance partner stops believing either of them.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
