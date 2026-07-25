# Acceptance Gate Review Template

```markdown
# Acceptance Gate Review: [subject]

## Gate summary
- Overall status: passed / partial / failed / blocked / insufficient evidence
- Decision: ready / not ready / ready with risk

## Gates reviewed
| gate | expected evidence | observed evidence | status | notes |
|---|---|---|---|---|
| build | successful build command or CI check | ... | ... | ... |
| tests | required test suites pass | ... | ... | ... |
| acceptance criteria | each criterion satisfied | ... | ... | ... |
| security/privacy | required checks complete | ... | ... | ... |
| docs/release | docs and release notes aligned | ... | ... | ... |

## Failed or blocked gates
List each failed or blocked gate with required next action.

## Evidence gaps
List missing logs, missing artifact links, missing test execution, missing requirement IDs, or missing reviewer approvals.
```
