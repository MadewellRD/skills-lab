# Root Cause Rubric

Use this taxonomy when classifying CI/CD failures.

## Categories

Code regression: changed source behavior caused a deterministic failure.

Test regression: test or fixture assumptions changed incorrectly, or a test is no longer valid for intended behavior.

Flaky test: intermittent failure with same-commit pass/fail evidence or repeated nondeterministic signature.

Environment failure: runner, OS, toolchain, cache, time, resource, or network state caused failure.

Dependency or registry issue: package download, version resolution, upstream API, or registry availability caused failure.

Workflow/config failure: YAML, permissions, matrix, path filters, caching, environment variables, or job ordering caused failure.

Permission or secret failure: token scope, missing secret, expired credential, branch protection, environment approval, or deploy key caused failure.

Quota, billing, or external outage: hosted CI, vendor service, or cloud quota prevented checks from running or completing.

## Confidence

High: supported by exact logs, repeated evidence, changed-file linkage, or local reproduction.

Medium: likely based on error signature and adjacent evidence, but missing one direct proof point.

Low: plausible hypothesis requiring more connector facts or reproduction.
