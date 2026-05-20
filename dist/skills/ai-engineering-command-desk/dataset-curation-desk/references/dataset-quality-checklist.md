# Dataset Quality Checklist

Use this checklist before marking `ready_to_continue: true`.

## Rights and governance

- Source owner is named.
- Intended use is explicit.
- License, rights, consent, and retention posture are known.
- Sensitivity classification and tenant boundary are explicit.
- Access controls and data residency constraints are captured.

## Dataset construction

- Inclusion and exclusion rules are explicit.
- Label schema and instructions are explicit.
- Label quality, adjudication, and reviewer requirements are defined.
- Sampling and balancing strategy is documented.
- Deduplication policy is explicit.

## Split and contamination

- Train/dev/test/eval split policy is explicit.
- Benchmark leakage risk is checked.
- Cross-split duplication risk is checked.
- Fine-tuning data is separated from eval/release-gate data.
- Known drift and coverage gaps are documented.

## Validation

- Row/file counts and schema checks are defined when applicable.
- Representative, edge, negative, safety, and high-risk slices are identified.
- Privacy redaction/minimization rules are explicit.
- Dataset versioning and change tracking are defined.
- Downstream handoff target is explicit.
