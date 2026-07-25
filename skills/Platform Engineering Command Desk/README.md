# Platform Engineering Command Desk

Source Markdown suite for the internal developer platform. The subject is the paved road itself: what the platform offers, what it hides, who consumes it, what it costs, how reliable it is, how teams get onto it, and how capabilities are retired without stranding anyone.

Tenant workloads running on top of the platform belong to their own teams and to other suites. This suite owns the platform as a product.

## Desks in workflow order

- `platform-engineering-command-desk.md` (orchestrator)
- `platform-product-intake-desk.md`
- `developer-experience-research-desk.md`
- `golden-path-design-desk.md`
- `service-catalog-desk.md`
- `platform-api-contract-desk.md`
- `tenancy-isolation-desk.md`
- `self-service-infrastructure-desk.md`
- `scaffolding-templates-desk.md`
- `environment-management-desk.md`
- `cicd-platform-desk.md`
- `platform-guardrails-policy-desk.md`
- `platform-observability-desk.md`
- `platform-slo-reliability-desk.md`
- `platform-cost-attribution-desk.md`
- `platform-change-rollout-desk.md`
- `platform-adoption-migration-desk.md`
- `platform-support-operations-desk.md`
- `platform-governance-desk.md`
- `platform-deprecation-sunset-desk.md`

## Workflow backbone

```text
product intake
  -> developer experience research
  -> golden path design
  -> service catalog
  -> platform api contract
  -> tenancy and isolation
  -> self-service infrastructure
  -> scaffolding and templates
  -> environment management
  -> ci/cd platform
  -> guardrails and policy
  -> platform observability
  -> platform slos
  -> cost attribution
  -> change rollout
  -> adoption and migration
  -> support operations
  -> governance
  -> deprecation and sunset
```

The chain is ordered by packet dependency, not by calendar. Few workflows need every stage: a template refresh does not need a chargeback stage, and a cost allocation redesign does not need a scaffolding stage. The orchestrator selects the stage path, carries the `platform_packet`, and records every skip with its reason.

## How to start

Ask the command desk for the outcome, not the stage. Name the platform surface, the tenants affected, and whether the change is new, hardening, consolidating, tightening enforcement, or removing something. The orchestrator classifies the request, starts at the earliest desk whose inputs are satisfied, and continues through the stages the outcome needs.

Examples: "define a paved road for our Go services and tell me what is missing to actually back it", "we are moving from showback to chargeback next quarter, plan it", "our preview environments take 40 minutes to provision, find where the time goes", "retire the legacy deploy pipeline without stranding the teams still on it".

## Suite references

- `references/suite-workflow-contract.md`: continuity rule, operating modes, the full `platform_packet` field set, source discipline, halt format, parallel surface, and cross-suite boundaries.
- `references/stage-contracts.md`: per-desk inputs, owned outputs, and handoff target.

Shared halt classes and capability assumptions come from the kernel references, `halt-taxonomy.md` and `capability-baseline.md`.
