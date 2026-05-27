# Web Release Deployment Desk

`web-release-deployment-desk` is part of the Web Development Command Desk suite.

## Role

CI/CD, preview, deployment, rollback, and launch validation.

## Suite position

- Suite: Web Development Command Desk
- Skill slug: `web-release-deployment-desk`
- Default next stage: `web-observability-desk`

## Primary outputs

- Stage artifact
- Source facts
- Updated `web_delivery_packet`
- Open questions and halt conditions
- Downstream handoff when continuation is possible

## Core rule

Complete the current stage, preserve packet continuity, and continue when source facts are sufficient. Halt only when a required fact, connector, approval, or source conflict blocks safe continuation.
