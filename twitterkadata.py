import tweepy
import pandas as pd
import time

bearer_token = "AAAAAAAAAAAAAAAAAAAAAO06yAEAAAAA9T2DWirdcaASwmaumW6LbvFlBBs%3DuH5LOODLD1l90aW6YNfeBzSQBNyZ0cpy72aoBodpfaPUr9y8oz"

client = tweepy.Client(bearer_token=bearer_token)

query = "sustainability OR ESG OR climate change -is:retweet lang:en"
custom_file_path = r"C:\Users\arjun\OneDrive\Documents\ESG\twitter_esg_data.csv"

def fetch_tweets():
    tweets_data = []
    try:
        for page in tweepy.Paginator(
            client.search_recent_tweets,
            query=query,
            max_results=100,
            tweet_fields=["created_at"]
        ).flatten(limit=500):
            tweets_data.append({"text": page.text, "created_at": page.created_at})
        
        df_twitter = pd.DataFrame(tweets_data)
        df_twitter.to_csv(custom_file_path, mode='a', index=False, header=False)
        print(f"{len(df_twitter)} tweets added successfully!")

    except tweepy.TooManyRequests:
        print("⚠️ Rate Limit Reached! Waiting for 15 minutes...")
        time.sleep(900) 
        fetch_tweets()  

fetch_tweets()
