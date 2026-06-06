# Security Policy

## Supported project surface

Skills-Lab contains source skill material, generated skill packages, release assets, documentation, and validation tooling. Security reports may relate to unsafe instructions, malicious examples, package integrity, release checksums, tool behavior, or repository automation.

The active supported branch is `main`. Published release artifacts listed in `MANIFEST.md` are considered supported for integrity and documentation corrections.

## Do not report security issues publicly

Do not open a public issue that contains exploit details, secrets, private data, or a working abuse path.

Use GitHub private vulnerability reporting if it is available for this repository. If private reporting is not available, open a minimal public issue that says a security report is needed and asks a maintainer for a private contact path. Do not include sensitive details in that public issue.

## What to report

Report issues such as:

- Credential, token, private key, or secret exposure.
- Malicious or unsafe instructions in a Desk Suite.
- Prompt-injection content embedded in repo material.
- Release artifact tampering or checksum mismatch.
- Package contents that do not match the documented source or manifest.
- Validation tooling behavior that can hide a failed package or corrupted artifact.
- Instructions that could cause unintended destructive operations when followed by an agent.

## What to include

A useful report should include:

- Affected file, package, release, or workflow.
- Minimal reproduction steps.
- Expected behavior.
- Observed behavior.
- Impact assessment.
- Suggested remediation, if known.

Do not include real credentials, live exploit targets, private user data, or third-party confidential material.

## Maintainer response target

Maintainers should acknowledge valid security reports as soon as practical. Triage should determine whether the issue affects source content, generated `dist/` material, release packages, documentation, or validation tooling.

A fix may require source edits, regenerated packages, updated checksums, updated release notes, and a new release tag. Security fixes should not bypass validation unless the validation tooling itself is the affected surface.

## Release integrity checks

Users and maintainers should verify package integrity with the published checksum files and the repository validation tools. For release asset changes, run:

```powershell
python tools/validate_release_assets.py
```

If validation fails, treat the affected package or release as untrusted until the mismatch is explained and corrected.
