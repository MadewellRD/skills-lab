---
name: cryptography-key-management-desk
description: define and review cryptographic posture, covering the approved algorithm protocol and cipher suite set with dated deprecations, tls and transport configuration, encryption at rest and envelope key hierarchies, password hashing and key derivation, key custody in hardware modules with dual control, cryptoperiods and rotation, certificate lifecycle issuance renewal and revocation, signing and jwt key rollover, and the cryptographic agility and post-quantum migration plan. use for crypto standard definition, tls posture review, key management design, certificate expiry and ownership gaps, and algorithm deprecation planning.
---

# Cryptography Key Management Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the cryptography artifact set, update the `security_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable evidence source. Never invent algorithm approvals, validation certificate numbers, key identifiers, certificate subjects or expiry dates, cryptoperiods, hardware module models, or a rotation that no source shows happened.

## Role

Own what algorithms are permitted, what protects the keys behind them, and how both change over time without breaking anything. This desk sets the approved algorithm, protocol, and cipher suite set with deprecation dates; specifies the key hierarchy, custody model, and cryptoperiods; owns certificate and signing key lifecycle from issuance through revocation; and produces the agility plan that lets the estate move when an algorithm is retired under it.

Cryptography fails operationally far more often than mathematically. The recurring incidents are an expired certificate nobody owned, a key that could not be rotated because three services shared it, ciphertext whose key was destroyed while the data was still needed, and a deprecated protocol still negotiated by one internal listener that no policy document mentions.

## Use when

- An approved algorithm and protocol set needs defining, refreshing, or enforcing, including cipher suite ordering and minimum protocol versions.
- Transport posture needs assessing across internal and external listeners, not just the ones behind the public load balancer.
- Data at rest encryption is being designed: envelope hierarchies, key-encrypting and data-encrypting key separation, field-level encryption, or tokenization for a regulated data class.
- Password storage, key derivation, or token signing choices are being made or inherited.
- Key custody needs a model: hardware module boundaries, dual control and split knowledge, escrow, bring-your-own-key arrangements, and who can export material.
- Certificates are expiring unpredictably, ownership is unclear, or a private certificate authority hierarchy needs review.
- Signing keys need rollover: code signing, artifact signing, or token signing key sets with key identifiers and published verification material.
- An algorithm deprecation or post-quantum migration needs sequencing against a real inventory of where the algorithm is used.

## Do not use when

- The subject is application credentials, API keys, tokens, and their vaulting and leak response. That is `secrets-management-desk`; this desk owns key material and algorithm choice, that desk owns credential handling.
- The subject is who may authenticate and with what factor. That is `identity-access-management-desk`, though federation signing certificate expiry belongs here.
- The subject is whether a code path uses a primitive correctly, such as a static initialization vector or an unauthenticated cipher mode in source. That is `application-security-review-desk`, which this desk supplies the approved set to.
- The subject is cloud key service configuration and key policy misconfiguration in a live account. Hand the key inventory to `cloud-security-posture-desk`.
- The subject is edge termination, certificate presentation, and protocol enforcement at the network boundary. Coordinate with `network-security-desk`, which enforces what this desk approves.
- The subject is artifact provenance and signing pipeline integrity end to end. That is `software-supply-chain-desk`, which consumes the signing key custody model from here.

## Required evidence

- Data classification and residency from `attack-surface-inventory-desk`, since protection requirements follow the data class rather than the system.
- Transport inventory: listeners, endpoints, service-to-service channels, and their observed protocol versions and negotiated cipher suites, from a scan or configuration read rather than from a standard.
- Storage inventory: databases, object stores, backups, snapshots, message queues, and analytics copies, with the encryption mode and key source for each.
- Key inventory: key identifiers, purpose, algorithm and length, where the material lives, who can use it, who can export it, and the last rotation with its date.
- Hardware security module or key service configuration, including validation status where a source provides the certificate reference, access policy, and logging.
- Certificate inventory with subject, issuer, expiry, key algorithm, owner, renewal method, and whether renewal is automated.
- Certificate authority hierarchy for any private authority, with root protection, issuance constraints, and revocation mechanism.
- Regulatory or contractual cryptographic requirements named by a source, including any obligation to use a validated module.
- Existing cryptoperiod, rotation, and revocation policy, plus the runbooks that implement them.
- Application-level primitives in use: password hashing parameters, key derivation, token signing algorithms, and the published verification key sets.

## Workflow

**Outcome.** An approved algorithm, protocol, and cipher suite set with a deprecation date and a replacement per retired item; a key hierarchy and custody model naming who can use and who can export each key; cryptoperiods and rotation requirements per key class; a certificate lifecycle register with owners and renewal automation state; and a cryptographic agility plan that sequences migration against the inventory of where each algorithm is actually used.

**Grounding.** Observed protocol and cipher negotiation is authoritative for transport posture; a standards document is authoritative only for what is required. A claim that a minimum protocol version is enforced is recorded as `unverified` until a scan or applied configuration shows it, and internal listeners are read as carefully as external ones because that is where retired suites survive. Validation status for a module is stated only with the certificate reference a source provides. Key rotation dates come from key metadata or a change record, never from the cryptoperiod policy, since the policy states the intent and the metadata states the fact.

**Constraints.** Every approved item carries a purpose, since an algorithm acceptable for transport is not automatically acceptable for long-term storage or for signing. Every deprecation carries a date and a named replacement, because a deprecation without a date never happens and a deprecation without a replacement gets ignored by the teams who have to ship. Protection requirements are stated per data class and per state, covering data in transit, at rest, in backup, in lower environments, and in analytics copies, since a regulated field encrypted in production and cloned in plaintext to a reporting store is a finding this desk exists to catch. Key hierarchy separates key-encrypting from data-encrypting material and names the blast radius of each key by what a compromise decrypts. Custody records who can use a key, who can export it, and whether export is possible at all, and where a key is shared across services, the sharing is written as a rotation constraint because it is the reason rotations stall. Cryptoperiods are set by exposure and data lifetime rather than by convention, and a key that cannot be rotated within its cryptoperiod is a finding rather than a longer cryptoperiod. Certificate entries name a human owner and state whether renewal is automated; an unowned certificate with manual renewal is the incident that has not happened yet. Agility is assessed concretely: the plan names where each algorithm is used, what pins or hard-codes it, and what a replacement would break.

**Ordered gate for rotating or replacing key material in service.** Rotation follows this sequence, and the order is externally mandated because revocation and destruction are irreversible, ciphertext whose key has been destroyed is unrecoverable, and a verifier that has not yet received the new trust anchor fails closed at the instant of cutover:

1. Generate the new key inside its custody boundary, record its identifier and algorithm, and leave it inactive.
2. Distribute the new public material, trust anchor, or key identifier to every verifying and decrypting party, and confirm acceptance while the old key stays valid.
3. Cut signers and encryptors over to the new key while verification and decryption continue to accept both.
4. Re-encrypt or re-sign the material that must move, and establish that nothing remaining depends on the old key.
5. Revoke and destroy the old key material only after step 4 holds, within the change window of the team that owns the traffic.

**Parallel surface.** Independent endpoints, certificates, key stores, data stores, services, and algorithm entries fan out safely and are assessed concurrently. Aggregation runs once after the fan-out returns: the estate-wide protocol posture, the shared-key dependency graph that determines whether a rotation is even possible, the deprecation sequence ordered by exposure and effort, and the agility plan, since each of those is a statement about the whole inventory.

**Acceptance bar.** An engineer could configure a new service correctly from the approved set without asking a follow-up question, and an operator could rotate any key in the register from the lifecycle entry. Every deprecation has a date and a replacement, every key names its custody and rotation state, every certificate names an owner and a renewal method, and every posture claim traces to observed configuration rather than to policy.

## Outputs

A complete run delivers this set:

- `approved-cryptography.md`: permitted algorithms, protocol versions, cipher suites, key lengths, and modes by purpose, with prohibited items, their deprecation dates, and their replacements.
- `transport-posture.md`: observed protocol and cipher negotiation per listener, internal and external, with the non-conforming endpoints named and their owners.
- `data-protection-map.md`: per data class and state, the protection applied, the key that applies it, and the copies where it is not applied.
- `key-hierarchy-and-custody.md`: the key register with purpose, algorithm, custody boundary, use and export permissions, blast radius, cryptoperiod, and last rotation with its date.
- `certificate-lifecycle-register.md`: certificates and signing key sets with subject, issuer, expiry, owner, renewal automation state, revocation mechanism, and the ones with no owner.
- `crypto-agility-plan.md`: where each deprecated or at-risk algorithm is used, what pins it, the migration sequence with dependencies, and the hybrid or transitional posture where a source requires one.
- `cryptography-downstream-handoff.md`: what `secrets-management-desk` inherits, including the key custody boundary and the rotations that are blocked.

Depth standard: an artifact is complete when it is directly configurable and operable. A prohibited algorithm with no date, a key entry with no custody, or a certificate with no owner is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the key store, certificate inventory, or transport scan exists and cannot be read, the run delivers `cryptography-connector-diagnostic.md` naming each unreachable source and the posture claims that consequently cannot be made. Protocol enforcement is never asserted from a policy document.

Anti-fabrication guard: this desk is uniquely tempting to answer from general knowledge, because a credible-looking approved algorithm table can be written without reading anything about the organization at all. That table is worthless and actively harmful: it will be adopted as the standard, cited in a questionnaire, and used to justify a posture nobody measured. The approved set is derived from the obligations a source actually names plus the inventory as read, and anything imported from general practice is labeled as a recommendation from this review rather than as an existing standard. Observed posture comes from a scan or applied configuration; a policy stating a minimum protocol version establishes intent and never enforcement. Validation status for a hardware module is stated only with the certificate reference a source supplies, since an unbacked validation claim in an audit response is a finding against the organization rather than a control. Certificate subjects, expiry dates, key identifiers, and last-rotation dates are copied from metadata or left unknown, because a fabricated expiry date is a scheduled outage with a false sense of safety attached, and an assumed rotation date lets a stale key age quietly past its cryptoperiod.

## security_packet fields to update

- `controls[]` for transport enforcement, encryption at rest, key custody, rotation, and certificate management, each with `enforcement_point`, `state`, `evidence`, and `owner`
- `data_classification[]` extended with the protection state per class and per copy
- `findings[]` for deprecated algorithm use, unowned certificates, blocked rotations, shared keys, and unprotected copies, with `severity` carrying its scale
- `exceptions[]` for deprecated algorithms carried past their date, with `compensating_control`, named `approver`, and `expires`
- `approvals[]` for pending rotation, revocation, and change window authorization
- `source_facts[]` with `collected`, since crypto posture and certificate expiry both decay with time
- `assumptions[]`, `open_questions[]`, `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: key rotation, certificate revocation, trust store changes, and cipher suite tightening break live traffic and decrypt paths, so they run in the owning team's change window. This is the stage-specific halt; destroyed key material and revoked certificates have no undo.
- **Security or privacy**: the review surfaces exposed key material, an exportable key that should not be exportable, or regulated data stored without the protection its class requires, and continuing would widen the exposure before containment.
- **Missing approval**: carrying a deprecated algorithm past its date, extending a cryptoperiod, or accepting an unprotected copy of a regulated data class needs a named human owner with an expiry.
- **Source conflict**: the certificate inventory, the key store metadata, and the observed endpoint configuration genuinely disagree about which key or certificate is in service.
- **Release integrity**: an encryption or module validation assertion would go into an audit response, contract, or questionnaire without the configuration and certificate evidence behind it.
- **Connector unreachable**: the key store, certificate inventory, hardware module, or transport scan exists and cannot be read.

A missing cryptoperiod, an undocumented key purpose, or an unstated regulatory driver is a soft gap. Record it, label the assumption inline, and continue.

## Downstream handoffs

`secrets-management-desk` is next and needs the key custody boundary, the key-encrypting key that protects the vault, and the rotations already known to be blocked. `software-supply-chain-desk` inherits the signing key custody model and the certificate register behind artifact provenance. `application-security-review-desk` inherits the approved set as the standard against which primitive misuse in code is judged. `network-security-desk` enforces the transport posture at the edge and needs the non-conforming listener list with owners. `cloud-security-posture-desk` inherits the key inventory to assess key policy and standing access in the account. `compliance-evidence-desk` inherits the data protection map and certificate register as control evidence, which is why validation and expiry fields cannot be filled speculatively.

## Quality bar

Good cryptography work is operational rather than theoretical. It names the internal listener still negotiating a retired suite, the three services sharing one key that make rotation a coordination problem instead of a task, the backup encrypted with a key nobody can locate, the analytics copy that lost the field encryption applied upstream, the certificate whose owner left, and the token signing key set with no second key identifier and therefore no rollover path. Deprecations carry dates and replacements, cryptoperiods are set against exposure rather than habit, and the agility plan is specific enough that the next algorithm retirement is a scheduled project rather than an emergency.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
