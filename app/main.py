import sys
import asyncio

# ✅ REQUIRED for Playwright on Windows
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from app.scraper import scrape_website

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/healthz")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/scrape")
async def scrape(data: dict):
    url = data.get("url")

    if not url or not url.startswith("http"):
        return JSONResponse(
            status_code=400,
            content={
                "result": {
                    "url": url,
                    "scrapedAt": "",
                    "meta": {
                        "title": "",
                        "description": "",
                        "language": "en",
                        "canonical": None
                    },
                    "sections": [],
                    "interactions": {
                        "clicks": [],
                        "scrolls": 0,
                        "pages": []
                    },
                    "errors": [
                        {"message": "Invalid URL", "phase": "input"}
                    ]
                }
            }
        )

    result = await scrape_website(url)
    return {"result": result}
