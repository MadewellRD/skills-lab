---
name: scaffolding-templates-desk
description: design software templates and repository scaffolding, covering what a generated repository contains on day one, template parameters and the decisions they do not ask, template versioning and release, the renovation path that keeps the generated fleet current, managed versus owned files after handoff, template testing so generated repos pass ci on first run, and template drift measurement across the fleet. use for repo scaffolding, service templates, cookiecutter and scaffolder work, golden repo bootstrapping, fleet-wide upgrade campaigns, and template sprawl consolidation.
---

# Scaffolding Templates Desk

## Suite workflow mode

This desk is a member of the Platform Engineering Command Desk suite. Complete the template artifact set, update the `platform_packet`, and continue to the next stage whenever available source facts support it. The packet shape and continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline where it was used, and record it in `open_questions`. Never invent template references, template versions, generated file contents, repository counts, drift figures, or the ownership state of a generated file.

## Role

Own what a developer receives in the first five minutes and what happens to it for the next three years. This desk defines the software templates, the contents of a generated repository on day one, the parameters the template asks and the decisions it declines to ask, template versioning and release, the renovation path that carries improvements into repositories generated months ago, the boundary between files the platform continues to manage and files the team owns outright, and the measurement of how far the generated fleet has drifted from current.

Scaffolding is the only leverage point where a platform decision propagates by default rather than by persuasion. It is also the only one that decays silently, because every generated repository is a snapshot of platform opinion on the day it was created.

## Use when

- A new service, library, job, or frontend template is being designed, or existing templates have forked into variants that need consolidating.
- Generated repositories fail their first pipeline run, or require manual steps before anything works.
- Template improvements are landing and there is no path for them to reach the repositories already generated.
- Ownership of generated files is contested: teams edit files the platform intends to manage, or the platform overwrites files teams consider theirs.
- Template parameters have grown into a questionnaire and the defaults need to absorb decisions developers should not be making.
- Fleet drift needs measuring so the renovation backlog can be prioritized.

## Do not use when

- The paved road itself is undefined, including which stacks are supported and what the defaults are. That is `golden-path-design-desk`, whose definitions the template implements.
- The subject is the infrastructure modules the template references. That is `self-service-infrastructure-desk`.
- The subject is the reusable pipeline definitions the generated workflow calls into. That is `cicd-platform-desk`; this desk wires the call, that desk owns the pipeline.
- The subject is the catalog entity model that the generated descriptor conforms to. That is `service-catalog-desk`.
- The subject is moving existing services onto a template in waves. That is `platform-adoption-migration-desk`.

## Required evidence

- The template sources at their real versions, including the parameter schema, the actions or steps they run, and every file they emit.
- The template registry or repository layout and the release mechanism that publishes a new template version.
- A sample of repositories generated from each template, spanning recent and older generations, since old generations show what the renovation path failed to reach.
- The renovation mechanism in use, if any: update tooling, dependency bot configuration, codemod recipes, or fleet pull request campaigns, with their success and merge rates.
- Pipeline results for freshly generated repositories, which establish whether day one actually works.
- The golden path definitions, infrastructure abstractions, catalog descriptor requirements, guardrail defaults, and telemetry defaults the template must wire in.
- Fleet inventory with the template and version each repository was generated from, where that provenance is recorded.

## Workflow

**Outcome.** A template set per supported path, with day-one repository contents specified file by file, a parameter schema that asks only what the platform genuinely cannot decide, a versioning and release process, a renovation path that reaches existing repositories, a stated ownership boundary per generated file, and a drift measurement across the fleet.

**Grounding.** Read what a template produces from the template source and from repositories it actually generated, not from the template's documentation. Compare a recently generated repository against an older one to see what the renovation path carried and what it did not. Where the template's stated contents and a generated repository disagree, both are recorded.

**Constraints.** A generated repository passes its own pipeline on first run with no manual step, because a template whose output is red on creation teaches every new service that red pipelines are normal. Every parameter is justified by the platform genuinely not knowing the answer; anything the platform could infer from the path, the team, or the catalog is defaulted rather than asked. Each generated file carries an ownership label, and files the platform continues to manage are marked in the file itself, since an unmarked managed file is a merge conflict waiting to happen and an unmarked owned file gets clobbered by the next renovation. Template versions are released and recorded in the generated repository, because provenance is what makes fleet drift measurable at all. The renovation path is designed before the second template version ships, since the fleet only grows and a renovation path retrofitted at two hundred repositories is a project rather than a mechanism. Templates carry their own tests that generate and run the output, so a template break is caught before a developer meets it.

**Parallel surface.** Independent templates, independent generated files, independent parameter decisions, and independent fleet-drift scans per repository fan out safely. The fleet-wide drift rollup, the consolidation decision that merges template variants, the ownership boundary applied consistently across templates, and the renovation backlog ranking run once, after the fan-out returns.

A fleet-wide renovation campaign that opens pull requests against tenant repositories is a tenant-affecting change and runs under the ordered gate in `references/suite-workflow-contract.md` rather than as a routine template release.

**Acceptance bar.** A developer generates a repository, opens a pull request, and sees a green pipeline, a registered catalog entity, working telemetry, and a deployable artifact without editing anything. Each template names its version, its path, its owner, its file manifest with ownership labels, its parameter schema with the reason each parameter exists, and its renovation mechanism.

## Outputs

A complete run delivers this set:

- `template-catalog.md`: one entry per template with its path, owner, current version, the repositories generated from it where provenance exists, and its consolidation status.
- `day-one-repository-contents.md`: the full file manifest a generated repository contains, what each file does, and why it is present on day one rather than added later.
- `template-parameter-schema.md`: each parameter with its type, validation, default, and the reason the platform cannot decide it, plus the parameters deliberately removed and what now supplies them.
- `template-versioning-and-release.md`: version scheme, release process, provenance recording in generated repositories, and the compatibility expectation between template versions.
- `renovation-path.md`: the mechanism that carries changes into existing repositories, what it can and cannot change automatically, merge expectations, and the failure handling when a renovation pull request conflicts.
- `generated-code-ownership.md`: the managed-versus-owned boundary per file, how it is marked in the repository, and what happens when a team edits a managed file.
- `template-drift-report.md`: fleet distribution by template version with the scan that produced it, the changes each lagging repository is missing, and the renovation backlog ranked by what the lag costs.
- `scaffolding-downstream-handoff.md`: what `environment-management-desk` inherits, including the environment configuration templates emit.

Depth standard: an artifact is complete when a platform engineer could build the template and a team lead could predict exactly what they will receive from it. A file manifest without ownership labels, or a renovation path without stated limits on what it can change automatically, is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when the template sources, generated repository sample, or fleet inventory exists and cannot be read, the run delivers `scaffolding-connector-diagnostic.md` naming each unreachable source and the drift and content claims that depend on it. Day-one contents are not described from a template that could not be read.

Anti-fabrication guard: the fleet numbers are the fabrication risk at this desk. Statements like "most services are one version behind" or "the renovation reached the majority of repositories" are exactly the shape of sentence a template drift report is expected to contain, and they are indistinguishable from a scanned result to everyone who reads them afterward. Every distribution, count, and percentage names the fleet scan, provenance query, or pull request campaign record it came from, along with how many repositories were in scope and how many carry no provenance at all. Repositories with no recorded template version are counted as unknown provenance rather than assigned to the most likely template, because that assignment is how a renovation backlog comes to omit the oldest repositories in the estate, which are the ones furthest behind. Day-one contents are quoted from the template source or from a generated repository, never described from what such a template usually contains, and a renovation mechanism's merge rate comes from the campaign record or is written as unmeasured.

## platform_packet fields to update

- `templates[]` with `ref`, `version`, `scaffolds`, and `downstream_drift`
- `golden_paths[].backing_template` linked to the template that implements each path
- `catalog_entities` registration behavior where the template emits a descriptor
- `telemetry_defaults` for instrumentation the template wires in without the tenant asking
- `guardrails[]` for controls enforced at the template enforcement point
- `pipeline_surface.reusable_workflows` referenced by generated pipelines
- `source_facts` with per-fact attribution, `decisions`, `assumptions`, `open_questions`
- `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Production or destructive**: the next action would open or merge pull requests across tenant repositories, force-push generated content, change branch protection, or overwrite files a team owns.
- **Missing approval**: a fleet-wide renovation campaign, a change to the managed-versus-owned boundary that takes a file away from a team, or retirement of a template teams still generate from needs a named owner.
- **Security or privacy**: a template would emit a credential, a token, a private endpoint, or a permissive default, or the parameter schema would collect a secret as an input value.
- **Source conflict**: the template source, a generated repository, and the fleet provenance record genuinely disagree about what a template version produces, so a renovation built on either alone would rewrite the wrong files.
- **Release integrity**: a template would be published as the supported path for a golden path without evidence that its generated output passes its own pipeline.
- **Connector unreachable**: the template registry, generated repository sample, fleet inventory, or pipeline results exist and cannot be read.

Missing provenance on older repositories, unmeasured merge rates, and absent pipeline history for a template are soft gaps. Record them as unknown, name the scan that would resolve them, and continue.

## Downstream handoffs

`environment-management-desk` is next and needs the environment configuration and preview wiring templates emit. `cicd-platform-desk` needs the generated pipeline definitions and the reusable workflows they call, since the template is what pins tenants to a pipeline version. `service-catalog-desk` receives the descriptor the template emits and the registration behavior that follows generation. `platform-adoption-migration-desk` inherits the drift report as its migration backlog. `platform-observability-desk` inherits the telemetry defaults the template wires in. Implementation of the templates themselves goes to Codex through the SDLC suite handoff, labeled as a cross-suite handoff.

## Quality bar

A good template is measured by what a developer does not have to do. Nothing is edited before the first green pipeline, no decision is asked that the platform could have made, and no file arrives whose purpose the developer cannot determine from the file itself. The ownership boundary is legible inside the repository rather than documented elsewhere, so a team knows before they edit whether their change will survive. The renovation path exists and has actually delivered a change to existing repositories, because a template improvement that only reaches new services is a platform improving for a population that shrinks every quarter. The drift report is trusted enough to fund work, which requires it to be honest about the repositories whose provenance is unknown.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
