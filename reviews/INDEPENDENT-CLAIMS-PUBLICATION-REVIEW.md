# Independent claims and publication review

## Verdict: BLOCK

Reviewed candidate `df2138dd86e4b838edca7f0d26a22569b5da7038` against remote base `ab54b145439ba6b25f6731585a2c5bcf4d65be08` and the Merit AI Legal Solutions website publication rules.

## Blocking defects

1. **The concept qualification does not limit the film's conflicting pilot offer.** At approximately 90.3 to 94.6 seconds, `assets/media/merit-ai-solutions-concept-preview-v9.mp4` says, “The founding pilot is open, free for the first 20 attorneys.” The current homepage and `pilot.html` state that the first three eligible attorneys may receive one pilot month at no charge. The qualification before the player describes the depicted workflows as illustrative and pending verification, but it does not say that the film's offer terms are obsolete or illustrative. A visitor therefore receives two incompatible public offers.

2. **The film ends with a stale discovery-call destination instead of the approved booking destination.** The final card displays `meriteducationgroup.com/merit-ai-legal-solutions` with “Schedule a discovery call.” The approved primary CTA is `https://tidycal.com/drdiaz/discovery-call`. The surrounding homepage uses the approved URL, but the visitor-facing film still directs viewers elsewhere. The concept-workflow qualification does not qualify or replace this CTA.

3. **The new visitor copy exposes internal publication governance.** The sentence “This owner-directed film...” tells visitors about the approval process rather than the product limit. The required limitation can be stated without “owner-directed.” The Merit humanization rules require visitor-facing governance language to be removed.

## Checks that passed

- The `Concept preview` panel is visually prominent, appears before the player at desktop and mobile widths, and states that workflows are illustrative pending current Lodestar verification, drafts require attorney review, and sending, filing, service, and calendaring are not automatic.
- The surrounding homepage consistently says external actions are manual. It does not imply automatic sending, filing, service, or external calendar writes.
- The homepage defines the AI Legal Associate as an AI-assisted preparation system, not a lawyer, employee, or substitute for attorney judgment. Site copy also states that Merit is not a law firm, does not provide legal advice, and requires attorney review.
- All inspected booking links in rendered HTML use the approved TidyCal URL. The defect above is confined to the film's rendered end card.
- A case-insensitive scan of all tracked bytes and rendered HTML found zero matches for the forbidden framework token.
- The recorded owner exception is hash-bound to SHA-256 `eea2b3f4f0055d571707b7a826839292717edb94879b920af2841bd54744d12f`. A fresh hash of the committed MP4 matched exactly. The record preserves unrelated claim and publication gates.
- No credentials, private keys, credential assignments, email addresses, private filesystem paths, or hidden personal metadata were found in tracked bytes. The film uses labeled demonstration material and fictional matter names.
- `CNAME` is byte-identical to the base. The canonical and redirect HTML route sets are preserved; every non-homepage HTML blob is identical to the base.
- The candidate content commit is the direct child of the claimed base, the branch was clean before this review was added, and `origin/main` resolved to the claimed base SHA.
- Fresh execution of `verify_publication.py` returned `PASS` with 9 canonical routes, 10 redirects, 16 preserved public URLs, four viewport widths, zero static errors, and zero browser errors. That automated PASS does not inspect the film's spoken offer or rendered end-card CTA, so it does not clear the defects above.
