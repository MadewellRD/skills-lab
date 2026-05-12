# Source Hierarchy

Truth order:

1. Current user instruction.
2. Live GitHub repo state for code, dependencies, branches, PRs, issues, and CI.
3. Current issue/project acceptance criteria.
4. Architecture, migration, release, and policy docs.
5. CI logs, test reports, and scan outputs.
6. Public vendor/package documentation for external compatibility facts.
7. Model inference, only when labeled as an assumption.

Conflict rules:

- GitHub wins for current code and dependency state.
- Current user instruction wins for priority and intended direction.
- Architecture/release docs win for compatibility and boundary policies unless repo state proves they are stale.
- CI evidence wins for current failure state.
- Conflicts that affect scope, compatibility, release, or safety must become halt conditions.
