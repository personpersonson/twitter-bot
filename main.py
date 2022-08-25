import tweepy
import time

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
    for tweet in tweepy.Cursor(api.search_tweets, q=('#indiegamedev OR #indiegame OR #gamedev OR indiedev -filter:retweets'), lang='en').items(10):
        try:
            # Add \n escape character to print() to organize tweets
            print('\nTweet by: @' + tweet.user.screen_name)
            print('\nTweet link: https://twitter.com/' + tweet.user.screen_name + '/status/' + str(tweet.id))

            # Retweet tweets as they are found
            tweet.retweet()
            print('Retweeted the tweet')

        except tweepy.errors.TweepyException as e:
            print(e)

        except StopIteration:
            break


    time.sleep(60)


