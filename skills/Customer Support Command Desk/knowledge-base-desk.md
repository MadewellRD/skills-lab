---
name: knowledge-base-desk
description: author and govern help center and internal knowledge base articles captured from resolved contacts, scoped to the product versions and editions they are true for, with steps verified against a stated build, titles and search terms written in the customer's words, ownership and review dates, duplicate and contradiction reconciliation, and a staleness register for articles a release has silently invalidated. use for knowledge-centered service work, article drafting, kb audits, content lifecycle, and post-release documentation checks.
---

# Knowledge Base Desk

## Suite workflow mode

This desk is a member of the Customer Support Command Desk suite. Complete the knowledge artifact set, update the `support_packet`, and continue to the next stage whenever the available source facts support it. The packet shape, the source hierarchy, and the continuity rule are in `references/suite-workflow-contract.md`; the input and output boundary for this stage is in `references/stage-contracts.md`.

Return `Workflow Halt` only for one of the six hard classes: missing approval, production or destructive action, security or privacy exposure, genuine source conflict, release integrity asserted without evidence, or an unreachable connector. Every other gap is soft: proceed, label the assumption inline against the article it affects, and record it in `open_questions`. Never invent a product step, a menu path, a setting name, a version range, an edition boundary, an article identifier, an owner, or a verification date.

## Role

This desk turns a solved contact into an answer that exists once, and then keeps that answer honest as the product moves underneath it.

The capture rule is the whole discipline. An article written from the product documentation restates what the product team already believes; an article written from a resolved ticket carries the thing the customer actually hit, the configuration that made it happen, and the step that was not obvious. The second one deflects contacts and the first one does not. So the source of an article here is the resolved contact and the workaround or fix that actually worked, with the product documentation used to check the claim rather than to generate it.

Scope is the second discipline. Every article is true for a set of versions, editions, deployment models, and sometimes regions, and an article that does not say which is wrong for everyone outside that set while looking authoritative to all of them. A self-hosted customer following cloud steps, or a customer on a release two behind following the current UI path, gets a failure with the company's logo on it.

The desk also owns what nobody volunteers for: the article lifecycle. Duplicates and contradictions reconciled to one surviving answer with the losers redirected rather than left to rank against it, an owner and a next review date on every article, and the staleness register that lists what the last release silently invalidated. Support content does not rot noisily. It rots by staying published.

## Use when

- A resolved contact carries an answer worth having once rather than retyping, and an article needs drafting from it.
- Agents are pasting the same explanation into replies, or a macro has quietly become the only place an answer exists.
- A release has shipped and the articles it affects need finding, rechecking, and rescoping.
- The article set has duplicates, near-duplicates, or two articles that contradict each other on the same question.
- Customers cannot find an article that exists, because it is titled in product vocabulary rather than in theirs.
- Articles need owners, review dates, and a lifecycle state rather than an indefinite published status.
- An article is suspected of causing contacts rather than preventing them.

## Do not use when

- The question is whether the self-service surfaces cover the ranked drivers, or how containment is being measured. That is `self-service-deflection-desk`, which consumes this article set.
- The content is a reply template, a canned response, or a saved reply in the agent-facing library. That is `macro-response-quality-desk`.
- The cause is not yet established and the article would document a guess. That is `diagnostic-troubleshooting-desk` first.
- The finding is that the product documentation and the product disagree. Record it and route it; the fix belongs with the docs owner, not in a help center article that papers over it.
- The subject is which contacts an existing article already answers for triage purposes. That is `ticket-triage-desk`.

## Required evidence

- The resolved contacts that justify each article, with their volume over a stated window, and the resolution or workaround as it actually worked.
- The product version, edition, deployment model, and configuration the answer is true for, and the release notes covering the window in question.
- An environment on the stated build where the steps can be run, plus the UI or API surface for the editions claimed.
- The existing article set with titles, identifiers, states, owners, last review dates, near-duplicates, and any article covering the same question.
- Search terms and queries customers actually used, including the ones that returned nothing useful, and the words used in ticket subjects.
- The content standard in force: template, reading level, terminology and style guide, localization requirements, and the accessibility standard for published content.
- The publication and review workflow, including who may publish, who reviews technical accuracy, and the localization pipeline.
- Article usage evidence where it exists: views, link-throughs from replies, helpfulness votes, and any contact reduction attributable to an article.

## Workflow

**Outcome.** A drafted article set captured from resolved contacts, each scoped to the versions and editions it is true for, with the steps verified against a stated build on a stated date, findability written in the customer's own words, an owner and a next review date, plus the duplicate and contradiction reconciliation and the staleness register for what the last release invalidated.

**Grounding.** The body comes from the resolved contact and from steps actually run on the stated build, not from the product documentation and not from how the feature is supposed to work. The scope statement comes from the release notes and the editions the steps were run against. Findability terms come from ticket subjects, search logs, and the customer's own phrasing, including the wrong word customers use for the feature, since the search box does not know the product's internal name for it. A claim about expected behavior is checked against documentation at a stated version, and a mismatch between documentation and product is recorded as a finding to route rather than resolved silently in the article.

**Constraints.** No article is published whose steps were not run against a build, and the article states which build and when. Every article carries its version, edition, and deployment scope on the article itself rather than in a category. Screenshots, log extracts, configuration exports, and example payloads carry the customer's tenant, names, identifiers, tokens, and data, and every one of those is replaced with synthetic values before the article leaves the ticket. Where two articles answer the same question differently, one survives, the other is redirected rather than merely unpublished, and the reason is recorded, because an orphaned near-duplicate keeps ranking. Where an article documents a workaround for an open defect, it is linked to the defect record so it can be retired when the fix ships instead of outliving it. Publication, retirement, and redirect are prepared and stopped at the gate.

**Parallel surface.** Independent items fan out safely: articles drafted from separate resolved contacts, staleness checked per article against the release, findability terms harvested per article, scope confirmed per version and edition pair, screenshots and examples redacted per asset, and localization drift checked per translated article against its source. Three passes are single after the fan-out returns. Duplicate and contradiction reconciliation is a statement about the whole set, since choosing a survivor requires seeing every candidate at once. The coverage map against the ranked contact drivers is a set-level read. And the taxonomy or category placement is decided once, because independently placed articles produce a help center whose structure nobody can navigate.

**Acceptance bar.** Every article names the versions, editions, and deployment models it applies to, the build its steps were verified on, the date of that verification, an owner, and a next review date. Every article traces to the contacts that justify it. Every duplicate group has one survivor with the others redirected. The staleness register names the release, the articles it affects, and what specifically changed in each. Titles and search terms use words that appear in customer tickets. No article contains a real customer's identifiers, data, or tenant detail.

## Outputs

A complete run delivers this set:

- `article-drafts.md`: each new or revised article with its title in customer language, the symptom as customers describe it, the cause where one is established, the steps as verified, the version and edition scope, the build and date verified, the source contacts, and the related articles.
- `article-scope-register.md`: one row per article with its applicable versions, editions, deployment models, and regions, and the articles whose scope could not be established flagged as unpublishable until it is.
- `findability-map.md`: the customer-language terms, wrong-word synonyms, ticket subject phrasings, and failing search queries mapped to the article that should answer each, with the terms that currently lead nowhere.
- `duplicate-and-contradiction-reconciliation.md`: each group of overlapping articles, the survivor, the redirects, the contradictions found, and which reading was verified against the build.
- `lifecycle-and-ownership-register.md`: every article touched with its state, its named owner, its last verification date, its next review date, and the trigger that should force an early review.
- `staleness-register.md`: articles a release has invalidated, with the release, the specific change, the affected steps or scope, the current risk of leaving each published, and the ones linked to a defect that has since been fixed.
- `documentation-conflict-findings.md`: places where the product documentation and the observed product behavior disagree, each routed to the owning function with what it needs to decide.
- `knowledge-downstream-handoff.md`: what `self-service-deflection-desk` inherits, including the drivers now covered, the drivers still uncovered, and the articles whose deflection can and cannot be measured.

Depth standard: an artifact is complete when a customer on the stated version could follow the steps to the stated outcome without contacting support, and when an agent could link it in a reply without checking anything first. An article with correct headings and a steps section that describes the feature rather than the path through it is unfinished rather than draft.

Mode-specific alternatives, called out separately: in `diagnostic` mode, where the article platform, the search logs, the release notes, or a verification environment cannot be reached, the run delivers `knowledge-connector-diagnostic.md` naming each unreachable source and which drafts, scope statements, or staleness findings are unavailable because of it. Drafts still ship marked as unverified with the build they need to be run against, because the capture is worth keeping while the ticket detail is fresh, and an unverified draft that says so is safe in a way a published one is not.

Anti-fabrication guard: a knowledge article is a set of instructions someone will follow while their system is broken, so the failure mode here is a UI path that is one menu item off. Nothing in a help center reads more convincingly than a numbered sequence of plausible clicks, and nothing is more useless to the customer standing in front of a screen that does not match it. In these artifacts every step, menu label, button name, field name, setting path, API parameter, permission name, and error string appears only as it was observed on the build named in the article header, and where the steps could not be run the article stays in draft marked unverified rather than being published with a path assembled from how the product is documented or from how it worked in an earlier release. Version and edition scope follows the same rule: an article covers the versions it was checked on, never a range extended because the feature probably has not changed, since the customer on the untested edition is exactly the one who will follow it. Where an article would need a screenshot or an example nobody could produce, it ships without one; an illustration invented to fill a template is worse than a gap, because the gap does not send anyone to the wrong screen.

## support_packet fields to update

- `knowledge[]` with `article_ref`, `title`, `state`, `source_tickets[]`, `applies_to_versions`, `last_verified_against` with the build and date, `owner`, `findability_terms`, `linked_in_replies`, and `deflection_evidence` left as `not_measured` where it is
- `self_service.coverage_gaps[]` extended with the drivers this run could not write an answer for and why
- `approvals[]` for each publication, retirement, redirect, and localization release
- `defect.tracker_ref` cross-linked on any article documenting a workaround for an open defect, so the article retires with the fix
- `drivers[].deflectable` updated where an article now exists that could answer a driver, recorded as capability rather than as measured deflection
- `open_questions` for every documentation and product conflict routed out of this desk
- `source_facts` with collection timestamps, `assumptions`, `artifacts`, `next_stage`, `ready_to_continue`

## Halt conditions

Halt only on a hard class from `references/halt-taxonomy.md`, justified by consequence:

- **Release integrity**: an article would be published whose steps were never run against the version it claims to cover, or whose version and edition scope is unstated. A published article is trusted precisely because it is official, it is linked from replies by agents who will not recheck it, and a wrong one generates the contacts it was written to prevent.
- **Security or privacy**: a draft still carries a customer's tenant identifier, account name, personal data, log output, API key, session token, or connection string, or the article would document a step that weakens a security control, such as disabling verification or widening a permission, as a routine workaround.
- **Missing approval**: publication, retirement, or a redirect would go live in the help center, or a workaround would be published that commits the company to supporting a configuration it does not support.
- **Source conflict**: the product documentation, the release notes, and the observed behavior on the build disagree on what the product does. Preserve every reading; the article cannot arbitrate a product question, and publishing one reading buries the finding.
- **Production or destructive**: the next action would unpublish, delete, or bulk-retire existing articles, which breaks inbound links, search rankings, and every reply that ever linked them.
- **Connector unreachable**: the article platform, the release notes, or the verification environment exists and cannot be read, so scope and steps would describe a build nobody opened.

An unowned article, a missing helpfulness signal, an unmeasured deflection figure, and an unlocalized translation are soft gaps. Proceed with the state recorded honestly, and leave the article in the lifecycle state its evidence supports.

## Downstream handoffs

`self-service-deflection-desk` is next and needs the coverage this run created against the ranked drivers, the findability terms and failing queries, and an explicit statement of which articles have deflection evidence and which are merely published. `macro-response-quality-desk` needs the surviving article for every question a macro currently answers inline, so the macro links the answer rather than duplicating a copy that will drift. `ticket-triage-desk` needs the new articles with their version scope, since deflection at triage depends on that scope being trustworthy. `contact-driver-analysis-desk` needs the drivers that still have no answer anywhere. `support-metrics-reporting-desk` needs the article coverage position and the honest limits of any deflection claim. `resolution-closure-desk` needs the articles linked to open defects so a workaround article does not outlive the fix.

## Quality bar

Good knowledge work reads like it was written by the person who solved the ticket, because it was. The title is the customer's sentence, not the feature's name, so the search box finds it. The scope line sits at the top and says exactly which versions and editions this is true for, and the article is honest enough to say it does not apply to the self-hosted edition rather than staying silent and letting that customer find out. The steps were run, on a named build, on a named date, and that line is in the article rather than in a review system nobody reads. There is one article per question, and the near-duplicate that used to outrank it is redirected rather than quietly unpublished. Every article has a person's name on it and a date it comes back for review. And after a release, the register says which articles the release broke, because the alternative is discovering it from a ticket that says the screen does not look like this.
