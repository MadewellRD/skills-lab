# Tool Schema Risk Checklist

Use this checklist before emitting a tool contract or implementation handoff.

## Authorization

- Actor identity is explicit.
- Authentication mechanism is known.
- Permission scope is least-privilege.
- Tool cannot escalate privileges through arguments, prompt text, or retrieved content.

## Tenancy and data exposure

- Tenant boundary is explicit.
- Private data exposure class is known.
- Logging and redaction rules are explicit.
- Outputs cannot leak hidden system, credential, or cross-tenant data.

## Side effects

- Operation type is read-only, reversible mutation, destructive mutation, external action, billing action, or infrastructure action.
- Mutating actions define approvals, idempotency keys, rollback or undo expectations, and audit events.
- Destructive actions cannot be triggered only through natural language.

## Validation and errors

- Required fields, types, ranges, formats, enums, and defaults are explicit.
- Invalid arguments fail closed with stable error semantics.
- Partial success, empty state, rate limits, timeouts, cancellation, and retry behavior are explicit.

## Observability

- Tool call start/end, arguments where safe, result class, latency, errors, actor, tenant, approval state, and correlation IDs are observable.
- Sensitive arguments and outputs are redacted or omitted according to policy.
