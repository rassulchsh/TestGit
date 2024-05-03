import requests
from dotenv import load_dotenv
import os

def fetch_tweets(query):
    url = "https://twitter-api45.p.rapidapi.com/tweet.php"

    querystring = {"id": "1671370010743263233"}

    headers = {
        "X-RapidAPI-Key": os.getenv('RAPIDAPI_KEY'),
        "X-RapidAPI-Host": os.getenv('RAPIDAPI_HOST')
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        tweets_data = response.json()
        tweets_text = ""
        for tweet in tweets_data['data']:
            tweets_text += tweet['text'] + "\n"  # 'text' key is used here instead of 'full_text'
        return tweets_text
    else:
        return "Failed to fetch tweets"

# Example: Fetch tweets related to Elon Musk
tweets_data_str = fetch_tweets("@elonmusk")

print(tweets_data_str)

