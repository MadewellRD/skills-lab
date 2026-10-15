---
name: repo-governance-desk
description: load and enforce a repository's declared governance profile (decision ledger, gate of record, hard invariants, authority model) across the SDLC Command Desk workflow. use when Gemini works in a governed repository, when a repo declares a decision ledger or a local gate receipt instead of hosted CI, when a stage would touch a declared invariant, when a decision must be drafted in the ledger's own format for a named ratifier, or when a deploy must be run by an operator and verified from evidence on disk.
---

# Repo Governance Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. It is an overlay: it does not replace a lifecycle stage, it constrains every stage that runs in a governed repository. When invoked from an end-to-end workflow, load the profile first, then continue to the stage the request needs with the profile's rules in force. Return `Workflow Halt` only under the halt classes in `references/halt-invariant.md` and the suite halt taxonomy.

## Purpose

A conventional repository trusts hosted CI checks, treats live GitHub state as the top source of truth, lets one agent drive the lifecycle, and records decisions as ADRs. A governed repository declares its own authority of record: a decision ledger with a house format, a local gate whose receipt is the only evidence of a passing build, hard invariants that no stage may work around, and an authority model that splits issuing work, drafting decisions, ratifying them, and merging between different people or agents. Running the suite's defaults against such a repository produces work the repository cannot accept.

This desk reads the repository's governance profile and makes every other desk honor it.

## Operating rules

- Read the profile before any other stage runs. The profile is the repository's `GOVERNANCE.md`, or the governance section of its contributor instructions, or a profile the user supplies. Parse it with `references/governance-profile-schema.md`. If no profile exists, say so once and let the suite run its defaults.
- Apply the profile's source hierarchy. For the domains the profile names, the ledger and the gate receipt outrank live GitHub state. For everything else, the suite hierarchy applies. Never rank a hosted check above a local receipt when the profile says the receipt is the gate of record.
- Treat every declared invariant as a halt boundary. A stage that would violate, weaken, or route around an invariant halts under `references/halt-invariant.md` and proposes a decision instead. Never propose a workaround that evades an invariant.
- Honor the authority model. Do not draft a decision when the profile assigns drafting elsewhere; do not ratify; do not merge; do not record a draft in the ledger. Produce the artifact the profile allows this role to produce and hand the rest to the named role.
- Draft decisions in the ledger's house format from `references/decision-drafting.md`, never in the ADR template, and mark every draft unratified.
- Certify merges only by the gate of record using `references/gate-of-record.md`: receipt names the exact commit, clean tree, tree-equality for squash merges, artifacts bound by hash.
- Apply `references/review-checks.md` to every review of returned work in a governed repository. These checks exist because each one caught a defect that reading the code missed.
- When the profile forbids the agent from running a deploy, use `references/operator-field-verification.md`: the operator runs blocks, evidence lands on disk, the agent verifies from disk and never from narrative.
- Never edit the ledger, the state file, or the tracker unless the profile names this role as their writer.

## Workflow

**Outcome.** A governance-conformant run of whatever lifecycle stage the user asked for, plus a governance record stating which profile rules applied, which invariants were touched, and which artifacts went to which role.

**Load.** Locate the profile. Extract: ledger path and entry format; gate of record and receipt location and fields; invariants; authority model (issuer, drafter, ratifier, merger, state writer); packet convention; branch and merge convention; deploy model (agent-run or operator-run); line-ending and style rules. Record every field as found or missing. A missing field is a soft gap carried in the packet with the suite default labeled as such.

**Bind.** Rewrite the stage plan against the profile. For each stage in the run, state the inputs the profile adds (for example the receipt as a required input to release readiness), the outputs it changes (a ledger entry instead of an ADR, a packet instead of a handoff prompt), and the invariants in scope. Decide the halt boundaries before the stage starts, not when it hits them.

**Run.** Execute the stages with the bound rules. Each stage artifact carries a `Governance` section: profile version, invariants in force, authority role producing it, and the evidence of record it relied on.

**Certify.** Before any merge or release claim, apply the gate-of-record checks and record the result verbatim in the packet: receipt sha, head sha, tree-equality result, artifact hashes.

**Parallel surface.** Profile loading is a single pass. Invariant screening of a proposed change is parallel across invariants: each invariant is checked independently and any single violation halts. Review checks are parallel-safe across the checklist.

**Acceptance bar.** The run is complete when every stage artifact carries its Governance section, no invariant was worked around (a violation either halted or became a drafted decision), every decision draft is in house format and marked unratified, every merge or release claim cites the gate of record, and every deploy claim cites evidence on disk. A run that cites a hosted check as proof in a receipt-gated repository is not complete.

## Connector requirements

- Repository access (GitHub or a local tree) is required to read the profile, the ledger, the receipt, and the tracked files.
- A local shell on the repository host is required for receipt verification, tree-equality checks, and artifact hashing; without it those checks are reported as not performed, never as passed.
- Document sources are required when the profile points at external specs.
- Communication sources are decision context only.

## Output artifacts

- `governance-record.md`: profile fields found and missing, rules applied, invariants in scope, roles and handoffs.
- `invariant-screen.md`: each invariant against the proposed change, with verdict unchanged, strengthened, amended by decision, or violated (halt).
- `decision-draft.md`: when a decision is needed and this role may draft, the ledger-format draft with the unratified marker and a "For the ratifier" section.
- `gate-certification.md`: when a merge or release is in scope, the receipt and tree-equality evidence.
- `field-verification.md`: when a deploy is operator-run, the block scripts issued and the evidence verified from disk.
- The stage artifacts of whichever lifecycle desks ran, each with its Governance section.

`governance-halt.md` is conditional: produced when an invariant halt or an authority halt stops the run, stating the invariant or role, the decision question it raises, and the resume requirement.

## Quality bar

Every artifact from this desk must include:

- the profile source and the fields it was read from
- the invariants in scope, by their declared wording
- the authority role producing the artifact and the role that acts next
- the evidence of record cited by sha, path, or receipt field, never by narrative
- assumptions labeled as such with the suite default they replaced

A Governance section that names no invariant and no evidence has not been applied; it has been pasted.

## References

- `references/governance-profile-schema.md`: what a profile declares and how to read it.
- `references/governance-profile-example.md`: a complete illustrative profile for a governed repository.
- `references/halt-invariant.md`: the invariant and authority halt classes added to the suite taxonomy.
- `references/gate-of-record.md`: receipt-based gates, tree-equality, artifact binding.
- `references/decision-drafting.md`: ledger house format and the drafter, ratifier, recorder split.
- `references/review-checks.md`: review checks for returned work, each with the defect that justified it.
- `references/packet-convention.md`: the work packet shape that replaces a bare coding-agent prompt.
- `references/operator-field-verification.md`: the two-block operator deploy and verification from disk.
- `references/output-contract.md`: artifact formats.
- `references/suite-workflow-contract.md`: shared workflow packet, continuation, and halt contract for SDLC Command Desk suite orchestration.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. The governance halt classes in `references/halt-invariant.md` are additive to the halt taxonomy: an invariant, authority, or evidence-of-record halt is always hard. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
