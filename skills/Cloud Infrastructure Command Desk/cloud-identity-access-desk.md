---
name: cloud-identity-access-desk
description: design cloud identity and access, covering federation and single sign-on for human access, role and permission-set structure with least privilege, permission boundaries and their interaction with organization-level denies, workload identity that removes static access keys, cross-account trust and its direction, standing and privileged access findings, break-glass with storage and alerting, and access review cadence with named reviewers. use for cloud iam design, federation rollout, least-privilege reduction, trust policy review, static credential elimination, and access recertification.
---

# Cloud Identity Access Desk

## Suite workflow mode

This desk is a member of the Cloud Infrastructure Command Desk suite. Complete the identity artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Identity is the surface where a soft gap and a hard halt are easiest to confuse: an unknown role owner is soft, while an access claim asserted without applied-policy evidence is a security halt. Never invent role, policy, permission-set, group, or principal identifiers; trust policy contents; condition keys; session durations; or the enablement state of any control.

## Role

Own who can do what, proven from applied policy rather than from intent. This desk defines the human access model and its federation path, the role and permission-set structure with least-privilege scoping, permission boundaries and how they interact with the organization-level denies inherited from the hierarchy, workload identity that removes static long-lived keys, cross-account trust relationships and their direction, the standing and privileged access findings, the break-glass path with its storage and alerting, and the review cadence with named reviewers.

Two properties make this desk different from an access review in any other domain. Cloud permissions compose across layers, so an account-level grant, a permission boundary, and an organization-level deny produce an effective permission that none of the three documents states on its own. And a role's trust policy is a wider control than its permission policy, because it decides who may become the principal at all; a permissive permission set on a role nobody can assume is theoretical, while a narrow permission set on a role any account may assume is a live path.

## Use when

- Federation or single sign-on is being designed, migrated, or extended to new accounts, including group-to-role mapping and automated user provisioning.
- Roles and permission sets are being structured, consolidated, or reduced toward least privilege using access history.
- Permission boundaries are being introduced, or delegated administration needs a ceiling that a delegated admin cannot raise.
- Static long-lived access keys exist in pipelines, workloads, or user hands and need replacing with short-lived or federated credentials.
- Cross-account trust is being established, audited, or found to be wider than intended, including third-party and vendor access.
- Standing privileged access needs converting to time-bound elevation, or privileged role usage needs a finding written against it.
- Break-glass is being defined, or nobody can say what happens if the identity provider is unavailable.
- An access review or recertification cycle is due and the reviewer set, the evidence, and the revocation path need defining.

## Do not use when

- The subject is the hierarchy, account separation, or organization-level deny attachment itself. That is `landing-zone-account-structure-desk`; this desk designs grants inside the boundaries it sets.
- The subject is key material, secret storage, or credential rotation mechanics. That is `configuration-secrets-desk`; this desk decides who may assume what, that desk holds what the credential is made of.
- The subject is benchmark-mapped posture findings across the estate. That is `cloud-security-posture-desk`.
- The subject is the pipeline apply identity's scope per environment as part of the promotion model. That is `provisioning-pipeline-desk`, which consumes the identity model defined here.
- The subject is application-level authorization, end-user identity, or customer accounts. That is a labeled cross-suite handoff to the Security or application suites.

## Required evidence

- The identity provider configuration: trust relationship, assertion or claim mapping, group membership source, provisioning method, and session lifetime.
- The applied role, policy, and permission-set inventory per account, at live values rather than at the values a module declares.
- Trust policies and their principals, including wildcard principals, external accounts, third-party vendors, and any external-identifier condition that exists or is missing.
- Permission boundaries: which exist, which principals they are attached to, and what they cap.
- The organization-level deny set and attachment points inherited from the landing zone stage, since effective permission cannot be computed without it.
- Access history: last-used data per role and per permission, credential age, and the authentication events that show which paths are actually exercised.
- Static credential inventory: access keys with age and last use, service accounts with passwords, and any credential embedded in pipeline configuration.
- Workload identity configuration: instance and service identities, federation trust for external workload identity, and the roles those identities may assume.
- Break-glass records: the accounts or roles, where their credentials are stored, what alerts on use, and the date of the last exercise.
- Separation-of-duties obligations from the compliance regimes recorded at intake.

## Workflow

**Outcome.** A human access model with its federation path and group-to-role mapping, a role and permission-set structure scoped from access evidence, permission boundaries with what they cap, a workload identity model that names every remaining static credential and its replacement path, a cross-account trust inventory with direction and condition per relationship, the standing-access findings, a break-glass path with storage and alerting, and a review cadence with named reviewers.

**Grounding.** Least privilege is assessed against access history, not against the wording of a policy document; a permission nobody has used in the observation window is a candidate for removal, and a permission the document does not mention but the logs show being used is a finding. Effective permission is computed across the organization deny, the boundary, and the grant together, because reporting a grant in isolation overstates what a principal can do and reporting a deny in isolation understates it. Where the identity provider's group mapping and the applied role assignments disagree about who holds a role, record both and preserve the conflict.

**Constraints.** Every role entry names its trust policy principals before its permissions, because the trust policy is the wider control. A trust relationship with a wildcard principal, a missing external identifier for third-party access, or a condition that does not constrain the source is recorded as an exposure with its reachable path rather than as a style issue. Workload identity is stated as the replacement for each static key found, with the credential's age and last use, and a key that cannot yet be replaced is recorded with the reason and an owner rather than being left out. Break-glass names the storage, the alert destination, the approval required to use it, and the date it was last exercised, and it is designed to survive the identity provider being unavailable, since a break-glass path that depends on federation is not a break-glass path. Review cadence names reviewers by role and states what evidence a reviewer must see to approve, because a recertification without last-used data is a signature, not a review.

**Parallel surface.** Independent accounts, roles, permission sets, trust relationships, static credentials, and workload identities are independent assessment units and fan out safely, as does the per-account read of applied policy. The effective-permission computation that composes organization denies with boundaries and grants, the cross-account trust graph, the aggregate standing-access finding, and the separation-of-duties judgment run once after the fan-out returns, because a per-account least-privilege review cannot see the role in one account that trusts a principal in another and thereby joins two blast radii into one.

**Ordered gate for changing a live access path.** Narrowing federation, removing a privileged role, tightening a trust policy, or revoking a standing grant runs in this order, because the permission being removed is frequently the one required to put it back, and step 4 is where lockout becomes real:

1. Establish from access history who and what actually uses the path, over a window long enough to include periodic and quarter-end activity.
2. Confirm an independent working access path exists that does not depend on the mechanism being changed, and that break-glass has been exercised rather than merely documented.
3. Obtain the approval the blast radius requires, recorded against this specific change.
4. Apply the narrowing with the old grant left in place but unused where the provider allows it, an observation window, and a stated rollback trigger, then remove the old grant after the window closes.

Deleting an identity provider trust, rotating a trust root, or removing the last administrative principal follows the destructive sequence in `references/suite-workflow-contract.md` instead of this one.

**Acceptance bar.** A security reviewer could state, from these artifacts alone, which humans can reach production and by what path, which workloads hold static credentials, which accounts can be entered from outside the organization, and what happens when the identity provider is down. Every access claim names the applied policy it was read from, and every remaining static credential has an owner and a replacement path.

## Outputs

A complete run delivers this set:

- `human-access-model.md`: federation design, group-to-role mapping, session lifetime, authentication requirements, and the path from a person to a production permission.
- `role-and-permission-structure.md`: roles and permission sets with trust policy principals stated before permissions, and the scoping evidence behind each.
- `least-privilege-findings.md`: permissions unused over the observation window, permissions used that no document grants, and the reduction proposed for each with its risk.
- `permission-boundary-model.md`: boundaries, what they cap, the principals they attach to, and the composition with organization-level denies including any grant the deny already makes inert.
- `workload-identity-plan.md`: every static credential found with age and last use, its replacement mechanism, and the ones that cannot be replaced yet with the reason and owner.
- `cross-account-trust-map.md`: every trust relationship with direction, principal, condition, and the reachable path it creates, including third-party and vendor access.
- `break-glass-and-review.md`: the emergency path with storage, alerting, approval, and last exercise date, plus the review cadence with named reviewers and the evidence each must see.
- `identity-downstream-handoff.md`: what `cloud-network-architecture-desk` and the later provisioning stages inherit, including the apply identity's expected scope.

Depth standard: an artifact is complete when a security reviewer and a platform engineer could both act on it unchanged. A role without its trust policy principals, a least-privilege finding without access evidence, and a break-glass path without an exercise date are unfinished rather than draft.

When the identity provider configuration, applied policy inventory, or access history exists and cannot be read, the run delivers `identity-connector-diagnostic.md` naming each unreachable source and the access claims that depend on it, in place of the artifacts that source would have grounded. Access is never described as least-privileged against evidence that could not be read.

Anti-fabrication guard: this desk writes sentences that a reader will treat as an audit result, and the tempting error is not inventing a role but promoting a policy document into an applied state. A permission boundary described in a design note and attached to no principal caps nothing, and reporting it as the control that limits delegated administration is a false assurance that survives until someone tests it. The same applies to least privilege claimed from reading a policy rather than from access history: without last-used evidence, the honest finding is that the scope is unassessed, not that it is appropriate. Role names, policy identifiers, trust principals, condition keys, session durations, and credential ages are quoted from applied configuration or left unresolved, since a wrong principal in a trust map sends the next reviewer to audit a relationship that does not exist while the real one keeps standing. Where the deny set could not be read, effective permission is reported as uncomputed rather than approximated from the grant alone.

## infrastructure_packet fields to update

- `identity.human_access_model` and the federation path
- `identity.workload_identity` with the mechanism replacing static keys
- `identity.privileged_roles` and `identity.permission_boundaries` with attachment state
- `identity.standing_access_findings` with the access evidence behind each
- `identity.break_glass` with storage, alerting, and last exercise date
- `identity.access_review_cadence` with named reviewers
- `secrets_and_config.known_exposure` for any static credential found in code, pipeline configuration, or logs
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: continuing would assert role scope, trust boundaries, credential state, or federation behavior as verified without applied-policy evidence, or the work would place credentials, keys, assertions, or personal data into an artifact or a log.
- **Production or destructive**: the next action would change live federation, delete or narrow a role in use, tighten a trust policy, revoke standing access, or rotate a trust root.
- **Missing approval**: a privileged grant, a third-party trust relationship, a break-glass design, or a separation-of-duties exception needs a named owner who has not authorized it.
- **Source conflict**: the identity provider, the applied policy inventory, and the access history genuinely disagree about who holds a role or what it permits, and choosing one silently would publish an access claim that does not hold.
- **Release integrity**: least privilege, credential elimination, or a separation-of-duties control would be declared satisfied without the access evidence that establishes it.
- **Connector unreachable**: the identity provider configuration, applied policy inventory, access history, or credential inventory exists and cannot be read.

Unknown role owners, undocumented historical grants, and missing business justification for an existing permission are soft gaps. Name them, label the assumption, and continue. Separation of duties, privileged access approval, and the prohibition on carrying credentials into artifacts are never relaxed to keep a workflow moving.

## Downstream handoffs

`cloud-network-architecture-desk` is next and needs the workload identity model, since private service access and endpoint policy are frequently enforced by principal rather than by address. `compute-platform-desk` and `container-platform-desk` need the workload identity mechanism so instances and pods receive credentials without static keys. `provisioning-pipeline-desk` inherits the apply identity and its expected scope per environment. `configuration-secrets-desk` inherits every static credential found here with its replacement path. `cloud-security-posture-desk` inherits the standing-access and trust findings as posture input. `resilience-multi-region-desk` needs to know whether the access path survives a regional failure. Send detection engineering for identity abuse and adversarial identity threat modeling to the Security suite as a labeled cross-suite handoff.

## Quality bar

Good identity work reads like a reachability analysis rather than a policy catalogue. It starts from who can become which principal, composes the deny, the boundary, and the grant into an effective permission, and says plainly which paths reach production. It counts static credentials rather than describing an intention to remove them, and it gives each one an owner and a date. Break-glass is described as something that has been used in a drill, with the alert that fired. And the review cadence names people, not a function, because an access review assigned to a team is an access review nobody performed.
