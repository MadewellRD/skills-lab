---
name: infrastructure-as-code-desk
description: design infrastructure as code repository and stack layout including state boundaries and blast radius, module interfaces and semantic versioning, remote state backend location with locking and encryption and read access, provider and dependency version pinning with lock files, composition patterns across environments, validation and policy unit test gates, secrets-out-of-state discipline, state import and refactor safety, and measured codification coverage of the live estate.
---

# Infrastructure As Code Desk

## Suite workflow mode

This desk is part of the Cloud Infrastructure Command Desk suite. Complete the codification artifact set, update the `infrastructure_packet`, and continue to the next stage whenever available facts allow rather than stopping at a bare next-desk recommendation. The packet shape, declared-versus-live source discipline, and halt format live in `references/suite-workflow-contract.md`; the stage input and output boundary lives in `references/stage-contracts.md`; what may be assumed about the executing model lives in `references/capability-baseline.md`.

Return `Workflow Halt` only for one of the six hard classes in `references/halt-taxonomy.md`: missing approval, production or destructive action, security or privacy exposure, source conflict, release integrity, or an unreachable connector. Every other gap is soft, so proceed with the assumption labeled inline where it was used and recorded in `open_questions`. Never invent module names or version tags, provider version constraints, state backend paths, resource addresses, workspace names, or coverage percentages.

## Role

Own the shape of the code that produces the estate. This desk decides where each state boundary falls and what one bad apply inside it can reach, what interface a module exposes to the people who consume it, how a consumer moves from one module version to the next, where state lives and who can read it, which versions are pinned and by what mechanism, and what share of what is actually running has code behind it at all.

The load-bearing decision is the state boundary. A state file is a blast radius: everything inside one can be destroyed by one apply, one lock holder blocks every other change to it, and one corrupt write takes the whole boundary with it. A single root module that holds the network, the identity roles, and every workload is convenient on day one and is the reason nobody will apply anything on day four hundred.

## Use when

- Repository layout, stack decomposition, or state boundary design is being set or revisited, including splitting a root module that has grown past what anyone will apply.
- Module work: interface design, input and output contracts, versioning scheme, registry publication, or the upgrade path for existing consumers.
- The state backend is being chosen, moved, or hardened: location, locking mechanism, encryption with named key ownership, object versioning, and who holds read access.
- Version pinning is loose or absent: provider constraints, dependency lock files, and module references pointing at a mutable branch.
- Code-level gates are being defined: format and validation, static analysis, policy unit tests against module fixtures, plan-only checks.
- The question is what fraction of the running estate is under code, and the answer today is a feeling rather than a measurement.

## Do not use when

- The pipeline that runs the code is the subject, including plan review, approval matrix, apply identity, and promotion: that is `provisioning-pipeline-desk`, which consumes the state boundaries this desk defines.
- Live resources have diverged from the code and the question is what changed and who changed it: that is `drift-detection-reconciliation-desk`. This desk owns the import mechanics; that desk owns the reconciliation decision.
- Key hierarchy, secret store selection, rotation, and secret delivery are the subject: that is `configuration-secrets-desk`. This desk owns only the rule that keeps secret material out of state and code.
- The architecture being codified is not settled yet: return to the design desks, from `landing-zone-account-structure-desk` through `resilience-multi-region-desk`.
- Application build and release pipelines rather than infrastructure provisioning: cross-suite handoff to the SDLC suite.

## Required evidence

- The IaC repository as it exists: directory layout, root modules, child modules, environment configuration files, and the composition mechanism that assembles them.
- Backend configuration blocks with the actual location, locking mechanism, encryption setting, and key reference, read from the code rather than from the wiki.
- State inventory: the resource addresses each state file holds, its serial or version count, its size, and the identities that can read and write it.
- Provider requirement blocks and the committed dependency lock file, which is where the resolved version lives when the constraint is a range.
- Module sources with their pinned reference, and the registry or repository each resolves to.
- Existing validation and policy configuration in the repository, with whether each currently runs on every change or only on demand.
- The live resource inventory or billing export, needed as the denominator for any coverage statement.

## Workflow

**Outcome.** A repository and state layout where every boundary states what one apply can reach, every module states its interface and its version, the backend states its locking, encryption, and read access with evidence, every provider and module reference is pinned by a named mechanism, and codification coverage is a measured figure against a named inventory or is written as unmeasured.

**Grounding.** Read the repository for what is declared and the state backend plus the provider inventory for what exists, and keep them labeled separately per `references/suite-workflow-contract.md`. Three lists rarely agree: resources in code, resource addresses in state, and resources in the account. Code without state is unapplied intent, state without code is a resource whose definition was deleted out from under it, and account without state is unmanaged and belongs in the tagging and drift stages rather than being quietly folded into a coverage number.

**Constraints.** Every state boundary carries a stated blast radius and a stated lock contention cost, because those are the two prices being paid for the split. Cross-boundary references are explicit inputs where the value is stable and remote state reads only where the coupling is intentional and named, since a remote state read makes the reader fail whenever the writer's boundary is mid-refactor. Module interfaces expose intent rather than provider surface: a module that passes through forty optional variables has no interface, it has a rename. Module versions are immutable tags and consumers pin to them; a module source pointing at a default branch means every consumer's next plan is a surprise. Provider versions are constrained in code and resolved in a committed lock file, and the resolved version is the one that matters when explaining behavior. Secret material never enters state or code: state records values in the clear, so any resource that generates a credential writes that credential into the state object, and the design either avoids generating it there or treats that state object as a secret with matching access control. Coverage is stated as a measured share against a named denominator, or as unmeasured.

Splitting a state boundary or importing existing resources into one runs in this order, and the order is mandated because state operations have no undo and a wrong move either orphans a live resource or queues it for destruction on the next apply:

1. Take a copy of the current state object and confirm the copy is readable, before touching the original.
2. Write or move the code so it describes the resource exactly as it exists live, including the attributes the provider set by default.
3. Move or import the addresses, then generate a plan whose only acceptable result is no changes.
4. Only after that plan is clean does the boundary rejoin the normal apply path.

**Parallel surface.** Modules, stacks, root modules, state files, provider blocks, and repositories are independent units and are parallel-safe; per-module interface review, per-stack boundary analysis, per-file pinning audit, and connector preflight across the repository, state backend, and inventory all fan out.

The aggregate work runs once after the fan-out returns: the boundary map that shows which stacks depend on which, the coverage measurement against the single inventory denominator, the module version matrix across all consumers, and the upgrade ordering that follows from it. Per-module version answers assembled in parallel and never reconciled produce an upgrade plan where two consumers of the same module are told to move in incompatible directions.

**Acceptance bar.** An engineer new to the repository can name, for any resource, which state file holds it, which module defines it, which version of that module is in force, what else one apply against that boundary would touch, and where the backend for it lives. Every version, path, and coverage figure traces to a file or a query, or is written as unresolved.

## Outputs

A complete run delivers this artifact set:

- `infrastructure-as-code-layout.md`: repository and stack layout, the state boundary per stack with its blast radius and lock contention cost, the composition pattern that builds environments, and the cross-boundary dependency map.
- `infrastructure-as-code-module-register.md`: every module with its interface, its current version, its consumers, its upgrade path, and the changes that would force resource replacement in a consumer.
- `infrastructure-as-code-state-backend.md`: backend location, locking mechanism, encryption and key ownership, object versioning and retention, the identities holding read and write access, and the recovery path when a state object is lost or corrupted.
- `infrastructure-as-code-coverage.md`: the measured codified share against a named inventory, the resource classes not under code, the resource addresses in state with no code, and what it would take to close each gap.
- `infrastructure-as-code-downstream-handoff.md`: the state boundaries, apply scopes, and test gates `provisioning-pipeline-desk` inherits, plus the unmanaged set that `tagging-inventory-desk` and `drift-detection-reconciliation-desk` receive.

Depth standard per artifact: a boundary entry names the resources inside it and what a destroy against it would take out, not the abstract idea that boundaries limit risk. A module entry gives the actual required and optional inputs and the outputs other stacks consume. A backend entry gives the locking mechanism in use, not the assertion that locking is enabled. A coverage figure gives its numerator, its denominator, and the query behind both.

In `diagnostic` mode, when the repository or the state backend exists and cannot be read, the run delivers `infrastructure-as-code-connector-diagnostic.md` naming what was attempted and the exact access needed. Layout and coverage claims are not drafted from a directory listing in that mode.

The failure specific to this desk is the version string. Module tags, provider constraints, and backend paths are short, patterned, and get copied straight into a `required_providers` block or a module source, where a plausible value is indistinguishable from a real one until an apply resolves it to something nobody reviewed. A version that no lock file, tag list, or source line produced is written as unpinned-unknown rather than as a number. The same holds for coverage: an estate whose inventory was never read is uncodified-unmeasured, and a percentage with no denominator behind it is worse than admitting the estate was never counted.

## infrastructure_packet fields to update

- `iac.approach`, `iac.repo_layout`, `iac.state_backend`, `iac.module_versions`, `iac.coverage`, `iac.test_gates`.
- `inventory.unmanaged_resources` with the state-versus-inventory difference this desk measured.
- `secrets_and_config.known_exposure` when credential material is found in state, variable files, or repository history.
- `blast_radius` where a state boundary widens the classified radius beyond what intake assumed.
- `source_facts` with attribution, `decisions`, `assumptions`, `open_questions`, `artifacts`, `halt_conditions`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- Missing approval: splitting, merging, or relocating a state boundary that holds production resources, or adopting a module version whose upgrade forces replacement of a stateful resource.
- Production or destructive: the next action would move or destroy a state backend, remove addresses from state, run an import against a live boundary, or apply a plan generated during this stage.
- Security or privacy: state, variable files, or repository history contain credential material, or the backend grants read access broadly enough that state contents are effectively public inside the organization.
- Source conflict: the repository, the state objects, and the provider inventory genuinely disagree about what exists or which version defines it, and choosing one would launder a guess into a coverage claim.
- Release integrity: a codification coverage figure or a module upgrade path would be declared without the inventory or plan evidence behind it.
- Connector unreachable: the repository, the state backend, or the inventory export exists and cannot be read. An empty state list and an unreadable one look alike and mean opposite things, so say which happened.

An undocumented module rationale, a missing owner for a stack, or an unmeasured lock contention rate is a soft gap: proceed with it named. Encryption of state, restriction of state read access, and the exclusion of secret material from code are not soft gaps and are never relaxed to keep the workflow moving.

## Downstream handoffs

`provisioning-pipeline-desk` needs the state boundary list with the apply scope each one implies, the test gates that must run before a plan is reviewable, and the boundaries whose locks serialize other work. `configuration-secrets-desk` needs any credential found in state or code as an exposure item with its location. `tagging-inventory-desk` and `drift-detection-reconciliation-desk` need the resource address set under code, which is the denominator both of them reconcile against. When code changes are handed to Codex, the handoff carries the target boundary, the module versions in force, and the replacement risk, so the change is not authored against a repository layout that was inferred.

## Quality bar

A layout an engineer can reason about under pressure: they know what they are about to touch before they run anything. Modules have interfaces rather than passthroughs, versions are pinned by mechanism rather than by intention, the backend's protections are described by their configuration rather than by their purpose, and the coverage number is either measured or honestly absent.
