-- =========================
-- Database: bank_reviews
-- =========================

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