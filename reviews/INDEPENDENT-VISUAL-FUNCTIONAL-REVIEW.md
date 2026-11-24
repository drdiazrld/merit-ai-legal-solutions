# Independent Visual / Responsive / Functional Review

**Reviewed branch:** `feat/homepage-v9-video`  
**Reviewed source commit:** `df2138dd86e4b838edca7f0d26a22569b5da7038`  
**Review scope:** exact committed homepage screenshots, independent local renders at 1440 / 1024 / 768 / 390, canonical routes, local resources, console/request behavior, navigation, and homepage video behavior.

## Final verdict: PASS

No publication-blocking visual, responsive, accessibility, resource, console, or playback defect was found.

## Homepage visual and responsive gate

| Viewport | Verdict | Findings |
|---|---|---|
| 1440 | **PASS** | The concept film is a dominant, polished feature directly after the hero. Crest/wordmark, review motif, qualification, native controls, caption, and discovery CTA are clear. No clipping, collision, horizontal overflow, or unfinished field was visible. |
| 1024 | **PASS** | Responsive hierarchy remains deliberate; the compact header, hero, qualification panel, 16:9 player, review strip, content sections, CTA, and footer retain clear spacing and alignment. No overflow or collision was found. |
| 768 | **PASS** | Tablet composition remains coherent and complete. The player stays prominent and proportional, the menu treatment is usable, and content does not clip or crowd. |
| 390 | **PASS** | Mobile layout is deliberately recomposed rather than merely reduced: full-width primary CTA, stacked review mark and qualification, readable player/caption, 2×2 review boundary, single-column matter UI, full-width secondary CTAs, and stacked footer. No horizontal overflow, collision, clipping, or underbuilt/empty field was found. |

The exact committed screenshots `screenshots/homepage-1440.png` and `screenshots/homepage-390.png` were inspected in full and in readable-scale crops. Independent renders reproduced them without visual drift.

## Brand, qualification, player, and CTA

- **PASS — approved brand preserved:** the same `assets/img/merit-crest.svg` is present in the header and footer, with the established Merit wordmark and navy/gold/ivory system. The favicon also uses the crest. Both rendered logo placements load at every tested width.
- **PASS — qualification precedes playback:** “Concept preview” and the owner-directed / illustrative-workflow / attorney-review / no-automatic-action qualification are visibly placed above the player at every width. The caption repeats that the film is illustrative rather than current product verification.
- **PASS — video prominence and polish:** the film receives the largest media surface on the page; the office poster is clean, cinematic, and consistent with the legal brand. Representative frames across the 99.8-second film showed a coherent navy/ivory/gold treatment, branded legal-workflow material, and no broken UI, desktop leakage, watermark, or obvious rendering artifact.
- **PASS — 16:9 and accessible controls:** measured ratios were 1.7778 at 1440, 1024, 768, and 390. Native controls, inline playback, metadata preload, poster, descriptive label/caption, and an MP4 fallback link are present. The video accepts keyboard focus. An independent playback probe advanced from 0 to 1.108 seconds and paused normally.
- **PASS — CTA clarity:** “Book a 30-minute discovery call” is visually prominent in the hero and closing gold section, with a persistent header booking action on desktop and a full-width primary action on mobile. All booking URLs in the supplied verification resolve to the intended TidyCal destination.

## Per-route verdicts

Each canonical route returned HTTP 200 at 1440 / 1024 / 768 / 390 with no console error, bad HTTP response, horizontal document/body overflow, out-of-viewport content, or missing crest placement.

| Route | Verdict |
|---|---|
| `/` (`index.html`) | **PASS** |
| `/capabilities.html` | **PASS** |
| `/commands.html` | **PASS** |
| `/pilot-demo.html` | **PASS** |
| `/testing.html` | **PASS** |
| `/security.html` | **PASS** |
| `/responsibility.html` | **PASS** |
| `/pilot.html` | **PASS** |
| `/about.html` | **PASS** |

**Compatibility routes: PASS.** The ten preserved legacy routes have valid local targets and canonical destinations in the supplied verification report: `ai-legal-associate-minnesota.html`, `hire-a-paralegal-minnesota.html`, `virtual-paralegal-minnesota.html`, `compliance.html`, `orchestration.html`, `proof.html`, `systems.html`, `vs-general-ai.html`, `vs-legal-ai.html`, and `work-time.html`.

## Functional and resource gate

- **PASS — navigation:** the 390px menu opens, exposes the navigation, and reports `aria-expanded="true"`; the supplied cross-viewport report also confirms the menu target meets its usability gate at all widths.
- **PASS — console:** no console errors occurred on any canonical route at any tested width.
- **PASS — local references:** the supplied verification reports no broken local references. Independent HTTP checks returned 200 for the homepage, CSS, JavaScript, crest, poster, and full MP4.
- **PASS — video load:** H.264 1920×1080 at 30 fps with AAC audio, duration 99.8 seconds, exact SHA-256 `eea2b3f4f0055d571707b7a826839292717edb94879b920af2841bd54744d12f`. Browser `readyState` reached 4 at every width and playback advanced successfully.
- Chrome emitted `net::ERR_ABORTED` only when its media request was cancelled during page-context teardown after the video had already reached `readyState 4`; full-file HTTP fetch, metadata, decode readiness, and playback all passed, so this is not classified as a resource failure.
- **PASS — completeness:** no visitor-facing form field is present on the homepage. The fictional matter UI contains complete headings and values rather than blank or placeholder states.

## Blocking issues

None.
