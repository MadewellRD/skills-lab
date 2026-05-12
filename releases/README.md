# Releases

This directory contains release notes and release-artifact guidance for SDLC Command Desk.

Current workflow-linked release candidate: `v0.1.1`.

## Artifact policy

Packaged skill archives should be published through GitHub Releases when stable.

Repository-facing artifact names should use ordered descriptive names:

```text
000-sdlc-command-desk-skill.zip
001-product-requirements-desk-skill.zip
```

Upload-facing archives may be renamed to `skill.zip` when uploading a single skill to ChatGPT.

## Checksums

Release artifacts should have SHA256 checksums recorded in `CHECKSUMS.txt`.

Before finalizing a release:

1. Regenerate or collect all packaged archives.
2. Compute SHA256 checksums for every archive.
3. Update `CHECKSUMS.txt`.
4. Attach archives to the GitHub Release.
5. Confirm the manifest and install guide reference the same artifact set.

## Versioning

Use semantic-ish release tags for bundle releases:

```text
v0.1.1
v0.2.0
v1.0.0
```

Use `v0.x` while the suite is still evolving quickly.
