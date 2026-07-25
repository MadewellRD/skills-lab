---
name: environment-management-desk
description: define environment classes and topology for a platform, covering ephemeral and per-pull-request preview provisioning, the promotion path and artifact immutability between classes, environment-scoped configuration and secrets, test-data seeding with masking and subsetting, lifetime leases reclamation and sprawl control, and the documented parity gaps between each lower environment and production. use for environment strategy, preview environments, staging parity, promotion pipelines, test data management, environment sprawl and idle cost, and environment-as-a-service design.
---

# Environment Management Desk

## Suite workflow mode

This desk is a member of the Platform Engineering Command Desk suite. Complete the environment artifact set, update the `platform_packet`, and continue to the next stage whenever available source facts support it. The packet shape and continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent environment names, cluster or account identifiers, lifetimes, reclamation figures, masking coverage, data volumes, or parity claims.

## Role

Own the ladder a change climbs from a developer's laptop to production, and the honest description of where each rung differs from the top. This desk defines environment classes and topology, how ephemeral and preview environments are provisioned and reclaimed, the promotion path and what is allowed to change between classes, environment-scoped configuration and secrets, how test data is seeded and masked, lifetime and reclamation rules, and the parity gaps between each lower environment and production.

Every environment below production is a deliberate approximation. The value of this desk is naming which approximations were chosen and what class of bug each one lets through, because an undocumented parity gap is found during an incident and attributed to bad luck.

## Use when

- Environment classes are undefined, or a class has accreted that nobody can explain the purpose of.
- Preview or per-pull-request environments are being introduced, or existing ones are slow, flaky, or never reclaimed.
- The promotion path rebuilds artifacts per environment and the tested artifact is not the shipped one.
- Staging is trusted more than its parity supports, or a class of production failure keeps passing staging cleanly.
- Test data is stale, insufficient, or sourced from production without a masking design.
- Environment sprawl is generating idle cost and lease and reclamation rules need setting.
- Environment configuration and secrets have leaked across class boundaries.

## Do not use when

- The subject is the provisioning modules and reconciliation path that create environment infrastructure. That is `self-service-infrastructure-desk`, whose abstractions this desk composes into classes.
- The subject is the tenancy boundary between teams rather than the boundary between environment classes. That is `tenancy-isolation-desk`.
- The subject is the pipeline that performs the promotion. That is `cicd-platform-desk`; this desk defines the path and its gates, that desk builds the mechanism.
- The subject is rolling a platform change across tenants in rings. That is `platform-change-rollout-desk`.
- The subject is cost allocation of environment spend to tenants. That is `platform-cost-attribution-desk`, which consumes the reclamation rules this desk sets.

## Required evidence

- The current environment inventory with class, topology, owner, and the infrastructure source that defines each.
- Promotion mechanics from pipeline definitions: what is built, what is promoted, whether the artifact digest is preserved across classes, and what is rebuilt.
- Configuration and secret sources per class, including which store, which key material, and whether any value is shared across a class boundary.
- Test data sources and their current handling: seeding jobs, refresh cadence, masking or subsetting logic, and the legal basis under which any production-derived data is used.
- Lifetime and reclamation evidence: environments currently running, their age, their last activity, and any existing lease mechanism.
- Parity evidence per dimension: infrastructure definitions for each class, data volume, traffic profile, third-party integration mode, identity and access configuration, feature flag state, and network topology.
- Provisioning latency for ephemeral and preview environments from pipeline or controller records.
- The tenancy model and infrastructure abstractions from upstream stages.

## Workflow

**Outcome.** Defined environment classes with their purpose, topology, and lifetime; a provisioning path for ephemeral and preview environments with a stated wait expectation; a promotion path with artifact immutability and the gates between classes; a test-data design with masking and refresh; reclamation rules that hold without human intervention; and a parity register naming what differs from production per class and what that difference lets through.

**Grounding.** Read environment topology from the infrastructure sources that define each class rather than from a diagram, and read promotion behavior from the pipeline definitions rather than from the release document. Parity is established by comparing definitions dimension by dimension; where the two classes are described as equivalent and their definitions differ, the difference is the finding.

**Constraints.** The artifact that reaches production is the artifact that was tested, identified by digest, with only configuration differing between classes. Every class states its purpose and what decision it exists to inform, because a class that informs no decision is cost with a hostname. Ephemeral environments carry a lease and are reclaimed by the mechanism rather than by a reminder, since reclamation that depends on human discipline produces the sprawl it was meant to prevent. Secrets and key material are scoped per class with no value shared upward or downward, because a lower environment is a lower trust boundary by definition. Test data is fit for the decision the class informs, and volume, distribution, and referential integrity are stated rather than assumed adequate. Every parity gap names the class of defect it allows through, which is what converts a list of differences into an input for test strategy.

**Parallel surface.** Independent environment classes, independent parity dimensions, independent seeding datasets, and independent reclamation scans fan out safely. The promotion path itself is sequential by construction and is not parallelized; the cross-class parity judgment, the aggregate sprawl and idle-cost picture, and the decision about which gaps to close run once, after the fan-out returns.

**Ordered gate for seeding a lower environment from production data.** This order is mandated by privacy obligation and by the fact that step 4 cannot be undone: once identifiable data has landed in a lower-trust environment, every consumer of that environment has already seen it and deleting the copy does not retract the exposure.

1. Establish the legal basis, the data classes in scope, and the retention limit for the copy, with a named approver.
2. Subset and mask or synthesize in a controlled environment at the source trust level, preserving referential integrity within the subset.
3. Confirm the transformed dataset against the identifiable-field inventory that the masking was specified to cover.
4. Load into the target environment, with the retention and re-refresh schedule already in force.

**Acceptance bar.** A developer opens a pull request and receives a working preview inside the stated wait, promotion carries the same artifact digest to production, no lower environment holds identifiable production data outside an approved and masked path, unused environments disappear on their own, and every class carries a parity register naming what it cannot catch.

## Outputs

A complete run delivers this set:

- `environment-classes.md`: each class with purpose, the decision it informs, topology, owner, lifetime, and its access boundary.
- `ephemeral-environment-design.md`: how preview environments are created and torn down, what they include and deliberately exclude, their wait expectation with its measurement source, and their concurrency limits.
- `promotion-path.md`: the ordered class sequence, what is immutable across it, what changes per class, the gate at each transition, and the rollback boundary.
- `environment-config-and-secrets.md`: configuration and secret sourcing per class, the scoping rule, and any value currently shared across a boundary with the remediation for it.
- `test-data-strategy.md`: data sources per class, subsetting and masking or synthesis design, refresh cadence, retention, and the fields the masking is specified to cover.
- `lifetime-and-reclamation.md`: lease durations, the reclamation mechanism, exemptions with expiry, and the current inventory of environments past their lease.
- `production-parity-register.md`: per class and per dimension, the difference from production and the defect class it allows through.
- `environment-downstream-handoff.md`: what `cicd-platform-desk` inherits, including the promotion gates the pipeline must implement.

Depth standard: an artifact is complete when a release engineer could implement the promotion path and a test lead could plan coverage around the parity register from the same set. A class entry with no stated purpose, or a parity gap with no defect class attached, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the environment inventory, pipeline definitions, configuration stores, or seeding jobs exist and cannot be read, the run delivers `environment-connector-diagnostic.md` naming each unreachable source and the parity and promotion claims that depend on it. Parity is never described from an unread environment definition.

Anti-fabrication guard: the phrase "staging mirrors production" is the fabrication this desk exists to prevent. It is almost never true, it is repeated because everyone assumes someone confirmed it, and it costs an outage the first time a defect class it was supposed to catch reaches production. Parity is asserted per dimension against compared definitions, and any dimension not compared is listed as parity-unknown rather than folded into a general statement of similarity. Masking coverage is claimed only against a named identifiable-field inventory, since coverage claimed against an unenumerated set of fields is a privacy incident with paperwork attached. Environment counts, idle spend, reclamation rates, and preview provisioning times name the inventory query, cost export, or pipeline records behind them or are written as uncounted, and a lease is quoted from the configured mechanism rather than from the intended policy, because the difference between the two is precisely the sprawl the report is meant to surface.

## platform_packet fields to update

- `environments[]` with `name`, `class`, `provisioning`, `lifetime`, and `parity_gaps`
- `devex_metrics` for preview provisioning wait and time to first deploy, with measured value or unmeasured state and source
- `tenancy.isolation_controls` where an environment class boundary carries its own controls
- `guardrails[]` for promotion gates enforced at a pipeline or provisioning point
- `cost_model.allocation_keys` where environment class becomes an allocation dimension
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: production data would move into a lower-trust environment without an approved masking or synthesis path, secrets or key material would cross a class boundary, or the identifiable-field inventory that masking is specified against does not exist.
- **Production or destructive**: the next action would reclaim, delete, or reconfigure a live environment, drop or refresh a dataset in use, or change promotion gates on the production path.
- **Missing approval**: using production-derived data in a lower class, shortening a promotion gate, or reclaiming an environment a team is relying on needs a named owner who has not authorized it.
- **Source conflict**: the environment definitions, the pipeline configuration, and the inventory genuinely disagree about what a class contains or how promotion works, and choosing one silently would publish a promotion path that does not exist.
- **Release integrity**: a class would be presented as a production-parity gate when the artifact it validates is rebuilt rather than promoted, so the tested artifact is not the shipped one.
- **Connector unreachable**: the environment inventory, pipeline definitions, configuration store, or seeding job definitions exist and cannot be read.

Unmeasured preview wait times, unknown idle spend, and undocumented historical class purposes are soft gaps. Name them and continue. Data-handling and secret-scoping boundaries are never relaxed to keep a workflow moving.

## Downstream handoffs

`cicd-platform-desk` is next and needs the class sequence, the promotion gates, and the artifact immutability rule, since the pipeline is where all three are enforced. `platform-cost-attribution-desk` inherits the reclamation rules and the environment class allocation dimension. `platform-observability-desk` needs which classes are instrumented and which are blind. `platform-guardrails-policy-desk` inherits the promotion gates as policy rules. The parity register goes to the SDLC suite's test strategy work as a labeled cross-suite handoff, because the defect classes a lower environment cannot catch are test coverage requirements rather than platform defects.

## Quality bar

Good environment work is honest about approximation. Each class says what decision it informs and what it cannot tell you. Promotion moves an artifact rather than rebuilding one, so the thing that passed the gate is the thing that ships. Preview environments arrive fast enough that developers use them instead of testing in a shared integration environment, and they disappear without anyone remembering to remove them. Test data is fit for the decision rather than merely present. The parity register is specific enough to be actionable: not "staging has less data" but the data volume, the resulting defect class, and where that class is caught instead.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
