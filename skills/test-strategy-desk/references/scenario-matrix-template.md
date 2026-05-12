# Scenario Matrix Template

Use a table when the user needs QA scenarios, acceptance coverage, or manual/exploratory test planning.

| id | requirement or risk | scenario | type | priority | automation target | required fixture | expected result | source fact |
|---|---|---|---|---|---|---|---|---|
| TS-001 | requirement id or risk name | user-visible action or system condition | positive, negative, edge, regression, integration, security, accessibility, performance, migration | p0, p1, p2 | unit, integration, e2e, manual, contract | fixture name or none | observable outcome | citation or source note |

Scenario rules:

- Include positive path before edge or negative cases.
- Include at least one regression scenario for any touched legacy behavior.
- Include integration scenarios when data crosses module, process, network, database, or third-party boundaries.
- Include accessibility and privacy/security scenarios only when the product surface or data sensitivity warrants them.
- Do not claim automation feasibility without checking repo test framework and existing test patterns.
