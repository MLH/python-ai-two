import tweepy
import re
import config
import random

# user authentication to use twitter API
def get_user_auth_twitter():
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    return auth

# fetch tweets
def get_user_tweets(twitter_handle):
    auth = get_user_auth_twitter()
    api = tweepy.API(auth)
    public_tweets = api.user_timeline(
        twitter_handle, count=(config.NUM_TWEETS_TO_GRAB or 100), tweet_mode="extended"
    )
    return public_tweets

# remove emoji, punctuation, urls from tweets
def clean_tweets_data(public_tweets):
    text = ""

    # remove emoji from tweets:
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )
    url_pattern = re.compile(r"http\S+", re.DOTALL)
    mentions_pattern = re.compile(r"@\S+", re.DOTALL)

    # return tweet
    for tweet in public_tweets:
        # workaround to get full_text from tweepy (otherwise text is truncated)
        full_text = tweet._json["full_text"]
        text_without_emoji = emoji_pattern.sub(r"", full_text)
        text_without_url = url_pattern.sub(r"", text_without_emoji)
        cleaned_text = mentions_pattern.sub(r"", text_without_url)
        text += (
            text_without_emoji + "\n\n"
        )  # Make sure each tweet is handled properly by markovify
    return text

def return_single_tweet(text):
    tweet_list = text.split('\n\n')
    random_index = random.randint(0, len(tweet_list)-1)
    return tweet_list[random_index]

# build the markov chain based on the text we read
# we use the markovify library to do this step
def generate_bot_answer(twitter_handle, user_question):
    tweets = get_user_tweets(twitter_handle)
    parsed_text = clean_tweets_data(tweets)
    
    return text_model
