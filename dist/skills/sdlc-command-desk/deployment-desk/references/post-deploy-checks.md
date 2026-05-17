# Post-Deploy Checks

Use this as the default verification checklist after deployment.

## Immediate checks

- Deployment completed in target environment.
- Target version, commit, image, or artifact is visible.
- Health checks pass.
- Smoke tests pass.
- Error rates remain within tolerance.
- Logs show no new critical failures.
- Alerts are quiet or expected.

## Functional checks

- Primary user flows work.
- Relevant APIs return expected results.
- Background jobs, queues, or scheduled tasks are healthy.
- Data migrations or schema changes are complete and safe.
- Feature flags are in intended state.

## Observability checks

- Dashboards show current deploy.
- Metrics are updating.
- Traces show expected paths.
- Synthetic checks pass.
- Support/customer signals are monitored.

## Completion note

Record deployment result, evidence, residual risks, and follow-up tasks.
