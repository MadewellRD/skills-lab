---
name: cloud-decommissioning-desk
description: retire cloud resources stacks accounts and regions safely using an evidence-backed dependent inventory from flow and access and authentication logs, a notice window with named owners, a reversible quarantine step before deletion, data disposition against retention and legal holds, ordered teardown with the irreversible boundary marked, credential revocation and address and dns release in the order that prevents takeover, removal of the code and pipeline entries that would recreate it, and confirmation that the billing line actually stopped.
---

# Cloud Decommissioning Desk

## Suite workflow mode

This desk is part of the Cloud Infrastructure Command Desk suite. Complete the decommissioning artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, declared-versus-live source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent dependents, traffic evidence, retention obligations, hold status, approval records, owner names, or the confirmation that spend stopped.

## Role

Own the retirement of infrastructure and the proof that it was safe to retire. This desk assembles the dependent inventory from evidence rather than from belief, runs the notice window with named owners, executes the reversible quarantine that turns a silent break into an observable one while it is still cheap to undo, decides data disposition against retention and legal holds, sequences the teardown with the irreversible boundary marked, releases credentials, addresses, and names in the order that prevents them from being weaponized, removes the code and pipeline entries that would otherwise recreate the resource, and confirms from the invoice that the spend actually stopped.

Cloud deletion has a property that shapes this entire desk: it does not fail when someone still needs the resource. It succeeds immediately, and the failure arrives later, in another team's outage, with no undo. Every gate here exists because the delete itself will not warn anyone.

## Use when

- A resource, stack, account, subscription, project, or region is being retired, whether or not anything replaced it.
- The source estate is ready for retirement after a migration wave has passed its validation window.
- Orphaned or idle resources identified elsewhere need a safe path to removal rather than a bulk delete.
- A dependent inventory is needed that will survive challenge, because someone will ask how anyone knows nothing calls it.
- Data disposition has to be decided against retention schedules and legal holds before anything is destroyed.
- Credentials, addresses, DNS names, and certificates need releasing and the release order matters.
- Spend was supposed to stop and the invoice says otherwise.

## Do not use when

- Workloads are moving rather than ending, and the source is still authoritative: that is `cloud-migration-desk`, which hands this desk the source estate only after its validation window closes.
- Idle resources have been identified but nobody has established dependents yet: `cloud-cost-rightsizing-desk` and `tagging-inventory-desk` produce candidate lists, which are inputs to this desk rather than authorizations to delete.
- The resource is drifted rather than dead, and the real question is reconciliation: that is `drift-detection-reconciliation-desk`.
- The code layout and state boundary that must be edited to remove the resource cleanly: that is `infrastructure-as-code-desk`, whose boundaries this desk edits through the normal apply path.
- The approval matrix and the apply gate the teardown runs through: that is `provisioning-pipeline-desk`.
- Customer or partner communication for an externally visible retirement: cross-suite handoff to the SDLC suite for the sunset and communication artifacts.

## Required evidence

- Traffic and access evidence over a window long enough to include monthly, quarterly, and annual callers: flow logs, load balancer and access logs, DNS query logs, authentication logs, function invocation counts, and connection metrics, each with its retention window stated.
- Identity last-used evidence for roles, keys, and service accounts that touch the target, since a credential with recent use names a dependent that no network log will show.
- The dependency graph and coexistence state from `cloud-migration-desk` where retirement follows a migration.
- Retention schedule and legal hold status from the obligations source of record, not from a team's understanding of it.
- Backup and archive state for the data involved, including whether a restore has ever been exercised from that archive rather than merely configured.
- Code and pipeline references: the module, stack, state addresses, pipeline jobs, monitors, alerts, backup jobs, and scheduled tasks that reference the target.
- Address, DNS, and certificate holdings tied to the target, plus the current billing lines that the retirement is meant to end.

## Workflow

**Outcome.** A retirement package with an evidence-backed dependent inventory naming its observation window, a notice record with owners and dates, a quarantine plan with an observation period and a reversal path, a data disposition decision checked against holds, an ordered teardown with the irreversible boundary marked, a release plan for credentials and addresses in a safe order, the code and pipeline removals that prevent recreation, and a billing confirmation checked against a full period rather than a day.

**Grounding.** Read logs, metrics, and last-used data for what still touches the target, and read documentation and team statements as intent, keeping the two labeled separately per `references/suite-workflow-contract.md`. The asymmetry matters more here than anywhere else in this suite: evidence of use proves a dependent exists, while absence of use over a window proves only that nothing called it during that window. Thirty days of silence says nothing about a quarterly reconciliation job, and the observation window is stated next to every claim of no dependents so a reader can judge it themselves.

**Constraints.** Every dependent claim carries its evidence source and its window. Quarantine is mandatory rather than optional, because it is the only step that converts a missed dependent from an outage into a reversible complaint, and its observation period covers the longest plausible call interval rather than a convenient number of days. Legal and regulatory holds override every other consideration, including a business decision to delete, and hold status is read from the obligations source of record rather than assumed absent. Archive is only credited as a disposition when a retrieval has actually been performed from it, since an archive nobody has read is an assumption with a storage bill. Code removal is part of the teardown, not a follow-up: a stack entry left behind means the next apply recreates the resource, and the monitors and backup jobs left behind page someone about a thing that no longer exists. Address and name release order is a security control, not housekeeping: a public address released while a DNS record still points at it, or a DNS record left pointing at a deallocated endpoint, hands a working name to whoever claims that address next.

Teardown runs in this order, and the order is mandated because each step produces the evidence that makes the next one safe, step 5 is the point of no return, and the release steps after it are the ones that turn a retired resource into someone else's foothold if they run early:

1. Establish the dependent inventory from evidence, with the observation window stated, and confirm that a restore point exists for the data and that its restore path has been exercised rather than configured.
2. Announce to the named owners with the notice window, and record the acknowledgements and the objections.
3. Quarantine: remove access and traffic through a deny policy, a security group closure, scaling to zero, or a weight shift, leaving the resource and its data fully intact and reversible for the stated observation period.
4. Obtain the approval the classified blast radius requires, recorded against this specific target, after the quarantine period has passed without a dependent surfacing and before anything is deleted.
5. Delete or close, in dependency order, taking data-bearing resources only after their disposition is executed. This is the irreversible boundary.
6. Revoke the credentials, roles, and trust relationships that existed only for this target; remove DNS records before releasing the addresses and names they point at; and revoke or let lapse the certificates.
7. Remove the code, state entries, pipeline jobs, monitors, alerts, and backup schedules, so nothing recreates the resource and nobody is paged for it.
8. Confirm across a full billing period that the line stopped, and account for the residual charges that legitimately continue, including retained backups, archived objects, held addresses, and log storage.

**Parallel surface.** Independent retirement targets, resource types, accounts, and evidence sources are independent units and are parallel-safe; per-target dependent analysis, per-source log querying, per-resource code reference discovery, and connector preflight across the logs, inventory, billing export, and obligations source all fan out.

The aggregate steps are not parallel and run once after the fan-out returns: the combined dependent inventory across all evidence sources, the teardown ordering derived from dependencies between the targets themselves, the approval that covers the whole retirement, and the billing confirmation. The ordered teardown above is strictly sequential per target and is never parallelized across its own steps, since the entire point of the sequence is that each step's evidence gates the next.

**Acceptance bar.** A reviewer can state, for the target, what evidence establishes that nothing depends on it and over what window, what the quarantine period was and what happened during it, which hold was checked and against which source, where the irreversible boundary sits in the runbook, and which billing line proves the spend ended. Every dependent, hold, approval, and billing figure traces to a query or a record, or is written as unverified.

## Outputs

A complete run delivers this artifact set:

- `decommission-dependent-inventory.md`: every evidence source queried, the observation window for each, the dependents found with their evidence, the sources that returned nothing and the window that covers, and the callers that could exist outside the window.
- `decommission-notice-record.md`: the owners notified, the notice window, the acknowledgements, the objections raised, and the disposition of each objection.
- `decommission-quarantine-plan.md`: the reversible access removal mechanism, the observation period and what justifies its length, the signals watched during it, and the exact reversal procedure.
- `decommission-data-disposition.md`: per data set, the disposition across archive, destroy, and hold; the retention obligation and its source; the hold check result; the archive location with the date a retrieval was last exercised; and the destruction method.
- `decommission-teardown-runbook.md`: the ordered sequence with the irreversible boundary marked explicitly, the dependency ordering between targets, the decision authority at each gate, and the release order for credentials, DNS records, and addresses.
- `decommission-code-removal.md`: the modules, stack entries, state addresses, pipeline jobs, monitors, alerts, and backup schedules to remove, so nothing recreates the resource and nothing pages for it.
- `decommission-closure-record.md`: the billing lines expected to stop, the period checked, the confirmed reduction, and the residual charges that legitimately continue with the reason for each.

Depth standard per artifact: a dependent entry names the source, the query, and the window rather than asserting a conclusion. A disposition entry names the obligation and where it was read. A runbook entry names who authorizes the step and what reversal looks like before the boundary and after it. A closure record names the actual billing line, since a retirement confirmed by absence of complaint is not confirmed.

In `diagnostic` mode, when the logs, inventory, obligations source, or billing export exists and cannot be read, the run delivers `decommission-connector-diagnostic.md` naming what was attempted and the access needed. No teardown is planned past quarantine in that mode, because unreachable evidence and absent dependents are indistinguishable and only one of them is safe.

The dangerous artifact on this desk is the empty dependent list, and it is dangerous precisely because it is what everyone wants to see. An empty list produced by a query that ran over the wrong window, against a log that was not enabled, or in a region nobody enumerated, is indistinguishable in the document from a genuine one, and it is the sentence that authorizes an irreversible action. So an unqueried source is recorded as unqueried rather than as clean, a log that was not enabled during the window is recorded as no-evidence-available rather than as no-traffic, and the retention limit of every source is stated beside its result. Retention holds get the same treatment: "no hold found" is only written when the obligations source of record was actually read, and otherwise the entry is hold-status-unknown, which blocks destruction rather than permitting it. This desk is judged on what it refused to delete without evidence.

## infrastructure_packet fields to update

- `decommission[]`: `target`, `dependents_checked`, `data_disposition`, `retention_hold`, `teardown_state` moving through announced, drained, quarantined, deleted, and closed.
- `inventory.unmanaged_resources` and `cost.waste_findings` reduced as targets are retired, with the remainder carried forward.
- `network.ipam_plan` where a range returns to the register, marked reclaimable only after DNS and address release are both complete.
- `identity.privileged_roles` and `secrets_and_config.key_hierarchy` where credentials and keys are revoked, including the keys that must outlive the data they protect in archive.
- `iac.repo_layout` and `provisioning.pipeline` where code and jobs are removed.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: deleting a stateful resource, closing an account or subscription, releasing an address block, or destroying data needs a named human owner recorded against this specific target, and approval collected after exposure is not approval.
- Production or destructive: the next action would delete, close, release, or destroy anything, or would move past the quarantine step before its observation period has run.
- Security or privacy: continuing would release an address while a name still resolves to it, revoke a credential still in use by an unidentified consumer, or destroy data whose classification or residency obligation is not established.
- Source conflict: the logs, the inventory, the billing export, and the owner statements genuinely disagree about whether the target is still in use, and choosing the convenient one would authorize an irreversible action on a resource something still calls.
- Release integrity: a retirement would be declared complete without the billing confirmation, or an archive would be declared a valid disposition without a retrieval having been performed from it.
- Connector unreachable: the traffic logs, access logs, identity last-used data, obligations source, or billing export exists and cannot be read. This class is decisive here: an unreachable log and a log showing no traffic produce the same empty result and support opposite decisions.

An incomplete historical usage record, a missing original owner, or an undocumented reason the resource was created is a soft gap: proceed with it named. Retention holds, data classification obligations, the quarantine step, and the approval gate are not soft gaps and are never compressed to finish a teardown on a schedule.

## Downstream handoffs

The orchestrator receives the closure record for workflow close. `cloud-migration-desk` receives the target back when a dependent surfaces during quarantine and a migration wave has to run before teardown can advance. `tagging-inventory-desk` and `cloud-cost-rightsizing-desk` need the confirmed removals so their inventories and waste lists stop carrying resources that no longer exist. `cloud-network-architecture-desk` receives released ranges for the register, marked reclaimable rather than free until the release is confirmed complete. `cloud-security-posture-desk` receives the revoked credentials and closed exposure paths.

## Quality bar

A retirement somebody can audit a year later: the evidence is named, the windows are stated, the quarantine actually happened, the holds were checked against a real source, the irreversible boundary was marked before anyone crossed it, and the closure record points at an invoice rather than at silence. The best outcome this desk produces is often the one where quarantine surfaced a dependent and the deletion did not happen.
