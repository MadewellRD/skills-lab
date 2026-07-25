---
name: test-strategy-desk
description: create connector-grounded test strategies, qa scenario matrices, regression plans, fixture plans, coverage-gap reports, and verification handoff notes from product requirements, architecture specs, issue plans, pull requests, repository tests, ci results, bug reports, and known regressions. use when the assistant needs to define what should be tested, map requirements to test coverage, identify missing tests, plan regression scope, design fixtures, classify test risk, or prepare downstream handoff notes for verification-desk, review-quality-desk, ci-failure-desk, or implementation-handoff-desk workflows.
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

**Outcome.** The test artifact the request calls for: a full test strategy, targeted regression plan, QA scenario matrix, fixture design, coverage-gap report, or downstream PR handoff.

**Grounding.** Follow `references/connector-routing.md` and `references/source-hierarchy.md`. Capture requirements, changed areas, existing tests, known failures, CI status, risk areas, and release constraints.

**Risk model.** Group risk by user impact, technical complexity, data migration risk, security/privacy exposure, integration surface, regression history, observability, and reversibility. Use `references/risk-rubric.md` when ranking coverage priority.

**Requirement mapping.** Use `references/test-strategy-template.md` and `references/coverage-gap-template.md`. Every material requirement carries exactly one of: covered, partially covered, not covered, intentionally deferred, or needs clarification.

**Scenarios and fixtures.** Use `references/scenario-matrix-template.md` and `references/fixture-plan-template.md`. Include positive, negative, edge, regression, integration, accessibility, security/privacy, performance, and migration scenarios only when relevant.

**Parallel surface.** Requirements, changed files, and scenario families are independent: each requirement's coverage classification and each file's existing-test discovery stand alone. Map them in parallel rather than iterating, then assemble the ranked coverage-gap view once.

**Handoff.** For downstream implementation, verification, review, or CI work, name the exact artifact to hand off and which skill consumes it next. Use `references/handoff-rules.md`.

**Acceptance bar.** The strategy is done when every material requirement has a coverage classification with the specific test or gap named; each gap carries a risk rank from `references/risk-rubric.md` rather than an undifferentiated list; scenarios are concrete enough to execute without further design; fixtures name their data shape and provenance; and existing coverage is distinguished from proposed coverage. Do not invent test names, file paths, coverage claims, CI status, defect history, or acceptance criteria, and do not claim local or CI validation unless the connector or user supplied the result.

## Halt behavior

Proceed by default. A requirement whose coverage cannot be determined is classified `needs clarification` and the plan continues. Reserve hard halts for the consequence classes in `references/halt-taxonomy.md`:

- **Approval**: deferring coverage on a material requirement needs a human owner to accept the risk.
- **Production or destructive**: the plan would run tests against production data or systems, or fixtures would require copying live data.
- **Security or privacy**: fixtures or scenarios would require real secrets, credentials, or personal data.
- **Source conflict**: requirements, issue scope, and existing tests genuinely disagree on intended behavior.
- **Release integrity**: the plan would be presented as release-gating coverage when the evidence cannot establish that the gates pass.
- **Connector unreachable**: a required repo, CI, or spec source exists but cannot be read. A source that is merely absent is a soft gap: produce a user-fact-only draft marked as such and continue.

Use `references/halt-conditions.md` for the halt artifact format.

## Output rules

A strategy run delivers the set together: the test strategy, the requirement-to-coverage map with every material requirement classified, the scenario matrix, the fixture plan, the ranked coverage-gap report, and the handoff to whichever desk consumes it next. A coverage-gap report without the scenarios that would close the gaps is a list of complaints; a scenario matrix with no requirement mapping cannot be checked for completeness. A targeted regression plan is this same set narrowed to a specific change, not a lighter substitute for it.

Prefer concise, audit-ready artifacts. Include source facts and assumptions. Separate verified facts from recommendations. Do not claim local or CI validation unless the connector or user provided the result.

Depth is measured by whether a tester can execute without redesigning. A scenario states preconditions, steps, and the expected result. A fixture names its data shape, its provenance, and how it is reset. A gap carries its risk rank from `references/risk-rubric.md` rather than sitting in an undifferentiated list. "Add integration tests for the checkout flow" is a gap, not a scenario.

Requirements, changed files, and scenario families are independent, so the artifacts in the set are mapped in parallel and assembled into the ranked view once.

Producing the whole set never converts absence into coverage. Test names, file paths, coverage claims, CI status, and defect history are sourced or absent, existing coverage stays separate from proposed coverage, and a requirement with no test is classified `not covered` rather than given a plausible one. A strategy that overstates coverage is worse than no strategy, because it retires a risk nobody is actually watching.

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

## Continuity Kernel Adoption

Use `references/continuity-kernel.md`, `references/capability-baseline.md`, `references/readiness-gates.md`, `references/halt-taxonomy.md`, `references/preflight-cache.md`, and `references/handoff-density-policy.md` when participating in an SDLC Command Desk workflow. Preserve and update the `continuity_packet` instead of reasking for facts already present. Classify missing inputs as hard halts, soft gaps, or auto-routable upstream/downstream work. Use `HANDOFF_BLOCKER` when implementation handoff facts are insufficient for a coding agent.
