# Architecture Artifact Template

Use this template for software design specs and solution architecture documents. Adapt section names only when the user has a stronger existing format.

```markdown
# [System or Feature] Architecture Design

## How to use this file

Use this design as the source for planning, issue decomposition, verification, security review, and implementation handoff. Treat assumptions and open questions as blockers until resolved.

## Executive summary

[One concise paragraph describing the proposed architecture and why it fits the requirement.]

## Scope

### In scope

- [Specific capabilities, modules, flows, or interfaces covered]

### Out of scope

- [Explicit exclusions]

## Source facts

| Fact | Source | Confidence |
|---|---|---|
| [Fact] | [connector/file/issue/doc] | high/medium/low |

## Current state

[Describe existing architecture, repository structure, dependencies, APIs, tests, and constraints verified from sources.]

## Requirements and constraints

| ID | Requirement or constraint | Source | Design impact |
|---|---|---|---|
| REQ-001 | [Requirement] | [Source] | [Impact] |

## Proposed architecture

[Describe the target design. Include component responsibilities and control/data flow.]

## Component boundaries

| Component | Responsibility | Inputs | Outputs | Owner/source |
|---|---|---|---|---|
| [Component] | [Responsibility] | [Inputs] | [Outputs] | [Source or owner] |

## Interface contracts

[Summarize APIs, events, schemas, module boundaries, or external integration contracts. Link to a separate contract artifact if needed.]

## Data model and state

[Describe data ownership, persistence, cache, migrations, retention, and consistency assumptions.]

## Security, privacy, and abuse considerations

[Describe trust boundaries, auth/authz, secret handling, data exposure, audit requirements, and privacy risks.]

## Tradeoffs and alternatives

| Option | Pros | Cons | Decision |
|---|---|---|---|
| [Option] | [Pros] | [Cons] | selected/rejected/deferred |

## Migration and rollout

[Describe phases, compatibility requirements, flags, rollback, and operational checks.]

## Verification implications

[Describe required tests, fixtures, acceptance gates, observability, and manual QA.]

## Risks and mitigations

| Risk | Impact | Likelihood | Mitigation | Owner |
|---|---|---|---|---|
| [Risk] | high/medium/low | high/medium/low | [Mitigation] | [Owner] |

## Open questions

| Question | Blocking? | Needed from | Next action |
|---|---|---|---|
| [Question] | yes/no | [Source/person/system] | [Action] |

## Downstream handoff notes

- For `issue-planning-desk`: [decomposition guidance]
- For `security-threat-desk`: [threat-model focus]
- For `verification-desk`: [proof and test requirements]
- For `implementation-handoff-desk`: [implementation prompt constraints]
```
