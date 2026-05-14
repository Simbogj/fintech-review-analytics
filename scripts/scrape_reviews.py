from google_play_scraper import reviews_all
import pandas as pd


apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank, app_id in apps.items():

    print(f"Scraping {bank} reviews...")

    result = reviews_all(
        app_id,
        sleep_milliseconds=0,
        lang='en',
        country='et'
    )

    for review in result:
        all_reviews.append({
            "review": review["content"],
            "rating": review["score"],
            "date": review["at"],
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)

print(df.head())
print(df.shape)

df.to_csv("data/raw/bank_reviews_raw.csv", index=False)

print("Scraping completed.")