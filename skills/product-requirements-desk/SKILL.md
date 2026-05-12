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

1. Classify the request.
   - New PRD from raw idea.
   - PRD refinement from existing docs or issues.
   - Acceptance criteria generation.
   - Requirement normalization or review.
   - Connector diagnostic because required context is missing.

2. Run connector preflight.
   - Use GitHub issues and repo context for product-facing bugs, feature requests, milestones, related code boundaries, and existing issue labels.
   - Use docs connectors or uploaded files for roadmap, customer, policy, architecture, or stakeholder decision context.
   - Use communication connectors only for decision-bearing messages and cite/record speaker, date, and context when available.

3. Build source facts.
   - Separate verified facts from assumptions.
   - Preserve source hierarchy from `references/source-hierarchy.md`.
   - Mark conflicting facts explicitly.

4. Produce the requested artifact.
   - Use `references/prd-template.md` for PRDs.
   - Use `references/output-contract.md` for output modes and file wrappers.
   - Use `references/downstream-handoff.md` when preparing the next SDLC desk handoff.

5. Halt when requirement-critical facts are missing.
   - Use `references/halt-conditions.md`.
   - Do not invent users, acceptance criteria, issue IDs, roadmap commitments, release dates, dependencies, owners, or compliance requirements.

## Default output modes

- `product-requirements-document.md`
- `acceptance-criteria.md`
- `requirements-review.md`
- `requirements-source-facts.md`
- `connector-diagnostic.md`

Every downloadable Markdown artifact must start with a short "How to use this file" section.

## Low-token downstream policy

Keep downstream handoffs compact. The goal is to reduce ambiguity before coding agents spend tokens. Use requirement IDs, concise acceptance criteria, explicit non-goals, source facts, and exact open questions rather than long narrative restatement.

## Bundled resources

- `references/prd-template.md` — canonical PRD structure.
- `references/connector-routing.md` — which connectors to use and what facts to retrieve.
- `references/source-hierarchy.md` — source priority and conflict behavior.
- `references/output-contract.md` — artifact names and wrappers.
- `references/halt-conditions.md` — missing-context and conflict halts.
- `references/downstream-handoff.md` — handoff format for later SDLC desks.
- `scripts/write_prd_markdown.py` — deterministic Markdown wrapper for PRD artifacts.
