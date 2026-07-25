# Model Upgrade Playbook

How to upgrade every skill in this repo when a new frontier model ships.

The point of this design: a model release should be a **config change and a rebuild**, not
217 hand edits. If you find yourself editing skill bodies one by one for a model release,
something has leaked out of the profile and back into the corpus. Fix the leak instead.

## The one-page version

```bash
# 1. edit the capability profile (or copy it to a new dated profile)
$EDITOR profiles/frontier-2026-07.yaml

# 2. rebuild every vendor target
for v in generic anthropic openai google; do
  python3 tools/build_skills.py --vendor $v
done

# 3. audit
python3 tools/audit_skills.py
python3 tools/validate_sdlc_suite.py
```

If the audit passes, every skill in the repo now runs on the new baseline.

## Where things live

| Layer | Path | Change it when |
|---|---|---|
| Capability profile | `profiles/frontier-2026-07.yaml` | A model release changes what you may assume |
| Vendor adapter | `profiles/vendors/<vendor>.yaml` | A vendor renames its agent, or you add a vendor |
| Kernel reference (tier 1) | `kernel/references/` | The change applies to every skill everywhere |
| Suite reference (tier 2) | `skills/<Desk>/references/` | The change applies to one suite |
| Skill reference (tier 3) | `skills/<Desk>/_skills/<slug>/references/` | The change applies to one skill |
| Skill body | `skills/<Desk>/<slug>.md` | The desk's actual domain logic changed |

Resolution is most-specific-wins: skill → suite → kernel. Nothing is duplicated on disk;
the build fans it out. That is why 277 source files produce 725+ packaged files.

## Adding a vendor

One file. `profiles/vendors/<name>.yaml`, following `_schema.yaml`. No skill body changes,
ever. If adding a vendor requires touching a skill body, that skill has hardcoded a vendor
and the audit's vendor-neutrality check should have caught it.

## Adding a skill

```
skills/<Desk Name>/<slug>.md                      # body, using {{TOKENS}} not vendor names
skills/<Desk Name>/_skills/<slug>/skill.yaml      # interface metadata
skills/<Desk Name>/_skills/<slug>/references/     # only refs unique to this skill
skills/<Desk Name>/_skills/<slug>/scripts/        # optional
```

Shared references are inherited from the kernel automatically. Do not copy them in.
The build injects `references/capability-baseline.md` into every skill, so a new skill
adopts the active profile with no action required.

## What a model release actually changes

Work through these four axes. Each maps to a section of the profile.

**1. Capability assumptions.** What can the floor model now do that it could not before?
Context size, self-verification, autonomy horizon, parallelism, tool use. Update
`capabilities:` with an `evidence:` string for each — a future maintainer needs to
re-verify your claim, not trust it.

**2. Authoring rules.** How does each capability change how skills should be *written*?
This is the part people skip. A bigger context window is not just a number; it invalidates
every "keep it short" instruction in the corpus. Write the translation down in
`authoring_rules:` so it is auditable.

**3. Capability debt.** What did the previous baseline force that is now wrong? Add a
detector to `DEBT` in `tools/audit_skills.py` so the next person can find it mechanically
instead of by reading 109 skills.

**4. New surfaces.** What can desks now do that they could not before? Parallel fan-out and
long-horizon continuation both landed this way.

## The line that matters most

**Capability scaffolding is removable. Governance is not.**

Scaffolding compensates for a model's weakness: numbered micro-steps, token rationing,
halt-on-uncertainty, "verify your work". A stronger model makes these unnecessary, and
keeping them actively costs quality — vendor guidance is now explicit that carried-over
verification instructions cause over-verification.

Governance constrains what a model is *allowed* to do regardless of how good it is: never
invent facts, separate fact from assumption, preserve conflicts, respect approval gates.
These never relax. Capability raises the fluency of a wrong answer exactly as fast as it
raises the accuracy of a right one, so the case for governance gets *stronger* as models
improve, not weaker.

When upgrading, the question for every line is not "is this still needed?" but
**"is this here because the model was weak, or because the action is consequential?"**
Only the first kind goes.

Two practical corollaries:

- **Ordered procedure is content; ordered hand-holding is scaffolding.** A numbered list is
  only scaffolding if the order is derivable. Deploy gates, rollback sequences, evidence
  capture before containment, dry-run before CRM write — those orders are load-bearing and
  survive. When you keep one, write down *why* so the next pass does not strip it.
- **Absent evidence is a soft gap; unreachable evidence is a hard halt.** The difference is
  whether continuing would launder a guess into a decision.

## Release discipline

`CHECKSUMS-*.txt` files pin published releases and are immutable. After a profile bump they
*should* mismatch — the content genuinely changed. Do not overwrite them. Cut a new version
and generate new checksums via `tools/generate_*_release.py`.

## Failure modes to watch

- **Silent drift.** Before the cascade existed, `desk-hardening-matrix.md` had 6 variants
  across 18 copies where 5 were lossy truncations of the 6th. Duplicated files always drift.
  If you catch yourself copying a reference between skills, promote it to a tier instead.
- **A profile that only describes one vendor.** The floor must hold across *all* reference
  models or skills silently assume capability a user's model does not have.
- **Audit noise.** If the audit reports the same known-good hits every run, people stop
  reading it. Add them to `ACCEPTED` with a reason, or fix them. Never leave them dangling.
