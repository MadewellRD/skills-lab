# Trust Boundary and Data-Flow Review

Use this when the request concerns authentication, authorization, API boundaries, data movement, third-party integrations, secrets, or deployment boundaries.

## Boundary review structure

```markdown
# Trust Boundary Review: <system or feature>

## Scope
- Components:
- Actors:
- Data classes:
- Integrations:

## Source facts
- Repo facts:
- Architecture/docs facts:
- Policy/compliance facts:

## Data-flow inventory
| Flow ID | Source | Destination | Data | Authn/Authz | Transport | Storage | Evidence |
|---|---|---|---|---|---|---|---|

## Trust boundaries
| Boundary | Components separated | Crossing actor/data | Current controls | Gap | Risk |
|---|---|---|---|---|---|

## Control checks
| Control | Present | Evidence | Gap or question |
|---|---|---|---|
| authentication |  |  |  |
| authorization |  |  |  |
| input validation |  |  |  |
| output encoding |  |  |  |
| rate limiting |  |  |  |
| audit logging |  |  |  |
| encryption in transit |  |  |  |
| encryption at rest |  |  |  |
| secret handling |  |  |  |
| tenant isolation |  |  |  |

## Required actions
- Action:
```
