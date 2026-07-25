# Test Strategy Template

Use this structure for full test strategy artifacts. Adjust only when the source material makes a section irrelevant.

```markdown
# Test Strategy: <feature or workstream>

## Executive summary
State what will be tested, why it matters, and the overall risk posture.

## Source facts
List verified facts from requirements, design docs, GitHub, CI, issues, and user-provided context.

## Scope under test
Define features, flows, APIs, data paths, platforms, and user roles in scope.

## Out of scope
Define explicitly deferred areas and why they are safe to defer.

## Risk model
Rank risks by impact, likelihood, detectability, and reversibility.

## Test layers
- Unit
- Component
- Integration
- End-to-end
- Contract/API
- Migration/data
- Security/privacy
- Accessibility
- Performance/load
- Manual exploratory

## Requirement-to-test mapping
Use covered, partially covered, not covered, intentionally deferred, or needs clarification.

## Scenario matrix
Summarize scenario groups and point to the detailed matrix when separate.

## Regression plan
Identify existing behavior that must not break.

## Fixture and data plan
Name required fixtures, mocks, seeds, snapshots, golden files, or real-world samples.

## Validation commands or checks
List known commands only when source facts identify them. Otherwise mark as unknown.

## Open questions
List unresolved questions that block a safe plan.

## Downstream handoff
State which artifact should go to verification-desk, review-quality-desk, ci-failure-desk, or implementation-handoff-desk.
```
