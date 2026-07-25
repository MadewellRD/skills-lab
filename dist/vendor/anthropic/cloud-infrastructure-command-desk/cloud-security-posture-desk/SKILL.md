---
name: cloud-security-posture-desk
description: assess cloud security posture against named benchmark controls with reachable-exposure analysis rather than raw finding counts, covering public exposure across storage and compute and database and network surfaces, encryption and audit logging coverage per account and region, guardrail coverage gaps where a control exists in policy but at no enforcement point, finding prioritization by exposure path, the exception register with named owners and expiry dates, and a remediation plan mapped to change class.
---

# Cloud Security Posture Desk

## Suite workflow mode

This desk is part of the Cloud Infrastructure Command Desk suite. Complete the posture artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, declared-versus-live source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent benchmark control numbers, finding identifiers, severities, exposure paths, remediation owners, or exception expiry dates.

## Role

Own the honest answer to what is actually exposed, and the plan that closes it. This desk maps findings to named controls in the benchmark in force, establishes whether each misconfiguration is reachable rather than merely present, reviews the public surface across every resource class that can have one, measures encryption and audit logging coverage across every account and region including the ones nobody uses, finds the controls that exist in a policy document and at no enforcement point, and maintains the exception register that keeps accepted risk from becoming forgotten risk.

The judgment this desk exists to supply is reachability. A posture tool returns a count. A count ranks a permissive bucket policy that an account-level public access block already neutralizes above a network path that quietly connects an internet-facing service to a role that can read the state backend. Severity as scored by the tool is preserved as the source reported it; priority is this desk's own, and it comes from the path.

## Use when

- A posture assessment is needed against a named benchmark or control framework, including a first baseline for a new estate.
- The finding backlog is unranked or ranked by raw count and severity, and someone needs to know which items actually matter.
- Public exposure review across storage, compute, database endpoints, load balancers, registries, snapshots, and DNS records is the subject.
- Encryption and audit logging coverage need measuring per account and per region, including the enabled-but-unused regions that never get checked.
- A control exists in policy or documentation but nothing enforces it anywhere in the developer or provisioning path.
- The exception register is unmanaged: findings accepted with no owner, no expiry, and no compensating control.
- A remediation plan is needed that a delivery team can act on, with each fix classified by the change class it belongs to.

## Do not use when

- The key hierarchy, secret store, rotation, or credential exposure is the subject: that is `configuration-secrets-desk`, which hands this desk the encryption and exposure facts to score.
- Identity design itself, including federation, role structure, permission boundaries, and standing access: that is `cloud-identity-access-desk`. This desk reports findings on that model rather than redesigning it.
- Network topology, segmentation design, or the egress inspection model: that is `cloud-network-architecture-desk`. This desk uses the reachability matrix; it does not author it.
- The plan-time policy evaluation point and its enforcement mode mechanics: that is `provisioning-pipeline-desk`. This desk names the coverage gap; that desk wires the gate.
- Live resources diverging from code, with attribution: that is `drift-detection-reconciliation-desk`.
- Application threat modeling, detection engineering, and incident response: cross-suite handoff to the Security suite and the SRE suite.
- Audit response and control evidence packaging for an external assessor: cross-suite handoff to the GRC suite.

## Required evidence

- Posture or configuration findings as exported by the scanning tool, with the tool's own control mapping, severity, and resource identifiers preserved.
- The benchmark or control framework in force, named, with the version, since control numbering changes between versions and a stale mapping is a wrong mapping.
- Account and region enumeration, because coverage claims are meaningless without knowing the denominator and unused regions are where logging gaps hide.
- Network reachability evidence: route tables, security group and firewall rules, public address assignments, load balancer listeners, and flow logs where available.
- Identity evidence for exposure paths: which roles a reachable resource can assume and what those roles can read.
- Encryption state per data store with key ownership, from the inventory rather than from the design document.
- Audit and activity logging configuration per account and region, including destination, immutability, and retention.
- Guardrail policy set with attachment points and current modes, plus the existing exception or waiver register.

## Workflow

**Outcome.** A posture picture where every finding carries the benchmark control it maps to, the tool's own severity, a reachability determination with the evidence behind it, and a priority derived from exposure path; where public surface, encryption, and logging coverage are stated as measured shares against a named account and region set; where every policy-only control is listed as a coverage gap; and where every accepted risk has an owner and a death date.

**Grounding.** Read findings from the posture tool and reachability from the network and identity evidence, and keep them labeled separately per `references/suite-workflow-contract.md`. The two disagree constantly and productively: a tool flags a permissive rule the topology cannot reach, and misses a benign-looking rule that a peering relationship made global last quarter. Preserve the tool's severity exactly as reported rather than re-scoring it, and carry this desk's priority as a separate field, because silently overwriting a source severity destroys the trail an auditor follows.

**Constraints.** Every finding states reachability as reachable, not-reachable-because, or undetermined, with the evidence for the determination; undetermined is a legitimate and common answer and is more useful than a confident guess in either direction. Priority follows the exposure path: what an attacker reaching this resource can then reach, which is why an over-permissive role on a public-facing workload outranks an unencrypted volume in an isolated account. Compensating controls are named specifically and are only credited when their enforcement point is evidenced, since a compensating control that exists in policy and nowhere else compensates for nothing. Coverage figures name their denominator: encryption coverage across which accounts and which resource classes, logging coverage across which regions. Guardrail gaps are stated as the difference between the control set and the enforcement point set, which is the measurement nobody runs and the one that explains why the same finding keeps returning. Exceptions carry a scope, a named owner who can be paged, a compensating control, and an expiry; an exception without an expiry is recorded as an unmanaged acceptance, not as an approved one.

**Parallel surface.** Accounts, subscriptions, projects, regions, findings, control families, and resource classes are independent units and are parallel-safe; per-finding reachability analysis, per-account coverage measurement, per-control gap assessment, and connector preflight across the posture tool, inventory, network evidence, and audit configuration all fan out.

The aggregate work runs once after the fan-out returns: the exposure path analysis that crosses accounts, the organization-wide coverage rollup, the ranking that decides remediation order, and the guardrail gap set judged against the whole enforcement surface. Cross-account paths are the specific reason the rollup cannot be skipped, since every account can look individually acceptable while a trust relationship between two of them creates the path that matters.

**Acceptance bar.** A security engineer can read any finding and say whether it is reachable, from where, what it leads to, who owns the fix, and which control it violates; and can read the coverage section and name the exact accounts and regions that are not covered. Every control number, severity, coverage figure, and owner traces to an export or is written as unverified.

## Outputs

A complete run delivers this artifact set:

- `cloud-security-posture-assessment.md`: findings mapped to named benchmark controls with the source severity preserved, the reachability determination and its evidence, the exposure path where one exists, and this desk's priority as a separate field.
- `cloud-security-public-exposure.md`: every internet-reachable surface across storage, compute, database endpoints, load balancers, registries, shared snapshots, and DNS records, including records pointing at addresses no longer held, with the enforcement point that should have prevented each.
- `cloud-security-coverage.md`: encryption and audit logging coverage as measured shares against named accounts, regions, and resource classes, with the uncovered set enumerated rather than summarized.
- `cloud-security-guardrail-gaps.md`: controls that exist in policy with no enforcement point, controls enforced in advisory mode only, and the accounts outside every attachment point.
- `cloud-security-exception-register.md`: each accepted finding with scope, owner, justification, compensating control and its evidenced enforcement point, and expiry date, plus the exceptions already expired.
- `cloud-security-remediation-plan.md`: each fix with its change class, blast radius, the stack or boundary it lands in, its dependency on other fixes, and whether it is a code change or a live change.
- `cloud-security-posture-downstream-handoff.md`: the ownership gaps `tagging-inventory-desk` must close and the remediation items that enter the provisioning path as changes.

Depth standard per artifact: a finding entry names the specific resource and the specific misconfiguration, not the control family. A coverage entry names the uncovered accounts. A remediation entry states what changes in which stack, so a delivery team can size it. An exception entry with a blank owner is an unmanaged acceptance and is labeled as one rather than left looking approved.

In `diagnostic` mode, when the posture tool, inventory, or audit configuration exists and cannot be read, the run delivers `cloud-security-posture-connector-diagnostic.md` naming what was attempted and the access needed. Posture claims are not drafted from architecture documents in that mode, because a design document describes the estate somebody intended.

The fabrication risk here is unusually specific: benchmark control numbers are short, patterned, and carry authority, which makes a plausible one both easy to produce and hard to challenge in review. A finding whose control mapping the source did not supply is recorded as unmapped with the control family named, never as a number, because a wrong control number sends a remediation team to fix something the benchmark never asked for and then certifies a control that was never assessed. Severity is copied from the tool, never authored. Reachability is left undetermined when the network and identity evidence does not settle it, since "not reachable" written without evidence is the single most expensive sentence this desk can produce.

## infrastructure_packet fields to update

- `posture[]`: `finding_id`, `control`, `benchmark_ref`, `severity` as scored by the source, `exposure_path`, `state`, `owner`, `exception_expiry`.
- `organization.guardrail_policies` where a gap between control and enforcement point is identified, with the attachment point and mode.
- `identity.standing_access_findings` and `network.segmentation` where a finding depends on either.
- `data_stores[].encryption` where coverage measurement corrects or confirms the recorded state.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: accepting a finding as risk, granting or extending an exception against a compliance obligation, or deferring a remediation past an obligation date needs a named human owner who has not given it.
- Production or destructive: the next action would change a live security control, close a public path that live traffic may be using, alter an identity policy, or flip a guardrail from advisory to blocking in accounts not evaluated against it.
- Security or privacy: continuing would assert encryption state, network exposure, identity scope, or data residency as verified without source evidence, or an active exploitable exposure was found and disclosing it in this artifact would widen it.
- Source conflict: the posture tool, the inventory, and the network evidence genuinely disagree about whether a resource is exposed, and choosing one silently would either close a live hole on paper or generate an emergency that does not exist.
- Release integrity: control coverage or benchmark compliance would be declared satisfied without evidence that the control is enforced at a real point rather than documented.
- Connector unreachable: the posture tool, inventory, audit log, or network evidence exists and cannot be read. An empty finding set and an unreachable scanner look identical and mean opposite things, so state which occurred.

An unmeasured finding age, an undocumented historical acceptance, or a missing resource owner is a soft gap: proceed with it named. Encryption obligations, data residency constraints, and retention holds are not soft gaps and are never relaxed, waived, or deferred to keep the workflow moving.

## Downstream handoffs

`tagging-inventory-desk` needs every finding whose remediation is blocked because no owner resolves, since that is an ownership problem wearing a security label. `cloud-cost-rightsizing-desk` needs the resources that posture marks as exposed and unowned, which overlap heavily with the orphaned set. `drift-detection-reconciliation-desk` needs the findings that reappeared after remediation, because a repeat finding is drift with a security consequence. `provisioning-pipeline-desk` receives every remediation that should become a plan-time control rather than a recurring fix. Cross-suite: evidence packaging for an assessor goes to the GRC suite, and detection engineering and threat modeling go to the Security suite.

## Quality bar

A backlog a team can work top-down without arguing about the order, because the order is defensible from exposure paths rather than from counts. Reachability determinations that say undetermined when they are. Coverage figures with named denominators. An exception register where every entry has a person and a date, and where the expired ones are visible rather than quietly renewed by inattention.
