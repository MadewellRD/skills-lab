# Halt Classes Added for Governed Repositories

These extend the suite halt taxonomy. They are hard halts: the run stops, the halt artifact states the exact fact or decision needed, and the resume prompt is written.

## Invariant

Trigger: the next action, or the artifact the stage is about to emit, would violate, weaken, bypass, or depend on bypassing a declared invariant. "Weaken" includes narrowing its wording, adding an exception, or moving its enforcement to a place the invariant did not name.

Behavior:
1. Name the invariant in its declared wording.
2. State the specific action or design that would breach it.
3. Do not propose a workaround. Propose either a design that satisfies the invariant or a decision question for the ratifier, in the ledger's format if this role may draft.
4. Halt. The resume requirement is a ratified decision or a changed design, never an acknowledgement.

A reviewer applying this class treats "the test was loosened to match the new condition" and "the guard allowlists the whole file" as candidate weakenings and checks them explicitly.

## Authority

Trigger: the stage is about to do something the profile assigns to another role: draft when it is not the drafter, record a decision, merge, write the state file, approve its own work, or run a deploy the profile marks operator-run.

Behavior: produce the artifact this role may produce, hand the rest to the named role with the exact inputs they need, and halt if the run cannot continue without their act. Never simulate the other role's act (a draft marked ratified, a "would merge", a narrated deploy).

## Evidence of record

Trigger: the stage would certify a merge, release, or deploy without the profile's evidence of record: a receipt for the exact sha, a clean tree, tree-equality, artifact hashes, or on-disk field evidence.

Behavior: report the check as not performed and halt. A hosted check, a narrative from a coding agent, or a prior receipt for a different sha is not a substitute.

## Soft gaps that are not halts

- A profile field is missing: carry the suite default, labeled.
- A field in the receipt is absent because the receipt predates it: report it as unknown, not as passed, and continue the stage with the merge or release verdict withheld.
- An operator has not yet run a field block: issue the block and stop the deploy stage at "issued", which is not a halt of the run.
