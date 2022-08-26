import tweepy
import time
import datetime
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth = tweepy.OAuthHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

while True:
    # get time at start of loop
    now = datetime.datetime.now()
    
    for tweet in tweepy.Cursor(api.search_tweets, q=('#indiegamedev OR #indiegame OR #gamedev OR indiedev -filter:retweets'), lang='en').items(6):
        try:
            # Add \n escape character to print() to organize tweets
            print('\nTweet by: @' + tweet.user.screen_name)
            print('Tweet link: https://twitter.com/' + tweet.user.screen_name + '/status/' + str(tweet.id))

            # Retweet and like tweets as they are found
            tweet.retweet()
            client.like(tweet.id)
            print('---- SUCCESS!')

        except tweepy.errors.TweepyException as e:
            # if tweet is already retweeted/liked, print this.
            print("FAILED - TWEET ALREADY RETWEETED AND LIKED")

        except StopIteration:
            break

    # print time at end of loop
    print ('\n-----     at  ' + str(now.time()) + '     -----')

    # wait for 2 minutes
    time.sleep(120)


