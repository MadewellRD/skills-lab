# Product Requirements Desk

`product-requirements-desk` turns rough product intent, customer notes, GitHub issues, roadmap context, stakeholder decisions, uploaded docs, and repo context into grounded product requirements artifacts.

## Lifecycle coverage

- Product requirements
- Acceptance criteria
- Requirement IDs
- Non-goals
- Risk and open-question capture
- Downstream handoff preparation

## Intended inputs

- Raw idea or feature brief
- Existing GitHub issues or milestones
- Customer/support notes
- Roadmap or strategy docs
- Stakeholder decisions
- Uploaded notes, specs, or product docs

## Intended outputs

- `product-requirements-document.md`
- `acceptance-criteria.md`
- `requirements-review.md`
- `requirements-source-facts.md`
- `connector-diagnostic.md`

## Required connectors

Use GitHub when product work depends on issues, repo state, milestones, labels, or existing implementation boundaries. Use docs/uploaded files for roadmap, product, and stakeholder context. Use communication sources only for decision-bearing messages.

## Composition

This skill feeds `technical-discovery-desk`, `architecture-design-desk`, `issue-planning-desk`, `test-strategy-desk`, `verification-desk`, and `implementation-handoff-desk`.


## Suite workflow integration

This skill is linked into the SDLC Command Desk workflow. In end-to-end mode, it should complete its stage, preserve a workflow packet, and continue when the next stage is sufficiently grounded. It should not only tell the user to use another desk next.
