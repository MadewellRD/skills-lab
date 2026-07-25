---
name: drift-detection-reconciliation-desk
description: detect and reconcile cloud infrastructure drift by comparing declared state in code against live provider state on a defined cadence, score the drift inventory by consequence rather than count, attribute each change to its actual origin from audit and activity log evidence, suppress provider-side diff noise deliberately, decide reconciliation disposition across codify and revert and adopt and accept, import unmanaged resources safely, and change the guardrail that stops the drift recurring.
---

# Drift Detection Reconciliation Desk

## Suite workflow mode

This desk is part of the Cloud Infrastructure Command Desk suite. Complete the drift artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, declared-versus-live source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent the principal who made a change, a change timestamp, a resource address, an attribute value, or a reconciliation approval.

## Role

Own the gap between what the code says and what the account contains, and the decision about what to do with each item in it. This desk defines the comparison method and its cadence, produces the drift inventory scored by consequence, attributes each change to a principal from audit evidence, assigns a disposition per item, runs the import path for resources that should be under code and are not, and identifies the guardrail or process change that stops the same drift from returning next month.

Three different objects get called drift and they need different work. A managed resource whose live attributes no longer match its declaration is drift. A resource that exists in the account with no declaration at all is unmanaged, and importing it is a different operation with different risk. A declaration whose resource no longer exists is an orphaned address, and the next apply will recreate it, which is sometimes exactly right and sometimes an outage. Keeping these separate is most of the value this desk produces.

## Use when

- Nothing matches the diagram anymore and the first question is what actually changed and who changed it.
- Detection needs designing: the comparison method, its cadence, its coverage, and what it structurally cannot see.
- The drift report is full of noise nobody reads, so real drift is invisible inside perpetual diffs.
- Each drift item needs a disposition and an owner: codify the change, revert it, adopt the resource, or accept it with a reason and an expiry.
- Unmanaged resources need importing into code safely, without the import itself rewriting production.
- The same drift keeps returning in the same place, which is a finding about the sanctioned path rather than about the resource.
- A change is about to be applied and its target may be in a drifted state, so the plan will do something nobody expects.

## Do not use when

- The resource has no code because nothing was ever codified for it and the question is coverage and ownership rather than reconciliation: start at `tagging-inventory-desk`, which supplies this desk's unmanaged candidate list.
- State boundaries, module structure, or backend configuration are the subject: that is `infrastructure-as-code-desk`, which owns the layout this desk imports into.
- The gate that should have prevented the out-of-band change, including the approval matrix and the sanctioned manual change path: that is `provisioning-pipeline-desk`. This desk reports the recurrence; that desk changes the path.
- A misconfiguration is a security finding needing benchmark mapping and exposure analysis: that is `cloud-security-posture-desk`. Drift and posture overlap on the same resource and answer different questions.
- The divergence is between two estates during a migration rather than between code and one estate: that is `cloud-migration-desk`.
- Production incident command when drift caused an outage: cross-suite handoff to the SRE suite.

## Required evidence

- The IaC code and the state objects, giving the declared resource address set and every declared attribute.
- The live provider inventory or configuration recorder output, including its change history where the recorder retains one.
- Audit and activity logs covering the drift window, which is the only source that can name a principal, and its retention period, because a change older than retention is unattributable and that is a fact rather than a gap to fill.
- Provider-side drift detection output where the platform offers it, with its known coverage limits.
- The sanctioned manual change path definition from `provisioning-pipeline-desk`, which is what separates authorized out-of-band work from unexplained change.
- Existing suppression configuration: ignored attributes, lifecycle exclusions, and the reason each was added, if a reason was ever recorded.
- Change records and ticket history for the same window, as intent evidence that stands beside the audit log rather than replacing it.

## Workflow

**Outcome.** A drift inventory where every item states the declared value, the live value, the resource address, the consequence class, the attributing principal and time from audit evidence or an explicit unattributable marker, a disposition, and an owner; plus the noise suppression decisions with their reasons, the import plan for unmanaged resources, and the guardrail change that addresses recurrence rather than the instance.

**Grounding.** Read code and state for declared and the provider inventory for live, keep them labeled separately per `references/suite-workflow-contract.md`, and preserve both values rather than resolving one into the other. Attribution comes only from the audit log; a naming convention, a team's likely involvement, or a ticket that describes similar work is intent evidence and never becomes an attribution. Note what the comparison structurally cannot see: a plan-based comparison sees only resources in state, so it is blind to the entire unmanaged set by construction, and a recorder-based comparison sees resource types the recorder supports and nothing else.

**Constraints.** Drift is scored by consequence, not by count: a security group rule opened by hand, an encryption setting turned off, a retention policy shortened, or a public access block removed outrank a hundred description and timestamp differences regardless of how the report sorts. Noise is treated as a design problem: provider-added defaults, computed attributes, autoscaling desired counts, and tags written by other automation produce perpetual diffs that train people to close the report, so each suppression is a recorded decision with a reason and an owner rather than a silencer, and a suppression on a security-relevant attribute is itself a finding. Reverting drift is a live change and runs through the apply gate in `provisioning-pipeline-desk` rather than being done by hand, because a hand-revert is one more out-of-band change. Accepting drift carries a reason and an expiry, or it is an unmanaged acceptance rather than a decision. Repeat drift in the same place is reported as a process finding with its frequency, since the third time an engineer edits the same setting by hand, the sanctioned path is the defect.

Importing an unmanaged resource into code runs in this order, and the order is mandated because reversing any two steps means the next apply rewrites a live resource to match code that was never made to match reality:

1. Read the live resource in full, including the attributes the provider set by default and the ones the console does not display.
2. Write the code to describe the resource exactly as it exists, rather than as the module's defaults would create it.
3. Import the address into state.
4. Generate a plan whose only acceptable result is no changes. A plan showing a replacement at this step means the code and the resource disagree, and applying it destroys the resource being adopted.

**Parallel surface.** Accounts, regions, stacks, state files, resource types, and individual drift items are independent units and are parallel-safe; per-item comparison, per-item audit lookup and attribution, per-resource import preparation, and connector preflight across the state backend, inventory, and audit log all fan out.

The aggregate work runs once after the fan-out returns: the consequence ranking across the whole inventory, the recurrence analysis that only appears when the same address shows up across multiple detection cycles, the systemic finding about the sanctioned path, and the guardrail change set. Recurrence is invisible per item by definition, since a single detection run cannot distinguish a first occurrence from a fourth.

**Acceptance bar.** An engineer can take any drift item and state the declared value, the live value, who changed it and when or that it is unattributable and why, what it breaks if reverted, and who decided its disposition. Every attribution traces to an audit event, and every value traces to code or inventory output.

## Outputs

A complete run delivers this artifact set:

- `drift-detection-design.md`: the comparison method, its cadence, its coverage and its structural blind spots, the noise suppression decisions with reasons and owners, and how detection results reach a person who can act.
- `drift-inventory.md`: every item with resource address, declared value, live value, consequence class, attributing principal and timestamp or an unattributable marker with the reason, and the stack it belongs to.
- `drift-attribution.md`: the audit evidence per item, the split between human principals, automation identities, and provider-initiated changes, and the changes that fall outside audit retention.
- `drift-reconciliation-plan.md`: the disposition per item across codify, revert, adopt, and accept, with the owner, the change class each disposition creates, and the ordering where one item's fix depends on another.
- `drift-import-plan.md`: the unmanaged resources to bring under code, the target state boundary for each, the module that will describe it, and the no-change plan requirement that gates the adoption.
- `drift-recurrence-findings.md`: the addresses that have drifted repeatedly, the frequency, the principal pattern, and the process or guardrail change that addresses the cause rather than the instance.
- `drift-downstream-handoff.md`: the guardrail changes `provisioning-pipeline-desk` and `cloud-security-posture-desk` inherit, and the resources whose state must be settled before `cloud-migration-desk` or `cloud-decommissioning-desk` touches them.

Depth standard per artifact: an inventory entry gives both values and the address, not the observation that a resource differs. A disposition entry states what reverting would break, since revert is the disposition most often chosen without asking. An import entry names the target boundary and the module. A recurrence entry gives the count and the window.

In `diagnostic` mode, when the state backend, inventory, or audit log exists and cannot be read, the run delivers `drift-connector-diagnostic.md` naming what was attempted and the access needed. Drift is not inferred from the code alone in that mode, because code compared against nothing produces zero drift and a false sense of order.

The fabrication hazard on this desk is attribution, and it is different in kind from the others in this suite. Naming who changed something is an accusation. The evidence chain runs from an audit event to a principal to a time, and nothing else substitutes: not a naming convention, not the team that owns the account, not the engineer who opened a similar ticket that week, and not the automation identity that merely had permission. An item whose audit evidence is missing or outside retention is recorded as unattributable with the reason, and unattributable is a complete and respectable answer that also happens to be a finding about log retention. A drift item with a confidently wrong principal attached does more damage than an unreconciled one, because it ends the investigation and starts an argument.

## infrastructure_packet fields to update

- `drift.detection_cadence`, `drift.drifted_resources`, `drift.out_of_band_change_source`, `drift.reconciliation_policy`.
- `inventory.unmanaged_resources` reduced by whatever the import plan adopts, with the remainder carried forward.
- `iac.coverage` where adoption changes the codified share.
- `organization.guardrail_policies` where a recurrence finding produces a new control or an enforcement mode change.
- `posture[].state` where reverting or codifying a drift item closes or reopens a finding.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: reverting drift on a production resource, accepting a security-relevant drift item, or adopting an unmanaged production resource into a state boundary needs a named human owner who has not given it.
- Production or destructive: the next action would apply a revert, import into a live state object, remove an address from state, or run an apply against a stack whose plan currently shows a replacement. An import that produces a replacement plan is the specific case that destroys the resource it was meant to adopt.
- Security or privacy: drift removed an encryption, logging, public-access, or network control and continuing would leave that state asserted rather than evidenced, or the audit evidence itself carries credential material.
- Source conflict: the state object, the live inventory, and the audit log genuinely disagree about the current value or about whether a change occurred, and choosing one silently would attribute a change to the wrong principal or revert a value that was never set.
- Release integrity: a reconciliation would be declared complete, or an import declared clean, without the no-change plan evidence behind it.
- Connector unreachable: the state backend, provider inventory, or audit log exists and cannot be read. An empty drift result and an unreachable comparison source look identical in a report and mean opposite things, so state which happened.

An undocumented historical suppression, a missing ticket for an attributed change, or an unmeasured recurrence rate is a soft gap: proceed with it named. Security-relevant drift is never accepted silently to keep the workflow moving, and an item outside audit retention is recorded as unattributable rather than assigned.

## Downstream handoffs

`provisioning-pipeline-desk` needs the recurrence findings, because repeat drift in one place is a verdict on the sanctioned path rather than on the engineer who took a shortcut. `cloud-security-posture-desk` needs the drift items that reopened findings, with both values preserved. `infrastructure-as-code-desk` receives the import targets with their intended state boundary. `cloud-migration-desk` and `cloud-decommissioning-desk` need any resource in their path that is currently drifted, since planning a cutover or a teardown against a declaration that does not match the live resource plans the wrong operation.

## Quality bar

A drift report people read, because the noise was designed out rather than tolerated and the top of the list is genuinely the top. Attribution that is either evidenced or honestly absent. Dispositions with owners and, where they are acceptances, with expiry dates. And at least one finding that is about the path rather than the resource, because an estate that drifts in the same place every month has a process defect wearing a technical costume.
