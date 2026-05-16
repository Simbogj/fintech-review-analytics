# Fintech Review Analytics

## Customer Experience Analytics for Ethiopian Banking Apps

This project analyzes customer experience and user satisfaction for Ethiopian fintech mobile banking applications using Google Play Store reviews from:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The project focuses on:

- Web scraping and review collection
- Data preprocessing and cleaning
- Exploratory data analysis (EDA)
- Sentiment analysis
- Thematic analysis

---

# Project Structure

```plaintext
fintech-review-analytics/
│
├── .github/                 # GitHub workflows and configurations
├── data/
│   ├── raw/                 # Raw, Processed and cleaned review datasets
│
├── notebooks/               # Jupyter notebooks for scraping and analysis
│   ├── scraping_cbe.ipynb
│   ├── scraping_boa.ipynb
│   ├── scraping_dashen.ipynb
│
├── scripts/                 # Python scripts for automation
├── src/                     # Source code modules
├── tests/                   # Unit and integration tests
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/Simbogj/fintech-review-analytics.git
cd fintech-review-analytics
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Scraping Methodology

## Source and Tools

Customer reviews were collected from the Google Play Store using the Python library `google-play-scraper`.

## Data Fields Collected

The following fields were extracted for each review:

- `review` → User review text
- `rating` → Star rating (1–5)
- `date` → Review date
- `bank` → Bank/app identifier
- `source` → Review platform (`Google Play`)

---

# Data Collection Details

## Sampling Strategy

- Up to **400 of the most recent reviews** were collected for each banking application.
- Scraping was performed using:
  - `lang='en'`
  - `country='et'`

---

# Date Ranges Used

The cleaned datasets stored in `data/raw/` contain reviews collected within the following ranges:

| Bank | Date Range |
|------|-------------|
| BOA | 2025-06-15 → 2026-05-15 |
| CBE | 2026-03-21 → 2026-05-15 |
| Dashen | 2025-09-29 → 2026-05-14 |

---

# Data Preprocessing

The following preprocessing steps were applied before analysis:

- Removed rows with missing critical fields:
  - `review`
  - `rating`
- Removed duplicate reviews using `review_id`
- Removed empty review texts
- Normalized dates to `YYYY-MM-DD`
- Cleaned review text:
  - Trimmed whitespace
  - Removed unnecessary line breaks
  - Standardized formatting
- Converted ratings into integer values between 1 and 5

---

# Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- TextBlob
- VADER Sentiment
- Google Play Scraper

---

# Running the Project

## Run Scraping Notebooks

- `scraping_cbe.ipynb`
- `scraping_boa.ipynb`
- `scraping_dashen.ipynb`

---

# Limitations

## Sampling Bias

The scraper retrieves a fixed number of the most recent reviews (`count=400`). Therefore, the dataset may not fully represent all historical customer feedback.

## Platform Dependency

The scraping process depends on Google Play Store availability and API behavior. Changes in the platform structure or rate limits may affect data collection.

## Language and Regional Constraints

Only reviews available under:

- English language (`lang='en'`)
- Ethiopia region (`country='et'`)

were included in the dataset.

## Review Quality

Some reviews may contain:

- Very short text
- Ambiguous feedback
- Non-informative comments (e.g., “Good”, “Nice app”)

Additional filtering or NLP preprocessing may be required for advanced analysis.

## Uneven Time Windows

The collected review periods differ across banks. For example, CBE reviews cover a shorter and more recent time range than BOA and Dashen reviews. Time-based comparisons should account for these differences.

---

# Future Improvements

Planned next steps include:

- Sentiment classification
- Topic modeling
- Customer pain-point detection
- Comparative fintech analytics
- Interactive dashboards and visualizations
- Deployment of automated data pipelines

---

# Author

Simbo Getachew 