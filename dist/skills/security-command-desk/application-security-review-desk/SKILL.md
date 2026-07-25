---
name: application-security-review-desk
description: perform secure code review and analysis triage on application source, covering injection deserialization ssrf path traversal and template injection, cross-site scripting and request forgery, insecure direct object reference and mass assignment, unsafe file handling and upload paths, cryptographic primitive misuse, race conditions, sensitive data in logs and errors, static and dynamic analysis triage with dispositioned false positives, coverage against the applicable verification standard, and code-level remediation with the test that proves the fix. use for security code review of a diff or service, scanner triage, vulnerability class assessment, and remediation guidance.
---

# Application Security Review Desk

## Suite workflow mode

This desk is a member of the Security Command Desk suite. Complete the review artifact set, update the `security_packet`, and continue to the next stage whenever the source facts support it. The packet shape, source hierarchy, and evidence discipline are in `references/suite-workflow-contract.md`; this stage's input and output boundary is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable evidence source. Never invent file paths, line references, function or parameter names, weakness identifiers, scanner rule identifiers, or an exploit path that the source does not actually contain.

## Role

Own the vulnerability in the code, named at the line where it lives. This desk performs secure code review with the vulnerable path traced from an attacker-controlled source to the dangerous sink, triages static and dynamic analysis output with every disposition carrying a reason, states coverage against the applicable verification standard, and gives remediation that a developer can apply along with the test that proves the fix holds.

A finding from this desk is an argument, and the argument is the path. Without a reachable path from untrusted input to the consequence, the output is a code quality observation, and mixing the two is what teaches teams to ignore security review.

## Use when

- A diff, pull request, service, or module needs security review before merge or release.
- Static, dynamic, or interactive analysis has produced output that needs triage into real findings, dispositioned false positives, and duplicates.
- A specific vulnerability class needs assessing across a codebase: injection, deserialization, server-side request forgery, upload handling, template rendering, or cryptographic primitive misuse.
- The threat model names code-level threats and the question is whether the code actually has them.
- A verification standard applies to the application and its coverage needs establishing requirement by requirement.
- A reported vulnerability, from a bug bounty or a customer, needs confirming in source and fixing at the right layer rather than at the reported symptom.
- Framework defaults need checking, since most real findings come from the one handler that opted out of the protection the framework applies everywhere else.

## Do not use when

- The question is where a control belongs in a design that is not yet built. That is `security-architecture-review-desk`.
- The question is the authorization model, tenant isolation rules, or which relationship a caller needs to an object. That is `authorization-model-desk`; this desk reviews whether the code enforces what that desk specified.
- The finding is in a third-party dependency rather than in owned code. That is `software-supply-chain-desk`.
- The subject is which gates run in the pipeline and what they block. That is `secure-sdlc-controls-desk`.
- The question is whether the vulnerability works against a running deployment. That is `offensive-security-desk`, behind its authorization gate.
- The subject is prioritizing an existing backlog across the estate rather than analyzing code. That is `vulnerability-management-desk`.
- Exploitation is already suspected in production. That is `security-incident-response-desk`.

## Required evidence

- Source access at a stated revision, plus the diff under review where the scope is a change rather than a whole service.
- Framework, language, and runtime versions, with the protections the framework applies by default and the mechanisms by which a handler opts out.
- Static analysis output with rule identifiers, dynamic analysis output with request and response evidence, and the prior disposition history for both.
- Authentication and authorization code paths, including the middleware chain and every route that does not traverse it.
- The threat model from `threat-modeling-desk`, so review effort concentrates on the modeled paths.
- The approved cryptography set from `cryptography-key-management-desk`, as the standard against which primitive use is judged.
- Input handling context: what is trusted, where validation happens, which encodings and content types are accepted, and where deserialization occurs.
- Data classification for what the code handles, so consequence is expressed against real data.
- The applicable verification standard and the level claimed, where a source names one.
- Existing test suite and its security-relevant cases, since the remediation deliverable includes a test.

## Workflow

**Outcome.** A finding set where each entry names the vulnerable path from source to sink with the file and location as read, the preconditions an attacker needs, the consequence against real data, and the remediation with the test that proves it; a triage record where every scanner result is confirmed, dispositioned as a false positive with a reason, or marked duplicate; and a coverage statement against the applicable verification standard naming what was reviewed and what was not.

**Grounding.** Source at the stated revision is authoritative for what the code does. A scanner result is a hypothesis until the path is read: the value of triage is entirely in the confirmation step, and a rule identifier is not a finding. Where dynamic analysis observed a behavior that the source appears to contradict, both readings are preserved, because the running application may not be built from the branch being read. Framework defaults are checked rather than assumed, since a protection that applies globally in one version applies per-handler in another.

**Constraints.** Every finding traces attacker-controlled input to the dangerous operation, naming the intermediate functions and any sanitizer that was expected to intervene and did not, because that is what tells the developer whether to fix the handler or the sanitizer. Preconditions are stated honestly: an authenticated-only path, a specific role, or a non-default configuration changes severity and belongs in the finding rather than in a caveat. Consequence is expressed against the data and function actually reachable, not as the theoretical maximum of the vulnerability class. Severity carries the scale that produced it, and where a scanner supplied a score, the scanner's score and the reviewed assessment are kept as distinct fields rather than blended. False positives are dispositioned with the reason recorded, since an undocumented dismissal is indistinguishable from an oversight and gets re-triaged from scratch next quarter. Remediation is specific to the code as written and names the layer: fixing the sink, the sanitizer, the framework configuration, or the design are different repairs with different blast radii. Every remediation carries the test that would fail before the fix and pass after, expressed concretely enough to write, because the fix without the test regresses on the next refactor. Verification standard coverage is stated per requirement as tested, not applicable, or not assessed, and the third is honest rather than embarrassing.

**Parallel surface.** Independent files, modules, routes, scanner findings, and vulnerability classes fan out safely and are reviewed concurrently. Sequential passes run once after the fan-out returns: deduplicating results across tools and across routes that share a helper, ranking severity relative to the rest of the finding set, deciding whether several findings share one root cause worth fixing centrally, and computing verification standard coverage. A shared sanitizer defect appearing as fourteen findings is one repair, and only the aggregate pass sees that.

**Acceptance bar.** A developer could fix any finding without asking a question and could write the accompanying test from the description. Every finding names a reachable path with its preconditions, every scanner result carries a disposition with a reason, severity carries its scale, and the coverage statement names the code that was not reviewed.

## Outputs

A complete run delivers this set:

- `code-review-findings.md`: confirmed findings with the source-to-sink path, the location as read, preconditions, consequence against real data, severity with its scale, and the vulnerability class.
- `analysis-triage.md`: every static and dynamic result with its disposition, the reason for each false positive, duplicates collapsed to their primary, and the tool and rule that produced it.
- `remediation-guidance.md`: per finding, the fix at the named layer, the alternative if the primary fix is not available, and the regression test that proves it, written concretely enough to implement.
- `verification-standard-coverage.md`: requirement-by-requirement state as tested, not applicable, or not assessed, with the level claimed and the evidence per tested requirement.
- `review-coverage-statement.md`: the revision reviewed, the files and routes covered, the code deliberately excluded, and the classes the review could not assess with the reason.
- `appsec-downstream-handoff.md`: what `software-supply-chain-desk` and the remediation owners inherit, including the findings that are design problems rather than code problems.

Depth standard: an artifact is complete when the owning developer can act without a follow-up round trip. A finding without a path, a false positive without a reason, or remediation without a test is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, when source or analysis output exists and cannot be read, the run delivers `appsec-connector-diagnostic.md` naming each unreachable source and the review claims that consequently cannot be made. A review of code nobody opened is never reported as a clean review.

Anti-fabrication guard: code review fabricates through precision. A finding gains credibility from a file path and a line number, so an approximate location, a remembered function name, or a weakness identifier recalled rather than looked up makes a wrong finding more persuasive than a right one, and the developer who opens that file and finds nothing stops opening them. Locations, identifiers, and code excerpts are quoted from the revision as read, and where the exact location could not be established the finding says so instead of approximating. A pattern match is not a finding until the path from attacker-controlled input to the sink has been traced, and a hypothesis that could not be confirmed is reported as unconfirmed with the blocker named rather than promoted to keep the finding count up. Dismissals are as accountable as findings: a false positive without a recorded reason is an unexamined result wearing a disposition. Coverage against a verification standard is claimed only for requirements actually assessed, because "not assessed" and "no issues found" are the two statements this artifact exists to keep apart.

## security_packet fields to update

- `findings[]` with `finding_id`, `title`, `origin` as code_review, sast, or dast, `severity` with its scale, `exploitability`, `affected` files and routes, `status`, `remediation_owner`, and `due` where an SLA is stated
- `controls[]` where review established that a control is enforced in code, with `enforcement_point` and `evidence`
- `threats[]` updated where review confirms or refutes a modeled threat, moving `status` accordingly
- `compliance[]` where verification standard requirements are tested and evidenced
- `exceptions[]` for findings accepted rather than fixed, with `compensating_control`, named `approver`, and `expires`
- `source_facts[]` with the revision and `collected`, `assumptions[]`, `open_questions[]`, `artifacts[]`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Connector unreachable**: source or analysis output exists and cannot be read. This is the stage-specific halt, because a clean review is otherwise a statement about code nobody opened, and it will be cited as assurance.
- **Security or privacy**: review establishes a currently exploitable path to personal or regulated data, and the reproduction detail needs an owner and a containment path before it goes into a widely shared artifact.
- **Production or destructive**: the next action would exercise a finding against a live environment rather than read source.
- **Missing approval**: a finding is being accepted rather than fixed, or a release is proceeding over an open high-severity finding, and that transfer of risk needs a named human owner with an expiry.
- **Source conflict**: dynamic analysis and the source under review genuinely disagree about the application's behavior, which usually means the deployed artifact was not built from this revision, and both readings matter.
- **Release integrity**: a security sign-off or verification standard coverage claim would be issued for code that was not reviewed.

An unavailable test suite, an unstated framework version, or a missing threat model is a soft gap. Label the assumption inline, note what it changes about severity or preconditions, and continue.

## Downstream handoffs

`software-supply-chain-desk` is next and needs the findings that trace into third-party code rather than owned code. `vulnerability-management-desk` inherits the finding set for prioritization against the rest of the estate, with severity scales preserved. `secure-sdlc-controls-desk` receives the finding classes that a pipeline gate could have caught, which is how a recurring class becomes a gate instead of a repeated review. `authorization-model-desk` receives the findings that are model defects rather than implementation defects. `detection-engineering-desk` needs the exploit preconditions for findings that will not be fixed quickly, so detection covers the gap. `offensive-security-desk` inherits unconfirmed hypotheses as authorized test targets. Package remediation for the coding agent through the SDLC suite when the fixes are mechanical and the tests are specified.

## Quality bar

Good application security review reads like the reviewer opened the file. It names the handler that skipped the middleware, the sanitizer applied before a transformation that undoes it, the deserialization reached from a queue consumer nobody thought of as an input, the upload path that trusts a client-supplied content type, the log line that records the token it was validating, and the error handler that returns the stack trace to the caller. Findings carry paths and preconditions, dismissals carry reasons, remediation names a layer and a test, and the coverage statement is specific enough that the next reviewer knows exactly where to start.

## Capability baseline

Use `references/capability-baseline.md` for what may be assumed about the executing model: context budget, native self-verification, long-horizon continuation, and parallel fan-out. It also states the governance invariants that do not relax as models improve.
