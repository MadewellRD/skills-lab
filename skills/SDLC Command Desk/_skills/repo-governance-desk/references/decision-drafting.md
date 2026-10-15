# Decision Drafting in a Governed Repository

## The split

A governed repository separates four acts that the design stage normally performs as one: drafting, ratifying, recording, and implementing. Read the profile's `authority` fields and perform only the act assigned to this role.

| Act | Who | What the artifact looks like |
|---|---|---|
| Commission | issuer | a decision question, the verified facts, the gaps, the constraints, the invariants involved, the ledger number to use |
| Draft | drafter | the entry in `ledger.entry_format`, marked unratified, with a "For the ratifier" section |
| Ratify | ratifier (human) | a statement in the chat; the draft is never self-ratified |
| Record | recorder | the ratified text written verbatim into the ledger; no edits, no summary |
| Implement | issuer via packets | work packets that cite the recorded entry by id |

## Drafting rules

- Use the ledger's own format, never the ADR template, so the text can be recorded without transformation.
- Read and cite the entries the commission relates to. A draft that contradicts a recorded entry says so and frames itself as an amendment or supersession.
- Every claim about the repository cites a path, a sha, or a finding id from the commission. A fact the commission did not supply is marked UNVERIFIED, not invented.
- Name every invariant the decision touches, with a verdict for each: unchanged, strengthened, or amended with the exact new wording. A draft that weakens an invariant says so in plain words.
- State what the decision implies: packets by title, follow-up decisions by question.
- End with the "For the ratifier" section: the open choices, the recommendation, and what evidence would change it, then the fixed line: UNRATIFIED DRAFT. Not recorded. Ratification required.

## Recording rules

- Record only after the ratifier's explicit statement in the chat.
- Copy verbatim. Diff the recorded entry against the ratified text and show the diff is empty.
- Place the entry in the ledger's order (by id), and never renumber.
- Record the ratification date, not the drafting date, as the entry's date unless the ledger says otherwise.
