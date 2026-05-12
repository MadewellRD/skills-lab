# Output Contract

Default artifact format is Markdown with these sections:

1. Title
2. How to use this file
3. Executive summary
4. Source facts
5. Unverified assumptions
6. Scope and non-scope
7. Dependency/consumer analysis
8. Retirement or cutover sequence
9. Data retention/archive handling when applicable
10. Communications plan when applicable
11. Risks, no-go gates, and rollback
12. Verification gates
13. Downstream handoff notes

When the artifact is meant for another implementation agent, include a `How to use this file` section that says to preserve guardrails, halt conditions, and final stop lines.

Every artifact must distinguish confirmed facts from assumptions. Do not present guessed usage, owner, traffic, retention, or consumer data as confirmed.
