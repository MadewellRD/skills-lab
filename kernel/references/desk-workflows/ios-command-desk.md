# iOS Command Desk Workflow Reference

Use after an iOS desk is activated.

## Workflow modes

- `workflow_run`: default for planning, building, validating, launching, operating, improving, migrating, or decommissioning an iOS app or iOS game.
- `single_stage`: use only when the user asks for one artifact from one desk.
- `resume`: continue from a prior `ios_delivery_packet` or halt-resume prompt.
- `diagnostic`: use when connector access, repo state, research facts, or source evidence are insufficient.

## Stage order

```text
ios-product-requirements
  -> ios-technical-discovery
  -> ios-architecture-design
  -> ios-ui-ux
  -> ios-app-engineering OR ios-game-engineering
  -> ios-backend-integration
  -> ios-security-privacy
  -> ios-performance-optimization
  -> ios-testing-qa
  -> ios-release-app-store-ops
  -> ios-observability-liveops
  -> ios-maintenance-growth
```

Run only the stages required to satisfy the outcome. Do not trigger game desks for normal app work. Do not skip game-specific asset, input, frame pacing, Game Center, StoreKit, or live-ops concerns when source facts show they are launch-critical.
