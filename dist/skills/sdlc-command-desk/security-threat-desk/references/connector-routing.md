# Connector Routing

## GitHub required

Use GitHub for any claim about:

- code paths, auth/authz behavior, APIs, data flows, dependencies, secrets, workflow files, branches, commits, PRs, issues, CI checks, or tests.

Retrieve:

- relevant files and directories
- changed files and PR diff when reviewing a PR
- dependency manifests and lockfiles
- workflow files and permissions
- issue acceptance criteria when risk is issue-driven
- commit/check status when release risk is discussed

## Docs required

Use docs, uploaded files, Notion, Drive, or SharePoint for:

- requirements, architecture, privacy policy, compliance requirements, data classification, design intent, roadmap constraints, and release policy.

## Communication connectors optional

Use Slack, Teams, or email only for decision history, halt reports, recent security decisions, or stakeholder approvals. Do not let chat override code-state facts.

## Public web allowed

Use public web only for current external tool, framework, CVE, vendor, or API documentation when internal sources do not contain the needed external fact.

## Missing connector behavior

If a required connector is unavailable, produce a connector diagnostic or mark the output as user-fact-only. Do not invent code, dependency, or policy facts.
