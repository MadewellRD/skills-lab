---
name: configuration-secrets-desk
description: design cloud key management and secrets handling including the key hierarchy with scope and ownership and rotation state, envelope encryption and key policy, secret store selection and per-consumer access policy, rotation with dual-slot cutover, short-lived workload credentials replacing static access keys, configuration layering and precedence across environments, secret delivery into compute and container and pipeline surfaces, and remediation of credentials found in state files, machine images, or logs.
---

# Configuration Secrets Desk

## Suite workflow mode

This desk is part of the Cloud Infrastructure Command Desk suite. Complete the key and secrets artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, declared-versus-live source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent key identifiers, secret paths, rotation dates, key policy statements, credential owners, or the contents of any secret. Secret material never enters an artifact, a packet field, a log line, or a handoff.

## Role

Own the material that unlocks everything else: keys, secrets, and the configuration that tells a workload which of them to use. This desk decides the key hierarchy and who administers versus uses each key, which store holds which secret and who may read it, which credentials are replaced by short-lived identity rather than rotated forever, how configuration layers resolve when two layers disagree, how a secret reaches a running workload without passing through a place that keeps a copy, and what happens to a credential that has already leaked.

The distinction that organizes this desk is between a secret and a credential path. A secret is a value that must be protected. A credential path is the question of whether a value needs to exist at all. Most static access keys in a mature estate are not rotation problems; they are identity problems that were solved with a key because the identity federation was not wired up yet.

## Use when

- The key hierarchy needs definition or review: which keys exist at what scope, who administers them, who may use them for encrypt versus decrypt, and whether rotation actually re-encrypts anything.
- Secret store selection or access policy per consumer is the subject, including which workload may read which path and under which identity.
- Rotation policy is being written or is failing: what breaks mid-rotation, whether consumers can hold two valid credentials at once, and which credentials cannot be rotated without a restart.
- Static long-lived keys exist and should be replaced by federated workload identity, instance or pod identity, database identity authentication, or short-lived certificates.
- Configuration layering and precedence are ambiguous, so nobody can say which value a production workload actually resolved.
- Secret delivery into compute, containers, or the provisioning pipeline needs a decision on mechanism and its exposure surface.
- Credentials have been found where they should not be: in a state file, a machine image, a repository history, a log stream, or an environment dump.

## Do not use when

- The identity model itself is the subject, including federation design, role structure, permission boundaries, and trust relationships: that is `cloud-identity-access-desk`. This desk consumes that model and removes the static credentials it makes unnecessary.
- The encryption posture of a specific data service, including default keys on buckets, volumes, and database storage: that belongs with `cloud-storage-data-services-desk` and `managed-database-platform-desk`, which own the resource-level setting. This desk owns the key those settings point at.
- Whether a benchmark control on encryption or key rotation is met across the estate, and the exception register for it: that is `cloud-security-posture-desk`.
- The pipeline's own gates and apply identity scope: that is `provisioning-pipeline-desk`, which hands this desk any credential the pipeline currently holds.
- Application-level secret handling in code, dependency scanning, and threat modeling: cross-suite handoff to the Security suite.

## Required evidence

- Key inventory with scope, key policy or access policy, administrator versus user separation, origin, and whether rotation is enabled and what it rotates.
- Secret store inventory: paths or names, the identities with read access to each, versioning, and deletion or recovery windows.
- The rotation state of record per credential class, taken from the store rather than from a policy document.
- Workload identity configuration: federation trust, service account bindings, instance profiles, and database identity authentication where enabled.
- Static credential inventory: access keys with last-used evidence, service account keys, connection strings, and any credential held by the pipeline.
- Configuration sources and their layering: parameter stores, environment configuration files, container environment definitions, and any runtime override mechanism.
- Exposure evidence: secret-scanning results, state file contents review, image layer scan output, and log query results for credential patterns.

## Workflow

**Outcome.** A key and secret model where every key states its scope, administrator, users, and true rotation state; every secret states its store, its readers, and its rotation class; every static credential either has a replacement identity path or a stated reason it survives; configuration precedence is written and unambiguous; delivery mechanism per surface is chosen with its exposure named; and every known exposure has a remediation with a sequence.

**Grounding.** Read the key and secret stores for what is configured and the audit log for what is actually used, and keep them labeled separately per `references/suite-workflow-contract.md`. Configured and used diverge in a specific way here: a key with a rotation policy and no recent decrypt activity may be protecting nothing, and an access key with no rotation and daily use is load-bearing for something nobody has mapped. A key policy is evidence of intent; last-used data is evidence of reality.

**Constraints.** Every key names an administrator and a user set that do not collapse into the same principal, because a role that can both use a key and change its policy can grant itself anything the key protects. Rotation is described by what it does rather than by its schedule: rotating a key that wraps existing data protects new writes and leaves old ciphertext under the previous version, which is a correct design and a wrong assumption to leave unstated. Every rotation policy names what breaks during the change and whether two credentials can be valid simultaneously, since a consumer that cannot hold two is a rotation that is really an outage. Static long-lived credentials are treated as an identity gap first and a rotation task second. Secret delivery names its exposure: values placed in environment variables are readable by child processes, appear in process listings and crash dumps, and survive into container inspection output, while file mounts and agent-fetched values have different and smaller surfaces. Configuration precedence is stated as an ordered resolution rule, because two layers that both look authoritative mean the production value is decided by load order. Nothing in this desk's output contains a secret value; it contains references, locations, and states.

Remediating a credential that is already exposed runs in this order, and the order is mandated because it is the only sequence that avoids either an outage or the destruction of the evidence needed to know whether the credential was used:

1. Establish scope from the audit log first: what the credential can reach, where it appears, and every use recorded during the exposure window. This step comes first because later steps destroy this evidence.
2. Issue the replacement and cut consumers over to it while the exposed credential is still valid, so the cutover is not also an outage.
3. Revoke or disable the exposed credential, and confirm from the audit log that use has stopped rather than assuming it.
4. Purge the material from where it leaked, including state objects, image layers, repository history, log retention, and any backup of those.
5. Record the exposure window, the observed use, and the control change that prevents a recurrence.

**Parallel surface.** Keys, secrets, credential classes, consumers, configuration layers, and delivery surfaces are independent units and are parallel-safe; per-key policy review, per-secret access analysis, per-consumer delivery assessment, and connector preflight across the key store, secret store, and scanning output all fan out.

The aggregate work runs once after the fan-out returns: the key hierarchy as a whole with its cross-account grants, the rotation calendar and the collisions in it, the blast radius of any single key or store compromise, and the precedence rule that only makes sense across all layers at once. A per-secret access review that never rolls up misses the case where four separately reasonable grants give one role the ability to read every environment.

**Acceptance bar.** An engineer can name, for any workload, which identity it uses, which secrets it reads, how those arrive at runtime, which key protects the data it writes, and when that credential was last rotated according to the store. Every rotation date, key scope, and access grant traces to store output or audit evidence, or is written as unverified.

## Outputs

A complete run delivers this artifact set:

- `configuration-secrets-key-hierarchy.md`: every key with scope, administrator, user set, origin, cross-account grants, rotation behavior and what it actually re-encrypts, and the blast radius if that key were compromised or deleted.
- `configuration-secrets-store-and-access.md`: secret paths by consumer, the identity behind each read, versioning and recovery windows, and the grants that exceed what the consumer needs.
- `configuration-secrets-rotation-plan.md`: rotation class per credential, what breaks during the change, whether dual-slot cutover is possible, the consumers that require a restart, and the credentials that cannot be rotated at all with the reason.
- `configuration-secrets-static-credential-elimination.md`: every static long-lived credential with its last-used evidence, the workload identity path that replaces it, and the ones that survive with a named reason and an owner.
- `configuration-secrets-config-layering.md`: the layers, the ordered precedence rule, what each environment overrides, and the values whose resolution is currently ambiguous.
- `configuration-secrets-exposure-remediation.md`: each exposure with its location, exposure window, observed use from the audit log, remediation state, and the control that prevents recurrence.
- `configuration-secrets-downstream-handoff.md`: the encryption and key ownership facts `cloud-security-posture-desk` needs, and the credential release items `cloud-decommissioning-desk` inherits.

Depth standard per artifact: a key entry names the data it protects and the principals on both sides of the administer-versus-use line, not the reassurance that key management is centralized. A rotation entry names the consumer that has to restart. A delivery entry names the mechanism and its readable surface. An exposure entry gives the window and the audit evidence, or states plainly that the audit retention does not cover the window.

In `diagnostic` mode, when the key store, secret store, or scanning output exists and cannot be read, the run delivers `configuration-secrets-connector-diagnostic.md` naming what was attempted and the access needed. Rotation and access claims are not drafted from policy documents alone in that mode.

The field that goes wrong on this desk is rotation state. "Last rotated" is a date, dates look like facts, and the policy that says annual rotation makes a plausible one trivially available. A credential whose store shows no rotation timestamp is recorded as rotation-state-unknown, never as compliant with the policy that governs it, because a fabricated rotation date closes a finding that is still open and quietly certifies a key that has been live since the account was created. The same restraint applies to key identifiers and secret paths: an invented path becomes a lookup that either fails closed in production or, far worse, resolves to a real secret meant for something else. And no artifact from this desk ever contains the value itself, however convenient it would be to show it.

## infrastructure_packet fields to update

- `secrets_and_config.key_hierarchy`, `secrets_and_config.secret_store`, `secrets_and_config.rotation_policy`, `secrets_and_config.dynamic_credentials`, `secrets_and_config.config_layers`, `secrets_and_config.known_exposure`.
- `identity.workload_identity` and `identity.standing_access_findings` where static credentials are replaced or persist.
- `data_stores[].encryption` where key ownership for a store is established or corrected.
- `posture` input for any exposure that maps to a benchmark control, left for `cloud-security-posture-desk` to score rather than re-scored here.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: rotating a trust root or a key that wraps production data, disabling a credential still in use, or accepting a static credential as permanent needs a named human owner who has not given it.
- Production or destructive: the next action would rotate, disable, delete, or schedule deletion of a live key or secret, or change a key policy in a production account. Key deletion is the sharpest case in this suite, because data encrypted under a deleted key is unrecoverable and the operation is asynchronous enough to look like it succeeded harmlessly.
- Security or privacy: a secret value would enter an artifact, log, packet, or handoff; credential material was found in state, an image, or a repository; or key ownership and access scope would be asserted as verified without store evidence.
- Source conflict: the key store, the secret store, the configuration files, and the audit log genuinely disagree about which credential a workload uses, and choosing one silently would leave a live credential unaccounted for.
- Release integrity: rotation compliance, encryption coverage, or static-credential elimination would be declared complete without store or audit evidence behind it.
- Connector unreachable: the key store, secret store, audit log, or scanning output exists and cannot be read.

An undocumented key rationale, a missing secret owner, or an unmeasured consumer list is a soft gap: proceed with it named. Encryption obligations, the administer-versus-use separation, and the prohibition on writing secret values into artifacts are not soft gaps and are never relaxed to keep the workflow moving.

## Downstream handoffs

`cloud-security-posture-desk` needs key ownership, encryption state, and every open exposure with its window, so those become findings with an exposure path rather than generic hardening. `provisioning-pipeline-desk` receives the replacement identity path for any credential the pipeline holds. `cloud-decommissioning-desk` inherits the credential and key release list for any resource being retired, including the keys that must outlive the data they protect. `drift-detection-reconciliation-desk` needs the configuration layers, since an override applied by hand at the top layer is drift that no plan will ever show.

## Quality bar

A model where the answer to "what can read this secret" is a short list of identities rather than a shrug, rotation is described by consequence rather than by calendar, static keys are shrinking against a named replacement path, and every exposure has an evidence-backed window instead of a reassurance. States are honest, including unknown, and no artifact anywhere contains the material it is protecting.
