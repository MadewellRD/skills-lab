---
name: backup-restore-desk
description: check backup coverage against the data inventory, record mechanism schedule retention and immutability with their sources, write the restore procedure and its measured time from a dated drill, verify integrity and deletion resistance including ransomware and accidental deletion, and name every dataset that has never had a restore proven. use for backup coverage, retention and immutability review, restore drills, point-in-time recovery, and data loss risk assessment.
---

# Backup Restore Desk

## Suite workflow mode

This desk is part of the SRE Reliability Command Desk suite. Complete the backup and restore artifact set, update the `reliability_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent backup schedules, retention periods, restore times, drill dates, or a restore that has not been performed.

## Role

Own the recoverability of data, which is a different property from the existence of backups. This desk establishes what data exists, which of it is backed up and by what mechanism, on what schedule, for how long, and whether the copies can be deleted by whoever or whatever deleted the original. It then establishes the only thing that makes any of that meaningful: a restore performed against a clock, on a date, by someone following the written procedure.

Backup coverage is measured against the data inventory rather than against the backup system's job list, because the job list can only tell you about datasets someone remembered to configure. The datasets that end an organization are the ones nobody registered: an object store holding uploaded documents, a search index treated as derived that turned out to be the only copy of a field, a self-managed database on ephemeral storage, infrastructure state, and the configuration and secret material without which the rest cannot be brought back.

## Use when

- Backup coverage needs establishing against what data actually exists rather than against what is already configured.
- Retention, immutability, or deletion resistance needs review, including against ransomware and accidental or malicious deletion.
- A restore procedure needs writing, or the existing one needs a measured time from an actual drill.
- An RPO needs grounding in backup recency and restore duration rather than in the schedule that was intended.
- A dataset is being introduced, migrated, or moved to a new store, and its recoverability is unestablished.
- A compliance obligation, a customer commitment, or an audit requires backup and restore evidence with dates.

## Do not use when

- The question is regional failover, evacuation, or the recovery order across a whole environment: that is `disaster-recovery-desk`, which consumes this desk's measured restore times.
- The question is replication for availability rather than for recoverability: replication is a dependency and topology concern for `dependency-failure-analysis-desk` and the recovery stage. A replica propagates a deletion; it is not a backup.
- The question is data classification, lawful retention limits, or deletion obligations: cross-suite handoff to the Privacy Data Protection suite, whose retention rules bound what this desk may keep.
- The question is a live data-loss event in progress: that is `incident-command-desk`, which executes the restore procedure this desk wrote.
- The question is archive and lifecycle cost: cross-suite handoff to the FinOps suite.

## Required evidence

- The data inventory with classification, ownership, and per-dataset RPO from upstream stages or from the data catalog, plus a reconciliation against what storage actually exists in the accounts and clusters.
- Backup configuration read from source: jobs, snapshot policies, log shipping and point-in-time recovery settings, export pipelines, and the datasets each one covers.
- Backup job history including failures, silent partial failures, and the last successful run per dataset with its timestamp.
- Retention configuration and lifecycle rules, including transitions to colder storage and the retrieval time each tier imposes.
- Immutability posture: object lock or equivalent, the account or tenant boundary the copies sit in, who holds delete permission, whether deletion requires additional authentication, and whether an offline or logically separated copy exists.
- Encryption and key management for the copies, including where the key lives and whether it is available in a scenario where the primary environment is unavailable.
- Restore tooling, the target environments a restore can land in, and the permissions the procedure requires.
- The history of restore attempts, drills, and real recoveries with dates, measured durations, and what failed.

## Workflow

**Outcome.** Coverage per dataset against the inventory including the explicit uncovered set, mechanism, schedule, retention, and immutability with the source of each value, a restore procedure with per-stage timings from a dated drill, integrity and deletion-resistance findings, and an unambiguous list of datasets whose restorability has never been demonstrated.

**Grounding.** Backup configuration and job history state what runs; the data inventory and the storage that actually exists state what should be covered; the drill record states what has been restored. A backup document without a corresponding job is recorded as intent, and a job whose last success is old is recorded with that date, per `references/suite-workflow-contract.md`.

**Constraints.** Reconcile coverage in the direction that finds gaps: start from data that exists and look for a backup, rather than starting from backup jobs and confirming they run. Include the categories habitually missed: object storage, message queues holding undelivered work, search and analytics indexes, caches that have quietly become authoritative, infrastructure state files, configuration and feature flag stores, secret material, certificate and key material, and self-managed data stores that were never onboarded.

Distinguish mechanisms by what they actually protect against. A replica protects against host and zone loss and faithfully replicates a destructive statement or a logical corruption within seconds. A snapshot protects against deletion from the point it was taken. Log shipping with point-in-time recovery protects against a mistake whose timestamp is known. State the failure class each mechanism covers, and state the ones it does not, since a dataset with three replicas and no snapshot has no protection against the failure mode most likely to destroy it.

Assess deletion resistance from the perspective of a compromised credential rather than a disk failure. If the identity that can delete the primary can also delete the copies, the backup is a convenience rather than a control; if the copies live in the same account, tenant, or trust boundary, the boundary does not exist. Record whether immutability is enforced by the storage layer, how long the lock holds, who can shorten it, and whether restoring requires a key that would itself be unavailable in the scenario the backup exists for.

Measure restore time as the whole path, not as the transfer. Locating the correct copy, provisioning a target, retrieving from a cold tier, transferring, restoring, replaying logs to the target point, validating, and cutting over are all inside the number that the recovery objective is compared against, and retrieval from cold storage alone can dominate it. Record the drill date, the dataset size at the time, and the person who executed it, because restore time scales with data volume and a figure from a much smaller dataset does not transfer.

Verify integrity beyond the job's exit status: a restored dataset is checked against a source-derived expectation such as row or object counts, referential consistency, and a query the application actually runs. Logical corruption and encryption by an attacker both replicate into backups happily, so retention needs to reach back past the detection window for the corruption class in question.

Restoring over live data is destructive and follows the ordered sequence in `references/suite-workflow-contract.md`, with this desk's additional constraint: take and confirm a fresh copy of the current live state before the restore begins, restore to a separate target, validate there, and only then cut over. That order is mandated because a restore over live data destroys the only copy of everything written since the backup, and a restore that turns out to be corrupt leaves nothing to return to.

**Parallel surface.** Datasets, backup jobs, retention and immutability checks, key availability checks, and drill history collection are independent units and are parallel-safe; per-dataset coverage reconciliation fans out.

The aggregate work runs once after the fan-out returns: composing per-dataset restore times into the journey or environment recovery time the recovery stage compares against RTO, identifying datasets that must be restored consistently with each other, ranking uncovered datasets by tier and by the journeys they carry, and reconciling total restore duration against the objective.

**Acceptance bar.** Every dataset in the inventory has a coverage state, including uncovered. Every schedule, retention, and immutability value names its configuration source. Every restore time comes from a dated drill with the dataset size recorded, or the dataset is marked never restored. Deletion resistance is assessed against a compromised credential, not only against hardware loss. The cross-dataset consistency requirement is stated where one exists.

## Outputs

A complete run delivers this artifact set:

- `backup-coverage-matrix.md`: every dataset from the inventory with its store, classification, owner, RPO, backup mechanism, and coverage state, with the uncovered set called out separately and ranked by tier.
- `backup-configuration-register.md`: per dataset, the mechanism, schedule, retention, storage tier and its retrieval time, immutability posture, encryption and key location, and the configuration source for each value, plus the last successful job with its date.
- `restore-procedure.md`: per dataset or dataset group, the executable steps, the permissions and credentials required, the target environment, the point-in-time selection method, the validation queries, the cutover step, and the abort path.
- `restore-drill-results.md`: per drill, the date, the dataset and its size, who executed it, the measured time per stage, what failed or surprised, and the resulting restore time with its scaling caveat.
- `deletion-resistance-assessment.md`: who and what can delete each copy, the trust boundary between primary and copy, immutability enforcement and its duration, key availability in the failure scenario, retention depth against the corruption detection window, and the residual exposure.
- `unproven-restore-register.md`: every dataset whose restore has never been demonstrated, the reason, the exposure if it were needed today, and the owner.
- `backup-downstream-handoff.md`: the restore durations `disaster-recovery-desk` folds into RTO, and the procedures `runbook-engineering-desk` turns into runbooks.

Depth standard per artifact: a restore procedure someone who has never restored this dataset could follow under pressure, including which credential is needed and where the key lives. A coverage entry that names the store and the account rather than the service category. A drill entry that records the dataset size, since restore time without volume is not transferable to the day it matters.

In `diagnostic` mode, when the backup system, job history, storage inventory, or drill records exist and cannot be read, the run delivers `backup-connector-diagnostic.md` reporting reachability, what was attempted, and the access needed. Coverage is not asserted from a backup policy document alone in that mode.

The failure this desk exists to prevent is the green backup job. A successful job means bytes were written somewhere; it says nothing about whether those bytes can be read back, whether the key is available, whether the schema still matches, whether the copy is complete, or whether the restore fits inside the recovery objective. Because the job status is available, dated, and looks like evidence, it is routinely quoted as if a restore had been proven. So in these artifacts a restore time appears only when a dated drill measured it, with the dataset size attached; a dataset with backups and no drill is recorded as unproven, never as recoverable; a retention or immutability value is read from configuration rather than from the policy document that describes it; and a key or credential the restore depends on is checked for availability in the scenario the backup exists for rather than assumed present. A register that says nine of fourteen datasets have never been restored is a plan for the next quarter. The same register with nine confident restore times is a data-loss event that has already been signed off.

## reliability_packet fields to update

- `backups[]`: `dataset`, `mechanism`, `schedule`, `retention`, `immutability`, `last_restore_test`, `coverage_gap`.
- `recovery.rpo_target` and `recovery.measured_recovery` refined where drill evidence bounds what is achievable.
- `reliability_risks[]` for uncovered datasets, deletable copies, unavailable keys, and restore times exceeding the objective.
- `readiness_gates[]` for the backup gate with the evidence behind its state.
- `reliability_surface` set to `backup_restore`.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: performing a restore, changing retention or immutability, deleting a copy, or accepting an uncovered tier 0 dataset as residual risk requires the named data owner.
- Production or destructive: the next action would restore over live data, delete or expire snapshots, shorten retention, release an immutability lock, or reconfigure a running backup job, and the mandated sequence has not been completed.
- Security or privacy: a restore would place regulated or personal data in a lower-trust environment, a procedure would embed credentials or key material, or retention would exceed a lawful limit that the privacy owner sets.
- Source conflict: the backup policy, the job configuration, and the job history disagree on whether a dataset is protected, so its recoverability is genuinely undetermined.
- Release integrity: a dataset would be recorded as recoverable, or an RPO declared met, without a dated restore establishing it.
- Connector unreachable: the backup system, job history, storage inventory, or drill record exists and cannot be read, so coverage and recoverability cannot be established.

Absent drill history, an incomplete data inventory, and an unrecorded dataset owner are soft gaps: record the dataset as unproven or unowned, name what is missing, and log the assumption where it was used. Immutability, retention against a lawful limit, and the requirement that a restore claim rests on a dated drill are never relaxed to make a coverage matrix look complete.

## Downstream handoffs

`disaster-recovery-desk` needs the measured restore times and the cross-dataset consistency constraints, because RTO is composed from them and a restore longer than the objective invalidates the plan. `runbook-engineering-desk` needs the restore procedures with their permission preconditions as on-call runbooks. `alerting-quality-desk` needs backup job failure and staleness as alertable conditions, since a silently failing backup is undetectable by design. `production-readiness-review-desk` needs the coverage matrix and the unproven register as the evidence behind the backup gate. `incident-command-desk` needs the restore procedure as an executable mitigation for data-loss events. Cross-suite: retention obligations and lawful deletion go to the Privacy Data Protection suite, storage lifecycle cost to the FinOps suite, and audit evidence packaging to the GRC suite.

## Quality bar

Coverage measured against the data that exists, with the uncovered list visible rather than buried. Mechanisms described by the failure class they defend against, so a replica is never counted as a backup. Deletion resistance assessed against a compromised credential. Restore times that come from a person, a clock, and a date, with the dataset size attached. An unproven register that is honest enough to be uncomfortable, because the datasets on it are the ones that decide whether an incident is recoverable.
