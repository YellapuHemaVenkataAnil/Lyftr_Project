from bs4 import BeautifulSoup
from urllib.parse import urljoin


def parse_html(html: str, base_url: str):
    soup = BeautifulSoup(html, "lxml")

    # -------------------------
    # META (SAFE DEFAULTS)
    # -------------------------
    title = soup.title.text.strip() if soup.title else ""

    description = ""
    desc = soup.find("meta", attrs={"name": "description"})
    if desc and desc.get("content"):
        description = desc["content"].strip()

    language = "en"
    if soup.html and soup.html.get("lang"):
        language = soup.html.get("lang")

    canonical_tag = soup.find("link", rel="canonical")
    canonical = canonical_tag["href"] if canonical_tag and canonical_tag.get("href") else None

    meta = {
        "title": title,
        "description": description,
        "language": language,
        "canonical": canonical
    }

    sections = []

    # -------------------------
    # PRIMARY SECTIONS
    # -------------------------
    tags = soup.find_all(["section", "main", "article", "nav", "footer"])

    for i, tag in enumerate(tags):
        text = tag.get_text(" ", strip=True)
        if len(text) < 40:
            continue

        headings = [h.get_text(strip=True) for h in tag.find_all(["h1", "h2", "h3"])]

        label = headings[0] if headings else " ".join(text.split()[:6])

        if tag.name == "nav":
            section_type = "nav"
        elif tag.name == "footer":
            section_type = "footer"
        else:
            section_type = "section"

        sections.append({
            "id": f"{section_type}-{i}",
            "type": section_type,
            "label": label,
            "sourceUrl": base_url,
            "content": {
                "headings": headings,
                "text": text,
                "links": [
                    {
                        "text": a.get_text(strip=True),
                        "href": urljoin(base_url, a.get("href"))
                    }
                    for a in tag.find_all("a", href=True)
                ],
                "images": [
                    {
                        "src": urljoin(base_url, img.get("src")),
                        "alt": img.get("alt", "")
                    }
                    for img in tag.find_all("img", src=True)
                ],
                "lists": [
                    [li.get_text(strip=True) for li in ul.find_all("li")]
                    for ul in tag.find_all(["ul", "ol"])
                ],
                "tables": []
            },
            "rawHtml": str(tag)[:1000],
            "truncated": len(str(tag)) > 1000
        })

    # -------------------------
    # FALLBACK (MANDATORY)
    # -------------------------
    if not sections and soup.body:
        body = soup.body
        text = body.get_text(" ", strip=True)

        sections.append({
            "id": "fallback-0",
            "type": "section",
            "label": "Main Content",
            "sourceUrl": base_url,
            "content": {
                "headings": [h.get_text(strip=True) for h in body.find_all(["h1", "h2", "h3"])],
                "text": text,
                "links": [
                    {
                        "text": a.get_text(strip=True),
                        "href": urljoin(base_url, a.get("href"))
                    }
                    for a in body.find_all("a", href=True)
                ],
                "images": [],
                "lists": [],
                "tables": []
            },
            "rawHtml": str(body)[:1000],
            "truncated": len(str(body)) > 1000
        })

    return sections, meta
