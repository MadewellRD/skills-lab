# Interface Contract Template

Use this for APIs, events, schemas, adapters, module boundaries, and integration handoffs.

```markdown
# [Interface Name] Contract

## Purpose

[What this interface enables and which components depend on it.]

## Source facts

| Fact | Source | Notes |
|---|---|---|
| [Fact] | [Source] | [Notes] |

## Producer / owner

- Component or system: [name]
- Owner: [team/person/source if known]
- Repository path: [path if verified]

## Consumers

| Consumer | Usage | Compatibility sensitivity |
|---|---|---|
| [Consumer] | [Usage] | high/medium/low |

## Contract

### Request, input, or event

```json
{
  "field": "example"
}
```

### Response, output, or side effect

```json
{
  "field": "example"
}
```

## Errors and edge cases

| Case | Expected behavior | Verification |
|---|---|---|
| [Case] | [Behavior] | [Test/check] |

## Versioning and compatibility

[Backward/forward compatibility rules and migration expectations.]

## Security and privacy

[Authentication, authorization, data exposure, PII, secrets, and audit requirements.]

## Verification requirements

[Test types, fixtures, integration checks, contract tests, or CI gates.]
```
