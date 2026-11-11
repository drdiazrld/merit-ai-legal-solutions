#!/usr/bin/env python3
"""Verify the static GitHub Pages publication candidate."""
import asyncio
import json
import re
import sys
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
FORBIDDEN = {
    "visitor_facing_framework_token": ["hermes"],
    "removed_commands_scope": ["lodestar command library", "pleadings and discovery"],
    "roadmap_language": ["roadmap", "planned / in development", "coming soon"],
    "rejected_security_diligence_phrases": [
        "current scope and due diligence", "ask for the evidence", "security questionnaire", "unapproved channel",
    ],
    "public_failure_outcomes": [
        "what failed", "known failures", "failure results", "failed run", "criterion not met",
    ],
    "b1_completion_claim": ["b1 is complete", "b1 complete"],
}


def canonical_url(route: str) -> str:
    return DOMAIN + ("/" if route == "index.html" else f"/{route}")


def static_checks():
    errors = []
    html_files = sorted(ROOT.glob("*.html"))
    scans = {}
    for group, terms in FORBIDDEN.items():
        hits = []
        for path in html_files:
            text = path.read_text(encoding="utf-8").casefold()
            hits.extend({"file": path.name, "term": term} for term in terms if term in text)
        scans[group] = hits
        if hits:
            errors.append(f"{group}: {hits}")

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

    required = ["CNAME", "google29ad838b30fb55e1.html", "sitemap.xml", "robots.txt", "build_site.py"]
    missing_required = [name for name in required if not (ROOT / name).is_file()]
    if missing_required:
        errors.append(f"required files missing: {missing_required}")

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
                      return e.children.length===0 && e.textContent.trim() && (r.width===0 || r.height===0 || e.scrollWidth>e.clientWidth+1 || e.scrollHeight>e.clientHeight+1) && !['visible','clip'].includes(s.overflow);
                    }).length
                })""")
                item = {
                    "status": response.status if response else None,
                    "console_errors": console_errors,
                    "request_failures": request_failures,
                    **metrics,
                }
                route_result[str(width)] = item
                if item["status"] != 200 or console_errors or request_failures or metrics["documentOverflow"] > 0 or metrics["bodyOverflow"] > 0 or metrics["clipped"] > 0:
                    errors.append({"route": route, "width": width, **item})
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
