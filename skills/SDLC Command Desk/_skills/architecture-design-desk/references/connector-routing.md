# Connector Routing

## Required by design mode

| Design mode | Required sources | Optional sources | Halt if missing |
|---|---|---|---|
| Repo-aware architecture | GitHub repo/code/search, dependency manifests, tests | prior PRs, issues, CI | yes |
| Requirements-backed design | PRD/SRS/discovery docs | roadmap, stakeholder notes | yes |
| Interface contract | existing API/schema/module files | consumers, examples, integration tests | yes when contract affects existing consumers |
| Migration plan | current implementation, target requirement, compatibility constraints | release history, deployment docs | yes |
| ADR set | decision context, alternatives, constraints | stakeholder messages | halt if decision facts conflict |
| Implementation handoff | design artifact, repo facts, issue scope | CI and prior PRs | produce handoff notes only if implementation facts are incomplete |

## Fact retrieval checklist

Before drafting, gather:

- repository owner/name and relevant paths;
- current modules/components involved;
- existing APIs, schemas, data models, or integration points;
- dependency and runtime constraints;
- requirements and acceptance criteria;
- existing tests and validation commands when available;
- prior decisions, ADRs, or open issues;
- security, privacy, and compliance constraints.

## Missing connector behavior

If a required connector is unavailable, create a connector diagnostic or label the artifact as user-fact-grounded only. Do not write a repo-specific architecture that claims verified files, APIs, tests, or constraints without evidence.
