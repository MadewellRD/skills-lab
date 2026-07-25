# Test Risk Rubric

Prioritize testing with these dimensions:

- User impact: how visible or harmful failure would be.
- Change complexity: number of modules, interfaces, or data paths touched.
- Regression history: prior bugs, flaky tests, incidents, or fragile areas.
- Integration breadth: external services, databases, async jobs, queues, files, devices, or networks.
- Security/privacy exposure: credentials, authorization, sensitive data, audit trails, or tenant isolation.
- Reversibility: whether rollback is simple, delayed, data-destructive, or impossible.
- Observability: whether failures are easy to detect in logs, metrics, traces, CI, or user reports.

Priority guidance:

- p0: missing coverage can block merge or release.
- p1: important coverage needed before broad rollout or follow-up verification.
- p2: useful hardening that can be deferred with clear rationale.

A high-risk area should have at least one deterministic automated check or a documented manual verification path. If neither is possible, mark the risk as unresolved.
