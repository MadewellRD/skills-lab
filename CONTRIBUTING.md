# Contributing to Skills-Lab

Skills-Lab publishes Desk Suites: structured ChatGPT skill systems that guide users through professional workflows and hand constrained, source-grounded work to execution agents. Contributions should improve those systems without weakening taxonomy, naming, packaging, validation, or release integrity.

## Contribution principles

A good contribution is narrow, reproducible, and easy to review. It should explain the affected suite or desk, the reason for the change, the source basis for the change, and the validation performed.

Do not submit broad rewrites, generated bulk edits, package rebuilds, checksum changes, or release-note changes without explaining why those artifacts had to change. If a change modifies both source and generated `dist/` output, the pull request must identify the generator or process used.

## Repository structure

Core paths:

- `skills/` contains source Desk Suite material.
- `dist/skills/` contains generated installable skill packages by suite.
- `dist/packages/` contains packaged release artifacts.
- `docs/` contains repo structure, installation, and operating guidance.
- `releases/` contains release notes and release-process material.
- `tools/` contains validation and packaging utilities.
- `MANIFEST.md` tracks published suites, versions, and package roots.

## Naming and taxonomy rules

Follow the existing Desk Suite conventions already present in the repo. Do not introduce a new suite, desk name, folder shape, release name, or artifact pattern unless it matches the existing taxonomy or the pull request explicitly proposes a maintainer-reviewed convention change.

Use command-desk naming for suite-level orchestrators and domain-desk naming for specialist desks. Keep generated package names, release names, checksums, and manifest entries aligned.

## Skill authoring expectations

Skill content should be operational, bounded, and low-token. Prefer checklists, gates, inputs, outputs, handoff formats, and halt conditions over long explanatory prose. A desk should tell the model what to do, what to inspect, what to produce, when to stop, and what evidence is required.

Every skill change should preserve these properties:

- Source-grounded reasoning.
- Explicit inputs and outputs.
- Clear escalation or halt conditions.
- Minimal ambiguity for coding agents and CLI handoffs.
- No invented source claims.
- No unsafe destructive instructions.
- No hidden dependencies on private systems.

## Development workflow

1. Create a branch from `main`.
2. Make the smallest coherent change.
3. Preserve line endings and existing formatting patterns.
4. Update related docs, manifest entries, release notes, packages, or checksums only when the change requires it.
5. Run the relevant validation before opening a pull request.
6. Fill out the pull request template completely.

## Validation

For release artifact changes, run:

```powershell
python tools/validate_release_assets.py
```

When a suite-specific generator or packaging script exists, run it before validating release assets. Include the exact commands and results in the pull request.

If a change only affects documentation or community files, state that release validation was not required and explain why.

## Pull request requirements

A pull request should include:

- Scope summary.
- Affected suite, desk, package, or documentation area.
- Source basis or rationale.
- Validation performed.
- Generated artifacts changed, if any.
- Release impact, if any.
- Risks or follow-up work.

Maintainers may ask contributors to split large pull requests, remove unrelated formatting churn, restore naming conventions, add validation evidence, or reduce generated noise.

## Security and safety

Do not include credentials, private data, production logs, proprietary content, or exploit instructions in issues or pull requests. Report vulnerabilities using `SECURITY.md`.

## License

By contributing to this repository, you agree that your contribution is submitted under the repository's Apache-2.0 license unless explicitly stated otherwise in the contribution and accepted by maintainers.
