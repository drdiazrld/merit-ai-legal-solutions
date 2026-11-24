#!/usr/bin/env python3
"""Verify the static GitHub Pages publication candidate."""
import asyncio
import json
import os
import re
import sys
import subprocess
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent
BASE = "http://127.0.0.1:4188"
DOMAIN = "https://meritailegalsolutions.com"
CANONICAL = [
    "index.html", "capabilities.html", "commands.html", "pilot-demo.html",
    "testing.html", "security.html", "responsibility.html", "pilot.html", "about.html",
]
REDIRECTS = {
    "ai-legal-associate-minnesota.html": "index.html",
    "hire-a-paralegal-minnesota.html": "capabilities.html",
    "virtual-paralegal-minnesota.html": "capabilities.html",
    "compliance.html": "responsibility.html",
    "orchestration.html": "commands.html",
    "proof.html": "testing.html",
    "systems.html": "security.html",
    "vs-general-ai.html": "capabilities.html",
    "vs-legal-ai.html": "capabilities.html",
    "work-time.html": "capabilities.html",
}
EXISTING_PUBLIC = [
    "index.html", "capabilities.html", "pilot-demo.html", "testing.html", "security.html", "pilot.html",
    *REDIRECTS.keys(),
]
VIEWPORTS = [1440, 1024, 768, 390]
BOOKING = "https://tidycal.com/drdiaz/discovery-call"
VIDEO = ROOT / "assets/media/merit-ai-solutions-concept-preview-v9-public.mp4"
POSTER = ROOT / "assets/media/merit-ai-solutions-concept-preview-poster.jpg"
VIDEO_SHA256 = "2a63818e06d4bd895b2dcaefc3d1c95d38b350fad15467d52307d19efac9d4ac"
FORBIDDEN = {
    "visitor_facing_framework_token": ["".join(("her", "mes"))],
    "removed_commands_scope": ["lodestar command library", "pleadings and discovery"],
    "roadmap_language": ["roadmap", "planned / in development", "coming soon"],
    "rejected_security_diligence_phrases": [
        "current scope and due diligence", "ask for the evidence", "security questionnaire", "unapproved channel",
    ],
    "public_failure_outcomes": [
        "what failed", "known failures", "failure results", "failed run", "criterion not met",
    ],
    "b1_completion_claim": ["b1 is complete", "b1 complete"],
    "superseded_film_governance": ["owner-directed"],
}
REJECTED_JARGON = {
    "vm_abbreviation": re.compile(r"\b" + "".join(("v", "m")) + r"\b", re.I),
    "fresh_seat": re.compile("".join(("fresh", "-seat")), re.I),
    "citation_gate": re.compile("".join(("citation", "-gate")), re.I),
    "seat_configuration": re.compile("".join(("seat ", "configuration")), re.I),
    "semantic_reviewer": re.compile("".join(("semantic ", "reviewer")), re.I),
    "restricted_runtime_controls": re.compile("".join(("restricted runtime ", "controls")), re.I),
}


def canonical_url(route: str) -> str:
    return DOMAIN + ("/" if route == "index.html" else f"/{route}")


def static_checks():
    errors = []
    html_files = sorted(ROOT.glob("*.html"))
    tracked_files = [ROOT / name for name in subprocess.check_output(
        ["git", "ls-files"], cwd=ROOT, text=True
    ).splitlines()]
    scans = {}
    for group, terms in FORBIDDEN.items():
        hits = []
        scan_files = tracked_files if group == "visitor_facing_framework_token" else html_files
        for path in scan_files:
            if not path.is_file():
                continue
            try:
                text = path.read_text(encoding="utf-8").casefold()
            except UnicodeDecodeError:
                continue
            hits.extend({"file": str(path.relative_to(ROOT)), "term": term} for term in terms if term in text)
        scans[group] = hits
        if hits:
            errors.append(f"{group}: {hits}")

    jargon_hits = []
    for path in tracked_files:
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        jargon_hits.extend(
            {"file": str(path.relative_to(ROOT)), "term": name}
            for name, pattern in REJECTED_JARGON.items()
            if pattern.search(text)
        )
    scans["rejected_visitor_jargon"] = jargon_hits
    if jargon_hits:
        errors.append(f"rejected_visitor_jargon: {jargon_hits}")

    command_html = (ROOT / "commands.html").read_text(encoding="utf-8").casefold()
    for term in ("time records", "pleadings and discovery", "lodestar command library"):
        if term in command_html:
            errors.append(f"commands.html contains removed scope: {term}")

    wrong_booking = []
    booking_count = 0
    for path in html_files:
        hrefs = re.findall(r"href=['\"]([^'\"]+)['\"]", path.read_text(encoding="utf-8"), re.I)
        for href in hrefs:
            if "tidycal.com" in href:
                booking_count += 1
                if href != BOOKING:
                    wrong_booking.append({"file": path.name, "href": href})
    if wrong_booking:
        errors.append(f"wrong booking URLs: {wrong_booking}")

    canonical_results = {}
    for route in CANONICAL:
        text = (ROOT / route).read_text(encoding="utf-8")
        expected = canonical_url(route)
        ok = f"rel='canonical' href='{expected}'" in text and "noindex" not in text.casefold()
        canonical_results[route] = {"expected": expected, "ok": ok}
        if not ok:
            errors.append(f"canonical page metadata incorrect: {route}")

    redirect_results = {}
    for source, target in REDIRECTS.items():
        text = (ROOT / source).read_text(encoding="utf-8")
        expected = canonical_url(target)
        ok = (
            f"rel='canonical' href='{expected}'" in text
            and f"content='0; url={target}'" in text
            and "noindex,follow" in text
        )
        redirect_results[source] = {"target": target, "canonical": expected, "ok": ok}
        if not ok:
            errors.append(f"redirect metadata incorrect: {source}")

    missing_existing = [route for route in EXISTING_PUBLIC if not (ROOT / route).is_file()]
    if len(EXISTING_PUBLIC) != 16 or missing_existing:
        errors.append(f"existing URL preservation failed: count={len(EXISTING_PUBLIC)} missing={missing_existing}")

    required = ["CNAME", "google29ad838b30fb55e1.html", "sitemap.xml", "robots.txt", "build_site.py", "assets/img/merit-crest.svg"]
    missing_required = [name for name in required if not (ROOT / name).is_file()]
    if missing_required:
        errors.append(f"required files missing: {missing_required}")

    if (ROOT / "favicon.ico").exists():
        errors.append("obsolete favicon.ico remains")

    video_result: dict[str, object] = {"path": str(VIDEO.relative_to(ROOT)), "poster": str(POSTER.relative_to(ROOT))}
    if not VIDEO.is_file() or not POSTER.is_file():
        errors.append("homepage concept video or poster is missing")
    else:
        import hashlib
        digest = hashlib.sha256(VIDEO.read_bytes()).hexdigest()
        probe = json.loads(subprocess.check_output([
            "ffprobe", "-v", "error", "-show_entries",
            "format=duration:stream=codec_name,width,height", "-of", "json", str(VIDEO)
        ], text=True))
        streams = probe.get("streams", [])
        visual = next((stream for stream in streams if stream.get("width") and stream.get("height")), {})
        duration = float(probe.get("format", {}).get("duration", 0))
        video_result.update({"sha256": digest, "duration": duration, "width": visual.get("width"), "height": visual.get("height"), "streams": streams})
        if digest != VIDEO_SHA256 or visual.get("width") != 1920 or visual.get("height") != 1080 or abs(duration - 99.8) > .05:
            errors.append(f"video identity or metadata mismatch: {video_result}")

    home = (ROOT / "index.html").read_text(encoding="utf-8")
    required_home_phrases = [
        "Concept preview",
        "This concept film depicts illustrative workflows pending current Lodestar verification",
        "illustrative workflows pending current Lodestar verification",
        "Every draft requires attorney review",
        "Nothing is sent, filed, served, or calendared automatically",
    ]
    missing_home_phrases = [phrase for phrase in required_home_phrases if phrase not in home]
    if missing_home_phrases:
        errors.append(f"homepage concept status incomplete: {missing_home_phrases}")
    if "<video controls playsinline preload='metadata'" not in home or " autoplay" in home.casefold():
        errors.append("homepage video controls, inline playback, preload, or autoplay boundary is incorrect")
    visitor_html = "\n".join(path.read_text(encoding="utf-8") for path in html_files)
    humanization_hits = [token for token in ("—", " --- ", " -- ") if token in visitor_html]
    if humanization_hits:
        errors.append(f"visitor-facing humanization scan: {humanization_hits}")

    logo_results = {}
    for route in CANONICAL:
        text = (ROOT / route).read_text(encoding="utf-8")
        result = {
            "favicon": "<link rel='icon' href='assets/img/merit-crest.svg' type='image/svg+xml'>" in text,
            "header": "class='brand-crest'" in text,
            "footer": "class='footer-crest'" in text,
        }
        logo_results[route] = result
        if not all(result.values()):
            errors.append(f"crest placement incomplete: {route}: {result}")

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    sitemap_urls = re.findall(r"<loc>(.*?)</loc>", sitemap)
    expected_sitemap = [canonical_url(route) for route in CANONICAL]
    if sitemap_urls != expected_sitemap:
        errors.append("sitemap does not exactly match canonical routes")

    return {
        "errors": errors,
        "forbidden_scans": scans,
        "booking_links": booking_count,
        "wrong_booking_links": wrong_booking,
        "canonical_routes": canonical_results,
        "redirects": redirect_results,
        "existing_public_url_count": len(EXISTING_PUBLIC),
        "missing_existing_urls": missing_existing,
        "missing_required_files": missing_required,
        "video": video_result,
        "homepage_status_missing": missing_home_phrases,
        "humanization_hits": humanization_hits,
        "logo_placements": logo_results,
        "sitemap_urls": sitemap_urls,
    }


async def browser_checks():
    results = {}
    errors = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
        for route in CANONICAL:
            route_result = {}
            for width in VIEWPORTS:
                context = await browser.new_context(viewport={"width": width, "height": 900})
                page = await context.new_page()
                await page.emulate_media(reduced_motion="reduce")
                console_errors = []
                request_failures = []
                page.on("console", lambda msg, bucket=console_errors: bucket.append(msg.text) if msg.type == "error" else None)
                page.on("requestfailed", lambda req, bucket=request_failures: bucket.append(f"{req.url}: {req.failure}"))
                response = await page.goto(BASE + ("/" if route == "index.html" else f"/{route}"), wait_until="networkidle")
                await page.evaluate("document.querySelectorAll('[data-reveal]').forEach(e=>e.classList.add('is-in'))")
                metrics = await page.evaluate("""() => ({
                    documentOverflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
                    bodyOverflow: document.body.scrollWidth - document.body.clientWidth,
                    clipped: [...document.querySelectorAll('main *')].filter(e => {
                      const s=getComputedStyle(e), r=e.getBoundingClientRect();
                      return !e.closest('video') && e.children.length===0 && e.textContent.trim() && (r.width===0 || r.height===0 || e.scrollWidth>e.clientWidth+1 || e.scrollHeight>e.clientHeight+1) && !['visible','clip'].includes(s.overflow);
                    }).length,
                    logoCount: document.querySelectorAll("img[src='assets/img/merit-crest.svg']").length,
                    logoProblems: [...document.querySelectorAll("img[src='assets/img/merit-crest.svg']")].filter(e => {
                      const r=e.getBoundingClientRect();
                      return !e.complete || e.naturalWidth !== 260 || e.naturalHeight !== 254 || r.width <= 0 || r.height <= 0 || Math.abs((r.width/r.height)-(260/254)) > .03 || r.left < 0 || r.right > innerWidth;
                    }).length,
                    headerOverflow: (() => { const e=document.querySelector('.site-header'); return e.scrollWidth-e.clientWidth; })(),
                    menuUsable: (() => { const e=document.querySelector('.menu-toggle'), r=e.getBoundingClientRect(); return getComputedStyle(e).display === 'none' || (r.width >= 44 && r.height >= 44 && r.right <= innerWidth); })(),
                    video: (() => { const e=document.querySelector('video'); if (!e) return null; const r=e.getBoundingClientRect(); return {controls:e.controls,autoplay:e.autoplay,playsInline:e.playsInline,preload:e.preload,poster:e.getAttribute('poster'),source:e.querySelector('source')?.getAttribute('src'),readyState:e.readyState,duration:e.duration,width:r.width,height:r.height}; })()
                })""")
                meaningful_failures = [failure for failure in request_failures if not ("merit-ai-solutions-concept-preview-v9-public.mp4" in failure and "ERR_ABORTED" in failure)]
                item = {
                    "status": response.status if response else None,
                    "console_errors": console_errors,
                    "request_failures": meaningful_failures,
                    **metrics,
                }
                route_result[str(width)] = item
                if item["status"] != 200 or console_errors or meaningful_failures or metrics["documentOverflow"] > 0 or metrics["bodyOverflow"] > 0 or metrics["clipped"] > 0 or metrics["logoCount"] != 2 or metrics["logoProblems"] > 0 or metrics["headerOverflow"] > 0 or not metrics["menuUsable"]:
                    errors.append({"route": route, "width": width, **item})
                if route == "index.html":
                    video = metrics["video"] or {}
                    if not video.get("controls") or video.get("autoplay") or not video.get("playsInline") or video.get("preload") != "metadata" or video.get("readyState", 0) < 1 or abs(video.get("duration", 0) - 99.8) > .05 or video.get("width", 0) <= 0 or video.get("height", 0) <= 0:
                        errors.append({"route": route, "width": width, "video_error": video})
                    if width in (1440, 390) and os.environ.get("CAPTURE_SCREENSHOTS") == "1":
                        shot = ROOT / "screenshots" / f"homepage-{width}.png"
                        shot.parent.mkdir(exist_ok=True)
                        await page.screenshot(path=str(shot), full_page=True)
                    if width == 1440:
                        playback = await page.evaluate("""async () => {
                          const e=document.querySelector('video');
                          e.muted=true; e.currentTime=0;
                          await e.play();
                          await new Promise(resolve => setTimeout(resolve, 500));
                          const result={paused:e.paused,currentTime:e.currentTime,readyState:e.readyState};
                          e.pause();
                          return result;
                        }""")
                        item["playback"] = playback
                        if playback["paused"] or playback["currentTime"] <= 0.3 or playback["readyState"] < 2:
                            errors.append({"route": route, "width": width, "video_playback_error": playback})
                await context.close()
            results[route] = route_result

        # Check all local links and resources from canonical pages.
        broken = []
        for route in CANONICAL:
            context = await browser.new_context(viewport={"width": 1024, "height": 900})
            page = await context.new_page()
            await page.goto(BASE + ("/" if route == "index.html" else f"/{route}"), wait_until="networkidle")
            refs = await page.locator("a[href],link[href],script[src],img[src]").evaluate_all(
                "els => els.map(e => e.getAttribute('href') || e.getAttribute('src'))"
            )
            for ref in refs:
                if not ref or ref.startswith(("mailto:", "tel:", "http://", "https://", "#")):
                    continue
                target = (ROOT / ref.split("#", 1)[0]).resolve()
                if not str(target).startswith(str(ROOT)) or not target.is_file():
                    broken.append({"route": route, "ref": ref})
            await context.close()
        await browser.close()
    if broken:
        errors.append({"broken_local_refs": broken})
    return {"errors": errors, "routes": results, "broken_local_refs": broken}


async def main():
    static = static_checks()
    browser = await browser_checks()
    result = {
        "status": "PASS" if not static["errors"] and not browser["errors"] else "BLOCK",
        "static": static,
        "browser": browser,
    }
    output = json.dumps(result, indent=2)
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(output + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "static_errors": len(static["errors"]),
        "browser_errors": len(browser["errors"]),
        "canonical_routes": len(CANONICAL),
        "viewports": VIEWPORTS,
        "existing_public_urls": len(EXISTING_PUBLIC),
        "redirects": len(REDIRECTS),
    }, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    asyncio.run(main())
