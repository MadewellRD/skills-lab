---
name: product-requirements-desk
description: create connector-grounded product requirements documents for software work. use when the user needs a prd, requirement ids, acceptance criteria, non-goals, risks, open questions, source facts, stakeholder decision synthesis, or downstream handoff notes before technical discovery, architecture, issue planning, implementation, testing, verification, or release work.
---

# Product Requirements Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Role

Turn product ideas, customer notes, GitHub issues, roadmap context, stakeholder decisions, uploaded docs, and repo/product context into connector-grounded PRDs and requirement artifacts.

This desk is an upstream SDLC skill. Do not write implementation prompts, branch plans, or pull request instructions unless the user explicitly asks for a downstream handoff summary. When execution-ready implementation work appears after requirements are settled, continue into the implementation handoff stage or emit a workflow packet for that stage.

## Workflow

**Outcome.** A connector-grounded requirements artifact — a new PRD from a raw idea, a PRD refined from existing docs or issues, generated acceptance criteria, a requirement normalization or review, or a connector diagnostic when required context cannot be reached.

**Grounding.** Use GitHub issues and repo context for product-facing bugs, feature requests, milestones, related code boundaries, and existing issue labels. Use docs connectors or uploaded files for roadmap, customer, policy, architecture, or stakeholder decision context. Use communication connectors only for decision-bearing messages, and record speaker, date, and context when available.

**Source facts.** Separate verified facts from assumptions, preserve the source hierarchy in `references/source-hierarchy.md`, and mark conflicting facts explicitly rather than resolving them silently.

**Templates.** Use `references/prd-template.md` for PRDs, `references/output-contract.md` for output modes and file wrappers, and `references/downstream-handoff.md` when preparing the next SDLC desk handoff.

**Parallel surface.** Evidence retrieval across independent sources — GitHub issues, docs, uploaded files, decision messages — carries no ordering dependency, and acceptance criteria for distinct requirement IDs are independent of each other. Fan out over both rather than iterating serially.

**Acceptance bar.** The PRD is done when every requirement carries a stable ID; each requirement has acceptance criteria that are testable without further product input; non-goals, risks, and open questions are explicit rather than implied; every load-bearing fact is attributed to its source; and assumptions are labeled inline as assumptions. Do not invent users, acceptance criteria, issue IDs, roadmap commitments, release dates, dependencies, owners, or compliance requirements.

## Halt policy

Proceed by default. A requirement gap is normally recorded as an open question with a labeled working assumption, not a stop. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval** — a scope, commitment, or policy decision requires a human owner to authorize.
- **Production or destructive** — the request would write to a live tracker, roadmap, or customer-facing commitment.
- **Security or privacy** — the requirements would encode handling of secrets or personal data that is not sourced.
- **Source conflict** — stakeholder decisions, docs, or issues genuinely disagree on a load-bearing requirement.
- **Release integrity** — acceptance criteria would be stated as agreed when no source establishes agreement.
- **Connector unreachable** — a required source exists but cannot be read. Context that is merely absent is a soft gap: continue with a labeled assumption or emit `connector-diagnostic.md`.

See `references/halt-conditions.md` for the artifact format a halt must take.

## Default output modes

- `product-requirements-document.md`
- `acceptance-criteria.md`
- `requirements-review.md`
- `requirements-source-facts.md`
- `connector-diagnostic.md`

Every downloadable Markdown artifact must start with a short "How to use this file" section.

## Downstream handoff density

Keep downstream handoffs compact. The goal is to reduce ambiguity before coding agents spend tokens. Use requirement IDs, concise acceptance criteria, explicit non-goals, source facts, and exact open questions rather than long narrative restatement.

## Bundled resources

- `references/prd-template.md` — canonical PRD structure.
- `references/connector-routing.md` — which connectors to use and what facts to retrieve.
- `references/source-hierarchy.md` — source priority and conflict behavior.
- `references/output-contract.md` — artifact names and wrappers.
- `references/halt-conditions.md` — missing-context and conflict halts.
- `references/downstream-handoff.md` — handoff format for later SDLC desks.
- `scripts/write_prd_markdown.py` — deterministic Markdown wrapper for PRD artifacts.

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `{{BLOCKER_TAG}}` when implementation handoff facts are insufficient for a coding agent.
