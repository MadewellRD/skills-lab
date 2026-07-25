---
name: cicd-platform-desk
description: design the ci/cd platform layer, covering reusable workflow and pipeline definitions, runner fleet sizing isolation and autoscaling, build and dependency cache strategy, artifact and container registry layout with retention and promotion by digest, dependency proxies and pull-through caches, supply-chain controls including provenance attestation signing and software bill of materials with their verification gates, build and queue performance targets, and the boundary between platform-owned and tenant-owned pipeline stages. use for shared pipeline design, runner fleet work, build cache and registry strategy, slsa and supply-chain hardening, ci queue performance, and pipeline ownership boundaries.
---

# CI/CD Platform Desk

## Suite workflow mode

This desk is a member of the Platform Engineering Command Desk suite. Complete the pipeline artifact set, update the `platform_packet`, and continue to the next stage whenever available source facts support it. The packet shape and continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent workflow references, runner counts or sizes, cache hit rates, registry paths, build durations, attestation coverage, or signing key locations.

## Role

Own the build and delivery substrate every tenant runs on. This desk defines the reusable workflows and pipeline definitions the platform publishes, the runner fleet and its isolation properties, cache and artifact strategy, registry and dependency proxy layout, the supply-chain controls and the gates that actually enforce them, build and queue performance targets, and the line between the pipeline stages the platform owns and the ones tenants own.

CI is the highest-privilege system most organizations run: it holds deploy credentials, it executes code from every repository, and it produces the artifacts that reach production. Treating it as developer tooling rather than as production infrastructure is the assumption behind most of the failures this desk exists to prevent.

## Use when

- Pipeline definitions have been copied across repositories and need consolidating into reusable workflows.
- The runner fleet needs sizing, autoscaling, isolation review, or a decision between hosted and self-hosted capacity.
- Build queue wait or build duration is a top friction item and the cache and fleet strategy need work.
- Registry layout, retention, garbage collection, or artifact promotion by digest needs designing.
- Upstream rate limits or outages break builds and a dependency proxy or pull-through cache is being introduced.
- Supply-chain controls are being introduced or audited: provenance, attestation, signing, bills of material, and the gates that verify them.
- The pipeline ownership boundary is unclear and tenants are editing stages the platform is accountable for.

## Do not use when

- The subject is the environment classes and promotion path the pipeline implements. That is `environment-management-desk`, whose gates this desk enforces.
- The subject is the generated pipeline file a new repository receives. That is `scaffolding-templates-desk`, which wires the call into the reusable workflow this desk publishes.
- The subject is the policy program with its waiver register and advisory-to-blocking rollout across all controls. That is `platform-guardrails-policy-desk`; this desk owns the pipeline enforcement point.
- The subject is a specific tenant's failing build or flaky test triage. That is the SDLC suite's CI failure work; label it as a cross-suite handoff.
- The subject is rolling a pipeline change to tenants in rings. That is `platform-change-rollout-desk`.

## Required evidence

- The reusable workflow and pipeline definitions the platform publishes, at their real versions and references, plus a sample of tenant pipelines that call them.
- Runner fleet configuration: hosted and self-hosted capacity, sizes and labels, autoscaling behavior, job-to-runner lifecycle, and whether runners are ephemeral per job.
- Runner privilege and trust settings: which events trigger runs from untrusted sources, the token and identity scope available to a job, and the isolation between concurrent jobs.
- Cache configuration: what is cached, the key scheme, scope and isolation between repositories or tenants, and measured hit rates where they exist.
- Registry and proxy layout: repositories and namespaces, retention and garbage collection policy, immutability settings, and promotion mechanics between registries or tags.
- Supply-chain configuration: what generates provenance, attestations, signatures, and bills of material, where each is stored, and which gate verifies them before an artifact runs.
- Build and queue telemetry: queue wait and duration distributions, concurrency limits, retry and flake rates, and their sources.
- The environment promotion path and gates from the upstream stage.

## Workflow

**Outcome.** A published reusable pipeline surface, a sized and isolated runner fleet, a cache and artifact strategy with registry and proxy layout, supply-chain controls each paired with the gate that enforces it, stated build and queue targets with their measurement source, and an explicit ownership boundary between platform-owned and tenant-owned stages.

**Grounding.** Read the pipeline surface from the workflow definitions and the tenant pipelines that call them, not from the CI documentation, since callers pin versions and the pinned set is the real surface. Read supply-chain state from both the producing step and the verifying gate, because those are separate facts and only the second one is a control. Where the documented pipeline standard and the tenant pipelines disagree, the disagreement is the finding.

**Constraints.** Every control names its enforcement point and whether it blocks, since a step that emits an attestation nobody checks is telemetry rather than a control. Runner isolation is stated against the untrusted-input case: what a job from a fork or an untrusted branch can reach, what credentials exist in its environment, and whether a compromised job affects the next job on that runner. Cache keys are scoped so that one repository cannot poison another's cache, and the isolation property is stated rather than assumed from the cache product. Artifacts are promoted by immutable digest rather than rebuilt or retagged, so the tested artifact is the deployed one. Dependencies and base images are pinned by digest, and actions or pipeline steps pulled from outside are pinned to an immutable reference. Performance targets are stated as distributions with their measurement source, because a mean build time hides the queue wait that developers actually experience. The ownership boundary states which stages tenants may modify, which are required and enforced, and what happens when a tenant needs an exception.

**Parallel surface.** Independent workflows, independent runner pools, independent registries and caches, independent supply-chain controls, and independent tenant pipeline scans fan out safely. The fleet capacity model, the aggregate supply-chain coverage figure, the cross-tenant cache and registry blast radius judgment, and the ownership boundary applied across the whole surface run once, after the fan-out returns.

**Ordered gate for rotating a signing key or trust root.** This order is mandated because verification and signing are two sides of one trust relationship: rotating the key before verifiers accept the new root makes every freshly built artifact unverifiable, and revoking the old root before existing artifacts are re-attested makes everything already deployed unverifiable. Step 4 is the point of no return.

1. Distribute the new trust root or public key to every verifying gate and confirm each accepts artifacts signed by it.
2. Begin signing with the new key while the old key remains trusted, so both are valid.
3. Re-sign or re-attest artifacts still in the deployable set under the new key.
4. Revoke trust in the old key and remove it, once no deployable artifact depends on it.

Runner fleet teardown and registry deletion follow the destructive sequence in `references/suite-workflow-contract.md`.

**Acceptance bar.** A tenant pipeline calls a published workflow, runs on an isolated runner, hits a warm cache, and produces a signed artifact with provenance that a deployment gate actually verifies before admitting it. Every control names its enforcement point and mode, the runner isolation statement covers the untrusted-input case, targets carry their measurement source, and the ownership boundary is specific enough to answer whether a given tenant edit is allowed.

## Outputs

A complete run delivers this set:

- `reusable-pipeline-surface.md`: the published workflows with versions, inputs, what each does, the version consumers are pinned to, and the compatibility expectation between versions.
- `runner-fleet-design.md`: pools, sizes, labels, scaling behavior, job lifecycle, cost profile, and the isolation properties of each pool including its behavior with untrusted input.
- `cache-and-artifact-strategy.md`: what is cached, key scheme and scope, isolation between tenants, measured or unmeasured hit rates, artifact retention, and promotion by digest.
- `registry-and-proxy-layout.md`: registries and namespaces, immutability and retention, garbage collection, dependency proxies and the upstream failures they absorb, and access scoping per tenant.
- `supply-chain-controls.md`: each control with what produces it, where it is stored, the gate that verifies it, whether that gate blocks, and the coverage across the fleet with the query behind the number.
- `build-performance-targets.md`: queue wait and duration distributions per pool and per workflow, the target, the current state with its source, and where the time goes.
- `pipeline-ownership-boundary.md`: platform-owned stages, tenant-owned stages, required and enforced stages, the exception path, and what a tenant may not override.
- `cicd-platform-downstream-handoff.md`: what `platform-guardrails-policy-desk` inherits, including which pipeline controls are advisory today and which block.

Depth standard: an artifact is complete when a platform engineer could implement the fleet and a security reviewer could assess the supply chain from the same set. A control listed without its verifying gate, or a runner pool described without its isolation behavior under untrusted input, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the workflow definitions, runner configuration, registry, or build telemetry exists and cannot be read, the run delivers `cicd-platform-connector-diagnostic.md` naming each unreachable source and the control and performance claims that depend on it. Supply-chain posture is not described from an unread pipeline.

Anti-fabrication guard: supply-chain claims fail here in a particular way. A pipeline that contains a step named for signing, attestation, or bill-of-material generation reads as a platform that has those controls, and the artifact writes them up as present, when the only question that matters is whether anything refuses an artifact that lacks them. Producing an attestation is telemetry; rejecting a deployment without one is a control. Each entry names the producing step and, separately, the verifying gate with its mode, and where no gate verifies, the control is recorded as produced-but-unenforced, which is the finding worth the whole run. Coverage percentages for signing, provenance, or bills of material name the query and the fleet scope behind them or are written as uncounted. Build and queue figures name their telemetry source and window, and cache hit rates come from the cache backend rather than from the expectation that caching is working. Runner isolation is asserted from configuration, since a pool assumed to be ephemeral and actually reused is the exact gap an attacker needs.

## platform_packet fields to update

- `pipeline_surface.reusable_workflows`, `pipeline_surface.runner_fleet`, `pipeline_surface.caches_and_registries`, `pipeline_surface.supply_chain_controls`, and `pipeline_surface.build_slo`
- `guardrails[]` for pipeline-enforced controls, each with `mode`, `enforcement_point`, and `exception_ref`
- `templates[].scaffolds` where generated pipelines pin a workflow version
- `devex_metrics` for build wait and pipeline duration, with measured value or unmeasured state and source
- `platform_slos` seeded for pipeline and registry availability where measurement exists
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Security or privacy**: runners execute untrusted code with access to deploy credentials or a shared cache, signing key material is held where a job can read it, or continuing would assert supply-chain integrity as enforced without gate evidence.
- **Production or destructive**: the next action would rotate a signing key or trust root, delete registry content or run garbage collection, drain or resize the live runner fleet, or change a required workflow that every tenant pipeline calls.
- **Missing approval**: changing a required stage, moving a supply-chain control from advisory to blocking, or altering artifact retention needs a named owner who has not authorized it.
- **Source conflict**: the workflow definitions, the tenant pipelines, and the registry contents genuinely disagree about what is built and deployed, so an artifact's provenance cannot be established without picking a story.
- **Release integrity**: an artifact would be promoted or declared trusted without provenance, signature, or bill-of-material evidence that a gate actually checks.
- **Connector unreachable**: the workflow definitions, runner configuration, registry, cache backend, or build telemetry exists and cannot be read.

Unmeasured cache hit rates, missing queue telemetry, and unknown per-pool cost are soft gaps. Name them and continue. Supply-chain and runner isolation boundaries are never relaxed to keep a workflow moving.

## Downstream handoffs

`platform-guardrails-policy-desk` is next and needs the pipeline enforcement points, each control's current mode, and the exception path, since the pipeline is where most guardrails land. `platform-observability-desk` needs the build and runner signals worth instrumenting. `platform-slo-reliability-desk` inherits the pipeline and registry availability objectives and the dependency on upstream registries. `platform-cost-attribution-desk` needs runner minutes, cache storage, and registry storage as allocation inputs. `platform-change-rollout-desk` inherits the workflow version pinning, since bumping a required workflow is a tenant-affecting change. Tenant-specific build failure triage and flaky test work go to the SDLC suite as a labeled cross-suite handoff.

## Quality bar

Good CI platform work treats the build system as production. Runners are ephemeral, and the artifact says what a job from an untrusted branch can reach rather than asserting that it cannot reach anything. Caches are fast and scoped so one tenant cannot poison another. Artifacts move by digest, so what shipped is what was tested and the provenance chain survives the promotion. Supply-chain controls are described by what they refuse, not by what they emit, and any control with no refusing gate is written up as unenforced. Build targets are distributions rather than averages, because the developer's experience is the queue wait at the tail, not the mean of a healthy afternoon.
