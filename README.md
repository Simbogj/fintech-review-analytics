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

-
rocessed/           # Sentiment and thematic analysis results
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
pip installry to collect reviews from Google Play Store
- Targeted 400+ reviews per bank (1,200+ total) for CBE, BOA, and Dashen Bank
- Collected fields: `review`, `rating`, `date`, `bank`, `source`
- Applied comprehensive preprocessing:
  - Removed duplicate reviews
  - Dropped rows missing `review` or `rating`
  - Normalized dates to `YYYY-MM-DD` format
  - Cleaned review text (whitespace trimming, line break removal, formatting standardization)
  - Converted 
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
--

## Task 2: Sentiment and Thematic Analysis

### Objective
Quantify review sentiment and identify recurring themes to uncover satisfaction drivers and pain points for each bank.

### Methodology
- **Sentiment Analysis**: Appliedis**: Extracted significant keywords and n-grams using TF-IDF and spaCy
- **Theme Mapping**: Grouped related keywords into business-relevant themes:
  - `Stability`: crash, freeze, bug, error, slow, stuck, failed
  - `Account`: login, otp, password, account, verify, sign
  - `UX`: ui, interface, clean, easy, navigation, design
  - `Features`: transfer, payment, bill, card, wallet, money

### Analysis Files
- `notebooks/sentiment_thematic_analysis.ipynb`: Comprehensive analysis notebook
- `data/processed/sentiment_themes.csv`: Processed thematic analysis results

### Key Performance Indicators
- Sentiment scores assigned to 90%+ of reviews
- 3+ distinct themes per bank, each supported by keyword examples
- Modular, reusable pipeline code with documented logic

---

## Task 3: PostgreSQL Database Implementation

### Objective
Design and implement a relational database schema in PostgreSQL to persistently store the cleaned and processed review data.

### Methodoleview data (`review_id`, `bank_id`, `review_text`, `rating`, `review_date`, `sentiment_label`, `sentiment_score`, `identified_theme`, `source`)
- **Data Insertion**: Used Python (psycopg2) to insert cleaned review data
- **Verification**: Executed SQL queries to verify data integrity

### Implementation Files
- `scripts/schema.sql`: Complete database schema definition
- `scripts/insert_review.py`: Database connection, schema creation, and data insertion script

### Key Performance Indicators
- Working database connection and insert script
- Tables populated with >1,000 review entries
- SQL schema file committed to GitHub
- Verification queries executed and results documented

---

## Task 4: Insights and Recommendations

### Objective
Synthesize the sentiment and t- `scripts/insert_review.py`: Database connection, schema creation, and data insertion script

### SQL Schema
```sql
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
```

### Data insertion
```sql
INSERT INTO banks (bank_name, app_name)
VALUES
('Bank of Abyssinia', 'BoA Mobile'),
('Dashen Bank', 'Dashen Super App'),
('Commercial Bank of Ethiopia', 'CBE Mobile');
```

---

 frequency per bank (horizontal bar chart)
  - Sentiment trend over time (proportion of positive reviews)
- **Business Scenarios Addressed**:
  - **Scenario 1: Retaining Users**: Analyzed systemic issues across apps (slow loading during transfers)
  - **Scenario 2: Enhancing Features**: Extracted desired features (fingerprint login, faster transfers, budgeting tools)
  - **Scenario 3: Managing Complaints**: Clustered and tracked recurring complaints ("login error", "OTP not received")

### Implementation Files
- `scripts/generate_insights.py`: Insights generation script that creates visualizations in `reports/figures/`
- `data/processed/sentiment_themes.csv`: Final processed insights data

### Key Performance Indicators
- Clear, evidence-backed insights for product managers
- Visualizations that communicate findings rather than raw data
- Concrete, actionable recommendations for each bank

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/Simbogj/fintech-review-analytics.git
cd fintech-review-analytics
```

## Create Virtual Environment

```bash
pyinstall -r requirements.txt
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