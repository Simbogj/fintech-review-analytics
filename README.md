# Fintech Review Analytics

## Customer Experience Analytics for Ethiopian Banking Apps

This project is an end-to-end data analytics pipeline that extracts insights from customer reviews of Ethiopian mobile banking applications. It covers the full workflow of **data collection, preprocessing, sentiment analysis, database engineering, and insight generation**.

The goal is to transform raw user feedback into structured, actionable business intelligence using Python, NLP techniques, and PostgreSQL.

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
│   └── processed/           # Sentiment and thematic analysis results
│
├── notebooks/               # Jupyter notebooks for scraping and analysis
│   ├── scraping_cbe.ipynb
│   ├── scraping_boa.ipynb
│   ├── scraping_dashen.ipynb
│   └── sentiment_thematic_analysis.ipynb
│
├── scripts/                 # Python scripts for automation
│   ├── generate_insights.py
│   ├── insert_review.py
│   └── schema.sql
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

# The Four Main Tasks

This project is divided into four main tasks that form a complete data engineering and analytics pipeline:

## Task 1: Data Collection and Preprocessing

### Objective
Scrape reviews from the Google Play Store, preprocess them into a clean, analysis-ready dataset, and manage all code via GitHub with proper version control hygiene.

### Methodology
- Used `google-play-scraper` library to collect reviews from Google Play Store

### Data Sources

Customer reviews were collected from Google Play Store applications of:

- Bank of Abyssinia (BoA Mobile)
- Dashen Bank (Dashen Super App)
- Commercial Bank of Ethiopia (CBE Mobile)

Targeted 400+ reviews per bank (1,200+ total)

### Data Collection

Reviews were scraped programmatically using Python scripts. The dataset included: `review`, `rating`, `date`, `bank`, `source`

### Data Preprocessing Steps

- Removed duplicate records  
- Handled missing values  
- Standardized column names  
- Normalized dates to `YYYY-MM-DD` format  
- Cleaned special characters and whitespace  
- Merged datasets into a single structured file  

### Output Data Files
- `data/raw/boa_reviews_clean.csv` - 400+ BOA reviews
- `data/raw/cbe_reviews_clean.csv` - 400+ CBE reviews
- `data/raw/dashen_reviews_clean.csv` - 400+ Dashen reviews
- `data/raw/cleaned_reviews.csv` - Combined dataset of all banks

---

## Task 2: Sentiment and Thematic Analysis

### Objective
Quantify review sentiment and identify recurring themes to uncover satisfaction drivers and pain points for each bank.

### Methodology
- **Sentiment Analysis**: Applied multiple approaches:
  - VADER lexicon-based sentiment analysis
  - TextBlob polarity analysis
  - DistilBERT transformer-based sentiment classification
- **Thematic Analysis**: Extracted significant keywords and n-grams using TF-IDF and spaCy
- **Theme Mapping**: Grouped related keywords into business-relevant themes:
  - `Stability`: crash, freeze, bug, error, slow, stuck, failed
  - `Account`: login, otp, password, account, verify, sign
  - `UX`: ui, interface, clean, easy, navigation, design
  - `Features`: transfer, payment, bill, card, wallet, money

### Analysis Files
- `notebooks/sentiment_thematic_analysis.ipynb`: Comprehensive analysis notebook
- `data/processed/sentiment_themes.csv`: Processed thematic analysis results

---

## Task 3: PostgreSQL Database Implementation

### Objective
Design and implement a relational database schema in PostgreSQL to persistently store the cleaned and processed review data.

### Methodology
- **Database Setup**: Created PostgreSQL database named `bank_reviews`
- **Schema Design**:
  - `banks` table: Stores bank metadata (`bank_id`, `bank_name`, `app_name`)
  - `reviews` table: Stores review data (`review_id`, `bank_id`, `review_text`, `rating`, `review_date`, `sentiment_label`, `sentiment_score`, `identified_theme`, `source`)
- **Data Insertion**: Used Python (psycopg2) to insert cleaned review data
- **Verification**: Executed SQL queries to verify data integrity

### Implementation Files
- `scripts/schema.sql`: Complete database schema definition
- `scripts/insert_review.py`: Database connection, schema creation, and data insertion script

### SQL Schema
-- Banks table
CREATE TABLE IF NOT EXISTS banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100) NOT NULL,
    app_name VARCHAR(150) NOT NULL
);

-- Reviews table
CREATE TABLE IF NOT EXISTS reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INTEGER NOT NULL REFERENCES banks(bank_id) ON DELETE CASCADE,
    review_text TEXT NOT NULL,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    review_date DATE,
    sentiment_label VARCHAR(20),
    sentiment_score FLOAT,
    identified_theme VARCHAR(100),
    source VARCHAR(50) DEFAULT 'Google Play'
);

-- Index for faster analysis
CREATE INDEX IF NOT EXISTS idx_reviews_bank_id ON reviews(bank_id);
CREATE INDEX IF NOT EXISTS idx_reviews_rating ON reviews(rating);
CREATE INDEX IF NOT EXISTS idx_reviews_date ON reviews(review_date);

### Data insertion

INSERT INTO banks (bank_name, app_name)
VALUES
('Bank of Abyssinia', 'BoA Mobile'),
('Dashen Bank', 'Dashen Super App'),
('Commercial Bank of Ethiopia', 'CBE Mobile');

---

## Task 4: Insights and Recommendations

### Objective
Synthesize the sentiment and thematic analysis into business-actionable insights, supported by clear visualizations and concrete product recommendations.

### Methodology
- **Insights Generation**: Created comprehensive visualizations including:
  - Sentiment distribution by bank (stacked bar chart)
  - Rating distribution per bank (boxplot)
  - Theme frequency per bank (horizontal bar chart)
  - Sentiment trend over time (proportion of positive reviews)
- **Business Scenarios Addressed**:
  - **Scenario 1: Retaining Users**: Analyzed systemic issues across apps (slow loading during transfers)
  - **Scenario 2: Enhancing Features**: Extracted desired features (fingerprint login, faster transfers, budgeting tools)
  - **Scenario 3: Managing Complaints**: Clustered and tracked recurring complaints ("login error", "OTP not received")

### Implementation Files
- `scripts/generate_insights.py`: Insights generation script that creates visualizations in `reports/figures/`
- `data/processed/sentiment_themes.csv`: Final processed insights data

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

# Running the Project

## Data Collection

1. Run the scraping notebooks:
   - `notebooks/scraping_cbe.ipynb`
   - `notebooks/scraping_boa.ipynb`
   - `notebooks/scraping_dashen.ipynb`
2. Verify data is saved in `data/raw/`

## Sentiment and Thematic Analysis

1. Run `notebooks/sentiment_thematic_analysis.ipynb`
2. Results are saved as `fintech_sentiment_analysis_results.csv`

## Database Integration

1. Ensure PostgreSQL is running with database `bank_reviews`
2. Run `scripts/insert_review.py` to populate the database

## Generate Insights

1. Run `scripts/generate_insights.py` to create visualizations
2. Reports are generated in `reports/figures/`

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
- spaCy
- scikit-learn
- transformers
- torch
- psycopg2
- SQLAlchemy
- WordCloud

---

# Business Impact

This analytics pipeline provides Omega Consultancy with a competitive intelligence asset that transforms raw Play Store reviews into actionable insights for Ethiopian banks. The final deliverable gives product managers a clear, evidence-backed picture of what their users love, what frustrates them most, and what to prioritize next.

---

# Author

Simbo Getachew 