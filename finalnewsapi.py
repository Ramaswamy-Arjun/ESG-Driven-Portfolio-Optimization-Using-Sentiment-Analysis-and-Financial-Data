import requests
import pandas as pd
from datetime import datetime, timedelta
from tqdm import tqdm 

api_key = "93c42bca53a14305811495b6353fae77"

query = "sustainability OR ESG OR climate change"
end_date = datetime.now()
start_date = end_date - timedelta(days=30) 

all_articles = []

print("📊 Starting data collection...")
for _ in tqdm(range(10), desc="Fetching NewsAPI Data"):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&from={start_date.strftime('%Y-%m-%d')}&to={end_date.strftime('%Y-%m-%d')}&pageSize=100&apiKey={api_key}"
    response = requests.get(url)
    news_data = response.json()
    
    articles = news_data.get('articles', [])
    all_articles.extend(articles)
    
    end_date -= timedelta(days=3)

df_newsapi = pd.DataFrame(all_articles)

df_newsapi.drop_duplicates(subset=['title', 'content'], inplace=True)

file_path = r"C:\Users\arjun\OneDrive\Documents\ESG\newsapi_maximum.xlsx"
df_newsapi.to_excel(file_path, index=False, engine="openpyxl")

print(f"\n✅ Data collection completed!")
print(f"Total articles collected before cleaning: {len(all_articles)}")
print(f"Total unique articles saved: {len(df_newsapi)}")
print(f"Data saved to: {file_path}")
