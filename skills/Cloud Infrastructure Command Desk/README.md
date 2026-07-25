# Cloud Infrastructure Command Desk

Source Markdown suite for the cloud estate. The subject is the substrate itself: the organization and account hierarchy, the address space, the identity model, the compute and data services, the code that provisions all of it, the pipeline that applies that code, and the live resources that result.

The applications running on top belong to their teams and to other suites. This suite owns the ground they land on, and it treats declared state and live state as two separate sources whose disagreement is the finding.

## Desks in workflow order

- `cloud-infrastructure-command-desk.md` (orchestrator)
- `cloud-workload-intake-desk.md`
- `landing-zone-account-structure-desk.md`
- `cloud-identity-access-desk.md`
- `cloud-network-architecture-desk.md`
- `hybrid-connectivity-dns-desk.md`
- `compute-platform-desk.md`
- `container-platform-desk.md`
- `cloud-storage-data-services-desk.md`
- `managed-database-platform-desk.md`
- `resilience-multi-region-desk.md`
- `infrastructure-as-code-desk.md`
- `provisioning-pipeline-desk.md`
- `configuration-secrets-desk.md`
- `cloud-security-posture-desk.md`
- `tagging-inventory-desk.md`
- `cloud-cost-rightsizing-desk.md`
- `drift-detection-reconciliation-desk.md`
- `cloud-migration-desk.md`
- `cloud-decommissioning-desk.md`

## Workflow backbone

```text
workload intake
  -> landing zone and account structure
  -> cloud identity and access
  -> network architecture
  -> hybrid connectivity and dns
  -> compute platform
  -> container platform
  -> storage and data services
  -> managed database platform
  -> resilience and multi-region
  -> infrastructure as code
  -> provisioning pipeline
  -> configuration and secrets
  -> cloud security posture
  -> tagging and inventory
  -> cost and rightsizing
  -> drift detection and reconciliation
  -> cloud migration
  -> decommissioning
```

The chain is ordered by packet dependency, not by calendar. Network design needs the account boundaries, cost allocation needs the tag coverage, and a migration wave needs a landing zone to land in. Few workflows need every stage: a rightsizing review does not need a landing zone stage, and a new account baseline does not need a migration wave plan. The orchestrator selects the stage path, carries the `infrastructure_packet`, and records every skip with its reason.

## How to start

Ask the command desk for the outcome, not the stage. Name the surface, the accounts and regions affected, whether the change is greenfield, hardening, remediation, rightsizing, migration, or teardown, and whether it reaches production. The orchestrator classifies the request, starts at the earliest desk whose inputs are satisfied, and continues through the stages the outcome needs.

Examples: "design the landing zone and address plan for our second region and tell me what collides with what we already have", "our bill jumped forty percent last month and nobody can say whose it is", "reconcile what the code says against what is actually running in the production accounts", "move these twelve workloads off the old estate in waves without a big-bang cutover", "retire the legacy account and prove the spend actually stopped".

## Suite references

- `references/suite-workflow-contract.md`: continuity rule, operating modes, the full `infrastructure_packet` field set, declared-versus-live source discipline, the destructive-action sequence, halt format, parallel surface, and cross-suite boundaries.
- `references/stage-contracts.md`: per-desk inputs, owned outputs, and handoff target.

Shared halt classes and capability assumptions come from the kernel references, `halt-taxonomy.md` and `capability-baseline.md`.
