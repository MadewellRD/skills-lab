---
name: secrets-management-desk
description: manage secret exposure and credential handling, covering secret scanning across full repository history, hardcoded credentials in code images build logs and infrastructure state, exposure recorded by locator rather than value, vaulting and dynamic credential brokering, short-lived credentials and workload identity replacing static keys, pipeline and runtime secret injection, rotation and revocation ordering, and leaked-credential response. use for secret leak triage, vault design, credential rotation planning, pipeline secret handling review, and eliminating long-lived static keys.
---

# Secrets Management Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the secrets artifact set, update the `security_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable evidence source. Never invent credential locators, validity states, rotation dates, consumer lists, or the conclusion that an exposed credential was never used. Secret values never appear in an artifact, a message, or the packet, in whole or in fragment.

## Role

Own credentials as material that leaks. This desk maintains the exposure list by locator, designs the vaulting and brokering model that keeps secrets out of code and images, sets the rules for how pipelines and runtimes receive them, sequences rotation and revocation so it neither strands consumers nor leaves a live credential in place, and runs the response when a credential is found somewhere it should not be.

The premise of this desk is that a secret checked into history is a secret that exists forever in every clone, so the only remediation that means anything is revocation. Removing the commit changes the evidence, not the credential.

## Use when

- Secret scanning has returned results and they need triage: which are live, what each reaches, and what order to rotate in.
- A credential has appeared somewhere it should not be, including repository history, a container image layer, a build log, infrastructure state, a configuration map, a mobile bundle, or a support ticket.
- A vaulting or brokering model is being designed or replaced, including dynamic credentials, short-lived tokens, and the bootstrap problem of the first credential.
- Long-lived static keys need eliminating in favor of workload identity federation or issued short-lived credentials.
- Pipeline secret handling needs rules: how variables are scoped, which jobs can read them, what masking exists, and whether a fork or a pull request from outside can reach them.
- Rotation is due, has stalled, or has no runbook, and the consumers of a credential are unknown.
- A third-party or partner credential held by the organization needs a handling and rotation story.

## Do not use when

- The subject is the algorithm, key hierarchy, or hardware custody of cryptographic key material rather than application credentials. That is `cryptography-key-management-desk`, and this desk inherits the key that protects the vault from it.
- The subject is who may authenticate as a principal and with what factor. That is `identity-access-management-desk`, which supplies the non-human identity inventory this desk works against.
- The subject is whether a scanning gate should block a merge and what its false-positive budget is. That is `secure-sdlc-controls-desk`; this desk defines what a true positive means, that desk sets the gate.
- The subject is a compromised dependency or a package that exfiltrates credentials at build time. That is `software-supply-chain-desk`, which coordinates with the rotation sequence here.
- The credential is confirmed used by an unknown party. That is an incident and belongs to `security-incident-response-desk`, with this desk supporting the reach and rotation work.

## Required evidence

- Repository access including full history and all branches, since a secret removed from the current tree survives in reachable commits, tags, and forks.
- Secret scanning output covering history rather than only the working tree, with the detector and its validity-check capability named.
- Pipeline definitions, variable scopes, masking configuration, and the trigger types that expose variables to untrusted contributors.
- Artifact and image inventory: build layers, published packages, infrastructure state files, and configuration objects that may embed credentials.
- Vault or secret store inventory: what is stored, who reads it, access policy, audit logging, and how consumers authenticate to it.
- The non-human identity inventory from `identity-access-management-desk`, particularly static keys with no rotation state.
- Provider capability facts for each credential type: whether it supports scoped issuance, short expiry, usage logging, and independent revocation.
- Existing rotation runbooks, the consumers each credential serves, and the change windows those consumers require.
- Runtime injection method per environment: environment variables, mounted files, sidecar or agent brokering, and whether values reach process listings or crash dumps.

## Workflow

**Outcome.** An exposure register recorded by locator with validity and reach per entry; a vaulting and brokering design that says where every class of secret lives and how each consumer obtains it; pipeline and runtime handling rules; a rotation and revocation plan ordered so consumers are never stranded and live credentials are never left in place; and a leaked-credential response that ends with detection added rather than only with the credential replaced.

**Grounding.** Validity is established from provider metadata or a validity check the scanner performed, never from how the string looks. Reach is established from the credential's own permissions rather than from its name, because the token called `readonly` frequently is not. Consumer lists come from configuration, deployment manifests, or usage logs, since rotating a credential whose consumers were guessed is how a rotation becomes an outage. Scanner output is authoritative only for what it scanned: a clean result over the default branch says nothing about history, forks, or images.

**Constraints.** Every exposure entry records the locator, the credential type, the validity state, the rotation state, and what the credential reaches; the value itself is never written down, quoted in part, or reconstructed into an artifact, because a credential pasted into a report has a wider audience than the leak that prompted it. Exposures are prioritized by reach and validity rather than by detector confidence, since a live credential to a production data store outranks a hundred high-confidence hits on expired test tokens. Test fixtures and placeholders are dispositioned with the reason recorded, and a string is treated as live until a source establishes otherwise, because closing a real credential as a fixture is the most expensive mistake this desk can make. The vaulting design states the bootstrap path explicitly, since a model that leaves the first credential unexplained has moved the problem rather than solved it. Preference runs toward eliminating the secret entirely, through workload identity federation or issued short-lived credentials, before designing a better place to keep a static one. Pipeline rules name which trigger types expose variables to code the organization does not control, which is the most common way a build system leaks its own credentials. Runtime rules state where the value becomes visible, including process environment, crash dumps, log lines, and error reporting payloads.

**Ordered gate for responding to an exposed credential.** Response follows this sequence, and the order is externally mandated because deleting the commit removes the evidence and not the credential, and because some providers stop returning usage history once a key is deleted, so revoking before preserving the log makes the misuse question permanently unanswerable:

1. Establish validity and reach from provider metadata and permissions, without reproducing the value.
2. Preserve the credential's usage and access logs while the credential record still exists.
3. Issue a replacement, distribute it to the confirmed consumers, and establish that cutover is complete.
4. Revoke or delete the exposed credential.
5. Remove the exposed material from history, images, artifacts, state files, and logs, and add the detection that would have caught it at commit or build time.
6. Assess misuse against the preserved logs, and open an incident where use by an unknown party appears.

Where reach makes exposure intolerable, revocation may precede cutover as a containment decision by the credential owner, which trades an outage for a closed window. That call belongs to the owner and is recorded as an approval rather than assumed.

**Parallel surface.** Independent repositories, exposure findings, credential types, pipelines, and vault namespaces fan out safely and are triaged concurrently. The sequential passes run once after the fan-out returns: deduplicating the same credential found in several locations, ordering the rotation queue by reach and blast radius, mapping consumers per credential, and the aggregate statement of which credential classes remain static. A rotation order is by nature a statement about the whole set.

**Acceptance bar.** An owner could act on any exposure entry immediately: what it is, where it was found, whether it is live, what it reaches, and what happens next in what order. Every rotation entry names its consumers and its change window, the vaulting design answers the bootstrap question, and no artifact produced by this desk contains a credential value.

## Outputs

A complete run delivers this set:

- `secret-exposure-register.md`: one entry per exposure with locator, credential type, validity, reach, rotation state, and disposition reason where closed, and no values.
- `vaulting-and-brokering-design.md`: where each secret class lives, how consumers authenticate to obtain it, the bootstrap path, dynamic and short-lived credential use, and access logging.
- `static-credential-elimination-plan.md`: the long-lived keys that can be replaced by workload identity or issued short-lived credentials, with the dependency each replacement carries.
- `pipeline-and-runtime-handling-rules.md`: variable scoping, masking, trigger types that expose secrets to untrusted contributors, injection method per environment, and the paths by which a value becomes visible at runtime.
- `rotation-and-revocation-plan.md`: per credential, the consumers, the change window, the ordering, the rollback, and the owner who executes.
- `leaked-credential-response.md`: the response sequence instantiated for the live exposures found, with evidence preservation, ownership, and the detection added at the end.
- `secrets-downstream-handoff.md`: what `secure-sdlc-controls-desk` inherits, including the detector, the true-positive definition, and the exposures still open.

Depth standard: an artifact is complete when the credential owner can execute from it without a follow-up round trip. An exposure with no reach, a rotation entry with no consumer list, or a disposition with no recorded reason is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when repository history, scanner output, the vault, or provider metadata exists and cannot be read, the run delivers `secrets-connector-diagnostic.md` naming each unreachable source and the exposure surface it would have covered. A clean scan of the working tree is never reported as a clean repository.

Anti-fabrication guard: this desk has an inverted failure mode. The danger is not an invented finding but a reproduced one, since writing the credential into the report republishes it to a wider and more permanent audience than the original leak, and reports get pasted into tickets, chats, and slide decks that outlive the rotation. Locators, credential types, and reach are recorded; values, partial values, and reconstructions are not, at any confidence and for any reason. The second failure is disposition by appearance: a string is treated as live until provider metadata or a validity check says otherwise, because closing a production credential as a test fixture because it contains the word sample is a decision that reads as diligence and leaves the door open. Validity, last-use, and rotation dates are copied from provider records or left unknown, and "no evidence of misuse" is written only where usage logs were actually read, since the absence of a log query is not the absence of use.

## security_packet fields to update

- `secrets_exposure[]` with `locator`, `credential_type`, `validity`, and `rotation_state`, and never a value
- `identities[]` updated where an exposed credential establishes a principal's actual reach
- `findings[]` for exposure classes, pipeline handling defects, and static credentials with no rotation path, with `severity` carrying its scale
- `controls[]` for vaulting, brokering, scanning, masking, and injection controls with `enforcement_point`, `state`, and `evidence`
- `approvals[]` for revocation decisions, change windows, and any containment revocation ahead of cutover
- `incident` fields where misuse by an unknown party is established
- `source_facts[]` with `collected`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: a live credential is exposed. The value stays out of every artifact, the reach goes to the credential owner, and rotation waits on that owner because rotating blind takes down whatever still uses it. This is the stage-specific halt.
- **Production or destructive**: the next action would revoke, rotate, or delete a credential in service, or rewrite repository history that others have cloned.
- **Missing approval**: revoking ahead of consumer cutover, accepting a static credential that cannot be rotated, or extending an exposure window needs a named human owner.
- **Source conflict**: the scanner, the vault records, and the provider metadata genuinely disagree about whether a credential is live or already rotated.
- **Release integrity**: a statement that a repository, image, or pipeline is free of secrets would go out based on a scan that covered only part of the surface.
- **Connector unreachable**: repository history, scanner output, the vault, or the provider's credential metadata exists and cannot be read.

An unknown consumer list, a missing runbook, or an undocumented owner is a soft gap. Record it, label the assumption inline, continue, and let the rotation plan carry the discovery step.

## Downstream handoffs

`secure-sdlc-controls-desk` is next and needs the detector configuration, the true-positive definition, and the false-positive experience so the pre-merge gate is set with a real budget rather than an aspiration. `identity-access-management-desk` receives the static credentials that should become workload identities. `software-supply-chain-desk` needs the build-time credential exposure surface, since a compromised dependency reaches whatever the build can read. `cryptography-key-management-desk` owns the key protecting the vault and the rotation constraints that follow from it. `detection-engineering-desk` needs the credential usage telemetry that would show misuse. `security-incident-response-desk` inherits any confirmed misuse with the preserved logs already in custody.

## Quality bar

Good secrets work is ordered and specific. It knows which exposures are live before it knows how many there are, names what each credential reaches rather than what it is called, lists the consumers before proposing a rotation, and ends with a detector that would have caught the leak at commit or build time rather than with a cleaned-up history. The register is readable by the person who owns the credential and contains nothing that would be dangerous if the register itself leaked, which is the property that makes it safe to circulate at the speed this work requires.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
