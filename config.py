import os
from dotenv import load_dotenv

load_dotenv()

FLASK_APP_SECRET_KEY = os.getenv("FLASK_APP_SECRET_KEY")
CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]
NUM_TWEETS_TO_GRAB = os.getenv("NUM_TWEETS_TO_GRAB")
MAX_WORDS_RESPONSE = os.getenv("MAX_WORDS_RESPONSE")
