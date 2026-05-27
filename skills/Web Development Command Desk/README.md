# Web Development Command Desk

Source Markdown suite for a workflow-linked web development command desk modeled after the SDLC Command Desk Suite.

This suite covers full web delivery: product intent, information architecture, UX/UI and design systems, frontend engineering, backend integration, CMS/content operations, SecOps, performance, accessibility, SEO, QA, observability, release/deployment, and post-launch maintenance/growth.

## Desks

- `web-development-command-desk.md`
- `site-product-requirements-desk.md`
- `information-architecture-desk.md`
- `ux-ui-design-system-desk.md`
- `frontend-engineering-desk.md`
- `backend-integration-desk.md`
- `cms-content-operations-desk.md`
- `web-security-secops-desk.md`
- `web-performance-desk.md`
- `accessibility-seo-desk.md`
- `web-testing-qa-desk.md`
- `web-observability-desk.md`
- `web-release-deployment-desk.md`
- `web-maintenance-growth-desk.md`

## Workflow backbone

```text
site product requirements
  -> information architecture
  -> ux/ui design system
  -> backend integration
  -> frontend engineering
  -> security/secops
  -> accessibility/seo
  -> performance
  -> testing/qa
  -> release/deployment
  -> observability
  -> maintenance/growth
```

Not every workflow needs every stage. The command desk selects the shortest safe stage path, preserves the `web_delivery_packet`, and halts only when a required fact, connector, approval, or source conflict blocks continuation.
