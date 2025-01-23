import requests
import pandas as pd
from datetime import datetime, timedelta

api_key = "041342dc7a7b4400b93ed5232c9ccb67"

end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

query = "sustainability OR ESG OR climate change"
articles = []

for page_num in range(1, 6):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&from={start_date}&to={end_date}&pageSize=100&page={page_num}&apiKey={api_key}"
    response = requests.get(url)
    news_data = response.json()
    
    if response.status_code != 200 or "articles" not in news_data:
        print(f"⚠️ Error fetching data: {news_data.get('message', 'Unknown Error')}")
        break
    
    articles += [
        {"title": article["title"], "content": article["content"], "publishedAt": article["publishedAt"]}
        for article in news_data["articles"]
    ]

df_news = pd.DataFrame(articles)
df_news.drop_duplicates(subset=["title", "content"], inplace=True)
df_news.to_csv(r"C:\Users\arjun\OneDrive\Documents\ESG\newsapi_esg_data_burnerse.csv", index=False)

print(f"{len(df_news)} unique news articles successfully saved!")
