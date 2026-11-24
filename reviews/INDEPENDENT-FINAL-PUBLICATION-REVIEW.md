# Independent Final Publication Review

## Verdict: PASS

The exact content candidate at `4a78fea6bb8f8c74f13946909886a50489b9e77e` passes final publication review under the recorded, hash-bound concept-film exception. This verdict does not verify the illustrated product claims or authorize publication.

- Content tree: `1c8ff421b0f6dc3085ebd06364cbedb4041730b0`
- Reviewed video: `assets/media/merit-ai-solutions-concept-preview-v9-public.mp4`
- Video SHA-256: `2a63818e06d4bd895b2dcaefc3d1c95d38b350fad15467d52307d19efac9d4ac`
- Exact base: `ab54b145439ba6b25f6731585a2c5bcf4d65be08`

## Prior blockers

All three prior blockers are closed on the delivered bytes.

1. **Offer conflict closed.** The player poster and final video card prominently display `Free for the first 3 eligible attorneys` and `One pilot month at no charge`. Independent transcription of the delivered audio says, “The first three eligible attorneys may receive one pilot month at no charge.” The homepage states that the first three attorneys may receive one pilot month at no charge, and `pilot.html` states the eligible-attorney version.
2. **Stale CTA closed.** The final card displays `tidycal.com/drdiaz/discovery-call`; all nine canonical pages use the exact clickable destination `https://tidycal.com/drdiaz/discovery-call`. No stale domain was found in rendered HTML, the audio transcript, or the one-frame-per-second full-film OCR sweep.
3. **Public governance wording closed.** No `owner-directed` wording appears in rendered HTML, the audio transcript, or the full-film OCR sweep. The visitor-facing qualification now describes the film and its limits directly.

Case-insensitive public scans also returned zero `first 20` / `first twenty` hits. The corrected offer and TidyCal destination were OCR-readable in every sampled end-card second from 91 through 99.

## Video and audio

- `ffprobe`: H.264 video, 1920×1080, 30 fps, 2,994 frames; AAC stereo, 48 kHz; 99.800-second container duration and 99.797-second audio duration.
- Full decode completed with exit code 0.
- Decoded-source comparison against the superseded video hash `eea2b3f4f0055d571707b7a826839292717edb94879b920af2841bd54744d12f` proved exact preservation before the replacement boundary:
  - Video frames 0–2708 were identical; the first changed frame was 2709 at 90.300 seconds.
  - Audio frames through sample PTS 4,332,544 were identical; the first changed audio frame began at PTS 4,333,568, or 90.2827 seconds at 48 kHz.
- The replacement card is present for the corrected narration. Independent ASR transcribed the final offer followed by `Merit AI Solutions` and `Book a 30-minute discovery call`; it found no first-20, stale-domain, or owner-directed wording.
- The final spoken CTA ended at 98.28 seconds. The 99.80-second runtime therefore leaves a 1.52-second narration-silent visual hold, exceeding the 1.1-second requirement.
- The final card remains static, unclipped, and readable through the end. Its offer hierarchy, one-month term, booking action, and TidyCal destination are synchronized with the spoken close.

## Qualification and attorney boundaries

The gold `Concept preview` qualification is prominent, appears immediately before the player at desktop and phone widths, and states that depicted workflows are illustrative pending current Lodestar verification. It also states that every draft requires attorney review and that nothing is sent, filed, served, or calendared automatically.

The surrounding homepage and canonical pages preserve the same boundary: Merit prepares material; attorneys check facts, sources, law, calculations, dates, and documents; attorneys decide what to use; filing, sending, service, submission, and external action remain manual. The film also includes review, approval, and hold-for-attorney language. The concept qualification is necessary because the film's illustrated workflow claims remain unverified.

## Rendered-site gates

Fresh execution of `verify_publication.py` returned `PASS` with:

- 9 canonical routes
- 10 redirect routes
- 16 preserved public URLs
- 1440, 1024, 768, and 390 pixel viewport checks
- 0 static errors
- 0 browser errors
- 0 console errors, meaningful request failures, broken local references, document/body overflow, clipped text nodes, logo failures, header overflow, or unusable-menu failures
- successful metadata load and playback advance for the exact video

The homepage video has controls, inline playback, metadata preload, no autoplay, a poster, an accessible label/caption, and a fallback link. Full-file HTTP retrieval, metadata, decode, and playback passed.

## Screenshots

The refreshed committed screenshots were inspected in full and at readable-scale crops:

- `screenshots/homepage-1440.png`: SHA-256 `d92ad057acc180ae458de784716077d00f470e02caf49823586de67c833ed2f6`, 1440×7456. A fresh exact-commit capture reproduced the file byte-for-byte.
- `screenshots/homepage-390.png`: SHA-256 `80f47c8c68511adbf257fc63a8ae79f5ecc315053772ee1a9afaebdf6b887c67`, 390×7700. A fresh exact-commit capture had the same dimensions and differed in only 46 raster pixels, with no semantic or layout drift.

Both views pass visual inspection. The qualification precedes the player, the corrected poster is legible, the responsive composition is deliberate, and there is no clipping, collision, horizontal overflow, empty field, stale offer, stale destination, or public governance wording.

## Routes, host files, and exposure scan

- `CNAME` is exactly `meritailegalsolutions.com` and is blob-identical to the base.
- The 20 tracked HTML/verification files match the base route set. Canonical metadata, redirects, sitemap order, robots file, domain verification file, and required assets passed.
- `CNAME`, `google29ad838b30fb55e1.html`, `robots.txt`, and `sitemap.xml` are blob-identical to the base.
- A tracked-file scan found zero secrets, credentials, private keys, private filesystem paths, or forbidden-framework hits.
- Full-film OCR and media metadata/string scans found zero secrets, credentials, private filesystem paths, forbidden-framework hits, first-20 wording, stale-domain wording, or owner-directed wording.

## Repository integrity

Before this review file was added, the branch was clean at exact content commit `4a78fea6bb8f8c74f13946909886a50489b9e77e`. `origin/main` resolved to `ab54b145439ba6b25f6731585a2c5bcf4d65be08`; that exact base is the merge base and an ancestor of the content commit. `git diff --check` and repository object verification passed.

No push or publication was performed.
