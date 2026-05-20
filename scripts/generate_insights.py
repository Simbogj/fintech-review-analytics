import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings

warnings.filterwarnings('ignore')

def generate_insights():
    print("Loading datasets...")
    # Load the datasets
    df_results = pd.read_csv('notebooks/fintech_sentiment_analysis_results.csv')
    df_final = pd.read_csv('notebooks/final_reviews.csv')
    
    # Merge datasets to get dates if needed, or just use df_results for the main plots
    # Note: final_reviews.csv has the date column, df_results has the theme and sentiment
    df_merged = pd.merge(df_results, df_final[['review', 'date', 'bank']], on=['review', 'bank'], how='left').drop_duplicates(subset=['review', 'bank'])
    
    # Ensure date is datetime
    df_merged['date'] = pd.to_datetime(df_merged['date'], errors='coerce')
    df_merged['month_year'] = df_merged['date'].dt.to_period('M')

    os.makedirs('reports/figures', exist_ok=True)
    
    sns.set_theme(style='whitegrid')
    
    # 1. Sentiment distribution by bank (stacked bar chart)
    print("Generating Sentiment Distribution...")
    plt.figure(figsize=(10, 6))
    sentiment_dist = df_merged.groupby(['bank', 'sentiment']).size().unstack().fillna(0)
    sentiment_dist.plot(kind='bar', stacked=True, colormap='viridis', figsize=(10,6))
    plt.title('Sentiment Distribution by Bank', fontsize=16)
    plt.xlabel('Bank', fontsize=12)
    plt.ylabel('Number of Reviews', fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title='Sentiment')
    plt.tight_layout()
    plt.savefig('reports/figures/sentiment_distribution.png', dpi=300)
    plt.close()

    # 2. Rating distribution per bank (boxplot)
    print("Generating Rating Distribution...")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='bank', y='rating', data=df_merged, palette='Set2')
    plt.title('Rating Distribution per Bank', fontsize=16)
    plt.xlabel('Bank', fontsize=12)
    plt.ylabel('Rating (1-5)', fontsize=12)
    plt.tight_layout()
    plt.savefig('reports/figures/rating_distribution.png', dpi=300)
    plt.close()

    # 3. Theme frequency per bank (horizontal bar chart)
    print("Generating Theme Frequency...")
    # Filter out 'Other' theme for better insights
    df_themes = df_merged[df_merged['theme'] != 'Other']
    plt.figure(figsize=(12, 8))
    sns.countplot(y='theme', hue='bank', data=df_themes, palette='muted', order=df_themes['theme'].value_counts().index)
    plt.title('Top Theme Frequency per Bank (Excluding "Other")', fontsize=16)
    plt.xlabel('Number of Mentions', fontsize=12)
    plt.ylabel('Identified Theme', fontsize=12)
    plt.legend(title='Bank')
    plt.tight_layout()
    plt.savefig('reports/figures/theme_frequency.png', dpi=300)
    plt.close()

    # 4. Sentiment Trend Over Time (Proportion of positive reviews)
    print("Generating Sentiment Trend Over Time...")
    df_merged['is_positive'] = (df_merged['sentiment'] == 'positive').astype(int)
    trend = df_merged.groupby(['month_year', 'bank'])['is_positive'].mean().unstack()
    if len(trend) > 1:
        plt.figure(figsize=(12, 6))
        trend.plot(marker='o', figsize=(12,6), colormap='Set1', linewidth=2)
        plt.title('Positive Sentiment Trend Over Time', fontsize=16)
        plt.xlabel('Date (Month-Year)', fontsize=12)
        plt.ylabel('Proportion of Positive Reviews', fontsize=12)
        plt.legend(title='Bank')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('reports/figures/sentiment_trend.png', dpi=300)
        plt.close()
    else:
        print("Not enough date data for trend plot.")

    print("Visualizations generated successfully in reports/figures/")

if __name__ == "__main__":
    generate_insights()
