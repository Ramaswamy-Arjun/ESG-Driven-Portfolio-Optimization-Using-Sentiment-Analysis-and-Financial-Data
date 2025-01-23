import tweepy
import pandas as pd
import os
import time

api_key = os.getenv("TWITTER_API_KEY", "Oc68nj6ve2HempkeGwlcTwu5K")
api_secret = os.getenv("TWITTER_API_SECRET", "DrI9mRziuh55ZkCqJyTT2OVgqK1BJj3N1HDBLjsFtPBlneumOu")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN", "AAAAAAAAAAAAAAAAAAAAAEkkyAEAAAAAvZ0wLhbAMouZ74TDZonOsjWJCZU%3DyYaf8fvnXD8Z9iuiIkBZCUh4SM9VxTg993plOsyKlLlmR2vR6D")

client = tweepy.Client(bearer_token=bearer_token)

search_query = "sustainability OR ESG OR climate change -is:retweet lang:en"

twitter_data = []

next_token = None
total_tweets_fetched = 0
max_tweets = 300 

while total_tweets_fetched < max_tweets:
    try:
        tweets = client.search_recent_tweets(
            query=search_query,
            max_results=100,
            tweet_fields=["created_at", "public_metrics"],
            user_fields=["username"],
            next_token=next_token 
        )
        
        if not tweets.data:
            print("No more tweets available.")
            break
        
        for tweet in tweets.data:
            tweet_datetime_naive = tweet.created_at.replace(tzinfo=None)
            twitter_data.append({
                "text": tweet.text,
                "source": "twitter",
                "created_at": tweet_datetime_naive,
                "retweet_count": tweet.public_metrics.get('retweet_count', 0),
                "like_count": tweet.public_metrics.get('like_count', 0)
            })

        total_tweets_fetched += len(tweets.data)
        next_token = tweets.meta.get('next_token')  
        
        
        if not next_token:
            print("End of results reached.")
            break

    except tweepy.TweepyException as e:
        print(f"Error fetching tweets: {e}")
        if "429" in str(e):
            print("Waiting for 15 minutes due to rate limiting...")
            time.sleep(15 * 60)  
        else:
            break  


if twitter_data:
    df_twitter = pd.DataFrame(twitter_data)
    df_twitter.drop_duplicates(subset="text", inplace=True)

    
    try:
        df_twitter.to_excel(r"C:\Users\arjun\OneDrive\Documents\ESG\twitterdata2.xlsx", index=False, engine="openpyxl")
        print(f"{len(df_twitter)} tweets successfully saved to twitterdata.xlsx")
    except Exception as e:
        print(f"Error saving data to Excel: {e}")
else:
    print("No data available to save.")
