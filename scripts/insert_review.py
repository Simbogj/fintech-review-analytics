
# ============================================================
# Database Engineering (PostgreSQL Integration)
# ============================================================


# Import required libraries
import psycopg2
import pandas as pd
import numpy as np

# Database Connection Configuration
DB_CONFIG = {
    "host": "localhost",
    "database": "bank_reviews",
    "user": "postgres",
    "password": "123456",
    "port": 5432
}


# Connect to PostgreSQL Database
try:
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    print("Connected to PostgreSQL successfully")

    # Create Database Schema
    schema_query = """
    -- Banks table
    CREATE TABLE IF NOT EXISTS banks (
        bank_id SERIAL PRIMARY KEY,
        bank_name VARCHAR(100) NOT NULL,
        app_name VARCHAR(150) NOT NULL
    );

    -- Reviews table
    CREATE TABLE IF NOT EXISTS reviews (
        review_id SERIAL PRIMARY KEY,
        bank_id INTEGER REFERENCES banks(bank_id) ON DELETE CASCADE,
        review_text TEXT NOT NULL,
        rating INTEGER CHECK (rating BETWEEN 1 AND 5),
        review_date DATE,
        sentiment_label VARCHAR(20),
        sentiment_score FLOAT,
        identified_theme VARCHAR(100),
        source VARCHAR(50) DEFAULT 'Google Play'
    );
    """

    cur.execute(schema_query)
    conn.commit()

    print("Tables created successfully")

    # Load Cleaned Dataset
    df = pd.read_csv("fintech-review-analytics/notebooks/final_reviews.csv")

    print("\nDataset Loaded Successfully")
    print(df.head())

   
    # Prepare Data for Database Insertion
    df_db = df.copy()

    df_db = df_db.rename(columns={
        "transformer_sentiment_label": "sentiment_label",
        "transformer_sentiment_score": "sentiment_score"
    })

   
    # Insert Banks into banks Table
    df_banks = df_db[['bank']].drop_duplicates()

    bank_id_map = {}

    for bank in df_banks['bank']:

        app_name = f"{bank} Mobile App"

        cur.execute("""
            INSERT INTO banks (bank_name, app_name)
            VALUES (%s, %s)
            RETURNING bank_id;
        """, (bank, app_name))

        bank_id = cur.fetchone()[0]

        bank_id_map[bank] = bank_id

    conn.commit()

    print("\nBanks inserted successfully")
    print(bank_id_map)

   
    # Insert Reviews into reviews Table
    insert_query = """
    INSERT INTO reviews (
        bank_id,
        review_text,
        rating,
        review_date,
        sentiment_label,
        sentiment_score,
        identified_theme,
        source
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    for _, row in df_db.iterrows():

        cur.execute(insert_query, (
            bank_id_map[row['bank']],
            row['review'],
            int(row['rating']),
            row['date'],
            row.get('sentiment_label'),
            float(row['sentiment_score'])
            if pd.notna(row.get('sentiment_score'))
            else None,
            row.get('identified_theme'),
            "Google Play"
        ))

    conn.commit()

    print("\nReviews inserted successfully")

   
    # Verify Total Number of Reviews
    cur.execute("SELECT COUNT(*) FROM reviews;")

    total_reviews = cur.fetchone()[0]

    print(f"\nTotal Reviews Inserted: {total_reviews}")

   
    # Review Count Per Bank
    print("\nReview Count Per Bank")

    cur.execute("""
    SELECT b.bank_name, COUNT(r.review_id)
    FROM reviews r
    JOIN banks b
    ON r.bank_id = b.bank_id
    GROUP BY b.bank_name;
    """)

    bank_reviews = cur.fetchall()

    for row in bank_reviews:
        print(row)

   
    # Average Rating Per Bank
    print("\nAverage Rating Per Bank")

    cur.execute("""
    SELECT b.bank_name, ROUND(AVG(r.rating), 2)
    FROM reviews r
    JOIN banks b
    ON r.bank_id = b.bank_id
    GROUP BY b.bank_name;
    """)

    avg_ratings = cur.fetchall()

    for row in avg_ratings:
        print(row)


    # Check for NULL Values
    print("\nChecking for NULL Values")
    cur.execute("""
    SELECT
        COUNT(*) FILTER (WHERE review_text IS NULL),
        COUNT(*) FILTER (WHERE rating IS NULL),
        COUNT(*) FILTER (WHERE review_date IS NULL)
    FROM reviews;
    """)

    null_check = cur.fetchall()

    print(null_check)


    # Retrieve Sample Reviews
    print("\nSample Reviews")

    sample_reviews = pd.read_sql_query("""
    SELECT
        r.review_text,
        r.rating,
        b.bank_name
    FROM reviews r
    JOIN banks b
    ON r.bank_id = b.bank_id
    LIMIT 10;
    """, conn)

    print(sample_reviews)

except Exception as e:
    print("Error:", e)

finally:

   
    # Close Database Connection
    if 'cur' in locals():
        cur.close()

    if 'conn' in locals():
        conn.close()

    print("\nDatabase connection closed")
