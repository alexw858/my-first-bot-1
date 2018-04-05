
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import time
import json
from config import consumer_key, consumer_secret, access_token, access_token_secret


# In[2]:


# Twitter API Keys
consumer_key = "5uxqcITPMH9boFAFM1R8PgpQa"
consumer_secret = "zJ235Uzde59tPNf4yQKa534BrZVX0i5uocb7gMTk2ie6BYkNFp"
access_token = "979169794699046913-ueoRRT7H6JplKK2aJWXT78NvKRlqdB8"
access_token_secret = "TyqqadYqYosiW8JfvkHclgqkhvD7F4I89iDb0b6NneMch"


# In[3]:


# Target Term
target_term = "@SouthwestAir"


# In[4]:


# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[5]:


# Search for all tweets
public_tweets = api.search(target_term, count=5, result_type="recent")


# In[6]:


# Loop through all public_tweets
for tweet in public_tweets["statuses"]:

    # Get ID and Author of most recent tweet directed to me
    tweet_id = tweet["id"]
    tweet_author = tweet["user"]["screen_name"]
    tweet_text = tweet["text"]

    # Print Tweet Text and Tweet Author
    print(tweet_text)
    print(tweet_author)

