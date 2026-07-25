# Connector Routing

## Required for live PR review

Use GitHub before making source-dependent review claims.

Retrieve when available:

- PR metadata: title, body, author, base/head, draft state, mergeability if exposed.
- Changed files and patch.
- Linked issue or referenced acceptance criteria.
- CI/check status for the head commit.
- Existing review comments and unresolved threads.
- Relevant source files outside the diff when needed to understand behavior.
- Ownership, conventions, and test layout when available.

## Required for requirements-backed review

Use docs, uploaded files, Drive, Notion, SharePoint, or other document connectors when review depends on:

- PRD, SRS, architecture/design spec, ADR, test plan, release criteria, security policy, compliance policy, or roadmap decision.

## Optional connectors

Use communication connectors only for decision history or halt reports. Treat Slack, Teams, and email as context, not repo truth.

Use public web only for external API/library behavior that is not present in repo docs or dependency docs.

## Missing connector behavior

If GitHub is unavailable for a live PR review, do not claim final approval. Produce either:

- a pasted-diff review limited to supplied material, or
- an `insufficient evidence` review that lists missing connector facts.
