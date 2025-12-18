# Universal Website Scraper (MVP)

A full-stack MVP that scrapes **static and JavaScript-rendered websites**, performs
basic interactions (scrolling), and returns **structured, section-aware JSON**.
Includes a clean web UI to trigger scrapes and view results in real time.

---

## 🚀 Tech Stack

- **Python 3.10+**
- **FastAPI** – backend API
- **httpx + BeautifulSoup** – static HTML scraping
- **Playwright** – JavaScript rendering fallback
- **Jinja2** – frontend templating
- **Uvicorn** – ASGI server

---

## 🛠️ Setup & Run (Windows)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/universal-website-scraper.git
cd universal-website-scraper
