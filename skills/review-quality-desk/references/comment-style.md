# Review Comment Style

Use direct, evidence-first comments.

Good comment structure:

1. State the observed issue.
2. Cite the affected behavior or source fact.
3. Explain impact.
4. Suggest a concrete fix or validation step.

Avoid:

- Vague preference comments.
- Comments that restate the diff without review value.
- Overconfident claims when connector facts are missing.
- Broad rewrites unrelated to the PR scope.

Example:

```markdown
This path now accepts an empty `user_id`, but the linked acceptance criteria require rejecting unauthenticated requests before persistence. Please add a guard before `save_profile` and cover the empty-id case with a regression test.
```
