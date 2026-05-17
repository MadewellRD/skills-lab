# Connector Routing

## GitHub required

Require GitHub when the discovery depends on:

- Repository topology, file paths, or source code behavior
- Branch, commit, PR, issue, milestone, or label state
- Dependency manifests, build scripts, tests, or CI status
- Prior implementation history or changed files

Facts to retrieve:

- Repo owner/name and selected branch/ref
- Relevant files and directories
- Dependency manifests and build/test commands
- Open issues or PRs linked to the request
- Recent commits or prior PRs for the same area
- CI/check status when relevant

## Docs required

Require Drive, Notion, SharePoint, uploaded docs, or equivalent document sources when discovery depends on:

- PRD, roadmap, strategy, design, architecture, audit, or parity language
- Product decisions or acceptance criteria not present in issues
- Existing technical docs or diagrams

## Issues/projects required

Require GitHub Issues, Linear, or equivalent when discovery depends on:

- Ticket scope
- Acceptance criteria
- Priority, labels, owner, blockers
- Linked PRs or milestones

## Communication sources optional but useful

Use Slack, Teams, email, or pasted agent reports for recent decision context. Do not treat communications as code truth.

## Public web allowed

Use public web for external API docs, SDK versions, vendor behavior, standards, security advisories, and library practices when not available in repo/docs.

## Missing connector behavior

If required connector facts are unavailable, produce a connector diagnostic with:

- Missing source
- Needed facts
- Why they matter
- Safe partial output, if any
- Next action for the user
