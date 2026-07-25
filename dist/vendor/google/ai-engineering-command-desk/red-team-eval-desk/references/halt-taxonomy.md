# Halt Taxonomy

## Default posture

Prefer `SOFT_GAP_ASSUMPTION_ALLOWED`. Proceed, label the assumption inline, and keep it
auditable so it is cheap to correct.

Hard halts are exceptional. They exist for cases where being wrong is expensive or
irreversible, not for cases where the answer is merely uncertain. Current models reason
through ambiguity that older ones could not, so a halt a competent human would have worked
through is now a defect, not a safeguard.

Before returning a hard halt, check that it belongs to one of the six classes below. If it
does not, it is a soft gap: continue and label it.

## Hard halts

Each is justified by consequence, not by uncertainty:

- `HARD_HALT_APPROVAL`: a human must authorize before proceeding.
- `HARD_HALT_PRODUCTION`: the action has irreversible or destructive side effects.
- `HARD_HALT_SECURITY`: proceeding risks exposure of secrets, credentials, or personal data.
- `HARD_HALT_SOURCE_CONFLICT`: sources genuinely disagree on a load-bearing fact, and
  picking one silently would launder a guess into a decision.
- `HARD_HALT_RELEASE_INTEGRITY`: shipping something whose correctness cannot be established.
- `HARD_HALT_CONNECTOR`: required evidence is *unreachable*. Evidence that is merely
  *absent* is a soft gap. Unreachable means the source exists and cannot be read.

## Continuation outcomes

- `SOFT_GAP_ASSUMPTION_ALLOWED`: default. Proceed with the assumption stated inline.
- `AUTO_ROUTE_UPSTREAM`: a prior stage owns the missing decision; route without asking.
- `AUTO_ROUTE_DOWNSTREAM`: this stage is complete; continue into the next.
- `HANDOFF_BLOCKER`: implementation handoff facts are insufficient for a coding agent.

## Required fields

For each halt outcome, include reason, continuation flag, required response fields, resume
requirements, and one example in the calling artifact.

A halt must be *actionable*: state the exact fact needed, what was already attempted to
obtain it, and the prompt that resumes the workflow once it arrives. A halt that only
reports being stuck is incomplete.
