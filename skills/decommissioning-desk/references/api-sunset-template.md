# API Sunset Template

Use this for retiring endpoints, SDK methods, webhooks, events, schemas, flags, or integrations exposed to other systems.

## API surface

- Endpoint/event/schema/method:
- Version or route:
- Public/internal classification:
- Known consumers:
- Compatibility promise:

## Consumer inventory

| Consumer | Evidence source | Usage level | Migration target | Owner | Deadline |
|---|---|---|---|---|---|

## Sunset timeline

- Announcement date:
- Deprecation warning start:
- Migration deadline:
- Read-only or compatibility window:
- Disable date:
- Removal date:

## Required changes

- Code changes:
- Docs/API reference changes:
- SDK/client changes:
- Monitoring/alerting changes:
- Support/customer messaging:

## Compatibility and fallback

- Replacement API:
- Migration path:
- Error behavior after disablement:
- Backward compatibility window:
- Rollback conditions:

## Halt conditions

- Unknown external consumers.
- Missing usage telemetry.
- Unclear replacement path.
- Contract or customer commitment conflict.
- No validated rollback behavior.
