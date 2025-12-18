# Universal Website Scraper (MVP)

This project is a full-stack MVP that scrapes websites (static and JS-rendered),
performs basic interactions (scroll), and returns structured, section-aware JSON.
A minimal frontend is provided to view and download the scraped data.

---

## Tech Stack
- Python 3.10+
- FastAPI
- httpx + BeautifulSoup (static scraping)
- Playwright (JS rendering fallback)
- Jinja2 (frontend)
- Uvicorn (server)

---

## How to Run (Windows)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
python -m uvicorn app.main:app --port 8000
