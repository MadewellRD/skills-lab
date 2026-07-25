---
name: golden-path-design-desk
description: define the paved road by stack, covering golden path definitions, path tiering across paved supported escape-hatch and unsupported, opinionated defaults and what each default buys the developer, the runtime and framework support matrix the platform commits to maintain, escape-hatch policy and its support boundary, and version support windows. use for paved road design, blessed stack decisions, supported technology matrices, off-road policy, platform default selection, and consolidating divergent service templates.
---

# Golden Path Design Desk

## Suite workflow mode

This desk is a member of the Platform Engineering Command Desk suite. Complete the golden path artifact set, update the `platform_packet`, and continue to the next stage whenever available source facts support it. The packet shape and continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent template references, module versions, runtime or framework versions, support windows, path owners, or the number of services on a path.

## Role

Define what the paved road actually is, per stack, and what the platform team commits to maintain. This desk owns path definitions, the tier each path sits in, the opinionated defaults each path ships with and what each default buys the developer, the escape-hatch policy and the support boundary that comes with leaving the road, and the supported matrix the team signs up to keep current.

The scarce resource here is maintenance capacity, not design imagination. Every language, framework version, deploy target, and datastore added to the matrix multiplies the combinations a small team owns forever. A path the team cannot keep patched is not a paved road; it is a promise that expires quietly.

## Use when

- The organization needs a blessed stack and the supported matrix has never been written down or has grown past what the team can maintain.
- Services have diverged and a consolidation target needs defining before templates or modules are rebuilt.
- Developers are going off-road and the escape-hatch policy needs a stated support boundary rather than an informal one.
- A new runtime, framework, or deploy target is being proposed for the matrix and the maintenance cost needs pricing.
- A path exists in documentation and needs testing against whether any template, module, or pipeline actually backs it.
- Defaults are being chosen and each one needs to be justified by what it removes from the developer rather than by preference.

## Do not use when

- The friction being solved has not been located or sized. That is `developer-experience-research-desk`, whose prioritized list this desk consumes.
- The question is whether the capability should exist and who funds it. That is `platform-product-intake-desk`.
- The work is building the repository template that implements the path. That is `scaffolding-templates-desk`, which consumes path definitions and produces the template.
- The work is the infrastructure modules the path provisions. That is `self-service-infrastructure-desk`.
- The question is how teams get moved onto the path and in what order. That is `platform-adoption-migration-desk`.
- A path tier is being demoted or a path retired. That is a capability removal, and it runs under the ordered destructive sequence in `references/suite-workflow-contract.md` with `platform-deprecation-sunset-desk` owning the sunset.

## Required evidence

- The existing stack inventory from repositories and deploy manifests: languages and versions, frameworks, base images, build tools, deploy targets, and datastores actually in production.
- The prioritized friction list and cognitive load assessment from the research stage.
- Current templates, modules, charts, and pipeline definitions, with their versions and their real usage counts.
- Organizational technology constraints: security-approved runtimes, licensing limits, regulated workload requirements, and any architecture standard already ratified.
- Escape-hatch evidence: services that bypass the path today, what they bypass, and the reason recorded in the repository or the ticket that authorized it.
- Platform team capacity and current maintenance load, since the matrix is bounded by it.
- Upstream support and end-of-life dates for the runtimes and frameworks under consideration, taken from the vendor or project source.

## Workflow

**Outcome.** A set of golden path definitions with a tier per path, the opinionated defaults each path ships and the decision each default removes, a supported matrix with version windows and a named owner per path, and an escape-hatch policy stating exactly what support a team keeps when it leaves the road.

**Grounding.** Read the stack inventory from repositories and deploy manifests, not from the portal, because the portal describes what the platform intended and the manifests describe what exists. A path is backed when a template, module, or pipeline reference can be named for it; a path documented with nothing behind it is recorded as documented-only, and that gap is one of the highest-value findings this desk produces.

**Constraints.** Every default is justified by what it removes from the developer: a decision they no longer make, a file they no longer author, a review they no longer wait for. A default that buys nothing is a preference and does not belong on the road. Tiering is a support commitment, so each tier states response expectations, upgrade responsibility, and who fixes a break. The matrix is bounded by the maintaining team's capacity, and adding a combination is priced against that capacity rather than approved on merit alone. The escape hatch is a first-class, documented route with a support boundary attached, because an undocumented escape hatch becomes a silent fork the platform later discovers during an incident. Version support windows come from upstream end-of-life dates, and where those dates are unavailable the window is recorded as unset rather than guessed.

**Parallel surface.** Independent stacks, independent candidate paths, and independent default decisions fan out safely. The matrix-wide capacity judgment, the tier assignment across the full path set, and the consolidation decision that says which existing paths merge run once, after the fan-out returns, because each one is a statement about the whole portfolio rather than about a single path.

**Acceptance bar.** A team could pick their path from the matrix and start without asking a platform engineer which one applies: each path names its stack, tier, owner, backing template or module, and version window; each default names what it buys; the escape-hatch policy states what a team loses and what it keeps; and any path with no backing artifact is labeled documented-only rather than presented as paved.

## Outputs

A complete run delivers this set:

- `golden-paths.md`: one definition per path with stack, tier, owner, backing template or module reference, what the path provisions on day one, and its current service count with the source of that count.
- `path-tiering-policy.md`: the four tiers with the support commitment, upgrade responsibility, and break-fix expectation attached to each, written so a team can tell which tier they are in.
- `opinionated-defaults.md`: each default with the decision it removes, its override mechanism, and the conditions under which overriding is legitimate.
- `supported-matrix.md`: runtime, framework, base image, deploy target, and datastore combinations the platform commits to, with version windows sourced from upstream end-of-life dates and the maintenance load the matrix implies.
- `escape-hatch-policy.md`: how a team leaves the road, what they must record, what support they keep, what they take over, and the review point at which repeated escape-hatch usage becomes a signal that the path is not paved.
- `golden-path-downstream-handoff.md`: what `service-catalog-desk` inherits, including which paths need catalog kinds and which are documented-only.

Depth standard: an artifact is complete when a team lead could choose a path and a platform engineer could start implementing its template from the same document. A path entry without a backing reference and an owner, or a default without the decision it removes, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the template repositories, module registry, or deploy manifests exist and cannot be read, the run delivers `golden-path-connector-diagnostic.md` naming each unreachable source and the path claims that depend on it. Path definitions are not tiered as paved against an unread template repository.

Anti-fabrication guard: the characteristic failure at this desk is declaring a road paved on the strength of a documentation page. Paved is a claim about artifacts that exist, so each path claiming the paved tier names the template reference, module version, or pipeline definition that backs it and the owner who maintains it. Where no backing artifact can be named, the path is recorded as documented-only and its tier is stated as aspirational, which is an honest and useful output rather than a hole in the matrix. Service counts per path name the catalog query or manifest scan that produced them or are written as uncounted. Runtime and framework support windows are quoted from the upstream project's published end-of-life date and are never inferred from a version number's age, because a wrong support window is a promise the platform will be held to during a security patch.

## platform_packet fields to update

- `golden_paths[]` with `path_id`, `stack`, `tier`, `owner`, and `backing_template`
- `consumers[].escape_hatches_in_use` for teams whose bypasses were evidenced
- `governance.standards` for matrix entries that become organizational standards
- `platform_surface` set to `golden_path`
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Missing approval**: making a path mandatory, removing a runtime from the supported matrix, or committing the platform team to a new maintenance combination needs a named owner from the governance forum who has not given it.
- **Production or destructive**: the next action would demote or retire a path that services currently run on, which strands those services and runs under the ordered destructive sequence rather than as a design change.
- **Security or privacy**: a proposed default or escape hatch would weaken secret handling, workload identity, or an approved-runtime constraint, or would place regulated workloads on an unapproved base image.
- **Source conflict**: the deploy manifests, the template repository, and the portal genuinely disagree about what backs a path, and picking one silently would publish a paved tier that no artifact supports.
- **Release integrity**: a path would be published as paved without a nameable backing template, module, or pipeline.
- **Connector unreachable**: the template repository, module registry, deploy manifests, or stack inventory exists and cannot be read.

Unknown service counts, missing capacity figures, and undated upstream support windows are soft gaps. Name them, label the assumption where it was used, and continue.

## Downstream handoffs

`service-catalog-desk` is next and needs the path definitions and tiers so catalog entities can carry a path attribute and a scorecard can measure conformance to it. `scaffolding-templates-desk` needs the defaults and the day-one contents each path promises, since the template is where the promise becomes real. `self-service-infrastructure-desk` needs the infrastructure each path provisions. `platform-adoption-migration-desk` needs the escape-hatch policy and the current service counts as its funnel baseline. `platform-governance-desk` inherits the matrix entries that are being proposed as mandatory standards.

## Quality bar

Good path design is narrow and honest. It commits to fewer combinations than the organization uses today and says which ones it is deliberately leaving unsupported. Every default has a developer-visible payoff, not a rationale about consistency. The escape hatch is documented well enough that a team using it does so on the record instead of in silence, because escape-hatch usage is the platform's earliest signal that a road it calls paved is gravel. The matrix is small enough that the maintaining team could patch every entry inside a single security response window, and if it is not, the artifact says so rather than implying a capacity the team does not have.
