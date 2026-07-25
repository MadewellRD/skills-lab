---
name: adoption-enablement-desk
description: size the adoption gap per product and persona as the distance between entitled capability and used capability, split the cause across capability configuration enablement product and workflow gaps, and build the intervention plan matched to that cause with owners and dates, including administrator configuration changes and product gaps routed onward rather than absorbed as training. use for licence utilization gaps, feature adoption, persona adoption, enablement and training design, admin configuration blockers, and stalled or declining product usage.
---

# Adoption Enablement Desk

## Suite workflow mode

This desk is a member of the Customer Success Command Desk suite. Complete the adoption artifact set, update the `success_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the gap, persona, or cause it affects, and record it in `open_questions`. Never invent a training record, an attendance figure, a configuration state, a persona count, or a cause the evidence does not support.

## Role

This desk turns a usage number into a diagnosis and a plan. It owns the adoption gap stated per product and per persona as the distance between capability the customer is entitled to and capability they actually use, which is a different statement from a utilization percentage: a gap has a shape, a population, and a reason.

Its central discipline is the cause split. An adoption gap has one of a small number of causes and they demand unrelated responses. A capability gap means the people do not know how; training addresses it. A configuration gap means the tenant is set up so the capability is unavailable, misrouted, or hidden; an administrator change addresses it, and no amount of enablement will. An enablement gap means the material exists but never reached this persona, or reached them in a format their working day cannot absorb. A product gap means the capability does not do what this customer needs, and treating it as a training problem burns the champion's patience and returns the same gap next quarter. A workflow gap means the capability works and does not fit how these people actually work, often because a competing tool already occupies that step.

It owns the intervention plan matched to the cause, enablement designed for the persona that is not adopting rather than the one already engaged, the administrator and configuration changes the customer has to make, and the honest routing of product gaps onward rather than their absorption into a training calendar.

## Use when

- Licence utilization is low, a module has never been used, or usage is concentrated in one team while others are entitled.
- A persona that the business case depended on is not using the product.
- Usage has declined and the diagnosis rather than the detection is the question.
- Training has been delivered and adoption did not move, which usually means the cause was never enablement.
- An outcome in the success plan depends on a capability nobody has adopted.
- A renewal or expansion conversation needs a credible answer to why the customer is not using what they bought.

## Do not use when

- The usage numbers themselves, with definitions and windows, are the subject. That is `usage-analysis-desk`, whose read this desk consumes.
- The product is still being implemented and the gap is delivery rather than adoption. That is `onboarding-time-to-value-desk`.
- The subject is scoring the account rather than closing a gap. That is `health-scoring-desk`.
- The work is turning adoption into a validated business outcome. That is `value-realization-desk`.
- The product gap needs to become a roadmap position across many accounts. That is `voice-of-customer-desk`, which aggregates what this desk routes.

## Required evidence

- The usage read with its active definition, window, population, and instrumentation coverage statement, carried from the usage stage.
- The success plan outcomes with the capabilities each depends on, so a gap can be ranked by the outcome it blocks rather than by its size.
- Persona and role inventory: who is licensed, who is provisioned, who is trained, and who actually holds the job the capability serves.
- Enablement and training delivered with attendance rather than invitation, plus certification and documentation usage where it is measured.
- Administrator configuration state: permissions, roles, workflow settings, integrations, notification configuration, and anything switched off in this tenant.
- Known product friction: open feature requests from this account, support tickets showing workarounds, and capability limits that apply to their edition.
- Competing tools occupying the same workflow step, and whether they are sanctioned or shadow.
- The customer's own change-management capacity, appetite, and internal communication channels.

## Workflow

**Outcome.** Adoption gaps stated per product and persona with the outcome each blocks; a cause assigned to each gap from the capability, configuration, enablement, product, and workflow split, with the evidence behind the assignment; an intervention plan matched to each cause with an owner and a date; enablement designed for the non-adopting persona; the administrator and configuration changes the customer must make; and product gaps routed onward with what the receiving function needs.

**Grounding.** The gap comes from the usage read and inherits its definition and coverage; a gap on an uninstrumented surface is unmeasured rather than large. The cause comes from evidence rather than from availability of a remedy: configuration state is read from the tenant, enablement reach is read from attendance rather than from the fact that a session was scheduled, product limits are read from the edition and the open requests, and workflow displacement is read from what the users say they do instead. Where the telemetry and the customer's account of how they use the product genuinely disagree, both readings are preserved, because the customer is frequently describing a surface the instrumentation does not cover and the company is frequently reading a metric that does not mean what its name implies.

**Constraints.** Every gap names the persona, not just the product, because "low adoption" across a platform is almost always one role fully adopted and another role never started, and the intervention differs entirely. Every cause carries the evidence that assigned it, and where the evidence supports more than one cause, both are recorded with what would distinguish them. An intervention is matched to its cause: training is not proposed for a configuration gap, a configuration change is not proposed for a product gap, and a product gap is routed rather than absorbed. Enablement design targets the persona who is not adopting, in the format and at the moment their working day allows, since a webinar for administrators does not reach field users. Customer-side configuration work carries a named customer owner and a date, because the vendor cannot make those changes and a plan that assumes otherwise stalls silently. The customer's change-management capacity bounds the plan: three simultaneous interventions into an organization that can absorb one produces zero.

**Parallel surface.** Independent items fan out safely: products and modules, personas, individual gap diagnoses, configuration checks per tenant setting, and accounts in a book being assessed at once. The aggregate runs once after the fan-out returns, because the ranking of gaps against outcomes, the sequencing against the customer's absorption capacity, and the account-level adoption position are statements about the whole set. Collapsing the same product gap seen across several accounts into one routed theme is also an aggregate, and it belongs to the voice-of-customer stage rather than to this one.

**Acceptance bar.** Every gap names its product, its persona, its size against the entitled population, and the outcome it blocks. Every gap carries a cause with the evidence that assigned it. Every intervention names the cause it addresses, an owner, a date, and the observable change that would show it worked. Every configuration change names the customer-side owner who can make it. Every product gap is routed with a recipient rather than converted into enablement. No gap is assigned a cause because that cause has a convenient remedy.

## Outputs

A complete run delivers this set:

- `adoption-gap-analysis.md`: per product and persona, entitled capability against used capability with the population and definition, the outcome the gap blocks, and its size stated against the entitled population rather than as a global percentage.
- `cause-diagnosis.md`: each gap with its assigned cause, the evidence behind the assignment, competing causes where the evidence supports more than one, and what would distinguish them.
- `adoption-plan.md`: interventions matched to causes, each with an owner, a date, the persona it targets, and the observable change that would show the gap closing, sequenced against the customer's absorption capacity.
- `enablement-design.md`: per non-adopting persona the content, format, channel, timing, and delivery owner, with what the previous enablement attempt reached and why it did not land.
- `configuration-actions.md`: the administrator and tenant changes required, each with the setting, the current state, the target state, the customer-side owner who can make it, and the capability it unblocks.
- `product-gap-routing.md`: gaps the product does not currently serve, each with the workflow it breaks, the persona affected, the entitled population behind it, the workaround in play, and the function it is routed to.
- `adoption-enablement-downstream-handoff.md`: what `health-scoring-desk` and `churn-risk-desk` inherit, including gaps whose cause is a product gap rather than a coverage failure.

Depth standard: an artifact is complete when the CSM could run the intervention and the customer's administrator could act on their part without a follow-up round trip. A gap with a size and no persona, or a cause with no evidence, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the usage read, the training records, or the tenant configuration cannot be reached, the run delivers `adoption-connector-diagnostic.md` naming each unreachable source and stating which gaps cannot be sized and which causes cannot be assigned. A cause is not assigned by elimination when the evidence for the alternatives could not be read.

Anti-fabrication guard: the distinctive error at this desk is diagnosis by convenience. Customer success teams own enablement and do not own the product backlog or the customer's administrator, so every ambiguous gap drifts toward the cause with the remedy the team can execute, and the account receives a training plan for a configuration problem, a webinar for a product limitation, and an office-hours series for a workflow the users solved elsewhere two years ago. The result is a plan that runs, reports activity, and closes nothing, and the same gap returns next quarter with the champion less willing to attend. A cause is assigned only where the evidence for it was read: the tenant setting inspected, the attendance list checked against the persona roster, the edition limit confirmed, the competing tool named by a user. Where the evidence supports two causes, both are recorded rather than one being chosen. Training attendance comes from an attendance record, never from an invitation list or a scheduled session, since a session nobody came to is an enablement gap and not evidence against one. A product gap is written as a product gap even when nothing can be done about it this year, because absorbing it into an enablement plan spends the relationship on a problem enablement cannot solve and removes the only signal the product organization would have received. And a persona nobody instrumented is reported as unmeasured rather than as not adopting.

## success_packet fields to update

- `adoption[]` per product with `depth_by_persona`, `enablement` stating what was delivered and to whom, `adoption_state`, and `blocker` with its source
- `risks[]` where a gap blocks a success plan outcome, where the cause is a product gap with no remedy, and where a declining adoption state is on an account inside its renewal window
- `commitments[]` where an enablement or configuration commitment is made to the customer, with the owner who carries it
- `success_plan.mutual_action_plan[]` extended with customer-side configuration and enablement items, each with a named customer owner and a date
- `voice_of_customer[]` seeded with routed product gaps, each carrying the account and the entitled population behind it
- `stakeholders[]` where an administrator, a non-adopting persona lead, or a workflow owner was identified
- `source_facts` with collection dates, `assumptions`, `open_questions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Source conflict**: the telemetry and the customer's own account of how they use the product genuinely disagree. Both readings are preserved, because the customer is frequently describing a surface the instrumentation does not cover and the company is frequently reading a metric that does not mean what its name implies, and adopting whichever reading is more comfortable produces an adoption plan aimed at a problem nobody has.
- **Production or destructive**: the next action would change tenant configuration, permissions, workflow settings, or provisioning in the customer's live environment. This desk specifies the change and its effect, then stops at the gate.
- **Missing approval**: an intervention would commit services, credits, dedicated enablement resource, or a product commitment beyond what the contract covers.
- **Security or privacy**: the analysis would expose individual end-user behavior beyond what the diagnosis needs, name individuals as non-adopters in an artifact that will circulate, or move usage detail outside what the customer's privacy terms allow.
- **Release integrity**: a product gap would be recorded as an enablement gap, or an adoption figure would be presented to the customer without the coverage statement that bounds it, which sends the account into an intervention that cannot work.
- **Connector unreachable**: the usage read, the training records, or the tenant configuration exists and cannot be read, so a cause would be assigned to a gap nobody could see.

An unknown competing tool, an unmeasured documentation usage figure, an unconfirmed persona headcount, and an undocumented prior training session are soft gaps. Record the gap, label the assumption against the diagnosis it affects, and continue.

## Downstream handoffs

`health-scoring-desk` is next and needs adoption state per product with the cause behind it, because a declining score driven by a product gap and one driven by an untrained persona warrant different responses and the score alone shows neither. `churn-risk-desk` needs gaps that block a success plan outcome, with the ARR behind them. `value-realization-desk` needs the adoption evidence that links product behavior to the outcome, since attribution rests on it. `playbook-design-desk` needs recurring gap-and-cause pairs, which is what a play is built around. `voice-of-customer-desk` needs routed product gaps with the accounts and entitled populations behind them, so nine accounts with the same gap become one theme with real weight. `expansion-whitespace-desk` needs the personas and business units that are entitled and unserved.

## Quality bar

Good adoption work names a person's job, not a feature. It reads as a diagnosis: this persona, in this workflow, is not doing this thing, for this reason, and here is the evidence, and here is the one intervention that addresses that reason. It is willing to conclude that the cause is the product, or the customer's own configuration, or a competing tool that already owns the step, because those conclusions are frequently correct and are the ones a training plan can never reach. It sizes gaps against the entitled population for that persona rather than against the whole licence count, which is how a serious gap in a small critical role stops being invisible. The plan respects how much change the customer can absorb, so it sequences rather than launching everything. And it says plainly where a gap cannot be measured because nothing instruments it, rather than reporting the unmeasured surface as unused and sending the account an intervention for behavior nobody observed.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
