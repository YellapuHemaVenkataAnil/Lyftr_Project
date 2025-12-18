
# Design Notes

## Static vs JS Fallback
- Strategy: Try static HTML first using httpx + BeautifulSoup.
- If extracted sections are empty or contain very little text, fall back to Playwright JS rendering.

## Wait Strategy for JS
- Network idle wait on page load
- Scroll down the page 3 times with short delays

## Click & Scroll Strategy
- Implemented infinite scroll via mouse wheel
- Scroll depth: 3
- No tab clicking implemented in this MVP

## Section Grouping & Labels
- Grouped content using semantic tags: section, main, article, nav, footer
- Section label:
  - First heading (h1–h3) if present
  - Otherwise, first 5–7 words of section text
- Fallback section created from <body> if no semantic sections exist

## Noise Filtering & Truncation
- Raw HTML truncated to 1000 characters
- Obvious empty or very small sections ignored
