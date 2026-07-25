# Dependency, Secrets, and Supply-Chain Review

Use this for dependency manifests, package updates, build pipelines, deployment credentials, or suspected secret exposure.

## Dependency review checklist

- Identify dependency manifests and lockfiles from GitHub.
- Identify direct vs transitive dependency changes when the PR changes manifests.
- Check whether dependency versions are pinned or floating.
- Check whether build scripts execute remote code or install untrusted packages.
- Check whether CI workflows use broad permissions or unpinned actions.
- Check whether artifacts are signed or checksummed when applicable.

## Secrets review checklist

- Search only within authorized repo/context.
- Look for committed tokens, API keys, private keys, cloud credentials, webhook secrets, and local environment files.
- Verify secret handling through configuration and docs when available.
- Do not print secret values back to the user. Redact suspected secrets.
- If a live secret is suspected, recommend rotation and access-log review.

## Output structure

```markdown
# Dependency and Secrets Review: <subject>

## Source facts
- Manifests reviewed:
- Workflow files reviewed:
- PR/commit scope:

## Findings
| ID | Finding | Severity | Evidence | Remediation |
|---|---|---:|---|---|

## Secret handling
- Confirmed secrets: none | redacted evidence
- Suspected secrets:
- Rotation required:

## Supply-chain risks
- Risk:

## Required follow-up
- Action:
```
