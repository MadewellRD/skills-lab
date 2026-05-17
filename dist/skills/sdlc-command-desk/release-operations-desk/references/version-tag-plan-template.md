# Version and Tag Plan Template

Use this when the user needs versioning or tagging guidance. Do not invent tag names or perform tagging.

```markdown
# Version and Tag Plan

## Proposed release identity

- Release name:
- Version:
- Tag:
- Branch:
- Commit SHA:

## Versioning rationale

- Current version:
- Change type: major | minor | patch | prerelease | internal
- Compatibility impact:
- Migration impact:

## Tagging preconditions

- CI green:
- Verification complete:
- Changelog ready:
- Approval captured:
- Rollback path defined:

## Commands for executor review

```bash
# commands here are proposed only unless the user explicitly authorizes execution
```

## Halt conditions

- Target commit cannot be verified
- Release scope does not match changelog
- Existing tag conflict found
- Verification or CI evidence missing
```
