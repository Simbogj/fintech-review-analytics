# Fintech Review Analytics

## Customer Experience Analytics for Ethiopian Banking Apps

This project objective is to analyze customer experience for Ethiopian fintech applications by collecting and analyzing Google Play Store reviews from:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The project focuses on:
- Web scraping
- Data preprocessing
- Sentiment analysis
- Thematic analysis
- PostgreSQL database engineering
- Business insight generation

---

# Project Structure

```plaintext
fintech-review-analytics/
├── .github/
├── data/
├── notebooks/
├── scripts/
├── src/
├── tests/
├── requirements.txt
└── README.md


**Scraping Methodology**
- **Source & Tooling:** Reviews were collected from Google Play using the `google-play-scraper` Python library.
- **Fields Collected:** `review` (text), `rating` (1–5 stars), `date` (UTC, normalized to `YYYY-MM-DD`), `bank` (app identifier), and `source` (`Google Play`).
- **Sampling:** For each app, up to 400 of the newest available reviews were requested in a single run.

**Date Range Used**
- The cleaned datasets in `data/raw/` cover the following ranges based on the collected reviews:
	- BOA: 2025-06-15 → 2026-05-15
	- CBE: 2026-03-21 → 2026-05-15
	- Dashen: 2025-09-29 → 2026-05-14

**Preprocessing Steps**
- Drop rows missing critical fields (`review`, `rating`).
- Deduplicate by `review_id` and remove empty reviews.
- Normalize `date` to `YYYY-MM-DD` using pandas datetime parsing.
- Clean review text by collapsing whitespace and trimming edges.
- Enforce rating integer values in the 1–5 range.

**Limitations & Notes**
- **Sampling bias:** The pipeline requests a fixed number (`count=400`) of the newest reviews. This is a convenience sample and may not represent the full historical distribution of reviews for each app.
- **Rate limits & availability:** Scraping depends on the Google Play Store endpoints and may be subject to rate-limiting or temporary changes in the page/API format.
- **Language & region:** Scrapes used `lang='en'` and `country='et'`; reviews in other languages or regions may be excluded.
- **Text quality:** Short, ambiguous, or non-informative reviews (e.g., "Good") remain in the cleaned CSVs; downstream analyses should consider filtering by text length or applying additional heuristics.
- **Temporal window differences:** CBE's collected reviews span a shorter, more recent window than BOA and Dashen—comparisons that rely on time trends should account for this difference.

**Next Steps**
- Run sentiment analysis and topic modeling on the cleaned CSVs in `data/raw/` to extract actionable insights and compare banks.
