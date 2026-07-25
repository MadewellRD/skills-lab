---
name: platform-api-contract-desk
description: define the platform's own interface contracts, covering resource schemas and custom resource definitions, api groups and versioning, stability labels from alpha through beta to stable, backward-compatibility guarantees and what counts as additive versus breaking, the deprecation window and notice policy, cli and portal action surface, and the abstraction boundary between what the platform hides and what it deliberately exposes. use for platform api design, crd and resource claim schemas, schema versioning, breaking-change policy, leaky abstraction reviews, and platform client surface decisions.
---

# Platform API Contract Desk

## Suite workflow mode

This desk is a member of the Platform Engineering Command Desk suite. Complete the contract artifact set, update the `platform_packet`, and continue to the next stage whenever available source facts support it. The packet shape and continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent schema fields, API versions, stored versions, stability labels, support windows, deprecation dates, or consumer counts.

## Role

Treat the platform's interface as a published API with consumers who wrote code against it. This desk owns resource schemas and custom resource definitions, API groups and versioning, the stability label attached to each surface, the compatibility guarantee a consumer may rely on, the notice policy and window that governs breaking changes, the client and portal action surface, and the abstraction boundary that decides what the platform hides and what it deliberately exposes.

The interface is the platform's real product. Everything behind it can be rewritten; the schema cannot, because tenant repositories, pipelines, and reconcilers are all written against it. An abstraction that hides the wrong thing forces every tenant into an escape hatch, and an abstraction that exposes too much freezes the implementation underneath it.

## Use when

- A new resource schema, custom resource definition, resource claim, or workload specification is being designed or revised.
- The stability label of an existing surface needs setting or promoting, and consumers need to know what promotion buys them.
- A change is proposed and its additive-versus-breaking classification decides whether a notice window applies.
- Consumers are reaching past the abstraction into the implementation, and the boundary needs redrawing or an extension point needs adding.
- A deprecation window and notice policy do not exist and breaking changes are landing without one.
- The CLI verbs and portal actions have diverged from the resource model and the client surface needs reconciling.

## Do not use when

- The subject is the catalog's entity model rather than the platform's resource schemas. That is `service-catalog-desk`.
- The subject is the infrastructure modules and compositions behind the schema rather than the schema itself. That is `self-service-infrastructure-desk`.
- The change has a contract already and the work is rolling it to tenants in rings. That is `platform-change-rollout-desk`, which consumes the compatibility classification this desk produces.
- The capability behind the interface is being retired outright. That is `platform-deprecation-sunset-desk`.
- The subject is the tenancy boundary the API operates within. That is `tenancy-isolation-desk`.

## Required evidence

- The current schema sources: custom resource definitions, composite resource definitions, chart value schemas, workload specifications, and API definitions, at the versions actually served.
- The stored version and conversion configuration for every served version, plus the count of objects persisted at each version.
- Consumer usage evidence: repositories referencing each field, pipeline invocations, API audit or request logs by version, and controller reconcile activity.
- Existing deprecation policy, notice history, and any published compatibility statement.
- The golden path definitions and catalog entity kinds from upstream stages.
- Escape-hatch and override usage in tenant manifests, which shows where the abstraction is failing in practice.
- The client surface: CLI verbs, portal actions, and any generated SDK, with their versions.

## Workflow

**Outcome.** A published contract per surface: schema with field-level semantics, version and stability label, the compatibility guarantee a consumer may rely on, the breaking-change notice window, the client surface that exercises it, and a stated abstraction boundary listing what is hidden and what is deliberately exposed.

**Grounding.** Read the schema from the served definitions rather than from the documentation, because documented fields and served fields diverge quickly. Read consumer reliance from actual usage evidence rather than from intent, since a field nobody uses and a field one critical tenant depends on look identical in a schema. Where the published policy and the change history disagree about whether the window was honored, record both.

**Constraints.** Every field carries its semantics, defaulting behavior, mutability, and validation, because a field's default is part of the contract and changing it silently mutates existing resources on the next reconcile. Classification is explicit: adding an optional field with a safe default is additive, while narrowing validation, tightening an enum, changing a default, altering defaulting order, making an optional field required, or removing a field is breaking, regardless of how few consumers appear to use it. Stability labels carry a promise rather than a maturity feeling, so each label states its change freedom and its notice obligation. The abstraction boundary is written as two lists, hidden and exposed, and each exposed item names the reason it is exposed, since an item exposed by accident is an item the platform can no longer change. Extension points are designed deliberately so that overriding does not require abandoning the resource.

**Parallel surface.** Independent resource kinds, independent schema fields, independent client surfaces, and independent consumer-usage extractions fan out safely. The cross-surface consistency judgment, the aggregate breaking-change classification for a release, and the abstraction boundary decision run once, after the fan-out returns, because a boundary drawn per resource without a portfolio view is how a platform ends up with three incompatible ways to express the same intent.

**Ordered gate for removing a served version.** This order is externally mandated by the published deprecation policy and the final step is irreversible for objects still stored at the old version, so it does not compress:

1. Publish the deprecation with the replacement field or version and the enforcement dates, against the notice window the stability label promised.
2. Establish the remaining consumers at the deprecated version from request logs, stored-object counts, and repository references.
3. Ship and prove the conversion path so stored objects can be read at the new version.
4. Stop serving the deprecated version while conversion remains available.
5. Remove the version and its conversion only once no objects remain stored at it.

**Acceptance bar.** A tenant engineer could write a manifest against the contract, and a platform engineer could change the implementation behind it, without either of them needing to ask what is guaranteed. Every field has semantics and defaulting stated, every surface has a stability label with its change freedom, every proposed change carries an additive-or-breaking classification with the reason, and the abstraction boundary names what is exposed and why.

## Outputs

A complete run delivers this set:

- `platform-api-contracts.md`: one entry per surface with API group, version, stability label, the compatibility guarantee, and the client surfaces that exercise it.
- `resource-schemas.md`: field-level specification with type, semantics, defaulting, mutability, validation, and the spec-versus-status split for each resource.
- `versioning-and-stability-policy.md`: what each stability label permits, how a surface is promoted, the notice window per label, and the conversion obligation when versions coexist.
- `compatibility-classification.md`: the additive-versus-breaking rules with worked examples from this platform's own schemas, including the changes that look additive and are not.
- `abstraction-boundary.md`: the hidden list, the exposed list with a reason per item, the extension points, and the escape-hatch fields with the support consequence of using them.
- `consumer-impact-map.md`: per surface and per field, the consumers established from usage evidence, with the evidence class for each.
- `platform-api-downstream-handoff.md`: what `tenancy-isolation-desk` inherits, including which API surfaces cross a tenant boundary.

Depth standard: an artifact is complete when a consumer could code against it and a maintainer could plan a change against it without a follow-up round trip. A field entry without defaulting and mutability, or a stability label without a notice window, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the served schema definitions, request logs, or repository search cannot be read, the run delivers `platform-api-connector-diagnostic.md` naming each unreachable source and the contract claims that depend on it. A compatibility guarantee is not published against an unread schema.

Anti-fabrication guard: the specific hazard here is writing a guarantee the platform never made. Compatibility policies have a familiar shape, so a plausible support window reads as though it were quoted from an existing policy, and once it appears in a contract artifact the platform is held to it by consumers who reasonably relied on it. Every window, notice period, and stability promise in the output is quoted from the platform's published policy or is marked as proposed and unratified, with the approver who would have to ratify it named. Schema fields, versions, and stored-version state are read from the served definitions rather than reconstructed from documentation or from what the resource obviously ought to contain. Consumer counts name the request log query, repository search, or stored-object count behind them; a field with no usage evidence is recorded as usage-unknown rather than as unused, because unused is the claim that gets a field removed.

## platform_packet fields to update

- `platform_apis[]` with `name`, `version`, `stability`, `compatibility_guarantee`, and `breaking_change_window`
- `abstractions[].name` and `abstractions[].provisions` where the API surface fronts an abstraction
- `deprecations[]` seeded for any surface entering a notice window, with `announced` and `eol` left unknown until published
- `governance.approval_gates` for changes requiring ratification
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: publishing a breaking change, shortening a notice window, or promoting a surface to stable commits the platform to a support obligation and needs the named governance owner.
- **Production or destructive**: the next action would apply a schema change to a live control plane, alter a stored version or conversion configuration, or remove a served version, any of which can render persisted tenant objects unreadable.
- **Security or privacy**: a schema field would carry a secret in plain text, an exposed field would leak another tenant's identifiers, or the client surface would widen access beyond the tenancy boundary.
- **Source conflict**: the served definitions, the published documentation, and the client surface genuinely disagree about a field's semantics or defaulting, and resolving that silently would publish a contract that does not match behavior.
- **Release integrity**: a surface would be labeled stable without evidence of a conversion path, a notice policy, and a consumer impact assessment.
- **Connector unreachable**: the schema source, request logs, control plane, or repository search needed to establish reliance exists and cannot be read.

Missing usage evidence for a low-traffic field and an unpublished notice history are soft gaps. Record the gap, label the assumption, and continue.

## Downstream handoffs

`tenancy-isolation-desk` is next and needs the API surfaces that cross a tenant boundary and the fields that carry tenant identity. `self-service-infrastructure-desk` needs the resource schemas its modules must satisfy. `scaffolding-templates-desk` needs the contract that generated manifests are written against, since templates pin consumers to a version. `platform-change-rollout-desk` needs the compatibility classification and consumer impact map, which decide the ring plan and whether a notice window applies. `platform-deprecation-sunset-desk` inherits any surface entering a notice window.

## Quality bar

Good contract work reads like a published API, not an internal design note. A consumer can tell from the artifact what they may rely on and what may change under them. The abstraction boundary is stated as a decision with reasons, so a future maintainer knows which exposures were deliberate and which were accidents to be reclaimed. The additive-versus-breaking rules use this platform's own schemas as examples, especially the changes that look harmless and are not. Escape-hatch fields exist, are documented, and carry a stated support consequence, because the alternative is tenants forking the resource entirely and the platform losing sight of them.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
