import httpx
from datetime import datetime
from playwright.async_api import async_playwright

from app.parser import parse_html


HEADERS = {
    # ✅ REQUIRED for Wikipedia & many sites
    "User-Agent": "Mozilla/5.0 (compatible; LyftrAssignmentBot/1.0)"
}


async def scrape_website(url: str):
    errors = []
    pages = [url]
    clicks = []
    scrolls = 0

    html = ""

    # -------------------------
    # 1️⃣ STATIC SCRAPING FIRST
    # -------------------------
    try:
        async with httpx.AsyncClient(headers=HEADERS, timeout=15) as client:
            resp = await client.get(url)
            html = resp.text
    except Exception as e:
        errors.append({"message": str(e), "phase": "fetch"})

    sections, meta = parse_html(html, url)

    # -------------------------
    # 2️⃣ JS FALLBACK (Playwright)
    # -------------------------
    if not sections or len(sections[0]["content"]["text"]) < 100:
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                await page.goto(url, wait_until="networkidle")

                # Scroll 3 times
                for _ in range(3):
                    await page.mouse.wheel(0, 3000)
                    await page.wait_for_timeout(1200)
                    scrolls += 1

                html = await page.content()
                await browser.close()

            sections, meta = parse_html(html, url)
            clicks.append("scroll")

        except Exception as e:
            errors.append({"message": str(e), "phase": "render"})

    # -------------------------
    # FINAL RESULT (REQUIRED SHAPE)
    # -------------------------
    return {
        "url": url,
        "scrapedAt": datetime.utcnow().isoformat() + "Z",
        "meta": meta,
        "sections": sections,
        "interactions": {
            "clicks": clicks,
            "scrolls": scrolls,
            "pages": pages
        },
        "errors": errors
    }
