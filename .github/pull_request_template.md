# Pull Request

## Summary

Describe the change in one or two sentences.

## Affected area

- [ ] Source skill material in `skills/`
- [ ] Generated skill packages in `dist/skills/`
- [ ] Release packages in `dist/packages/`
- [ ] Manifest or checksum files
- [ ] Release notes or release scripts
- [ ] Documentation
- [ ] Repository/community files
- [ ] Tooling or validation scripts

## Suite or desk impact

Name the affected suite, desk, package, or workflow. Use `N/A` for repo-only changes.

## Source basis or rationale

Explain why this change is needed. For domain or workflow changes, include the public source basis, existing repo convention, or maintainer decision that supports it.

## Validation

List the exact checks run and results.

```text
Command:
Result:
```

For release artifact changes, include the result of:

```powershell
python tools/validate_release_assets.py
```

## Generated artifacts

- [ ] No generated artifacts changed.
- [ ] Generated artifacts changed and the generator/process is documented below.

Generator or process:

## Release impact

- [ ] No release impact.
- [ ] Manifest update required.
- [ ] Checksums updated.
- [ ] Release notes updated.
- [ ] New GitHub Release required.
- [ ] Existing release correction required.

## Safety and quality checklist

- [ ] Naming follows existing Desk Suite, desk, package, and release conventions.
- [ ] Taxonomy changes are explicit and justified.
- [ ] Skill content is source-grounded and bounded.
- [ ] Halt conditions or validation gates are preserved where relevant.
- [ ] No secrets, credentials, private data, or proprietary content were added.
- [ ] No unsafe destructive instructions were added.
- [ ] Formatting churn is limited to the scope of this change.
- [ ] Related docs, manifest entries, checksums, and release notes are updated when required.

## Risks or follow-up

List known risks, deferred work, or reviewer focus areas.
