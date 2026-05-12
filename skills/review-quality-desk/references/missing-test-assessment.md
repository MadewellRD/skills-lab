# Missing-Test Assessment

Check for missing validation in this order:

1. Does the PR body or linked issue state acceptance criteria?
2. Do changed files alter user-visible behavior, API behavior, persistence, security, or build/release behavior?
3. Are there corresponding unit, integration, regression, fixture, e2e, or manual validation notes?
4. Are existing tests updated rather than weakened?
5. Do new tests fail for the right reason before the fix when this is a regression PR?
6. Do CI checks cover the changed subsystem?

Report gaps with:

- Behavior not covered.
- Why coverage matters.
- Recommended test type.
- Whether the gap blocks merge.
