# Halt Taxonomy

Use these halt classes:

- `MISSING_SOURCE_FACT`: a required source-backed fact is absent.
- `CONNECTOR_UNAVAILABLE`: required connector access is unavailable.
- `SOURCE_CONFLICT`: authoritative sources disagree.
- `APPROVAL_REQUIRED`: human signoff is required before continuation.
- `UNSAFE_RELEASE`: a security, performance, accessibility, observability, rollback, or QA gate blocks release.
- `CODE_AGENT_BLOCKER`: implementation handoff would force a coding agent to rediscover essential facts.
