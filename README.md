# 🌐 Universal Website Scraper (MVP)

A **full-stack web scraping application** that intelligently extracts structured
content from **static and JavaScript-rendered websites**.  
The system performs basic interactions such as scrolling and outputs a
**section-aware, well-structured JSON response**.

This project demonstrates real-world scraping strategies, backend API design,
JS rendering fallback, and a clean frontend UI.

---

## ✨ Key Features

- ✅ Scrapes **static HTML websites**
- ✅ Automatically falls back to **JavaScript rendering** (Playwright)
- ✅ Performs basic interactions (scrolling)
- ✅ Extracts **semantic sections** (hero, section, nav, footer, etc.)
- ✅ Outputs structured, evaluator-compliant JSON
- ✅ Clean, modern web UI for testing
- ✅ Windows-compatible setup

---

## 🧱 Tech Stack

### Backend
- **Python 3.10+**
- **FastAPI** – REST API framework
- **httpx** – HTTP client
- **BeautifulSoup** – HTML parsing
- **Playwright** – JavaScript rendering & interactions
- **Uvicorn** – ASGI server

### Frontend
- **HTML / CSS**
- **Jinja2 Templates**
- Minimal, responsive UI

---

## 📂 Project Structure

