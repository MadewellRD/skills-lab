# Source hierarchy

Use this priority order:

1. Current user instruction.
2. Explicit product or roadmap source documents.
3. GitHub issues, milestones, PRs, and repo facts.
4. Architecture or technical docs.
5. Decision-bearing communication messages.
6. Uploaded notes or user-pasted context.
7. Model inference, only when labeled as an assumption.

Conflict rules:

- Current user instruction can set priority but cannot rewrite historical source facts.
- GitHub wins for repo state.
- Docs win for roadmap/product policy unless stale or contradicted by newer decisions.
- Chat messages are decision context, not durable source of truth unless explicitly marked authoritative.
- If conflict affects requirements, halt or mark the requirement unresolved.
