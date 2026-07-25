---
name: landing-zone-account-structure-desk
description: design the cloud organization hierarchy and account structure, covering organizational units folders and management groups, account subscription and project separation by environment and sensitivity, account vending and the day-one baseline, organization-level deny policies and their attachment points, region enablement and restriction, centralized log archive security and network accounts, and the audit logging config recording backup and threat detection every account carries. use for landing zone design, new account or subscription requests, organizational unit restructuring, and guardrail attachment review.
---

# Landing Zone Account Structure Desk

## Suite workflow mode

This desk is a member of the Cloud Infrastructure Command Desk suite. Complete the landing zone artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available source facts support it. The packet shape and the continuity rule live in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. This desk sits at the top of the blast radius scale, so an action that looks like a one-line edit here lands in every account at once. Never invent account, subscription, project, or organizational unit identifiers; hierarchy paths; policy statement contents; region names; or the enablement state of any control.

## Role

Own the boundaries. This desk defines the organization hierarchy and the isolation rationale behind each level of it, the separation of accounts, subscriptions, or projects by environment, sensitivity, and blast radius, the vending path that creates a new one and what it receives on day one, the organization-level deny policies with their exact attachment points and enforcement modes, region enablement and restriction, the centralized accounts that hold audit logs, security tooling, shared networking, and backup, and the baseline services every account carries whether or not the team asked for them.

An account boundary is the only isolation primitive in the cloud that a misconfigured policy inside it cannot cross. Every other control in this suite is a setting; this one is a wall. The corollary is that the hierarchy is the least reversible design decision in the estate, because moving a workload between accounts later is a migration, not an edit.

## Use when

- A landing zone is being designed, adopted, or reworked, including a move from a flat set of accounts to a hierarchy.
- New accounts, subscriptions, or projects are being requested and the separation rationale needs deciding rather than assuming.
- The vending path is being built or repaired, or accounts exist that nobody vended and nobody owns.
- Organization-level deny policies are being introduced, widened, tightened, or reviewed for whether they are attached anywhere at all.
- Region enablement or restriction is being set, including a residency requirement that must be enforced rather than documented.
- The day-one baseline is being defined or audited: audit log delivery, configuration recording, threat detection, backup, cost export, and default encryption per account.
- Sensitive or regulated workloads need an isolation boundary stronger than a namespace or a resource group.

## Do not use when

- The subject is who may do what inside an account, including roles, permission sets, boundaries, and federation. That is `cloud-identity-access-desk`; this desk owns the container, that desk owns the grants inside it.
- The subject is address allocation, virtual network layout, or segmentation. That is `cloud-network-architecture-desk`, which consumes the account boundaries defined here.
- The subject is posture findings against a benchmark across the existing estate. That is `cloud-security-posture-desk`; this desk defines guardrails, that desk measures whether reality matches them.
- The subject is accounts that already drifted from their baseline. That is `drift-detection-reconciliation-desk`.
- The subject is closing an account or region. That is `cloud-decommissioning-desk`.

## Required evidence

- The current organization hierarchy export: root, organizational units, folders, or management groups, with the accounts, subscriptions, or projects placed under each.
- The account inventory with, per account, its purpose, owner, environment, and creation date, plus the accounts present in the inventory that appear in no hierarchy document.
- The existing policy set: organization-level deny policies, their attachment points, their enforcement mode, and the exemptions attached to each.
- Any adopted landing zone pattern or accelerator, its version, and the deviations already taken from it.
- The account vending path as it exists today: what creates an account, which identity does it, what it applies, and what a requester has to supply.
- Region enablement state per account, and any residency obligation from intake that has to be enforced by policy rather than by convention.
- Baseline service state per account: audit log destination, configuration recorder, threat detection, backup vault, cost and usage export, and default encryption settings, read from live configuration rather than from the baseline template.
- Billing and payer relationships, including which accounts consolidate under which agreement.

## Workflow

**Outcome.** A hierarchy with the isolation rationale stated at each boundary, an account separation model keyed to environment, sensitivity, and blast radius, a vending path with the day-one baseline it installs, a deny policy set with attachment point and enforcement mode per control, region enablement and restriction as enforced settings, and an honest statement of which accounts currently satisfy the baseline and which do not.

**Grounding.** The hierarchy is read from the organization export, never from the reference architecture the organization says it adopted. Baseline coverage is read from live per-account configuration, because a baseline that is applied at vending time and never reasserted degrades silently as accounts age. Where the hierarchy document and the organization export disagree about placement or policy attachment, record both with attribution and preserve the conflict; an account sitting in a different organizational unit than the design says is inheriting different denies than anyone believes.

**Constraints.** Every boundary in the hierarchy states what it isolates and why that isolation is worth an account, since a level that exists only to mirror the org chart adds policy surface without adding containment. Every deny policy names the control, its attachment point, its enforcement mode, its exemption path with owner and expiry, and the identities deliberately excluded from it, because a policy with no exemption for the paths that repair the estate is the one that turns a tightening into an outage nobody can fix. Region restriction is expressed as enforced policy where residency is an obligation, not as a naming convention. The baseline is stated as the set of services every account carries plus the evidence of current coverage, and an account that predates the baseline is recorded as non-conforming rather than assumed conforming. Shared accounts for logging, security tooling, networking, and backup are separated with their access direction stated, so the account holding the audit trail is not administered by the accounts it audits.

**Parallel surface.** Independent accounts, subscriptions, projects, organizational units, and baseline controls are independent assessment units and fan out safely, as does the per-account read of baseline coverage. The hierarchy shape itself, the organization-wide deny policy set, the region enablement decision, and the blast radius judgment run once after the fan-out returns, because a per-account view of guardrails cannot see the policy that is attached at the root and therefore applies to accounts nobody inspected.

**Ordered gate for attaching or widening an organization-level deny.** A deny attached above an account takes effect in every account beneath it the moment it lands, cannot be evaluated in advance by the teams it affects, and can remove the very permission needed to detach it. That is why this order is mandated and why step 4 is the point of no easy return:

1. Enumerate every account in scope of the intended attachment point and establish, from audit log evidence, which principals and actions the policy would have denied over a representative window.
2. Confirm the management, break-glass, and pipeline apply identities are explicitly exempt, and that the exemption itself does not depend on the permission being denied.
3. Attach in advisory or audit mode where the provider supports it, or at the narrowest organizational unit that proves the control, and reconcile the observed denials against the expected set.
4. Attach at the intended point in blocking mode, with the rollback trigger, the observation window, and the exemption request path stated before the change is applied.

Account closure, organizational unit deletion, and region disablement follow the destructive sequence in `references/suite-workflow-contract.md` instead of this one, and account closure is handled by `cloud-decommissioning-desk`.

**Acceptance bar.** A new account could be vended from these artifacts and would land in a defined organizational unit, inherit a named policy set, and come up with the full baseline, with no step left to tribal knowledge. Every boundary has a stated rationale, every deny has an attachment point and an exemption path, and baseline coverage is a measured statement rather than an assumption.

## Outputs

A complete run delivers this set:

- `organization-hierarchy.md`: the root, organizational unit, folder, or management group tree with the isolation rationale at each level and the placement rule that decides where a new workload lands.
- `account-separation-model.md`: separation by environment, sensitivity, and blast radius, the shared accounts for logging, security, networking, and backup with their access direction, and the naming and ownership conventions.
- `account-vending.md`: what creates an account, the identity that does it, the inputs a requester supplies, what is applied at creation, and how the baseline is reasserted afterward.
- `guardrail-policy-set.md`: each deny policy with its control, attachment point, enforcement mode, exemptions with owner and expiry, and the identities excluded so the estate stays repairable.
- `region-enablement.md`: enabled and restricted regions per scope, the residency obligation each restriction enforces, and the enforcement point.
- `account-baseline.md`: the day-one service set with the current coverage per account and the non-conforming accounts named.
- `landing-zone-downstream-handoff.md`: the boundaries and inherited policies `cloud-identity-access-desk` and `cloud-network-architecture-desk` must design within.

Depth standard: an artifact is complete when a platform engineer could vend an account and a security reviewer could confirm what it inherits, both without asking a follow-up question. A hierarchy level with no isolation rationale, a policy with no attachment point, and a baseline with no coverage evidence are unfinished rather than draft.

When the organization export, policy set, or per-account configuration exists and cannot be read, the run delivers `landing-zone-connector-diagnostic.md` naming each unreachable source and the structural claims that depend on it, in place of the artifacts that source would have grounded.

Anti-fabrication guard: the reference landing zone patterns are widely published and easy to reproduce from memory, which is exactly the trap at this stage. The failure mode is writing the tidy four-organizational-unit tree with the standard shared accounts because that is what a good landing zone looks like, when the export shows nineteen accounts hanging off the root with three deny policies attached to nothing. Hierarchy paths, account and subscription identifiers, policy names, and enforcement modes are transcribed from the export or left unresolved, and the estate is described in the shape it is in rather than in the shape the pattern recommends. A control that exists in a policy document and is attached at no point is recorded as authored and unattached, which is a different and more urgent finding than absent. Baseline coverage is stated as measured or unmeasured; an account is never described as conforming because the vending template would have made it so.

## infrastructure_packet fields to update

- `organization.hierarchy` with the full path per account, subscription, or project
- `organization.account_vending` with the creating identity and the inputs it requires
- `organization.guardrail_policies[]` with `control`, `mechanism`, `attachment_point`, `mode`, and `exception_ref`
- `organization.baseline_services` with per-account coverage state
- `providers[].accounts` and `providers[].regions`, source-backed only, plus `providers[].landing_zone_pattern`
- `blast_radius` reassessed against the attachment points this stage touches
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would attach or widen a deny policy in live accounts, move an account between organizational units, disable a region, change an enforcement mode from advisory to blocking, or close an account.
- **Missing approval**: an organization-level policy change, a hierarchy restructure, a region enablement, or a deviation from the adopted pattern needs a named owner who has not authorized it.
- **Security or privacy**: continuing would assert audit log delivery, threat detection coverage, encryption defaults, or residency enforcement as verified without live configuration evidence, or would place account identifiers, payer relationships, or policy contents where they should not be.
- **Source conflict**: the organization export, the landing zone documentation, and the policy inventory genuinely disagree about placement, attachment, or enforcement mode, and silently choosing one would publish an inheritance claim that does not hold.
- **Release integrity**: the baseline would be declared satisfied across the estate without per-account evidence, or a residency obligation declared enforced when only a naming convention implements it.
- **Connector unreachable**: the organization export, account inventory, policy set, or per-account configuration exists and cannot be read. An empty policy list and an unreadable one look identical and mean opposite things, so say which occurred.

Unknown account owners, undocumented historical accounts, and unstated placement intent for legacy workloads are soft gaps. Name them, label the assumption, and continue. Residency enforcement, audit log isolation, and approval requirements for organization-scoped change are never relaxed to keep a workflow moving.

## Downstream handoffs

`cloud-identity-access-desk` is next and needs the hierarchy, the attachment points of every deny, and the exempt identities, because an account-level grant that an organization-level deny overrides is a permission that silently does nothing. `cloud-network-architecture-desk` needs the account set and region enablement before any range is allocated, since the allocation register is keyed to accounts. `cloud-security-posture-desk` inherits the guardrail set as the control expectation it measures reality against. `tagging-inventory-desk` needs the account inventory and ownership state. `infrastructure-as-code-desk` needs the state boundaries the hierarchy implies. `cloud-decommissioning-desk` inherits the account closure path. Send organization-wide spend policy and payer structure negotiation to the FinOps suite as a labeled cross-suite handoff.

## Quality bar

Good landing zone work is legible at the boundary. Someone reading it can say what a given account is allowed to do, what it inherits and from where, and why the workload is in that account rather than the one next door. Policies are described where they are attached rather than where they were written, and the exemptions that keep the estate repairable are named rather than assumed. Baseline coverage is a number with a date on it. And the accounts that do not fit the model, the ones that predate it or were vended by hand, appear by name rather than being quietly excluded from the diagram, because those are the accounts the next incident comes from.
