---
name: service-catalog-desk
description: design the software catalog and developer portal surface, covering entity kinds and the entity model, ownership and lifecycle metadata, relations between components systems apis and resources, registration and ingestion mechanics including auto-discovery and entity descriptors, metadata freshness and staleness rules, scorecard definitions and thresholds, and how developers discover and act on entities. use for service catalog design, catalog rot and orphaned entities, ownership metadata, service registration, tech health scorecards, and developer portal information architecture.
---

# Service Catalog Desk

## Suite workflow mode

This desk is a member of the Platform Engineering Command Desk suite. Complete the catalog artifact set, update the `platform_packet`, and continue to the next stage whenever available source facts support it. The packet shape and continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent entity names, owning groups, on-call rotations, lifecycle states, dependency relations, scorecard scores, or entity counts.

## Role

Own the catalog as the system of record for what exists, who owns it, and what state it is in. This desk defines the entity model and its kinds, the ownership and lifecycle metadata every entity must carry, the relations that make the graph navigable, how entities get registered and stay registered, the freshness rules that keep the catalog from rotting, the scorecards that turn metadata into pressure, and the portal surface where developers find and act on all of it.

A catalog is only worth the trust placed in it during an incident. The measure that matters is whether someone paged at two in the morning can find the owner of an unfamiliar service and reach a human. Everything else in the entity model exists to support that and to make platform-wide questions answerable without a spreadsheet.

## Use when

- The catalog does not exist, or it exists and nobody trusts it enough to use it during an incident.
- Ownership is stale: entities point at teams that reorganized, dissolved, or never agreed to own them.
- Registration is manual and drifting, and discovery or ingestion needs designing so entities appear without a ticket.
- The entity model needs kinds and relations defined so questions about dependency, API consumers, and blast radius are answerable.
- Scorecards are being introduced, or existing ones measure what is easy to collect rather than what predicts operational risk.
- The portal surface needs designing so the catalog is where developers act rather than a directory they visit once.

## Do not use when

- The question is what the supported stacks and paved roads are. That is `golden-path-design-desk`, whose tiers this desk stores as entity attributes.
- The subject is the platform's own API and resource schemas rather than the catalog's entity model. That is `platform-api-contract-desk`.
- The subject is the repository template that emits a catalog descriptor on scaffold. That is `scaffolding-templates-desk`.
- The subject is scorecard thresholds becoming mandatory standards with consequences attached. That is `platform-governance-desk`; this desk defines the scorecard, governance decides what a failing score costs.
- The subject is telemetry, dashboards, and instrumentation defaults. That is `platform-observability-desk`.

## Required evidence

- The existing catalog or registry export in full, including entities in an error or orphaned state, not only the healthy ones.
- Repository inventory, deploy manifests, and running workload inventory, which together establish what actually exists and can be reconciled against the catalog.
- Ownership records from the source the organization treats as authoritative: the group directory, on-call rotation, or team registry, with its own last-updated state.
- Existing entity descriptor files and their annotations, plus the ingestion configuration and any discovery processors in use.
- Portal configuration and its plugin or action surface, so the catalog's action affordances are known rather than assumed.
- Incident records where finding an owner delayed response, which is the sharpest evidence of catalog quality.
- Golden path tiers and backing templates from the upstream stage.

## Workflow

**Outcome.** An entity model with defined kinds, required metadata, and relations; registration and ingestion mechanics that keep the catalog current without manual upkeep; freshness rules with an explicit staleness consequence; scorecard definitions with thresholds; and the portal surface through which entities are discovered and acted on.

**Grounding.** Reconcile the catalog against reality rather than describing the catalog on its own terms. Repositories, deploy manifests, and running workloads say what exists; the catalog says what the organization believes exists. The delta in both directions is the finding: entities in the catalog with no running workload, and running workloads with no entity. Ownership comes from the authoritative group source, and where that source disagrees with the entity descriptor, both are recorded.

**Constraints.** Every kind states its required metadata, its optional metadata, and what a missing required field blocks, because a required field with no consequence is decoration. Relations are modeled so blast radius and API consumer questions are answerable by traversal rather than by search. Registration favors the path that produces entities as a side effect of work developers already do, since any mechanism requiring a separate remembered step decays to the coverage of whoever remembers. Freshness rules attach a staleness window and a consequence to each field class, because a catalog with no expiry becomes a museum. Scorecards measure what predicts operational risk, and every check names the signal it reads and the action that fixes a failure. Ownership is recorded as a group reference with a reachable escalation path, never as an individual, because individuals leave and the entity outlives them.

**Parallel surface.** Independent entities, independent kinds, independent scorecard checks, and independent ingestion sources fan out safely. The reconciliation between catalog and reality, the ownership coverage total, the duplicate-entity resolution across ingestion paths, and the scorecard rollup across the estate run once, after the fan-out returns, because each is a statement about the whole catalog rather than about one entry.

**Acceptance bar.** Someone paged against an unfamiliar service could find its owner, its lifecycle state, its dependencies, and its runbook from the catalog alone. The entity model states required metadata per kind with a consequence for absence, registration works without a remembered manual step, freshness has a window and a consequence, and every scorecard check names its signal and its remediation.

## Outputs

A complete run delivers this set:

- `catalog-entity-model.md`: kinds, required and optional metadata per kind, relations, naming and namespace rules, and what a missing required field blocks.
- `ownership-and-lifecycle-policy.md`: how ownership is expressed and sourced, the escalation path behind a group reference, lifecycle states with their transitions, and the process for an entity whose owner has dissolved.
- `registration-and-ingestion.md`: descriptor location and format, discovery and ingestion mechanics, the deduplication rule across ingestion paths, error-state handling, and the reconciliation job against repository and workload inventory.
- `metadata-freshness-rules.md`: field classes with staleness windows, the consequence at each window, and the reporting surface that shows decay before it becomes rot.
- `catalog-scorecards.md`: each check with its signal, threshold, remediation, and the risk it predicts, plus the checks deliberately excluded and why.
- `portal-surface-spec.md`: the discovery and action surface, what a developer can do from an entity page without leaving it, and the entry points into the paved road.
- `catalog-reconciliation-report.md`: catalog entries with no corresponding workload, workloads with no entity, and entities whose owner does not resolve in the authoritative group source.
- `service-catalog-downstream-handoff.md`: what `platform-api-contract-desk` inherits, including which kinds represent platform-owned interfaces.

Depth standard: an artifact is complete when a platform engineer could implement the ingestion and a team lead could register their service from the same set without asking a follow-up question. A kind with required fields but no stated consequence, or a scorecard check with a threshold but no remediation, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the catalog export, repository inventory, or authoritative group source exists and cannot be read, the run delivers `catalog-connector-diagnostic.md` naming each unreachable source and the reconciliation claims that depend on it. Ownership coverage is not reported against an unread group directory.

Anti-fabrication guard: ownership is where this desk fabricates if it is going to. The temptation is structural, because an unowned entity looks like a defect in the artifact and the repository history always offers a plausible name to fill it with. The most frequent committer is an author, not an owner, and writing that name into an owner field converts a research gap into an on-call expectation nobody agreed to. An entity whose owner does not resolve in the authoritative group source is recorded as unowned and listed for resolution, and that list is the most valuable page in the output rather than a blemish on it. Entity counts, coverage percentages, and scorecard rollups name the export and query that produced them or are written as uncounted, and a dependency relation is recorded only where a manifest, descriptor, or trace establishes it, never because two services plausibly talk to each other.

## platform_packet fields to update

- `catalog_entities[]` with `kind`, `ref`, `owner`, `lifecycle`, and `metadata_gaps`
- `consumers[].services` populated from resolved ownership
- `platform_surface` set to `service_catalog` or `developer_portal`
- `governance.standards` for scorecard checks proposed as organizational standards
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: assigning ownership of an unowned entity to a team, or attaching a consequence to a failing scorecard, commits that team to on-call work and needs a named owner's authorization.
- **Production or destructive**: the next action would delete, merge, or bulk-mutate catalog entities, deregister a live service, or change the ingestion configuration in the running portal.
- **Security or privacy**: catalog metadata or descriptor annotations would expose credentials, internal endpoints, or personal contact details beyond their intended audience, or the portal surface would grant an action across a tenancy boundary.
- **Source conflict**: the entity descriptor, the group directory, and the on-call rotation genuinely disagree about who owns an entity, and silently choosing one would publish an owner who has not accepted the page.
- **Release integrity**: catalog coverage or scorecard conformance would be reported as an estate-wide figure when the reconciliation covered only part of the inventory.
- **Connector unreachable**: the catalog export, repository inventory, group directory, or portal configuration exists and cannot be read.

Missing descriptors, absent annotations, and unpopulated optional metadata are soft gaps. Record them in `metadata_gaps` and continue.

## Downstream handoffs

`platform-api-contract-desk` is next and needs the entity kinds and relations, since platform APIs are catalog entities with their own stability contracts. `scaffolding-templates-desk` needs the descriptor format and required metadata so generated repositories register themselves on day one. `platform-observability-desk` needs the entity identifiers that telemetry will be tagged against. `platform-cost-attribution-desk` needs the ownership graph as its allocation key source. `platform-governance-desk` inherits the scorecard definitions and decides what a failing score costs.

## Quality bar

A good catalog is judged during an incident, not during a review. The owner resolves to a group with a reachable escalation path, the lifecycle state is current enough to be trusted, and the dependency graph answers a blast-radius question without a human tracing it by hand. Registration happens as a byproduct of work developers already do, so coverage does not depend on discipline. Freshness has teeth: a field that has aged past its window is visibly stale rather than silently wrong. The scorecard measures things that predict operational pain and says out loud which easy-to-collect checks it deliberately left out.
