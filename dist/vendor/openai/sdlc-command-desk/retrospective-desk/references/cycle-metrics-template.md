# Cycle Metrics Template

Use when the retrospective needs delivery metrics.

Track only metrics supported by available evidence:

- Cycle time from issue ready to PR opened.
- PR review duration.
- Time from PR opened to merge.
- CI failure count and dominant failure category.
- Rework count or follow-up PR count.
- Escaped defect count.
- Rollback or hotfix count.
- Scope changes after implementation began.
- Documentation drift or proof-map gaps found.

Format:

```markdown
## Cycle metrics

| metric | value | source | interpretation | confidence |
|---|---:|---|---|---|
```

If a metric cannot be verified, omit it or list it under missing evidence.
