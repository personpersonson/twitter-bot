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

while True:
    try:
        client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        auth = tweepy.OAuthHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)

        while True:
            # get time at start of loop
            now = datetime.datetime.now()

            tweetNum = 0
            
            for tweet in tweepy.Cursor(api.search_tweets, q=('#indiegamedev OR #madewithunity OR #unity3d OR #godot OR #trailertuesday OR #wishlistwednesday OR #indiegame OR #gamedev OR #indiedev -filter:retweets'), lang='en').items(5):
                try:
                    tweetNum += 1
                    print('\nTweet by: @' + tweet.user.screen_name)
                    print('Tweet link: https://twitter.com/' + tweet.user.screen_name + '/status/' + str(tweet.id))

                    tweet.retweet()
                    client.like(tweet.id)
                    print('---- SUCCESS!')

                except tweepy.errors.TweepyException as e:
                    # if tweet is already retweeted/liked, print this.
                    tweetNum -= 1
                    print("FAILED - TWEET ALREADY RETWEETED AND LIKED")
                    print(e)

                except StopIteration:
                    break

            print ('\n-----    Retweeted and Liked ' + str(tweetNum) +  ' Tweets at ' + str(now.time())[:-7] + '     -----')

            time.sleep(120)

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

    time.sleep(300)













