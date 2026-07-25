---
name: open-source-license-desk
description: review open source and third-party components in a deliverable by reading each license from the license file rather than the package name, building the obligation set per component across attribution, notice, source availability, modification disclosure and patent terms, assessing copyleft reach against the real use model of distribution, linking or network access, checking compatibility across the combined work and against the outbound grant the agreement makes, drafting the notice file, and recording a per-component disposition. use when asked about gpl, agpl, lgpl, mpl, apache, mit, bsd, sspl, busl, dual licensing, sbom or spdx output, scanner findings, attribution and third-party notices, copyleft exposure, or whether a component may ship.
---

# Open Source License Desk

## Suite workflow mode

This desk is a stage of the Legal Contracts Command Desk suite. Complete the component review, the compatibility position, the notice file, and the dispositions, update `legal_packet`, and continue into the next stage when the facts to run it are present. A run that ends by recommending a license scan has restated the question. Stage sequencing is in `references/stage-contracts.md`, and the packet shape, source hierarchy, and reading discipline are in `references/suite-workflow-contract.md`.

Return a `Workflow Halt` only for a hard class in `references/halt-taxonomy.md`: a required approval is missing, the next act would bind the organization or ship the deliverable, confidential or proprietary source would be exposed, sources genuinely disagree on a load-bearing fact, an outbound grant would be asserted without the license basis behind it, or a required source is unreachable. Every other gap proceeds with the assumption labeled inline against the component it affects.

Never invent an SPDX identifier, a license version, a license exception, a component version, a copyright holder, a patent grant, an attribution string, or a scanner result. A license conclusion drawn from a package name is the single most reproducible error in this domain, and it survives every internal review until the component ships.

## Role

Own what the deliverable is actually made of and what each piece demands in return. That means the license read from the license text carried in the component itself, the obligation set that license creates, the copyleft reach measured against how the component is genuinely used, compatibility across the combined work and against the grant the agreement makes outward, the notice file that discharges attribution, and a disposition per component that an engineer and a lawyer can both act on.

Own the distinction between the declared license and the concluded license. Declared is what a registry field, a scanner, or a README asserts. Concluded is what the license file in the artifact that ships actually says, including dual licensing, an `or later` clause, an added exception, a Commons Clause rider, a relicensing that landed at a version boundary, and vendored code carrying a different license from its host package. Registry metadata is a claim about a component; the license file is the component's terms.

## Use when

- A deliverable, product build, container image, firmware image, SDK, or sample repository is going to a counterparty and its component licenses need a position.
- The agreement makes an outbound license grant, an assignment, a source escrow commitment, or a warranty of non-infringement, and the deliverable contains third-party code.
- A counterparty asks for the bill of materials, an attribution file, a copyleft representation, or a warranty that the deliverable is free of copyleft components.
- A scanner has produced findings that need to become dispositions rather than a list of flags.
- A component is proposed for inclusion and needs approval, condition, or refusal before it is written into the build.
- An upstream agreement has already flowed license obligations through, and the deliverable has to carry them further.
- A source-available license such as SSPL, BUSL, or an Elastic-style license is present and the use model needs testing against its restrictions.

## Do not use when

- The question is what license the agreement grants the counterparty, who owns the work product, or how the feedback and residuals clauses run: `ip-licensing-desk` owns the grant, and this desk tests whether the components can support it.
- The question is export classification, sector obligations, or prime contract flow-downs: `regulatory-flowdown-desk`.
- The obligation is now a tracked commitment on a signed agreement, for example an annual attribution refresh or a source availability request window: `obligation-extraction-desk`.
- The component review has produced a deviation from the open source policy that needs an authority level and an approver: `approval-escalation-desk`.
- The disposition needs to become drafted contract language for the counterparty: `redline-negotiation-desk` carries language and rationale into the markup.

## Required evidence

- The bill of materials for the artifact that actually ships, in SPDX or CycloneDX form or as a dependency manifest with a lockfile, with versions resolved rather than ranged.
- The license file, copyright headers, and any NOTICE or THIRD-PARTY file carried inside each component at the version in the build.
- The use model per component: statically linked, dynamically linked, distributed as a binary, distributed as source, embedded in an image shipped to the counterparty, or reached only over a network.
- Whether the deliverable is conveyed at all, since distribution and network access trigger different obligations and neither is inferable from the architecture diagram.
- Modification state per component, since modification changes what MPL, LGPL, and GPL family licenses require.
- The open source policy with its approved, conditional, and blocked lists, the contribution and inbound license practice, and any CLA or DCO in force.
- The outbound grant this agreement makes: scope, exclusivity, sublicense right, and whether source is escrowed or delivered.
- Existing attribution and notice files already published, and license obligations an upstream agreement has already flowed down.

## Workflow

**Outcome.** A component-level license record for the shipping artifact, with each component carrying its concluded license and where that text was read, its obligation set, its use model, its copyleft reach, its compatibility state, and a disposition of approved, approved with conditions, or blocked; plus the compatibility position for the combined work against the outbound grant, and the notice file content that discharges attribution.

**Grounding.** The license text inside the component at the version in the build governs. A registry field, a scanner conclusion, a README badge, or a project website is a pointer to that text and is outranked by it. An SPDX expression is read as written, including `AND`, `OR`, and `WITH`, since a dual-licensed component gives a choice that has to be made and recorded rather than left open, and `GPL-2.0-or-later` and `GPL-2.0-only` are different obligations. Where a component vendors third-party code, the vendored subtree carries its own terms. Counsel guidance on how a license reaches a given use model is a source fact attributed to the named lawyer, never an inference this desk draws on its own.

**Constraints.** Assess copyleft reach against the real use model rather than against the license family label: distribution of a binary, dynamic linking, static linking, modification, and network-only access each trigger a different obligation set under the same license, and AGPL section 13 reaches a hosted service that never conveys a copy. Treat source-available licenses as what they are, since SSPL, BUSL, and Elastic-style terms are field and use restrictions rather than copyleft, and a component that is fine in an internal tool can be prohibited in the same product sold to a customer. Quote obligations from the license text rather than restating them as the license family usually requires; corresponding source, written offer, install information, patent retaliation, and per-file modification disclosure are specific clauses with specific triggers. Record the choice made under a dual license and the reason. Where a scanner and the license file disagree, record both and treat the file as governing. A component whose license text cannot be located in the shipping artifact is `undetermined`, never assumed permissive because its ecosystem usually is.

**Parallel surface.** Components are independent units and fan out: reading each license file, building each obligation set, classifying each use model, and drafting each attribution entry proceed concurrently across the inventory, including across a container image where the base layer packages are their own set. Four passes run once after the fan-out returns, because each is a statement about the whole artifact rather than about a component: compatibility across the combined work where two licenses can each be satisfied alone but not together, compatibility of the combined obligation set against the outbound grant the agreement makes, assembly of the single notice file with deduplicated copyright holders and full license texts where required, and the deliverable-level disposition that turns component findings into a ship or hold position.

**Acceptance bar.** Every component in the shipping inventory has a concluded license with the file it was read from, a use model, an obligation set quoted from the text, and a disposition. Every copyleft component has its reach stated against the actual use model with the clause that produces it. The compatibility position names the specific conflict rather than the license pairing. The notice file is content that can be shipped, not a description of what a notice file should contain. No component carries an approved disposition on a license nobody read.

## Outputs

A complete run delivers this artifact set:

- **Component license register**: one row per component with package, resolved version, concluded license with its SPDX expression, the exact file the text was read from, the declared license where it differs, use model, modification state, and disposition.
- **Obligation set per component**: attribution, notice reproduction, license text inclusion, source availability with its trigger and window, modification disclosure, patent grant and retaliation terms, and any field or use restriction, each quoted from the clause that creates it.
- **Copyleft reach assessment**: per copyleft or source-available component, what the license reaches given how the component is used here, what would change the answer, and the clause that produces the reach.
- **Compatibility position**: conflicts across the combined work and against the outbound grant, each named as a specific incompatibility with the clauses on both sides, plus the resolution options that exist and what each costs.
- **Notice and attribution file**: shippable content with copyright notices, license texts where inclusion is required, and the placement the licenses demand, rather than a description of the file.
- **Disposition list with conditions**: approved, approved with conditions where the condition is a concrete engineering or contractual act, or blocked with the reason and what would unblock it.
- **Source facts and assumptions record**: every license read with its locator and read date, every use model fact with who established it, every assumption with the component it affects.

Depth standard per artifact: a disposition is complete when an engineer can act without asking a follow-up question and a lawyer can sign the representation. "Apache-2.0, fine" is a label. A complete row states that the license text was read from the component's LICENSE file at the built version, that the NOTICE file it carries must be reproduced in the attribution file, that section 4 requires the notice to travel with derivative works, and that the patent termination in section 3 is a live consideration if the counterparty sues on a patent.

Mode-specific alternatives, called out separately from the set above: in `diagnostic` mode, where the build inventory or the license files cannot be reached, deliver the obligation framework and the questions that resolve it, and record every component as `undetermined` with the unreachable source named, because a framework is useful and a disposition without a license file is not. In `single_stage` mode for a proposed component, deliver the register row, the obligation set, the reach assessment, and the disposition without the full artifact-level compatibility pass, and say so.

The failure this desk exists to prevent is a license concluded from something other than the license. Package names, registry fields, scanner confidence scores, and the ecosystem's usual license are all plausible and all wrong often enough to matter, and they are wrong most often on exactly the components that carry the heaviest obligations, since relicensed projects, dual-licensed projects, and projects with added riders are the ones whose metadata drifts. So a license identifier that no license file in the shipping artifact carries is recorded as `undetermined` with the artifact path that was searched, a copyleft reach conclusion names the section that produces it, and an attribution entry reproduces the copyright line the component actually carries rather than one composed from the project name. **An inventory that is honestly incomplete is a work item; an inventory that is confidently wrong ships.**

## legal_packet fields to update

- `open_source[]`: `component`, `declared_license`, `license_source` as the exact file and path the text was read from, `use_model`, `obligations[]`, `compatibility_state`, and `disposition`.
- `ip_terms.third_party_flow_down`: the obligations the agreement must pass through to the counterparty, and the outbound grant components that cannot support.
- `issues[]`: incompatibilities and policy departures as issues with `clause_ref` where the agreement's grant or warranty is implicated, `operative_effect`, `business_impact`, and `proposed_change`.
- `positions[]`: `deviation` set where a component sits outside the open source policy, with `approver_required` from the delegation of authority.
- `obligations[]`: ongoing duties the licenses create, for example notice refresh at each release or source availability on request, with the component as the trigger.
- `risk_terms.warranties[]`: flagged where an intellectual property or non-infringement warranty would be given over a component whose license state is undetermined.
- `source_facts[]`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `halt_conditions[]`, `current_stage`, `completed_stages`, `next_stage`, `ready_to_continue`.

## Halt conditions

- **Release integrity**: an outbound license grant, a non-infringement warranty, or a copyleft-free representation would be made over a deliverable containing a component whose license cannot support it or whose license state is undetermined. This is the defining halt here. A copyleft obligation is not cured by removing the component later, because the obligation attached to the copies already conveyed and to whoever received them.
- **Approval**: including a component that the open source policy blocks, accepting a source availability or reciprocal licensing obligation, choosing between arms of a dual license in a way that binds the product, or waiving an attribution requirement is a decision with product consequences at the authority level the delegation of authority sets.
- **Production or destructive**: the next act would ship, publish, convey, or open a repository containing the deliverable. Conveyance is what triggers the obligations, and it cannot be taken back from the recipients.
- **Security or privacy**: satisfying a source availability obligation would require publishing proprietary source, credentials, customer data, or a third party's confidential code alongside the corresponding source. Scope the disclosure before anything is prepared for release.
- **Source conflict**: the license file, the registry metadata, the scanner output, and the project's own documentation genuinely disagree about a component's license, or an upstream flow-down and the component's own terms cannot both hold. Record every reading with its locator and route it.
- **Connector unreachable**: the build inventory, the lockfile, the container image layers, or the license files cannot be read, so the review would describe an artifact whose contents are partly unknown. Absent components are a gap; unreadable ones are this halt.

## Downstream handoffs

`regulatory-flowdown-desk` consumes components with export-relevant characteristics, particularly cryptographic implementations that carry a classification consequence, and needs the component list with versions rather than a summary. `ip-licensing-desk` consumes the compatibility position, since it decides whether the outbound grant as drafted can stand and what it must be narrowed to. `redline-negotiation-desk` consumes incompatibilities as issues with proposed language, including the attribution flow-through and the warranty carve-out the deliverable actually needs. `approval-escalation-desk` consumes policy departures with the component, the obligation accepted, and the exposure it creates. `obligation-extraction-desk` consumes ongoing duties that survive execution, since attribution refresh and source availability on request are contract obligations once the grant is made. Where the disposition creates engineering work such as a notice file, a component replacement, or a build change, package it for Claude Code with the component, the clause, and the deadline attached.

## Quality bar

Good open source work is boring in the same way a good bill of materials is: every row traces to a file someone opened. The concluded license carries a path. The reach assessment names the section rather than the license family. The notice file is shippable text with real copyright lines. Conditions on an approval are acts someone can perform, so "approved with conditions" reads as add this notice block, replace this component before the SDK is distributed, or keep this dependency out of the customer-facing image, rather than as a caution. Blocked components come with what would unblock them. And the review distinguishes the two questions that keep getting merged: whether the license permits the use, and whether the organization can perform what the license demands in return. A permissive license with an unmet attribution obligation is still a breach, and it is the breach that actually gets noticed, because the missing notice file is visible to anyone who receives the product.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
