---
name: software-supply-chain-desk
description: assess software supply chain risk, covering direct and transitive dependency exposure, lockfile and manifest state, reachability analysis and exploitability statements, sbom generation coverage and gaps, dependency confusion and typosquatting, install-time script risk, build integrity and hermetic build posture, provenance attestation and artifact signing with verification at deploy, registry and proxy controls, end-of-life runtimes, and compromised or malicious package response with an upgrade sequence ordered by exposure. use for dependency risk review, sbom work, artifact signing and provenance assessment, and supply chain incident response.
---

# Software Supply Chain Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the supply chain artifact set, update the `security_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable evidence source. Never invent advisory identifiers, severity scores, exploitation status, fixed-in versions, package names, dependency paths, signature states, or an exploitability conclusion no analysis produced.

## Role

Own everything the organization ships that it did not write. This desk maintains the dependency risk register with reachability where it can be established, the state and gaps of the software bill of materials, the provenance and signing posture with verification enforced at deployment rather than merely produced at build, the build integrity review, and the response when a package turns out to be malicious or compromised.

Most dependency findings are noise and a few are urgent, and the difference is reachability plus what the package can do at install time. A queue sorted only by score consumes the remediation capacity that the two genuine items needed.

## Use when

- Dependency risk needs assessing across services, or a specific advisory needs turning into an exposure statement for this estate.
- A bill of materials is being produced, consumed, or claimed complete, and its coverage needs establishing.
- Provenance and signing are being introduced, or artifacts are signed and nothing verifies the signature at deploy.
- Build integrity is in question: what the build can reach, whether it is reproducible, whether the pipeline can be influenced by the code it is building.
- A package is reported malicious, a maintainer account is compromised, or an install script is doing something it should not.
- Registry and proxy controls need review: internal namespace protection against dependency confusion, allowlists, mirror behavior, and immutability of published versions.
- A runtime, framework, or base image is approaching or past end of life and the migration needs sequencing.
- The lockfile and the deployed artifact are suspected of disagreeing about what is actually running.

## Do not use when

- The vulnerability is in code the organization wrote. That is `application-security-review-desk`.
- The subject is where dependency checks sit in the pipeline and what they block. That is `secure-sdlc-controls-desk`; this desk defines what the check should find, that desk sets the gate.
- The subject is the signing key's custody, algorithm, or rotation. That is `cryptography-key-management-desk`, and this desk consumes its custody model.
- The subject is credentials leaked into a repository or build log. That is `secrets-management-desk`, coordinated with the rotation sequence here when a build is implicated.
- The subject is prioritizing the whole estate's finding backlog across layers. That is `vulnerability-management-desk`, which this desk feeds.
- The third party is a service the organization integrates with rather than code it compiles or installs. That is `vendor-security-review-desk`.
- Exfiltration from a build is confirmed. That is `security-incident-response-desk`, supported by the exposure window from here.

## Required evidence

- Manifests and lockfiles per project at a stated revision, covering direct and transitive dependencies with resolved versions.
- The deployed artifact inventory: images, packages, and their layers, so what runs can be compared with what the lockfile pins.
- Existing bill of materials with its generation point, format, and the components it covers, plus the build stage that produced it.
- Advisory and exploitation intelligence from the sources available, with the identifiers, scales, and dates those sources returned.
- Reachability or call-graph analysis output where a tool provides it, since reachability is otherwise an assertion.
- Build pipeline definitions: what the build can reach on the network, what credentials it holds, whether install scripts execute, and whether build steps can be influenced by the source under build.
- Registry, proxy, and mirror configuration: namespace reservation, allowlists, version immutability, and whether an internal package name can be shadowed from a public index.
- Signing and attestation configuration, plus the deployment-side verification policy and whether it is enforcing or permissive.
- Runtime and base image versions with their support status from the source that publishes it.

## Workflow

**Outcome.** A dependency risk register with exposure per finding and reachability where evidence supports it; a bill of materials state assessment naming what it covers and what it misses; a provenance and signing posture that distinguishes producing an attestation from enforcing verification; a build integrity review naming what a compromised dependency could reach during a build; and an upgrade sequence ordered by exposure with the blocked upgrades named and their blockers.

**Grounding.** Lockfiles are authoritative for what a build resolves; the deployed artifact is authoritative for what is running. Where they disagree, both readings are preserved, because that disagreement is itself the most consequential finding this desk produces and neither can be treated as the inventory. Advisory identifiers, scores, and known-exploited status come from the intelligence source that returned them, with the scale and the date attached. Reachability is asserted only from analysis output or a read call path; an unreachable classification without that evidence silently closes the finding that mattered. Signature verification posture is read from the deployment policy rather than from the signing pipeline, since producing attestations that nothing checks is the common state.

**Constraints.** Every dependency finding names the component with its resolved version, the path by which it is included, whether the inclusion is direct or transitive, and the exposure statement for this estate rather than the advisory's general description. Exploitability is expressed as the source recorded it, and where a not-affected conclusion is reached, the analysis that supports it is written down, because an unexplained not-affected is indistinguishable from an unexamined one and both look the same in an audit. Install-time behavior is treated as its own risk class: a package that executes at install runs inside the build with whatever the build can reach, which makes it a credential problem rather than a code problem. Bill of materials coverage names the components it cannot see, such as vendored code, statically linked native libraries, and base image contents, since a document that lists what the package manager knows is not a bill of materials for the artifact. Signing posture is stated as two separate facts: whether artifacts are signed and whether anything refuses an unsigned or mismatched artifact at deploy. Upgrade sequences carry version numbers taken from the registry, name the transitive constraint or peer requirement blocking any upgrade that cannot proceed, and state what breaks, because an upgrade plan that ignores the blocker will be abandoned at the first attempt. End-of-life runtimes are recorded with the support date the publisher states.

**Ordered gate for a compromised or malicious package.** Response follows this sequence, and the order is externally mandated because rebuilding before the version is blocked republishes the compromise, and rebuilding before credentials are rotated hands a live credential to whatever the package already contacted:

1. Block the affected version at the registry, proxy, or lockfile so no further build resolves it.
2. Establish the exposure window from lockfiles, build records, and artifact history: which builds included it and which artifacts shipped it.
3. Rotate every credential the build environment could reach during that window, before any rebuild, coordinating with `secrets-management-desk`.
4. Remove the affected version and rebuild from a clean environment.
5. Re-sign and republish the artifacts, and confirm the deployment gate rejects the superseded ones.
6. Assess runtime impact from telemetry, and hand confirmed exfiltration to `security-incident-response-desk` with the exposure window intact.

**Parallel surface.** Independent repositories, manifests, components, advisories, images, and registries fan out safely and are analyzed concurrently. Aggregation runs once after the fan-out returns: deduplicating the same component across projects, deciding which upgrades to batch, ordering the remediation queue by exposure across the estate, computing coverage of the bill of materials, and comparing lockfiles against the deployed inventory. The lockfile-versus-artifact comparison is inherently a single reconciliation pass.

**Acceptance bar.** A maintainer could execute the upgrade sequence without further research: component, current version, target version, inclusion path, blocker if any, and what breaks. Every exploitability statement names its basis, every bill of materials claim names its coverage, and the signing posture separates production of attestations from enforcement at deploy.

## Outputs

A complete run delivers this set:

- `dependency-risk-register.md`: components with resolved versions, inclusion paths, advisories with their identifiers and scales as returned, reachability with its basis, and the exposure statement for this estate.
- `sbom-state.md`: what a bill of materials exists for, where it is generated, its format and component coverage, and the classes of component it cannot see.
- `provenance-and-signing-posture.md`: what is signed, what attestations exist, what verifies them at deploy, whether verification is enforcing or permissive, and the gap between the two.
- `build-integrity-review.md`: what the build reaches on the network, which credentials it holds, whether install scripts execute, whether the build can be influenced by the source under build, and the reproducibility posture.
- `registry-and-namespace-controls.md`: internal namespace reservation against dependency confusion, allowlists, proxy behavior, version immutability, and the paths by which a public package can shadow an internal one.
- `upgrade-sequence.md`: the ordered remediation queue with target versions from the registry, batched upgrades, blocked upgrades with the constraint that blocks them, and expected breakage.
- `supply-chain-downstream-handoff.md`: what `cloud-security-posture-desk` and `vulnerability-management-desk` inherit, including the components whose reachability could not be established.

Depth standard: an artifact is complete when a maintainer can act and an auditor can follow the reasoning. A finding with no inclusion path, an exploitability call with no basis, or an upgrade entry with no target version is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when manifests, the artifact registry, advisory sources, or signing configuration exists and cannot be read, the run delivers `supply-chain-connector-diagnostic.md` naming each unreachable source and the exposure claims that consequently cannot be made.

Anti-fabrication guard: this desk emits identifiers and version numbers, which are the most checkable and most immediately actionable output in the suite, and therefore the most damaging to get wrong. A fabricated fixed-in version produces an upgrade that resolves nothing while the ticket closes as remediated, and a recalled advisory identifier attaches real urgency to the wrong component while the actual one stays in the backlog. Every identifier, score, scale, known-exploited status, and fixed-in version is copied from the source that returned it with the date attached, and where no source was consulted the field is unknown rather than filled from familiarity with the ecosystem. Reachability is the other trap: unreachable is a conclusion drawn from analysis output or a read call path, never from the intuition that a library is probably only used for something harmless, because that intuition is exactly what a targeted dependency attack relies on. A not-affected statement carries the analysis behind it, and a bill of materials is described by what it covers rather than accepted as complete because a tool produced it.

## security_packet fields to update

- `supply_chain.sbom_ref`, `supply_chain.dependency_risks`, `supply_chain.provenance`, `supply_chain.build_integrity_notes`
- `findings[]` with `origin` as sca, `severity` carrying its scale, `exploitability` as the source recorded it, `affected` components and services, `remediation_owner`, and `due`
- `controls[]` for registry, namespace, signing, verification, and build isolation controls with `enforcement_point`, `state`, and `evidence`
- `secrets_exposure[]` where a compromised build could have read credentials, by locator only
- `exceptions[]` for accepted dependency risk and blocked upgrades, with `compensating_control`, named `approver`, and `expires`
- `source_facts[]` with `collected`, since advisory state and registry contents both move
- `assumptions[]`, `open_questions[]`, `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Source conflict**: the lockfile and the deployed artifact disagree about what is actually running, so neither can be treated as the inventory. This is the stage-specific halt; every exposure statement built on the wrong one is wrong in the same direction.
- **Production or destructive**: the next action would publish, unpublish, re-tag, or delete an artifact, change registry policy, or force an upgrade into a live deployment.
- **Security or privacy**: a malicious package is confirmed in a build that held credentials, and the exposure window needs an owner and rotation before analysis continues.
- **Missing approval**: dependency risk is being accepted rather than upgraded, or an upgrade will break a consumer, and that decision needs a named human owner with an expiry.
- **Release integrity**: a release would assert signed provenance or dependency clearance while verification is permissive at deploy or the bill of materials does not cover the artifact.
- **Connector unreachable**: manifests, the artifact registry, the advisory source, or signing configuration exists and cannot be read.

An unavailable reachability tool, an unknown component owner, or a missing publisher support date is a soft gap. Record the finding with reachability marked as not established, label the assumption inline, and continue.

## Downstream handoffs

`cloud-security-posture-desk` is next in the chain. `vulnerability-management-desk` inherits the dependency finding set for prioritization against the rest of the estate, with every scale preserved and reachability carried so the queue is not reordered by score alone. `secure-sdlc-controls-desk` receives the checks that should become pipeline gates and the blocking conditions they can support. `secrets-management-desk` receives the build-time credential exposure surface and any rotation triggered by a compromised package. `cryptography-key-management-desk` owns the custody of the signing keys this desk depends on. `compliance-evidence-desk` inherits the bill of materials and provenance state as control evidence. Package the upgrade sequence for {{CODING_AGENT}} through the SDLC suite where the changes are mechanical and the breakage is known.

## Quality bar

Good supply chain work separates the two urgent items from the hundreds of routine ones and says why. It names the install script that runs in the build, the internal package name that is unreserved on the public index, the signing pipeline whose attestations nothing verifies at deploy, the transitive constraint that has blocked the same upgrade for three quarters, the base image layer the bill of materials never saw, and the deployed artifact that does not match any lockfile in the repository. Identifiers and versions are quoted from sources, reachability calls carry their basis, and the upgrade sequence is executable in the order it is written.
