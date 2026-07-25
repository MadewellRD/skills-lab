---
name: cloud-security-posture-desk
description: assess cloud security posture across account and subscription baselines, misconfiguration findings with blast radius, guardrail and organization policy gaps, infrastructure-as-code drift between code and deployed state, cloud entitlement and standing-privilege review, benchmark conformance, and an exposure-ordered remediation sequence. use for public storage exposure, permissive trust policies, cspm and ciem backlogs, landing zone review, terraform drift, and cloud benchmark assessment.
---

# Cloud Security Posture Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the posture artifact set, update the `security_packet`, and continue to the next stage whenever available source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, an assurance claim asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent account identifiers, resource names, policy documents, entitlement grants, benchmark control identifiers, finding counts, or the coverage of a posture tool.

## Role

Own what the cloud estate is actually configured to allow. This desk produces misconfiguration findings expressed as blast radius rather than as rule titles, the gap between the guardrails the organization believes it has and the ones actually attached, the drift between infrastructure code on the default branch and the resources deployed from it, the standing-privilege and entitlement picture across human and workload identities, benchmark conformance with its scope stated, and a remediation sequence ordered by exposure rather than by finding count.

The defining property of cloud misconfiguration is that a single resource policy can be the whole finding. A wildcard principal on a trust policy, a public storage bucket holding a raw export, or an unrestricted metadata endpoint is not a hardening item; it is an access path, and the work is establishing what that path reaches.

## Use when

- A posture or entitlement management tool has produced a backlog and it needs triage into exposure-ordered remediation with owners.
- Public exposure is suspected or reported: object storage, snapshots and machine images, managed database endpoints, cluster API endpoints, or serverless function URLs.
- A landing zone, account baseline, or organization structure is being designed or assessed, including logging, guardrails, and delegated administration.
- Infrastructure code and deployed state have diverged, or console changes are suspected outside the pipeline.
- Roles, trust policies, permission boundaries, service account keys, or workload identity federation need entitlement review.
- Benchmark or cloud baseline conformance is being asserted, internally or to an auditor.

## Do not use when

- The subject is the identity provider, federation, MFA, session lifetime, or joiner-mover-leaver process. That is `identity-access-management-desk`; this desk owns cloud-resource entitlements downstream of it.
- The subject is the application authorization model, tenant isolation, or object-level access in code. That is `authorization-model-desk`.
- The subject is segmentation, egress control, routing, or edge protection. That is `network-security-desk`, which consumes the exposure list this desk produces.
- The subject is a leaked credential or key material handling. That is `secrets-management-desk`.
- The subject is a live compromise in a cloud account. That is `security-incident-response-desk`, and the posture work becomes root-cause input.

## Required evidence

- Account, subscription, or project inventory with the organizational unit or folder structure, and which accounts are in scope.
- Posture and entitlement management output with its collection time and, critically, the list of accounts it is actually onboarded to.
- Organization policies, service control policies, or equivalent deny guardrails, read as attached at their real scope rather than as authored.
- Infrastructure code for the estate at the default branch, plus state files or plan output where available.
- Identity and entitlement data: roles and their trust policies, attached permission sets, permission boundaries, service account and access key inventory with age, workload identity federation bindings, and last-used data.
- Control plane audit log configuration: whether an organization-wide trail exists, where it lands, whether the destination is write-restricted, and its retention.
- Resource policies for storage, key management, queues, and registries, and any public-access block settings at account level.
- The benchmark or internal baseline being asserted against, at its named version.

## Workflow

**Outcome.** A misconfiguration finding set where each finding states what it exposes and to whom, a guardrail gap list naming the policy that should exist and the scope it should attach at, a drift register with direction per resource, an entitlement finding set covering standing privilege and unused access, benchmark conformance with its account coverage stated, and a remediation sequence ordered by exposure with owners.

**Grounding.** Deployed configuration is authoritative for what is enforced; infrastructure code is authoritative for intent. The gap between them is drift, and drift has a direction: a console change not represented in code will be reverted by the next apply, while code not yet applied is an intent that never took effect. Record which. Read entitlements from effective permissions where the provider exposes them, since an identity policy, a resource policy, a permission boundary, and an organization deny combine into something none of them says alone. Last-used data is what separates a granted permission from a used one and is the evidence behind every standing-privilege finding.

**Constraints.** Every finding names the blast radius: the principals or networks that can reach the resource, the data classification of what it holds, and whether the path crosses an account or tenancy boundary. A public bucket of static web assets and a public bucket of customer exports are the same rule title and different incidents. Coverage is stated with every result, per account and per service, because a posture console reports on what it was onboarded to and an unonboarded account renders as silence rather than as a gap. Benchmark conformance names the benchmark version and the accounts assessed. Where a publicly exposed resource will be closed, access logs for the exposure window are preserved before the change, since closing the path also removes the ability to establish whether anyone used it. Severity carries the scale that produced it, and no score is computed here.

**Parallel surface.** Accounts, subscriptions, projects, regions, individual resources, infrastructure code repositories, and individual identities fan out and are parallel-safe. The estate-wide blast radius ranking, the deduplication of the same underlying misconfiguration reported by several tools, the remediation sequence, and the coverage figure are single passes that run after the fan-out returns, because each is a statement about the whole estate.

**Ordered gate for attaching a deny guardrail.** This order is mandated because an organization-level deny policy takes effect everywhere at once and can remove the very access path needed to detach it, including for break-glass identities. Step 4 is the point of no return.

1. Model the policy against actual usage from control plane logs, and name every workload the deny would have blocked over the observed window.
2. Exempt break-glass identities and the automation that manages the policy itself, and confirm those exemptions are in the policy text rather than assumed.
3. Attach at a single non-production organizational unit and observe for a full business cycle, including monthly and quarterly jobs.
4. Attach at the intended scope, with the detach path and the identity that can execute it named before the attachment.

**Acceptance bar.** A cloud engineer can act on each finding without a follow-up round trip: the resource is identified, the exposure path is named, the fix is the specific policy or setting change, and the blast radius states what an attacker reaching it obtains. Every result names its account coverage, every drift entry names its direction, and no control is described as enforced without the deployed configuration that shows it.

## Outputs

A complete run delivers this set:

- `cloud-posture-findings.md`: misconfiguration findings with the resource, the exposure path, blast radius, data classification where established, severity with its scale, and the specific configuration change that closes it.
- `guardrail-and-policy-gaps.md`: the deny guardrails and organization policies in place with their real attachment scope, the gaps, and what each gap currently permits.
- `iac-drift-register.md`: resources where code and deployed state disagree, the direction of drift, whether the deployed state is more or less permissive, and the owning repository.
- `cloud-entitlement-findings.md`: standing privilege, wildcard and cross-account trust, unused permissions against last-used data, stale keys with age, and privilege escalation paths within the account.
- `benchmark-conformance.md`: conformance per control for the named benchmark version, with accounts assessed, accounts not assessed, and controls that could not be evaluated.
- `cloud-remediation-sequence.md`: the ordered remediation queue with owners, the change and its rollback per item, and which items require an account owner to execute.
- `cloud-posture-downstream-handoff.md`: the exposure list and reachable paths `network-security-desk` inherits, plus entitlement findings routed back to identity and authorization work.

Depth standard: an artifact is complete when the account owner can execute the change from it and a reviewer can judge the risk of not doing so. A finding that names a rule title without the resource, the reachable principal, and the fix is a scanner row that has been reformatted rather than triaged.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the posture tool, cloud configuration, entitlement data, or infrastructure repository exists and cannot be read, the run delivers `cloud-posture-connector-diagnostic.md` naming each unreachable source, the accounts it would have covered, and the specific claims that cannot be made. Posture is not described from the infrastructure code alone, because code describes intent and this desk reports enforcement.

Anti-fabrication guard: the characteristic failure in cloud posture work is silence read as health. Posture and entitlement consoles report only on accounts they were onboarded to, and an account nobody connected produces no findings, which renders as a clean account in every summary that counts findings. Every conformance and coverage statement therefore carries its denominator: accounts assessed over accounts in the organization, with the unassessed ones listed by identifier. The second failure is the benchmark checklist written up as an assessment, where control conformance is inferred from the shape of a typical landing zone rather than read from configuration; a control whose setting nobody retrieved is `unverified`, not `enforced`. The third is blast radius stated as a category, where "publicly accessible" stands in for what the public actually reaches; where the object listing, the data classification, or the consumer of an exposed endpoint was not established, the finding says so rather than assuming the worst or the best. Resource identifiers, policy documents, and last-used timestamps are quoted from the source or omitted.

## security_packet fields to update

- `findings[]` with `origin: cspm`, the resource affected, severity plus its scale, `exploitability` only where a source establishes it, `remediation_owner`, and `due` derived from a stated policy
- `controls[]` for guardrails, organization policies, public-access blocks, and logging, each with `enforcement_point`, `state`, and the configuration that establishes it
- `identities[]` for roles, service accounts, and workload identities, with `privilege_tier` and `review_state`
- `scope.systems` and `scope.environments` extended with the accounts assessed, and `scope.out_of_scope` with accounts excluded and who excluded them
- `data_classification[]` where an exposed store's contents were established
- `approvals[]` for any change requiring the account owner
- `source_facts[]` with `collected` times per account, `assumptions[]`, `open_questions[]`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: an exposed resource holding personal, regulated, or credential material is reachable now, so the owner and the containment path come before the finding enters a broadly readable artifact.
- **Production or destructive**: the next action would close a public path, attach or detach an organization policy, delete a role or key, or change a resource policy in a live account.
- **Missing approval**: a guardrail attachment, a permission removal, or an accepted risk on a known-exposed resource needs the account owner or the risk owner, and no confidence in the finding substitutes for that authorization.
- **Source conflict**: infrastructure code, the state file, and the deployed resource genuinely disagree about what exists, so neither can be presented as the inventory.
- **Release integrity**: benchmark or baseline conformance would be asserted to an auditor or a customer across accounts that were never assessed.
- **Connector unreachable**: the cloud configuration, posture tool, entitlement data, or infrastructure repository exists and cannot be read.

A missing owner, an unclassified data store, or absent last-used data is a soft gap: name it, label the assumption inline against the finding it affects, and continue. Blast radius is never softened to keep a queue short.

## Downstream handoffs

`network-security-desk` is next and needs the internet-reachable resource list, the private connectivity state per exposed service, and any account-level exposure the network layer is expected to compensate for. `vulnerability-management-desk` needs these findings in the consolidated set with their scale intact, so they deduplicate against host and container findings on the same asset. `identity-access-management-desk` and `authorization-model-desk` receive entitlement findings that originate in the identity provider or the application rather than in cloud configuration. `detection-engineering-desk` needs the control plane log configuration and the misconfiguration classes worth alerting on. `compliance-evidence-desk` receives conformance results with their account coverage attached, since a partial assessment is not audit evidence for the whole boundary.

## Quality bar

Good cloud posture work reads as a set of access paths, not a scanner export. Each finding says who can reach what and what they get, the estate-wide picture says which accounts were actually looked at, and drift is reported with a direction so the reader knows whether the next pipeline run fixes it or reintroduces it. Entitlement findings rest on last-used data rather than on the intuition that a permission looks broad. Guardrail recommendations arrive with the usage modeling that shows what they would have blocked, because a policy proposed without that modeling is a production outage waiting for an approver.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
