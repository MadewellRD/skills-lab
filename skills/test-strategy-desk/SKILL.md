---
name: test-strategy-desk
description: create connector-grounded test strategies, qa scenario matrices, regression plans, fixture plans, coverage-gap reports, and verification handoff notes from product requirements, architecture specs, issue plans, pull requests, repository tests, ci results, bug reports, and known regressions. use when chatgpt needs to define what should be tested, map requirements to test coverage, identify missing tests, plan regression scope, design fixtures, classify test risk, or prepare downstream handoff notes for verification-desk, review-quality-desk, ci-failure-desk, or implementation-handoff-desk workflows.
---

# Test Strategy Desk

## Suite workflow mode

This desk is part of the SDLC Command Desk workflow suite. When invoked from an end-to-end workflow, do not stop with only a bare next-desk instruction. Complete this desk's artifact, emit a workflow packet, and continue to the next stage when enough facts are available.

If the next stage cannot be completed because required facts, connector access, approval, or source evidence are missing, return `Workflow Halt` with specific resume requirements. Use `references/suite-workflow-contract.md` for the packet, continuation, and halt format.


## Role

Use this skill to turn requirements, design intent, repo state, and failure history into a precise test strategy before implementation, review, or release. The skill produces test-planning artifacts, not implementation code, unless the user explicitly asks for test-writing handoff material.

Default outputs are Markdown artifacts: test strategy, QA scenario matrix, regression plan, fixture plan, coverage-gap report, and downstream handoff notes. When the output is intended for another agent, wrap it as a downloadable Markdown file with a short `How to use this file` section.

## Connector preflight

Before producing a test artifact, identify which sources are required.

Use GitHub when the plan depends on repository truth: existing test files, changed files, PR diffs, issues, labels, commit history, CI checks, flaky failures, or prior regressions. Use document connectors or uploaded files when the plan depends on PRDs, SRS/SDS, architecture docs, QA plans, acceptance criteria, release docs, or audit material. Use communication connectors only for decision context, triage notes, halt reports, or stakeholder clarifications.

If required source facts are unavailable, either produce a clearly marked user-fact-only draft or a connector diagnostic. Do not invent test names, file paths, coverage claims, CI status, defect history, or acceptance criteria.

## Workflow

1. Classify the request.
   Decide whether the user needs a full test strategy, targeted regression plan, QA scenario matrix, fixture design, coverage-gap report, or downstream PR handoff.

2. Gather source facts.
   Follow `references/connector-routing.md` and `references/source-hierarchy.md`. Capture requirements, changed areas, existing tests, known failures, CI status, risk areas, and release constraints.

3. Build the risk model.
   Group risk by user impact, technical complexity, data migration risk, security/privacy exposure, integration surface, regression history, observability, and reversibility. Use `references/risk-rubric.md` when ranking coverage priority.

4. Map requirements to tests.
   Use `references/test-strategy-template.md` and `references/coverage-gap-template.md`. Every material requirement should have one of: covered, partially covered, not covered, intentionally deferred, or needs clarification.

5. Define scenarios and fixtures.
   Use `references/scenario-matrix-template.md` and `references/fixture-plan-template.md`. Include positive, negative, edge, regression, integration, accessibility, security/privacy, performance, and migration scenarios only when relevant.

6. Produce handoff notes.
   For downstream implementation, verification, review, or CI work, include the exact artifact to hand off and state which skill should consume it next. Use `references/handoff-rules.md`.

7. Apply halt behavior.
   Use `references/halt-conditions.md` whenever missing source facts or conflicts would make the plan unsafe.

## Output rules

Prefer concise, audit-ready artifacts. Include source facts and assumptions. Separate verified facts from recommendations. Do not claim local or CI validation unless the connector or user provided the result.

When creating a file for the user, use `scripts/write_test_strategy_markdown.py` to wrap the artifact with:

- title
- how to use this file
- source facts
- unverified assumptions
- main artifact body

## Composition with other SDLC skills

- Consume PRDs from `product-requirements-desk`.
- Consume architecture and interface context from `architecture-design-desk`.
- Consume issue scope and acceptance gates from `issue-planning-desk`.
- Feed missing-test findings to `review-quality-desk`.
- Feed V&V-ready test mapping to `verification-desk`.
- Feed CI failure minimization or flaky-test findings to `ci-failure-desk`.
- Feed implementation-agent test-writing prompts to `implementation-handoff-desk`.

## Required references

Read only the references needed for the current request:

- `references/test-strategy-template.md`
- `references/scenario-matrix-template.md`
- `references/regression-plan-template.md`
- `references/fixture-plan-template.md`
- `references/coverage-gap-template.md`
- `references/risk-rubric.md`
- `references/connector-routing.md`
- `references/source-hierarchy.md`
- `references/output-contract.md`
- `references/handoff-rules.md`
- `references/halt-conditions.md`
