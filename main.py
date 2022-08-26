import tweepy
import time
import datetime


api_key = "XXXX"
api_secret = "XXXX"
bearer_token = r"XXXX"
access_token = "XXXX"
access_token_secret = "XXXX"

# replace the "XXXX" with your own keys, tokens, and secrets!

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
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


