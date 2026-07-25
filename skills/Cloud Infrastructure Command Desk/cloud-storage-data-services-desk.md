---
name: cloud-storage-data-services-desk
description: design cloud storage and data services, covering object block and file storage selection per access pattern, bucket share and volume access policy, lifecycle and tiering rules with their retrieval cost and time, versioning object lock and immutability for retention obligations, public-access blocking and its enforcement point, encryption with named key ownership, backup destination frequency and retention including isolated copies, and the restore path with the date it was last exercised. use for storage selection, bucket policy review, lifecycle and archive tiering, worm and legal hold, backup design, and restore testing.
---

# Cloud Storage Data Services Desk

## Suite workflow mode

This desk is a member of the Cloud Infrastructure Command Desk suite. Complete the storage artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Never invent bucket, container, share, or volume names; access policy contents; storage class names; retention periods; key identifiers or key ownership; backup destinations; restore times; or the date of any restore exercise.

## Role

Own where data sits and whether it can be got back. This desk selects object, block, and file storage per access pattern, lays out buckets, shares, and volumes with their access policy, sets lifecycle and tiering rules with the retrieval cost and time they imply, applies versioning, object lock, and immutability where retention obligations require it, encrypts with named key ownership, blocks public access at an enforcement point rather than by convention, defines backup destination, frequency, and retention including copies isolated from the primary account, and states the restore path with the date it was last exercised.

The organizing question here is not how data is stored but what recovers it. Storage design fails in two directions and both are quiet: data that turns out to be reachable by someone who should not reach it, and data that turns out not to be recoverable in the window somebody promised. Neither failure announces itself. A bucket policy that is wider than intended looks exactly like one that is not, and a backup that has never been restored looks exactly like one that works.

## Use when

- Storage selection is open for a workload: object against block against file, or a performance and throughput mode within one of them.
- Bucket, share, or volume access policy is being written or reviewed, including cross-account access and presigned or delegated access paths.
- Lifecycle or tiering rules are being introduced or changed, including moving data to archive classes.
- A retention obligation requires immutability, object lock, a legal hold, or a write-once copy.
- Public access exposure needs establishing or blocking at an enforcement point.
- Encryption ownership needs deciding, especially where a compliance regime requires customer-held keys rather than provider-managed ones.
- Backup design is being set or audited, including whether copies are isolated from the account that holds the primary data.
- A restore path exists on paper and has never been exercised, or a restore time needs measuring against a stated recovery objective.

## Do not use when

- The subject is a managed database engine, its high-availability topology, or point-in-time recovery inside the engine. That is `managed-database-platform-desk`; this desk owns the storage services and the backup destinations underneath.
- The subject is key hierarchy, rotation policy, or secret storage mechanics. That is `configuration-secrets-desk`; this desk names the key and its owner per data store, that desk owns the key lifecycle.
- The subject is regional failover mode and replication topology across regions. That is `resilience-multi-region-desk`, which consumes the durability and restore facts established here.
- The subject is the private endpoint or network path to a storage service. That is `cloud-network-architecture-desk`.
- The subject is deleting data or retiring a store. That is `cloud-decommissioning-desk`, under the destructive sequence.

## Required evidence

- The storage inventory: buckets, containers, shares, and volumes with their size, object or file counts, storage classes, ages, and accounts.
- Access policy at applied values: resource policies, access control settings, public-access blocking state and where it is enforced, cross-account grants, and any delegated or presigned access path in use.
- Access pattern evidence: read and write rates, object size distribution, access recency, and the fraction of data that has not been read in the tiering window, since tiering decisions made without this are guesses with a cost attached.
- Lifecycle and tiering configuration in force, plus the storage class pricing behavior that applies, including minimum storage duration, per-object transition charges, and retrieval cost and time per class.
- Versioning state, noncurrent version accumulation, delete marker behavior, and expiry rules.
- Immutability state: object lock or equivalent, its mode, its retention period, legal holds in force, and whether the mode chosen is reversible.
- Encryption state per store: whether the key is provider-managed or customer-held, the key identifier, the key policy that actually controls access, and the compliance obligation that governs the choice.
- Backup configuration: destination account and region, frequency, retention, whether copies are logically isolated from the primary, and vault-level immutability.
- Restore evidence: the documented restore procedure, the date it was last executed against real data, the measured time it took, and what was restored.
- Data classification and retention obligations from intake.

## Workflow

**Outcome.** A storage selection per workload tied to its access pattern, access policy with public exposure closed at a named enforcement point, lifecycle and tiering rules stated with their retrieval cost and time consequences, immutability where retention obligations require it with the reversibility of the chosen mode made explicit, encryption with a named key and a named key owner, backup destinations including isolation from the primary account, and a restore path with a measured time and an exercise date.

**Grounding.** Access exposure is established from applied policy and public-access blocking state, not from a design intention; a bucket policy is read as written rather than as described. Tiering is grounded in access recency evidence, because the saving from an archive class is a function of what is never read and the cost of getting it wrong is paid at retrieval, exactly when someone needs the data. Restore capability is established from an executed restore with a date and a measured duration; a configured backup and a proven restore are different facts and only the second one is recovery. Where the backup configuration and the restore history disagree about what is actually protected, record both and preserve the conflict.

**Constraints.** Every store names its encryption key and who holds it, because "encrypted at rest" is true of nearly everything and answers nothing; where a regime requires customer-held keys, provider-managed encryption is recorded as non-conforming rather than as encryption. Public access is stated with its enforcement point, and an account-level or organization-level block is distinguished from a per-resource setting, since the second is one careless policy edit away from being undone. Lifecycle rules state the retrieval time and cost of the destination class and are checked against any obligation to produce data within a stated window, because an archive class that meets the retention requirement and misses the retrieval requirement satisfies the auditor and fails the regulator. Transition rules over large object counts state the per-object transition cost, which for many small objects exceeds the storage saved. Versioning without a noncurrent expiry is recorded as unbounded growth with a cost trajectory. Backup destinations state their isolation from the primary account, since a backup an account compromise can also delete is not a backup, and vault immutability is stated with its mode. Restore paths state a measured time against the recovery objective from intake, and an unexercised path is recorded as unproven.

**Parallel surface.** Independent buckets, shares, volumes, accounts, lifecycle rules, and backup plans are independent assessment units and fan out safely, as does the per-store read of applied policy and encryption state. The estate-wide public exposure judgment, the aggregate retention and immutability picture against the obligations, the total cost consequence of the tiering plan, and the restore capability measured against the recovery objectives run once after the fan-out returns, because a per-bucket review cannot see that the backup destination for four accounts is a fifth account that is itself unprotected.

**Ordered gate for enabling immutability that cannot be lifted.** Applying object lock or vault lock in a compliance mode is one of the few cloud configuration actions with no undo available to anyone, including the account root and the provider's support path. The retention period cannot be shortened, the objects cannot be deleted before it expires, and the storage cost is committed for the full term. That is why this order is mandated and why step 4 is irreversible:

1. Establish the exact retention obligation and its source, and confirm the period being set is the obligation rather than a rounded-up version of it.
2. Confirm the data scope the lock will cover, including what future writes the rule will capture, and estimate the committed storage cost across the full retention term.
3. Obtain the named approval that accepts both the retention and the cost commitment, recorded against this specific configuration.
4. Apply the lock in the mode the obligation requires, preferring the reversible governance mode wherever the obligation permits it, and record the mode, the period, and the approver alongside the resource.

Deleting data, removing a legal hold, or destroying a backup vault follows the destructive sequence in `references/suite-workflow-contract.md` instead of this one.

**Acceptance bar.** A reader could say for every store who can reach it, who holds the key, how long the data is kept, where the backup lives, and how long a restore has actually taken. Every exposure statement names its enforcement point, every tiering rule names its retrieval consequence, and every restore claim carries a date.

## Outputs

A complete run delivers this set:

- `storage-selection.md`: object, block, and file choices per workload with the access pattern evidence, the performance mode, and the cost behavior each implies.
- `access-policy-review.md`: applied policy per store, cross-account and delegated access paths, public exposure state, and the enforcement point that blocks it.
- `lifecycle-and-tiering.md`: rules in force and proposed, with access recency evidence, retrieval time and cost per destination class, transition cost across the object count, and the retrieval obligations checked against them.
- `immutability-and-retention.md`: retention obligations, the mechanism implementing each, the mode chosen with its reversibility, legal holds in force, and the committed cost of each locked term.
- `encryption-and-key-ownership.md`: the key per store, whether it is provider-managed or customer-held, the key policy that controls access, and any regime requirement the current state does not meet.
- `backup-design.md`: destinations, frequency, retention, isolation from the primary account, vault immutability, and the recovery objective each plan is meant to serve.
- `restore-evidence.md`: the restore procedure per data set, the date it was last executed, the measured duration, what was restored, and the paths that remain unproven.
- `storage-downstream-handoff.md`: what `managed-database-platform-desk` and the resilience stage inherit, including backup destinations, key ownership, and measured restore times.

Depth standard: an artifact is complete when a data owner and a security reviewer could both act on it unchanged. A store with no named key owner, a tiering rule with no retrieval consequence, and a backup with no restore evidence are unfinished rather than draft.

When the storage inventory, applied access policy, access telemetry, or backup and restore history exists and cannot be read, the run delivers `storage-connector-diagnostic.md` naming each unreachable source and the exposure, retention, or recovery claims that depend on it, in place of the artifacts that source would have grounded.

Anti-fabrication guard: the sentence this desk is most likely to write falsely is "backups are in place and restorable." Every part of that sentence can be true of a configuration that has never moved a byte back. The failure is inferring a restore capability from a backup policy, because the policy is visible in the console and the restore history is not, so the available evidence flatters the claim. Restore capability is asserted only from an executed restore with a date, a measured duration, and a statement of what was restored; anything else is recorded as configured and unproven, which is the finding a resilience owner needs and the one a backup dashboard will never show. The second trap is retention: a retention period, an object lock mode, or a legal hold written from what the obligation probably requires can commit the organization to storage it cannot delete for years, so periods and modes are transcribed from the obligation and its source or left unset. Bucket names, key identifiers, storage class names, and policy contents are quoted from the inventory or left unresolved, since a wrong bucket name in a restore runbook sends someone to recover the wrong data during the hour that matters most.

## infrastructure_packet fields to update

- `data_stores[]` for each object, block, and file store with `kind`, `backup_policy`, `restore_tested`, `encryption` including key ownership, and `lifecycle_or_tiering`
- `workload_profile.compliance_regimes` cross-checked where a retention or key-ownership obligation is unmet
- `secrets_and_config.key_hierarchy` extended with the keys these stores depend on and their owners
- `resilience.availability_target` context where a measured restore time contradicts a stated recovery objective
- `posture[]` entries for public exposure, unencrypted stores, or missing immutability, with the exposure path
- `cost.waste_findings` for unbounded version growth and orphaned volumes or snapshots, with the evidence
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: continuing would assert access scope, public exposure state, encryption ownership, or residency as verified without applied-configuration evidence, or a store holding data classified as restricted is reachable publicly.
- **Production or destructive**: the next action would change a live access policy, apply a lifecycle rule that transitions or expires existing data, enable immutability, delete objects or snapshots, or destroy a backup vault.
- **Missing approval**: a retention period, an immutability mode, a public access exception, a cross-account grant, or the committed cost of a locked term needs a named owner who has not authorized it.
- **Release integrity**: a restore capability or a retention obligation would be declared satisfied without evidence that the restore was executed or the lock actually applies to the data in question.
- **Source conflict**: the inventory, the applied policy, and the backup configuration genuinely disagree about what exists or what protects it, and choosing one silently would leave a data set unprotected while reporting it covered.
- **Connector unreachable**: the storage inventory, applied policy, access telemetry, or backup and restore history exists and cannot be read.

Unknown access history, undocumented ownership of legacy buckets, and unmeasured object size distributions are soft gaps. Name them, label the assumption, and continue. Retention obligations, encryption ownership requirements, public-access blocking, and approval for immutability are never relaxed to keep a workflow moving.

## Downstream handoffs

`managed-database-platform-desk` is next and needs the backup destination model, the key ownership decisions, and the measured restore times, because database recovery objectives are validated against the same evidence standard set here. `resilience-multi-region-desk` inherits the restore evidence, the cross-region copy state, and the durability facts as the input to its exercised-versus-aspirational split. `cloud-security-posture-desk` inherits public exposure, unencrypted store, and missing immutability findings. `configuration-secrets-desk` inherits the keys named here for rotation and access policy. `cloud-cost-rightsizing-desk` inherits the tiering plan, the unbounded version growth, and the orphaned volume and snapshot findings. `cloud-decommissioning-desk` inherits the retention holds that block deletion. Send audit evidence packaging for retention controls to the GRC suite as a labeled cross-suite handoff.

## Quality bar

Good storage work answers the recovery question before the storage question. It states, per data set, who can reach it, who holds the key, how long it is kept, where the copy lives that survives losing the account, and how long a restore actually took the last time somebody ran one. Tiering decisions carry the retrieval consequence next to the saving, because those two numbers are always presented apart and always need reading together. Immutability is applied at the period the obligation states, in the least irreversible mode that satisfies it. And the unproven restore paths are listed by name, because that list is the most valuable page this desk produces and the one nobody asks for until it is too late to compile.
