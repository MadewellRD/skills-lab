# Synthetic Data Quality Checklist

Use this checklist before accepting a synthetic-data plan or handoff.

## Rights and privacy

- Intended use is explicit.
- Source rights, consent, and ownership are known.
- Privacy class and retention policy are known.
- Sensitive examples are transformed, excluded, or approved.

## Contamination controls

- Training, eval, benchmark, red-team, and documentation uses are separated.
- Held-out and baseline datasets are protected.
- Generated examples are deduplicated and decontaminated against restricted sets.

## Generation quality

- Target distribution is explicit.
- Diversity targets are measurable.
- Label schema and output format are explicit.
- Exclusion rules and rejection criteria are explicit.

## Review and validation

- Human or automated review gates are defined.
- Failure modes and adverse examples are covered.
- Synthetic examples are not used as production proof without independent validation.
- Provenance, versioning, and usage limits are recorded.

## Halt triggers

Return `Workflow Halt` if rights, privacy, seed policy, contamination boundary, intended use, or validation plan is missing.
