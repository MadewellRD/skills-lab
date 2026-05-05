# SDLC Skills Research Map

Status: initial source sweep
Owner: MadewellRD

## Mission

Scour public GitHub and adjacent public skill indexes for skills, agent definitions, prompts, hooks, and lifecycle workflows that map to the full software development lifecycle. Extract useful patterns, reject weak or generic material, and convert the best patterns into a House-style skill suite with strict connector grounding, evidence blocks, halt conditions, and downloadable artifacts.

## Current completed anchor

- `pr-command-desk`: connector-grounded PR, repo-operations, halt-resume, merge-train, docs/proof, and implementation-agent handoff prompt generator.

## SDLC stage taxonomy

1. Strategy and portfolio intake
2. Product discovery and requirements
3. Research and technical discovery
4. Architecture and design
5. Planning, decomposition, and issue generation
6. Implementation handoff and branch/PR operations
7. Code review and quality gates
8. Testing, verification, and validation
9. Security, threat modeling, and compliance
10. CI/CD, release, and deployment
11. Observability, incident response, and maintenance
12. Documentation, knowledge management, and traceability
13. Retrospective, audit, and continuous improvement

## Seed sources discovered

### Ed-Fi Alliance OSS — AI Tools for Ed-Fi SDLC

Repository: https://github.com/Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC

Why it matters:

- Explicitly targets the software development lifecycle.
- Contains prompts, skills, hooks, agents, and docs.
- Uses a repository layout with `prompts/`, `skills/`, `hooks/`, `agents/`, and `docs/`.
- Good source for lifecycle packaging conventions and multi-artifact organization.

Extraction targets:

- Skill repo layout conventions.
- Prompt/skill/hook separation.
- Contribution and installation guidance.
- Claude Code / Copilot interoperability patterns.

### kcenon — AD-SDLC / claude_code_agent

Repository: https://github.com/kcenon/claude_code_agent

Why it matters:

- Defines Agent-Driven Software Development Lifecycle across greenfield, enhancement, and GitHub issue import modes.
- Describes 35 specialized agent types from mode detection through validation and documentation indexing.
- Strong candidate source for full lifecycle stage coverage.

Extraction targets:

- PRD writer, SRS writer, SDP writer, SDS writer.
- Threat model writer.
- Technology decision writer.
- UI spec writer.
- Issue generator.
- Software verification plan writer.
- Requirements traceability matrix builder.
- Stage verifier and validation agent.
- Codebase analyzer, doc-code comparator, and impact analyzer.
- CI fixer and regression tester.

### VoltAgent — Awesome Agent Skills

Repository: https://github.com/VoltAgent/awesome-agent-skills

Why it matters:

- Large curated index of agent skills from official teams and community sources.
- Lists 1100+ skills and explicitly filters for real-world skills rather than bulk-generated material.
- Includes official development-team skills from Cloudflare, Vercel, Expo, HashiCorp, Trail of Bits, Sentry, Figma, OpenAI, Angular, Supabase, Stripe, Netlify, and others.

Extraction targets:

- Official skill quality standards.
- Platform-specific implementation best practices.
- DevOps, deployment, web performance, cloud, testing, and security skill patterns.
- References for official team skill structure and naming.

## First-pass target skill suite

The first skill suite should not mirror external repos verbatim. It should synthesize best practices into a coherent SDLC operating system.

### Tier 1: Core lifecycle control-plane skills

1. `product-requirements-desk`
   - Inputs: product brief, customer notes, issue themes, docs.
   - Outputs: PRD, acceptance criteria, traceability-ready requirement IDs.

2. `technical-discovery-desk`
   - Inputs: repo, docs, APIs, architectural constraints.
   - Outputs: technical discovery memo, unknowns, risk register, spike plan.

3. `architecture-design-desk`
   - Inputs: PRD/SRS, repo topology, constraints.
   - Outputs: design spec, decision records, interface contracts, migration plan.

4. `issue-planning-desk`
   - Inputs: PRD/SDS, repo state, milestones.
   - Outputs: GitHub issues, dependency graph, labels, sequencing.

5. `pr-command-desk`
   - Existing anchor skill.
   - Outputs: grounded PR prompts, halt resumes, merge-train runbooks, docs/proof prompts.

6. `review-quality-desk`
   - Inputs: PR diff, checks, tests, code ownership, style docs.
   - Outputs: review findings, approval/change-request decision, risk-tagged comments.

7. `verification-desk`
   - Inputs: requirements, test plan, code changes, CI, artifacts.
   - Outputs: V&V report, RTM, test gaps, release-blocking defects.

8. `release-operations-desk`
   - Inputs: merged PRs, changelog, CI, deployment config, release notes.
   - Outputs: release runbook, rollback plan, release notes, post-release checks.

### Tier 2: Specialized assurance skills

9. `security-threat-desk`
   - STRIDE/DREAD/threat modeling, dependency risk, secrets review, authorization boundaries.

10. `ci-failure-desk`
    - CI log triage, flaky-test classification, failure minimization, rerun policy.

11. `observability-incident-desk`
    - Logs, traces, metrics, incident summaries, remediation PR prompts.

12. `docs-traceability-desk`
    - Proof maps, claim maps, status docs, doc-code consistency, audit trails.

13. `maintenance-refactor-desk`
    - Refactor planning, dependency upgrades, dead-code removal, migration sequencing.

## Design rules for all derived skills

- Never copy weak external wording directly.
- Treat external repos as pattern sources, not final authority.
- Require connector grounding before operational outputs.
- Use GitHub as repo truth for files, branches, commits, PRs, issues, and checks.
- Use docs/connectors for product and policy truth.
- Require evidence blocks or companion provenance files.
- Include halt conditions for missing connector context, baseline drift, conflicting source truth, failing gates, and unsafe scope expansion.
- Output downloadable Markdown artifacts when the skill creates instructions, prompts, runbooks, reports, or checklists.

## Open questions

- Which SDLC stages should be built first after `pr-command-desk`?
- Should each desk become a separate ChatGPT skill, or should some be bundled as references inside one larger SDLC command system?
- Should source extraction produce a public catalog, a private working catalog, or both?
- Should packaged `skill.zip` files be attached via GitHub Releases rather than committed into the repo?
